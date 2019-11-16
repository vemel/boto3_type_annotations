"Main interface for waf type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    "ClientCreateByteMatchSetResponseTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientCreateGeoMatchSetResponseTypeDef",
    "ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientCreateIpSetResponseIPSetTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientCreateRateBasedRuleResponseRuleTypeDef",
    "ClientCreateRateBasedRuleResponseTypeDef",
    "ClientCreateRateBasedRuleTagsTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientCreateRegexMatchSetResponseTypeDef",
    "ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientCreateRegexPatternSetResponseTypeDef",
    "ClientCreateRuleGroupResponseRuleGroupTypeDef",
    "ClientCreateRuleGroupResponseTypeDef",
    "ClientCreateRuleGroupTagsTypeDef",
    "ClientCreateRuleResponseRulePredicatesTypeDef",
    "ClientCreateRuleResponseRuleTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateRuleTagsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientCreateSizeConstraintSetResponseTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseTypeDef",
    "ClientCreateWebAclDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesTypeDef",
    "ClientCreateWebAclResponseWebACLTypeDef",
    "ClientCreateWebAclResponseTypeDef",
    "ClientCreateWebAclTagsTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    "ClientCreateXssMatchSetResponseTypeDef",
    "ClientDeleteByteMatchSetResponseTypeDef",
    "ClientDeleteGeoMatchSetResponseTypeDef",
    "ClientDeleteIpSetResponseTypeDef",
    "ClientDeleteRateBasedRuleResponseTypeDef",
    "ClientDeleteRegexMatchSetResponseTypeDef",
    "ClientDeleteRegexPatternSetResponseTypeDef",
    "ClientDeleteRuleGroupResponseTypeDef",
    "ClientDeleteRuleResponseTypeDef",
    "ClientDeleteSizeConstraintSetResponseTypeDef",
    "ClientDeleteSqlInjectionMatchSetResponseTypeDef",
    "ClientDeleteWebAclResponseTypeDef",
    "ClientDeleteXssMatchSetResponseTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    "ClientGetByteMatchSetResponseTypeDef",
    "ClientGetChangeTokenResponseTypeDef",
    "ClientGetChangeTokenStatusResponseTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientGetGeoMatchSetResponseTypeDef",
    "ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientGetIpSetResponseIPSetTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetLoggingConfigurationResponseTypeDef",
    "ClientGetPermissionPolicyResponseTypeDef",
    "ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    "ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientGetRateBasedRuleResponseRuleTypeDef",
    "ClientGetRateBasedRuleResponseTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientGetRegexMatchSetResponseTypeDef",
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientGetRegexPatternSetResponseTypeDef",
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    "ClientGetRuleGroupResponseTypeDef",
    "ClientGetRuleResponseRulePredicatesTypeDef",
    "ClientGetRuleResponseRuleTypeDef",
    "ClientGetRuleResponseTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    "ClientGetSampledRequestsResponseTimeWindowTypeDef",
    "ClientGetSampledRequestsResponseTypeDef",
    "ClientGetSampledRequestsTimeWindowTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientGetSizeConstraintSetResponseTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientGetSqlInjectionMatchSetResponseTypeDef",
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    "ClientGetWebAclResponseWebACLTypeDef",
    "ClientGetWebAclResponseTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    "ClientGetXssMatchSetResponseTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseTypeDef",
    "ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    "ClientListByteMatchSetsResponseTypeDef",
    "ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    "ClientListGeoMatchSetsResponseTypeDef",
    "ClientListIpSetsResponseIPSetsTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    "ClientListLoggingConfigurationsResponseTypeDef",
    "ClientListRateBasedRulesResponseRulesTypeDef",
    "ClientListRateBasedRulesResponseTypeDef",
    "ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    "ClientListRegexMatchSetsResponseTypeDef",
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    "ClientListRegexPatternSetsResponseTypeDef",
    "ClientListRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListRuleGroupsResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    "ClientListSizeConstraintSetsResponseTypeDef",
    "ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    "ClientListSqlInjectionMatchSetsResponseTypeDef",
    "ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListSubscribedRuleGroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebAclsResponseWebACLsTypeDef",
    "ClientListWebAclsResponseTypeDef",
    "ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    "ClientListXssMatchSetsResponseTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateByteMatchSetResponseTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    "ClientUpdateByteMatchSetUpdatesTypeDef",
    "ClientUpdateGeoMatchSetResponseTypeDef",
    "ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    "ClientUpdateGeoMatchSetUpdatesTypeDef",
    "ClientUpdateIpSetResponseTypeDef",
    "ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef",
    "ClientUpdateIpSetUpdatesTypeDef",
    "ClientUpdateRateBasedRuleResponseTypeDef",
    "ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    "ClientUpdateRateBasedRuleUpdatesTypeDef",
    "ClientUpdateRegexMatchSetResponseTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    "ClientUpdateRegexMatchSetUpdatesTypeDef",
    "ClientUpdateRegexPatternSetResponseTypeDef",
    "ClientUpdateRegexPatternSetUpdatesTypeDef",
    "ClientUpdateRuleGroupResponseTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    "ClientUpdateRuleGroupUpdatesTypeDef",
    "ClientUpdateRuleResponseTypeDef",
    "ClientUpdateRuleUpdatesPredicateTypeDef",
    "ClientUpdateRuleUpdatesTypeDef",
    "ClientUpdateSizeConstraintSetResponseTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesTypeDef",
    "ClientUpdateSqlInjectionMatchSetResponseTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    "ClientUpdateWebAclDefaultActionTypeDef",
    "ClientUpdateWebAclResponseTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    "ClientUpdateWebAclUpdatesTypeDef",
    "ClientUpdateXssMatchSetResponseTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    "ClientUpdateXssMatchSetUpdatesTypeDef",
    "GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef",
    "GetRateBasedRuleManagedKeysPaginateResponseTypeDef",
    "ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef",
    "ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef",
    "ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef",
    "ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef",
    "ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef",
    "ListActivatedRulesInRuleGroupPaginateResponseTypeDef",
    "ListByteMatchSetsPaginatePaginationConfigTypeDef",
    "ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef",
    "ListByteMatchSetsPaginateResponseTypeDef",
    "ListGeoMatchSetsPaginatePaginationConfigTypeDef",
    "ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef",
    "ListGeoMatchSetsPaginateResponseTypeDef",
    "ListIPSetsPaginatePaginationConfigTypeDef",
    "ListIPSetsPaginateResponseIPSetsTypeDef",
    "ListIPSetsPaginateResponseTypeDef",
    "ListLoggingConfigurationsPaginatePaginationConfigTypeDef",
    "ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef",
    "ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef",
    "ListLoggingConfigurationsPaginateResponseTypeDef",
    "ListRateBasedRulesPaginatePaginationConfigTypeDef",
    "ListRateBasedRulesPaginateResponseRulesTypeDef",
    "ListRateBasedRulesPaginateResponseTypeDef",
    "ListRegexMatchSetsPaginatePaginationConfigTypeDef",
    "ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef",
    "ListRegexMatchSetsPaginateResponseTypeDef",
    "ListRegexPatternSetsPaginatePaginationConfigTypeDef",
    "ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef",
    "ListRegexPatternSetsPaginateResponseTypeDef",
    "ListRuleGroupsPaginatePaginationConfigTypeDef",
    "ListRuleGroupsPaginateResponseRuleGroupsTypeDef",
    "ListRuleGroupsPaginateResponseTypeDef",
    "ListRulesPaginatePaginationConfigTypeDef",
    "ListRulesPaginateResponseRulesTypeDef",
    "ListRulesPaginateResponseTypeDef",
    "ListSizeConstraintSetsPaginatePaginationConfigTypeDef",
    "ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef",
    "ListSizeConstraintSetsPaginateResponseTypeDef",
    "ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef",
    "ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef",
    "ListSqlInjectionMatchSetsPaginateResponseTypeDef",
    "ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef",
    "ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef",
    "ListSubscribedRuleGroupsPaginateResponseTypeDef",
    "ListWebACLsPaginatePaginationConfigTypeDef",
    "ListWebACLsPaginateResponseWebACLsTypeDef",
    "ListWebACLsPaginateResponseTypeDef",
    "ListXssMatchSetsPaginatePaginationConfigTypeDef",
    "ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef",
    "ListXssMatchSetsPaginateResponseTypeDef",
)


_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuples` `FieldToMatch`

    The part of a web request that you want AWS WAF to search, such as a specified header
    or a query string. For more information, see  FieldToMatch .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": str,
        "PositionalConstraint": str,
    },
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
):
    """
    Type definition for `ClientCreateByteMatchSetResponseByteMatchSet` `ByteMatchTuples`

    The bytes (typically a string that corresponds with ASCII characters) that you want AWS
    WAF to search for in web requests, the location in requests that you want AWS WAF to
    search, and other settings.

    - **FieldToMatch** *(dict) --*

      The part of a web request that you want AWS WAF to search, such as a specified header
      or a query string. For more information, see  FieldToMatch .

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TargetString** *(bytes) --*

      The value that you want AWS WAF to search for. AWS WAF searches for the specified
      string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
      length of the value is 50 bytes.

      Valid values depend on the values that you specified for ``FieldToMatch`` :

      * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
      you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
      ``Referer`` header.

      * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
      request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
      ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
      which is the part of a URL that appears after a ``?`` character.

      * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
      identifies a resource, for example, ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes
      of the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
      as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
      single parameter, AWS WAF inspects all parameters within the query string for the value
      or regex pattern that you specify in ``TargetString`` .

      If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
      case sensitive.

       **If you're using the AWS WAF API**

      Specify a base64-encoded version of the value. The maximum length of the value before
      you base64-encode it is 50 bytes.

      For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
      ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
      ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
      resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

       **If you're using the AWS CLI or one of the AWS SDKs**

      The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
      value.

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``TargetString`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **PositionalConstraint** *(string) --*

      Within the portion of a web request that you want to search (for example, in the query
      string, if any), specify where you want AWS WAF to search. Valid values include the
      following:

       **CONTAINS**

      The specified part of the web request must include the value of ``TargetString`` , but
      the location doesn't matter.

       **CONTAINS_WORD**

      The specified part of the web request must include the value of ``TargetString`` , and
      ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
      0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
      following:

      * ``TargetString`` exactly matches the value of the specified part of the web request,
      such as the value of a header.

      * ``TargetString`` is at the beginning of the specified part of the web request and is
      followed by a character other than an alphanumeric character or underscore (_), for
      example, ``BadBot;`` .

      * ``TargetString`` is at the end of the specified part of the web request and is
      preceded by a character other than an alphanumeric character or underscore (_), for
      example, ``;BadBot`` .

      * ``TargetString`` is in the middle of the specified part of the web request and is
      preceded and followed by characters other than alphanumeric characters or underscore
      (_), for example, ``-BadBot;`` .

       **EXACTLY**

      The value of the specified part of the web request must exactly match the value of
      ``TargetString`` .

       **STARTS_WITH**

      The value of ``TargetString`` must appear at the beginning of the specified part of the
      web request.

       **ENDS_WITH**

      The value of ``TargetString`` must appear at the end of the specified part of the web
      request.
    """


_ClientCreateByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[
            ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetTypeDef
):
    """
    Type definition for `ClientCreateByteMatchSetResponse` `ByteMatchSet`

    A  ByteMatchSet that contains no ``ByteMatchTuple`` objects.

    - **ByteMatchSetId** *(string) --*

      The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
      information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
      (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
      DeleteByteMatchSet ).

       ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
      create a ``ByteMatchSet`` .

    - **ByteMatchTuples** *(list) --*

      Specifies the bytes (typically a string that corresponds with ASCII characters) that you
      want AWS WAF to search for in web requests, the location in requests that you want AWS WAF
      to search, and other settings.

      - *(dict) --*

        The bytes (typically a string that corresponds with ASCII characters) that you want AWS
        WAF to search for in web requests, the location in requests that you want AWS WAF to
        search, and other settings.

        - **FieldToMatch** *(dict) --*

          The part of a web request that you want AWS WAF to search, such as a specified header
          or a query string. For more information, see  FieldToMatch .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TargetString** *(bytes) --*

          The value that you want AWS WAF to search for. AWS WAF searches for the specified
          string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
          length of the value is 50 bytes.

          Valid values depend on the values that you specified for ``FieldToMatch`` :

          * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
          you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
          ``Referer`` header.

          * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
          request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
          ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
          which is the part of a URL that appears after a ``?`` character.

          * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
          identifies a resource, for example, ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes
          of the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
          as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
          single parameter, AWS WAF inspects all parameters within the query string for the value
          or regex pattern that you specify in ``TargetString`` .

          If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
          case sensitive.

           **If you're using the AWS WAF API**

          Specify a base64-encoded version of the value. The maximum length of the value before
          you base64-encode it is 50 bytes.

          For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
          ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
          ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
          resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

           **If you're using the AWS CLI or one of the AWS SDKs**

          The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
          value.

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``TargetString`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

        - **PositionalConstraint** *(string) --*

          Within the portion of a web request that you want to search (for example, in the query
          string, if any), specify where you want AWS WAF to search. Valid values include the
          following:

           **CONTAINS**

          The specified part of the web request must include the value of ``TargetString`` , but
          the location doesn't matter.

           **CONTAINS_WORD**

          The specified part of the web request must include the value of ``TargetString`` , and
          ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
          0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
          following:

          * ``TargetString`` exactly matches the value of the specified part of the web request,
          such as the value of a header.

          * ``TargetString`` is at the beginning of the specified part of the web request and is
          followed by a character other than an alphanumeric character or underscore (_), for
          example, ``BadBot;`` .

          * ``TargetString`` is at the end of the specified part of the web request and is
          preceded by a character other than an alphanumeric character or underscore (_), for
          example, ``;BadBot`` .

          * ``TargetString`` is in the middle of the specified part of the web request and is
          preceded and followed by characters other than alphanumeric characters or underscore
          (_), for example, ``-BadBot;`` .

           **EXACTLY**

          The value of the specified part of the web request must exactly match the value of
          ``TargetString`` .

           **STARTS_WITH**

          The value of ``TargetString`` must appear at the beginning of the specified part of the
          web request.

           **ENDS_WITH**

          The value of ``TargetString`` must appear at the end of the specified part of the web
          request.
    """


_ClientCreateByteMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": ClientCreateByteMatchSetResponseByteMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateByteMatchSetResponseTypeDef(_ClientCreateByteMatchSetResponseTypeDef):
    """
    Type definition for `ClientCreateByteMatchSet` `Response`

    - **ByteMatchSet** *(dict) --*

      A  ByteMatchSet that contains no ``ByteMatchTuple`` objects.

      - **ByteMatchSetId** *(string) --*

        The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
        information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
        (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
        DeleteByteMatchSet ).

         ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
        create a ``ByteMatchSet`` .

      - **ByteMatchTuples** *(list) --*

        Specifies the bytes (typically a string that corresponds with ASCII characters) that you
        want AWS WAF to search for in web requests, the location in requests that you want AWS WAF
        to search, and other settings.

        - *(dict) --*

          The bytes (typically a string that corresponds with ASCII characters) that you want AWS
          WAF to search for in web requests, the location in requests that you want AWS WAF to
          search, and other settings.

          - **FieldToMatch** *(dict) --*

            The part of a web request that you want AWS WAF to search, such as a specified header
            or a query string. For more information, see  FieldToMatch .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TargetString** *(bytes) --*

            The value that you want AWS WAF to search for. AWS WAF searches for the specified
            string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
            length of the value is 50 bytes.

            Valid values depend on the values that you specified for ``FieldToMatch`` :

            * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
            you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
            ``Referer`` header.

            * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
            request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
            ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

            * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
            which is the part of a URL that appears after a ``?`` character.

            * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
            identifies a resource, for example, ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The request
            body immediately follows the request headers. Note that only the first ``8192`` bytes
            of the request body are forwarded to AWS WAF for inspection. To allow or block requests
            based on the length of the body, you can create a size constraint set. For more
            information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
            as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
            characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
            single parameter, AWS WAF inspects all parameters within the query string for the value
            or regex pattern that you specify in ``TargetString`` .

            If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
            case sensitive.

             **If you're using the AWS WAF API**

            Specify a base64-encoded version of the value. The maximum length of the value before
            you base64-encode it is 50 bytes.

            For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
            ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
            ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
            resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

             **If you're using the AWS CLI or one of the AWS SDKs**

            The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
            value.

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``TargetString`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

          - **PositionalConstraint** *(string) --*

            Within the portion of a web request that you want to search (for example, in the query
            string, if any), specify where you want AWS WAF to search. Valid values include the
            following:

             **CONTAINS**

            The specified part of the web request must include the value of ``TargetString`` , but
            the location doesn't matter.

             **CONTAINS_WORD**

            The specified part of the web request must include the value of ``TargetString`` , and
            ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
            0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
            following:

            * ``TargetString`` exactly matches the value of the specified part of the web request,
            such as the value of a header.

            * ``TargetString`` is at the beginning of the specified part of the web request and is
            followed by a character other than an alphanumeric character or underscore (_), for
            example, ``BadBot;`` .

            * ``TargetString`` is at the end of the specified part of the web request and is
            preceded by a character other than an alphanumeric character or underscore (_), for
            example, ``;BadBot`` .

            * ``TargetString`` is in the middle of the specified part of the web request and is
            preceded and followed by characters other than alphanumeric characters or underscore
            (_), for example, ``-BadBot;`` .

             **EXACTLY**

            The value of the specified part of the web request must exactly match the value of
            ``TargetString`` .

             **STARTS_WITH**

            The value of ``TargetString`` must appear at the beginning of the specified part of the
            web request.

             **ENDS_WITH**

            The value of ``TargetString`` must appear at the end of the specified part of the web
            request.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateByteMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef(
    _ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
):
    """
    Type definition for `ClientCreateGeoMatchSetResponseGeoMatchSet` `GeoMatchConstraints`

    The country from which web requests originate that you want AWS WAF to search for.

    - **Type** *(string) --*

      The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
      the only valid value.

    - **Value** *(string) --*

      The country that you want AWS WAF to search for.
    """


_ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef(
    _ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef
):
    """
    Type definition for `ClientCreateGeoMatchSetResponse` `GeoMatchSet`

    The  GeoMatchSet returned in the ``CreateGeoMatchSet`` response. The ``GeoMatchSet`` contains
    no ``GeoMatchConstraints`` .

    - **GeoMatchSetId** *(string) --*

      The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
      about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
      UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
      (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

       ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  GeoMatchSet . You can't change the name of an
      ``GeoMatchSet`` after you create it.

    - **GeoMatchConstraints** *(list) --*

      An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to
      search for.

      - *(dict) --*

        The country from which web requests originate that you want AWS WAF to search for.

        - **Type** *(string) --*

          The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
          the only valid value.

        - **Value** *(string) --*

          The country that you want AWS WAF to search for.
    """


_ClientCreateGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateGeoMatchSetResponseTypeDef(_ClientCreateGeoMatchSetResponseTypeDef):
    """
    Type definition for `ClientCreateGeoMatchSet` `Response`

    - **GeoMatchSet** *(dict) --*

      The  GeoMatchSet returned in the ``CreateGeoMatchSet`` response. The ``GeoMatchSet`` contains
      no ``GeoMatchConstraints`` .

      - **GeoMatchSetId** *(string) --*

        The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
        about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
        UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

         ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  GeoMatchSet . You can't change the name of an
        ``GeoMatchSet`` after you create it.

      - **GeoMatchConstraints** *(list) --*

        An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to
        search for.

        - *(dict) --*

          The country from which web requests originate that you want AWS WAF to search for.

          - **Type** *(string) --*

            The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
            the only valid value.

          - **Value** *(string) --*

            The country that you want AWS WAF to search for.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateGeoMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "_ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef(
    _ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef
):
    """
    Type definition for `ClientCreateIpSetResponseIPSet` `IPSetDescriptors`

    Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
    format) that web requests originate from.

    - **Type** *(string) --*

      Specify ``IPV4`` or ``IPV6`` .

    - **Value** *(string) --*

      Specify an IPv4 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 192.0.2.44, specify ``192.0.2.44/32`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP
      addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

      For more information about CIDR notation, see the Wikipedia entry `Classless
      Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

      Specify an IPv6 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 1111:0000:0000:0000:0000:0000:0000:0111, specify
      ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP
      addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
      1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
      ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientCreateIpSetResponseIPSetTypeDef = TypedDict(
    "_ClientCreateIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)


class ClientCreateIpSetResponseIPSetTypeDef(_ClientCreateIpSetResponseIPSetTypeDef):
    """
    Type definition for `ClientCreateIpSetResponse` `IPSet`

    The  IPSet returned in the ``CreateIPSet`` response.

    - **IPSetId** *(string) --*

      The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
      ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
      into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
      from AWS WAF (see  DeleteIPSet ).

       ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

    - **Name** *(string) --*

      A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
      after you create it.

    - **IPSetDescriptors** *(list) --*

      The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation)
      that web requests originate from. If the ``WebACL`` is associated with a CloudFront
      distribution and the viewer did not use an HTTP proxy or a load balancer to send the
      request, this is the value of the c-ip field in the CloudFront access logs.

      - *(dict) --*

        Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
        format) that web requests originate from.

        - **Type** *(string) --*

          Specify ``IPV4`` or ``IPV6`` .

        - **Value** *(string) --*

          Specify an IPv4 address by using CIDR notation. For example:

          * To configure AWS WAF to allow, block, or count requests that originated from the IP
          address 192.0.2.44, specify ``192.0.2.44/32`` .

          * To configure AWS WAF to allow, block, or count requests that originated from IP
          addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

          For more information about CIDR notation, see the Wikipedia entry `Classless
          Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

          Specify an IPv6 address by using CIDR notation. For example:

          * To configure AWS WAF to allow, block, or count requests that originated from the IP
          address 1111:0000:0000:0000:0000:0000:0000:0111, specify
          ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

          * To configure AWS WAF to allow, block, or count requests that originated from IP
          addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
          1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
          ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientCreateIpSetResponseTypeDef = TypedDict(
    "_ClientCreateIpSetResponseTypeDef",
    {"IPSet": ClientCreateIpSetResponseIPSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateIpSetResponseTypeDef(_ClientCreateIpSetResponseTypeDef):
    """
    Type definition for `ClientCreateIpSet` `Response`

    - **IPSet** *(dict) --*

      The  IPSet returned in the ``CreateIPSet`` response.

      - **IPSetId** *(string) --*

        The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
        ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
        into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
        from AWS WAF (see  DeleteIPSet ).

         ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

      - **Name** *(string) --*

        A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
        after you create it.

      - **IPSetDescriptors** *(list) --*

        The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation)
        that web requests originate from. If the ``WebACL`` is associated with a CloudFront
        distribution and the viewer did not use an HTTP proxy or a load balancer to send the
        request, this is the value of the c-ip field in the CloudFront access logs.

        - *(dict) --*

          Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
          format) that web requests originate from.

          - **Type** *(string) --*

            Specify ``IPV4`` or ``IPV6`` .

          - **Value** *(string) --*

            Specify an IPv4 address by using CIDR notation. For example:

            * To configure AWS WAF to allow, block, or count requests that originated from the IP
            address 192.0.2.44, specify ``192.0.2.44/32`` .

            * To configure AWS WAF to allow, block, or count requests that originated from IP
            addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless
            Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

            Specify an IPv6 address by using CIDR notation. For example:

            * To configure AWS WAF to allow, block, or count requests that originated from the IP
            address 1111:0000:0000:0000:0000:0000:0000:0111, specify
            ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

            * To configure AWS WAF to allow, block, or count requests that originated from IP
            addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
            1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
            ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateIPSet`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
    total=False,
)


class ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef(
    _ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef
):
    """
    Type definition for `ClientCreateRateBasedRuleResponseRule` `MatchPredicates`

    Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
    RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
    ``Rule`` and, for each object, indicates whether you want to negate the settings, for
    example, requests that do NOT originate from the IP address 192.0.2.44.

    - **Negated** *(boolean) --*

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
      based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
       XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
       an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
       requests based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
      the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
      an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
      count requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --*

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --*

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientCreateRateBasedRuleResponseRuleTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[
            ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef
        ],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)


class ClientCreateRateBasedRuleResponseRuleTypeDef(
    _ClientCreateRateBasedRuleResponseRuleTypeDef
):
    """
    Type definition for `ClientCreateRateBasedRuleResponse` `Rule`

    The  RateBasedRule that is returned in the ``CreateRateBasedRule`` response.

    - **RuleId** *(string) --*

      A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
      about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
      UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
      ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
      DeleteRateBasedRule ).

    - **Name** *(string) --*

      A friendly name or description for a ``RateBasedRule`` . You can't change the name of a
      ``RateBasedRule`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for a ``RateBasedRule`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RateBasedRule`` .

    - **MatchPredicates** *(list) --*

      The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
      IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

      - *(dict) --*

        Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
        RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
        ``Rule`` and, for each object, indicates whether you want to negate the settings, for
        example, requests that do NOT originate from the IP address 192.0.2.44.

        - **Negated** *(boolean) --*

          Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
          based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
           XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
           an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
           requests based on that IP address.

          Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
          the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
          XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
          an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
          count requests based on all IP addresses *except*  ``192.0.2.44`` .

        - **Type** *(string) --*

          The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

        - **DataId** *(string) --*

          A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
          ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

    - **RateKey** *(string) --*

      The field that AWS WAF uses to determine if requests are likely arriving from single source
      and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` .
      ``IP`` indicates that requests arriving from the same IP address are subject to the
      ``RateLimit`` that is specified in the ``RateBasedRule`` .

    - **RateLimit** *(integer) --*

      The maximum number of requests, which have an identical value in the field specified by the
      ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the
      ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers
      the action that is specified for this rule.
    """


_ClientCreateRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseTypeDef",
    {"Rule": ClientCreateRateBasedRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRateBasedRuleResponseTypeDef(
    _ClientCreateRateBasedRuleResponseTypeDef
):
    """
    Type definition for `ClientCreateRateBasedRule` `Response`

    - **Rule** *(dict) --*

      The  RateBasedRule that is returned in the ``CreateRateBasedRule`` response.

      - **RuleId** *(string) --*

        A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
        about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
        UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
        ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
        DeleteRateBasedRule ).

      - **Name** *(string) --*

        A friendly name or description for a ``RateBasedRule`` . You can't change the name of a
        ``RateBasedRule`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for a ``RateBasedRule`` . The name can
        contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
        length one. It can't contain whitespace or metric names reserved for AWS WAF, including
        "All" and "Default_Action." You can't change the name of the metric after you create the
        ``RateBasedRule`` .

      - **MatchPredicates** *(list) --*

        The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
        IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

        - *(dict) --*

          Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
          RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
          ``Rule`` and, for each object, indicates whether you want to negate the settings, for
          example, requests that do NOT originate from the IP address 192.0.2.44.

          - **Negated** *(boolean) --*

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
            based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
             XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
             an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
             requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
            the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
            XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
            an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
            count requests based on all IP addresses *except*  ``192.0.2.44`` .

          - **Type** *(string) --*

            The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

          - **DataId** *(string) --*

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
            ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

      - **RateKey** *(string) --*

        The field that AWS WAF uses to determine if requests are likely arriving from single source
        and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` .
        ``IP`` indicates that requests arriving from the same IP address are subject to the
        ``RateLimit`` that is specified in the ``RateBasedRule`` .

      - **RateLimit** *(integer) --*

        The maximum number of requests, which have an identical value in the field specified by the
        ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the
        ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers
        the action that is specified for this rule.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateRateBasedRule`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateRateBasedRuleTagsTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRateBasedRuleTagsTypeDef(_ClientCreateRateBasedRuleTagsTypeDef):
    """
    Type definition for `ClientCreateRateBasedRule` `Tags`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for the ``RegexPatternSet`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
        "RegexPatternSetId": str,
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
):
    """
    Type definition for `ClientCreateRegexMatchSetResponseRegexMatchSet` `RegexMatchTuples`

    The regular expression pattern that you want AWS WAF to search for in web requests, the
    location in requests that you want AWS WAF to search, and other settings. Each
    ``RegexMatchTuple`` object contains:

    * The part of a web request that you want AWS WAF to inspect, such as a query string or
    the value of the ``User-Agent`` header.

    * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
    For more information, see  RegexPatternSet .

    * Whether to perform any conversions on the request, such as converting it to lowercase,
    before inspecting it for the specified string.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for the ``RegexPatternSet`` .

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``RegexPatternSet`` before inspecting a request for a
      match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system commandline
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **RegexPatternSetId** *(string) --*

      The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
      get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
      ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
      ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
      and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

       ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
       ListRegexPatternSets .
    """


_ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef
):
    """
    Type definition for `ClientCreateRegexMatchSetResponse` `RegexMatchSet`

    A  RegexMatchSet that contains no ``RegexMatchTuple`` objects.

    - **RegexMatchSetId** *(string) --*

      The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
      information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
      (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
      a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
      DeleteRegexMatchSet ).

       ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you
      create a ``RegexMatchSet`` .

    - **RegexMatchTuples** *(list) --*

      Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains:

      * The part of a web request that you want AWS WAF to inspect, such as a query string or the
      value of the ``User-Agent`` header.

      * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
      For more information, see  RegexPatternSet .

      * Whether to perform any conversions on the request, such as converting it to lowercase,
      before inspecting it for the specified string.

      - *(dict) --*

        The regular expression pattern that you want AWS WAF to search for in web requests, the
        location in requests that you want AWS WAF to search, and other settings. Each
        ``RegexMatchTuple`` object contains:

        * The part of a web request that you want AWS WAF to inspect, such as a query string or
        the value of the ``User-Agent`` header.

        * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
        For more information, see  RegexPatternSet .

        * Whether to perform any conversions on the request, such as converting it to lowercase,
        before inspecting it for the specified string.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for the ``RegexPatternSet`` .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``RegexPatternSet`` before inspecting a request for a
          match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system commandline
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

        - **RegexPatternSetId** *(string) --*

          The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
          get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
          ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
          ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
          and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

           ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
           ListRegexPatternSets .
    """


_ClientCreateRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseTypeDef(
    _ClientCreateRegexMatchSetResponseTypeDef
):
    """
    Type definition for `ClientCreateRegexMatchSet` `Response`

    - **RegexMatchSet** *(dict) --*

      A  RegexMatchSet that contains no ``RegexMatchTuple`` objects.

      - **RegexMatchSetId** *(string) --*

        The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
        information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
        (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
        a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
        DeleteRegexMatchSet ).

         ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you
        create a ``RegexMatchSet`` .

      - **RegexMatchTuples** *(list) --*

        Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains:

        * The part of a web request that you want AWS WAF to inspect, such as a query string or the
        value of the ``User-Agent`` header.

        * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
        For more information, see  RegexPatternSet .

        * Whether to perform any conversions on the request, such as converting it to lowercase,
        before inspecting it for the specified string.

        - *(dict) --*

          The regular expression pattern that you want AWS WAF to search for in web requests, the
          location in requests that you want AWS WAF to search, and other settings. Each
          ``RegexMatchTuple`` object contains:

          * The part of a web request that you want AWS WAF to inspect, such as a query string or
          the value of the ``User-Agent`` header.

          * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
          For more information, see  RegexPatternSet .

          * Whether to perform any conversions on the request, such as converting it to lowercase,
          before inspecting it for the specified string.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for the ``RegexPatternSet`` .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``RegexPatternSet`` before inspecting a request for a
            match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system commandline
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

          - **RegexPatternSetId** *(string) --*

            The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
            get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
            ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
            ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
            and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

             ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
             ListRegexPatternSets .

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateRegexMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "_ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)


class ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef(
    _ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef
):
    """
    Type definition for `ClientCreateRegexPatternSetResponse` `RegexPatternSet`

    A  RegexPatternSet that contains no objects.

    - **RegexPatternSetId** *(string) --*

      The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
      information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
      ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
      WAF.

       ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
      you create a ``RegexPatternSet`` .

    - **RegexPatternStrings** *(list) --*

      Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such
      as ``B[a@]dB[o0]t`` .

      - *(string) --*
    """


_ClientCreateRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientCreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateRegexPatternSetResponseTypeDef(
    _ClientCreateRegexPatternSetResponseTypeDef
):
    """
    Type definition for `ClientCreateRegexPatternSet` `Response`

    - **RegexPatternSet** *(dict) --*

      A  RegexPatternSet that contains no objects.

      - **RegexPatternSetId** *(string) --*

        The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
        information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
        ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
        WAF.

         ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

      - **Name** *(string) --*

        A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
        you create a ``RegexPatternSet`` .

      - **RegexPatternStrings** *(list) --*

        Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such
        as ``B[a@]dB[o0]t`` .

        - *(string) --*

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateRegexPatternSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "_ClientCreateRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientCreateRuleGroupResponseRuleGroupTypeDef(
    _ClientCreateRuleGroupResponseRuleGroupTypeDef
):
    """
    Type definition for `ClientCreateRuleGroupResponse` `RuleGroup`

    An empty  RuleGroup .

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
      about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
      insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
      UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

       ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

    - **Name** *(string) --*

      The friendly name or description for the ``RuleGroup`` . You can't change the name of a
      ``RuleGroup`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``RuleGroup`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RuleGroup`` .
    """


_ClientCreateRuleGroupResponseTypeDef = TypedDict(
    "_ClientCreateRuleGroupResponseTypeDef",
    {"RuleGroup": ClientCreateRuleGroupResponseRuleGroupTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRuleGroupResponseTypeDef(_ClientCreateRuleGroupResponseTypeDef):
    """
    Type definition for `ClientCreateRuleGroup` `Response`

    - **RuleGroup** *(dict) --*

      An empty  RuleGroup .

      - **RuleGroupId** *(string) --*

        A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
        about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
        insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
        UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

         ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

      - **Name** *(string) --*

        The friendly name or description for the ``RuleGroup`` . You can't change the name of a
        ``RuleGroup`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``RuleGroup`` . The name can
        contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
        length one. It can't contain whitespace or metric names reserved for AWS WAF, including
        "All" and "Default_Action." You can't change the name of the metric after you create the
        ``RuleGroup`` .

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateRuleGroup`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateRuleGroupTagsTypeDef = TypedDict(
    "_ClientCreateRuleGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRuleGroupTagsTypeDef(_ClientCreateRuleGroupTagsTypeDef):
    """
    Type definition for `ClientCreateRuleGroup` `Tags`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientCreateRuleResponseRulePredicatesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulePredicatesTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
    total=False,
)


class ClientCreateRuleResponseRulePredicatesTypeDef(
    _ClientCreateRuleResponseRulePredicatesTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRule` `Predicates`

    Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
    RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
    ``Rule`` and, for each object, indicates whether you want to negate the settings, for
    example, requests that do NOT originate from the IP address 192.0.2.44.

    - **Negated** *(boolean) --*

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
      based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
       XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
       an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
       requests based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
      the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
      an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
      count requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --*

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --*

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientCreateRuleResponseRuleTypeDef = TypedDict(
    "_ClientCreateRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientCreateRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)


class ClientCreateRuleResponseRuleTypeDef(_ClientCreateRuleResponseRuleTypeDef):
    """
    Type definition for `ClientCreateRuleResponse` `Rule`

    The  Rule returned in the ``CreateRule`` response.

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule``
      after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``Rule`` . The name can contain
      only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
      one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
      "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .

    - **Predicates** *(list) --*

      The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
      IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

      - *(dict) --*

        Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
        RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
        ``Rule`` and, for each object, indicates whether you want to negate the settings, for
        example, requests that do NOT originate from the IP address 192.0.2.44.

        - **Negated** *(boolean) --*

          Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
          based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
           XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
           an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
           requests based on that IP address.

          Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
          the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
          XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
          an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
          count requests based on all IP addresses *except*  ``192.0.2.44`` .

        - **Type** *(string) --*

          The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

        - **DataId** *(string) --*

          A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
          ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientCreateRuleResponseTypeDef = TypedDict(
    "_ClientCreateRuleResponseTypeDef",
    {"Rule": ClientCreateRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRuleResponseTypeDef(_ClientCreateRuleResponseTypeDef):
    """
    Type definition for `ClientCreateRule` `Response`

    - **Rule** *(dict) --*

      The  Rule returned in the ``CreateRule`` response.

      - **RuleId** *(string) --*

        A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
        ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
        ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
        from AWS WAF (see  DeleteRule ).

         ``RuleId`` is returned by  CreateRule and by  ListRules .

      - **Name** *(string) --*

        The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule``
        after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``Rule`` . The name can contain
        only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
        one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
        "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .

      - **Predicates** *(list) --*

        The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
        IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

        - *(dict) --*

          Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
          RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
          ``Rule`` and, for each object, indicates whether you want to negate the settings, for
          example, requests that do NOT originate from the IP address 192.0.2.44.

          - **Negated** *(boolean) --*

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
            based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
             XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
             an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
             requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
            the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
            XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
            an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
            count requests based on all IP addresses *except*  ``192.0.2.44`` .

          - **Type** *(string) --*

            The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

          - **DataId** *(string) --*

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
            ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateRule`` request. You can also use this
      value to query the status of the request. For more information, see  GetChangeTokenStatus .
    """


_ClientCreateRuleTagsTypeDef = TypedDict(
    "_ClientCreateRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRuleTagsTypeDef(_ClientCreateRuleTagsTypeDef):
    """
    Type definition for `ClientCreateRule` `Tags`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef
):
    """
    Type definition for `ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraints` `FieldToMatch`

    Specifies where in a web request to look for the size constraint.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": str,
        "ComparisonOperator": str,
        "Size": int,
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
):
    """
    Type definition for `ClientCreateSizeConstraintSetResponseSizeConstraintSet` `SizeConstraints`

    Specifies a constraint on the size of a part of the web request. AWS WAF uses the
    ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
    form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
    expression is true, the ``SizeConstraint`` is considered to match.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for the size constraint.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

      Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
      for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
      inspection.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

    - **ComparisonOperator** *(string) --*

      The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
      with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
      "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
      expression is true, the ``SizeConstraint`` is considered to match.

       **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

       **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

       **LE** : Used to test if the ``Size`` is less than or equal to the size of the
       ``FieldToMatch``

       **LT** : Used to test if the ``Size`` is strictly less than the size of the
       ``FieldToMatch``

       **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
       ``FieldToMatch``

       **GT** : Used to test if the ``Size`` is strictly greater than the size of the
       ``FieldToMatch``

    - **Size** *(integer) --*

      The size in bytes that you want AWS WAF to compare against the size of the specified
      ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
      ``FieldToMatch`` to build an expression in the form of "``Size``
      ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
      the ``SizeConstraint`` is considered to match.

      Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

      If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
      character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef
):
    """
    Type definition for `ClientCreateSizeConstraintSetResponse` `SizeConstraintSet`

    A  SizeConstraintSet that contains no ``SizeConstraint`` objects.

    - **SizeConstraintSetId** *(string) --*

      A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
      information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
      ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
      a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
      ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

       ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
       ListSizeConstraintSets .

    - **Name** *(string) --*

      The name, if any, of the ``SizeConstraintSet`` .

    - **SizeConstraints** *(list) --*

      Specifies the parts of web requests that you want to inspect the size of.

      - *(dict) --*

        Specifies a constraint on the size of a part of the web request. AWS WAF uses the
        ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
        form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
        expression is true, the ``SizeConstraint`` is considered to match.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for the size constraint.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

          Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
          for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
          inspection.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

        - **ComparisonOperator** *(string) --*

          The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
          with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
          "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
          expression is true, the ``SizeConstraint`` is considered to match.

           **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

           **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

           **LE** : Used to test if the ``Size`` is less than or equal to the size of the
           ``FieldToMatch``

           **LT** : Used to test if the ``Size`` is strictly less than the size of the
           ``FieldToMatch``

           **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
           ``FieldToMatch``

           **GT** : Used to test if the ``Size`` is strictly greater than the size of the
           ``FieldToMatch``

        - **Size** *(integer) --*

          The size in bytes that you want AWS WAF to compare against the size of the specified
          ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
          ``FieldToMatch`` to build an expression in the form of "``Size``
          ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
          the ``SizeConstraint`` is considered to match.

          Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

          If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
          character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientCreateSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseTypeDef(
    _ClientCreateSizeConstraintSetResponseTypeDef
):
    """
    Type definition for `ClientCreateSizeConstraintSet` `Response`

    - **SizeConstraintSet** *(dict) --*

      A  SizeConstraintSet that contains no ``SizeConstraint`` objects.

      - **SizeConstraintSetId** *(string) --*

        A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
        information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
        ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
        a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
        ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

         ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
         ListSizeConstraintSets .

      - **Name** *(string) --*

        The name, if any, of the ``SizeConstraintSet`` .

      - **SizeConstraints** *(list) --*

        Specifies the parts of web requests that you want to inspect the size of.

        - *(dict) --*

          Specifies a constraint on the size of a part of the web request. AWS WAF uses the
          ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
          form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
          expression is true, the ``SizeConstraint`` is considered to match.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for the size constraint.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

            Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
            for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
            inspection.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

          - **ComparisonOperator** *(string) --*

            The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
            with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
            "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
            expression is true, the ``SizeConstraint`` is considered to match.

             **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

             **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

             **LE** : Used to test if the ``Size`` is less than or equal to the size of the
             ``FieldToMatch``

             **LT** : Used to test if the ``Size`` is strictly less than the size of the
             ``FieldToMatch``

             **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
             ``FieldToMatch``

             **GT** : Used to test if the ``Size`` is strictly greater than the size of the
             ``FieldToMatch``

          - **Size** *(integer) --*

            The size in bytes that you want AWS WAF to compare against the size of the specified
            ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
            ``FieldToMatch`` to build an expression in the form of "``Size``
            ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
            the ``SizeConstraint`` is considered to match.

            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

            If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
            character. For example, the URI ``/logo.jpg`` is nine characters long.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateSizeConstraintSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for snippets of malicious SQL code.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
):
    """
    Type definition for `ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSet` `SqlInjectionMatchTuples`

    Specifies the part of a web request that you want AWS WAF to inspect for snippets of
    malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for snippets of malicious SQL code.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef
):
    """
    Type definition for `ClientCreateSqlInjectionMatchSetResponse` `SqlInjectionMatchSet`

    A  SqlInjectionMatchSet .

    - **SqlInjectionMatchSetId** *(string) --*

      A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
      get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
      ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
      ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
      and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

       ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
       ListSqlInjectionMatchSets .

    - **Name** *(string) --*

      The name, if any, of the ``SqlInjectionMatchSet`` .

    - **SqlInjectionMatchTuples** *(list) --*

      Specifies the parts of web requests that you want to inspect for snippets of malicious SQL
      code.

      - *(dict) --*

        Specifies the part of a web request that you want AWS WAF to inspect for snippets of
        malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for snippets of malicious SQL code.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientCreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseTypeDef
):
    """
    Type definition for `ClientCreateSqlInjectionMatchSet` `Response`

    The response to a ``CreateSqlInjectionMatchSet`` request.

    - **SqlInjectionMatchSet** *(dict) --*

      A  SqlInjectionMatchSet .

      - **SqlInjectionMatchSetId** *(string) --*

        A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
        get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
        ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
        ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
        and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

         ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
         ListSqlInjectionMatchSets .

      - **Name** *(string) --*

        The name, if any, of the ``SqlInjectionMatchSet`` .

      - **SqlInjectionMatchTuples** *(list) --*

        Specifies the parts of web requests that you want to inspect for snippets of malicious SQL
        code.

        - *(dict) --*

          Specifies the part of a web request that you want AWS WAF to inspect for snippets of
          malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for snippets of malicious SQL code.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateSqlInjectionMatchSet`` request. You
      can also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateWebAclDefaultActionTypeDef = TypedDict(
    "_ClientCreateWebAclDefaultActionTypeDef", {"Type": str}
)


class ClientCreateWebAclDefaultActionTypeDef(_ClientCreateWebAclDefaultActionTypeDef):
    """
    Type definition for `ClientCreateWebAcl` `DefaultAction`

    The action that you want AWS WAF to take when a request doesn't match the criteria specified in
    any of the ``Rule`` objects that are associated with the ``WebACL`` .

    - **Type** *(string) --* **[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` .
      Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in
      the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the
      web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` .
    """


_ClientCreateWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLDefaultActionTypeDef", {"Type": str}, total=False
)


class ClientCreateWebAclResponseWebACLDefaultActionTypeDef(
    _ClientCreateWebAclResponseWebACLDefaultActionTypeDef
):
    """
    Type definition for `ClientCreateWebAclResponseWebACL` `DefaultAction`

    The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
    action is specified by the  WafAction object.

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
      ``WebACL`` .
    """


_ClientCreateWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesActionTypeDef", {"Type": str}, total=False
)


class ClientCreateWebAclResponseWebACLRulesActionTypeDef(
    _ClientCreateWebAclResponseWebACLRulesActionTypeDef
):
    """
    Type definition for `ClientCreateWebAclResponseWebACLRules` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the
    web ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
     to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
     other update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on
      the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
      action for a ``WebACL`` .
    """


_ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef(
    _ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef
):
    """
    Type definition for `ClientCreateWebAclResponseWebACLRules` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the
    ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
    ``RuleGroup`` that is specified by the ``ActivatedRule`` .

    - **RuleId** *(string) --*

      The unique identifier for the rule to exclude from the rule group.
    """


_ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef(
    _ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef
):
    """
    Type definition for `ClientCreateWebAclResponseWebACLRules` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
    individual rule in the ``RuleGroup`` matches the request and is configured to block
    that request. However if you first want to test the ``RuleGroup`` , set the
    ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
    specified by individual rules contained within the group. Instead of blocking matching
    requests, those requests will be counted. You can view a record of counted requests
    using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
     to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

       ``COUNT`` overrides the action specified by the individual rule within a
       ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.
    """


_ClientCreateWebAclResponseWebACLRulesTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientCreateWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[
            ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesTypeDef(
    _ClientCreateWebAclResponseWebACLRulesTypeDef
):
    """
    Type definition for `ClientCreateWebAclResponseWebACL` `Rules`

    The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
    want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
    that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
    ``BLOCK`` , or ``COUNT`` ).

    To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
    WebACLUpdate data type.

    - **Priority** *(integer) --*

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
      value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
      values don't need to be consecutive.

    - **RuleId** *(string) --*

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
      a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
      ``Rule`` from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the
      web ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
       to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
       other update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on
        the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
        action for a ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
      individual rule in the ``RuleGroup`` matches the request and is configured to block
      that request. However if you first want to test the ``RuleGroup`` , set the
      ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
      specified by individual rules contained within the group. Instead of blocking matching
      requests, those requests will be counted. You can view a record of counted requests
      using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
       to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

         ``COUNT`` overrides the action specified by the individual rule within a
         ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
      by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
      Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
      web ACL without setting the type, the  UpdateWebACL request will fail because the
      request tries to add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the
      specific rule within the rule group that is blocking the legitimate traffic and then
      disable (exclude) that particular rule. You can exclude rules from both your own rule
      groups and AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
      it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
      COUNT metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web
      ACL, perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
      more information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
        that you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
        ``RuleGroup`` that is specified by the ``ActivatedRule`` .

        - **RuleId** *(string) --*

          The unique identifier for the rule to exclude from the rule group.
    """


_ClientCreateWebAclResponseWebACLTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientCreateWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientCreateWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)


class ClientCreateWebAclResponseWebACLTypeDef(_ClientCreateWebAclResponseWebACLTypeDef):
    """
    Type definition for `ClientCreateWebAclResponse` `WebACL`

    The  WebACL returned in the ``CreateWebACL`` response.

    - **WebACLId** *(string) --*

      A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
      ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
      ``WebACL`` from AWS WAF (see  DeleteWebACL ).

       ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

    - **Name** *(string) --*

      A friendly name or description of the ``WebACL`` . You can't change the name of a
      ``WebACL`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``WebACL`` . The name can contain
      only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
      one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
      "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .

    - **DefaultAction** *(dict) --*

      The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
      action is specified by the  WafAction object.

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
        ``WebACL`` .

    - **Rules** *(list) --*

      An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the
      ``Rule`` , and the ID of the ``Rule`` .

      - *(dict) --*

        The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
        want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
        that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
        ``BLOCK`` , or ``COUNT`` ).

        To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
        WebACLUpdate data type.

        - **Priority** *(integer) --*

          Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
          lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
          value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
          values don't need to be consecutive.

        - **RuleId** *(string) --*

          The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
          a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
          ``Rule`` from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Action** *(dict) --*

          Specifies the action that CloudFront or AWS WAF takes when a web request matches the
          conditions in the ``Rule`` . Valid values for ``Action`` include the following:

          * ``ALLOW`` : CloudFront responds with the requested object.

          * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

          * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
          rule and then continues to inspect the web request based on the remaining rules in the
          web ACL.

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
           to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
           other update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

            Specifies how you want AWS WAF to respond to requests that match the settings in a
            ``Rule`` . Valid settings include the following:

            * ``ALLOW`` : AWS WAF allows requests

            * ``BLOCK`` : AWS WAF blocks requests

            * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
            conditions in the rule. AWS WAF then continues to inspect the web request based on
            the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
            action for a ``WebACL`` .

        - **OverrideAction** *(dict) --*

          Use the ``OverrideAction`` to test your ``RuleGroup`` .

          Any rule in a ``RuleGroup`` can potentially block a request. If you set the
          ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
          individual rule in the ``RuleGroup`` matches the request and is configured to block
          that request. However if you first want to test the ``RuleGroup`` , set the
          ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
          specified by individual rules contained within the group. Instead of blocking matching
          requests, those requests will be counted. You can view a record of counted requests
          using  GetSampledRequests .

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
           to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

             ``COUNT`` overrides the action specified by the individual rule within a
             ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

        - **Type** *(string) --*

          The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
          by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
          Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
          web ACL without setting the type, the  UpdateWebACL request will fail because the
          request tries to add a REGULAR rule with the specified ID, which does not exist.

        - **ExcludedRules** *(list) --*

          An array of rules to exclude from a rule group. This is applicable only when the
          ``ActivatedRule`` refers to a ``RuleGroup`` .

          Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
          unexpectedly (false positives). One troubleshooting technique is to identify the
          specific rule within the rule group that is blocking the legitimate traffic and then
          disable (exclude) that particular rule. You can exclude rules from both your own rule
          groups and AWS Marketplace rule groups that have been associated with a web ACL.

          Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
          it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
          ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
          COUNT metrics for each ``ExcludedRule`` .

          If you want to exclude rules from a rule group that is already associated with a web
          ACL, perform the following steps:

          * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
          more information about the logs, see `Logging Web ACL Traffic Information
          <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

          * Submit an  UpdateWebACL request that has two actions:

            * The first action deletes the existing rule group from the web ACL. That is, in the
            UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
            ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
            that you want to exclude.

            * The second action inserts the same rule group back in, but specifying the rules to
            exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
            ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
            ``ExcludedRules`` should contain the rules that you want to exclude.

          - *(dict) --*

            The rule to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
            ``RuleGroup`` that is specified by the ``ActivatedRule`` .

            - **RuleId** *(string) --*

              The unique identifier for the rule to exclude from the rule group.

    - **WebACLArn** *(string) --*

      Tha Amazon Resource Name (ARN) of the web ACL.
    """


_ClientCreateWebAclResponseTypeDef = TypedDict(
    "_ClientCreateWebAclResponseTypeDef",
    {"WebACL": ClientCreateWebAclResponseWebACLTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateWebAclResponseTypeDef(_ClientCreateWebAclResponseTypeDef):
    """
    Type definition for `ClientCreateWebAcl` `Response`

    - **WebACL** *(dict) --*

      The  WebACL returned in the ``CreateWebACL`` response.

      - **WebACLId** *(string) --*

        A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
        ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
        ``WebACL`` from AWS WAF (see  DeleteWebACL ).

         ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

      - **Name** *(string) --*

        A friendly name or description of the ``WebACL`` . You can't change the name of a
        ``WebACL`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``WebACL`` . The name can contain
        only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
        one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
        "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .

      - **DefaultAction** *(dict) --*

        The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
        action is specified by the  WafAction object.

        - **Type** *(string) --*

          Specifies how you want AWS WAF to respond to requests that match the settings in a
          ``Rule`` . Valid settings include the following:

          * ``ALLOW`` : AWS WAF allows requests

          * ``BLOCK`` : AWS WAF blocks requests

          * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
          conditions in the rule. AWS WAF then continues to inspect the web request based on the
          remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
          ``WebACL`` .

      - **Rules** *(list) --*

        An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the
        ``Rule`` , and the ID of the ``Rule`` .

        - *(dict) --*

          The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
          want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
          that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
          ``BLOCK`` , or ``COUNT`` ).

          To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
          WebACLUpdate data type.

          - **Priority** *(integer) --*

            Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
            lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
            value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
            values don't need to be consecutive.

          - **RuleId** *(string) --*

            The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
            ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
            a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
            ``Rule`` from AWS WAF (see  DeleteRule ).

             ``RuleId`` is returned by  CreateRule and by  ListRules .

          - **Action** *(dict) --*

            Specifies the action that CloudFront or AWS WAF takes when a web request matches the
            conditions in the ``Rule`` . Valid values for ``Action`` include the following:

            * ``ALLOW`` : CloudFront responds with the requested object.

            * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

            * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
            rule and then continues to inspect the web request based on the remaining rules in the
            web ACL.

             ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
             to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
             other update requests, ``ActivatedRule|Action`` is used instead of
             ``ActivatedRule|OverrideAction`` .

            - **Type** *(string) --*

              Specifies how you want AWS WAF to respond to requests that match the settings in a
              ``Rule`` . Valid settings include the following:

              * ``ALLOW`` : AWS WAF allows requests

              * ``BLOCK`` : AWS WAF blocks requests

              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
              conditions in the rule. AWS WAF then continues to inspect the web request based on
              the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
              action for a ``WebACL`` .

          - **OverrideAction** *(dict) --*

            Use the ``OverrideAction`` to test your ``RuleGroup`` .

            Any rule in a ``RuleGroup`` can potentially block a request. If you set the
            ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
            individual rule in the ``RuleGroup`` matches the request and is configured to block
            that request. However if you first want to test the ``RuleGroup`` , set the
            ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
            specified by individual rules contained within the group. Instead of blocking matching
            requests, those requests will be counted. You can view a record of counted requests
            using  GetSampledRequests .

             ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
             to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
             update requests, ``ActivatedRule|Action`` is used instead of
             ``ActivatedRule|OverrideAction`` .

            - **Type** *(string) --*

               ``COUNT`` overrides the action specified by the individual rule within a
               ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

          - **Type** *(string) --*

            The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
            by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
            Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
            web ACL without setting the type, the  UpdateWebACL request will fail because the
            request tries to add a REGULAR rule with the specified ID, which does not exist.

          - **ExcludedRules** *(list) --*

            An array of rules to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` .

            Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
            unexpectedly (false positives). One troubleshooting technique is to identify the
            specific rule within the rule group that is blocking the legitimate traffic and then
            disable (exclude) that particular rule. You can exclude rules from both your own rule
            groups and AWS Marketplace rule groups that have been associated with a web ACL.

            Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
            it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
            ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
            COUNT metrics for each ``ExcludedRule`` .

            If you want to exclude rules from a rule group that is already associated with a web
            ACL, perform the following steps:

            * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
            more information about the logs, see `Logging Web ACL Traffic Information
            <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

            * Submit an  UpdateWebACL request that has two actions:

              * The first action deletes the existing rule group from the web ACL. That is, in the
              UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
              ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
              that you want to exclude.

              * The second action inserts the same rule group back in, but specifying the rules to
              exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
              ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
              ``ExcludedRules`` should contain the rules that you want to exclude.

            - *(dict) --*

              The rule to exclude from a rule group. This is applicable only when the
              ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
              ``RuleGroup`` that is specified by the ``ActivatedRule`` .

              - **RuleId** *(string) --*

                The unique identifier for the rule to exclude from the rule group.

      - **WebACLArn** *(string) --*

        Tha Amazon Resource Name (ARN) of the web ACL.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateWebACL`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientCreateWebAclTagsTypeDef = TypedDict(
    "_ClientCreateWebAclTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateWebAclTagsTypeDef(_ClientCreateWebAclTagsTypeDef):
    """
    Type definition for `ClientCreateWebAcl` `Tags`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for cross-site scripting attacks.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
    },
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
):
    """
    Type definition for `ClientCreateXssMatchSetResponseXssMatchSet` `XssMatchTuples`

    Specifies the part of a web request that you want AWS WAF to inspect for cross-site
    scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for cross-site scripting attacks.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientCreateXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[
            ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetTypeDef
):
    """
    Type definition for `ClientCreateXssMatchSetResponse` `XssMatchSet`

    An  XssMatchSet .

    - **XssMatchSetId** *(string) --*

      A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
      about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
      UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
      DeleteXssMatchSet ).

       ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

    - **Name** *(string) --*

      The name, if any, of the ``XssMatchSet`` .

    - **XssMatchTuples** *(list) --*

      Specifies the parts of web requests that you want to inspect for cross-site scripting
      attacks.

      - *(dict) --*

        Specifies the part of a web request that you want AWS WAF to inspect for cross-site
        scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for cross-site scripting attacks.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientCreateXssMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": ClientCreateXssMatchSetResponseXssMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateXssMatchSetResponseTypeDef(_ClientCreateXssMatchSetResponseTypeDef):
    """
    Type definition for `ClientCreateXssMatchSet` `Response`

    The response to a ``CreateXssMatchSet`` request.

    - **XssMatchSet** *(dict) --*

      An  XssMatchSet .

      - **XssMatchSetId** *(string) --*

        A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
        about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
        UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
        DeleteXssMatchSet ).

         ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

      - **Name** *(string) --*

        The name, if any, of the ``XssMatchSet`` .

      - **XssMatchTuples** *(list) --*

        Specifies the parts of web requests that you want to inspect for cross-site scripting
        attacks.

        - *(dict) --*

          Specifies the part of a web request that you want AWS WAF to inspect for cross-site
          scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for cross-site scripting attacks.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``CreateXssMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteByteMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteByteMatchSetResponseTypeDef(_ClientDeleteByteMatchSetResponseTypeDef):
    """
    Type definition for `ClientDeleteByteMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteByteMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteGeoMatchSetResponseTypeDef(_ClientDeleteGeoMatchSetResponseTypeDef):
    """
    Type definition for `ClientDeleteGeoMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteGeoMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteIpSetResponseTypeDef = TypedDict(
    "_ClientDeleteIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteIpSetResponseTypeDef(_ClientDeleteIpSetResponseTypeDef):
    """
    Type definition for `ClientDeleteIpSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteIPSet`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientDeleteRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRateBasedRuleResponseTypeDef(
    _ClientDeleteRateBasedRuleResponseTypeDef
):
    """
    Type definition for `ClientDeleteRateBasedRule` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteRateBasedRule`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRegexMatchSetResponseTypeDef(
    _ClientDeleteRegexMatchSetResponseTypeDef
):
    """
    Type definition for `ClientDeleteRegexMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteRegexMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientDeleteRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRegexPatternSetResponseTypeDef(
    _ClientDeleteRegexPatternSetResponseTypeDef
):
    """
    Type definition for `ClientDeleteRegexPatternSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteRegexPatternSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteRuleGroupResponseTypeDef = TypedDict(
    "_ClientDeleteRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRuleGroupResponseTypeDef(_ClientDeleteRuleGroupResponseTypeDef):
    """
    Type definition for `ClientDeleteRuleGroup` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteRuleGroup`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteRuleResponseTypeDef = TypedDict(
    "_ClientDeleteRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRuleResponseTypeDef(_ClientDeleteRuleResponseTypeDef):
    """
    Type definition for `ClientDeleteRule` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteRule`` request. You can also use this
      value to query the status of the request. For more information, see  GetChangeTokenStatus .
    """


_ClientDeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientDeleteSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteSizeConstraintSetResponseTypeDef(
    _ClientDeleteSizeConstraintSetResponseTypeDef
):
    """
    Type definition for `ClientDeleteSizeConstraintSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteSizeConstraintSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteSqlInjectionMatchSetResponseTypeDef",
    {"ChangeToken": str},
    total=False,
)


class ClientDeleteSqlInjectionMatchSetResponseTypeDef(
    _ClientDeleteSqlInjectionMatchSetResponseTypeDef
):
    """
    Type definition for `ClientDeleteSqlInjectionMatchSet` `Response`

    The response to a request to delete a  SqlInjectionMatchSet from AWS WAF.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteSqlInjectionMatchSet`` request. You
      can also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteWebAclResponseTypeDef = TypedDict(
    "_ClientDeleteWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteWebAclResponseTypeDef(_ClientDeleteWebAclResponseTypeDef):
    """
    Type definition for `ClientDeleteWebAcl` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteWebACL`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientDeleteXssMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteXssMatchSetResponseTypeDef(_ClientDeleteXssMatchSetResponseTypeDef):
    """
    Type definition for `ClientDeleteXssMatchSet` `Response`

    The response to a request to delete an  XssMatchSet from AWS WAF.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``DeleteXssMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientGetByteMatchSetResponseByteMatchSetByteMatchTuples` `FieldToMatch`

    The part of a web request that you want AWS WAF to search, such as a specified header
    or a query string. For more information, see  FieldToMatch .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": str,
        "PositionalConstraint": str,
    },
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
):
    """
    Type definition for `ClientGetByteMatchSetResponseByteMatchSet` `ByteMatchTuples`

    The bytes (typically a string that corresponds with ASCII characters) that you want AWS
    WAF to search for in web requests, the location in requests that you want AWS WAF to
    search, and other settings.

    - **FieldToMatch** *(dict) --*

      The part of a web request that you want AWS WAF to search, such as a specified header
      or a query string. For more information, see  FieldToMatch .

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TargetString** *(bytes) --*

      The value that you want AWS WAF to search for. AWS WAF searches for the specified
      string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
      length of the value is 50 bytes.

      Valid values depend on the values that you specified for ``FieldToMatch`` :

      * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
      you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
      ``Referer`` header.

      * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
      request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
      ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
      which is the part of a URL that appears after a ``?`` character.

      * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
      identifies a resource, for example, ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes
      of the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
      as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
      single parameter, AWS WAF inspects all parameters within the query string for the value
      or regex pattern that you specify in ``TargetString`` .

      If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
      case sensitive.

       **If you're using the AWS WAF API**

      Specify a base64-encoded version of the value. The maximum length of the value before
      you base64-encode it is 50 bytes.

      For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
      ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
      ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
      resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

       **If you're using the AWS CLI or one of the AWS SDKs**

      The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
      value.

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``TargetString`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **PositionalConstraint** *(string) --*

      Within the portion of a web request that you want to search (for example, in the query
      string, if any), specify where you want AWS WAF to search. Valid values include the
      following:

       **CONTAINS**

      The specified part of the web request must include the value of ``TargetString`` , but
      the location doesn't matter.

       **CONTAINS_WORD**

      The specified part of the web request must include the value of ``TargetString`` , and
      ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
      0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
      following:

      * ``TargetString`` exactly matches the value of the specified part of the web request,
      such as the value of a header.

      * ``TargetString`` is at the beginning of the specified part of the web request and is
      followed by a character other than an alphanumeric character or underscore (_), for
      example, ``BadBot;`` .

      * ``TargetString`` is at the end of the specified part of the web request and is
      preceded by a character other than an alphanumeric character or underscore (_), for
      example, ``;BadBot`` .

      * ``TargetString`` is in the middle of the specified part of the web request and is
      preceded and followed by characters other than alphanumeric characters or underscore
      (_), for example, ``-BadBot;`` .

       **EXACTLY**

      The value of the specified part of the web request must exactly match the value of
      ``TargetString`` .

       **STARTS_WITH**

      The value of ``TargetString`` must appear at the beginning of the specified part of the
      web request.

       **ENDS_WITH**

      The value of ``TargetString`` must appear at the end of the specified part of the web
      request.
    """


_ClientGetByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[
            ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetTypeDef
):
    """
    Type definition for `ClientGetByteMatchSetResponse` `ByteMatchSet`

    Information about the  ByteMatchSet that you specified in the ``GetByteMatchSet`` request.
    For more information, see the following topics:

    *  ByteMatchSet : Contains ``ByteMatchSetId`` , ``ByteMatchTuples`` , and ``Name``

    * ``ByteMatchTuples`` : Contains an array of  ByteMatchTuple objects. Each ``ByteMatchTuple``
    object contains  FieldToMatch , ``PositionalConstraint`` , ``TargetString`` , and
    ``TextTransformation``

    *  FieldToMatch : Contains ``Data`` and ``Type``

    - **ByteMatchSetId** *(string) --*

      The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
      information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
      (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
      DeleteByteMatchSet ).

       ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
      create a ``ByteMatchSet`` .

    - **ByteMatchTuples** *(list) --*

      Specifies the bytes (typically a string that corresponds with ASCII characters) that you
      want AWS WAF to search for in web requests, the location in requests that you want AWS WAF
      to search, and other settings.

      - *(dict) --*

        The bytes (typically a string that corresponds with ASCII characters) that you want AWS
        WAF to search for in web requests, the location in requests that you want AWS WAF to
        search, and other settings.

        - **FieldToMatch** *(dict) --*

          The part of a web request that you want AWS WAF to search, such as a specified header
          or a query string. For more information, see  FieldToMatch .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TargetString** *(bytes) --*

          The value that you want AWS WAF to search for. AWS WAF searches for the specified
          string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
          length of the value is 50 bytes.

          Valid values depend on the values that you specified for ``FieldToMatch`` :

          * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
          you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
          ``Referer`` header.

          * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
          request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
          ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
          which is the part of a URL that appears after a ``?`` character.

          * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
          identifies a resource, for example, ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes
          of the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
          as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
          single parameter, AWS WAF inspects all parameters within the query string for the value
          or regex pattern that you specify in ``TargetString`` .

          If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
          case sensitive.

           **If you're using the AWS WAF API**

          Specify a base64-encoded version of the value. The maximum length of the value before
          you base64-encode it is 50 bytes.

          For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
          ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
          ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
          resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

           **If you're using the AWS CLI or one of the AWS SDKs**

          The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
          value.

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``TargetString`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

        - **PositionalConstraint** *(string) --*

          Within the portion of a web request that you want to search (for example, in the query
          string, if any), specify where you want AWS WAF to search. Valid values include the
          following:

           **CONTAINS**

          The specified part of the web request must include the value of ``TargetString`` , but
          the location doesn't matter.

           **CONTAINS_WORD**

          The specified part of the web request must include the value of ``TargetString`` , and
          ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
          0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
          following:

          * ``TargetString`` exactly matches the value of the specified part of the web request,
          such as the value of a header.

          * ``TargetString`` is at the beginning of the specified part of the web request and is
          followed by a character other than an alphanumeric character or underscore (_), for
          example, ``BadBot;`` .

          * ``TargetString`` is at the end of the specified part of the web request and is
          preceded by a character other than an alphanumeric character or underscore (_), for
          example, ``;BadBot`` .

          * ``TargetString`` is in the middle of the specified part of the web request and is
          preceded and followed by characters other than alphanumeric characters or underscore
          (_), for example, ``-BadBot;`` .

           **EXACTLY**

          The value of the specified part of the web request must exactly match the value of
          ``TargetString`` .

           **STARTS_WITH**

          The value of ``TargetString`` must appear at the beginning of the specified part of the
          web request.

           **ENDS_WITH**

          The value of ``TargetString`` must appear at the end of the specified part of the web
          request.
    """


_ClientGetByteMatchSetResponseTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseTypeDef",
    {"ByteMatchSet": ClientGetByteMatchSetResponseByteMatchSetTypeDef},
    total=False,
)


class ClientGetByteMatchSetResponseTypeDef(_ClientGetByteMatchSetResponseTypeDef):
    """
    Type definition for `ClientGetByteMatchSet` `Response`

    - **ByteMatchSet** *(dict) --*

      Information about the  ByteMatchSet that you specified in the ``GetByteMatchSet`` request.
      For more information, see the following topics:

      *  ByteMatchSet : Contains ``ByteMatchSetId`` , ``ByteMatchTuples`` , and ``Name``

      * ``ByteMatchTuples`` : Contains an array of  ByteMatchTuple objects. Each ``ByteMatchTuple``
      object contains  FieldToMatch , ``PositionalConstraint`` , ``TargetString`` , and
      ``TextTransformation``

      *  FieldToMatch : Contains ``Data`` and ``Type``

      - **ByteMatchSetId** *(string) --*

        The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
        information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
        (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
        DeleteByteMatchSet ).

         ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
        create a ``ByteMatchSet`` .

      - **ByteMatchTuples** *(list) --*

        Specifies the bytes (typically a string that corresponds with ASCII characters) that you
        want AWS WAF to search for in web requests, the location in requests that you want AWS WAF
        to search, and other settings.

        - *(dict) --*

          The bytes (typically a string that corresponds with ASCII characters) that you want AWS
          WAF to search for in web requests, the location in requests that you want AWS WAF to
          search, and other settings.

          - **FieldToMatch** *(dict) --*

            The part of a web request that you want AWS WAF to search, such as a specified header
            or a query string. For more information, see  FieldToMatch .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TargetString** *(bytes) --*

            The value that you want AWS WAF to search for. AWS WAF searches for the specified
            string in the part of web requests that you specified in ``FieldToMatch`` . The maximum
            length of the value is 50 bytes.

            Valid values depend on the values that you specified for ``FieldToMatch`` :

            * ``HEADER`` : The value that you want AWS WAF to search for in the request header that
            you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or
            ``Referer`` header.

            * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
            request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
            ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

            * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
            which is the part of a URL that appears after a ``?`` character.

            * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
            identifies a resource, for example, ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The request
            body immediately follows the request headers. Note that only the first ``8192`` bytes
            of the request body are forwarded to AWS WAF for inspection. To allow or block requests
            based on the length of the body, you can create a size constraint set. For more
            information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
            as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
            characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a
            single parameter, AWS WAF inspects all parameters within the query string for the value
            or regex pattern that you specify in ``TargetString`` .

            If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is
            case sensitive.

             **If you're using the AWS WAF API**

            Specify a base64-encoded version of the value. The maximum length of the value before
            you base64-encode it is 50 bytes.

            For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
            ``User-Agent`` . If you want to search the ``User-Agent`` header for the value
            ``BadBot`` , you base64-encode ``BadBot`` using MIME base64-encoding and include the
            resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

             **If you're using the AWS CLI or one of the AWS SDKs**

            The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
            value.

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``TargetString`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

          - **PositionalConstraint** *(string) --*

            Within the portion of a web request that you want to search (for example, in the query
            string, if any), specify where you want AWS WAF to search. Valid values include the
            following:

             **CONTAINS**

            The specified part of the web request must include the value of ``TargetString`` , but
            the location doesn't matter.

             **CONTAINS_WORD**

            The specified part of the web request must include the value of ``TargetString`` , and
            ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z,
            0-9, or _). In addition, ``TargetString`` must be a word, which means one of the
            following:

            * ``TargetString`` exactly matches the value of the specified part of the web request,
            such as the value of a header.

            * ``TargetString`` is at the beginning of the specified part of the web request and is
            followed by a character other than an alphanumeric character or underscore (_), for
            example, ``BadBot;`` .

            * ``TargetString`` is at the end of the specified part of the web request and is
            preceded by a character other than an alphanumeric character or underscore (_), for
            example, ``;BadBot`` .

            * ``TargetString`` is in the middle of the specified part of the web request and is
            preceded and followed by characters other than alphanumeric characters or underscore
            (_), for example, ``-BadBot;`` .

             **EXACTLY**

            The value of the specified part of the web request must exactly match the value of
            ``TargetString`` .

             **STARTS_WITH**

            The value of ``TargetString`` must appear at the beginning of the specified part of the
            web request.

             **ENDS_WITH**

            The value of ``TargetString`` must appear at the end of the specified part of the web
            request.
    """


_ClientGetChangeTokenResponseTypeDef = TypedDict(
    "_ClientGetChangeTokenResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientGetChangeTokenResponseTypeDef(_ClientGetChangeTokenResponseTypeDef):
    """
    Type definition for `ClientGetChangeToken` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used in the request. Use this value in a
      ``GetChangeTokenStatus`` request to get the current status of the request.
    """


_ClientGetChangeTokenStatusResponseTypeDef = TypedDict(
    "_ClientGetChangeTokenStatusResponseTypeDef",
    {"ChangeTokenStatus": str},
    total=False,
)


class ClientGetChangeTokenStatusResponseTypeDef(
    _ClientGetChangeTokenStatusResponseTypeDef
):
    """
    Type definition for `ClientGetChangeTokenStatus` `Response`

    - **ChangeTokenStatus** *(string) --*

      The status of the change token.
    """


_ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef(
    _ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
):
    """
    Type definition for `ClientGetGeoMatchSetResponseGeoMatchSet` `GeoMatchConstraints`

    The country from which web requests originate that you want AWS WAF to search for.

    - **Type** *(string) --*

      The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
      the only valid value.

    - **Value** *(string) --*

      The country that you want AWS WAF to search for.
    """


_ClientGetGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientGetGeoMatchSetResponseGeoMatchSetTypeDef(
    _ClientGetGeoMatchSetResponseGeoMatchSetTypeDef
):
    """
    Type definition for `ClientGetGeoMatchSetResponse` `GeoMatchSet`

    Information about the  GeoMatchSet that you specified in the ``GetGeoMatchSet`` request. This
    includes the ``Type`` , which for a ``GeoMatchContraint`` is always ``Country`` , as well as
    the ``Value`` , which is the identifier for a specific country.

    - **GeoMatchSetId** *(string) --*

      The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
      about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
      UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
      (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

       ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  GeoMatchSet . You can't change the name of an
      ``GeoMatchSet`` after you create it.

    - **GeoMatchConstraints** *(list) --*

      An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to
      search for.

      - *(dict) --*

        The country from which web requests originate that you want AWS WAF to search for.

        - **Type** *(string) --*

          The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
          the only valid value.

        - **Value** *(string) --*

          The country that you want AWS WAF to search for.
    """


_ClientGetGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseTypeDef",
    {"GeoMatchSet": ClientGetGeoMatchSetResponseGeoMatchSetTypeDef},
    total=False,
)


class ClientGetGeoMatchSetResponseTypeDef(_ClientGetGeoMatchSetResponseTypeDef):
    """
    Type definition for `ClientGetGeoMatchSet` `Response`

    - **GeoMatchSet** *(dict) --*

      Information about the  GeoMatchSet that you specified in the ``GetGeoMatchSet`` request. This
      includes the ``Type`` , which for a ``GeoMatchContraint`` is always ``Country`` , as well as
      the ``Value`` , which is the identifier for a specific country.

      - **GeoMatchSetId** *(string) --*

        The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
        about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
        UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

         ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  GeoMatchSet . You can't change the name of an
        ``GeoMatchSet`` after you create it.

      - **GeoMatchConstraints** *(list) --*

        An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to
        search for.

        - *(dict) --*

          The country from which web requests originate that you want AWS WAF to search for.

          - **Type** *(string) --*

            The type of geographical area you want AWS WAF to search for. Currently ``Country`` is
            the only valid value.

          - **Value** *(string) --*

            The country that you want AWS WAF to search for.
    """


_ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "_ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef(
    _ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef
):
    """
    Type definition for `ClientGetIpSetResponseIPSet` `IPSetDescriptors`

    Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
    format) that web requests originate from.

    - **Type** *(string) --*

      Specify ``IPV4`` or ``IPV6`` .

    - **Value** *(string) --*

      Specify an IPv4 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 192.0.2.44, specify ``192.0.2.44/32`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP
      addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

      For more information about CIDR notation, see the Wikipedia entry `Classless
      Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

      Specify an IPv6 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 1111:0000:0000:0000:0000:0000:0000:0111, specify
      ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP
      addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
      1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
      ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientGetIpSetResponseIPSetTypeDef = TypedDict(
    "_ClientGetIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)


class ClientGetIpSetResponseIPSetTypeDef(_ClientGetIpSetResponseIPSetTypeDef):
    """
    Type definition for `ClientGetIpSetResponse` `IPSet`

    Information about the  IPSet that you specified in the ``GetIPSet`` request. For more
    information, see the following topics:

    *  IPSet : Contains ``IPSetDescriptors`` , ``IPSetId`` , and ``Name``

    * ``IPSetDescriptors`` : Contains an array of  IPSetDescriptor objects. Each
    ``IPSetDescriptor`` object contains ``Type`` and ``Value``

    - **IPSetId** *(string) --*

      The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
      ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
      into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
      from AWS WAF (see  DeleteIPSet ).

       ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

    - **Name** *(string) --*

      A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
      after you create it.

    - **IPSetDescriptors** *(list) --*

      The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation)
      that web requests originate from. If the ``WebACL`` is associated with a CloudFront
      distribution and the viewer did not use an HTTP proxy or a load balancer to send the
      request, this is the value of the c-ip field in the CloudFront access logs.

      - *(dict) --*

        Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
        format) that web requests originate from.

        - **Type** *(string) --*

          Specify ``IPV4`` or ``IPV6`` .

        - **Value** *(string) --*

          Specify an IPv4 address by using CIDR notation. For example:

          * To configure AWS WAF to allow, block, or count requests that originated from the IP
          address 192.0.2.44, specify ``192.0.2.44/32`` .

          * To configure AWS WAF to allow, block, or count requests that originated from IP
          addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

          For more information about CIDR notation, see the Wikipedia entry `Classless
          Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

          Specify an IPv6 address by using CIDR notation. For example:

          * To configure AWS WAF to allow, block, or count requests that originated from the IP
          address 1111:0000:0000:0000:0000:0000:0000:0111, specify
          ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

          * To configure AWS WAF to allow, block, or count requests that originated from IP
          addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
          1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
          ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientGetIpSetResponseTypeDef = TypedDict(
    "_ClientGetIpSetResponseTypeDef",
    {"IPSet": ClientGetIpSetResponseIPSetTypeDef},
    total=False,
)


class ClientGetIpSetResponseTypeDef(_ClientGetIpSetResponseTypeDef):
    """
    Type definition for `ClientGetIpSet` `Response`

    - **IPSet** *(dict) --*

      Information about the  IPSet that you specified in the ``GetIPSet`` request. For more
      information, see the following topics:

      *  IPSet : Contains ``IPSetDescriptors`` , ``IPSetId`` , and ``Name``

      * ``IPSetDescriptors`` : Contains an array of  IPSetDescriptor objects. Each
      ``IPSetDescriptor`` object contains ``Type`` and ``Value``

      - **IPSetId** *(string) --*

        The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
        ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
        into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
        from AWS WAF (see  DeleteIPSet ).

         ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

      - **Name** *(string) --*

        A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
        after you create it.

      - **IPSetDescriptors** *(list) --*

        The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation)
        that web requests originate from. If the ``WebACL`` is associated with a CloudFront
        distribution and the viewer did not use an HTTP proxy or a load balancer to send the
        request, this is the value of the c-ip field in the CloudFront access logs.

        - *(dict) --*

          Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR
          format) that web requests originate from.

          - **Type** *(string) --*

            Specify ``IPV4`` or ``IPV6`` .

          - **Value** *(string) --*

            Specify an IPv4 address by using CIDR notation. For example:

            * To configure AWS WAF to allow, block, or count requests that originated from the IP
            address 192.0.2.44, specify ``192.0.2.44/32`` .

            * To configure AWS WAF to allow, block, or count requests that originated from IP
            addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless
            Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

            Specify an IPv6 address by using CIDR notation. For example:

            * To configure AWS WAF to allow, block, or count requests that originated from the IP
            address 1111:0000:0000:0000:0000:0000:0000:0111, specify
            ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

            * To configure AWS WAF to allow, block, or count requests that originated from IP
            addresses 1111:0000:0000:0000:0000:0000:0000:0000 to
            1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
            ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef(
    _ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
):
    """
    Type definition for `ClientGetLoggingConfigurationResponseLoggingConfiguration` `RedactedFields`

    Specifies where in a web request to look for ``TargetString`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
      is asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes
      of the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
      as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
      is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    Type definition for `ClientGetLoggingConfigurationResponse` `LoggingConfiguration`

    The  LoggingConfiguration for the specified web ACL.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the web ACL that you want to associate with
      ``LogDestinationConfigs`` .

    - **LogDestinationConfigs** *(list) --*

      An array of Amazon Kinesis Data Firehose ARNs.

      - *(string) --*

    - **RedactedFields** *(list) --*

      The parts of the request that you want redacted from the logs. For example, if you redact
      the cookie field, the cookie field in the firehose will be ``xxx`` .

      - *(dict) --*

        Specifies where in a web request to look for ``TargetString`` .

        - **Type** *(string) --*

          The part of the web request that you want AWS WAF to search for a specified string.
          Parts of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
          is asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes
          of the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
          as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
          AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
          is not case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
          that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
          parameter name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientGetLoggingConfigurationResponseTypeDef(
    _ClientGetLoggingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetLoggingConfiguration` `Response`

    - **LoggingConfiguration** *(dict) --*

      The  LoggingConfiguration for the specified web ACL.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the web ACL that you want to associate with
        ``LogDestinationConfigs`` .

      - **LogDestinationConfigs** *(list) --*

        An array of Amazon Kinesis Data Firehose ARNs.

        - *(string) --*

      - **RedactedFields** *(list) --*

        The parts of the request that you want redacted from the logs. For example, if you redact
        the cookie field, the cookie field in the firehose will be ``xxx`` .

        - *(dict) --*

          Specifies where in a web request to look for ``TargetString`` .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
            or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
            header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
            is asking the origin to perform. Amazon CloudFront supports the following methods:
            ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The request
            body immediately follows the request headers. Note that only the first ``8192`` bytes
            of the request body are forwarded to AWS WAF for inspection. To allow or block requests
            based on the length of the body, you can create a size constraint set. For more
            information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
            as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
            characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value or
            regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
            is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetPermissionPolicyResponseTypeDef = TypedDict(
    "_ClientGetPermissionPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetPermissionPolicyResponseTypeDef(
    _ClientGetPermissionPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetPermissionPolicy` `Response`

    - **Policy** *(string) --*

      The IAM policy attached to the specified RuleGroup.
    """


_ClientGetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "_ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    {"ManagedKeys": List[str], "NextMarker": str},
    total=False,
)


class ClientGetRateBasedRuleManagedKeysResponseTypeDef(
    _ClientGetRateBasedRuleManagedKeysResponseTypeDef
):
    """
    Type definition for `ClientGetRateBasedRuleManagedKeys` `Response`

    - **ManagedKeys** *(list) --*

      An array of IP addresses that currently are blocked by the specified  RateBasedRule .

      - *(string) --*

    - **NextMarker** *(string) --*

      A null value and not currently used.
    """


_ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
    total=False,
)


class ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef(
    _ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef
):
    """
    Type definition for `ClientGetRateBasedRuleResponseRule` `MatchPredicates`

    Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
    RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
    ``Rule`` and, for each object, indicates whether you want to negate the settings, for
    example, requests that do NOT originate from the IP address 192.0.2.44.

    - **Negated** *(boolean) --*

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
      based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
       XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
       an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
       requests based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
      the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
      an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
      count requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --*

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --*

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientGetRateBasedRuleResponseRuleTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[
            ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef
        ],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)


class ClientGetRateBasedRuleResponseRuleTypeDef(
    _ClientGetRateBasedRuleResponseRuleTypeDef
):
    """
    Type definition for `ClientGetRateBasedRuleResponse` `Rule`

    Information about the  RateBasedRule that you specified in the ``GetRateBasedRule`` request.

    - **RuleId** *(string) --*

      A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
      about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
      UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
      ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
      DeleteRateBasedRule ).

    - **Name** *(string) --*

      A friendly name or description for a ``RateBasedRule`` . You can't change the name of a
      ``RateBasedRule`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for a ``RateBasedRule`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RateBasedRule`` .

    - **MatchPredicates** *(list) --*

      The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
      IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

      - *(dict) --*

        Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
        RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
        ``Rule`` and, for each object, indicates whether you want to negate the settings, for
        example, requests that do NOT originate from the IP address 192.0.2.44.

        - **Negated** *(boolean) --*

          Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
          based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
           XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
           an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
           requests based on that IP address.

          Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
          the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
          XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
          an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
          count requests based on all IP addresses *except*  ``192.0.2.44`` .

        - **Type** *(string) --*

          The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

        - **DataId** *(string) --*

          A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
          ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

    - **RateKey** *(string) --*

      The field that AWS WAF uses to determine if requests are likely arriving from single source
      and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` .
      ``IP`` indicates that requests arriving from the same IP address are subject to the
      ``RateLimit`` that is specified in the ``RateBasedRule`` .

    - **RateLimit** *(integer) --*

      The maximum number of requests, which have an identical value in the field specified by the
      ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the
      ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers
      the action that is specified for this rule.
    """


_ClientGetRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseTypeDef",
    {"Rule": ClientGetRateBasedRuleResponseRuleTypeDef},
    total=False,
)


class ClientGetRateBasedRuleResponseTypeDef(_ClientGetRateBasedRuleResponseTypeDef):
    """
    Type definition for `ClientGetRateBasedRule` `Response`

    - **Rule** *(dict) --*

      Information about the  RateBasedRule that you specified in the ``GetRateBasedRule`` request.

      - **RuleId** *(string) --*

        A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
        about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
        UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
        ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
        DeleteRateBasedRule ).

      - **Name** *(string) --*

        A friendly name or description for a ``RateBasedRule`` . You can't change the name of a
        ``RateBasedRule`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for a ``RateBasedRule`` . The name can
        contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
        length one. It can't contain whitespace or metric names reserved for AWS WAF, including
        "All" and "Default_Action." You can't change the name of the metric after you create the
        ``RateBasedRule`` .

      - **MatchPredicates** *(list) --*

        The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
        IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

        - *(dict) --*

          Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
          RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
          ``Rule`` and, for each object, indicates whether you want to negate the settings, for
          example, requests that do NOT originate from the IP address 192.0.2.44.

          - **Negated** *(boolean) --*

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
            based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
             XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
             an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
             requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
            the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
            XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
            an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
            count requests based on all IP addresses *except*  ``192.0.2.44`` .

          - **Type** *(string) --*

            The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

          - **DataId** *(string) --*

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
            ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

      - **RateKey** *(string) --*

        The field that AWS WAF uses to determine if requests are likely arriving from single source
        and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` .
        ``IP`` indicates that requests arriving from the same IP address are subject to the
        ``RateLimit`` that is specified in the ``RateBasedRule`` .

      - **RateLimit** *(integer) --*

        The maximum number of requests, which have an identical value in the field specified by the
        ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the
        ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers
        the action that is specified for this rule.
    """


_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for the ``RegexPatternSet`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
        "RegexPatternSetId": str,
    },
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
):
    """
    Type definition for `ClientGetRegexMatchSetResponseRegexMatchSet` `RegexMatchTuples`

    The regular expression pattern that you want AWS WAF to search for in web requests, the
    location in requests that you want AWS WAF to search, and other settings. Each
    ``RegexMatchTuple`` object contains:

    * The part of a web request that you want AWS WAF to inspect, such as a query string or
    the value of the ``User-Agent`` header.

    * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
    For more information, see  RegexPatternSet .

    * Whether to perform any conversions on the request, such as converting it to lowercase,
    before inspecting it for the specified string.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for the ``RegexPatternSet`` .

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``RegexPatternSet`` before inspecting a request for a
      match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system commandline
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **RegexPatternSetId** *(string) --*

      The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
      get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
      ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
      ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
      and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

       ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
       ListRegexPatternSets .
    """


_ClientGetRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetTypeDef
):
    """
    Type definition for `ClientGetRegexMatchSetResponse` `RegexMatchSet`

    Information about the  RegexMatchSet that you specified in the ``GetRegexMatchSet`` request.
    For more information, see  RegexMatchTuple .

    - **RegexMatchSetId** *(string) --*

      The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
      information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
      (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
      a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
      DeleteRegexMatchSet ).

       ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you
      create a ``RegexMatchSet`` .

    - **RegexMatchTuples** *(list) --*

      Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains:

      * The part of a web request that you want AWS WAF to inspect, such as a query string or the
      value of the ``User-Agent`` header.

      * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
      For more information, see  RegexPatternSet .

      * Whether to perform any conversions on the request, such as converting it to lowercase,
      before inspecting it for the specified string.

      - *(dict) --*

        The regular expression pattern that you want AWS WAF to search for in web requests, the
        location in requests that you want AWS WAF to search, and other settings. Each
        ``RegexMatchTuple`` object contains:

        * The part of a web request that you want AWS WAF to inspect, such as a query string or
        the value of the ``User-Agent`` header.

        * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
        For more information, see  RegexPatternSet .

        * Whether to perform any conversions on the request, such as converting it to lowercase,
        before inspecting it for the specified string.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for the ``RegexPatternSet`` .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``RegexPatternSet`` before inspecting a request for a
          match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system commandline
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

        - **RegexPatternSetId** *(string) --*

          The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
          get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
          ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
          ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
          and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

           ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
           ListRegexPatternSets .
    """


_ClientGetRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseTypeDef",
    {"RegexMatchSet": ClientGetRegexMatchSetResponseRegexMatchSetTypeDef},
    total=False,
)


class ClientGetRegexMatchSetResponseTypeDef(_ClientGetRegexMatchSetResponseTypeDef):
    """
    Type definition for `ClientGetRegexMatchSet` `Response`

    - **RegexMatchSet** *(dict) --*

      Information about the  RegexMatchSet that you specified in the ``GetRegexMatchSet`` request.
      For more information, see  RegexMatchTuple .

      - **RegexMatchSetId** *(string) --*

        The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
        information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
        (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
        a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
        DeleteRegexMatchSet ).

         ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

      - **Name** *(string) --*

        A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you
        create a ``RegexMatchSet`` .

      - **RegexMatchTuples** *(list) --*

        Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains:

        * The part of a web request that you want AWS WAF to inspect, such as a query string or the
        value of the ``User-Agent`` header.

        * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
        For more information, see  RegexPatternSet .

        * Whether to perform any conversions on the request, such as converting it to lowercase,
        before inspecting it for the specified string.

        - *(dict) --*

          The regular expression pattern that you want AWS WAF to search for in web requests, the
          location in requests that you want AWS WAF to search, and other settings. Each
          ``RegexMatchTuple`` object contains:

          * The part of a web request that you want AWS WAF to inspect, such as a query string or
          the value of the ``User-Agent`` header.

          * The identifier of the pattern (a regular expression) that you want AWS WAF to look for.
          For more information, see  RegexPatternSet .

          * Whether to perform any conversions on the request, such as converting it to lowercase,
          before inspecting it for the specified string.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for the ``RegexPatternSet`` .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``RegexPatternSet`` before inspecting a request for a
            match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system commandline
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

          - **RegexPatternSetId** *(string) --*

            The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
            get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
            ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
            ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ),
            and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

             ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by
             ListRegexPatternSets .
    """


_ClientGetRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "_ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)


class ClientGetRegexPatternSetResponseRegexPatternSetTypeDef(
    _ClientGetRegexPatternSetResponseRegexPatternSetTypeDef
):
    """
    Type definition for `ClientGetRegexPatternSetResponse` `RegexPatternSet`

    Information about the  RegexPatternSet that you specified in the ``GetRegexPatternSet``
    request, including the identifier of the pattern set and the regular expression patterns you
    want AWS WAF to search for.

    - **RegexPatternSetId** *(string) --*

      The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
      information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
      ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
      WAF.

       ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
      you create a ``RegexPatternSet`` .

    - **RegexPatternStrings** *(list) --*

      Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such
      as ``B[a@]dB[o0]t`` .

      - *(string) --*
    """


_ClientGetRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientGetRegexPatternSetResponseTypeDef",
    {"RegexPatternSet": ClientGetRegexPatternSetResponseRegexPatternSetTypeDef},
    total=False,
)


class ClientGetRegexPatternSetResponseTypeDef(_ClientGetRegexPatternSetResponseTypeDef):
    """
    Type definition for `ClientGetRegexPatternSet` `Response`

    - **RegexPatternSet** *(dict) --*

      Information about the  RegexPatternSet that you specified in the ``GetRegexPatternSet``
      request, including the identifier of the pattern set and the regular expression patterns you
      want AWS WAF to search for.

      - **RegexPatternSetId** *(string) --*

        The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
        information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
        ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
        WAF.

         ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

      - **Name** *(string) --*

        A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
        you create a ``RegexPatternSet`` .

      - **RegexPatternStrings** *(list) --*

        Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such
        as ``B[a@]dB[o0]t`` .

        - *(string) --*
    """


_ClientGetRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "_ClientGetRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientGetRuleGroupResponseRuleGroupTypeDef(
    _ClientGetRuleGroupResponseRuleGroupTypeDef
):
    """
    Type definition for `ClientGetRuleGroupResponse` `RuleGroup`

    Information about the  RuleGroup that you specified in the ``GetRuleGroup`` request.

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
      about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
      insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
      UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

       ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

    - **Name** *(string) --*

      The friendly name or description for the ``RuleGroup`` . You can't change the name of a
      ``RuleGroup`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``RuleGroup`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RuleGroup`` .
    """


_ClientGetRuleGroupResponseTypeDef = TypedDict(
    "_ClientGetRuleGroupResponseTypeDef",
    {"RuleGroup": ClientGetRuleGroupResponseRuleGroupTypeDef},
    total=False,
)


class ClientGetRuleGroupResponseTypeDef(_ClientGetRuleGroupResponseTypeDef):
    """
    Type definition for `ClientGetRuleGroup` `Response`

    - **RuleGroup** *(dict) --*

      Information about the  RuleGroup that you specified in the ``GetRuleGroup`` request.

      - **RuleGroupId** *(string) --*

        A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
        about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
        insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
        UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

         ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

      - **Name** *(string) --*

        The friendly name or description for the ``RuleGroup`` . You can't change the name of a
        ``RuleGroup`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``RuleGroup`` . The name can
        contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
        length one. It can't contain whitespace or metric names reserved for AWS WAF, including
        "All" and "Default_Action." You can't change the name of the metric after you create the
        ``RuleGroup`` .
    """


_ClientGetRuleResponseRulePredicatesTypeDef = TypedDict(
    "_ClientGetRuleResponseRulePredicatesTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
    total=False,
)


class ClientGetRuleResponseRulePredicatesTypeDef(
    _ClientGetRuleResponseRulePredicatesTypeDef
):
    """
    Type definition for `ClientGetRuleResponseRule` `Predicates`

    Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
    RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
    ``Rule`` and, for each object, indicates whether you want to negate the settings, for
    example, requests that do NOT originate from the IP address 192.0.2.44.

    - **Negated** *(boolean) --*

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
      based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
       XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
       an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
       requests based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
      the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
      an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
      count requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --*

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --*

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientGetRuleResponseRuleTypeDef = TypedDict(
    "_ClientGetRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientGetRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)


class ClientGetRuleResponseRuleTypeDef(_ClientGetRuleResponseRuleTypeDef):
    """
    Type definition for `ClientGetRuleResponse` `Rule`

    Information about the  Rule that you specified in the ``GetRule`` request. For more
    information, see the following topics:

    *  Rule : Contains ``MetricName`` , ``Name`` , an array of ``Predicate`` objects, and
    ``RuleId``

    *  Predicate : Each ``Predicate`` object contains ``DataId`` , ``Negated`` , and ``Type``

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule``
      after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``Rule`` . The name can contain
      only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
      one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
      "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .

    - **Predicates** *(list) --*

      The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
      IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

      - *(dict) --*

        Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
        RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
        ``Rule`` and, for each object, indicates whether you want to negate the settings, for
        example, requests that do NOT originate from the IP address 192.0.2.44.

        - **Negated** *(boolean) --*

          Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
          based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
           XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
           an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
           requests based on that IP address.

          Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
          the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
          XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
          an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
          count requests based on all IP addresses *except*  ``192.0.2.44`` .

        - **Type** *(string) --*

          The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

        - **DataId** *(string) --*

          A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
          ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientGetRuleResponseTypeDef = TypedDict(
    "_ClientGetRuleResponseTypeDef",
    {"Rule": ClientGetRuleResponseRuleTypeDef},
    total=False,
)


class ClientGetRuleResponseTypeDef(_ClientGetRuleResponseTypeDef):
    """
    Type definition for `ClientGetRule` `Response`

    - **Rule** *(dict) --*

      Information about the  Rule that you specified in the ``GetRule`` request. For more
      information, see the following topics:

      *  Rule : Contains ``MetricName`` , ``Name`` , an array of ``Predicate`` objects, and
      ``RuleId``

      *  Predicate : Each ``Predicate`` object contains ``DataId`` , ``Negated`` , and ``Type``

      - **RuleId** *(string) --*

        A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
        ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
        ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
        from AWS WAF (see  DeleteRule ).

         ``RuleId`` is returned by  CreateRule and by  ListRules .

      - **Name** *(string) --*

        The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule``
        after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``Rule`` . The name can contain
        only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
        one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
        "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .

      - **Predicates** *(list) --*

        The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,
        IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

        - *(dict) --*

          Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,
          RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a
          ``Rule`` and, for each object, indicates whether you want to negate the settings, for
          example, requests that do NOT originate from the IP address 192.0.2.44.

          - **Negated** *(boolean) --*

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests
            based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
             XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
             an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block
             requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on
            the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
            XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if
            an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or
            count requests based on all IP addresses *except*  ``192.0.2.44`` .

          - **Type** *(string) --*

            The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

          - **DataId** *(string) --*

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
            ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef
):
    """
    Type definition for `ClientGetSampledRequestsResponseSampledRequestsRequest` `Headers`

    The response from a  GetSampledRequests request includes an ``HTTPHeader`` complex
    type that appears as ``Headers`` in the response syntax. ``HTTPHeader`` contains the
    names and values of all of the headers that appear in one of the web requests that
    were returned by ``GetSampledRequests`` .

    - **Name** *(string) --*

      The name of one of the headers in the sampled web request.

    - **Value** *(string) --*

      The value of one of the headers in the sampled web request.
    """


_ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List[
            ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef
        ],
    },
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef
):
    """
    Type definition for `ClientGetSampledRequestsResponseSampledRequests` `Request`

    A complex type that contains detailed information about the request.

    - **ClientIP** *(string) --*

      The IP address that the request originated from. If the ``WebACL`` is associated with a
      CloudFront distribution, this is the value of one of the following fields in CloudFront
      access logs:

      * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the
      request

      * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send
      the request

    - **Country** *(string) --*

      The two-letter country code for the country that the request originated from. For a
      current list of country codes, see the Wikipedia entry `ISO 3166-1 alpha-2
      <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

    - **URI** *(string) --*

      The part of a web request that identifies the resource, for example,
      ``/images/daily-ad.jpg`` .

    - **Method** *(string) --*

      The HTTP method specified in the sampled web request. CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

    - **HTTPVersion** *(string) --*

      The HTTP version specified in the sampled web request, for example, ``HTTP/1.1`` .

    - **Headers** *(list) --*

      A complex type that contains two values for each header in the sampled web request: the
      name of the header and the value of the header.

      - *(dict) --*

        The response from a  GetSampledRequests request includes an ``HTTPHeader`` complex
        type that appears as ``Headers`` in the response syntax. ``HTTPHeader`` contains the
        names and values of all of the headers that appear in one of the web requests that
        were returned by ``GetSampledRequests`` .

        - **Name** *(string) --*

          The name of one of the headers in the sampled web request.

        - **Value** *(string) --*

          The value of one of the headers in the sampled web request.
    """


_ClientGetSampledRequestsResponseSampledRequestsTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    {
        "Request": ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef,
        "Weight": int,
        "Timestamp": datetime,
        "Action": str,
        "RuleWithinRuleGroup": str,
    },
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsTypeDef
):
    """
    Type definition for `ClientGetSampledRequestsResponse` `SampledRequests`

    The response from a  GetSampledRequests request includes a ``SampledHTTPRequests`` complex
    type that appears as ``SampledRequests`` in the response syntax. ``SampledHTTPRequests``
    contains one ``SampledHTTPRequest`` object for each web request that is returned by
    ``GetSampledRequests`` .

    - **Request** *(dict) --*

      A complex type that contains detailed information about the request.

      - **ClientIP** *(string) --*

        The IP address that the request originated from. If the ``WebACL`` is associated with a
        CloudFront distribution, this is the value of one of the following fields in CloudFront
        access logs:

        * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the
        request

        * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send
        the request

      - **Country** *(string) --*

        The two-letter country code for the country that the request originated from. For a
        current list of country codes, see the Wikipedia entry `ISO 3166-1 alpha-2
        <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

      - **URI** *(string) --*

        The part of a web request that identifies the resource, for example,
        ``/images/daily-ad.jpg`` .

      - **Method** *(string) --*

        The HTTP method specified in the sampled web request. CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

      - **HTTPVersion** *(string) --*

        The HTTP version specified in the sampled web request, for example, ``HTTP/1.1`` .

      - **Headers** *(list) --*

        A complex type that contains two values for each header in the sampled web request: the
        name of the header and the value of the header.

        - *(dict) --*

          The response from a  GetSampledRequests request includes an ``HTTPHeader`` complex
          type that appears as ``Headers`` in the response syntax. ``HTTPHeader`` contains the
          names and values of all of the headers that appear in one of the web requests that
          were returned by ``GetSampledRequests`` .

          - **Name** *(string) --*

            The name of one of the headers in the sampled web request.

          - **Value** *(string) --*

            The value of one of the headers in the sampled web request.

    - **Weight** *(integer) --*

      A value that indicates how one result in the response relates proportionally to other
      results in the response. A result that has a weight of ``2`` represents roughly twice as
      many CloudFront web requests as a result that has a weight of ``1`` .

    - **Timestamp** *(datetime) --*

      The time at which AWS WAF received the request from your AWS resource, in Unix time
      format (in seconds).

    - **Action** *(string) --*

      The action for the ``Rule`` that the request matched: ``ALLOW`` , ``BLOCK`` , or
      ``COUNT`` .

    - **RuleWithinRuleGroup** *(string) --*

      This value is returned if the ``GetSampledRequests`` request specifies the ID of a
      ``RuleGroup`` rather than the ID of an individual rule. ``RuleWithinRuleGroup`` is the
      rule within the specified ``RuleGroup`` that matched the request listed in the response.
    """


_ClientGetSampledRequestsResponseTimeWindowTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseTimeWindowTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientGetSampledRequestsResponseTimeWindowTypeDef(
    _ClientGetSampledRequestsResponseTimeWindowTypeDef
):
    """
    Type definition for `ClientGetSampledRequestsResponse` `TimeWindow`

    Usually, ``TimeWindow`` is the time range that you specified in the ``GetSampledRequests``
    request. However, if your AWS resource received more than 5,000 requests during the time
    range that you specified in the request, ``GetSampledRequests`` returns the time range for
    the first 5,000 requests.

    - **StartTime** *(datetime) --*

      The beginning of the time range from which you want ``GetSampledRequests`` to return a
      sample of the requests that your AWS resource received. Specify the date and time in the
      following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous
      three hours.

    - **EndTime** *(datetime) --*

      The end of the time range from which you want ``GetSampledRequests`` to return a sample of
      the requests that your AWS resource received. Specify the date and time in the following
      format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three
      hours.
    """


_ClientGetSampledRequestsResponseTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List[ClientGetSampledRequestsResponseSampledRequestsTypeDef],
        "PopulationSize": int,
        "TimeWindow": ClientGetSampledRequestsResponseTimeWindowTypeDef,
    },
    total=False,
)


class ClientGetSampledRequestsResponseTypeDef(_ClientGetSampledRequestsResponseTypeDef):
    """
    Type definition for `ClientGetSampledRequests` `Response`

    - **SampledRequests** *(list) --*

      A complex type that contains detailed information about each of the requests in the sample.

      - *(dict) --*

        The response from a  GetSampledRequests request includes a ``SampledHTTPRequests`` complex
        type that appears as ``SampledRequests`` in the response syntax. ``SampledHTTPRequests``
        contains one ``SampledHTTPRequest`` object for each web request that is returned by
        ``GetSampledRequests`` .

        - **Request** *(dict) --*

          A complex type that contains detailed information about the request.

          - **ClientIP** *(string) --*

            The IP address that the request originated from. If the ``WebACL`` is associated with a
            CloudFront distribution, this is the value of one of the following fields in CloudFront
            access logs:

            * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the
            request

            * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send
            the request

          - **Country** *(string) --*

            The two-letter country code for the country that the request originated from. For a
            current list of country codes, see the Wikipedia entry `ISO 3166-1 alpha-2
            <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

          - **URI** *(string) --*

            The part of a web request that identifies the resource, for example,
            ``/images/daily-ad.jpg`` .

          - **Method** *(string) --*

            The HTTP method specified in the sampled web request. CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

          - **HTTPVersion** *(string) --*

            The HTTP version specified in the sampled web request, for example, ``HTTP/1.1`` .

          - **Headers** *(list) --*

            A complex type that contains two values for each header in the sampled web request: the
            name of the header and the value of the header.

            - *(dict) --*

              The response from a  GetSampledRequests request includes an ``HTTPHeader`` complex
              type that appears as ``Headers`` in the response syntax. ``HTTPHeader`` contains the
              names and values of all of the headers that appear in one of the web requests that
              were returned by ``GetSampledRequests`` .

              - **Name** *(string) --*

                The name of one of the headers in the sampled web request.

              - **Value** *(string) --*

                The value of one of the headers in the sampled web request.

        - **Weight** *(integer) --*

          A value that indicates how one result in the response relates proportionally to other
          results in the response. A result that has a weight of ``2`` represents roughly twice as
          many CloudFront web requests as a result that has a weight of ``1`` .

        - **Timestamp** *(datetime) --*

          The time at which AWS WAF received the request from your AWS resource, in Unix time
          format (in seconds).

        - **Action** *(string) --*

          The action for the ``Rule`` that the request matched: ``ALLOW`` , ``BLOCK`` , or
          ``COUNT`` .

        - **RuleWithinRuleGroup** *(string) --*

          This value is returned if the ``GetSampledRequests`` request specifies the ID of a
          ``RuleGroup`` rather than the ID of an individual rule. ``RuleWithinRuleGroup`` is the
          rule within the specified ``RuleGroup`` that matched the request listed in the response.

    - **PopulationSize** *(integer) --*

      The total number of requests from which ``GetSampledRequests`` got a sample of ``MaxItems``
      requests. If ``PopulationSize`` is less than ``MaxItems`` , the sample includes every request
      that your AWS resource received during the specified time range.

    - **TimeWindow** *(dict) --*

      Usually, ``TimeWindow`` is the time range that you specified in the ``GetSampledRequests``
      request. However, if your AWS resource received more than 5,000 requests during the time
      range that you specified in the request, ``GetSampledRequests`` returns the time range for
      the first 5,000 requests.

      - **StartTime** *(datetime) --*

        The beginning of the time range from which you want ``GetSampledRequests`` to return a
        sample of the requests that your AWS resource received. Specify the date and time in the
        following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous
        three hours.

      - **EndTime** *(datetime) --*

        The end of the time range from which you want ``GetSampledRequests`` to return a sample of
        the requests that your AWS resource received. Specify the date and time in the following
        format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three
        hours.
    """


_ClientGetSampledRequestsTimeWindowTypeDef = TypedDict(
    "_ClientGetSampledRequestsTimeWindowTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
)


class ClientGetSampledRequestsTimeWindowTypeDef(
    _ClientGetSampledRequestsTimeWindowTypeDef
):
    """
    Type definition for `ClientGetSampledRequests` `TimeWindow`

    The start date and time and the end date and time of the range for which you want
    ``GetSampledRequests`` to return a sample of requests. Specify the date and time in the following
    format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

    - **StartTime** *(datetime) --* **[REQUIRED]**

      The beginning of the time range from which you want ``GetSampledRequests`` to return a sample
      of the requests that your AWS resource received. Specify the date and time in the following
      format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

    - **EndTime** *(datetime) --* **[REQUIRED]**

      The end of the time range from which you want ``GetSampledRequests`` to return a sample of the
      requests that your AWS resource received. Specify the date and time in the following format:
      ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.
    """


_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef
):
    """
    Type definition for `ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraints` `FieldToMatch`

    Specifies where in a web request to look for the size constraint.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": str,
        "ComparisonOperator": str,
        "Size": int,
    },
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
):
    """
    Type definition for `ClientGetSizeConstraintSetResponseSizeConstraintSet` `SizeConstraints`

    Specifies a constraint on the size of a part of the web request. AWS WAF uses the
    ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
    form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
    expression is true, the ``SizeConstraint`` is considered to match.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for the size constraint.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

      Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
      for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
      inspection.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

    - **ComparisonOperator** *(string) --*

      The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
      with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
      "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
      expression is true, the ``SizeConstraint`` is considered to match.

       **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

       **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

       **LE** : Used to test if the ``Size`` is less than or equal to the size of the
       ``FieldToMatch``

       **LT** : Used to test if the ``Size`` is strictly less than the size of the
       ``FieldToMatch``

       **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
       ``FieldToMatch``

       **GT** : Used to test if the ``Size`` is strictly greater than the size of the
       ``FieldToMatch``

    - **Size** *(integer) --*

      The size in bytes that you want AWS WAF to compare against the size of the specified
      ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
      ``FieldToMatch`` to build an expression in the form of "``Size``
      ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
      the ``SizeConstraint`` is considered to match.

      Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

      If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
      character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef
):
    """
    Type definition for `ClientGetSizeConstraintSetResponse` `SizeConstraintSet`

    Information about the  SizeConstraintSet that you specified in the ``GetSizeConstraintSet``
    request. For more information, see the following topics:

    *  SizeConstraintSet : Contains ``SizeConstraintSetId`` , ``SizeConstraints`` , and ``Name``

    * ``SizeConstraints`` : Contains an array of  SizeConstraint objects. Each ``SizeConstraint``
    object contains  FieldToMatch , ``TextTransformation`` , ``ComparisonOperator`` , and ``Size``

    *  FieldToMatch : Contains ``Data`` and ``Type``

    - **SizeConstraintSetId** *(string) --*

      A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
      information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
      ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
      a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
      ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

       ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
       ListSizeConstraintSets .

    - **Name** *(string) --*

      The name, if any, of the ``SizeConstraintSet`` .

    - **SizeConstraints** *(list) --*

      Specifies the parts of web requests that you want to inspect the size of.

      - *(dict) --*

        Specifies a constraint on the size of a part of the web request. AWS WAF uses the
        ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
        form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
        expression is true, the ``SizeConstraint`` is considered to match.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for the size constraint.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

          Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
          for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
          inspection.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

        - **ComparisonOperator** *(string) --*

          The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
          with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
          "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
          expression is true, the ``SizeConstraint`` is considered to match.

           **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

           **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

           **LE** : Used to test if the ``Size`` is less than or equal to the size of the
           ``FieldToMatch``

           **LT** : Used to test if the ``Size`` is strictly less than the size of the
           ``FieldToMatch``

           **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
           ``FieldToMatch``

           **GT** : Used to test if the ``Size`` is strictly greater than the size of the
           ``FieldToMatch``

        - **Size** *(integer) --*

          The size in bytes that you want AWS WAF to compare against the size of the specified
          ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
          ``FieldToMatch`` to build an expression in the form of "``Size``
          ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
          the ``SizeConstraint`` is considered to match.

          Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

          If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
          character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientGetSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseTypeDef",
    {"SizeConstraintSet": ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef},
    total=False,
)


class ClientGetSizeConstraintSetResponseTypeDef(
    _ClientGetSizeConstraintSetResponseTypeDef
):
    """
    Type definition for `ClientGetSizeConstraintSet` `Response`

    - **SizeConstraintSet** *(dict) --*

      Information about the  SizeConstraintSet that you specified in the ``GetSizeConstraintSet``
      request. For more information, see the following topics:

      *  SizeConstraintSet : Contains ``SizeConstraintSetId`` , ``SizeConstraints`` , and ``Name``

      * ``SizeConstraints`` : Contains an array of  SizeConstraint objects. Each ``SizeConstraint``
      object contains  FieldToMatch , ``TextTransformation`` , ``ComparisonOperator`` , and ``Size``

      *  FieldToMatch : Contains ``Data`` and ``Type``

      - **SizeConstraintSetId** *(string) --*

        A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
        information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
        ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
        a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
        ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

         ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
         ListSizeConstraintSets .

      - **Name** *(string) --*

        The name, if any, of the ``SizeConstraintSet`` .

      - **SizeConstraints** *(list) --*

        Specifies the parts of web requests that you want to inspect the size of.

        - *(dict) --*

          Specifies a constraint on the size of a part of the web request. AWS WAF uses the
          ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the
          form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
          expression is true, the ``SizeConstraint`` is considered to match.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for the size constraint.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

            Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE``
            for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for
            inspection.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

          - **ComparisonOperator** *(string) --*

            The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination
            with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of
            "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that
            expression is true, the ``SizeConstraint`` is considered to match.

             **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

             **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

             **LE** : Used to test if the ``Size`` is less than or equal to the size of the
             ``FieldToMatch``

             **LT** : Used to test if the ``Size`` is strictly less than the size of the
             ``FieldToMatch``

             **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
             ``FieldToMatch``

             **GT** : Used to test if the ``Size`` is strictly greater than the size of the
             ``FieldToMatch``

          - **Size** *(integer) --*

            The size in bytes that you want AWS WAF to compare against the size of the specified
            ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
            ``FieldToMatch`` to build an expression in the form of "``Size``
            ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true,
            the ``SizeConstraint`` is considered to match.

            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

            If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
            character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for snippets of malicious SQL code.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
):
    """
    Type definition for `ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSet` `SqlInjectionMatchTuples`

    Specifies the part of a web request that you want AWS WAF to inspect for snippets of
    malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for snippets of malicious SQL code.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef
):
    """
    Type definition for `ClientGetSqlInjectionMatchSetResponse` `SqlInjectionMatchSet`

    Information about the  SqlInjectionMatchSet that you specified in the
    ``GetSqlInjectionMatchSet`` request. For more information, see the following topics:

    *  SqlInjectionMatchSet : Contains ``Name`` , ``SqlInjectionMatchSetId`` , and an array of
    ``SqlInjectionMatchTuple`` objects

    *  SqlInjectionMatchTuple : Each ``SqlInjectionMatchTuple`` object contains ``FieldToMatch``
    and ``TextTransformation``

    *  FieldToMatch : Contains ``Data`` and ``Type``

    - **SqlInjectionMatchSetId** *(string) --*

      A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
      get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
      ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
      ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
      and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

       ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
       ListSqlInjectionMatchSets .

    - **Name** *(string) --*

      The name, if any, of the ``SqlInjectionMatchSet`` .

    - **SqlInjectionMatchTuples** *(list) --*

      Specifies the parts of web requests that you want to inspect for snippets of malicious SQL
      code.

      - *(dict) --*

        Specifies the part of a web request that you want AWS WAF to inspect for snippets of
        malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for snippets of malicious SQL code.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientGetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseTypeDef(
    _ClientGetSqlInjectionMatchSetResponseTypeDef
):
    """
    Type definition for `ClientGetSqlInjectionMatchSet` `Response`

    The response to a  GetSqlInjectionMatchSet request.

    - **SqlInjectionMatchSet** *(dict) --*

      Information about the  SqlInjectionMatchSet that you specified in the
      ``GetSqlInjectionMatchSet`` request. For more information, see the following topics:

      *  SqlInjectionMatchSet : Contains ``Name`` , ``SqlInjectionMatchSetId`` , and an array of
      ``SqlInjectionMatchTuple`` objects

      *  SqlInjectionMatchTuple : Each ``SqlInjectionMatchTuple`` object contains ``FieldToMatch``
      and ``TextTransformation``

      *  FieldToMatch : Contains ``Data`` and ``Type``

      - **SqlInjectionMatchSetId** *(string) --*

        A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
        get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
        ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
        ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
        and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

         ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
         ListSqlInjectionMatchSets .

      - **Name** *(string) --*

        The name, if any, of the ``SqlInjectionMatchSet`` .

      - **SqlInjectionMatchTuples** *(list) --*

        Specifies the parts of web requests that you want to inspect for snippets of malicious SQL
        code.

        - *(dict) --*

          Specifies the part of a web request that you want AWS WAF to inspect for snippets of
          malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for snippets of malicious SQL code.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientGetWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLDefaultActionTypeDef", {"Type": str}, total=False
)


class ClientGetWebAclResponseWebACLDefaultActionTypeDef(
    _ClientGetWebAclResponseWebACLDefaultActionTypeDef
):
    """
    Type definition for `ClientGetWebAclResponseWebACL` `DefaultAction`

    The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
    action is specified by the  WafAction object.

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
      ``WebACL`` .
    """


_ClientGetWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesActionTypeDef", {"Type": str}, total=False
)


class ClientGetWebAclResponseWebACLRulesActionTypeDef(
    _ClientGetWebAclResponseWebACLRulesActionTypeDef
):
    """
    Type definition for `ClientGetWebAclResponseWebACLRules` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the
    web ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
     to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
     other update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on
      the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
      action for a ``WebACL`` .
    """


_ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)


class ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef(
    _ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef
):
    """
    Type definition for `ClientGetWebAclResponseWebACLRules` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the
    ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
    ``RuleGroup`` that is specified by the ``ActivatedRule`` .

    - **RuleId** *(string) --*

      The unique identifier for the rule to exclude from the rule group.
    """


_ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)


class ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef(
    _ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef
):
    """
    Type definition for `ClientGetWebAclResponseWebACLRules` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
    individual rule in the ``RuleGroup`` matches the request and is configured to block
    that request. However if you first want to test the ``RuleGroup`` , set the
    ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
    specified by individual rules contained within the group. Instead of blocking matching
    requests, those requests will be counted. You can view a record of counted requests
    using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
     to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

       ``COUNT`` overrides the action specified by the individual rule within a
       ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.
    """


_ClientGetWebAclResponseWebACLRulesTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientGetWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef],
    },
    total=False,
)


class ClientGetWebAclResponseWebACLRulesTypeDef(
    _ClientGetWebAclResponseWebACLRulesTypeDef
):
    """
    Type definition for `ClientGetWebAclResponseWebACL` `Rules`

    The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
    want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
    that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
    ``BLOCK`` , or ``COUNT`` ).

    To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
    WebACLUpdate data type.

    - **Priority** *(integer) --*

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
      value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
      values don't need to be consecutive.

    - **RuleId** *(string) --*

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
      a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
      ``Rule`` from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the
      web ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
       to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
       other update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on
        the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
        action for a ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
      individual rule in the ``RuleGroup`` matches the request and is configured to block
      that request. However if you first want to test the ``RuleGroup`` , set the
      ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
      specified by individual rules contained within the group. Instead of blocking matching
      requests, those requests will be counted. You can view a record of counted requests
      using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
       to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

         ``COUNT`` overrides the action specified by the individual rule within a
         ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
      by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
      Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
      web ACL without setting the type, the  UpdateWebACL request will fail because the
      request tries to add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the
      specific rule within the rule group that is blocking the legitimate traffic and then
      disable (exclude) that particular rule. You can exclude rules from both your own rule
      groups and AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
      it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
      COUNT metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web
      ACL, perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
      more information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
        that you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
        ``RuleGroup`` that is specified by the ``ActivatedRule`` .

        - **RuleId** *(string) --*

          The unique identifier for the rule to exclude from the rule group.
    """


_ClientGetWebAclResponseWebACLTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientGetWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientGetWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)


class ClientGetWebAclResponseWebACLTypeDef(_ClientGetWebAclResponseWebACLTypeDef):
    """
    Type definition for `ClientGetWebAclResponse` `WebACL`

    Information about the  WebACL that you specified in the ``GetWebACL`` request. For more
    information, see the following topics:

    *  WebACL : Contains ``DefaultAction`` , ``MetricName`` , ``Name`` , an array of ``Rule``
    objects, and ``WebACLId``

    * ``DefaultAction`` (Data type is  WafAction ): Contains ``Type``

    * ``Rules`` : Contains an array of ``ActivatedRule`` objects, which contain ``Action`` ,
    ``Priority`` , and ``RuleId``

    * ``Action`` : Contains ``Type``

    - **WebACLId** *(string) --*

      A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
      ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
      ``WebACL`` from AWS WAF (see  DeleteWebACL ).

       ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

    - **Name** *(string) --*

      A friendly name or description of the ``WebACL`` . You can't change the name of a
      ``WebACL`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``WebACL`` . The name can contain
      only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
      one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
      "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .

    - **DefaultAction** *(dict) --*

      The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
      action is specified by the  WafAction object.

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
        ``WebACL`` .

    - **Rules** *(list) --*

      An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the
      ``Rule`` , and the ID of the ``Rule`` .

      - *(dict) --*

        The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
        want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
        that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
        ``BLOCK`` , or ``COUNT`` ).

        To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
        WebACLUpdate data type.

        - **Priority** *(integer) --*

          Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
          lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
          value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
          values don't need to be consecutive.

        - **RuleId** *(string) --*

          The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
          a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
          ``Rule`` from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Action** *(dict) --*

          Specifies the action that CloudFront or AWS WAF takes when a web request matches the
          conditions in the ``Rule`` . Valid values for ``Action`` include the following:

          * ``ALLOW`` : CloudFront responds with the requested object.

          * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

          * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
          rule and then continues to inspect the web request based on the remaining rules in the
          web ACL.

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
           to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
           other update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

            Specifies how you want AWS WAF to respond to requests that match the settings in a
            ``Rule`` . Valid settings include the following:

            * ``ALLOW`` : AWS WAF allows requests

            * ``BLOCK`` : AWS WAF blocks requests

            * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
            conditions in the rule. AWS WAF then continues to inspect the web request based on
            the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
            action for a ``WebACL`` .

        - **OverrideAction** *(dict) --*

          Use the ``OverrideAction`` to test your ``RuleGroup`` .

          Any rule in a ``RuleGroup`` can potentially block a request. If you set the
          ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
          individual rule in the ``RuleGroup`` matches the request and is configured to block
          that request. However if you first want to test the ``RuleGroup`` , set the
          ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
          specified by individual rules contained within the group. Instead of blocking matching
          requests, those requests will be counted. You can view a record of counted requests
          using  GetSampledRequests .

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
           to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

             ``COUNT`` overrides the action specified by the individual rule within a
             ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

        - **Type** *(string) --*

          The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
          by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
          Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
          web ACL without setting the type, the  UpdateWebACL request will fail because the
          request tries to add a REGULAR rule with the specified ID, which does not exist.

        - **ExcludedRules** *(list) --*

          An array of rules to exclude from a rule group. This is applicable only when the
          ``ActivatedRule`` refers to a ``RuleGroup`` .

          Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
          unexpectedly (false positives). One troubleshooting technique is to identify the
          specific rule within the rule group that is blocking the legitimate traffic and then
          disable (exclude) that particular rule. You can exclude rules from both your own rule
          groups and AWS Marketplace rule groups that have been associated with a web ACL.

          Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
          it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
          ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
          COUNT metrics for each ``ExcludedRule`` .

          If you want to exclude rules from a rule group that is already associated with a web
          ACL, perform the following steps:

          * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
          more information about the logs, see `Logging Web ACL Traffic Information
          <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

          * Submit an  UpdateWebACL request that has two actions:

            * The first action deletes the existing rule group from the web ACL. That is, in the
            UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
            ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
            that you want to exclude.

            * The second action inserts the same rule group back in, but specifying the rules to
            exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
            ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
            ``ExcludedRules`` should contain the rules that you want to exclude.

          - *(dict) --*

            The rule to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
            ``RuleGroup`` that is specified by the ``ActivatedRule`` .

            - **RuleId** *(string) --*

              The unique identifier for the rule to exclude from the rule group.

    - **WebACLArn** *(string) --*

      Tha Amazon Resource Name (ARN) of the web ACL.
    """


_ClientGetWebAclResponseTypeDef = TypedDict(
    "_ClientGetWebAclResponseTypeDef",
    {"WebACL": ClientGetWebAclResponseWebACLTypeDef},
    total=False,
)


class ClientGetWebAclResponseTypeDef(_ClientGetWebAclResponseTypeDef):
    """
    Type definition for `ClientGetWebAcl` `Response`

    - **WebACL** *(dict) --*

      Information about the  WebACL that you specified in the ``GetWebACL`` request. For more
      information, see the following topics:

      *  WebACL : Contains ``DefaultAction`` , ``MetricName`` , ``Name`` , an array of ``Rule``
      objects, and ``WebACLId``

      * ``DefaultAction`` (Data type is  WafAction ): Contains ``Type``

      * ``Rules`` : Contains an array of ``ActivatedRule`` objects, which contain ``Action`` ,
      ``Priority`` , and ``RuleId``

      * ``Action`` : Contains ``Type``

      - **WebACLId** *(string) --*

        A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
        ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
        ``WebACL`` from AWS WAF (see  DeleteWebACL ).

         ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

      - **Name** *(string) --*

        A friendly name or description of the ``WebACL`` . You can't change the name of a
        ``WebACL`` after you create it.

      - **MetricName** *(string) --*

        A friendly name or description for the metrics for this ``WebACL`` . The name can contain
        only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length
        one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and
        "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .

      - **DefaultAction** *(dict) --*

        The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The
        action is specified by the  WafAction object.

        - **Type** *(string) --*

          Specifies how you want AWS WAF to respond to requests that match the settings in a
          ``Rule`` . Valid settings include the following:

          * ``ALLOW`` : AWS WAF allows requests

          * ``BLOCK`` : AWS WAF blocks requests

          * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
          conditions in the rule. AWS WAF then continues to inspect the web request based on the
          remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
          ``WebACL`` .

      - **Rules** *(list) --*

        An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the
        ``Rule`` , and the ID of the ``Rule`` .

        - *(dict) --*

          The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you
          want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action
          that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` ,
          ``BLOCK`` , or ``COUNT`` ).

          To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
          WebACLUpdate data type.

          - **Priority** *(integer) --*

            Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
            lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
            value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
            values don't need to be consecutive.

          - **RuleId** *(string) --*

            The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
            ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into
            a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a
            ``Rule`` from AWS WAF (see  DeleteRule ).

             ``RuleId`` is returned by  CreateRule and by  ListRules .

          - **Action** *(dict) --*

            Specifies the action that CloudFront or AWS WAF takes when a web request matches the
            conditions in the ``Rule`` . Valid values for ``Action`` include the following:

            * ``ALLOW`` : CloudFront responds with the requested object.

            * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

            * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
            rule and then continues to inspect the web request based on the remaining rules in the
            web ACL.

             ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
             to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all
             other update requests, ``ActivatedRule|Action`` is used instead of
             ``ActivatedRule|OverrideAction`` .

            - **Type** *(string) --*

              Specifies how you want AWS WAF to respond to requests that match the settings in a
              ``Rule`` . Valid settings include the following:

              * ``ALLOW`` : AWS WAF allows requests

              * ``BLOCK`` : AWS WAF blocks requests

              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
              conditions in the rule. AWS WAF then continues to inspect the web request based on
              the remaining rules in the web ACL. You can't specify ``COUNT`` for the default
              action for a ``WebACL`` .

          - **OverrideAction** *(dict) --*

            Use the ``OverrideAction`` to test your ``RuleGroup`` .

            Any rule in a ``RuleGroup`` can potentially block a request. If you set the
            ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any
            individual rule in the ``RuleGroup`` matches the request and is configured to block
            that request. However if you first want to test the ``RuleGroup`` , set the
            ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action
            specified by individual rules contained within the group. Instead of blocking matching
            requests, those requests will be counted. You can view a record of counted requests
            using  GetSampledRequests .

             ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup``
             to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
             update requests, ``ActivatedRule|Action`` is used instead of
             ``ActivatedRule|OverrideAction`` .

            - **Type** *(string) --*

               ``COUNT`` overrides the action specified by the individual rule within a
               ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

          - **Type** *(string) --*

            The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined
            by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
            Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
            web ACL without setting the type, the  UpdateWebACL request will fail because the
            request tries to add a REGULAR rule with the specified ID, which does not exist.

          - **ExcludedRules** *(list) --*

            An array of rules to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` .

            Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
            unexpectedly (false positives). One troubleshooting technique is to identify the
            specific rule within the rule group that is blocking the legitimate traffic and then
            disable (exclude) that particular rule. You can exclude rules from both your own rule
            groups and AWS Marketplace rule groups that have been associated with a web ACL.

            Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather,
            it changes the action for the rules to ``COUNT`` . Therefore, requests that match an
            ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive
            COUNT metrics for each ``ExcludedRule`` .

            If you want to exclude rules from a rule group that is already associated with a web
            ACL, perform the following steps:

            * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
            more information about the logs, see `Logging Web ACL Traffic Information
            <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

            * Submit an  UpdateWebACL request that has two actions:

              * The first action deletes the existing rule group from the web ACL. That is, in the
              UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
              ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules
              that you want to exclude.

              * The second action inserts the same rule group back in, but specifying the rules to
              exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
              ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
              ``ExcludedRules`` should contain the rules that you want to exclude.

            - *(dict) --*

              The rule to exclude from a rule group. This is applicable only when the
              ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the
              ``RuleGroup`` that is specified by the ``ActivatedRule`` .

              - **RuleId** *(string) --*

                The unique identifier for the rule to exclude from the rule group.

      - **WebACLArn** *(string) --*

        Tha Amazon Resource Name (ARN) of the web ACL.
    """


_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef
):
    """
    Type definition for `ClientGetXssMatchSetResponseXssMatchSetXssMatchTuples` `FieldToMatch`

    Specifies where in a web request to look for cross-site scripting attacks.

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": str,
    },
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
):
    """
    Type definition for `ClientGetXssMatchSetResponseXssMatchSet` `XssMatchTuples`

    Specifies the part of a web request that you want AWS WAF to inspect for cross-site
    scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --*

      Specifies where in a web request to look for cross-site scripting attacks.

      - **Type** *(string) --*

        The part of the web request that you want AWS WAF to search for a specified string.
        Parts of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the
        ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
        the name of the header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the
        request is asking the origin to perform. Amazon CloudFront supports the following
        methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
        ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The
        request body immediately follows the request headers. Note that only the first
        ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
        or block requests based on the length of the body, you can create a size constraint
        set. For more information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
        such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
        30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value
        or regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
        AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
        header is not case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
        that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
        parameter name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --*

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
      performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line
      command and using unusual formatting to disguise some or all of the command, use this
      option to perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format,
      ``(ampersand)#xhhhh;`` , with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
      with the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientGetXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[
            ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetTypeDef
):
    """
    Type definition for `ClientGetXssMatchSetResponse` `XssMatchSet`

    Information about the  XssMatchSet that you specified in the ``GetXssMatchSet`` request. For
    more information, see the following topics:

    *  XssMatchSet : Contains ``Name`` , ``XssMatchSetId`` , and an array of ``XssMatchTuple``
    objects

    *  XssMatchTuple : Each ``XssMatchTuple`` object contains ``FieldToMatch`` and
    ``TextTransformation``

    *  FieldToMatch : Contains ``Data`` and ``Type``

    - **XssMatchSetId** *(string) --*

      A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
      about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
      UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
      DeleteXssMatchSet ).

       ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

    - **Name** *(string) --*

      The name, if any, of the ``XssMatchSet`` .

    - **XssMatchTuples** *(list) --*

      Specifies the parts of web requests that you want to inspect for cross-site scripting
      attacks.

      - *(dict) --*

        Specifies the part of a web request that you want AWS WAF to inspect for cross-site
        scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

        - **FieldToMatch** *(dict) --*

          Specifies where in a web request to look for cross-site scripting attacks.

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the
            ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
            the name of the header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the
            request is asking the origin to perform. Amazon CloudFront supports the following
            methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
            ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The
            request body immediately follows the request headers. Note that only the first
            ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
            or block requests based on the length of the body, you can create a size constraint
            set. For more information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
            such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
            30 characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value
            or regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
            header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

        - **TextTransformation** *(string) --*

          Text transformations eliminate some of the unusual formatting that attackers use in web
          requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
          performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

          You can only specify a single type of TextTransformation.

           **CMD_LINE**

          When you're concerned that attackers are injecting an operating system command line
          command and using unusual formatting to disguise some or all of the command, use this
          option to perform the following transformations:

          * Delete the following characters: \\ " ' ^

          * Delete spaces before the following characters: / (

          * Replace the following characters with a space: , ;

          * Replace multiple spaces with one space

          * Convert uppercase letters (A-Z) to lowercase (a-z)

           **COMPRESS_WHITE_SPACE**

          Use this option to replace the following characters with a space character (decimal 32):

          * \\f, formfeed, decimal 12

          * \\t, tab, decimal 9

          * \\n, newline, decimal 10

          * \\r, carriage return, decimal 13

          * \\v, vertical tab, decimal 11

          * non-breaking space, decimal 160

           ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

           **HTML_ENTITY_DECODE**

          Use this option to replace HTML-encoded characters with unencoded characters.
          ``HTML_ENTITY_DECODE`` performs the following operations:

          * Replaces ``(ampersand)quot;`` with ``"``

          * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

          * Replaces ``(ampersand)lt;`` with a "less than" symbol

          * Replaces ``(ampersand)gt;`` with ``>``

          * Replaces characters that are represented in hexadecimal format,
          ``(ampersand)#xhhhh;`` , with the corresponding characters

          * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
          with the corresponding characters

           **LOWERCASE**

          Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

           **URL_DECODE**

          Use this option to decode a URL-encoded value.

           **NONE**

          Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientGetXssMatchSetResponseTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseTypeDef",
    {"XssMatchSet": ClientGetXssMatchSetResponseXssMatchSetTypeDef},
    total=False,
)


class ClientGetXssMatchSetResponseTypeDef(_ClientGetXssMatchSetResponseTypeDef):
    """
    Type definition for `ClientGetXssMatchSet` `Response`

    The response to a  GetXssMatchSet request.

    - **XssMatchSet** *(dict) --*

      Information about the  XssMatchSet that you specified in the ``GetXssMatchSet`` request. For
      more information, see the following topics:

      *  XssMatchSet : Contains ``Name`` , ``XssMatchSetId`` , and an array of ``XssMatchTuple``
      objects

      *  XssMatchTuple : Each ``XssMatchTuple`` object contains ``FieldToMatch`` and
      ``TextTransformation``

      *  FieldToMatch : Contains ``Data`` and ``Type``

      - **XssMatchSetId** *(string) --*

        A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
        about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
        UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
        DeleteXssMatchSet ).

         ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

      - **Name** *(string) --*

        The name, if any, of the ``XssMatchSet`` .

      - **XssMatchTuples** *(list) --*

        Specifies the parts of web requests that you want to inspect for cross-site scripting
        attacks.

        - *(dict) --*

          Specifies the part of a web request that you want AWS WAF to inspect for cross-site
          scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

          - **FieldToMatch** *(dict) --*

            Specifies where in a web request to look for cross-site scripting attacks.

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

          - **TextTransformation** *(string) --*

            Text transformations eliminate some of the unusual formatting that attackers use in web
            requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF
            performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

             **CMD_LINE**

            When you're concerned that attackers are injecting an operating system command line
            command and using unusual formatting to disguise some or all of the command, use this
            option to perform the following transformations:

            * Delete the following characters: \\ " ' ^

            * Delete spaces before the following characters: / (

            * Replace the following characters with a space: , ;

            * Replace multiple spaces with one space

            * Convert uppercase letters (A-Z) to lowercase (a-z)

             **COMPRESS_WHITE_SPACE**

            Use this option to replace the following characters with a space character (decimal 32):

            * \\f, formfeed, decimal 12

            * \\t, tab, decimal 9

            * \\n, newline, decimal 10

            * \\r, carriage return, decimal 13

            * \\v, vertical tab, decimal 11

            * non-breaking space, decimal 160

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             **HTML_ENTITY_DECODE**

            Use this option to replace HTML-encoded characters with unencoded characters.
            ``HTML_ENTITY_DECODE`` performs the following operations:

            * Replaces ``(ampersand)quot;`` with ``"``

            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

            * Replaces ``(ampersand)lt;`` with a "less than" symbol

            * Replaces ``(ampersand)gt;`` with ``>``

            * Replaces characters that are represented in hexadecimal format,
            ``(ampersand)#xhhhh;`` , with the corresponding characters

            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` ,
            with the corresponding characters

             **LOWERCASE**

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             **URL_DECODE**

            Use this option to decode a URL-encoded value.

             **NONE**

            Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    {"Type": str},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef
):
    """
    Type definition for `ClientListActivatedRulesInRuleGroupResponseActivatedRules` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the
    web ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
     a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
      a ``WebACL`` .
    """


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef
):
    """
    Type definition for `ClientListActivatedRulesInRuleGroupResponseActivatedRules` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the
    ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
    that is specified by the ``ActivatedRule`` .

    - **RuleId** *(string) --*

      The unique identifier for the rule to exclude from the rule group.
    """


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef
):
    """
    Type definition for `ClientListActivatedRulesInRuleGroupResponseActivatedRules` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
    rule in the ``RuleGroup`` matches the request and is configured to block that request.
    However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
    ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
    rules contained within the group. Instead of blocking matching requests, those requests
    will be counted. You can view a record of counted requests using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
     a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

       ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
       . If set to ``NONE`` , the rule's action will take place.
    """


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef,
        "OverrideAction": ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[
            ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef
):
    """
    Type definition for `ClientListActivatedRulesInRuleGroupResponse` `ActivatedRules`

    The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
    to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that
    you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` ,
    or ``COUNT`` ).

    To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
    WebACLUpdate data type.

    - **Priority** *(integer) --*

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
      value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
      values don't need to be consecutive.

    - **RuleId** *(string) --*

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the
      web ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
       a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
        a ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
      rule in the ``RuleGroup`` matches the request and is configured to block that request.
      However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
      ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
      rules contained within the group. Instead of blocking matching requests, those requests
      will be counted. You can view a record of counted requests using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
       a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

         ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
         . If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
      RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
      Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
      web ACL without setting the type, the  UpdateWebACL request will fail because the request
      tries to add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the specific
      rule within the rule group that is blocking the legitimate traffic and then disable
      (exclude) that particular rule. You can exclude rules from both your own rule groups and
      AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
      changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
      metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web ACL,
      perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
      more information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
        you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
        that is specified by the ``ActivatedRule`` .

        - **RuleId** *(string) --*

          The unique identifier for the rule to exclude from the rule group.
    """


_ClientListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List[
            ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef
        ],
    },
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseTypeDef
):
    """
    Type definition for `ClientListActivatedRulesInRuleGroup` `Response`

    - **NextMarker** *(string) --*

      If you have more ``ActivatedRules`` than the number that you specified for ``Limit`` in the
      request, the response includes a ``NextMarker`` value. To list more ``ActivatedRules`` ,
      submit another ``ListActivatedRulesInRuleGroup`` request, and specify the ``NextMarker``
      value from the response in the ``NextMarker`` value in the next request.

    - **ActivatedRules** *(list) --*

      An array of ``ActivatedRules`` objects.

      - *(dict) --*

        The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
        to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that
        you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` ,
        or ``COUNT`` ).

        To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
        WebACLUpdate data type.

        - **Priority** *(integer) --*

          Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
          lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
          value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
          values don't need to be consecutive.

        - **RuleId** *(string) --*

          The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Action** *(dict) --*

          Specifies the action that CloudFront or AWS WAF takes when a web request matches the
          conditions in the ``Rule`` . Valid values for ``Action`` include the following:

          * ``ALLOW`` : CloudFront responds with the requested object.

          * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

          * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
          rule and then continues to inspect the web request based on the remaining rules in the
          web ACL.

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
           a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

            Specifies how you want AWS WAF to respond to requests that match the settings in a
            ``Rule`` . Valid settings include the following:

            * ``ALLOW`` : AWS WAF allows requests

            * ``BLOCK`` : AWS WAF blocks requests

            * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
            conditions in the rule. AWS WAF then continues to inspect the web request based on the
            remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
            a ``WebACL`` .

        - **OverrideAction** *(dict) --*

          Use the ``OverrideAction`` to test your ``RuleGroup`` .

          Any rule in a ``RuleGroup`` can potentially block a request. If you set the
          ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
          rule in the ``RuleGroup`` matches the request and is configured to block that request.
          However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
          ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
          rules contained within the group. Instead of blocking matching requests, those requests
          will be counted. You can view a record of counted requests using  GetSampledRequests .

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
           a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

             ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
             . If set to ``NONE`` , the rule's action will take place.

        - **Type** *(string) --*

          The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
          RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
          Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
          web ACL without setting the type, the  UpdateWebACL request will fail because the request
          tries to add a REGULAR rule with the specified ID, which does not exist.

        - **ExcludedRules** *(list) --*

          An array of rules to exclude from a rule group. This is applicable only when the
          ``ActivatedRule`` refers to a ``RuleGroup`` .

          Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
          unexpectedly (false positives). One troubleshooting technique is to identify the specific
          rule within the rule group that is blocking the legitimate traffic and then disable
          (exclude) that particular rule. You can exclude rules from both your own rule groups and
          AWS Marketplace rule groups that have been associated with a web ACL.

          Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
          changes the action for the rules to ``COUNT`` . Therefore, requests that match an
          ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
          metrics for each ``ExcludedRule`` .

          If you want to exclude rules from a rule group that is already associated with a web ACL,
          perform the following steps:

          * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
          more information about the logs, see `Logging Web ACL Traffic Information
          <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

          * Submit an  UpdateWebACL request that has two actions:

            * The first action deletes the existing rule group from the web ACL. That is, in the
            UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
            ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
            you want to exclude.

            * The second action inserts the same rule group back in, but specifying the rules to
            exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
            ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
            ``ExcludedRules`` should contain the rules that you want to exclude.

          - *(dict) --*

            The rule to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
            that is specified by the ``ActivatedRule`` .

            - **RuleId** *(string) --*

              The unique identifier for the rule to exclude from the rule group.
    """


_ClientListByteMatchSetsResponseByteMatchSetsTypeDef = TypedDict(
    "_ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    {"ByteMatchSetId": str, "Name": str},
    total=False,
)


class ClientListByteMatchSetsResponseByteMatchSetsTypeDef(
    _ClientListByteMatchSetsResponseByteMatchSetsTypeDef
):
    """
    Type definition for `ClientListByteMatchSetsResponse` `ByteMatchSets`

    Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name``
    and ``ByteMatchSetId`` for one  ByteMatchSet .

    - **ByteMatchSetId** *(string) --*

      The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
      information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a
      ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.

       ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
      create a ``ByteMatchSet`` .
    """


_ClientListByteMatchSetsResponseTypeDef = TypedDict(
    "_ClientListByteMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List[ClientListByteMatchSetsResponseByteMatchSetsTypeDef],
    },
    total=False,
)


class ClientListByteMatchSetsResponseTypeDef(_ClientListByteMatchSetsResponseTypeDef):
    """
    Type definition for `ClientListByteMatchSets` `Response`

    - **NextMarker** *(string) --*

      If you have more ``ByteMatchSet`` objects than the number that you specified for ``Limit`` in
      the request, the response includes a ``NextMarker`` value. To list more ``ByteMatchSet``
      objects, submit another ``ListByteMatchSets`` request, and specify the ``NextMarker`` value
      from the response in the ``NextMarker`` value in the next request.

    - **ByteMatchSets** *(list) --*

      An array of  ByteMatchSetSummary objects.

      - *(dict) --*

        Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name``
        and ``ByteMatchSetId`` for one  ByteMatchSet .

        - **ByteMatchSetId** *(string) --*

          The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
          information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a
          ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.

           ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

        - **Name** *(string) --*

          A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
          create a ``ByteMatchSet`` .
    """


_ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef = TypedDict(
    "_ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    {"GeoMatchSetId": str, "Name": str},
    total=False,
)


class ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef(
    _ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef
):
    """
    Type definition for `ClientListGeoMatchSetsResponse` `GeoMatchSets`

    Contains the identifier and the name of the ``GeoMatchSet`` .

    - **GeoMatchSetId** *(string) --*

      The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a
      GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

    - **Name** *(string) --*

      A friendly name or description of the  GeoMatchSet . You can't change the name of an
      ``GeoMatchSet`` after you create it.
    """


_ClientListGeoMatchSetsResponseTypeDef = TypedDict(
    "_ClientListGeoMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List[ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef],
    },
    total=False,
)


class ClientListGeoMatchSetsResponseTypeDef(_ClientListGeoMatchSetsResponseTypeDef):
    """
    Type definition for `ClientListGeoMatchSets` `Response`

    - **NextMarker** *(string) --*

      If you have more ``GeoMatchSet`` objects than the number that you specified for ``Limit`` in
      the request, the response includes a ``NextMarker`` value. To list more ``GeoMatchSet``
      objects, submit another ``ListGeoMatchSets`` request, and specify the ``NextMarker`` value
      from the response in the ``NextMarker`` value in the next request.

    - **GeoMatchSets** *(list) --*

      An array of  GeoMatchSetSummary objects.

      - *(dict) --*

        Contains the identifier and the name of the ``GeoMatchSet`` .

        - **GeoMatchSetId** *(string) --*

          The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a
          GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

        - **Name** *(string) --*

          A friendly name or description of the  GeoMatchSet . You can't change the name of an
          ``GeoMatchSet`` after you create it.
    """


_ClientListIpSetsResponseIPSetsTypeDef = TypedDict(
    "_ClientListIpSetsResponseIPSetsTypeDef", {"IPSetId": str, "Name": str}, total=False
)


class ClientListIpSetsResponseIPSetsTypeDef(_ClientListIpSetsResponseIPSetsTypeDef):
    """
    Type definition for `ClientListIpSetsResponse` `IPSets`

    Contains the identifier and the name of the ``IPSet`` .

    - **IPSetId** *(string) --*

      The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get
      detailed information about an  IPSet .

    - **Name** *(string) --*

      A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
      after you create it.
    """


_ClientListIpSetsResponseTypeDef = TypedDict(
    "_ClientListIpSetsResponseTypeDef",
    {"NextMarker": str, "IPSets": List[ClientListIpSetsResponseIPSetsTypeDef]},
    total=False,
)


class ClientListIpSetsResponseTypeDef(_ClientListIpSetsResponseTypeDef):
    """
    Type definition for `ClientListIpSets` `Response`

    - **NextMarker** *(string) --*

      To list more ``IPSet`` objects, submit another ``ListIPSets`` request, and in the next
      request use the ``NextMarker`` response value as the ``NextMarker`` value.

    - **IPSets** *(list) --*

      An array of  IPSetSummary objects.

      - *(dict) --*

        Contains the identifier and the name of the ``IPSet`` .

        - **IPSetId** *(string) --*

          The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get
          detailed information about an  IPSet .

        - **Name** *(string) --*

          A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
          after you create it.
    """


_ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef(
    _ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef
):
    """
    Type definition for `ClientListLoggingConfigurationsResponseLoggingConfigurations` `RedactedFields`

    Specifies where in a web request to look for ``TargetString`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef(
    _ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef
):
    """
    Type definition for `ClientListLoggingConfigurationsResponse` `LoggingConfigurations`

    The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
    Resource Name (ARN).

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the web ACL that you want to associate with
      ``LogDestinationConfigs`` .

    - **LogDestinationConfigs** *(list) --*

      An array of Amazon Kinesis Data Firehose ARNs.

      - *(string) --*

    - **RedactedFields** *(list) --*

      The parts of the request that you want redacted from the logs. For example, if you redact
      the cookie field, the cookie field in the firehose will be ``xxx`` .

      - *(dict) --*

        Specifies where in a web request to look for ``TargetString`` .

        - **Type** *(string) --*

          The part of the web request that you want AWS WAF to search for a specified string.
          Parts of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the
          ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
          the name of the header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the
          request is asking the origin to perform. Amazon CloudFront supports the following
          methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
          ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The
          request body immediately follows the request headers. Note that only the first
          ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
          or block requests based on the length of the body, you can create a size constraint
          set. For more information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
          such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
          30 characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value
          or regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
          AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
          header is not case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
          that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
          parameter name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientListLoggingConfigurationsResponseTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientListLoggingConfigurationsResponseTypeDef(
    _ClientListLoggingConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListLoggingConfigurations` `Response`

    - **LoggingConfigurations** *(list) --*

      An array of  LoggingConfiguration objects.

      - *(dict) --*

        The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
        Resource Name (ARN).

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the web ACL that you want to associate with
          ``LogDestinationConfigs`` .

        - **LogDestinationConfigs** *(list) --*

          An array of Amazon Kinesis Data Firehose ARNs.

          - *(string) --*

        - **RedactedFields** *(list) --*

          The parts of the request that you want redacted from the logs. For example, if you redact
          the cookie field, the cookie field in the firehose will be ``xxx`` .

          - *(dict) --*

            Specifies where in a web request to look for ``TargetString`` .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

    - **NextMarker** *(string) --*

      If you have more ``LoggingConfigurations`` than the number that you specified for ``Limit``
      in the request, the response includes a ``NextMarker`` value. To list more
      ``LoggingConfigurations`` , submit another ``ListLoggingConfigurations`` request, and specify
      the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.
    """


_ClientListRateBasedRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRateBasedRulesResponseRulesTypeDef",
    {"RuleId": str, "Name": str},
    total=False,
)


class ClientListRateBasedRulesResponseRulesTypeDef(
    _ClientListRateBasedRulesResponseRulesTypeDef
):
    """
    Type definition for `ClientListRateBasedRulesResponse` `Rules`

    Contains the identifier and the friendly name or description of the ``Rule`` .

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      A friendly name or description of the  Rule . You can't change the name of a ``Rule``
      after you create it.
    """


_ClientListRateBasedRulesResponseTypeDef = TypedDict(
    "_ClientListRateBasedRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRateBasedRulesResponseRulesTypeDef]},
    total=False,
)


class ClientListRateBasedRulesResponseTypeDef(_ClientListRateBasedRulesResponseTypeDef):
    """
    Type definition for `ClientListRateBasedRules` `Response`

    - **NextMarker** *(string) --*

      If you have more ``Rules`` than the number that you specified for ``Limit`` in the request,
      the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another
      ``ListRateBasedRules`` request, and specify the ``NextMarker`` value from the response in the
      ``NextMarker`` value in the next request.

    - **Rules** *(list) --*

      An array of  RuleSummary objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``Rule`` .

        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Name** *(string) --*

          A friendly name or description of the  Rule . You can't change the name of a ``Rule``
          after you create it.
    """


_ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef = TypedDict(
    "_ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    {"RegexMatchSetId": str, "Name": str},
    total=False,
)


class ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef(
    _ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef
):
    """
    Type definition for `ClientListRegexMatchSetsResponse` `RegexMatchSets`

    Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the
    ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .

    - **RegexMatchSetId** *(string) --*

      The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
      information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a
      ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.

       ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after
      you create a ``RegexMatchSet`` .
    """


_ClientListRegexMatchSetsResponseTypeDef = TypedDict(
    "_ClientListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List[ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef],
    },
    total=False,
)


class ClientListRegexMatchSetsResponseTypeDef(_ClientListRegexMatchSetsResponseTypeDef):
    """
    Type definition for `ClientListRegexMatchSets` `Response`

    - **NextMarker** *(string) --*

      If you have more ``RegexMatchSet`` objects than the number that you specified for ``Limit``
      in the request, the response includes a ``NextMarker`` value. To list more ``RegexMatchSet``
      objects, submit another ``ListRegexMatchSets`` request, and specify the ``NextMarker`` value
      from the response in the ``NextMarker`` value in the next request.

    - **RegexMatchSets** *(list) --*

      An array of  RegexMatchSetSummary objects.

      - *(dict) --*

        Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the
        ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .

        - **RegexMatchSetId** *(string) --*

          The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
          information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a
          ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.

           ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

        - **Name** *(string) --*

          A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after
          you create a ``RegexMatchSet`` .
    """


_ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef = TypedDict(
    "_ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    {"RegexPatternSetId": str, "Name": str},
    total=False,
)


class ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef(
    _ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef
):
    """
    Type definition for `ClientListRegexPatternSetsResponse` `RegexPatternSets`

    Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the
    ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .

    - **RegexPatternSetId** *(string) --*

      The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
      get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
      ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
      WAF.

       ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets
       .

    - **Name** *(string) --*

      A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
      you create a ``RegexPatternSet`` .
    """


_ClientListRegexPatternSetsResponseTypeDef = TypedDict(
    "_ClientListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List[
            ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef
        ],
    },
    total=False,
)


class ClientListRegexPatternSetsResponseTypeDef(
    _ClientListRegexPatternSetsResponseTypeDef
):
    """
    Type definition for `ClientListRegexPatternSets` `Response`

    - **NextMarker** *(string) --*

      If you have more ``RegexPatternSet`` objects than the number that you specified for ``Limit``
      in the request, the response includes a ``NextMarker`` value. To list more
      ``RegexPatternSet`` objects, submit another ``ListRegexPatternSets`` request, and specify the
      ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

    - **RegexPatternSets** *(list) --*

      An array of  RegexPatternSetSummary objects.

      - *(dict) --*

        Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the
        ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .

        - **RegexPatternSetId** *(string) --*

          The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
          get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
          ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
          WAF.

           ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets
           .

        - **Name** *(string) --*

          A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
          you create a ``RegexPatternSet`` .
    """


_ClientListRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "_ClientListRuleGroupsResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str},
    total=False,
)


class ClientListRuleGroupsResponseRuleGroupsTypeDef(
    _ClientListRuleGroupsResponseRuleGroupsTypeDef
):
    """
    Type definition for `ClientListRuleGroupsResponse` `RuleGroups`

    Contains the identifier and the friendly name or description of the ``RuleGroup`` .

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
      about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
      ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see
      UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

       ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

    - **Name** *(string) --*

      A friendly name or description of the  RuleGroup . You can't change the name of a
      ``RuleGroup`` after you create it.
    """


_ClientListRuleGroupsResponseTypeDef = TypedDict(
    "_ClientListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[ClientListRuleGroupsResponseRuleGroupsTypeDef],
    },
    total=False,
)


class ClientListRuleGroupsResponseTypeDef(_ClientListRuleGroupsResponseTypeDef):
    """
    Type definition for `ClientListRuleGroups` `Response`

    - **NextMarker** *(string) --*

      If you have more ``RuleGroups`` than the number that you specified for ``Limit`` in the
      request, the response includes a ``NextMarker`` value. To list more ``RuleGroups`` , submit
      another ``ListRuleGroups`` request, and specify the ``NextMarker`` value from the response in
      the ``NextMarker`` value in the next request.

    - **RuleGroups** *(list) --*

      An array of  RuleGroup objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``RuleGroup`` .

        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
          about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
          ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see
          UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

           ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

        - **Name** *(string) --*

          A friendly name or description of the  RuleGroup . You can't change the name of a
          ``RuleGroup`` after you create it.
    """


_ClientListRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRulesResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)


class ClientListRulesResponseRulesTypeDef(_ClientListRulesResponseRulesTypeDef):
    """
    Type definition for `ClientListRulesResponse` `Rules`

    Contains the identifier and the friendly name or description of the ``Rule`` .

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      A friendly name or description of the  Rule . You can't change the name of a ``Rule``
      after you create it.
    """


_ClientListRulesResponseTypeDef = TypedDict(
    "_ClientListRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRulesResponseRulesTypeDef]},
    total=False,
)


class ClientListRulesResponseTypeDef(_ClientListRulesResponseTypeDef):
    """
    Type definition for `ClientListRules` `Response`

    - **NextMarker** *(string) --*

      If you have more ``Rules`` than the number that you specified for ``Limit`` in the request,
      the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another
      ``ListRules`` request, and specify the ``NextMarker`` value from the response in the
      ``NextMarker`` value in the next request.

    - **Rules** *(list) --*

      An array of  RuleSummary objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``Rule`` .

        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Name** *(string) --*

          A friendly name or description of the  Rule . You can't change the name of a ``Rule``
          after you create it.
    """


_ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef = TypedDict(
    "_ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    {"SizeConstraintSetId": str, "Name": str},
    total=False,
)


class ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef(
    _ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef
):
    """
    Type definition for `ClientListSizeConstraintSetsResponse` `SizeConstraintSets`

    The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .

    - **SizeConstraintSetId** *(string) --*

      A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
      information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
      ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet``
      into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
      ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

       ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
       ListSizeConstraintSets .

    - **Name** *(string) --*

      The name of the ``SizeConstraintSet`` , if any.
    """


_ClientListSizeConstraintSetsResponseTypeDef = TypedDict(
    "_ClientListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List[
            ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef
        ],
    },
    total=False,
)


class ClientListSizeConstraintSetsResponseTypeDef(
    _ClientListSizeConstraintSetsResponseTypeDef
):
    """
    Type definition for `ClientListSizeConstraintSets` `Response`

    - **NextMarker** *(string) --*

      If you have more ``SizeConstraintSet`` objects than the number that you specified for
      ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more
      ``SizeConstraintSet`` objects, submit another ``ListSizeConstraintSets`` request, and specify
      the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

    - **SizeConstraintSets** *(list) --*

      An array of  SizeConstraintSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .

        - **SizeConstraintSetId** *(string) --*

          A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
          information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
          ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet``
          into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
          ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

           ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
           ListSizeConstraintSets .

        - **Name** *(string) --*

          The name of the ``SizeConstraintSet`` , if any.
    """


_ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef = TypedDict(
    "_ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    {"SqlInjectionMatchSetId": str, "Name": str},
    total=False,
)


class ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef(
    _ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef
):
    """
    Type definition for `ClientListSqlInjectionMatchSetsResponse` `SqlInjectionMatchSets`

    The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .

    - **SqlInjectionMatchSetId** *(string) --*

      A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId``
      to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ),
      update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
      ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule
      ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

       ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
       ListSqlInjectionMatchSets .

    - **Name** *(string) --*

      The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .
    """


_ClientListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "_ClientListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List[
            ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef
        ],
    },
    total=False,
)


class ClientListSqlInjectionMatchSetsResponseTypeDef(
    _ClientListSqlInjectionMatchSetsResponseTypeDef
):
    """
    Type definition for `ClientListSqlInjectionMatchSets` `Response`

    The response to a  ListSqlInjectionMatchSets request.

    - **NextMarker** *(string) --*

      If you have more  SqlInjectionMatchSet objects than the number that you specified for
      ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more
      ``SqlInjectionMatchSet`` objects, submit another ``ListSqlInjectionMatchSets`` request, and
      specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next
      request.

    - **SqlInjectionMatchSets** *(list) --*

      An array of  SqlInjectionMatchSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .

        - **SqlInjectionMatchSetId** *(string) --*

          A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId``
          to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ),
          update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
          ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule
          ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

           ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
           ListSqlInjectionMatchSets .

        - **Name** *(string) --*

          The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .
    """


_ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "_ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef(
    _ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef
):
    """
    Type definition for `ClientListSubscribedRuleGroupsResponse` `RuleGroups`

    A summary of the rule groups you are subscribed to.

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` .

    - **Name** *(string) --*

      A friendly name or description of the ``RuleGroup`` . You can't change the name of a
      ``RuleGroup`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``RuleGroup`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RuleGroup`` .
    """


_ClientListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "_ClientListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef],
    },
    total=False,
)


class ClientListSubscribedRuleGroupsResponseTypeDef(
    _ClientListSubscribedRuleGroupsResponseTypeDef
):
    """
    Type definition for `ClientListSubscribedRuleGroups` `Response`

    - **NextMarker** *(string) --*

      If you have more objects than the number that you specified for ``Limit`` in the request, the
      response includes a ``NextMarker`` value. To list more objects, submit another
      ``ListSubscribedRuleGroups`` request, and specify the ``NextMarker`` value from the response
      in the ``NextMarker`` value in the next request.

    - **RuleGroups** *(list) --*

      An array of  RuleGroup objects.

      - *(dict) --*

        A summary of the rule groups you are subscribed to.

        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` .

        - **Name** *(string) --*

          A friendly name or description of the ``RuleGroup`` . You can't change the name of a
          ``RuleGroup`` after you create it.

        - **MetricName** *(string) --*

          A friendly name or description for the metrics for this ``RuleGroup`` . The name can
          contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
          length one. It can't contain whitespace or metric names reserved for AWS WAF, including
          "All" and "Default_Action." You can't change the name of the metric after you create the
          ``RuleGroup`` .
    """


_ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef(
    _ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponseTagInfoForResource` `TagList`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientListTagsForResourceResponseTagInfoForResourceTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List[
            ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef
        ],
    },
    total=False,
)


class ClientListTagsForResourceResponseTagInfoForResourceTypeDef(
    _ClientListTagsForResourceResponseTagInfoForResourceTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `TagInfoForResource`

    - **ResourceARN** *(string) --*

    - **TagList** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **Value** *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": ClientListTagsForResourceResponseTagInfoForResourceTypeDef,
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **NextMarker** *(string) --*

    - **TagInfoForResource** *(dict) --*

      - **ResourceARN** *(string) --*

      - **TagList** *(list) --*

        - *(dict) --*

          - **Key** *(string) --*

          - **Value** *(string) --*
    """


_ClientListWebAclsResponseWebACLsTypeDef = TypedDict(
    "_ClientListWebAclsResponseWebACLsTypeDef",
    {"WebACLId": str, "Name": str},
    total=False,
)


class ClientListWebAclsResponseWebACLsTypeDef(_ClientListWebAclsResponseWebACLsTypeDef):
    """
    Type definition for `ClientListWebAclsResponse` `WebACLs`

    Contains the identifier and the name or description of the  WebACL .

    - **WebACLId** *(string) --*

      A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
      ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
      ``WebACL`` from AWS WAF (see  DeleteWebACL ).

       ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

    - **Name** *(string) --*

      A friendly name or description of the  WebACL . You can't change the name of a ``WebACL``
      after you create it.
    """


_ClientListWebAclsResponseTypeDef = TypedDict(
    "_ClientListWebAclsResponseTypeDef",
    {"NextMarker": str, "WebACLs": List[ClientListWebAclsResponseWebACLsTypeDef]},
    total=False,
)


class ClientListWebAclsResponseTypeDef(_ClientListWebAclsResponseTypeDef):
    """
    Type definition for `ClientListWebAcls` `Response`

    - **NextMarker** *(string) --*

      If you have more ``WebACL`` objects than the number that you specified for ``Limit`` in the
      request, the response includes a ``NextMarker`` value. To list more ``WebACL`` objects,
      submit another ``ListWebACLs`` request, and specify the ``NextMarker`` value from the
      response in the ``NextMarker`` value in the next request.

    - **WebACLs** *(list) --*

      An array of  WebACLSummary objects.

      - *(dict) --*

        Contains the identifier and the name or description of the  WebACL .

        - **WebACLId** *(string) --*

          A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
          ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
          ``WebACL`` from AWS WAF (see  DeleteWebACL ).

           ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

        - **Name** *(string) --*

          A friendly name or description of the  WebACL . You can't change the name of a ``WebACL``
          after you create it.
    """


_ClientListXssMatchSetsResponseXssMatchSetsTypeDef = TypedDict(
    "_ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    {"XssMatchSetId": str, "Name": str},
    total=False,
)


class ClientListXssMatchSetsResponseXssMatchSetsTypeDef(
    _ClientListXssMatchSetsResponseXssMatchSetsTypeDef
):
    """
    Type definition for `ClientListXssMatchSetsResponse` `XssMatchSets`

    The ``Id`` and ``Name`` of an ``XssMatchSet`` .

    - **XssMatchSetId** *(string) --*

      A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
      about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
      UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
      DeleteXssMatchSet ).

       ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

    - **Name** *(string) --*

      The name of the ``XssMatchSet`` , if any, specified by ``Id`` .
    """


_ClientListXssMatchSetsResponseTypeDef = TypedDict(
    "_ClientListXssMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List[ClientListXssMatchSetsResponseXssMatchSetsTypeDef],
    },
    total=False,
)


class ClientListXssMatchSetsResponseTypeDef(_ClientListXssMatchSetsResponseTypeDef):
    """
    Type definition for `ClientListXssMatchSets` `Response`

    The response to a  ListXssMatchSets request.

    - **NextMarker** *(string) --*

      If you have more  XssMatchSet objects than the number that you specified for ``Limit`` in the
      request, the response includes a ``NextMarker`` value. To list more ``XssMatchSet`` objects,
      submit another ``ListXssMatchSets`` request, and specify the ``NextMarker`` value from the
      response in the ``NextMarker`` value in the next request.

    - **XssMatchSets** *(list) --*

      An array of  XssMatchSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of an ``XssMatchSet`` .

        - **XssMatchSetId** *(string) --*

          A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
          about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
          UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
          DeleteXssMatchSet ).

           ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

        - **Name** *(string) --*

          The name of the ``XssMatchSet`` , if any, specified by ``Id`` .
    """


_RequiredClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_RequiredClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    {"Type": str},
)
_OptionalClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_OptionalClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    {"Data": str},
    total=False,
)


class ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef(
    _RequiredClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef,
    _OptionalClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef,
):
    """
    Type definition for `ClientPutLoggingConfigurationLoggingConfiguration` `RedactedFields`

    Specifies where in a web request to look for ``TargetString`` .

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or
      ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header
      in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE``
      , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?``
      character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to send
      to your web server as the HTTP request body, such as data from a form. The request body
      immediately follows the request headers. Note that only the first ``8192`` bytes of the
      request body are forwarded to AWS WAF for inspection. To allow or block requests based on
      the length of the body, you can create a size constraint set. For more information, see
      CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    {"ResourceArn": str, "LogDestinationConfigs": List[str]},
)
_OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    {
        "RedactedFields": List[
            ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef
        ]
    },
    total=False,
)


class ClientPutLoggingConfigurationLoggingConfigurationTypeDef(
    _RequiredClientPutLoggingConfigurationLoggingConfigurationTypeDef,
    _OptionalClientPutLoggingConfigurationLoggingConfigurationTypeDef,
):
    """
    Type definition for `ClientPutLoggingConfiguration` `LoggingConfiguration`

    The Amazon Kinesis Data Firehose that contains the inspected traffic information, the redacted
    fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.

    .. note::

      When specifying ``Type`` in ``RedactedFields`` , you must use one of the following values:
      ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the web ACL that you want to associate with
      ``LogDestinationConfigs`` .

    - **LogDestinationConfigs** *(list) --* **[REQUIRED]**

      An array of Amazon Kinesis Data Firehose ARNs.

      - *(string) --*

    - **RedactedFields** *(list) --*

      The parts of the request that you want redacted from the logs. For example, if you redact the
      cookie field, the cookie field in the firehose will be ``xxx`` .

      - *(dict) --*

        Specifies where in a web request to look for ``TargetString`` .

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or
          ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header
          in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE``
          , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?``
          character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to send
          to your web server as the HTTP request body, such as data from a form. The request body
          immediately follows the request headers. Note that only the first ``8192`` bytes of the
          request body are forwarded to AWS WAF for inspection. To allow or block requests based on
          the length of the body, you can create a size constraint set. For more information, see
          CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef(
    _ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
):
    """
    Type definition for `ClientPutLoggingConfigurationResponseLoggingConfiguration` `RedactedFields`

    Specifies where in a web request to look for ``TargetString`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
      is asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes
      of the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
      as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
      is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    Type definition for `ClientPutLoggingConfigurationResponse` `LoggingConfiguration`

    The  LoggingConfiguration that you submitted in the request.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the web ACL that you want to associate with
      ``LogDestinationConfigs`` .

    - **LogDestinationConfigs** *(list) --*

      An array of Amazon Kinesis Data Firehose ARNs.

      - *(string) --*

    - **RedactedFields** *(list) --*

      The parts of the request that you want redacted from the logs. For example, if you redact
      the cookie field, the cookie field in the firehose will be ``xxx`` .

      - *(dict) --*

        Specifies where in a web request to look for ``TargetString`` .

        - **Type** *(string) --*

          The part of the web request that you want AWS WAF to search for a specified string.
          Parts of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
          is asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes
          of the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
          as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
          AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
          is not case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
          that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
          parameter name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientPutLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef
    },
    total=False,
)


class ClientPutLoggingConfigurationResponseTypeDef(
    _ClientPutLoggingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutLoggingConfiguration` `Response`

    - **LoggingConfiguration** *(dict) --*

      The  LoggingConfiguration that you submitted in the request.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the web ACL that you want to associate with
        ``LogDestinationConfigs`` .

      - **LogDestinationConfigs** *(list) --*

        An array of Amazon Kinesis Data Firehose ARNs.

        - *(string) --*

      - **RedactedFields** *(list) --*

        The parts of the request that you want redacted from the logs. For example, if you redact
        the cookie field, the cookie field in the firehose will be ``xxx`` .

        - *(dict) --*

          Specifies where in a web request to look for ``TargetString`` .

          - **Type** *(string) --*

            The part of the web request that you want AWS WAF to search for a specified string.
            Parts of a request that you can search include the following:

            * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
            or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
            header in ``Data`` .

            * ``METHOD`` : The HTTP method, which indicated the type of operation that the request
            is asking the origin to perform. Amazon CloudFront supports the following methods:
            ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

            * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
            ``?`` character, if any.

            * ``URI`` : The part of a web request that identifies a resource, for example,
            ``/images/daily-ad.jpg`` .

            * ``BODY`` : The part of a request that contains any additional data that you want to
            send to your web server as the HTTP request body, such as data from a form. The request
            body immediately follows the request headers. Note that only the first ``8192`` bytes
            of the request body are forwarded to AWS WAF for inspection. To allow or block requests
            based on the length of the body, you can create a size constraint set. For more
            information, see  CreateSizeConstraintSet .

            * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such
            as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
            characters.

            * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
            single parameter, AWS WAF will inspect all parameters within the query for the value or
            regex pattern that you specify in ``TargetString`` .

          - **Data** *(string) --*

            When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
            AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header
            is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
            that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
            parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientUpdateByteMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateByteMatchSetResponseTypeDef(_ClientUpdateByteMatchSetResponseTypeDef):
    """
    Type definition for `ClientUpdateByteMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateByteMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_RequiredClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef = TypedDict(
    "_RequiredClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    {"Type": str},
)
_OptionalClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef = TypedDict(
    "_OptionalClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    {"Data": str},
    total=False,
)


class ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef(
    _RequiredClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef,
    _OptionalClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef,
):
    """
    Type definition for `ClientUpdateByteMatchSetUpdatesByteMatchTuple` `FieldToMatch`

    The part of a web request that you want AWS WAF to search, such as a specified header or a
    query string. For more information, see  FieldToMatch .

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes of
      the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": str,
        "PositionalConstraint": str,
    },
)


class ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef(
    _ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef
):
    """
    Type definition for `ClientUpdateByteMatchSetUpdates` `ByteMatchTuple`

    Information about the part of a web request that you want AWS WAF to inspect and the value
    that you want AWS WAF to search for. If you specify ``DELETE`` for the value of ``Action`` ,
    the ``ByteMatchTuple`` values must exactly match the values in the ``ByteMatchTuple`` that
    you want to delete from the ``ByteMatchSet`` .

    - **FieldToMatch** *(dict) --* **[REQUIRED]**

      The part of a web request that you want AWS WAF to search, such as a specified header or a
      query string. For more information, see  FieldToMatch .

      - **Type** *(string) --* **[REQUIRED]**

        The part of the web request that you want AWS WAF to search for a specified string. Parts
        of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
        or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
        header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
        asking the origin to perform. Amazon CloudFront supports the following methods:
        ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The request
        body immediately follows the request headers. Note that only the first ``8192`` bytes of
        the request body are forwarded to AWS WAF for inspection. To allow or block requests
        based on the length of the body, you can create a size constraint set. For more
        information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
        characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value or
        regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
        WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
        case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
        you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
        name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TargetString** *(bytes) --* **[REQUIRED]**

      The value that you want AWS WAF to search for. AWS WAF searches for the specified string in
      the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the
      value is 50 bytes.

      Valid values depend on the values that you specified for ``FieldToMatch`` :

      * ``HEADER`` : The value that you want AWS WAF to search for in the request header that you
      specified in  FieldToMatch , for example, the value of the ``User-Agent`` or ``Referer``
      header.

      * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
      request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
      ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
      which is the part of a URL that appears after a ``?`` character.

      * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
      identifies a resource, for example, ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to send
      to your web server as the HTTP request body, such as data from a form. The request body
      immediately follows the request headers. Note that only the first ``8192`` bytes of the
      request body are forwarded to AWS WAF for inspection. To allow or block requests based on
      the length of the body, you can create a size constraint set. For more information, see
      CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a single
      parameter, AWS WAF inspects all parameters within the query string for the value or regex
      pattern that you specify in ``TargetString`` .

      If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case
      sensitive.

       **If you're using the AWS WAF API**

      Specify a base64-encoded version of the value. The maximum length of the value before you
      base64-encode it is 50 bytes.

      For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
      ``User-Agent`` . If you want to search the ``User-Agent`` header for the value ``BadBot`` ,
      you base64-encode ``BadBot`` using MIME base64-encoding and include the resulting value,
      ``QmFkQm90`` , in the value of ``TargetString`` .

       **If you're using the AWS CLI or one of the AWS SDKs**

      The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
      value.

    - **TextTransformation** *(string) --* **[REQUIRED]**

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
      the transformation on ``TargetString`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line command
      and using unusual formatting to disguise some or all of the command, use this option to
      perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
      with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
      the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **PositionalConstraint** *(string) --* **[REQUIRED]**

      Within the portion of a web request that you want to search (for example, in the query
      string, if any), specify where you want AWS WAF to search. Valid values include the
      following:

       **CONTAINS**

      The specified part of the web request must include the value of ``TargetString`` , but the
      location doesn't matter.

       **CONTAINS_WORD**

      The specified part of the web request must include the value of ``TargetString`` , and
      ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or
      _). In addition, ``TargetString`` must be a word, which means one of the following:

      * ``TargetString`` exactly matches the value of the specified part of the web request, such
      as the value of a header.

      * ``TargetString`` is at the beginning of the specified part of the web request and is
      followed by a character other than an alphanumeric character or underscore (_), for
      example, ``BadBot;`` .

      * ``TargetString`` is at the end of the specified part of the web request and is preceded
      by a character other than an alphanumeric character or underscore (_), for example,
      ``;BadBot`` .

      * ``TargetString`` is in the middle of the specified part of the web request and is
      preceded and followed by characters other than alphanumeric characters or underscore (_),
      for example, ``-BadBot;`` .

       **EXACTLY**

      The value of the specified part of the web request must exactly match the value of
      ``TargetString`` .

       **STARTS_WITH**

      The value of ``TargetString`` must appear at the beginning of the specified part of the web
      request.

       **ENDS_WITH**

      The value of ``TargetString`` must appear at the end of the specified part of the web
      request.
    """


_ClientUpdateByteMatchSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetUpdatesTypeDef",
    {
        "Action": str,
        "ByteMatchTuple": ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef,
    },
)


class ClientUpdateByteMatchSetUpdatesTypeDef(_ClientUpdateByteMatchSetUpdatesTypeDef):
    """
    Type definition for `ClientUpdateByteMatchSet` `Updates`

    In an  UpdateByteMatchSet request, ``ByteMatchSetUpdate`` specifies whether to insert or delete
    a  ByteMatchTuple and includes the settings for the ``ByteMatchTuple`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert or delete a  ByteMatchTuple .

    - **ByteMatchTuple** *(dict) --* **[REQUIRED]**

      Information about the part of a web request that you want AWS WAF to inspect and the value
      that you want AWS WAF to search for. If you specify ``DELETE`` for the value of ``Action`` ,
      the ``ByteMatchTuple`` values must exactly match the values in the ``ByteMatchTuple`` that
      you want to delete from the ``ByteMatchSet`` .

      - **FieldToMatch** *(dict) --* **[REQUIRED]**

        The part of a web request that you want AWS WAF to search, such as a specified header or a
        query string. For more information, see  FieldToMatch .

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes of
          the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .

      - **TargetString** *(bytes) --* **[REQUIRED]**

        The value that you want AWS WAF to search for. AWS WAF searches for the specified string in
        the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the
        value is 50 bytes.

        Valid values depend on the values that you specified for ``FieldToMatch`` :

        * ``HEADER`` : The value that you want AWS WAF to search for in the request header that you
        specified in  FieldToMatch , for example, the value of the ``User-Agent`` or ``Referer``
        header.

        * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the
        request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` ,
        ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string,
        which is the part of a URL that appears after a ``?`` character.

        * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that
        identifies a resource, for example, ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to send
        to your web server as the HTTP request body, such as data from a form. The request body
        immediately follows the request headers. Note that only the first ``8192`` bytes of the
        request body are forwarded to AWS WAF for inspection. To allow or block requests based on
        the length of the body, you can create a size constraint set. For more information, see
        CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a single
        parameter, AWS WAF inspects all parameters within the query string for the value or regex
        pattern that you specify in ``TargetString`` .

        If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case
        sensitive.

         **If you're using the AWS WAF API**

        Specify a base64-encoded version of the value. The maximum length of the value before you
        base64-encode it is 50 bytes.

        For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is
        ``User-Agent`` . If you want to search the ``User-Agent`` header for the value ``BadBot`` ,
        you base64-encode ``BadBot`` using MIME base64-encoding and include the resulting value,
        ``QmFkQm90`` , in the value of ``TargetString`` .

         **If you're using the AWS CLI or one of the AWS SDKs**

        The value that you want AWS WAF to search for. The SDK automatically base64 encodes the
        value.

      - **TextTransformation** *(string) --* **[REQUIRED]**

        Text transformations eliminate some of the unusual formatting that attackers use in web
        requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
        the transformation on ``TargetString`` before inspecting a request for a match.

        You can only specify a single type of TextTransformation.

         **CMD_LINE**

        When you're concerned that attackers are injecting an operating system command line command
        and using unusual formatting to disguise some or all of the command, use this option to
        perform the following transformations:

        * Delete the following characters: \\ " ' ^

        * Delete spaces before the following characters: / (

        * Replace the following characters with a space: , ;

        * Replace multiple spaces with one space

        * Convert uppercase letters (A-Z) to lowercase (a-z)

         **COMPRESS_WHITE_SPACE**

        Use this option to replace the following characters with a space character (decimal 32):

        * \\f, formfeed, decimal 12

        * \\t, tab, decimal 9

        * \\n, newline, decimal 10

        * \\r, carriage return, decimal 13

        * \\v, vertical tab, decimal 11

        * non-breaking space, decimal 160

         ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

         **HTML_ENTITY_DECODE**

        Use this option to replace HTML-encoded characters with unencoded characters.
        ``HTML_ENTITY_DECODE`` performs the following operations:

        * Replaces ``(ampersand)quot;`` with ``"``

        * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

        * Replaces ``(ampersand)lt;`` with a "less than" symbol

        * Replaces ``(ampersand)gt;`` with ``>``

        * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
        with the corresponding characters

        * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
        the corresponding characters

         **LOWERCASE**

        Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

         **URL_DECODE**

        Use this option to decode a URL-encoded value.

         **NONE**

        Specify ``NONE`` if you don't want to perform any text transformations.

      - **PositionalConstraint** *(string) --* **[REQUIRED]**

        Within the portion of a web request that you want to search (for example, in the query
        string, if any), specify where you want AWS WAF to search. Valid values include the
        following:

         **CONTAINS**

        The specified part of the web request must include the value of ``TargetString`` , but the
        location doesn't matter.

         **CONTAINS_WORD**

        The specified part of the web request must include the value of ``TargetString`` , and
        ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or
        _). In addition, ``TargetString`` must be a word, which means one of the following:

        * ``TargetString`` exactly matches the value of the specified part of the web request, such
        as the value of a header.

        * ``TargetString`` is at the beginning of the specified part of the web request and is
        followed by a character other than an alphanumeric character or underscore (_), for
        example, ``BadBot;`` .

        * ``TargetString`` is at the end of the specified part of the web request and is preceded
        by a character other than an alphanumeric character or underscore (_), for example,
        ``;BadBot`` .

        * ``TargetString`` is in the middle of the specified part of the web request and is
        preceded and followed by characters other than alphanumeric characters or underscore (_),
        for example, ``-BadBot;`` .

         **EXACTLY**

        The value of the specified part of the web request must exactly match the value of
        ``TargetString`` .

         **STARTS_WITH**

        The value of ``TargetString`` must appear at the beginning of the specified part of the web
        request.

         **ENDS_WITH**

        The value of ``TargetString`` must appear at the end of the specified part of the web
        request.
    """


_ClientUpdateGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateGeoMatchSetResponseTypeDef(_ClientUpdateGeoMatchSetResponseTypeDef):
    """
    Type definition for `ClientUpdateGeoMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateGeoMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef = TypedDict(
    "_ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    {"Type": str, "Value": str},
)


class ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef(
    _ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef
):
    """
    Type definition for `ClientUpdateGeoMatchSetUpdates` `GeoMatchConstraint`

    The country from which web requests originate that you want AWS WAF to search for.

    - **Type** *(string) --* **[REQUIRED]**

      The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the
      only valid value.

    - **Value** *(string) --* **[REQUIRED]**

      The country that you want AWS WAF to search for.
    """


_ClientUpdateGeoMatchSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateGeoMatchSetUpdatesTypeDef",
    {
        "Action": str,
        "GeoMatchConstraint": ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef,
    },
)


class ClientUpdateGeoMatchSetUpdatesTypeDef(_ClientUpdateGeoMatchSetUpdatesTypeDef):
    """
    Type definition for `ClientUpdateGeoMatchSet` `Updates`

    Specifies the type of update to perform to an  GeoMatchSet with  UpdateGeoMatchSet .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert or delete a country with  UpdateGeoMatchSet .

    - **GeoMatchConstraint** *(dict) --* **[REQUIRED]**

      The country from which web requests originate that you want AWS WAF to search for.

      - **Type** *(string) --* **[REQUIRED]**

        The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the
        only valid value.

      - **Value** *(string) --* **[REQUIRED]**

        The country that you want AWS WAF to search for.
    """


_ClientUpdateIpSetResponseTypeDef = TypedDict(
    "_ClientUpdateIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateIpSetResponseTypeDef(_ClientUpdateIpSetResponseTypeDef):
    """
    Type definition for `ClientUpdateIpSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateIPSet`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef = TypedDict(
    "_ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef", {"Type": str, "Value": str}
)


class ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef(
    _ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef
):
    """
    Type definition for `ClientUpdateIpSetUpdates` `IPSetDescriptor`

    The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that
    web requests originate from.

    - **Type** *(string) --* **[REQUIRED]**

      Specify ``IPV4`` or ``IPV6`` .

    - **Value** *(string) --* **[REQUIRED]**

      Specify an IPv4 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 192.0.2.44, specify ``192.0.2.44/32`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP addresses
      from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

      For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain
      Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

      Specify an IPv6 address by using CIDR notation. For example:

      * To configure AWS WAF to allow, block, or count requests that originated from the IP
      address 1111:0000:0000:0000:0000:0000:0000:0111, specify
      ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

      * To configure AWS WAF to allow, block, or count requests that originated from IP addresses
      1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
      ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientUpdateIpSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateIpSetUpdatesTypeDef",
    {"Action": str, "IPSetDescriptor": ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef},
)


class ClientUpdateIpSetUpdatesTypeDef(_ClientUpdateIpSetUpdatesTypeDef):
    """
    Type definition for `ClientUpdateIpSet` `Updates`

    Specifies the type of update to perform to an  IPSet with  UpdateIPSet .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert or delete an IP address with  UpdateIPSet .

    - **IPSetDescriptor** *(dict) --* **[REQUIRED]**

      The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that
      web requests originate from.

      - **Type** *(string) --* **[REQUIRED]**

        Specify ``IPV4`` or ``IPV6`` .

      - **Value** *(string) --* **[REQUIRED]**

        Specify an IPv4 address by using CIDR notation. For example:

        * To configure AWS WAF to allow, block, or count requests that originated from the IP
        address 192.0.2.44, specify ``192.0.2.44/32`` .

        * To configure AWS WAF to allow, block, or count requests that originated from IP addresses
        from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

        For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain
        Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

        Specify an IPv6 address by using CIDR notation. For example:

        * To configure AWS WAF to allow, block, or count requests that originated from the IP
        address 1111:0000:0000:0000:0000:0000:0000:0111, specify
        ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .

        * To configure AWS WAF to allow, block, or count requests that originated from IP addresses
        1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify
        ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .
    """


_ClientUpdateRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientUpdateRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRateBasedRuleResponseTypeDef(
    _ClientUpdateRateBasedRuleResponseTypeDef
):
    """
    Type definition for `ClientUpdateRateBasedRule` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateRateBasedRule`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateRateBasedRuleUpdatesPredicateTypeDef = TypedDict(
    "_ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
)


class ClientUpdateRateBasedRuleUpdatesPredicateTypeDef(
    _ClientUpdateRateBasedRuleUpdatesPredicateTypeDef
):
    """
    Type definition for `ClientUpdateRateBasedRuleUpdates` `Predicate`

    The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

    - **Negated** *(boolean) --* **[REQUIRED]**

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based
      on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
      ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests
      based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the
      negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
      ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count
      requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --* **[REQUIRED]**

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --* **[REQUIRED]**

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientUpdateRateBasedRuleUpdatesTypeDef = TypedDict(
    "_ClientUpdateRateBasedRuleUpdatesTypeDef",
    {"Action": str, "Predicate": ClientUpdateRateBasedRuleUpdatesPredicateTypeDef},
)


class ClientUpdateRateBasedRuleUpdatesTypeDef(_ClientUpdateRateBasedRuleUpdatesTypeDef):
    """
    Type definition for `ClientUpdateRateBasedRule` `Updates`

    Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to a
    ``Rule`` or delete it from a ``Rule`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a
      ``Predicate`` from a ``Rule`` .

    - **Predicate** *(dict) --* **[REQUIRED]**

      The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

      - **Negated** *(boolean) --* **[REQUIRED]**

        Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based
        on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
        XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
        ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests
        based on that IP address.

        Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the
        negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
        XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
        ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count
        requests based on all IP addresses *except*  ``192.0.2.44`` .

      - **Type** *(string) --* **[REQUIRED]**

        The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

      - **DataId** *(string) --* **[REQUIRED]**

        A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
        ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientUpdateRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRegexMatchSetResponseTypeDef(
    _ClientUpdateRegexMatchSetResponseTypeDef
):
    """
    Type definition for `ClientUpdateRegexMatchSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateRegexMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_RequiredClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef = TypedDict(
    "_RequiredClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    {"Type": str},
)
_OptionalClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef = TypedDict(
    "_OptionalClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    {"Data": str},
    total=False,
)


class ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef(
    _RequiredClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef,
    _OptionalClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef,
):
    """
    Type definition for `ClientUpdateRegexMatchSetUpdatesRegexMatchTuple` `FieldToMatch`

    Specifies where in a web request to look for the ``RegexPatternSet`` .

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes of
      the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef,
        "TextTransformation": str,
        "RegexPatternSetId": str,
    },
)


class ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef(
    _ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef
):
    """
    Type definition for `ClientUpdateRegexMatchSetUpdates` `RegexMatchTuple`

    Information about the part of a web request that you want AWS WAF to inspect and the
    identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If
    you specify ``DELETE`` for the value of ``Action`` , the ``RegexMatchTuple`` values must
    exactly match the values in the ``RegexMatchTuple`` that you want to delete from the
    ``RegexMatchSet`` .

    - **FieldToMatch** *(dict) --* **[REQUIRED]**

      Specifies where in a web request to look for the ``RegexPatternSet`` .

      - **Type** *(string) --* **[REQUIRED]**

        The part of the web request that you want AWS WAF to search for a specified string. Parts
        of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
        or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
        header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
        asking the origin to perform. Amazon CloudFront supports the following methods:
        ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The request
        body immediately follows the request headers. Note that only the first ``8192`` bytes of
        the request body are forwarded to AWS WAF for inspection. To allow or block requests
        based on the length of the body, you can create a size constraint set. For more
        information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
        characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value or
        regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
        WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
        case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
        you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
        name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --* **[REQUIRED]**

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
      the transformation on ``RegexPatternSet`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system commandline command
      and using unusual formatting to disguise some or all of the command, use this option to
      perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
      with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
      the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

    - **RegexPatternSetId** *(string) --* **[REQUIRED]**

      The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
      information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
      ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
      ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), and
      delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

       ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientUpdateRegexMatchSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetUpdatesTypeDef",
    {
        "Action": str,
        "RegexMatchTuple": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef,
    },
)


class ClientUpdateRegexMatchSetUpdatesTypeDef(_ClientUpdateRegexMatchSetUpdatesTypeDef):
    """
    Type definition for `ClientUpdateRegexMatchSet` `Updates`

    In an  UpdateRegexMatchSet request, ``RegexMatchSetUpdate`` specifies whether to insert or
    delete a  RegexMatchTuple and includes the settings for the ``RegexMatchTuple`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert or delete a  RegexMatchTuple .

    - **RegexMatchTuple** *(dict) --* **[REQUIRED]**

      Information about the part of a web request that you want AWS WAF to inspect and the
      identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If
      you specify ``DELETE`` for the value of ``Action`` , the ``RegexMatchTuple`` values must
      exactly match the values in the ``RegexMatchTuple`` that you want to delete from the
      ``RegexMatchSet`` .

      - **FieldToMatch** *(dict) --* **[REQUIRED]**

        Specifies where in a web request to look for the ``RegexPatternSet`` .

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes of
          the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .

      - **TextTransformation** *(string) --* **[REQUIRED]**

        Text transformations eliminate some of the unusual formatting that attackers use in web
        requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
        the transformation on ``RegexPatternSet`` before inspecting a request for a match.

        You can only specify a single type of TextTransformation.

         **CMD_LINE**

        When you're concerned that attackers are injecting an operating system commandline command
        and using unusual formatting to disguise some or all of the command, use this option to
        perform the following transformations:

        * Delete the following characters: \\ " ' ^

        * Delete spaces before the following characters: / (

        * Replace the following characters with a space: , ;

        * Replace multiple spaces with one space

        * Convert uppercase letters (A-Z) to lowercase (a-z)

         **COMPRESS_WHITE_SPACE**

        Use this option to replace the following characters with a space character (decimal 32):

        * \\f, formfeed, decimal 12

        * \\t, tab, decimal 9

        * \\n, newline, decimal 10

        * \\r, carriage return, decimal 13

        * \\v, vertical tab, decimal 11

        * non-breaking space, decimal 160

         ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

         **HTML_ENTITY_DECODE**

        Use this option to replace HTML-encoded characters with unencoded characters.
        ``HTML_ENTITY_DECODE`` performs the following operations:

        * Replaces ``(ampersand)quot;`` with ``"``

        * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

        * Replaces ``(ampersand)lt;`` with a "less than" symbol

        * Replaces ``(ampersand)gt;`` with ``>``

        * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
        with the corresponding characters

        * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
        the corresponding characters

         **LOWERCASE**

        Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

         **URL_DECODE**

        Use this option to decode a URL-encoded value.

         **NONE**

        Specify ``NONE`` if you don't want to perform any text transformations.

      - **RegexPatternSetId** *(string) --* **[REQUIRED]**

        The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
        information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a
        ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a
        ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), and
        delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

         ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientUpdateRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientUpdateRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRegexPatternSetResponseTypeDef(
    _ClientUpdateRegexPatternSetResponseTypeDef
):
    """
    Type definition for `ClientUpdateRegexPatternSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateRegexPatternSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateRegexPatternSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateRegexPatternSetUpdatesTypeDef",
    {"Action": str, "RegexPatternString": str},
)


class ClientUpdateRegexPatternSetUpdatesTypeDef(
    _ClientUpdateRegexPatternSetUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateRegexPatternSet` `Updates`

    In an  UpdateRegexPatternSet request, ``RegexPatternSetUpdate`` specifies whether to insert or
    delete a ``RegexPatternString`` and includes the settings for the ``RegexPatternString`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert or delete a ``RegexPatternString`` .

    - **RegexPatternString** *(string) --* **[REQUIRED]**

      Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as
      ``B[a@]dB[o0]t`` .
    """


_ClientUpdateRuleGroupResponseTypeDef = TypedDict(
    "_ClientUpdateRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRuleGroupResponseTypeDef(_ClientUpdateRuleGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateRuleGroup` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateRuleGroup`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef", {"Type": str}
)


class ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef
):
    """
    Type definition for `ClientUpdateRuleGroupUpdatesActivatedRule` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the web
    ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
     ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
     requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --* **[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
      ``WebACL`` .
    """


_ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}
)


class ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef
):
    """
    Type definition for `ClientUpdateRuleGroupUpdatesActivatedRule` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
    refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
    by the ``ActivatedRule`` .

    - **RuleId** *(string) --* **[REQUIRED]**

      The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef", {"Type": str}
)


class ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef
):
    """
    Type definition for `ClientUpdateRuleGroupUpdatesActivatedRule` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
    rule in the ``RuleGroup`` matches the request and is configured to block that request.
    However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
    ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
    rules contained within the group. Instead of blocking matching requests, those requests
    will be counted. You can view a record of counted requests using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
     ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
     requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --* **[REQUIRED]**

       ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
       If set to ``NONE`` , the rule's action will take place.
    """


_RequiredClientUpdateRuleGroupUpdatesActivatedRuleTypeDef = TypedDict(
    "_RequiredClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    {"Priority": int, "RuleId": str},
)
_OptionalClientUpdateRuleGroupUpdatesActivatedRuleTypeDef = TypedDict(
    "_OptionalClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    {
        "Action": ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[
            ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef(
    _RequiredClientUpdateRuleGroupUpdatesActivatedRuleTypeDef,
    _OptionalClientUpdateRuleGroupUpdatesActivatedRuleTypeDef,
):
    """
    Type definition for `ClientUpdateRuleGroupUpdates` `ActivatedRule`

    The ``ActivatedRule`` object specifies a ``Rule`` that you want to insert or delete, the
    priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take
    when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

    - **Priority** *(integer) --* **[REQUIRED]**

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value
      must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't
      need to be consecutive.

    - **RuleId** *(string) --* **[REQUIRED]**

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule``
      (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL``
      or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF
      (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the web
      ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
       ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
       requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --* **[REQUIRED]**

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
        ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
      rule in the ``RuleGroup`` matches the request and is configured to block that request.
      However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
      ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
      rules contained within the group. Instead of blocking matching requests, those requests
      will be counted. You can view a record of counted requests using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
       ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
       requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --* **[REQUIRED]**

         ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
         If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
      RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although
      this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL
      without setting the type, the  UpdateWebACL request will fail because the request tries to
      add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the specific
      rule within the rule group that is blocking the legitimate traffic and then disable
      (exclude) that particular rule. You can exclude rules from both your own rule groups and
      AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
      changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
      metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web ACL,
      perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more
      information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
        you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
        refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
        by the ``ActivatedRule`` .

        - **RuleId** *(string) --* **[REQUIRED]**

          The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateRuleGroupUpdatesTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesTypeDef",
    {"Action": str, "ActivatedRule": ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef},
)


class ClientUpdateRuleGroupUpdatesTypeDef(_ClientUpdateRuleGroupUpdatesTypeDef):
    """
    Type definition for `ClientUpdateRuleGroup` `Updates`

    Specifies an ``ActivatedRule`` and indicates whether you want to add it to a ``RuleGroup`` or
    delete it from a ``RuleGroup`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add an ``ActivatedRule`` to a ``RuleGroup`` . Use ``DELETE`` to remove
      an ``ActivatedRule`` from a ``RuleGroup`` .

    - **ActivatedRule** *(dict) --* **[REQUIRED]**

      The ``ActivatedRule`` object specifies a ``Rule`` that you want to insert or delete, the
      priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take
      when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

      - **Priority** *(integer) --* **[REQUIRED]**

        Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
        lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value
        must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't
        need to be consecutive.

      - **RuleId** *(string) --* **[REQUIRED]**

        The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule``
        (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL``
        or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF
        (see  DeleteRule ).

         ``RuleId`` is returned by  CreateRule and by  ListRules .

      - **Action** *(dict) --*

        Specifies the action that CloudFront or AWS WAF takes when a web request matches the
        conditions in the ``Rule`` . Valid values for ``Action`` include the following:

        * ``ALLOW`` : CloudFront responds with the requested object.

        * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

        * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
        rule and then continues to inspect the web request based on the remaining rules in the web
        ACL.

         ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
         ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
         requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

        - **Type** *(string) --* **[REQUIRED]**

          Specifies how you want AWS WAF to respond to requests that match the settings in a
          ``Rule`` . Valid settings include the following:

          * ``ALLOW`` : AWS WAF allows requests

          * ``BLOCK`` : AWS WAF blocks requests

          * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
          conditions in the rule. AWS WAF then continues to inspect the web request based on the
          remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
          ``WebACL`` .

      - **OverrideAction** *(dict) --*

        Use the ``OverrideAction`` to test your ``RuleGroup`` .

        Any rule in a ``RuleGroup`` can potentially block a request. If you set the
        ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
        rule in the ``RuleGroup`` matches the request and is configured to block that request.
        However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
        ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
        rules contained within the group. Instead of blocking matching requests, those requests
        will be counted. You can view a record of counted requests using  GetSampledRequests .

         ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
         ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
         requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

        - **Type** *(string) --* **[REQUIRED]**

           ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
           If set to ``NONE`` , the rule's action will take place.

      - **Type** *(string) --*

        The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
        RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although
        this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL
        without setting the type, the  UpdateWebACL request will fail because the request tries to
        add a REGULAR rule with the specified ID, which does not exist.

      - **ExcludedRules** *(list) --*

        An array of rules to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` .

        Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
        unexpectedly (false positives). One troubleshooting technique is to identify the specific
        rule within the rule group that is blocking the legitimate traffic and then disable
        (exclude) that particular rule. You can exclude rules from both your own rule groups and
        AWS Marketplace rule groups that have been associated with a web ACL.

        Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
        changes the action for the rules to ``COUNT`` . Therefore, requests that match an
        ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
        metrics for each ``ExcludedRule`` .

        If you want to exclude rules from a rule group that is already associated with a web ACL,
        perform the following steps:

        * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more
        information about the logs, see `Logging Web ACL Traffic Information
        <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

        * Submit an  UpdateWebACL request that has two actions:

          * The first action deletes the existing rule group from the web ACL. That is, in the
          UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
          ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
          you want to exclude.

          * The second action inserts the same rule group back in, but specifying the rules to
          exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
          ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
          ``ExcludedRules`` should contain the rules that you want to exclude.

        - *(dict) --*

          The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
          refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
          by the ``ActivatedRule`` .

          - **RuleId** *(string) --* **[REQUIRED]**

            The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateRuleResponseTypeDef = TypedDict(
    "_ClientUpdateRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRuleResponseTypeDef(_ClientUpdateRuleResponseTypeDef):
    """
    Type definition for `ClientUpdateRule` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateRule`` request. You can also use this
      value to query the status of the request. For more information, see  GetChangeTokenStatus .
    """


_ClientUpdateRuleUpdatesPredicateTypeDef = TypedDict(
    "_ClientUpdateRuleUpdatesPredicateTypeDef",
    {"Negated": bool, "Type": str, "DataId": str},
)


class ClientUpdateRuleUpdatesPredicateTypeDef(_ClientUpdateRuleUpdatesPredicateTypeDef):
    """
    Type definition for `ClientUpdateRuleUpdates` `Predicate`

    The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

    - **Negated** *(boolean) --* **[REQUIRED]**

      Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based
      on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
      ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests
      based on that IP address.

      Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the
      negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
      XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
      ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count
      requests based on all IP addresses *except*  ``192.0.2.44`` .

    - **Type** *(string) --* **[REQUIRED]**

      The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

    - **DataId** *(string) --* **[REQUIRED]**

      A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
      ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientUpdateRuleUpdatesTypeDef = TypedDict(
    "_ClientUpdateRuleUpdatesTypeDef",
    {"Action": str, "Predicate": ClientUpdateRuleUpdatesPredicateTypeDef},
)


class ClientUpdateRuleUpdatesTypeDef(_ClientUpdateRuleUpdatesTypeDef):
    """
    Type definition for `ClientUpdateRule` `Updates`

    Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to a
    ``Rule`` or delete it from a ``Rule`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a
      ``Predicate`` from a ``Rule`` .

    - **Predicate** *(dict) --* **[REQUIRED]**

      The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

      - **Negated** *(boolean) --* **[REQUIRED]**

        Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based
        on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
        XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
        ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests
        based on that IP address.

        Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the
        negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,
        XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an
        ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count
        requests based on all IP addresses *except*  ``192.0.2.44`` .

      - **Type** *(string) --* **[REQUIRED]**

        The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

      - **DataId** *(string) --* **[REQUIRED]**

        A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or
        ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
    """


_ClientUpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateSizeConstraintSetResponseTypeDef(
    _ClientUpdateSizeConstraintSetResponseTypeDef
):
    """
    Type definition for `ClientUpdateSizeConstraintSet` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateSizeConstraintSet`` request. You can
      also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_RequiredClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef = TypedDict(
    "_RequiredClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    {"Type": str},
)
_OptionalClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef = TypedDict(
    "_OptionalClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    {"Data": str},
    total=False,
)


class ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef(
    _RequiredClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef,
    _OptionalClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef,
):
    """
    Type definition for `ClientUpdateSizeConstraintSetUpdatesSizeConstraint` `FieldToMatch`

    Specifies where in a web request to look for the size constraint.

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes of
      the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    {
        "FieldToMatch": ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef,
        "TextTransformation": str,
        "ComparisonOperator": str,
        "Size": int,
    },
)


class ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef(
    _ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef
):
    """
    Type definition for `ClientUpdateSizeConstraintSetUpdates` `SizeConstraint`

    Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` ,
    ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of "``Size``
     ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the
     ``SizeConstraint`` is considered to match.

    - **FieldToMatch** *(dict) --* **[REQUIRED]**

      Specifies where in a web request to look for the size constraint.

      - **Type** *(string) --* **[REQUIRED]**

        The part of the web request that you want AWS WAF to search for a specified string. Parts
        of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
        or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
        header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
        asking the origin to perform. Amazon CloudFront supports the following methods:
        ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The request
        body immediately follows the request headers. Note that only the first ``8192`` bytes of
        the request body are forwarded to AWS WAF for inspection. To allow or block requests
        based on the length of the body, you can create a size constraint set. For more
        information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
        characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value or
        regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
        WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
        case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
        you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
        name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --* **[REQUIRED]**

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
      the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

      Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for
      ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for inspection.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line command
      and using unusual formatting to disguise some or all of the command, use this option to
      perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
      with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
      the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

    - **ComparisonOperator** *(string) --* **[REQUIRED]**

      The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with
      the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of "``Size``
      ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the
      ``SizeConstraint`` is considered to match.

       **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

       **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

       **LE** : Used to test if the ``Size`` is less than or equal to the size of the
       ``FieldToMatch``

       **LT** : Used to test if the ``Size`` is strictly less than the size of the
       ``FieldToMatch``

       **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
       ``FieldToMatch``

       **GT** : Used to test if the ``Size`` is strictly greater than the size of the
       ``FieldToMatch``

    - **Size** *(integer) --* **[REQUIRED]**

      The size in bytes that you want AWS WAF to compare against the size of the specified
      ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
      ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator``
      size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is
      considered to match.

      Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

      If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
      character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientUpdateSizeConstraintSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetUpdatesTypeDef",
    {
        "Action": str,
        "SizeConstraint": ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef,
    },
)


class ClientUpdateSizeConstraintSetUpdatesTypeDef(
    _ClientUpdateSizeConstraintSetUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateSizeConstraintSet` `Updates`

    Specifies the part of a web request that you want to inspect the size of and indicates whether
    you want to add the specification to a  SizeConstraintSet or delete it from a
    ``SizeConstraintSet`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add a  SizeConstraintSetUpdate to a  SizeConstraintSet . Use ``DELETE``
      to remove a ``SizeConstraintSetUpdate`` from a ``SizeConstraintSet`` .

    - **SizeConstraint** *(dict) --* **[REQUIRED]**

      Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` ,
      ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of "``Size``
       ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the
       ``SizeConstraint`` is considered to match.

      - **FieldToMatch** *(dict) --* **[REQUIRED]**

        Specifies where in a web request to look for the size constraint.

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes of
          the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .

      - **TextTransformation** *(string) --* **[REQUIRED]**

        Text transformations eliminate some of the unusual formatting that attackers use in web
        requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
        the transformation on ``FieldToMatch`` before inspecting a request for a match.

        You can only specify a single type of TextTransformation.

        Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for
        ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for inspection.

         **NONE**

        Specify ``NONE`` if you don't want to perform any text transformations.

         **CMD_LINE**

        When you're concerned that attackers are injecting an operating system command line command
        and using unusual formatting to disguise some or all of the command, use this option to
        perform the following transformations:

        * Delete the following characters: \\ " ' ^

        * Delete spaces before the following characters: / (

        * Replace the following characters with a space: , ;

        * Replace multiple spaces with one space

        * Convert uppercase letters (A-Z) to lowercase (a-z)

         **COMPRESS_WHITE_SPACE**

        Use this option to replace the following characters with a space character (decimal 32):

        * \\f, formfeed, decimal 12

        * \\t, tab, decimal 9

        * \\n, newline, decimal 10

        * \\r, carriage return, decimal 13

        * \\v, vertical tab, decimal 11

        * non-breaking space, decimal 160

         ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

         **HTML_ENTITY_DECODE**

        Use this option to replace HTML-encoded characters with unencoded characters.
        ``HTML_ENTITY_DECODE`` performs the following operations:

        * Replaces ``(ampersand)quot;`` with ``"``

        * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

        * Replaces ``(ampersand)lt;`` with a "less than" symbol

        * Replaces ``(ampersand)gt;`` with ``>``

        * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
        with the corresponding characters

        * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
        the corresponding characters

         **LOWERCASE**

        Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

         **URL_DECODE**

        Use this option to decode a URL-encoded value.

      - **ComparisonOperator** *(string) --* **[REQUIRED]**

        The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with
        the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of "``Size``
        ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the
        ``SizeConstraint`` is considered to match.

         **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

         **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

         **LE** : Used to test if the ``Size`` is less than or equal to the size of the
         ``FieldToMatch``

         **LT** : Used to test if the ``Size`` is strictly less than the size of the
         ``FieldToMatch``

         **GE** : Used to test if the ``Size`` is greater than or equal to the size of the
         ``FieldToMatch``

         **GT** : Used to test if the ``Size`` is strictly greater than the size of the
         ``FieldToMatch``

      - **Size** *(integer) --* **[REQUIRED]**

        The size in bytes that you want AWS WAF to compare against the size of the specified
        ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and
        ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator``
        size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is
        considered to match.

        Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

        If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one
        character. For example, the URI ``/logo.jpg`` is nine characters long.
    """


_ClientUpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetResponseTypeDef",
    {"ChangeToken": str},
    total=False,
)


class ClientUpdateSqlInjectionMatchSetResponseTypeDef(
    _ClientUpdateSqlInjectionMatchSetResponseTypeDef
):
    """
    Type definition for `ClientUpdateSqlInjectionMatchSet` `Response`

    The response to an  UpdateSqlInjectionMatchSets request.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateSqlInjectionMatchSet`` request. You
      can also use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_RequiredClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef = TypedDict(
    "_RequiredClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    {"Type": str},
)
_OptionalClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef = TypedDict(
    "_OptionalClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    {"Data": str},
    total=False,
)


class ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef(
    _RequiredClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef,
    _OptionalClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef,
):
    """
    Type definition for `ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTuple` `FieldToMatch`

    Specifies where in a web request to look for snippets of malicious SQL code.

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes of
      the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef,
        "TextTransformation": str,
    },
)


class ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef(
    _ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef
):
    """
    Type definition for `ClientUpdateSqlInjectionMatchSetUpdates` `SqlInjectionMatchTuple`

    Specifies the part of a web request that you want AWS WAF to inspect for snippets of
    malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --* **[REQUIRED]**

      Specifies where in a web request to look for snippets of malicious SQL code.

      - **Type** *(string) --* **[REQUIRED]**

        The part of the web request that you want AWS WAF to search for a specified string. Parts
        of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
        or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
        header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
        asking the origin to perform. Amazon CloudFront supports the following methods:
        ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The request
        body immediately follows the request headers. Note that only the first ``8192`` bytes of
        the request body are forwarded to AWS WAF for inspection. To allow or block requests
        based on the length of the body, you can create a size constraint set. For more
        information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
        characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value or
        regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
        WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
        case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
        you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
        name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --* **[REQUIRED]**

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
      the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line command
      and using unusual formatting to disguise some or all of the command, use this option to
      perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
      with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
      the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientUpdateSqlInjectionMatchSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    {
        "Action": str,
        "SqlInjectionMatchTuple": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef,
    },
)


class ClientUpdateSqlInjectionMatchSetUpdatesTypeDef(
    _ClientUpdateSqlInjectionMatchSetUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateSqlInjectionMatchSet` `Updates`

    Specifies the part of a web request that you want to inspect for snippets of malicious SQL code
    and indicates whether you want to add the specification to a  SqlInjectionMatchSet or delete it
    from a ``SqlInjectionMatchSet`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add a  SqlInjectionMatchSetUpdate to a  SqlInjectionMatchSet . Use
      ``DELETE`` to remove a ``SqlInjectionMatchSetUpdate`` from a ``SqlInjectionMatchSet`` .

    - **SqlInjectionMatchTuple** *(dict) --* **[REQUIRED]**

      Specifies the part of a web request that you want AWS WAF to inspect for snippets of
      malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

      - **FieldToMatch** *(dict) --* **[REQUIRED]**

        Specifies where in a web request to look for snippets of malicious SQL code.

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes of
          the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .

      - **TextTransformation** *(string) --* **[REQUIRED]**

        Text transformations eliminate some of the unusual formatting that attackers use in web
        requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
        the transformation on ``FieldToMatch`` before inspecting a request for a match.

        You can only specify a single type of TextTransformation.

         **CMD_LINE**

        When you're concerned that attackers are injecting an operating system command line command
        and using unusual formatting to disguise some or all of the command, use this option to
        perform the following transformations:

        * Delete the following characters: \\ " ' ^

        * Delete spaces before the following characters: / (

        * Replace the following characters with a space: , ;

        * Replace multiple spaces with one space

        * Convert uppercase letters (A-Z) to lowercase (a-z)

         **COMPRESS_WHITE_SPACE**

        Use this option to replace the following characters with a space character (decimal 32):

        * \\f, formfeed, decimal 12

        * \\t, tab, decimal 9

        * \\n, newline, decimal 10

        * \\r, carriage return, decimal 13

        * \\v, vertical tab, decimal 11

        * non-breaking space, decimal 160

         ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

         **HTML_ENTITY_DECODE**

        Use this option to replace HTML-encoded characters with unencoded characters.
        ``HTML_ENTITY_DECODE`` performs the following operations:

        * Replaces ``(ampersand)quot;`` with ``"``

        * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

        * Replaces ``(ampersand)lt;`` with a "less than" symbol

        * Replaces ``(ampersand)gt;`` with ``>``

        * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
        with the corresponding characters

        * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
        the corresponding characters

         **LOWERCASE**

        Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

         **URL_DECODE**

        Use this option to decode a URL-encoded value.

         **NONE**

        Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientUpdateWebAclDefaultActionTypeDef = TypedDict(
    "_ClientUpdateWebAclDefaultActionTypeDef", {"Type": str}
)


class ClientUpdateWebAclDefaultActionTypeDef(_ClientUpdateWebAclDefaultActionTypeDef):
    """
    Type definition for `ClientUpdateWebAcl` `DefaultAction`

    A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a
    request doesn't match the criteria in any of the rules in a web ACL.

    - **Type** *(string) --* **[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` .
      Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in
      the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the
      web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` .
    """


_ClientUpdateWebAclResponseTypeDef = TypedDict(
    "_ClientUpdateWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateWebAclResponseTypeDef(_ClientUpdateWebAclResponseTypeDef):
    """
    Type definition for `ClientUpdateWebAcl` `Response`

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateWebACL`` request. You can also use
      this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef", {"Type": str}
)


class ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef
):
    """
    Type definition for `ClientUpdateWebAclUpdatesActivatedRule` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the web
    ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
     ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
     requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --* **[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
      ``WebACL`` .
    """


_ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}
)


class ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef
):
    """
    Type definition for `ClientUpdateWebAclUpdatesActivatedRule` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
    refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
    by the ``ActivatedRule`` .

    - **RuleId** *(string) --* **[REQUIRED]**

      The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef", {"Type": str}
)


class ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef
):
    """
    Type definition for `ClientUpdateWebAclUpdatesActivatedRule` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
    rule in the ``RuleGroup`` matches the request and is configured to block that request.
    However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
    ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
    rules contained within the group. Instead of blocking matching requests, those requests
    will be counted. You can view a record of counted requests using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
     ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
     requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --* **[REQUIRED]**

       ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
       If set to ``NONE`` , the rule's action will take place.
    """


_RequiredClientUpdateWebAclUpdatesActivatedRuleTypeDef = TypedDict(
    "_RequiredClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    {"Priority": int, "RuleId": str},
)
_OptionalClientUpdateWebAclUpdatesActivatedRuleTypeDef = TypedDict(
    "_OptionalClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    {
        "Action": ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[
            ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateWebAclUpdatesActivatedRuleTypeDef(
    _RequiredClientUpdateWebAclUpdatesActivatedRuleTypeDef,
    _OptionalClientUpdateWebAclUpdatesActivatedRuleTypeDef,
):
    """
    Type definition for `ClientUpdateWebAclUpdates` `ActivatedRule`

    The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
    to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you
    want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or
    ``COUNT`` ).

    - **Priority** *(integer) --* **[REQUIRED]**

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value
      must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't
      need to be consecutive.

    - **RuleId** *(string) --* **[REQUIRED]**

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule``
      (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL``
      or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF
      (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the web
      ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
       ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
       requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --* **[REQUIRED]**

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
        ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
      rule in the ``RuleGroup`` matches the request and is configured to block that request.
      However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
      ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
      rules contained within the group. Instead of blocking matching requests, those requests
      will be counted. You can view a record of counted requests using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
       ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
       requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --* **[REQUIRED]**

         ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
         If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
      RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although
      this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL
      without setting the type, the  UpdateWebACL request will fail because the request tries to
      add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the specific
      rule within the rule group that is blocking the legitimate traffic and then disable
      (exclude) that particular rule. You can exclude rules from both your own rule groups and
      AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
      changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
      metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web ACL,
      perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more
      information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
        you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
        refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
        by the ``ActivatedRule`` .

        - **RuleId** *(string) --* **[REQUIRED]**

          The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateWebAclUpdatesTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesTypeDef",
    {"Action": str, "ActivatedRule": ClientUpdateWebAclUpdatesActivatedRuleTypeDef},
)


class ClientUpdateWebAclUpdatesTypeDef(_ClientUpdateWebAclUpdatesTypeDef):
    """
    Type definition for `ClientUpdateWebAcl` `Updates`

    Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .

    - **ActivatedRule** *(dict) --* **[REQUIRED]**

      The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
      to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you
      want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or
      ``COUNT`` ).

      - **Priority** *(integer) --* **[REQUIRED]**

        Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
        lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value
        must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't
        need to be consecutive.

      - **RuleId** *(string) --* **[REQUIRED]**

        The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule``
        (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL``
        or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF
        (see  DeleteRule ).

         ``RuleId`` is returned by  CreateRule and by  ListRules .

      - **Action** *(dict) --*

        Specifies the action that CloudFront or AWS WAF takes when a web request matches the
        conditions in the ``Rule`` . Valid values for ``Action`` include the following:

        * ``ALLOW`` : CloudFront responds with the requested object.

        * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

        * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
        rule and then continues to inspect the web request based on the remaining rules in the web
        ACL.

         ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
         ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update
         requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

        - **Type** *(string) --* **[REQUIRED]**

          Specifies how you want AWS WAF to respond to requests that match the settings in a
          ``Rule`` . Valid settings include the following:

          * ``ALLOW`` : AWS WAF allows requests

          * ``BLOCK`` : AWS WAF blocks requests

          * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
          conditions in the rule. AWS WAF then continues to inspect the web request based on the
          remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a
          ``WebACL`` .

      - **OverrideAction** *(dict) --*

        Use the ``OverrideAction`` to test your ``RuleGroup`` .

        Any rule in a ``RuleGroup`` can potentially block a request. If you set the
        ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
        rule in the ``RuleGroup`` matches the request and is configured to block that request.
        However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
        ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
        rules contained within the group. Instead of blocking matching requests, those requests
        will be counted. You can view a record of counted requests using  GetSampledRequests .

         ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a
         ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update
         requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .

        - **Type** *(string) --* **[REQUIRED]**

           ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` .
           If set to ``NONE`` , the rule's action will take place.

      - **Type** *(string) --*

        The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
        RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although
        this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL
        without setting the type, the  UpdateWebACL request will fail because the request tries to
        add a REGULAR rule with the specified ID, which does not exist.

      - **ExcludedRules** *(list) --*

        An array of rules to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` .

        Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
        unexpectedly (false positives). One troubleshooting technique is to identify the specific
        rule within the rule group that is blocking the legitimate traffic and then disable
        (exclude) that particular rule. You can exclude rules from both your own rule groups and
        AWS Marketplace rule groups that have been associated with a web ACL.

        Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
        changes the action for the rules to ``COUNT`` . Therefore, requests that match an
        ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
        metrics for each ``ExcludedRule`` .

        If you want to exclude rules from a rule group that is already associated with a web ACL,
        perform the following steps:

        * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more
        information about the logs, see `Logging Web ACL Traffic Information
        <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

        * Submit an  UpdateWebACL request that has two actions:

          * The first action deletes the existing rule group from the web ACL. That is, in the
          UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
          ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
          you want to exclude.

          * The second action inserts the same rule group back in, but specifying the rules to
          exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
          ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
          ``ExcludedRules`` should contain the rules that you want to exclude.

        - *(dict) --*

          The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule``
          refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified
          by the ``ActivatedRule`` .

          - **RuleId** *(string) --* **[REQUIRED]**

            The unique identifier for the rule to exclude from the rule group.
    """


_ClientUpdateXssMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateXssMatchSetResponseTypeDef(_ClientUpdateXssMatchSetResponseTypeDef):
    """
    Type definition for `ClientUpdateXssMatchSet` `Response`

    The response to an  UpdateXssMatchSets request.

    - **ChangeToken** *(string) --*

      The ``ChangeToken`` that you used to submit the ``UpdateXssMatchSet`` request. You can also
      use this value to query the status of the request. For more information, see
      GetChangeTokenStatus .
    """


_RequiredClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef = TypedDict(
    "_RequiredClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    {"Type": str},
)
_OptionalClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef = TypedDict(
    "_OptionalClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    {"Data": str},
    total=False,
)


class ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef(
    _RequiredClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef,
    _OptionalClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef,
):
    """
    Type definition for `ClientUpdateXssMatchSetUpdatesXssMatchTuple` `FieldToMatch`

    Specifies where in a web request to look for cross-site scripting attacks.

    - **Type** *(string) --* **[REQUIRED]**

      The part of the web request that you want AWS WAF to search for a specified string. Parts
      of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
      or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
      header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
      asking the origin to perform. Amazon CloudFront supports the following methods:
      ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The request
      body immediately follows the request headers. Note that only the first ``8192`` bytes of
      the request body are forwarded to AWS WAF for inspection. To allow or block requests
      based on the length of the body, you can create a size constraint set. For more
      information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
      *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
      characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value or
      regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
      WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
      case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
      you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
      name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef,
        "TextTransformation": str,
    },
)


class ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef(
    _ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef
):
    """
    Type definition for `ClientUpdateXssMatchSetUpdates` `XssMatchTuple`

    Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting
    attacks and, if you want AWS WAF to inspect a header, the name of the header.

    - **FieldToMatch** *(dict) --* **[REQUIRED]**

      Specifies where in a web request to look for cross-site scripting attacks.

      - **Type** *(string) --* **[REQUIRED]**

        The part of the web request that you want AWS WAF to search for a specified string. Parts
        of a request that you can search include the following:

        * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
        or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
        header in ``Data`` .

        * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
        asking the origin to perform. Amazon CloudFront supports the following methods:
        ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

        * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
        ``?`` character, if any.

        * ``URI`` : The part of a web request that identifies a resource, for example,
        ``/images/daily-ad.jpg`` .

        * ``BODY`` : The part of a request that contains any additional data that you want to
        send to your web server as the HTTP request body, such as data from a form. The request
        body immediately follows the request headers. Note that only the first ``8192`` bytes of
        the request body are forwarded to AWS WAF for inspection. To allow or block requests
        based on the length of the body, you can create a size constraint set. For more
        information, see  CreateSizeConstraintSet .

        * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
        *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
        characters.

        * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
        single parameter, AWS WAF will inspect all parameters within the query for the value or
        regex pattern that you specify in ``TargetString`` .

      - **Data** *(string) --*

        When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
        WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
        case sensitive.

        When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
        you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
        name is not case sensitive.

        If the value of ``Type`` is any other value, omit ``Data`` .

    - **TextTransformation** *(string) --* **[REQUIRED]**

      Text transformations eliminate some of the unusual formatting that attackers use in web
      requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
      the transformation on ``FieldToMatch`` before inspecting a request for a match.

      You can only specify a single type of TextTransformation.

       **CMD_LINE**

      When you're concerned that attackers are injecting an operating system command line command
      and using unusual formatting to disguise some or all of the command, use this option to
      perform the following transformations:

      * Delete the following characters: \\ " ' ^

      * Delete spaces before the following characters: / (

      * Replace the following characters with a space: , ;

      * Replace multiple spaces with one space

      * Convert uppercase letters (A-Z) to lowercase (a-z)

       **COMPRESS_WHITE_SPACE**

      Use this option to replace the following characters with a space character (decimal 32):

      * \\f, formfeed, decimal 12

      * \\t, tab, decimal 9

      * \\n, newline, decimal 10

      * \\r, carriage return, decimal 13

      * \\v, vertical tab, decimal 11

      * non-breaking space, decimal 160

       ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

       **HTML_ENTITY_DECODE**

      Use this option to replace HTML-encoded characters with unencoded characters.
      ``HTML_ENTITY_DECODE`` performs the following operations:

      * Replaces ``(ampersand)quot;`` with ``"``

      * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

      * Replaces ``(ampersand)lt;`` with a "less than" symbol

      * Replaces ``(ampersand)gt;`` with ``>``

      * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
      with the corresponding characters

      * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
      the corresponding characters

       **LOWERCASE**

      Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

       **URL_DECODE**

      Use this option to decode a URL-encoded value.

       **NONE**

      Specify ``NONE`` if you don't want to perform any text transformations.
    """


_ClientUpdateXssMatchSetUpdatesTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetUpdatesTypeDef",
    {
        "Action": str,
        "XssMatchTuple": ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef,
    },
)


class ClientUpdateXssMatchSetUpdatesTypeDef(_ClientUpdateXssMatchSetUpdatesTypeDef):
    """
    Type definition for `ClientUpdateXssMatchSet` `Updates`

    Specifies the part of a web request that you want to inspect for cross-site scripting attacks
    and indicates whether you want to add the specification to an  XssMatchSet or delete it from an
    ``XssMatchSet`` .

    - **Action** *(string) --* **[REQUIRED]**

      Specify ``INSERT`` to add an  XssMatchSetUpdate to an  XssMatchSet . Use ``DELETE`` to remove
      an ``XssMatchSetUpdate`` from an ``XssMatchSet`` .

    - **XssMatchTuple** *(dict) --* **[REQUIRED]**

      Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting
      attacks and, if you want AWS WAF to inspect a header, the name of the header.

      - **FieldToMatch** *(dict) --* **[REQUIRED]**

        Specifies where in a web request to look for cross-site scripting attacks.

        - **Type** *(string) --* **[REQUIRED]**

          The part of the web request that you want AWS WAF to search for a specified string. Parts
          of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent``
          or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the
          header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is
          asking the origin to perform. Amazon CloudFront supports the following methods:
          ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The request
          body immediately follows the request headers. Note that only the first ``8192`` bytes of
          the request body are forwarded to AWS WAF for inspection. To allow or block requests
          based on the length of the body, you can create a size constraint set. For more
          information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as
          *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30
          characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value or
          regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS
          WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not
          case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that
          you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter
          name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .

      - **TextTransformation** *(string) --* **[REQUIRED]**

        Text transformations eliminate some of the unusual formatting that attackers use in web
        requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs
        the transformation on ``FieldToMatch`` before inspecting a request for a match.

        You can only specify a single type of TextTransformation.

         **CMD_LINE**

        When you're concerned that attackers are injecting an operating system command line command
        and using unusual formatting to disguise some or all of the command, use this option to
        perform the following transformations:

        * Delete the following characters: \\ " ' ^

        * Delete spaces before the following characters: / (

        * Replace the following characters with a space: , ;

        * Replace multiple spaces with one space

        * Convert uppercase letters (A-Z) to lowercase (a-z)

         **COMPRESS_WHITE_SPACE**

        Use this option to replace the following characters with a space character (decimal 32):

        * \\f, formfeed, decimal 12

        * \\t, tab, decimal 9

        * \\n, newline, decimal 10

        * \\r, carriage return, decimal 13

        * \\v, vertical tab, decimal 11

        * non-breaking space, decimal 160

         ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

         **HTML_ENTITY_DECODE**

        Use this option to replace HTML-encoded characters with unencoded characters.
        ``HTML_ENTITY_DECODE`` performs the following operations:

        * Replaces ``(ampersand)quot;`` with ``"``

        * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160

        * Replaces ``(ampersand)lt;`` with a "less than" symbol

        * Replaces ``(ampersand)gt;`` with ``>``

        * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` ,
        with the corresponding characters

        * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with
        the corresponding characters

         **LOWERCASE**

        Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

         **URL_DECODE**

        Use this option to decode a URL-encoded value.

         **NONE**

        Specify ``NONE`` if you don't want to perform any text transformations.
    """


_GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef(
    _GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetRateBasedRuleManagedKeysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetRateBasedRuleManagedKeysPaginateResponseTypeDef = TypedDict(
    "_GetRateBasedRuleManagedKeysPaginateResponseTypeDef",
    {"ManagedKeys": List[str], "NextToken": str},
    total=False,
)


class GetRateBasedRuleManagedKeysPaginateResponseTypeDef(
    _GetRateBasedRuleManagedKeysPaginateResponseTypeDef
):
    """
    Type definition for `GetRateBasedRuleManagedKeysPaginate` `Response`

    - **ManagedKeys** *(list) --*

      An array of IP addresses that currently are blocked by the specified  RateBasedRule .

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef(
    _ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginate` `PaginationConfig`

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


_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef",
    {"Type": str},
    total=False,
)


class ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef(
    _ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginateResponseActivatedRules` `Action`

    Specifies the action that CloudFront or AWS WAF takes when a web request matches the
    conditions in the ``Rule`` . Valid values for ``Action`` include the following:

    * ``ALLOW`` : CloudFront responds with the requested object.

    * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

    * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
    rule and then continues to inspect the web request based on the remaining rules in the
    web ACL.

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
     a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

      Specifies how you want AWS WAF to respond to requests that match the settings in a
      ``Rule`` . Valid settings include the following:

      * ``ALLOW`` : AWS WAF allows requests

      * ``BLOCK`` : AWS WAF blocks requests

      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
      conditions in the rule. AWS WAF then continues to inspect the web request based on the
      remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
      a ``WebACL`` .
    """


_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)


class ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef(
    _ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginateResponseActivatedRules` `ExcludedRules`

    The rule to exclude from a rule group. This is applicable only when the
    ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
    that is specified by the ``ActivatedRule`` .

    - **RuleId** *(string) --*

      The unique identifier for the rule to exclude from the rule group.
    """


_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef",
    {"Type": str},
    total=False,
)


class ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef(
    _ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginateResponseActivatedRules` `OverrideAction`

    Use the ``OverrideAction`` to test your ``RuleGroup`` .

    Any rule in a ``RuleGroup`` can potentially block a request. If you set the
    ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
    rule in the ``RuleGroup`` matches the request and is configured to block that request.
    However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
    ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
    rules contained within the group. Instead of blocking matching requests, those requests
    will be counted. You can view a record of counted requests using  GetSampledRequests .

     ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
     a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
     update requests, ``ActivatedRule|Action`` is used instead of
     ``ActivatedRule|OverrideAction`` .

    - **Type** *(string) --*

       ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
       . If set to ``NONE`` , the rule's action will take place.
    """


_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesActionTypeDef,
        "OverrideAction": ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesOverrideActionTypeDef,
        "Type": str,
        "ExcludedRules": List[
            ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef(
    _ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginateResponse` `ActivatedRules`

    The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
    to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that
    you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` ,
    or ``COUNT`` ).

    To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
    WebACLUpdate data type.

    - **Priority** *(integer) --*

      Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
      lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
      value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
      values don't need to be consecutive.

    - **RuleId** *(string) --*

      The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Action** *(dict) --*

      Specifies the action that CloudFront or AWS WAF takes when a web request matches the
      conditions in the ``Rule`` . Valid values for ``Action`` include the following:

      * ``ALLOW`` : CloudFront responds with the requested object.

      * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

      * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
      rule and then continues to inspect the web request based on the remaining rules in the
      web ACL.

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
       a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

        Specifies how you want AWS WAF to respond to requests that match the settings in a
        ``Rule`` . Valid settings include the following:

        * ``ALLOW`` : AWS WAF allows requests

        * ``BLOCK`` : AWS WAF blocks requests

        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
        conditions in the rule. AWS WAF then continues to inspect the web request based on the
        remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
        a ``WebACL`` .

    - **OverrideAction** *(dict) --*

      Use the ``OverrideAction`` to test your ``RuleGroup`` .

      Any rule in a ``RuleGroup`` can potentially block a request. If you set the
      ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
      rule in the ``RuleGroup`` matches the request and is configured to block that request.
      However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
      ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
      rules contained within the group. Instead of blocking matching requests, those requests
      will be counted. You can view a record of counted requests using  GetSampledRequests .

       ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
       a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
       update requests, ``ActivatedRule|Action`` is used instead of
       ``ActivatedRule|OverrideAction`` .

      - **Type** *(string) --*

         ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
         . If set to ``NONE`` , the rule's action will take place.

    - **Type** *(string) --*

      The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
      RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
      Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
      web ACL without setting the type, the  UpdateWebACL request will fail because the request
      tries to add a REGULAR rule with the specified ID, which does not exist.

    - **ExcludedRules** *(list) --*

      An array of rules to exclude from a rule group. This is applicable only when the
      ``ActivatedRule`` refers to a ``RuleGroup`` .

      Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
      unexpectedly (false positives). One troubleshooting technique is to identify the specific
      rule within the rule group that is blocking the legitimate traffic and then disable
      (exclude) that particular rule. You can exclude rules from both your own rule groups and
      AWS Marketplace rule groups that have been associated with a web ACL.

      Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
      changes the action for the rules to ``COUNT`` . Therefore, requests that match an
      ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
      metrics for each ``ExcludedRule`` .

      If you want to exclude rules from a rule group that is already associated with a web ACL,
      perform the following steps:

      * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
      more information about the logs, see `Logging Web ACL Traffic Information
      <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

      * Submit an  UpdateWebACL request that has two actions:

        * The first action deletes the existing rule group from the web ACL. That is, in the
        UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
        ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
        you want to exclude.

        * The second action inserts the same rule group back in, but specifying the rules to
        exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
        ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
        ``ExcludedRules`` should contain the rules that you want to exclude.

      - *(dict) --*

        The rule to exclude from a rule group. This is applicable only when the
        ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
        that is specified by the ``ActivatedRule`` .

        - **RuleId** *(string) --*

          The unique identifier for the rule to exclude from the rule group.
    """


_ListActivatedRulesInRuleGroupPaginateResponseTypeDef = TypedDict(
    "_ListActivatedRulesInRuleGroupPaginateResponseTypeDef",
    {
        "ActivatedRules": List[
            ListActivatedRulesInRuleGroupPaginateResponseActivatedRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListActivatedRulesInRuleGroupPaginateResponseTypeDef(
    _ListActivatedRulesInRuleGroupPaginateResponseTypeDef
):
    """
    Type definition for `ListActivatedRulesInRuleGroupPaginate` `Response`

    - **ActivatedRules** *(list) --*

      An array of ``ActivatedRules`` objects.

      - *(dict) --*

        The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want
        to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that
        you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` ,
        or ``COUNT`` ).

        To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the
        WebACLUpdate data type.

        - **Priority** *(integer) --*

          Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a
          lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The
          value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the
          values don't need to be consecutive.

        - **RuleId** *(string) --*

          The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Action** *(dict) --*

          Specifies the action that CloudFront or AWS WAF takes when a web request matches the
          conditions in the ``Rule`` . Valid values for ``Action`` include the following:

          * ``ALLOW`` : CloudFront responds with the requested object.

          * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code.

          * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the
          rule and then continues to inspect the web request based on the remaining rules in the
          web ACL.

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
           a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

            Specifies how you want AWS WAF to respond to requests that match the settings in a
            ``Rule`` . Valid settings include the following:

            * ``ALLOW`` : AWS WAF allows requests

            * ``BLOCK`` : AWS WAF blocks requests

            * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the
            conditions in the rule. AWS WAF then continues to inspect the web request based on the
            remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for
            a ``WebACL`` .

        - **OverrideAction** *(dict) --*

          Use the ``OverrideAction`` to test your ``RuleGroup`` .

          Any rule in a ``RuleGroup`` can potentially block a request. If you set the
          ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual
          rule in the ``RuleGroup`` matches the request and is configured to block that request.
          However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to
          ``Count`` . The ``RuleGroup`` will then override any block action specified by individual
          rules contained within the group. Instead of blocking matching requests, those requests
          will be counted. You can view a record of counted requests using  GetSampledRequests .

           ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to
           a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other
           update requests, ``ActivatedRule|Action`` is used instead of
           ``ActivatedRule|OverrideAction`` .

          - **Type** *(string) --*

             ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup``
             . If set to ``NONE`` , the rule's action will take place.

        - **Type** *(string) --*

          The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by
          RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR.
          Although this field is optional, be aware that if you try to add a RATE_BASED rule to a
          web ACL without setting the type, the  UpdateWebACL request will fail because the request
          tries to add a REGULAR rule with the specified ID, which does not exist.

        - **ExcludedRules** *(list) --*

          An array of rules to exclude from a rule group. This is applicable only when the
          ``ActivatedRule`` refers to a ``RuleGroup`` .

          Sometimes it is necessary to troubleshoot rule groups that are blocking traffic
          unexpectedly (false positives). One troubleshooting technique is to identify the specific
          rule within the rule group that is blocking the legitimate traffic and then disable
          (exclude) that particular rule. You can exclude rules from both your own rule groups and
          AWS Marketplace rule groups that have been associated with a web ACL.

          Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it
          changes the action for the rules to ``COUNT`` . Therefore, requests that match an
          ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT
          metrics for each ``ExcludedRule`` .

          If you want to exclude rules from a rule group that is already associated with a web ACL,
          perform the following steps:

          * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For
          more information about the logs, see `Logging Web ACL Traffic Information
          <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ .

          * Submit an  UpdateWebACL request that has two actions:

            * The first action deletes the existing rule group from the web ACL. That is, in the
            UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and
            ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that
            you want to exclude.

            * The second action inserts the same rule group back in, but specifying the rules to
            exclude. That is, the second ``Updates:Action`` should be ``INSERT`` ,
            ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and
            ``ExcludedRules`` should contain the rules that you want to exclude.

          - *(dict) --*

            The rule to exclude from a rule group. This is applicable only when the
            ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup``
            that is specified by the ``ActivatedRule`` .

            - **RuleId** *(string) --*

              The unique identifier for the rule to exclude from the rule group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListByteMatchSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListByteMatchSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListByteMatchSetsPaginatePaginationConfigTypeDef(
    _ListByteMatchSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListByteMatchSetsPaginate` `PaginationConfig`

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


_ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef = TypedDict(
    "_ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef",
    {"ByteMatchSetId": str, "Name": str},
    total=False,
)


class ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef(
    _ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef
):
    """
    Type definition for `ListByteMatchSetsPaginateResponse` `ByteMatchSets`

    Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name``
    and ``ByteMatchSetId`` for one  ByteMatchSet .

    - **ByteMatchSetId** *(string) --*

      The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
      information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a
      ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.

       ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
      create a ``ByteMatchSet`` .
    """


_ListByteMatchSetsPaginateResponseTypeDef = TypedDict(
    "_ListByteMatchSetsPaginateResponseTypeDef",
    {
        "ByteMatchSets": List[ListByteMatchSetsPaginateResponseByteMatchSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListByteMatchSetsPaginateResponseTypeDef(
    _ListByteMatchSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListByteMatchSetsPaginate` `Response`

    - **ByteMatchSets** *(list) --*

      An array of  ByteMatchSetSummary objects.

      - *(dict) --*

        Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name``
        and ``ByteMatchSetId`` for one  ByteMatchSet .

        - **ByteMatchSetId** *(string) --*

          The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
          information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a
          ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.

           ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

        - **Name** *(string) --*

          A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you
          create a ``ByteMatchSet`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGeoMatchSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGeoMatchSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGeoMatchSetsPaginatePaginationConfigTypeDef(
    _ListGeoMatchSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGeoMatchSetsPaginate` `PaginationConfig`

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


_ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef = TypedDict(
    "_ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef",
    {"GeoMatchSetId": str, "Name": str},
    total=False,
)


class ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef(
    _ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef
):
    """
    Type definition for `ListGeoMatchSetsPaginateResponse` `GeoMatchSets`

    Contains the identifier and the name of the ``GeoMatchSet`` .

    - **GeoMatchSetId** *(string) --*

      The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a
      GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

    - **Name** *(string) --*

      A friendly name or description of the  GeoMatchSet . You can't change the name of an
      ``GeoMatchSet`` after you create it.
    """


_ListGeoMatchSetsPaginateResponseTypeDef = TypedDict(
    "_ListGeoMatchSetsPaginateResponseTypeDef",
    {
        "GeoMatchSets": List[ListGeoMatchSetsPaginateResponseGeoMatchSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListGeoMatchSetsPaginateResponseTypeDef(_ListGeoMatchSetsPaginateResponseTypeDef):
    """
    Type definition for `ListGeoMatchSetsPaginate` `Response`

    - **GeoMatchSets** *(list) --*

      An array of  GeoMatchSetSummary objects.

      - *(dict) --*

        Contains the identifier and the name of the ``GeoMatchSet`` .

        - **GeoMatchSetId** *(string) --*

          The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a
          GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

        - **Name** *(string) --*

          A friendly name or description of the  GeoMatchSet . You can't change the name of an
          ``GeoMatchSet`` after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListIPSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIPSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIPSetsPaginatePaginationConfigTypeDef(
    _ListIPSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIPSetsPaginate` `PaginationConfig`

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


_ListIPSetsPaginateResponseIPSetsTypeDef = TypedDict(
    "_ListIPSetsPaginateResponseIPSetsTypeDef",
    {"IPSetId": str, "Name": str},
    total=False,
)


class ListIPSetsPaginateResponseIPSetsTypeDef(_ListIPSetsPaginateResponseIPSetsTypeDef):
    """
    Type definition for `ListIPSetsPaginateResponse` `IPSets`

    Contains the identifier and the name of the ``IPSet`` .

    - **IPSetId** *(string) --*

      The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get
      detailed information about an  IPSet .

    - **Name** *(string) --*

      A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
      after you create it.
    """


_ListIPSetsPaginateResponseTypeDef = TypedDict(
    "_ListIPSetsPaginateResponseTypeDef",
    {"IPSets": List[ListIPSetsPaginateResponseIPSetsTypeDef], "NextToken": str},
    total=False,
)


class ListIPSetsPaginateResponseTypeDef(_ListIPSetsPaginateResponseTypeDef):
    """
    Type definition for `ListIPSetsPaginate` `Response`

    - **IPSets** *(list) --*

      An array of  IPSetSummary objects.

      - *(dict) --*

        Contains the identifier and the name of the ``IPSet`` .

        - **IPSetId** *(string) --*

          The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get
          detailed information about an  IPSet .

        - **Name** *(string) --*

          A friendly name or description of the  IPSet . You can't change the name of an ``IPSet``
          after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListLoggingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLoggingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLoggingConfigurationsPaginatePaginationConfigTypeDef(
    _ListLoggingConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLoggingConfigurationsPaginate` `PaginationConfig`

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


_ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef = TypedDict(
    "_ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef",
    {"Type": str, "Data": str},
    total=False,
)


class ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef(
    _ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef
):
    """
    Type definition for `ListLoggingConfigurationsPaginateResponseLoggingConfigurations` `RedactedFields`

    Specifies where in a web request to look for ``TargetString`` .

    - **Type** *(string) --*

      The part of the web request that you want AWS WAF to search for a specified string.
      Parts of a request that you can search include the following:

      * ``HEADER`` : A specified request header, for example, the value of the
      ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
      the name of the header in ``Data`` .

      * ``METHOD`` : The HTTP method, which indicated the type of operation that the
      request is asking the origin to perform. Amazon CloudFront supports the following
      methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
      ``PUT`` .

      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
      ``?`` character, if any.

      * ``URI`` : The part of a web request that identifies a resource, for example,
      ``/images/daily-ad.jpg`` .

      * ``BODY`` : The part of a request that contains any additional data that you want to
      send to your web server as the HTTP request body, such as data from a form. The
      request body immediately follows the request headers. Note that only the first
      ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
      or block requests based on the length of the body, you can create a size constraint
      set. For more information, see  CreateSizeConstraintSet .

      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
      such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
      30 characters.

      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
      single parameter, AWS WAF will inspect all parameters within the query for the value
      or regex pattern that you specify in ``TargetString`` .

    - **Data** *(string) --*

      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
      AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
      header is not case sensitive.

      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
      that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
      parameter name is not case sensitive.

      If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef = TypedDict(
    "_ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ListLoggingConfigurationsPaginateResponseLoggingConfigurationsRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef(
    _ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef
):
    """
    Type definition for `ListLoggingConfigurationsPaginateResponse` `LoggingConfigurations`

    The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
    Resource Name (ARN).

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the web ACL that you want to associate with
      ``LogDestinationConfigs`` .

    - **LogDestinationConfigs** *(list) --*

      An array of Amazon Kinesis Data Firehose ARNs.

      - *(string) --*

    - **RedactedFields** *(list) --*

      The parts of the request that you want redacted from the logs. For example, if you redact
      the cookie field, the cookie field in the firehose will be ``xxx`` .

      - *(dict) --*

        Specifies where in a web request to look for ``TargetString`` .

        - **Type** *(string) --*

          The part of the web request that you want AWS WAF to search for a specified string.
          Parts of a request that you can search include the following:

          * ``HEADER`` : A specified request header, for example, the value of the
          ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
          the name of the header in ``Data`` .

          * ``METHOD`` : The HTTP method, which indicated the type of operation that the
          request is asking the origin to perform. Amazon CloudFront supports the following
          methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
          ``PUT`` .

          * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
          ``?`` character, if any.

          * ``URI`` : The part of a web request that identifies a resource, for example,
          ``/images/daily-ad.jpg`` .

          * ``BODY`` : The part of a request that contains any additional data that you want to
          send to your web server as the HTTP request body, such as data from a form. The
          request body immediately follows the request headers. Note that only the first
          ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
          or block requests based on the length of the body, you can create a size constraint
          set. For more information, see  CreateSizeConstraintSet .

          * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
          such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
          30 characters.

          * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
          single parameter, AWS WAF will inspect all parameters within the query for the value
          or regex pattern that you specify in ``TargetString`` .

        - **Data** *(string) --*

          When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
          AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
          header is not case sensitive.

          When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
          that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
          parameter name is not case sensitive.

          If the value of ``Type`` is any other value, omit ``Data`` .
    """


_ListLoggingConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListLoggingConfigurationsPaginateResponseTypeDef",
    {
        "LoggingConfigurations": List[
            ListLoggingConfigurationsPaginateResponseLoggingConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListLoggingConfigurationsPaginateResponseTypeDef(
    _ListLoggingConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListLoggingConfigurationsPaginate` `Response`

    - **LoggingConfigurations** *(list) --*

      An array of  LoggingConfiguration objects.

      - *(dict) --*

        The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
        Resource Name (ARN).

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the web ACL that you want to associate with
          ``LogDestinationConfigs`` .

        - **LogDestinationConfigs** *(list) --*

          An array of Amazon Kinesis Data Firehose ARNs.

          - *(string) --*

        - **RedactedFields** *(list) --*

          The parts of the request that you want redacted from the logs. For example, if you redact
          the cookie field, the cookie field in the firehose will be ``xxx`` .

          - *(dict) --*

            Specifies where in a web request to look for ``TargetString`` .

            - **Type** *(string) --*

              The part of the web request that you want AWS WAF to search for a specified string.
              Parts of a request that you can search include the following:

              * ``HEADER`` : A specified request header, for example, the value of the
              ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify
              the name of the header in ``Data`` .

              * ``METHOD`` : The HTTP method, which indicated the type of operation that the
              request is asking the origin to perform. Amazon CloudFront supports the following
              methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and
              ``PUT`` .

              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a
              ``?`` character, if any.

              * ``URI`` : The part of a web request that identifies a resource, for example,
              ``/images/daily-ad.jpg`` .

              * ``BODY`` : The part of a request that contains any additional data that you want to
              send to your web server as the HTTP request body, such as data from a form. The
              request body immediately follows the request headers. Note that only the first
              ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow
              or block requests based on the length of the body, you can create a size constraint
              set. For more information, see  CreateSizeConstraintSet .

              * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect,
              such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is
              30 characters.

              * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a
              single parameter, AWS WAF will inspect all parameters within the query for the value
              or regex pattern that you specify in ``TargetString`` .

            - **Data** *(string) --*

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want
              AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the
              header is not case sensitive.

              When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter
              that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The
              parameter name is not case sensitive.

              If the value of ``Type`` is any other value, omit ``Data`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRateBasedRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRateBasedRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRateBasedRulesPaginatePaginationConfigTypeDef(
    _ListRateBasedRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRateBasedRulesPaginate` `PaginationConfig`

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


_ListRateBasedRulesPaginateResponseRulesTypeDef = TypedDict(
    "_ListRateBasedRulesPaginateResponseRulesTypeDef",
    {"RuleId": str, "Name": str},
    total=False,
)


class ListRateBasedRulesPaginateResponseRulesTypeDef(
    _ListRateBasedRulesPaginateResponseRulesTypeDef
):
    """
    Type definition for `ListRateBasedRulesPaginateResponse` `Rules`

    Contains the identifier and the friendly name or description of the ``Rule`` .

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      A friendly name or description of the  Rule . You can't change the name of a ``Rule``
      after you create it.
    """


_ListRateBasedRulesPaginateResponseTypeDef = TypedDict(
    "_ListRateBasedRulesPaginateResponseTypeDef",
    {"Rules": List[ListRateBasedRulesPaginateResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class ListRateBasedRulesPaginateResponseTypeDef(
    _ListRateBasedRulesPaginateResponseTypeDef
):
    """
    Type definition for `ListRateBasedRulesPaginate` `Response`

    - **Rules** *(list) --*

      An array of  RuleSummary objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``Rule`` .

        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Name** *(string) --*

          A friendly name or description of the  Rule . You can't change the name of a ``Rule``
          after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRegexMatchSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRegexMatchSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRegexMatchSetsPaginatePaginationConfigTypeDef(
    _ListRegexMatchSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRegexMatchSetsPaginate` `PaginationConfig`

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


_ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef = TypedDict(
    "_ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef",
    {"RegexMatchSetId": str, "Name": str},
    total=False,
)


class ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef(
    _ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef
):
    """
    Type definition for `ListRegexMatchSetsPaginateResponse` `RegexMatchSets`

    Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the
    ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .

    - **RegexMatchSetId** *(string) --*

      The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
      information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a
      ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.

       ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

    - **Name** *(string) --*

      A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after
      you create a ``RegexMatchSet`` .
    """


_ListRegexMatchSetsPaginateResponseTypeDef = TypedDict(
    "_ListRegexMatchSetsPaginateResponseTypeDef",
    {
        "RegexMatchSets": List[ListRegexMatchSetsPaginateResponseRegexMatchSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListRegexMatchSetsPaginateResponseTypeDef(
    _ListRegexMatchSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListRegexMatchSetsPaginate` `Response`

    - **RegexMatchSets** *(list) --*

      An array of  RegexMatchSetSummary objects.

      - *(dict) --*

        Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the
        ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .

        - **RegexMatchSetId** *(string) --*

          The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
          information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a
          ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.

           ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

        - **Name** *(string) --*

          A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after
          you create a ``RegexMatchSet`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRegexPatternSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRegexPatternSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRegexPatternSetsPaginatePaginationConfigTypeDef(
    _ListRegexPatternSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRegexPatternSetsPaginate` `PaginationConfig`

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


_ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef = TypedDict(
    "_ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef",
    {"RegexPatternSetId": str, "Name": str},
    total=False,
)


class ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef(
    _ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef
):
    """
    Type definition for `ListRegexPatternSetsPaginateResponse` `RegexPatternSets`

    Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the
    ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .

    - **RegexPatternSetId** *(string) --*

      The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
      get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
      ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
      WAF.

       ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets
       .

    - **Name** *(string) --*

      A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
      you create a ``RegexPatternSet`` .
    """


_ListRegexPatternSetsPaginateResponseTypeDef = TypedDict(
    "_ListRegexPatternSetsPaginateResponseTypeDef",
    {
        "RegexPatternSets": List[
            ListRegexPatternSetsPaginateResponseRegexPatternSetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListRegexPatternSetsPaginateResponseTypeDef(
    _ListRegexPatternSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListRegexPatternSetsPaginate` `Response`

    - **RegexPatternSets** *(list) --*

      An array of  RegexPatternSetSummary objects.

      - *(dict) --*

        Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the
        ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .

        - **RegexPatternSetId** *(string) --*

          The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to
          get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
          ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
          WAF.

           ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets
           .

        - **Name** *(string) --*

          A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after
          you create a ``RegexPatternSet`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRuleGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRuleGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRuleGroupsPaginatePaginationConfigTypeDef(
    _ListRuleGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRuleGroupsPaginate` `PaginationConfig`

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


_ListRuleGroupsPaginateResponseRuleGroupsTypeDef = TypedDict(
    "_ListRuleGroupsPaginateResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str},
    total=False,
)


class ListRuleGroupsPaginateResponseRuleGroupsTypeDef(
    _ListRuleGroupsPaginateResponseRuleGroupsTypeDef
):
    """
    Type definition for `ListRuleGroupsPaginateResponse` `RuleGroups`

    Contains the identifier and the friendly name or description of the ``RuleGroup`` .

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
      about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
      ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see
      UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

       ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

    - **Name** *(string) --*

      A friendly name or description of the  RuleGroup . You can't change the name of a
      ``RuleGroup`` after you create it.
    """


_ListRuleGroupsPaginateResponseTypeDef = TypedDict(
    "_ListRuleGroupsPaginateResponseTypeDef",
    {
        "RuleGroups": List[ListRuleGroupsPaginateResponseRuleGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListRuleGroupsPaginateResponseTypeDef(_ListRuleGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListRuleGroupsPaginate` `Response`

    - **RuleGroups** *(list) --*

      An array of  RuleGroup objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``RuleGroup`` .

        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
          about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
          ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see
          UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

           ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

        - **Name** *(string) --*

          A friendly name or description of the  RuleGroup . You can't change the name of a
          ``RuleGroup`` after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRulesPaginatePaginationConfigTypeDef(
    _ListRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRulesPaginate` `PaginationConfig`

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


_ListRulesPaginateResponseRulesTypeDef = TypedDict(
    "_ListRulesPaginateResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)


class ListRulesPaginateResponseRulesTypeDef(_ListRulesPaginateResponseRulesTypeDef):
    """
    Type definition for `ListRulesPaginateResponse` `Rules`

    Contains the identifier and the friendly name or description of the ``Rule`` .

    - **RuleId** *(string) --*

      A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
      ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
      ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
      from AWS WAF (see  DeleteRule ).

       ``RuleId`` is returned by  CreateRule and by  ListRules .

    - **Name** *(string) --*

      A friendly name or description of the  Rule . You can't change the name of a ``Rule``
      after you create it.
    """


_ListRulesPaginateResponseTypeDef = TypedDict(
    "_ListRulesPaginateResponseTypeDef",
    {"Rules": List[ListRulesPaginateResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class ListRulesPaginateResponseTypeDef(_ListRulesPaginateResponseTypeDef):
    """
    Type definition for `ListRulesPaginate` `Response`

    - **Rules** *(list) --*

      An array of  RuleSummary objects.

      - *(dict) --*

        Contains the identifier and the friendly name or description of the ``Rule`` .

        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

           ``RuleId`` is returned by  CreateRule and by  ListRules .

        - **Name** *(string) --*

          A friendly name or description of the  Rule . You can't change the name of a ``Rule``
          after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSizeConstraintSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSizeConstraintSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSizeConstraintSetsPaginatePaginationConfigTypeDef(
    _ListSizeConstraintSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSizeConstraintSetsPaginate` `PaginationConfig`

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


_ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef = TypedDict(
    "_ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef",
    {"SizeConstraintSetId": str, "Name": str},
    total=False,
)


class ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef(
    _ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef
):
    """
    Type definition for `ListSizeConstraintSetsPaginateResponse` `SizeConstraintSets`

    The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .

    - **SizeConstraintSetId** *(string) --*

      A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
      information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
      ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet``
      into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
      ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

       ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
       ListSizeConstraintSets .

    - **Name** *(string) --*

      The name of the ``SizeConstraintSet`` , if any.
    """


_ListSizeConstraintSetsPaginateResponseTypeDef = TypedDict(
    "_ListSizeConstraintSetsPaginateResponseTypeDef",
    {
        "SizeConstraintSets": List[
            ListSizeConstraintSetsPaginateResponseSizeConstraintSetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSizeConstraintSetsPaginateResponseTypeDef(
    _ListSizeConstraintSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListSizeConstraintSetsPaginate` `Response`

    - **SizeConstraintSets** *(list) --*

      An array of  SizeConstraintSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .

        - **SizeConstraintSetId** *(string) --*

          A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
          information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
          ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet``
          into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
          ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

           ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
           ListSizeConstraintSets .

        - **Name** *(string) --*

          The name of the ``SizeConstraintSet`` , if any.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef(
    _ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSqlInjectionMatchSetsPaginate` `PaginationConfig`

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


_ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef = TypedDict(
    "_ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef",
    {"SqlInjectionMatchSetId": str, "Name": str},
    total=False,
)


class ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef(
    _ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef
):
    """
    Type definition for `ListSqlInjectionMatchSetsPaginateResponse` `SqlInjectionMatchSets`

    The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .

    - **SqlInjectionMatchSetId** *(string) --*

      A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId``
      to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ),
      update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
      ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule
      ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

       ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
       ListSqlInjectionMatchSets .

    - **Name** *(string) --*

      The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .
    """


_ListSqlInjectionMatchSetsPaginateResponseTypeDef = TypedDict(
    "_ListSqlInjectionMatchSetsPaginateResponseTypeDef",
    {
        "SqlInjectionMatchSets": List[
            ListSqlInjectionMatchSetsPaginateResponseSqlInjectionMatchSetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSqlInjectionMatchSetsPaginateResponseTypeDef(
    _ListSqlInjectionMatchSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListSqlInjectionMatchSetsPaginate` `Response`

    The response to a  ListSqlInjectionMatchSets request.

    - **SqlInjectionMatchSets** *(list) --*

      An array of  SqlInjectionMatchSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .

        - **SqlInjectionMatchSetId** *(string) --*

          A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId``
          to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ),
          update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
          ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule
          ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

           ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
           ListSqlInjectionMatchSets .

        - **Name** *(string) --*

          The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef(
    _ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSubscribedRuleGroupsPaginate` `PaginationConfig`

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


_ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef = TypedDict(
    "_ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef(
    _ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef
):
    """
    Type definition for `ListSubscribedRuleGroupsPaginateResponse` `RuleGroups`

    A summary of the rule groups you are subscribed to.

    - **RuleGroupId** *(string) --*

      A unique identifier for a ``RuleGroup`` .

    - **Name** *(string) --*

      A friendly name or description of the ``RuleGroup`` . You can't change the name of a
      ``RuleGroup`` after you create it.

    - **MetricName** *(string) --*

      A friendly name or description for the metrics for this ``RuleGroup`` . The name can
      contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
      length one. It can't contain whitespace or metric names reserved for AWS WAF, including
      "All" and "Default_Action." You can't change the name of the metric after you create the
      ``RuleGroup`` .
    """


_ListSubscribedRuleGroupsPaginateResponseTypeDef = TypedDict(
    "_ListSubscribedRuleGroupsPaginateResponseTypeDef",
    {
        "RuleGroups": List[ListSubscribedRuleGroupsPaginateResponseRuleGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSubscribedRuleGroupsPaginateResponseTypeDef(
    _ListSubscribedRuleGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListSubscribedRuleGroupsPaginate` `Response`

    - **RuleGroups** *(list) --*

      An array of  RuleGroup objects.

      - *(dict) --*

        A summary of the rule groups you are subscribed to.

        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` .

        - **Name** *(string) --*

          A friendly name or description of the ``RuleGroup`` . You can't change the name of a
          ``RuleGroup`` after you create it.

        - **MetricName** *(string) --*

          A friendly name or description for the metrics for this ``RuleGroup`` . The name can
          contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum
          length one. It can't contain whitespace or metric names reserved for AWS WAF, including
          "All" and "Default_Action." You can't change the name of the metric after you create the
          ``RuleGroup`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListWebACLsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWebACLsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWebACLsPaginatePaginationConfigTypeDef(
    _ListWebACLsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListWebACLsPaginate` `PaginationConfig`

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


_ListWebACLsPaginateResponseWebACLsTypeDef = TypedDict(
    "_ListWebACLsPaginateResponseWebACLsTypeDef",
    {"WebACLId": str, "Name": str},
    total=False,
)


class ListWebACLsPaginateResponseWebACLsTypeDef(
    _ListWebACLsPaginateResponseWebACLsTypeDef
):
    """
    Type definition for `ListWebACLsPaginateResponse` `WebACLs`

    Contains the identifier and the name or description of the  WebACL .

    - **WebACLId** *(string) --*

      A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
      ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
      ``WebACL`` from AWS WAF (see  DeleteWebACL ).

       ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

    - **Name** *(string) --*

      A friendly name or description of the  WebACL . You can't change the name of a ``WebACL``
      after you create it.
    """


_ListWebACLsPaginateResponseTypeDef = TypedDict(
    "_ListWebACLsPaginateResponseTypeDef",
    {"WebACLs": List[ListWebACLsPaginateResponseWebACLsTypeDef], "NextToken": str},
    total=False,
)


class ListWebACLsPaginateResponseTypeDef(_ListWebACLsPaginateResponseTypeDef):
    """
    Type definition for `ListWebACLsPaginate` `Response`

    - **WebACLs** *(list) --*

      An array of  WebACLSummary objects.

      - *(dict) --*

        Contains the identifier and the name or description of the  WebACL .

        - **WebACLId** *(string) --*

          A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
          ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
          ``WebACL`` from AWS WAF (see  DeleteWebACL ).

           ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

        - **Name** *(string) --*

          A friendly name or description of the  WebACL . You can't change the name of a ``WebACL``
          after you create it.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListXssMatchSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListXssMatchSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListXssMatchSetsPaginatePaginationConfigTypeDef(
    _ListXssMatchSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListXssMatchSetsPaginate` `PaginationConfig`

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


_ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef = TypedDict(
    "_ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef",
    {"XssMatchSetId": str, "Name": str},
    total=False,
)


class ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef(
    _ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef
):
    """
    Type definition for `ListXssMatchSetsPaginateResponse` `XssMatchSets`

    The ``Id`` and ``Name`` of an ``XssMatchSet`` .

    - **XssMatchSetId** *(string) --*

      A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
      about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
      UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
      ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
      DeleteXssMatchSet ).

       ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

    - **Name** *(string) --*

      The name of the ``XssMatchSet`` , if any, specified by ``Id`` .
    """


_ListXssMatchSetsPaginateResponseTypeDef = TypedDict(
    "_ListXssMatchSetsPaginateResponseTypeDef",
    {
        "XssMatchSets": List[ListXssMatchSetsPaginateResponseXssMatchSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListXssMatchSetsPaginateResponseTypeDef(_ListXssMatchSetsPaginateResponseTypeDef):
    """
    Type definition for `ListXssMatchSetsPaginate` `Response`

    The response to a  ListXssMatchSets request.

    - **XssMatchSets** *(list) --*

      An array of  XssMatchSetSummary objects.

      - *(dict) --*

        The ``Id`` and ``Name`` of an ``XssMatchSet`` .

        - **XssMatchSetId** *(string) --*

          A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
          about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
          UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
          DeleteXssMatchSet ).

           ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

        - **Name** *(string) --*

          The name of the ``XssMatchSet`` , if any, specified by ``Id`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
