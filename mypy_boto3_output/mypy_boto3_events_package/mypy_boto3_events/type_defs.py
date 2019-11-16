"Main interface for events type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateEventBusResponseTypeDef",
    "ClientCreatePartnerEventSourceResponseTypeDef",
    "ClientDescribeEventBusResponseTypeDef",
    "ClientDescribeEventSourceResponseTypeDef",
    "ClientDescribePartnerEventSourceResponseTypeDef",
    "ClientDescribeRuleResponseTypeDef",
    "ClientListEventBusesResponseEventBusesTypeDef",
    "ClientListEventBusesResponseTypeDef",
    "ClientListEventSourcesResponseEventSourcesTypeDef",
    "ClientListEventSourcesResponseTypeDef",
    "ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    "ClientListPartnerEventSourceAccountsResponseTypeDef",
    "ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    "ClientListPartnerEventSourcesResponseTypeDef",
    "ClientListRuleNamesByTargetResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    "ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsTypeDef",
    "ClientListTargetsByRuleResponseTypeDef",
    "ClientPutEventsEntriesTypeDef",
    "ClientPutEventsResponseEntriesTypeDef",
    "ClientPutEventsResponseTypeDef",
    "ClientPutPartnerEventsEntriesTypeDef",
    "ClientPutPartnerEventsResponseEntriesTypeDef",
    "ClientPutPartnerEventsResponseTypeDef",
    "ClientPutPermissionConditionTypeDef",
    "ClientPutRuleResponseTypeDef",
    "ClientPutRuleTagsTypeDef",
    "ClientPutTargetsResponseFailedEntriesTypeDef",
    "ClientPutTargetsResponseTypeDef",
    "ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef",
    "ClientPutTargetsTargetsBatchParametersTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersTypeDef",
    "ClientPutTargetsTargetsInputTransformerTypeDef",
    "ClientPutTargetsTargetsKinesisParametersTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersTypeDef",
    "ClientPutTargetsTargetsSqsParametersTypeDef",
    "ClientPutTargetsTargetsTypeDef",
    "ClientRemoveTargetsResponseFailedEntriesTypeDef",
    "ClientRemoveTargetsResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestEventPatternResponseTypeDef",
    "ListRuleNamesByTargetPaginatePaginationConfigTypeDef",
    "ListRuleNamesByTargetPaginateResponseTypeDef",
    "ListRulesPaginatePaginationConfigTypeDef",
    "ListRulesPaginateResponseRulesTypeDef",
    "ListRulesPaginateResponseTypeDef",
    "ListTargetsByRulePaginatePaginationConfigTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef",
    "ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsTypeDef",
    "ListTargetsByRulePaginateResponseTypeDef",
)


_ClientCreateEventBusResponseTypeDef = TypedDict(
    "_ClientCreateEventBusResponseTypeDef", {"EventBusArn": str}, total=False
)


class ClientCreateEventBusResponseTypeDef(_ClientCreateEventBusResponseTypeDef):
    """
    Type definition for `ClientCreateEventBus` `Response`

    - **EventBusArn** *(string) --*

      The ARN of the new event bus.
    """


_ClientCreatePartnerEventSourceResponseTypeDef = TypedDict(
    "_ClientCreatePartnerEventSourceResponseTypeDef",
    {"EventSourceArn": str},
    total=False,
)


class ClientCreatePartnerEventSourceResponseTypeDef(
    _ClientCreatePartnerEventSourceResponseTypeDef
):
    """
    Type definition for `ClientCreatePartnerEventSource` `Response`

    - **EventSourceArn** *(string) --*

      The ARN of the partner event source.
    """


_ClientDescribeEventBusResponseTypeDef = TypedDict(
    "_ClientDescribeEventBusResponseTypeDef",
    {"Name": str, "Arn": str, "Policy": str},
    total=False,
)


class ClientDescribeEventBusResponseTypeDef(_ClientDescribeEventBusResponseTypeDef):
    """
    Type definition for `ClientDescribeEventBus` `Response`

    - **Name** *(string) --*

      The name of the event bus. Currently, this is always ``default`` .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the account permitted to write events to the current
      account.

    - **Policy** *(string) --*

      The policy that enables the external account to send events to your account.
    """


_ClientDescribeEventSourceResponseTypeDef = TypedDict(
    "_ClientDescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": str,
    },
    total=False,
)


class ClientDescribeEventSourceResponseTypeDef(
    _ClientDescribeEventSourceResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventSource` `Response`

    - **Arn** *(string) --*

      The ARN of the partner event source.

    - **CreatedBy** *(string) --*

      The name of the SaaS partner that created the event source.

    - **CreationTime** *(datetime) --*

      The date and time that the event source was created.

    - **ExpirationTime** *(datetime) --*

      The date and time that the event source will expire if you don't create a matching event bus.

    - **Name** *(string) --*

      The name of the partner event source.

    - **State** *(string) --*

      The state of the event source. If it's ``ACTIVE`` , you have already created a matching event
      bus for this event source, and that event bus is active. If it's ``PENDING`` , either you
      haven't yet created a matching event bus, or that event bus is deactivated. If it's
      ``DELETED`` , you have created a matching event bus, but the event source has since been
      deleted.
    """


_ClientDescribePartnerEventSourceResponseTypeDef = TypedDict(
    "_ClientDescribePartnerEventSourceResponseTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)


class ClientDescribePartnerEventSourceResponseTypeDef(
    _ClientDescribePartnerEventSourceResponseTypeDef
):
    """
    Type definition for `ClientDescribePartnerEventSource` `Response`

    - **Arn** *(string) --*

      The ARN of the event source.

    - **Name** *(string) --*

      The name of the event source.
    """


_ClientDescribeRuleResponseTypeDef = TypedDict(
    "_ClientDescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": str,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)


class ClientDescribeRuleResponseTypeDef(_ClientDescribeRuleResponseTypeDef):
    """
    Type definition for `ClientDescribeRule` `Response`

    - **Name** *(string) --*

      The name of the rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **EventPattern** *(string) --*

      The event pattern. For more information, see `Event Patterns
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
      in the *Amazon EventBridge User Guide* .

    - **ScheduleExpression** *(string) --*

      The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"`` .

    - **State** *(string) --*

      Specifies whether the rule is enabled or disabled.

    - **Description** *(string) --*

      The description of the rule.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role associated with the rule.

    - **ManagedBy** *(string) --*

      If this is a managed rule, created by an AWS service on your behalf, this field displays the
      principal name of the AWS service that created the rule.

    - **EventBusName** *(string) --*

      The event bus associated with the rule.
    """


_ClientListEventBusesResponseEventBusesTypeDef = TypedDict(
    "_ClientListEventBusesResponseEventBusesTypeDef",
    {"Name": str, "Arn": str, "Policy": str},
    total=False,
)


class ClientListEventBusesResponseEventBusesTypeDef(
    _ClientListEventBusesResponseEventBusesTypeDef
):
    """
    Type definition for `ClientListEventBusesResponse` `EventBuses`

    An event bus receives events from a source and routes them to rules associated with that
    event bus. Your account's default event bus receives rules from AWS services. A custom
    event bus can receive rules from AWS services as well as your custom applications and
    services. A partner event bus receives events from an event source created by an SaaS
    partner. These events come from the partners services or applications.

    - **Name** *(string) --*

      The name of the event bus.

    - **Arn** *(string) --*

      The ARN of the event bus.

    - **Policy** *(string) --*

      The permissions policy of the event bus, describing which other AWS accounts can write
      events to this event bus.
    """


_ClientListEventBusesResponseTypeDef = TypedDict(
    "_ClientListEventBusesResponseTypeDef",
    {
        "EventBuses": List[ClientListEventBusesResponseEventBusesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEventBusesResponseTypeDef(_ClientListEventBusesResponseTypeDef):
    """
    Type definition for `ClientListEventBuses` `Response`

    - **EventBuses** *(list) --*

      This list of event buses.

      - *(dict) --*

        An event bus receives events from a source and routes them to rules associated with that
        event bus. Your account's default event bus receives rules from AWS services. A custom
        event bus can receive rules from AWS services as well as your custom applications and
        services. A partner event bus receives events from an event source created by an SaaS
        partner. These events come from the partners services or applications.

        - **Name** *(string) --*

          The name of the event bus.

        - **Arn** *(string) --*

          The ARN of the event bus.

        - **Policy** *(string) --*

          The permissions policy of the event bus, describing which other AWS accounts can write
          events to this event bus.

    - **NextToken** *(string) --*

      A token you can use in a subsequent operation to retrieve the next set of results.
    """


_ClientListEventSourcesResponseEventSourcesTypeDef = TypedDict(
    "_ClientListEventSourcesResponseEventSourcesTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": str,
    },
    total=False,
)


class ClientListEventSourcesResponseEventSourcesTypeDef(
    _ClientListEventSourcesResponseEventSourcesTypeDef
):
    """
    Type definition for `ClientListEventSourcesResponse` `EventSources`

    A partner event source is created by an SaaS partner. If a customer creates a partner event
    bus that matches this event source, that AWS account can receive events from the partner's
    applications or services.

    - **Arn** *(string) --*

      The ARN of the event source.

    - **CreatedBy** *(string) --*

      The name of the partner that created the event source.

    - **CreationTime** *(datetime) --*

      The date and time when the event source was created.

    - **ExpirationTime** *(datetime) --*

      The date and time when the event source will expire if the AWS account doesn't create a
      matching event bus for it.

    - **Name** *(string) --*

      The name of the event source.

    - **State** *(string) --*

      The state of the event source. If it's ``ACTIVE`` , you have already created a matching
      event bus for this event source, and that event bus is active. If it's ``PENDING`` ,
      either you haven't yet created a matching event bus, or that event bus is deactivated. If
      it's ``DELETED`` , you have created a matching event bus, but the event source has since
      been deleted.
    """


_ClientListEventSourcesResponseTypeDef = TypedDict(
    "_ClientListEventSourcesResponseTypeDef",
    {
        "EventSources": List[ClientListEventSourcesResponseEventSourcesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEventSourcesResponseTypeDef(_ClientListEventSourcesResponseTypeDef):
    """
    Type definition for `ClientListEventSources` `Response`

    - **EventSources** *(list) --*

      The list of event sources.

      - *(dict) --*

        A partner event source is created by an SaaS partner. If a customer creates a partner event
        bus that matches this event source, that AWS account can receive events from the partner's
        applications or services.

        - **Arn** *(string) --*

          The ARN of the event source.

        - **CreatedBy** *(string) --*

          The name of the partner that created the event source.

        - **CreationTime** *(datetime) --*

          The date and time when the event source was created.

        - **ExpirationTime** *(datetime) --*

          The date and time when the event source will expire if the AWS account doesn't create a
          matching event bus for it.

        - **Name** *(string) --*

          The name of the event source.

        - **State** *(string) --*

          The state of the event source. If it's ``ACTIVE`` , you have already created a matching
          event bus for this event source, and that event bus is active. If it's ``PENDING`` ,
          either you haven't yet created a matching event bus, or that event bus is deactivated. If
          it's ``DELETED`` , you have created a matching event bus, but the event source has since
          been deleted.

    - **NextToken** *(string) --*

      A token you can use in a subsequent operation to retrieve the next set of results.
    """


_ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef = TypedDict(
    "_ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": str,
    },
    total=False,
)


class ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef(
    _ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
):
    """
    Type definition for `ClientListPartnerEventSourceAccountsResponse` `PartnerEventSourceAccounts`

    The AWS account that a partner event source has been offered to.

    - **Account** *(string) --*

      The AWS account ID that the partner event source was offered to.

    - **CreationTime** *(datetime) --*

      The date and time when the event source was created.

    - **ExpirationTime** *(datetime) --*

      The date and time when the event source will expire if the AWS account doesn't create a
      matching event bus for it.

    - **State** *(string) --*

      The state of the event source. If it's ``ACTIVE`` , you have already created a matching
      event bus for this event source, and that event bus is active. If it's ``PENDING`` ,
      either you haven't yet created a matching event bus, or that event bus is deactivated. If
      it's ``DELETED`` , you have created a matching event bus, but the event source has since
      been deleted.
    """


_ClientListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "_ClientListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[
            ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPartnerEventSourceAccountsResponseTypeDef(
    _ClientListPartnerEventSourceAccountsResponseTypeDef
):
    """
    Type definition for `ClientListPartnerEventSourceAccounts` `Response`

    - **PartnerEventSourceAccounts** *(list) --*

      The list of partner event sources returned by the operation.

      - *(dict) --*

        The AWS account that a partner event source has been offered to.

        - **Account** *(string) --*

          The AWS account ID that the partner event source was offered to.

        - **CreationTime** *(datetime) --*

          The date and time when the event source was created.

        - **ExpirationTime** *(datetime) --*

          The date and time when the event source will expire if the AWS account doesn't create a
          matching event bus for it.

        - **State** *(string) --*

          The state of the event source. If it's ``ACTIVE`` , you have already created a matching
          event bus for this event source, and that event bus is active. If it's ``PENDING`` ,
          either you haven't yet created a matching event bus, or that event bus is deactivated. If
          it's ``DELETED`` , you have created a matching event bus, but the event source has since
          been deleted.

    - **NextToken** *(string) --*

      A token you can use in a subsequent operation to retrieve the next set of results.
    """


_ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef = TypedDict(
    "_ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)


class ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef(
    _ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
):
    """
    Type definition for `ClientListPartnerEventSourcesResponse` `PartnerEventSources`

    A partner event source is created by an SaaS partner. If a customer creates a partner event
    bus that matches this event source, that AWS account can receive events from the partner's
    applications or services.

    - **Arn** *(string) --*

      The ARN of the partner event source.

    - **Name** *(string) --*

      The name of the partner event source.
    """


_ClientListPartnerEventSourcesResponseTypeDef = TypedDict(
    "_ClientListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[
            ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPartnerEventSourcesResponseTypeDef(
    _ClientListPartnerEventSourcesResponseTypeDef
):
    """
    Type definition for `ClientListPartnerEventSources` `Response`

    - **PartnerEventSources** *(list) --*

      The list of partner event sources returned by the operation.

      - *(dict) --*

        A partner event source is created by an SaaS partner. If a customer creates a partner event
        bus that matches this event source, that AWS account can receive events from the partner's
        applications or services.

        - **Arn** *(string) --*

          The ARN of the partner event source.

        - **Name** *(string) --*

          The name of the partner event source.

    - **NextToken** *(string) --*

      A token you can use in a subsequent operation to retrieve the next set of results.
    """


_ClientListRuleNamesByTargetResponseTypeDef = TypedDict(
    "_ClientListRuleNamesByTargetResponseTypeDef",
    {"RuleNames": List[str], "NextToken": str},
    total=False,
)


class ClientListRuleNamesByTargetResponseTypeDef(
    _ClientListRuleNamesByTargetResponseTypeDef
):
    """
    Type definition for `ClientListRuleNamesByTarget` `Response`

    - **RuleNames** *(list) --*

      The names of the rules that can invoke the given target.

      - *(string) --*

    - **NextToken** *(string) --*

      Indicates whether there are additional results to retrieve. If there are no more results, the
      value is null.
    """


_ClientListRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRulesResponseRulesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": str,
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)


class ClientListRulesResponseRulesTypeDef(_ClientListRulesResponseRulesTypeDef):
    """
    Type definition for `ClientListRulesResponse` `Rules`

    Contains information about a rule in Amazon EventBridge.

    - **Name** *(string) --*

      The name of the rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **EventPattern** *(string) --*

      The event pattern of the rule. For more information, see `Event Patterns
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
      in the *Amazon EventBridge User Guide* .

    - **State** *(string) --*

      The state of the rule.

    - **Description** *(string) --*

      The description of the rule.

    - **ScheduleExpression** *(string) --*

      The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"``
      .

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the role that is used for target invocation.

    - **ManagedBy** *(string) --*

      If an AWS service created the rule on behalf of your account, this field displays the
      principal name of the service that created the rule.

    - **EventBusName** *(string) --*

      The event bus associated with the rule.
    """


_ClientListRulesResponseTypeDef = TypedDict(
    "_ClientListRulesResponseTypeDef",
    {"Rules": List[ClientListRulesResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class ClientListRulesResponseTypeDef(_ClientListRulesResponseTypeDef):
    """
    Type definition for `ClientListRules` `Response`

    - **Rules** *(list) --*

      The rules that match the specified criteria.

      - *(dict) --*

        Contains information about a rule in Amazon EventBridge.

        - **Name** *(string) --*

          The name of the rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **EventPattern** *(string) --*

          The event pattern of the rule. For more information, see `Event Patterns
          <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
          in the *Amazon EventBridge User Guide* .

        - **State** *(string) --*

          The state of the rule.

        - **Description** *(string) --*

          The description of the rule.

        - **ScheduleExpression** *(string) --*

          The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"``
          .

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the role that is used for target invocation.

        - **ManagedBy** *(string) --*

          If an AWS service created the rule on behalf of your account, this field displays the
          principal name of the service that created the rule.

        - **EventBusName** *(string) --*

          The event bus associated with the rule.

    - **NextToken** *(string) --*

      Indicates whether there are additional results to retrieve. If there are no more results, the
      value is null.
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

    A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.

    - **Key** *(string) --*

      A string that you can use to assign a value. The combination of tag keys and values can
      help you organize and categorize your resources.

    - **Value** *(string) --*

      The value for the specified tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The list of tag keys and values associated with the rule that you specified.

      - *(dict) --*

        A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.

        - **Key** *(string) --*

          A string that you can use to assign a value. The combination of tag keys and values can
          help you organize and categorize your resources.

        - **Value** *(string) --*

          The value for the specified tag key.
    """


_ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargetsBatchParameters` `ArrayProperties`

    The array properties for the submitted job, such as the size of the array. The array
    size can be between 2 and 10,000. If you specify array properties for a job, it becomes
    an array job. This parameter is used only if the target is an AWS Batch job.

    - **Size** *(integer) --*

      The size of the array, if this is an array batch job. Valid values are integers
      between 2 and 10,000.
    """


_ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargetsBatchParameters` `RetryStrategy`

    The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
    strategy is the number of times to retry the failed job execution. Valid values are
    1–10. When you specify a retry strategy here, it overrides the retry strategy defined
    in the job definition.

    - **Attempts** *(integer) --*

      The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `BatchParameters`

    If the event target is an AWS Batch job, this contains the job definition, job name, and
    other parameters. For more information, see `Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
    Guide* .

    - **JobDefinition** *(string) --*

      The ARN or name of the job definition to use if the event target is an AWS Batch job.
      This job definition must already exist.

    - **JobName** *(string) --*

      The name to use for this execution of the job, if the target is an AWS Batch job.

    - **ArrayProperties** *(dict) --*

      The array properties for the submitted job, such as the size of the array. The array
      size can be between 2 and 10,000. If you specify array properties for a job, it becomes
      an array job. This parameter is used only if the target is an AWS Batch job.

      - **Size** *(integer) --*

        The size of the array, if this is an array batch job. Valid values are integers
        between 2 and 10,000.

    - **RetryStrategy** *(dict) --*

      The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
      strategy is the number of times to retry the failed job execution. Valid values are
      1–10. When you specify a retry strategy here, it overrides the retry strategy defined
      in the job definition.

      - **Attempts** *(integer) --*

        The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {"Subnets": List[str], "SecurityGroups": List[str], "AssignPublicIp": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfiguration` `awsvpcConfiguration`

    Use this structure to specify the VPC subnets and security groups for the task and
    whether a public IP address is to be used. This structure is relevant only for ECS
    tasks that use the ``awsvpc`` network mode.

    - **Subnets** *(list) --*

      Specifies the subnets associated with the task. These subnets must all be in the
      same VPC. You can specify as many as 16 subnets.

      - *(string) --*

    - **SecurityGroups** *(list) --*

      Specifies the security groups associated with the task. These security groups must
      all be in the same VPC. You can specify as many as five security groups. If you
      don't specify a security group, the default security group for the VPC is used.

      - *(string) --*

    - **AssignPublicIp** *(string) --*

      Specifies whether the task's elastic network interface receives a public IP
      address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
      is set to ``FARGATE`` .
    """


_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargetsEcsParameters` `NetworkConfiguration`

    Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
    specifies the VPC subnets and security groups associated with the task and whether a
    public IP address is to be used. This structure is required if ``LaunchType`` is
    ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

    If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
    ``awsvpc`` network mode, the task fails.

    - **awsvpcConfiguration** *(dict) --*

      Use this structure to specify the VPC subnets and security groups for the task and
      whether a public IP address is to be used. This structure is relevant only for ECS
      tasks that use the ``awsvpc`` network mode.

      - **Subnets** *(list) --*

        Specifies the subnets associated with the task. These subnets must all be in the
        same VPC. You can specify as many as 16 subnets.

        - *(string) --*

      - **SecurityGroups** *(list) --*

        Specifies the security groups associated with the task. These security groups must
        all be in the same VPC. You can specify as many as five security groups. If you
        don't specify a security group, the default security group for the VPC is used.

        - *(string) --*

      - **AssignPublicIp** *(string) --*

        Specifies whether the task's elastic network interface receives a public IP
        address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
        is set to ``FARGATE`` .
    """


_ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": str,
        "NetworkConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `EcsParameters`

    Contains the Amazon ECS task definition and task count to be used if the event target is
    an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
    the *Amazon EC2 Container Service Developer Guide* .

    - **TaskDefinitionArn** *(string) --*

      The ARN of the task definition to use if the event target is an Amazon ECS task.

    - **TaskCount** *(integer) --*

      The number of tasks to create based on ``TaskDefinition`` . The default is 1.

    - **LaunchType** *(string) --*

      Specifies the launch type on which your task is running. The launch type that you
      specify here must match one of the launch type (compatibilities) of the target task.
      The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
      ECS is supported. For more information, see `AWS Fargate on Amazon ECS
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
      the *Amazon Elastic Container Service Developer Guide* .

    - **NetworkConfiguration** *(dict) --*

      Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
      specifies the VPC subnets and security groups associated with the task and whether a
      public IP address is to be used. This structure is required if ``LaunchType`` is
      ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

      If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
      ``awsvpc`` network mode, the task fails.

      - **awsvpcConfiguration** *(dict) --*

        Use this structure to specify the VPC subnets and security groups for the task and
        whether a public IP address is to be used. This structure is relevant only for ECS
        tasks that use the ``awsvpc`` network mode.

        - **Subnets** *(list) --*

          Specifies the subnets associated with the task. These subnets must all be in the
          same VPC. You can specify as many as 16 subnets.

          - *(string) --*

        - **SecurityGroups** *(list) --*

          Specifies the security groups associated with the task. These security groups must
          all be in the same VPC. You can specify as many as five security groups. If you
          don't specify a security group, the default security group for the VPC is used.

          - *(string) --*

        - **AssignPublicIp** *(string) --*

          Specifies whether the task's elastic network interface receives a public IP
          address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
          is set to ``FARGATE`` .

    - **PlatformVersion** *(string) --*

      Specifies the platform version for the task. Specify only the numeric portion of the
      platform version, such as ``1.1.0`` .

      This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
      about valid platform versions, see `AWS Fargate Platform Versions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .

    - **Group** *(string) --*

      Specifies an ECS task group for the task. The maximum length is 255 characters.
    """


_ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef(
    _ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `InputTransformer`

    Settings to enable you to provide custom input to a target based on certain event data.
    You can extract one or more key-value pairs from the event and then use that data to send
    customized input to the target.

    - **InputPathsMap** *(dict) --*

      Map of JSON paths to be extracted from the event. You can then insert these in the
      template in ``InputTemplate`` to produce the output to be sent to the target.

       ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
       You can have as many as 10 key-value pairs. You must use JSON dot notation, not
       bracket notation.

      The keys can't start with ``"AWS"`` .

      - *(string) --*

        - *(string) --*

    - **InputTemplate** *(string) --*

      Input template where you specify placeholders that will be filled with the values of
      the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
      ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

      If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
      restrictions apply:

      * The placeholder can't be used as an object key

      * Object values can't include quote marks

      The following example shows the syntax for using ``InputPathsMap`` and
      ``InputTemplate`` .

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state <status>"``

       ``}``

      To have the ``InputTemplate`` include quote marks within a JSON string, escape each
      quote marks with a slash, as in the following example:

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state \\"<status>\\""``

       ``}``
    """


_ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `KinesisParameters`

    The custom parameter that you can use to control the shard assignment when the target is
    a Kinesis data stream. If you don't include this parameter, the default is to use the
    ``eventId`` as the partition key.

    - **PartitionKeyPath** *(string) --*

      The JSON path to be extracted from the event and used as the partition key. For more
      information, see `Amazon Kinesis Streams Key Concepts
      <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
      the *Amazon Kinesis Streams Developer Guide* .
    """


_ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargetsRunCommandParameters` `RunCommandTargets`

    Information about the EC2 instances that are to be sent the command, specified as
    key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
    key can specify multiple values.

    - **Key** *(string) --*

      Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

    - **Values** *(list) --*

      If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
      is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

      - *(string) --*
    """


_ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `RunCommandParameters`

    Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

    - **RunCommandTargets** *(list) --*

      Currently, we support including only one ``RunCommandTarget`` block, which specifies
      either an array of ``InstanceIds`` or a tag.

      - *(dict) --*

        Information about the EC2 instances that are to be sent the command, specified as
        key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
        key can specify multiple values.

        - **Key** *(string) --*

          Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

        - **Values** *(list) --*

          If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
          is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

          - *(string) --*
    """


_ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponseTargets` `SqsParameters`

    Contains the message group ID to use when the target is a FIFO queue.

    If you specify an SQS FIFO queue as a target, the queue must have content-based
    deduplication enabled.

    - **MessageGroupId** *(string) --*

      The FIFO message group ID to use as the target.
    """


_ClientListTargetsByRuleResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef,
        "BatchParameters": ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef,
        "SqsParameters": ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef,
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsTypeDef(
    _ClientListTargetsByRuleResponseTargetsTypeDef
):
    """
    Type definition for `ClientListTargetsByRuleResponse` `Targets`

    Targets are the resources to be invoked when a rule is triggered. For a complete list of
    services and resources that can be set as a target, see  PutTargets .

    If you're setting the event bus of another account as the target and that account granted
    permission to your account through an organization instead of directly by the account ID,
    you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
    more information, see `Sending and Receiving Events Between AWS Accounts
    <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
    in the *Amazon EventBridge User Guide* .

    - **Id** *(string) --*

      A name for the target. Use a string that will help you identify the target. Each target
      associated with a rule must have an ``Id`` unique for that rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the target.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule
      is triggered. If one rule triggers multiple targets, you can use a different IAM role for
      each target.

    - **Input** *(string) --*

      Valid JSON text passed to the target. In this case, nothing from the event itself is
      passed to the target. For more information, see `The JavaScript Object Notation (JSON)
      Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

    - **InputPath** *(string) --*

      The value of the JSONPath that is used for extracting part of the matched event when
      passing it to the target. You must use JSON dot notation, not bracket notation. For more
      information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

    - **InputTransformer** *(dict) --*

      Settings to enable you to provide custom input to a target based on certain event data.
      You can extract one or more key-value pairs from the event and then use that data to send
      customized input to the target.

      - **InputPathsMap** *(dict) --*

        Map of JSON paths to be extracted from the event. You can then insert these in the
        template in ``InputTemplate`` to produce the output to be sent to the target.

         ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
         You can have as many as 10 key-value pairs. You must use JSON dot notation, not
         bracket notation.

        The keys can't start with ``"AWS"`` .

        - *(string) --*

          - *(string) --*

      - **InputTemplate** *(string) --*

        Input template where you specify placeholders that will be filled with the values of
        the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
        ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

        If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
        restrictions apply:

        * The placeholder can't be used as an object key

        * Object values can't include quote marks

        The following example shows the syntax for using ``InputPathsMap`` and
        ``InputTemplate`` .

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state <status>"``

         ``}``

        To have the ``InputTemplate`` include quote marks within a JSON string, escape each
        quote marks with a slash, as in the following example:

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state \\"<status>\\""``

         ``}``

    - **KinesisParameters** *(dict) --*

      The custom parameter that you can use to control the shard assignment when the target is
      a Kinesis data stream. If you don't include this parameter, the default is to use the
      ``eventId`` as the partition key.

      - **PartitionKeyPath** *(string) --*

        The JSON path to be extracted from the event and used as the partition key. For more
        information, see `Amazon Kinesis Streams Key Concepts
        <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
        the *Amazon Kinesis Streams Developer Guide* .

    - **RunCommandParameters** *(dict) --*

      Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

      - **RunCommandTargets** *(list) --*

        Currently, we support including only one ``RunCommandTarget`` block, which specifies
        either an array of ``InstanceIds`` or a tag.

        - *(dict) --*

          Information about the EC2 instances that are to be sent the command, specified as
          key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
          key can specify multiple values.

          - **Key** *(string) --*

            Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

          - **Values** *(list) --*

            If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
            is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

            - *(string) --*

    - **EcsParameters** *(dict) --*

      Contains the Amazon ECS task definition and task count to be used if the event target is
      an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
      the *Amazon EC2 Container Service Developer Guide* .

      - **TaskDefinitionArn** *(string) --*

        The ARN of the task definition to use if the event target is an Amazon ECS task.

      - **TaskCount** *(integer) --*

        The number of tasks to create based on ``TaskDefinition`` . The default is 1.

      - **LaunchType** *(string) --*

        Specifies the launch type on which your task is running. The launch type that you
        specify here must match one of the launch type (compatibilities) of the target task.
        The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
        ECS is supported. For more information, see `AWS Fargate on Amazon ECS
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
        the *Amazon Elastic Container Service Developer Guide* .

      - **NetworkConfiguration** *(dict) --*

        Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
        specifies the VPC subnets and security groups associated with the task and whether a
        public IP address is to be used. This structure is required if ``LaunchType`` is
        ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

        If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
        ``awsvpc`` network mode, the task fails.

        - **awsvpcConfiguration** *(dict) --*

          Use this structure to specify the VPC subnets and security groups for the task and
          whether a public IP address is to be used. This structure is relevant only for ECS
          tasks that use the ``awsvpc`` network mode.

          - **Subnets** *(list) --*

            Specifies the subnets associated with the task. These subnets must all be in the
            same VPC. You can specify as many as 16 subnets.

            - *(string) --*

          - **SecurityGroups** *(list) --*

            Specifies the security groups associated with the task. These security groups must
            all be in the same VPC. You can specify as many as five security groups. If you
            don't specify a security group, the default security group for the VPC is used.

            - *(string) --*

          - **AssignPublicIp** *(string) --*

            Specifies whether the task's elastic network interface receives a public IP
            address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
            is set to ``FARGATE`` .

      - **PlatformVersion** *(string) --*

        Specifies the platform version for the task. Specify only the numeric portion of the
        platform version, such as ``1.1.0`` .

        This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
        about valid platform versions, see `AWS Fargate Platform Versions
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .

      - **Group** *(string) --*

        Specifies an ECS task group for the task. The maximum length is 255 characters.

    - **BatchParameters** *(dict) --*

      If the event target is an AWS Batch job, this contains the job definition, job name, and
      other parameters. For more information, see `Jobs
      <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
      Guide* .

      - **JobDefinition** *(string) --*

        The ARN or name of the job definition to use if the event target is an AWS Batch job.
        This job definition must already exist.

      - **JobName** *(string) --*

        The name to use for this execution of the job, if the target is an AWS Batch job.

      - **ArrayProperties** *(dict) --*

        The array properties for the submitted job, such as the size of the array. The array
        size can be between 2 and 10,000. If you specify array properties for a job, it becomes
        an array job. This parameter is used only if the target is an AWS Batch job.

        - **Size** *(integer) --*

          The size of the array, if this is an array batch job. Valid values are integers
          between 2 and 10,000.

      - **RetryStrategy** *(dict) --*

        The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
        strategy is the number of times to retry the failed job execution. Valid values are
        1–10. When you specify a retry strategy here, it overrides the retry strategy defined
        in the job definition.

        - **Attempts** *(integer) --*

          The number of times to attempt to retry, if the job fails. Valid values are 1–10.

    - **SqsParameters** *(dict) --*

      Contains the message group ID to use when the target is a FIFO queue.

      If you specify an SQS FIFO queue as a target, the queue must have content-based
      deduplication enabled.

      - **MessageGroupId** *(string) --*

        The FIFO message group ID to use as the target.
    """


_ClientListTargetsByRuleResponseTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTypeDef",
    {"Targets": List[ClientListTargetsByRuleResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTargetsByRuleResponseTypeDef(_ClientListTargetsByRuleResponseTypeDef):
    """
    Type definition for `ClientListTargetsByRule` `Response`

    - **Targets** *(list) --*

      The targets assigned to the rule.

      - *(dict) --*

        Targets are the resources to be invoked when a rule is triggered. For a complete list of
        services and resources that can be set as a target, see  PutTargets .

        If you're setting the event bus of another account as the target and that account granted
        permission to your account through an organization instead of directly by the account ID,
        you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
        more information, see `Sending and Receiving Events Between AWS Accounts
        <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
        in the *Amazon EventBridge User Guide* .

        - **Id** *(string) --*

          A name for the target. Use a string that will help you identify the target. Each target
          associated with a rule must have an ``Id`` unique for that rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the target.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule
          is triggered. If one rule triggers multiple targets, you can use a different IAM role for
          each target.

        - **Input** *(string) --*

          Valid JSON text passed to the target. In this case, nothing from the event itself is
          passed to the target. For more information, see `The JavaScript Object Notation (JSON)
          Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

        - **InputPath** *(string) --*

          The value of the JSONPath that is used for extracting part of the matched event when
          passing it to the target. You must use JSON dot notation, not bracket notation. For more
          information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

        - **InputTransformer** *(dict) --*

          Settings to enable you to provide custom input to a target based on certain event data.
          You can extract one or more key-value pairs from the event and then use that data to send
          customized input to the target.

          - **InputPathsMap** *(dict) --*

            Map of JSON paths to be extracted from the event. You can then insert these in the
            template in ``InputTemplate`` to produce the output to be sent to the target.

             ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
             You can have as many as 10 key-value pairs. You must use JSON dot notation, not
             bracket notation.

            The keys can't start with ``"AWS"`` .

            - *(string) --*

              - *(string) --*

          - **InputTemplate** *(string) --*

            Input template where you specify placeholders that will be filled with the values of
            the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
            ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

            If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
            restrictions apply:

            * The placeholder can't be used as an object key

            * Object values can't include quote marks

            The following example shows the syntax for using ``InputPathsMap`` and
            ``InputTemplate`` .

             ``"InputTransformer":``

             ``{``

             ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

             ``"InputTemplate": "<instance> is in state <status>"``

             ``}``

            To have the ``InputTemplate`` include quote marks within a JSON string, escape each
            quote marks with a slash, as in the following example:

             ``"InputTransformer":``

             ``{``

             ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

             ``"InputTemplate": "<instance> is in state \\"<status>\\""``

             ``}``

        - **KinesisParameters** *(dict) --*

          The custom parameter that you can use to control the shard assignment when the target is
          a Kinesis data stream. If you don't include this parameter, the default is to use the
          ``eventId`` as the partition key.

          - **PartitionKeyPath** *(string) --*

            The JSON path to be extracted from the event and used as the partition key. For more
            information, see `Amazon Kinesis Streams Key Concepts
            <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
            the *Amazon Kinesis Streams Developer Guide* .

        - **RunCommandParameters** *(dict) --*

          Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

          - **RunCommandTargets** *(list) --*

            Currently, we support including only one ``RunCommandTarget`` block, which specifies
            either an array of ``InstanceIds`` or a tag.

            - *(dict) --*

              Information about the EC2 instances that are to be sent the command, specified as
              key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
              key can specify multiple values.

              - **Key** *(string) --*

                Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

              - **Values** *(list) --*

                If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
                is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

                - *(string) --*

        - **EcsParameters** *(dict) --*

          Contains the Amazon ECS task definition and task count to be used if the event target is
          an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
          the *Amazon EC2 Container Service Developer Guide* .

          - **TaskDefinitionArn** *(string) --*

            The ARN of the task definition to use if the event target is an Amazon ECS task.

          - **TaskCount** *(integer) --*

            The number of tasks to create based on ``TaskDefinition`` . The default is 1.

          - **LaunchType** *(string) --*

            Specifies the launch type on which your task is running. The launch type that you
            specify here must match one of the launch type (compatibilities) of the target task.
            The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
            ECS is supported. For more information, see `AWS Fargate on Amazon ECS
            <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
            the *Amazon Elastic Container Service Developer Guide* .

          - **NetworkConfiguration** *(dict) --*

            Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
            specifies the VPC subnets and security groups associated with the task and whether a
            public IP address is to be used. This structure is required if ``LaunchType`` is
            ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

            If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
            ``awsvpc`` network mode, the task fails.

            - **awsvpcConfiguration** *(dict) --*

              Use this structure to specify the VPC subnets and security groups for the task and
              whether a public IP address is to be used. This structure is relevant only for ECS
              tasks that use the ``awsvpc`` network mode.

              - **Subnets** *(list) --*

                Specifies the subnets associated with the task. These subnets must all be in the
                same VPC. You can specify as many as 16 subnets.

                - *(string) --*

              - **SecurityGroups** *(list) --*

                Specifies the security groups associated with the task. These security groups must
                all be in the same VPC. You can specify as many as five security groups. If you
                don't specify a security group, the default security group for the VPC is used.

                - *(string) --*

              - **AssignPublicIp** *(string) --*

                Specifies whether the task's elastic network interface receives a public IP
                address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
                is set to ``FARGATE`` .

          - **PlatformVersion** *(string) --*

            Specifies the platform version for the task. Specify only the numeric portion of the
            platform version, such as ``1.1.0`` .

            This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
            about valid platform versions, see `AWS Fargate Platform Versions
            <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
            in the *Amazon Elastic Container Service Developer Guide* .

          - **Group** *(string) --*

            Specifies an ECS task group for the task. The maximum length is 255 characters.

        - **BatchParameters** *(dict) --*

          If the event target is an AWS Batch job, this contains the job definition, job name, and
          other parameters. For more information, see `Jobs
          <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
          Guide* .

          - **JobDefinition** *(string) --*

            The ARN or name of the job definition to use if the event target is an AWS Batch job.
            This job definition must already exist.

          - **JobName** *(string) --*

            The name to use for this execution of the job, if the target is an AWS Batch job.

          - **ArrayProperties** *(dict) --*

            The array properties for the submitted job, such as the size of the array. The array
            size can be between 2 and 10,000. If you specify array properties for a job, it becomes
            an array job. This parameter is used only if the target is an AWS Batch job.

            - **Size** *(integer) --*

              The size of the array, if this is an array batch job. Valid values are integers
              between 2 and 10,000.

          - **RetryStrategy** *(dict) --*

            The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
            strategy is the number of times to retry the failed job execution. Valid values are
            1–10. When you specify a retry strategy here, it overrides the retry strategy defined
            in the job definition.

            - **Attempts** *(integer) --*

              The number of times to attempt to retry, if the job fails. Valid values are 1–10.

        - **SqsParameters** *(dict) --*

          Contains the message group ID to use when the target is a FIFO queue.

          If you specify an SQS FIFO queue as a target, the queue must have content-based
          deduplication enabled.

          - **MessageGroupId** *(string) --*

            The FIFO message group ID to use as the target.

    - **NextToken** *(string) --*

      Indicates whether there are additional results to retrieve. If there are no more results, the
      value is null.
    """


_ClientPutEventsEntriesTypeDef = TypedDict(
    "_ClientPutEventsEntriesTypeDef",
    {
        "Time": datetime,
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
    },
    total=False,
)


class ClientPutEventsEntriesTypeDef(_ClientPutEventsEntriesTypeDef):
    """
    Type definition for `ClientPutEvents` `Entries`

    Represents an event to be submitted.

    - **Time** *(datetime) --*

      The timestamp of the event, per `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339.txt>`__ . If
      no timestamp is provided, the timestamp of the  PutEvents call is used.

    - **Source** *(string) --*

      The source of the event. This field is required.

    - **Resources** *(list) --*

      AWS resources, identified by Amazon Resource Name (ARN), that the event primarily concerns.
      Any number, including zero, can be present.

      - *(string) --*

    - **DetailType** *(string) --*

      Free-form string used to decide which fields to expect in the event detail. This field is
      required.

    - **Detail** *(string) --*

      A valid JSON object. There is no other schema imposed. The JSON object can contain fields and
      nested subobjects.

      This field is required.

    - **EventBusName** *(string) --*

      The event bus that will receive the event. Only the rules that are associated with this event
      bus can match the event.
    """


_ClientPutEventsResponseEntriesTypeDef = TypedDict(
    "_ClientPutEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutEventsResponseEntriesTypeDef(_ClientPutEventsResponseEntriesTypeDef):
    """
    Type definition for `ClientPutEventsResponse` `Entries`

    Represents an event that failed to be submitted.

    - **EventId** *(string) --*

      The ID of the event.

    - **ErrorCode** *(string) --*

      The error code that indicates why the event submission failed.

    - **ErrorMessage** *(string) --*

      The error message that explains why the event submission failed.
    """


_ClientPutEventsResponseTypeDef = TypedDict(
    "_ClientPutEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutEventsResponseEntriesTypeDef]},
    total=False,
)


class ClientPutEventsResponseTypeDef(_ClientPutEventsResponseTypeDef):
    """
    Type definition for `ClientPutEvents` `Response`

    - **FailedEntryCount** *(integer) --*

      The number of failed entries.

    - **Entries** *(list) --*

      The successfully and unsuccessfully ingested events results. If the ingestion was successful,
      the entry has the event ID in it. Otherwise, you can use the error code and error message to
      identify the problem with the entry.

      - *(dict) --*

        Represents an event that failed to be submitted.

        - **EventId** *(string) --*

          The ID of the event.

        - **ErrorCode** *(string) --*

          The error code that indicates why the event submission failed.

        - **ErrorMessage** *(string) --*

          The error message that explains why the event submission failed.
    """


_ClientPutPartnerEventsEntriesTypeDef = TypedDict(
    "_ClientPutPartnerEventsEntriesTypeDef",
    {
        "Time": datetime,
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
    },
    total=False,
)


class ClientPutPartnerEventsEntriesTypeDef(_ClientPutPartnerEventsEntriesTypeDef):
    """
    Type definition for `ClientPutPartnerEvents` `Entries`

    The details about an event generated by an SaaS partner.

    - **Time** *(datetime) --*

      The date and time of the event.

    - **Source** *(string) --*

      The event source that is generating the evntry. This field is required.

    - **Resources** *(list) --*

      AWS resources, identified by Amazon Resource Name (ARN), that the event primarily concerns.
      Any number, including zero, can be present.

      - *(string) --*

    - **DetailType** *(string) --*

      A free-form string used to decide which fields to expect in the event detail. This field is
      required.

    - **Detail** *(string) --*

      A valid JSON object. There is no other schema imposed. The JSON object can contain fields and
      nested subobjects. This field is required.
    """


_ClientPutPartnerEventsResponseEntriesTypeDef = TypedDict(
    "_ClientPutPartnerEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutPartnerEventsResponseEntriesTypeDef(
    _ClientPutPartnerEventsResponseEntriesTypeDef
):
    """
    Type definition for `ClientPutPartnerEventsResponse` `Entries`

    Represents an event that a partner tried to generate but failed.

    - **EventId** *(string) --*

      The ID of the event.

    - **ErrorCode** *(string) --*

      The error code that indicates why the event submission failed.

    - **ErrorMessage** *(string) --*

      The error message that explains why the event submission failed.
    """


_ClientPutPartnerEventsResponseTypeDef = TypedDict(
    "_ClientPutPartnerEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List[ClientPutPartnerEventsResponseEntriesTypeDef],
    },
    total=False,
)


class ClientPutPartnerEventsResponseTypeDef(_ClientPutPartnerEventsResponseTypeDef):
    """
    Type definition for `ClientPutPartnerEvents` `Response`

    - **FailedEntryCount** *(integer) --*

      The number of events from this operation that couldn't be written to the partner event bus.

    - **Entries** *(list) --*

      The list of events from this operation that were successfully written to the partner event
      bus.

      - *(dict) --*

        Represents an event that a partner tried to generate but failed.

        - **EventId** *(string) --*

          The ID of the event.

        - **ErrorCode** *(string) --*

          The error code that indicates why the event submission failed.

        - **ErrorMessage** *(string) --*

          The error message that explains why the event submission failed.
    """


_ClientPutPermissionConditionTypeDef = TypedDict(
    "_ClientPutPermissionConditionTypeDef", {"Type": str, "Key": str, "Value": str}
)


class ClientPutPermissionConditionTypeDef(_ClientPutPermissionConditionTypeDef):
    """
    Type definition for `ClientPutPermission` `Condition`

    This parameter enables you to limit the permission to accounts that fulfill a certain condition,
    such as being a member of a certain AWS organization. For more information about AWS
    Organizations, see `What Is AWS Organizations?
    <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`__ in the
    *AWS Organizations User Guide* .

    If you specify ``Condition`` with an AWS organization ID and specify "*" as the value for
    ``Principal`` , you grant permission to all the accounts in the named organization.

    The ``Condition`` is a JSON string that must contain ``Type`` , ``Key`` , and ``Value`` fields.

    - **Type** *(string) --* **[REQUIRED]**

      The type of condition. Currently, the only supported value is ``StringEquals`` .

    - **Key** *(string) --* **[REQUIRED]**

      The key for the condition. Currently, the only supported key is ``aws:PrincipalOrgID`` .

    - **Value** *(string) --* **[REQUIRED]**

      The value for the key. Currently, this must be the ID of the organization.
    """


_ClientPutRuleResponseTypeDef = TypedDict(
    "_ClientPutRuleResponseTypeDef", {"RuleArn": str}, total=False
)


class ClientPutRuleResponseTypeDef(_ClientPutRuleResponseTypeDef):
    """
    Type definition for `ClientPutRule` `Response`

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.
    """


_ClientPutRuleTagsTypeDef = TypedDict(
    "_ClientPutRuleTagsTypeDef", {"Key": str, "Value": str}
)


class ClientPutRuleTagsTypeDef(_ClientPutRuleTagsTypeDef):
    """
    Type definition for `ClientPutRule` `Tags`

    A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.

    - **Key** *(string) --* **[REQUIRED]**

      A string that you can use to assign a value. The combination of tag keys and values can help
      you organize and categorize your resources.

    - **Value** *(string) --* **[REQUIRED]**

      The value for the specified tag key.
    """


_ClientPutTargetsResponseFailedEntriesTypeDef = TypedDict(
    "_ClientPutTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutTargetsResponseFailedEntriesTypeDef(
    _ClientPutTargetsResponseFailedEntriesTypeDef
):
    """
    Type definition for `ClientPutTargetsResponse` `FailedEntries`

    Represents a target that failed to be added to a rule.

    - **TargetId** *(string) --*

      The ID of the target.

    - **ErrorCode** *(string) --*

      The error code that indicates why the target addition failed. If the value is
      ``ConcurrentModificationException`` , too many requests were made at the same time.

    - **ErrorMessage** *(string) --*

      The error message that explains why the target addition failed.
    """


_ClientPutTargetsResponseTypeDef = TypedDict(
    "_ClientPutTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[ClientPutTargetsResponseFailedEntriesTypeDef],
    },
    total=False,
)


class ClientPutTargetsResponseTypeDef(_ClientPutTargetsResponseTypeDef):
    """
    Type definition for `ClientPutTargets` `Response`

    - **FailedEntryCount** *(integer) --*

      The number of failed entries.

    - **FailedEntries** *(list) --*

      The failed target entries.

      - *(dict) --*

        Represents a target that failed to be added to a rule.

        - **TargetId** *(string) --*

          The ID of the target.

        - **ErrorCode** *(string) --*

          The error code that indicates why the target addition failed. If the value is
          ``ConcurrentModificationException`` , too many requests were made at the same time.

        - **ErrorMessage** *(string) --*

          The error message that explains why the target addition failed.
    """


_ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)


class ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef(
    _ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef
):
    """
    Type definition for `ClientPutTargetsTargetsBatchParameters` `ArrayProperties`

    The array properties for the submitted job, such as the size of the array. The array size
    can be between 2 and 10,000. If you specify array properties for a job, it becomes an array
    job. This parameter is used only if the target is an AWS Batch job.

    - **Size** *(integer) --*

      The size of the array, if this is an array batch job. Valid values are integers between 2
      and 10,000.
    """


_ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)


class ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef(
    _ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef
):
    """
    Type definition for `ClientPutTargetsTargetsBatchParameters` `RetryStrategy`

    The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
    strategy is the number of times to retry the failed job execution. Valid values are 1–10.
    When you specify a retry strategy here, it overrides the retry strategy defined in the job
    definition.

    - **Attempts** *(integer) --*

      The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_RequiredClientPutTargetsTargetsBatchParametersTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsBatchParametersTypeDef",
    {"JobDefinition": str, "JobName": str},
)
_OptionalClientPutTargetsTargetsBatchParametersTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsBatchParametersTypeDef",
    {
        "ArrayProperties": ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ClientPutTargetsTargetsBatchParametersTypeDef(
    _RequiredClientPutTargetsTargetsBatchParametersTypeDef,
    _OptionalClientPutTargetsTargetsBatchParametersTypeDef,
):
    """
    Type definition for `ClientPutTargetsTargets` `BatchParameters`

    If the event target is an AWS Batch job, this contains the job definition, job name, and
    other parameters. For more information, see `Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
    Guide* .

    - **JobDefinition** *(string) --* **[REQUIRED]**

      The ARN or name of the job definition to use if the event target is an AWS Batch job. This
      job definition must already exist.

    - **JobName** *(string) --* **[REQUIRED]**

      The name to use for this execution of the job, if the target is an AWS Batch job.

    - **ArrayProperties** *(dict) --*

      The array properties for the submitted job, such as the size of the array. The array size
      can be between 2 and 10,000. If you specify array properties for a job, it becomes an array
      job. This parameter is used only if the target is an AWS Batch job.

      - **Size** *(integer) --*

        The size of the array, if this is an array batch job. Valid values are integers between 2
        and 10,000.

    - **RetryStrategy** *(dict) --*

      The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
      strategy is the number of times to retry the failed job execution. Valid values are 1–10.
      When you specify a retry strategy here, it overrides the retry strategy defined in the job
      definition.

      - **Attempts** *(integer) --*

        The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_RequiredClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {"Subnets": List[str]},
)
_OptionalClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {"SecurityGroups": List[str], "AssignPublicIp": str},
    total=False,
)


class ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _RequiredClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef,
    _OptionalClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef,
):
    """
    Type definition for `ClientPutTargetsTargetsEcsParametersNetworkConfiguration` `awsvpcConfiguration`

    Use this structure to specify the VPC subnets and security groups for the task and
    whether a public IP address is to be used. This structure is relevant only for ECS tasks
    that use the ``awsvpc`` network mode.

    - **Subnets** *(list) --* **[REQUIRED]**

      Specifies the subnets associated with the task. These subnets must all be in the same
      VPC. You can specify as many as 16 subnets.

      - *(string) --*

    - **SecurityGroups** *(list) --*

      Specifies the security groups associated with the task. These security groups must all
      be in the same VPC. You can specify as many as five security groups. If you don't
      specify a security group, the default security group for the VPC is used.

      - *(string) --*

    - **AssignPublicIp** *(string) --*

      Specifies whether the task's elastic network interface receives a public IP address.
      You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to
      ``FARGATE`` .
    """


_ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef(
    _ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef
):
    """
    Type definition for `ClientPutTargetsTargetsEcsParameters` `NetworkConfiguration`

    Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
    specifies the VPC subnets and security groups associated with the task and whether a public
    IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE``
    because the ``awsvpc`` mode is required for Fargate tasks.

    If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the ``awsvpc``
    network mode, the task fails.

    - **awsvpcConfiguration** *(dict) --*

      Use this structure to specify the VPC subnets and security groups for the task and
      whether a public IP address is to be used. This structure is relevant only for ECS tasks
      that use the ``awsvpc`` network mode.

      - **Subnets** *(list) --* **[REQUIRED]**

        Specifies the subnets associated with the task. These subnets must all be in the same
        VPC. You can specify as many as 16 subnets.

        - *(string) --*

      - **SecurityGroups** *(list) --*

        Specifies the security groups associated with the task. These security groups must all
        be in the same VPC. You can specify as many as five security groups. If you don't
        specify a security group, the default security group for the VPC is used.

        - *(string) --*

      - **AssignPublicIp** *(string) --*

        Specifies whether the task's elastic network interface receives a public IP address.
        You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to
        ``FARGATE`` .
    """


_RequiredClientPutTargetsTargetsEcsParametersTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsEcsParametersTypeDef", {"TaskDefinitionArn": str}
)
_OptionalClientPutTargetsTargetsEcsParametersTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsEcsParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": str,
        "NetworkConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)


class ClientPutTargetsTargetsEcsParametersTypeDef(
    _RequiredClientPutTargetsTargetsEcsParametersTypeDef,
    _OptionalClientPutTargetsTargetsEcsParametersTypeDef,
):
    """
    Type definition for `ClientPutTargetsTargets` `EcsParameters`

    Contains the Amazon ECS task definition and task count to be used if the event target is an
    Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the
    *Amazon EC2 Container Service Developer Guide* .

    - **TaskDefinitionArn** *(string) --* **[REQUIRED]**

      The ARN of the task definition to use if the event target is an Amazon ECS task.

    - **TaskCount** *(integer) --*

      The number of tasks to create based on ``TaskDefinition`` . The default is 1.

    - **LaunchType** *(string) --*

      Specifies the launch type on which your task is running. The launch type that you specify
      here must match one of the launch type (compatibilities) of the target task. The
      ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is
      supported. For more information, see `AWS Fargate on Amazon ECS
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in the
      *Amazon Elastic Container Service Developer Guide* .

    - **NetworkConfiguration** *(dict) --*

      Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
      specifies the VPC subnets and security groups associated with the task and whether a public
      IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE``
      because the ``awsvpc`` mode is required for Fargate tasks.

      If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the ``awsvpc``
      network mode, the task fails.

      - **awsvpcConfiguration** *(dict) --*

        Use this structure to specify the VPC subnets and security groups for the task and
        whether a public IP address is to be used. This structure is relevant only for ECS tasks
        that use the ``awsvpc`` network mode.

        - **Subnets** *(list) --* **[REQUIRED]**

          Specifies the subnets associated with the task. These subnets must all be in the same
          VPC. You can specify as many as 16 subnets.

          - *(string) --*

        - **SecurityGroups** *(list) --*

          Specifies the security groups associated with the task. These security groups must all
          be in the same VPC. You can specify as many as five security groups. If you don't
          specify a security group, the default security group for the VPC is used.

          - *(string) --*

        - **AssignPublicIp** *(string) --*

          Specifies whether the task's elastic network interface receives a public IP address.
          You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to
          ``FARGATE`` .

    - **PlatformVersion** *(string) --*

      Specifies the platform version for the task. Specify only the numeric portion of the
      platform version, such as ``1.1.0`` .

      This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about
      valid platform versions, see `AWS Fargate Platform Versions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in
      the *Amazon Elastic Container Service Developer Guide* .

    - **Group** *(string) --*

      Specifies an ECS task group for the task. The maximum length is 255 characters.
    """


_RequiredClientPutTargetsTargetsInputTransformerTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsInputTransformerTypeDef", {"InputTemplate": str}
)
_OptionalClientPutTargetsTargetsInputTransformerTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str]},
    total=False,
)


class ClientPutTargetsTargetsInputTransformerTypeDef(
    _RequiredClientPutTargetsTargetsInputTransformerTypeDef,
    _OptionalClientPutTargetsTargetsInputTransformerTypeDef,
):
    """
    Type definition for `ClientPutTargetsTargets` `InputTransformer`

    Settings to enable you to provide custom input to a target based on certain event data. You
    can extract one or more key-value pairs from the event and then use that data to send
    customized input to the target.

    - **InputPathsMap** *(dict) --*

      Map of JSON paths to be extracted from the event. You can then insert these in the template
      in ``InputTemplate`` to produce the output to be sent to the target.

       ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path. You
       can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket
       notation.

      The keys can't start with ``"AWS"`` .

      - *(string) --*

        - *(string) --*

    - **InputTemplate** *(string) --* **[REQUIRED]**

      Input template where you specify placeholders that will be filled with the values of the
      keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
      ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

      If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
      restrictions apply:

      * The placeholder can't be used as an object key

      * Object values can't include quote marks

      The following example shows the syntax for using ``InputPathsMap`` and ``InputTemplate`` .

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state <status>"``

       ``}``

      To have the ``InputTemplate`` include quote marks within a JSON string, escape each quote
      marks with a slash, as in the following example:

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state \\"<status>\\""``

       ``}``
    """


_ClientPutTargetsTargetsKinesisParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsKinesisParametersTypeDef", {"PartitionKeyPath": str}
)


class ClientPutTargetsTargetsKinesisParametersTypeDef(
    _ClientPutTargetsTargetsKinesisParametersTypeDef
):
    """
    Type definition for `ClientPutTargetsTargets` `KinesisParameters`

    The custom parameter that you can use to control the shard assignment when the target is a
    Kinesis data stream. If you don't include this parameter, the default is to use the
    ``eventId`` as the partition key.

    - **PartitionKeyPath** *(string) --* **[REQUIRED]**

      The JSON path to be extracted from the event and used as the partition key. For more
      information, see `Amazon Kinesis Streams Key Concepts
      <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the
      *Amazon Kinesis Streams Developer Guide* .
    """


_ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
)


class ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    """
    Type definition for `ClientPutTargetsTargetsRunCommandParameters` `RunCommandTargets`

    Information about the EC2 instances that are to be sent the command, specified as
    key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key
    can specify multiple values.

    - **Key** *(string) --* **[REQUIRED]**

      Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

    - **Values** *(list) --* **[REQUIRED]**

      If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is
      ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

      - *(string) --*
    """


_ClientPutTargetsTargetsRunCommandParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
)


class ClientPutTargetsTargetsRunCommandParametersTypeDef(
    _ClientPutTargetsTargetsRunCommandParametersTypeDef
):
    """
    Type definition for `ClientPutTargetsTargets` `RunCommandParameters`

    Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

    - **RunCommandTargets** *(list) --* **[REQUIRED]**

      Currently, we support including only one ``RunCommandTarget`` block, which specifies either
      an array of ``InstanceIds`` or a tag.

      - *(dict) --*

        Information about the EC2 instances that are to be sent the command, specified as
        key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key
        can specify multiple values.

        - **Key** *(string) --* **[REQUIRED]**

          Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

        - **Values** *(list) --* **[REQUIRED]**

          If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is
          ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

          - *(string) --*
    """


_ClientPutTargetsTargetsSqsParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsSqsParametersTypeDef", {"MessageGroupId": str}, total=False
)


class ClientPutTargetsTargetsSqsParametersTypeDef(
    _ClientPutTargetsTargetsSqsParametersTypeDef
):
    """
    Type definition for `ClientPutTargetsTargets` `SqsParameters`

    Contains the message group ID to use when the target is a FIFO queue.

    If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication
    enabled.

    - **MessageGroupId** *(string) --*

      The FIFO message group ID to use as the target.
    """


_RequiredClientPutTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsTypeDef", {"Id": str, "Arn": str}
)
_OptionalClientPutTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientPutTargetsTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientPutTargetsTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientPutTargetsTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientPutTargetsTargetsEcsParametersTypeDef,
        "BatchParameters": ClientPutTargetsTargetsBatchParametersTypeDef,
        "SqsParameters": ClientPutTargetsTargetsSqsParametersTypeDef,
    },
    total=False,
)


class ClientPutTargetsTargetsTypeDef(
    _RequiredClientPutTargetsTargetsTypeDef, _OptionalClientPutTargetsTargetsTypeDef
):
    """
    Type definition for `ClientPutTargets` `Targets`

    Targets are the resources to be invoked when a rule is triggered. For a complete list of
    services and resources that can be set as a target, see  PutTargets .

    If you're setting the event bus of another account as the target and that account granted
    permission to your account through an organization instead of directly by the account ID, you
    must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more
    information, see `Sending and Receiving Events Between AWS Accounts
    <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
    in the *Amazon EventBridge User Guide* .

    - **Id** *(string) --* **[REQUIRED]**

      A name for the target. Use a string that will help you identify the target. Each target
      associated with a rule must have an ``Id`` unique for that rule.

    - **Arn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the target.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is
      triggered. If one rule triggers multiple targets, you can use a different IAM role for each
      target.

    - **Input** *(string) --*

      Valid JSON text passed to the target. In this case, nothing from the event itself is passed
      to the target. For more information, see `The JavaScript Object Notation (JSON) Data
      Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

    - **InputPath** *(string) --*

      The value of the JSONPath that is used for extracting part of the matched event when passing
      it to the target. You must use JSON dot notation, not bracket notation. For more information
      about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

    - **InputTransformer** *(dict) --*

      Settings to enable you to provide custom input to a target based on certain event data. You
      can extract one or more key-value pairs from the event and then use that data to send
      customized input to the target.

      - **InputPathsMap** *(dict) --*

        Map of JSON paths to be extracted from the event. You can then insert these in the template
        in ``InputTemplate`` to produce the output to be sent to the target.

         ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path. You
         can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket
         notation.

        The keys can't start with ``"AWS"`` .

        - *(string) --*

          - *(string) --*

      - **InputTemplate** *(string) --* **[REQUIRED]**

        Input template where you specify placeholders that will be filled with the values of the
        keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
        ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

        If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
        restrictions apply:

        * The placeholder can't be used as an object key

        * Object values can't include quote marks

        The following example shows the syntax for using ``InputPathsMap`` and ``InputTemplate`` .

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state <status>"``

         ``}``

        To have the ``InputTemplate`` include quote marks within a JSON string, escape each quote
        marks with a slash, as in the following example:

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state \\"<status>\\""``

         ``}``

    - **KinesisParameters** *(dict) --*

      The custom parameter that you can use to control the shard assignment when the target is a
      Kinesis data stream. If you don't include this parameter, the default is to use the
      ``eventId`` as the partition key.

      - **PartitionKeyPath** *(string) --* **[REQUIRED]**

        The JSON path to be extracted from the event and used as the partition key. For more
        information, see `Amazon Kinesis Streams Key Concepts
        <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the
        *Amazon Kinesis Streams Developer Guide* .

    - **RunCommandParameters** *(dict) --*

      Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

      - **RunCommandTargets** *(list) --* **[REQUIRED]**

        Currently, we support including only one ``RunCommandTarget`` block, which specifies either
        an array of ``InstanceIds`` or a tag.

        - *(dict) --*

          Information about the EC2 instances that are to be sent the command, specified as
          key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key
          can specify multiple values.

          - **Key** *(string) --* **[REQUIRED]**

            Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

          - **Values** *(list) --* **[REQUIRED]**

            If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is
            ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

            - *(string) --*

    - **EcsParameters** *(dict) --*

      Contains the Amazon ECS task definition and task count to be used if the event target is an
      Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the
      *Amazon EC2 Container Service Developer Guide* .

      - **TaskDefinitionArn** *(string) --* **[REQUIRED]**

        The ARN of the task definition to use if the event target is an Amazon ECS task.

      - **TaskCount** *(integer) --*

        The number of tasks to create based on ``TaskDefinition`` . The default is 1.

      - **LaunchType** *(string) --*

        Specifies the launch type on which your task is running. The launch type that you specify
        here must match one of the launch type (compatibilities) of the target task. The
        ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is
        supported. For more information, see `AWS Fargate on Amazon ECS
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in the
        *Amazon Elastic Container Service Developer Guide* .

      - **NetworkConfiguration** *(dict) --*

        Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
        specifies the VPC subnets and security groups associated with the task and whether a public
        IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE``
        because the ``awsvpc`` mode is required for Fargate tasks.

        If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the ``awsvpc``
        network mode, the task fails.

        - **awsvpcConfiguration** *(dict) --*

          Use this structure to specify the VPC subnets and security groups for the task and
          whether a public IP address is to be used. This structure is relevant only for ECS tasks
          that use the ``awsvpc`` network mode.

          - **Subnets** *(list) --* **[REQUIRED]**

            Specifies the subnets associated with the task. These subnets must all be in the same
            VPC. You can specify as many as 16 subnets.

            - *(string) --*

          - **SecurityGroups** *(list) --*

            Specifies the security groups associated with the task. These security groups must all
            be in the same VPC. You can specify as many as five security groups. If you don't
            specify a security group, the default security group for the VPC is used.

            - *(string) --*

          - **AssignPublicIp** *(string) --*

            Specifies whether the task's elastic network interface receives a public IP address.
            You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to
            ``FARGATE`` .

      - **PlatformVersion** *(string) --*

        Specifies the platform version for the task. Specify only the numeric portion of the
        platform version, such as ``1.1.0`` .

        This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about
        valid platform versions, see `AWS Fargate Platform Versions
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in
        the *Amazon Elastic Container Service Developer Guide* .

      - **Group** *(string) --*

        Specifies an ECS task group for the task. The maximum length is 255 characters.

    - **BatchParameters** *(dict) --*

      If the event target is an AWS Batch job, this contains the job definition, job name, and
      other parameters. For more information, see `Jobs
      <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
      Guide* .

      - **JobDefinition** *(string) --* **[REQUIRED]**

        The ARN or name of the job definition to use if the event target is an AWS Batch job. This
        job definition must already exist.

      - **JobName** *(string) --* **[REQUIRED]**

        The name to use for this execution of the job, if the target is an AWS Batch job.

      - **ArrayProperties** *(dict) --*

        The array properties for the submitted job, such as the size of the array. The array size
        can be between 2 and 10,000. If you specify array properties for a job, it becomes an array
        job. This parameter is used only if the target is an AWS Batch job.

        - **Size** *(integer) --*

          The size of the array, if this is an array batch job. Valid values are integers between 2
          and 10,000.

      - **RetryStrategy** *(dict) --*

        The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
        strategy is the number of times to retry the failed job execution. Valid values are 1–10.
        When you specify a retry strategy here, it overrides the retry strategy defined in the job
        definition.

        - **Attempts** *(integer) --*

          The number of times to attempt to retry, if the job fails. Valid values are 1–10.

    - **SqsParameters** *(dict) --*

      Contains the message group ID to use when the target is a FIFO queue.

      If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication
      enabled.

      - **MessageGroupId** *(string) --*

        The FIFO message group ID to use as the target.
    """


_ClientRemoveTargetsResponseFailedEntriesTypeDef = TypedDict(
    "_ClientRemoveTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRemoveTargetsResponseFailedEntriesTypeDef(
    _ClientRemoveTargetsResponseFailedEntriesTypeDef
):
    """
    Type definition for `ClientRemoveTargetsResponse` `FailedEntries`

    Represents a target that failed to be removed from a rule.

    - **TargetId** *(string) --*

      The ID of the target.

    - **ErrorCode** *(string) --*

      The error code that indicates why the target removal failed. If the value is
      ``ConcurrentModificationException`` , too many requests were made at the same time.

    - **ErrorMessage** *(string) --*

      The error message that explains why the target removal failed.
    """


_ClientRemoveTargetsResponseTypeDef = TypedDict(
    "_ClientRemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[ClientRemoveTargetsResponseFailedEntriesTypeDef],
    },
    total=False,
)


class ClientRemoveTargetsResponseTypeDef(_ClientRemoveTargetsResponseTypeDef):
    """
    Type definition for `ClientRemoveTargets` `Response`

    - **FailedEntryCount** *(integer) --*

      The number of failed entries.

    - **FailedEntries** *(list) --*

      The failed target entries.

      - *(dict) --*

        Represents a target that failed to be removed from a rule.

        - **TargetId** *(string) --*

          The ID of the target.

        - **ErrorCode** *(string) --*

          The error code that indicates why the target removal failed. If the value is
          ``ConcurrentModificationException`` , too many requests were made at the same time.

        - **ErrorMessage** *(string) --*

          The error message that explains why the target removal failed.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.

    - **Key** *(string) --* **[REQUIRED]**

      A string that you can use to assign a value. The combination of tag keys and values can help
      you organize and categorize your resources.

    - **Value** *(string) --* **[REQUIRED]**

      The value for the specified tag key.
    """


_ClientTestEventPatternResponseTypeDef = TypedDict(
    "_ClientTestEventPatternResponseTypeDef", {"Result": bool}, total=False
)


class ClientTestEventPatternResponseTypeDef(_ClientTestEventPatternResponseTypeDef):
    """
    Type definition for `ClientTestEventPattern` `Response`

    - **Result** *(boolean) --*

      Indicates whether the event matches the event pattern.
    """


_ListRuleNamesByTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRuleNamesByTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRuleNamesByTargetPaginatePaginationConfigTypeDef(
    _ListRuleNamesByTargetPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRuleNamesByTargetPaginate` `PaginationConfig`

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


_ListRuleNamesByTargetPaginateResponseTypeDef = TypedDict(
    "_ListRuleNamesByTargetPaginateResponseTypeDef",
    {"RuleNames": List[str]},
    total=False,
)


class ListRuleNamesByTargetPaginateResponseTypeDef(
    _ListRuleNamesByTargetPaginateResponseTypeDef
):
    """
    Type definition for `ListRuleNamesByTargetPaginate` `Response`

    - **RuleNames** *(list) --*

      The names of the rules that can invoke the given target.

      - *(string) --*
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
    "_ListRulesPaginateResponseRulesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": str,
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)


class ListRulesPaginateResponseRulesTypeDef(_ListRulesPaginateResponseRulesTypeDef):
    """
    Type definition for `ListRulesPaginateResponse` `Rules`

    Contains information about a rule in Amazon EventBridge.

    - **Name** *(string) --*

      The name of the rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **EventPattern** *(string) --*

      The event pattern of the rule. For more information, see `Event Patterns
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
      in the *Amazon EventBridge User Guide* .

    - **State** *(string) --*

      The state of the rule.

    - **Description** *(string) --*

      The description of the rule.

    - **ScheduleExpression** *(string) --*

      The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"``
      .

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the role that is used for target invocation.

    - **ManagedBy** *(string) --*

      If an AWS service created the rule on behalf of your account, this field displays the
      principal name of the service that created the rule.

    - **EventBusName** *(string) --*

      The event bus associated with the rule.
    """


_ListRulesPaginateResponseTypeDef = TypedDict(
    "_ListRulesPaginateResponseTypeDef",
    {"Rules": List[ListRulesPaginateResponseRulesTypeDef]},
    total=False,
)


class ListRulesPaginateResponseTypeDef(_ListRulesPaginateResponseTypeDef):
    """
    Type definition for `ListRulesPaginate` `Response`

    - **Rules** *(list) --*

      The rules that match the specified criteria.

      - *(dict) --*

        Contains information about a rule in Amazon EventBridge.

        - **Name** *(string) --*

          The name of the rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **EventPattern** *(string) --*

          The event pattern of the rule. For more information, see `Event Patterns
          <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`__
          in the *Amazon EventBridge User Guide* .

        - **State** *(string) --*

          The state of the rule.

        - **Description** *(string) --*

          The description of the rule.

        - **ScheduleExpression** *(string) --*

          The scheduling expression: for example, ``"cron(0 20 * * ? *)"`` or ``"rate(5 minutes)"``
          .

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the role that is used for target invocation.

        - **ManagedBy** *(string) --*

          If an AWS service created the rule on behalf of your account, this field displays the
          principal name of the service that created the rule.

        - **EventBusName** *(string) --*

          The event bus associated with the rule.
    """


_ListTargetsByRulePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsByRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsByRulePaginatePaginationConfigTypeDef(
    _ListTargetsByRulePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginate` `PaginationConfig`

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


_ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargetsBatchParameters` `ArrayProperties`

    The array properties for the submitted job, such as the size of the array. The array
    size can be between 2 and 10,000. If you specify array properties for a job, it becomes
    an array job. This parameter is used only if the target is an AWS Batch job.

    - **Size** *(integer) --*

      The size of the array, if this is an array batch job. Valid values are integers
      between 2 and 10,000.
    """


_ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargetsBatchParameters` `RetryStrategy`

    The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
    strategy is the number of times to retry the failed job execution. Valid values are
    1–10. When you specify a retry strategy here, it overrides the retry strategy defined
    in the job definition.

    - **Attempts** *(integer) --*

      The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `BatchParameters`

    If the event target is an AWS Batch job, this contains the job definition, job name, and
    other parameters. For more information, see `Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
    Guide* .

    - **JobDefinition** *(string) --*

      The ARN or name of the job definition to use if the event target is an AWS Batch job.
      This job definition must already exist.

    - **JobName** *(string) --*

      The name to use for this execution of the job, if the target is an AWS Batch job.

    - **ArrayProperties** *(dict) --*

      The array properties for the submitted job, such as the size of the array. The array
      size can be between 2 and 10,000. If you specify array properties for a job, it becomes
      an array job. This parameter is used only if the target is an AWS Batch job.

      - **Size** *(integer) --*

        The size of the array, if this is an array batch job. Valid values are integers
        between 2 and 10,000.

    - **RetryStrategy** *(dict) --*

      The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
      strategy is the number of times to retry the failed job execution. Valid values are
      1–10. When you specify a retry strategy here, it overrides the retry strategy defined
      in the job definition.

      - **Attempts** *(integer) --*

        The number of times to attempt to retry, if the job fails. Valid values are 1–10.
    """


_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {"Subnets": List[str], "SecurityGroups": List[str], "AssignPublicIp": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfiguration` `awsvpcConfiguration`

    Use this structure to specify the VPC subnets and security groups for the task and
    whether a public IP address is to be used. This structure is relevant only for ECS
    tasks that use the ``awsvpc`` network mode.

    - **Subnets** *(list) --*

      Specifies the subnets associated with the task. These subnets must all be in the
      same VPC. You can specify as many as 16 subnets.

      - *(string) --*

    - **SecurityGroups** *(list) --*

      Specifies the security groups associated with the task. These security groups must
      all be in the same VPC. You can specify as many as five security groups. If you
      don't specify a security group, the default security group for the VPC is used.

      - *(string) --*

    - **AssignPublicIp** *(string) --*

      Specifies whether the task's elastic network interface receives a public IP
      address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
      is set to ``FARGATE`` .
    """


_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargetsEcsParameters` `NetworkConfiguration`

    Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
    specifies the VPC subnets and security groups associated with the task and whether a
    public IP address is to be used. This structure is required if ``LaunchType`` is
    ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

    If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
    ``awsvpc`` network mode, the task fails.

    - **awsvpcConfiguration** *(dict) --*

      Use this structure to specify the VPC subnets and security groups for the task and
      whether a public IP address is to be used. This structure is relevant only for ECS
      tasks that use the ``awsvpc`` network mode.

      - **Subnets** *(list) --*

        Specifies the subnets associated with the task. These subnets must all be in the
        same VPC. You can specify as many as 16 subnets.

        - *(string) --*

      - **SecurityGroups** *(list) --*

        Specifies the security groups associated with the task. These security groups must
        all be in the same VPC. You can specify as many as five security groups. If you
        don't specify a security group, the default security group for the VPC is used.

        - *(string) --*

      - **AssignPublicIp** *(string) --*

        Specifies whether the task's elastic network interface receives a public IP
        address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
        is set to ``FARGATE`` .
    """


_ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": str,
        "NetworkConfiguration": ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `EcsParameters`

    Contains the Amazon ECS task definition and task count to be used if the event target is
    an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
    the *Amazon EC2 Container Service Developer Guide* .

    - **TaskDefinitionArn** *(string) --*

      The ARN of the task definition to use if the event target is an Amazon ECS task.

    - **TaskCount** *(integer) --*

      The number of tasks to create based on ``TaskDefinition`` . The default is 1.

    - **LaunchType** *(string) --*

      Specifies the launch type on which your task is running. The launch type that you
      specify here must match one of the launch type (compatibilities) of the target task.
      The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
      ECS is supported. For more information, see `AWS Fargate on Amazon ECS
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
      the *Amazon Elastic Container Service Developer Guide* .

    - **NetworkConfiguration** *(dict) --*

      Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
      specifies the VPC subnets and security groups associated with the task and whether a
      public IP address is to be used. This structure is required if ``LaunchType`` is
      ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

      If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
      ``awsvpc`` network mode, the task fails.

      - **awsvpcConfiguration** *(dict) --*

        Use this structure to specify the VPC subnets and security groups for the task and
        whether a public IP address is to be used. This structure is relevant only for ECS
        tasks that use the ``awsvpc`` network mode.

        - **Subnets** *(list) --*

          Specifies the subnets associated with the task. These subnets must all be in the
          same VPC. You can specify as many as 16 subnets.

          - *(string) --*

        - **SecurityGroups** *(list) --*

          Specifies the security groups associated with the task. These security groups must
          all be in the same VPC. You can specify as many as five security groups. If you
          don't specify a security group, the default security group for the VPC is used.

          - *(string) --*

        - **AssignPublicIp** *(string) --*

          Specifies whether the task's elastic network interface receives a public IP
          address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
          is set to ``FARGATE`` .

    - **PlatformVersion** *(string) --*

      Specifies the platform version for the task. Specify only the numeric portion of the
      platform version, such as ``1.1.0`` .

      This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
      about valid platform versions, see `AWS Fargate Platform Versions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .

    - **Group** *(string) --*

      Specifies an ECS task group for the task. The maximum length is 255 characters.
    """


_ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef(
    _ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `InputTransformer`

    Settings to enable you to provide custom input to a target based on certain event data.
    You can extract one or more key-value pairs from the event and then use that data to send
    customized input to the target.

    - **InputPathsMap** *(dict) --*

      Map of JSON paths to be extracted from the event. You can then insert these in the
      template in ``InputTemplate`` to produce the output to be sent to the target.

       ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
       You can have as many as 10 key-value pairs. You must use JSON dot notation, not
       bracket notation.

      The keys can't start with ``"AWS"`` .

      - *(string) --*

        - *(string) --*

    - **InputTemplate** *(string) --*

      Input template where you specify placeholders that will be filled with the values of
      the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
      ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

      If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
      restrictions apply:

      * The placeholder can't be used as an object key

      * Object values can't include quote marks

      The following example shows the syntax for using ``InputPathsMap`` and
      ``InputTemplate`` .

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state <status>"``

       ``}``

      To have the ``InputTemplate`` include quote marks within a JSON string, escape each
      quote marks with a slash, as in the following example:

       ``"InputTransformer":``

       ``{``

       ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

       ``"InputTemplate": "<instance> is in state \\"<status>\\""``

       ``}``
    """


_ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `KinesisParameters`

    The custom parameter that you can use to control the shard assignment when the target is
    a Kinesis data stream. If you don't include this parameter, the default is to use the
    ``eventId`` as the partition key.

    - **PartitionKeyPath** *(string) --*

      The JSON path to be extracted from the event and used as the partition key. For more
      information, see `Amazon Kinesis Streams Key Concepts
      <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
      the *Amazon Kinesis Streams Developer Guide* .
    """


_ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargetsRunCommandParameters` `RunCommandTargets`

    Information about the EC2 instances that are to be sent the command, specified as
    key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
    key can specify multiple values.

    - **Key** *(string) --*

      Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

    - **Values** *(list) --*

      If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
      is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

      - *(string) --*
    """


_ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `RunCommandParameters`

    Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

    - **RunCommandTargets** *(list) --*

      Currently, we support including only one ``RunCommandTarget`` block, which specifies
      either an array of ``InstanceIds`` or a tag.

      - *(dict) --*

        Information about the EC2 instances that are to be sent the command, specified as
        key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
        key can specify multiple values.

        - **Key** *(string) --*

          Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

        - **Values** *(list) --*

          If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
          is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

          - *(string) --*
    """


_ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponseTargets` `SqsParameters`

    Contains the message group ID to use when the target is a FIFO queue.

    If you specify an SQS FIFO queue as a target, the queue must have content-based
    deduplication enabled.

    - **MessageGroupId** *(string) --*

      The FIFO message group ID to use as the target.
    """


_ListTargetsByRulePaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef,
        "KinesisParameters": ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef,
        "EcsParameters": ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef,
        "BatchParameters": ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef,
        "SqsParameters": ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef,
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsTypeDef(
    _ListTargetsByRulePaginateResponseTargetsTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginateResponse` `Targets`

    Targets are the resources to be invoked when a rule is triggered. For a complete list of
    services and resources that can be set as a target, see  PutTargets .

    If you're setting the event bus of another account as the target and that account granted
    permission to your account through an organization instead of directly by the account ID,
    you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
    more information, see `Sending and Receiving Events Between AWS Accounts
    <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
    in the *Amazon EventBridge User Guide* .

    - **Id** *(string) --*

      A name for the target. Use a string that will help you identify the target. Each target
      associated with a rule must have an ``Id`` unique for that rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the target.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule
      is triggered. If one rule triggers multiple targets, you can use a different IAM role for
      each target.

    - **Input** *(string) --*

      Valid JSON text passed to the target. In this case, nothing from the event itself is
      passed to the target. For more information, see `The JavaScript Object Notation (JSON)
      Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

    - **InputPath** *(string) --*

      The value of the JSONPath that is used for extracting part of the matched event when
      passing it to the target. You must use JSON dot notation, not bracket notation. For more
      information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

    - **InputTransformer** *(dict) --*

      Settings to enable you to provide custom input to a target based on certain event data.
      You can extract one or more key-value pairs from the event and then use that data to send
      customized input to the target.

      - **InputPathsMap** *(dict) --*

        Map of JSON paths to be extracted from the event. You can then insert these in the
        template in ``InputTemplate`` to produce the output to be sent to the target.

         ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
         You can have as many as 10 key-value pairs. You must use JSON dot notation, not
         bracket notation.

        The keys can't start with ``"AWS"`` .

        - *(string) --*

          - *(string) --*

      - **InputTemplate** *(string) --*

        Input template where you specify placeholders that will be filled with the values of
        the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
        ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

        If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
        restrictions apply:

        * The placeholder can't be used as an object key

        * Object values can't include quote marks

        The following example shows the syntax for using ``InputPathsMap`` and
        ``InputTemplate`` .

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state <status>"``

         ``}``

        To have the ``InputTemplate`` include quote marks within a JSON string, escape each
        quote marks with a slash, as in the following example:

         ``"InputTransformer":``

         ``{``

         ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

         ``"InputTemplate": "<instance> is in state \\"<status>\\""``

         ``}``

    - **KinesisParameters** *(dict) --*

      The custom parameter that you can use to control the shard assignment when the target is
      a Kinesis data stream. If you don't include this parameter, the default is to use the
      ``eventId`` as the partition key.

      - **PartitionKeyPath** *(string) --*

        The JSON path to be extracted from the event and used as the partition key. For more
        information, see `Amazon Kinesis Streams Key Concepts
        <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
        the *Amazon Kinesis Streams Developer Guide* .

    - **RunCommandParameters** *(dict) --*

      Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

      - **RunCommandTargets** *(list) --*

        Currently, we support including only one ``RunCommandTarget`` block, which specifies
        either an array of ``InstanceIds`` or a tag.

        - *(dict) --*

          Information about the EC2 instances that are to be sent the command, specified as
          key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
          key can specify multiple values.

          - **Key** *(string) --*

            Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

          - **Values** *(list) --*

            If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
            is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

            - *(string) --*

    - **EcsParameters** *(dict) --*

      Contains the Amazon ECS task definition and task count to be used if the event target is
      an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
      the *Amazon EC2 Container Service Developer Guide* .

      - **TaskDefinitionArn** *(string) --*

        The ARN of the task definition to use if the event target is an Amazon ECS task.

      - **TaskCount** *(integer) --*

        The number of tasks to create based on ``TaskDefinition`` . The default is 1.

      - **LaunchType** *(string) --*

        Specifies the launch type on which your task is running. The launch type that you
        specify here must match one of the launch type (compatibilities) of the target task.
        The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
        ECS is supported. For more information, see `AWS Fargate on Amazon ECS
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
        the *Amazon Elastic Container Service Developer Guide* .

      - **NetworkConfiguration** *(dict) --*

        Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
        specifies the VPC subnets and security groups associated with the task and whether a
        public IP address is to be used. This structure is required if ``LaunchType`` is
        ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

        If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
        ``awsvpc`` network mode, the task fails.

        - **awsvpcConfiguration** *(dict) --*

          Use this structure to specify the VPC subnets and security groups for the task and
          whether a public IP address is to be used. This structure is relevant only for ECS
          tasks that use the ``awsvpc`` network mode.

          - **Subnets** *(list) --*

            Specifies the subnets associated with the task. These subnets must all be in the
            same VPC. You can specify as many as 16 subnets.

            - *(string) --*

          - **SecurityGroups** *(list) --*

            Specifies the security groups associated with the task. These security groups must
            all be in the same VPC. You can specify as many as five security groups. If you
            don't specify a security group, the default security group for the VPC is used.

            - *(string) --*

          - **AssignPublicIp** *(string) --*

            Specifies whether the task's elastic network interface receives a public IP
            address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
            is set to ``FARGATE`` .

      - **PlatformVersion** *(string) --*

        Specifies the platform version for the task. Specify only the numeric portion of the
        platform version, such as ``1.1.0`` .

        This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
        about valid platform versions, see `AWS Fargate Platform Versions
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .

      - **Group** *(string) --*

        Specifies an ECS task group for the task. The maximum length is 255 characters.

    - **BatchParameters** *(dict) --*

      If the event target is an AWS Batch job, this contains the job definition, job name, and
      other parameters. For more information, see `Jobs
      <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
      Guide* .

      - **JobDefinition** *(string) --*

        The ARN or name of the job definition to use if the event target is an AWS Batch job.
        This job definition must already exist.

      - **JobName** *(string) --*

        The name to use for this execution of the job, if the target is an AWS Batch job.

      - **ArrayProperties** *(dict) --*

        The array properties for the submitted job, such as the size of the array. The array
        size can be between 2 and 10,000. If you specify array properties for a job, it becomes
        an array job. This parameter is used only if the target is an AWS Batch job.

        - **Size** *(integer) --*

          The size of the array, if this is an array batch job. Valid values are integers
          between 2 and 10,000.

      - **RetryStrategy** *(dict) --*

        The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
        strategy is the number of times to retry the failed job execution. Valid values are
        1–10. When you specify a retry strategy here, it overrides the retry strategy defined
        in the job definition.

        - **Attempts** *(integer) --*

          The number of times to attempt to retry, if the job fails. Valid values are 1–10.

    - **SqsParameters** *(dict) --*

      Contains the message group ID to use when the target is a FIFO queue.

      If you specify an SQS FIFO queue as a target, the queue must have content-based
      deduplication enabled.

      - **MessageGroupId** *(string) --*

        The FIFO message group ID to use as the target.
    """


_ListTargetsByRulePaginateResponseTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTypeDef",
    {"Targets": List[ListTargetsByRulePaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsByRulePaginateResponseTypeDef(
    _ListTargetsByRulePaginateResponseTypeDef
):
    """
    Type definition for `ListTargetsByRulePaginate` `Response`

    - **Targets** *(list) --*

      The targets assigned to the rule.

      - *(dict) --*

        Targets are the resources to be invoked when a rule is triggered. For a complete list of
        services and resources that can be set as a target, see  PutTargets .

        If you're setting the event bus of another account as the target and that account granted
        permission to your account through an organization instead of directly by the account ID,
        you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
        more information, see `Sending and Receiving Events Between AWS Accounts
        <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
        in the *Amazon EventBridge User Guide* .

        - **Id** *(string) --*

          A name for the target. Use a string that will help you identify the target. Each target
          associated with a rule must have an ``Id`` unique for that rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the target.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule
          is triggered. If one rule triggers multiple targets, you can use a different IAM role for
          each target.

        - **Input** *(string) --*

          Valid JSON text passed to the target. In this case, nothing from the event itself is
          passed to the target. For more information, see `The JavaScript Object Notation (JSON)
          Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .

        - **InputPath** *(string) --*

          The value of the JSONPath that is used for extracting part of the matched event when
          passing it to the target. You must use JSON dot notation, not bracket notation. For more
          information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .

        - **InputTransformer** *(dict) --*

          Settings to enable you to provide custom input to a target based on certain event data.
          You can extract one or more key-value pairs from the event and then use that data to send
          customized input to the target.

          - **InputPathsMap** *(dict) --*

            Map of JSON paths to be extracted from the event. You can then insert these in the
            template in ``InputTemplate`` to produce the output to be sent to the target.

             ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path.
             You can have as many as 10 key-value pairs. You must use JSON dot notation, not
             bracket notation.

            The keys can't start with ``"AWS"`` .

            - *(string) --*

              - *(string) --*

          - **InputTemplate** *(string) --*

            Input template where you specify placeholders that will be filled with the values of
            the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each
            ``InputPathsMaps`` value in brackets: <*value* >. The InputTemplate must be valid JSON.

            If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following
            restrictions apply:

            * The placeholder can't be used as an object key

            * Object values can't include quote marks

            The following example shows the syntax for using ``InputPathsMap`` and
            ``InputTemplate`` .

             ``"InputTransformer":``

             ``{``

             ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

             ``"InputTemplate": "<instance> is in state <status>"``

             ``}``

            To have the ``InputTemplate`` include quote marks within a JSON string, escape each
            quote marks with a slash, as in the following example:

             ``"InputTransformer":``

             ``{``

             ``"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},``

             ``"InputTemplate": "<instance> is in state \\"<status>\\""``

             ``}``

        - **KinesisParameters** *(dict) --*

          The custom parameter that you can use to control the shard assignment when the target is
          a Kinesis data stream. If you don't include this parameter, the default is to use the
          ``eventId`` as the partition key.

          - **PartitionKeyPath** *(string) --*

            The JSON path to be extracted from the event and used as the partition key. For more
            information, see `Amazon Kinesis Streams Key Concepts
            <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in
            the *Amazon Kinesis Streams Developer Guide* .

        - **RunCommandParameters** *(dict) --*

          Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

          - **RunCommandTargets** *(list) --*

            Currently, we support including only one ``RunCommandTarget`` block, which specifies
            either an array of ``InstanceIds`` or a tag.

            - *(dict) --*

              Information about the EC2 instances that are to be sent the command, specified as
              key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this
              key can specify multiple values.

              - **Key** *(string) --*

                Can be either ``tag:``  *tag-key* or ``InstanceIds`` .

              - **Values** *(list) --*

                If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key``
                is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.

                - *(string) --*

        - **EcsParameters** *(dict) --*

          Contains the Amazon ECS task definition and task count to be used if the event target is
          an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in
          the *Amazon EC2 Container Service Developer Guide* .

          - **TaskDefinitionArn** *(string) --*

            The ARN of the task definition to use if the event target is an Amazon ECS task.

          - **TaskCount** *(integer) --*

            The number of tasks to create based on ``TaskDefinition`` . The default is 1.

          - **LaunchType** *(string) --*

            Specifies the launch type on which your task is running. The launch type that you
            specify here must match one of the launch type (compatibilities) of the target task.
            The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon
            ECS is supported. For more information, see `AWS Fargate on Amazon ECS
            <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in
            the *Amazon Elastic Container Service Developer Guide* .

          - **NetworkConfiguration** *(dict) --*

            Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure
            specifies the VPC subnets and security groups associated with the task and whether a
            public IP address is to be used. This structure is required if ``LaunchType`` is
            ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

            If you specify ``NetworkConfiguration`` when the target ECS task doesn't use the
            ``awsvpc`` network mode, the task fails.

            - **awsvpcConfiguration** *(dict) --*

              Use this structure to specify the VPC subnets and security groups for the task and
              whether a public IP address is to be used. This structure is relevant only for ECS
              tasks that use the ``awsvpc`` network mode.

              - **Subnets** *(list) --*

                Specifies the subnets associated with the task. These subnets must all be in the
                same VPC. You can specify as many as 16 subnets.

                - *(string) --*

              - **SecurityGroups** *(list) --*

                Specifies the security groups associated with the task. These security groups must
                all be in the same VPC. You can specify as many as five security groups. If you
                don't specify a security group, the default security group for the VPC is used.

                - *(string) --*

              - **AssignPublicIp** *(string) --*

                Specifies whether the task's elastic network interface receives a public IP
                address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters``
                is set to ``FARGATE`` .

          - **PlatformVersion** *(string) --*

            Specifies the platform version for the task. Specify only the numeric portion of the
            platform version, such as ``1.1.0`` .

            This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information
            about valid platform versions, see `AWS Fargate Platform Versions
            <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__
            in the *Amazon Elastic Container Service Developer Guide* .

          - **Group** *(string) --*

            Specifies an ECS task group for the task. The maximum length is 255 characters.

        - **BatchParameters** *(dict) --*

          If the event target is an AWS Batch job, this contains the job definition, job name, and
          other parameters. For more information, see `Jobs
          <https://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User
          Guide* .

          - **JobDefinition** *(string) --*

            The ARN or name of the job definition to use if the event target is an AWS Batch job.
            This job definition must already exist.

          - **JobName** *(string) --*

            The name to use for this execution of the job, if the target is an AWS Batch job.

          - **ArrayProperties** *(dict) --*

            The array properties for the submitted job, such as the size of the array. The array
            size can be between 2 and 10,000. If you specify array properties for a job, it becomes
            an array job. This parameter is used only if the target is an AWS Batch job.

            - **Size** *(integer) --*

              The size of the array, if this is an array batch job. Valid values are integers
              between 2 and 10,000.

          - **RetryStrategy** *(dict) --*

            The retry strategy to use for failed jobs if the target is an AWS Batch job. The retry
            strategy is the number of times to retry the failed job execution. Valid values are
            1–10. When you specify a retry strategy here, it overrides the retry strategy defined
            in the job definition.

            - **Attempts** *(integer) --*

              The number of times to attempt to retry, if the job fails. Valid values are 1–10.

        - **SqsParameters** *(dict) --*

          Contains the message group ID to use when the target is a FIFO queue.

          If you specify an SQS FIFO queue as a target, the queue must have content-based
          deduplication enabled.

          - **MessageGroupId** *(string) --*

            The FIFO message group ID to use as the target.
    """
