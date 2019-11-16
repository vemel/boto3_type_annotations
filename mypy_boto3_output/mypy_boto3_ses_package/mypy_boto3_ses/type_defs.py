"Main interface for ses type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateConfigurationSetConfigurationSetTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientCreateReceiptFilterFilterIpFilterTypeDef",
    "ClientCreateReceiptFilterFilterTypeDef",
    "ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsTypeDef",
    "ClientCreateReceiptRuleRuleTypeDef",
    "ClientCreateTemplateTemplateTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    "ClientDescribeConfigurationSetResponseConfigurationSetTypeDef",
    "ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    "ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    "ClientDescribeReceiptRuleResponseRuleTypeDef",
    "ClientDescribeReceiptRuleResponseTypeDef",
    "ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeReceiptRuleSetResponseTypeDef",
    "ClientGetAccountSendingEnabledResponseTypeDef",
    "ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    "ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    "ClientGetIdentityDkimAttributesResponseTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    "ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    "ClientGetIdentityNotificationAttributesResponseTypeDef",
    "ClientGetIdentityPoliciesResponseTypeDef",
    "ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    "ClientGetIdentityVerificationAttributesResponseTypeDef",
    "ClientGetSendQuotaResponseTypeDef",
    "ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    "ClientGetSendStatisticsResponseTypeDef",
    "ClientGetTemplateResponseTemplateTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientListConfigurationSetsResponseConfigurationSetsTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoliciesResponseTypeDef",
    "ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    "ClientListReceiptFiltersResponseFiltersTypeDef",
    "ClientListReceiptFiltersResponseTypeDef",
    "ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    "ClientListReceiptRuleSetsResponseTypeDef",
    "ClientListTemplatesResponseTemplatesMetadataTypeDef",
    "ClientListTemplatesResponseTypeDef",
    "ClientListVerifiedEmailAddressesResponseTypeDef",
    "ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListTypeDef",
    "ClientSendBounceMessageDsnExtensionFieldsTypeDef",
    "ClientSendBounceMessageDsnTypeDef",
    "ClientSendBounceResponseTypeDef",
    "ClientSendBulkTemplatedEmailDefaultTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsTypeDef",
    "ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    "ClientSendBulkTemplatedEmailResponseTypeDef",
    "ClientSendCustomVerificationEmailResponseTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailMessageBodyHtmlTypeDef",
    "ClientSendEmailMessageBodyTextTypeDef",
    "ClientSendEmailMessageBodyTypeDef",
    "ClientSendEmailMessageSubjectTypeDef",
    "ClientSendEmailMessageTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientSendEmailTagsTypeDef",
    "ClientSendRawEmailRawMessageTypeDef",
    "ClientSendRawEmailResponseTypeDef",
    "ClientSendRawEmailTagsTypeDef",
    "ClientSendTemplatedEmailDestinationTypeDef",
    "ClientSendTemplatedEmailResponseTypeDef",
    "ClientSendTemplatedEmailTagsTypeDef",
    "ClientTestRenderTemplateResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsTypeDef",
    "ClientUpdateReceiptRuleRuleTypeDef",
    "ClientUpdateTemplateTemplateTypeDef",
    "ClientVerifyDomainDkimResponseTypeDef",
    "ClientVerifyDomainIdentityResponseTypeDef",
    "IdentityExistsWaitWaiterConfigTypeDef",
    "ListConfigurationSetsPaginatePaginationConfigTypeDef",
    "ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef",
    "ListConfigurationSetsPaginateResponseTypeDef",
    "ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef",
    "ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef",
    "ListCustomVerificationEmailTemplatesPaginateResponseTypeDef",
    "ListIdentitiesPaginatePaginationConfigTypeDef",
    "ListIdentitiesPaginateResponseTypeDef",
    "ListReceiptRuleSetsPaginatePaginationConfigTypeDef",
    "ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef",
    "ListReceiptRuleSetsPaginateResponseTypeDef",
    "ListTemplatesPaginatePaginationConfigTypeDef",
    "ListTemplatesPaginateResponseTemplatesMetadataTypeDef",
    "ListTemplatesPaginateResponseTypeDef",
)


_ClientCreateConfigurationSetConfigurationSetTypeDef = TypedDict(
    "_ClientCreateConfigurationSetConfigurationSetTypeDef", {"Name": str}
)


class ClientCreateConfigurationSetConfigurationSetTypeDef(
    _ClientCreateConfigurationSetConfigurationSetTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSet` `ConfigurationSet`

    A data structure that contains the name of the configuration set.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the configuration set. The name must meet the following requirements:

      * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

      * Contain 64 characters or fewer.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {"DimensionName": str, "DimensionValueSource": str, "DefaultDimensionValue": str},
)


class ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestination` `DimensionConfigurations`

    Contains the dimension configuration to use when you publish email sending events to Amazon
    CloudWatch.

    For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
    SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **DimensionName** *(string) --* **[REQUIRED]**

      The name of an Amazon CloudWatch dimension associated with an email sending metric. The
      name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.

    - **DimensionValueSource** *(string) --* **[REQUIRED]**

      The place where Amazon SES finds the value of a dimension to publish to Amazon
      CloudWatch. If you want Amazon SES to use the message tags that you specify using an
      ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
      choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
      ``emailHeader`` .

    - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

      The default value of the dimension that is published to Amazon CloudWatch if you do not
      provide the value of the dimension when you send an email. The default value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
)


class ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `CloudWatchDestination`

    An object that contains the names, default values, and sources of the dimensions associated
    with an Amazon CloudWatch event destination.

    - **DimensionConfigurations** *(list) --* **[REQUIRED]**

      A list of dimensions upon which to categorize your emails when you publish email sending
      events to Amazon CloudWatch.

      - *(dict) --*

        Contains the dimension configuration to use when you publish email sending events to Amazon
        CloudWatch.

        For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
        SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        - **DimensionName** *(string) --* **[REQUIRED]**

          The name of an Amazon CloudWatch dimension associated with an email sending metric. The
          name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.

        - **DimensionValueSource** *(string) --* **[REQUIRED]**

          The place where Amazon SES finds the value of a dimension to publish to Amazon
          CloudWatch. If you want Amazon SES to use the message tags that you specify using an
          ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
          choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
          ``emailHeader`` .

        - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

          The default value of the dimension that is published to Amazon CloudWatch if you do not
          provide the value of the dimension when you send an email. The default value must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
)


class ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `KinesisFirehoseDestination`

    An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon
    Kinesis Firehose event destination.

    - **IAMRoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon
      Kinesis Firehose stream.

    - **DeliveryStreamARN** *(string) --* **[REQUIRED]**

      The ARN of the Amazon Kinesis Firehose stream that email sending events should be published
      to.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
)


class ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `SNSDestination`

    An object that contains the topic ARN associated with an Amazon Simple Notification Service
    (Amazon SNS) event destination.

    - **TopicARN** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS topic that email sending events will be published to. An example of
      an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
      information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {"Name": str, "MatchingEventTypes": List[str]},
)
_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestination` `EventDestination`

    An object that describes the AWS service that email sending event information will be published
    to.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the event destination. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      Sets whether Amazon SES publishes events to this destination when you send an email with the
      associated configuration set. Set to ``true`` to enable publishing to this destination; set to
      ``false`` to prevent publishing to this destination. The default value is ``false`` .

    - **MatchingEventTypes** *(list) --* **[REQUIRED]**

      The type of email sending events to publish to the event destination.

      - *(string) --*

    - **KinesisFirehoseDestination** *(dict) --*

      An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon
      Kinesis Firehose event destination.

      - **IAMRoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon
        Kinesis Firehose stream.

      - **DeliveryStreamARN** *(string) --* **[REQUIRED]**

        The ARN of the Amazon Kinesis Firehose stream that email sending events should be published
        to.

    - **CloudWatchDestination** *(dict) --*

      An object that contains the names, default values, and sources of the dimensions associated
      with an Amazon CloudWatch event destination.

      - **DimensionConfigurations** *(list) --* **[REQUIRED]**

        A list of dimensions upon which to categorize your emails when you publish email sending
        events to Amazon CloudWatch.

        - *(dict) --*

          Contains the dimension configuration to use when you publish email sending events to Amazon
          CloudWatch.

          For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
          SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

          - **DimensionName** *(string) --* **[REQUIRED]**

            The name of an Amazon CloudWatch dimension associated with an email sending metric. The
            name must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).

            * Contain less than 256 characters.

          - **DimensionValueSource** *(string) --* **[REQUIRED]**

            The place where Amazon SES finds the value of a dimension to publish to Amazon
            CloudWatch. If you want Amazon SES to use the message tags that you specify using an
            ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
            choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
            ``emailHeader`` .

          - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

            The default value of the dimension that is published to Amazon CloudWatch if you do not
            provide the value of the dimension when you send an email. The default value must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).

            * Contain less than 256 characters.

    - **SNSDestination** *(dict) --*

      An object that contains the topic ARN associated with an Amazon Simple Notification Service
      (Amazon SNS) event destination.

      - **TopicARN** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS topic that email sending events will be published to. An example of
        an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
        information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef(
    _ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetTrackingOptions` `TrackingOptions`

    A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain
    captures open and click events generated by Amazon SES emails.

    For more information, see `Configuring Custom Domains to Handle Open and Click Tracking
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__
    in the *Amazon SES Developer Guide* .

    - **CustomRedirectDomain** *(string) --*

      The custom subdomain that will be used to redirect email recipients to the Amazon SES event
      tracking domain.
    """


_ClientCreateReceiptFilterFilterIpFilterTypeDef = TypedDict(
    "_ClientCreateReceiptFilterFilterIpFilterTypeDef", {"Policy": str, "Cidr": str}
)


class ClientCreateReceiptFilterFilterIpFilterTypeDef(
    _ClientCreateReceiptFilterFilterIpFilterTypeDef
):
    """
    Type definition for `ClientCreateReceiptFilterFilter` `IpFilter`

    A structure that provides the IP addresses to block or allow, and whether to block or allow
    incoming mail from them.

    - **Policy** *(string) --* **[REQUIRED]**

      Indicates whether to block or allow incoming mail from the specified IP addresses.

    - **Cidr** *(string) --* **[REQUIRED]**

      A single IP address or a range of IP addresses that you want to block or allow, specified in
      Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is
      10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about
      CIDR notation, see `RFC 2317 <https://tools.ietf.org/html/rfc2317>`__ .
    """


_ClientCreateReceiptFilterFilterTypeDef = TypedDict(
    "_ClientCreateReceiptFilterFilterTypeDef",
    {"Name": str, "IpFilter": ClientCreateReceiptFilterFilterIpFilterTypeDef},
)


class ClientCreateReceiptFilterFilterTypeDef(_ClientCreateReceiptFilterFilterTypeDef):
    """
    Type definition for `ClientCreateReceiptFilter` `Filter`

    A data structure that describes the IP address filter to create, which consists of a name, an IP
    address range, and whether to allow or block mail from it.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the IP address filter. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **IpFilter** *(dict) --* **[REQUIRED]**

      A structure that provides the IP addresses to block or allow, and whether to block or allow
      incoming mail from them.

      - **Policy** *(string) --* **[REQUIRED]**

        Indicates whether to block or allow incoming mail from the specified IP addresses.

      - **Cidr** *(string) --* **[REQUIRED]**

        A single IP address or a range of IP addresses that you want to block or allow, specified in
        Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is
        10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about
        CIDR notation, see `RFC 2317 <https://tools.ietf.org/html/rfc2317>`__ .
    """


_ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
)


class ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `AddHeaderAction`

    Adds a header to the received email.

    - **HeaderName** *(string) --* **[REQUIRED]**

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **HeaderValue** *(string) --* **[REQUIRED]**

      Must be less than 2048 characters, and must not contain newline characters ("\\r" or
      "\\n").
    """


_RequiredClientCreateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    {"SmtpReplyCode": str, "Message": str, "Sender": str},
)
_OptionalClientCreateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "StatusCode": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsBounceActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsBounceActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsBounceActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `BounceAction`

    Rejects the received email by returning a bounce response to the sender and, optionally,
    publishes a notification to Amazon Simple Notification Service (Amazon SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
      is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **SmtpReplyCode** *(string) --* **[REQUIRED]**

      The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **StatusCode** *(string) --*

      The SMTP enhanced status code, as defined by `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ .

    - **Message** *(string) --* **[REQUIRED]**

      Human-readable text to include in the bounce message.

    - **Sender** *(string) --* **[REQUIRED]**

      The email address of the sender of the bounced email. This is the address from which the
      bounce message will be sent.
    """


_RequiredClientCreateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"FunctionArn": str},
)
_OptionalClientCreateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "InvocationType": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsLambdaActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsLambdaActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `LambdaAction`

    Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
      is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **FunctionArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
      function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
      information about AWS Lambda, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

    - **InvocationType** *(string) --*

      The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
      means that the execution of the function will immediately result in a response, and a
      value of ``Event`` means that the function will be invoked asynchronously. The default
      value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
      Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

      .. warning::

        There is a 30-second timeout on ``RequestResponse`` invocations. You should use
        ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
        a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
    """


_RequiredClientCreateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsS3ActionTypeDef", {"BucketName": str}
)
_OptionalClientCreateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsS3ActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsS3ActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsS3ActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `S3Action`

    Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
    optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
      bucket. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **BucketName** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket that incoming email will be saved to.

    - **ObjectKeyPrefix** *(string) --*

      The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
      that enables you to store similar data under the same directory in a bucket.

    - **KmsKeyArn** *(string) --*

      The customer master key that Amazon SES should use to encrypt your emails before saving
      them to the Amazon S3 bucket. You can use the default master key or a custom master key
      you created in AWS KMS as follows:

      * To use the default master key, provide an ARN in the form of
      ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
      AWS account ID is 123456789012 and you want to use the default master key in the US West
      (Oregon) region, the ARN of the default master key would be
      ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
      you don't need to perform any extra steps to give Amazon SES permission to use the key.

      * To use a custom master key you created in AWS KMS, provide the ARN of the master key
      and ensure that you add a statement to your key's policy to give Amazon SES permission to
      use it. For more information about giving permissions, see the `Amazon SES Developer
      Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
      .

      For more information about key policies, see the `AWS KMS Developer Guide
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
      specify a master key, Amazon SES will not encrypt your emails.

      .. warning::

        Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
        mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
        server-side encryption. This means that you must use the Amazon S3 encryption client to
        decrypt the email after retrieving it from Amazon S3, as the service has no access to
        use your AWS KMS keys for decryption. This encryption client is currently available
        with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
        Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
        client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .
    """


_RequiredClientCreateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsSNSActionTypeDef", {"TopicArn": str}
)
_OptionalClientCreateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    {"Encoding": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsSNSActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsSNSActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsSNSActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `SNSAction`

    Publishes the email content within a notification to Amazon SNS.

    - **TopicArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
      SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
      about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **Encoding** *(string) --*

      The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
      use, but may not preserve all special characters when a message was encoded with a
      different encoding format. Base64 preserves all special characters. The default value is
      UTF-8.
    """


_RequiredClientCreateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsStopActionTypeDef", {"Scope": str}
)
_OptionalClientCreateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsStopActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsStopActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsStopActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `StopAction`

    Terminates the evaluation of the receipt rule set and optionally publishes a notification
    to Amazon SNS.

    - **Scope** *(string) --* **[REQUIRED]**

      The scope of the StopAction. The only acceptable value is ``RuleSet`` .

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
      taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_RequiredClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"OrganizationArn": str},
)
_OptionalClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef(
    _RequiredClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef,
    _OptionalClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRuleRuleActions` `WorkmailAction`

    Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
      is called. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **OrganizationArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
      organization ARN is
      ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
      . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
      Administrator Guide
      <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .
    """


_ClientCreateReceiptRuleRuleActionsTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientCreateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientCreateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientCreateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientCreateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientCreateReceiptRuleRuleActionsTypeDef(
    _ClientCreateReceiptRuleRuleActionsTypeDef
):
    """
    Type definition for `ClientCreateReceiptRuleRule` `Actions`

    An action that Amazon SES can take when it receives an email on behalf of one or more email
    addresses or domains that you own. An instance of this data type can represent only one
    action.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **S3Action** *(dict) --*

      Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
      optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
        bucket. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **BucketName** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket that incoming email will be saved to.

      - **ObjectKeyPrefix** *(string) --*

        The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
        that enables you to store similar data under the same directory in a bucket.

      - **KmsKeyArn** *(string) --*

        The customer master key that Amazon SES should use to encrypt your emails before saving
        them to the Amazon S3 bucket. You can use the default master key or a custom master key
        you created in AWS KMS as follows:

        * To use the default master key, provide an ARN in the form of
        ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
        AWS account ID is 123456789012 and you want to use the default master key in the US West
        (Oregon) region, the ARN of the default master key would be
        ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
        you don't need to perform any extra steps to give Amazon SES permission to use the key.

        * To use a custom master key you created in AWS KMS, provide the ARN of the master key
        and ensure that you add a statement to your key's policy to give Amazon SES permission to
        use it. For more information about giving permissions, see the `Amazon SES Developer
        Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
        .

        For more information about key policies, see the `AWS KMS Developer Guide
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
        specify a master key, Amazon SES will not encrypt your emails.

        .. warning::

          Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
          mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
          server-side encryption. This means that you must use the Amazon S3 encryption client to
          decrypt the email after retrieving it from Amazon S3, as the service has no access to
          use your AWS KMS keys for decryption. This encryption client is currently available
          with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
          Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
          client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

    - **BounceAction** *(dict) --*

      Rejects the received email by returning a bounce response to the sender and, optionally,
      publishes a notification to Amazon Simple Notification Service (Amazon SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
        is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **SmtpReplyCode** *(string) --* **[REQUIRED]**

        The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

      - **StatusCode** *(string) --*

        The SMTP enhanced status code, as defined by `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ .

      - **Message** *(string) --* **[REQUIRED]**

        Human-readable text to include in the bounce message.

      - **Sender** *(string) --* **[REQUIRED]**

        The email address of the sender of the bounced email. This is the address from which the
        bounce message will be sent.

    - **WorkmailAction** *(dict) --*

      Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
        is called. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **OrganizationArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
        organization ARN is
        ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
        . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
        Administrator Guide
        <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

    - **LambdaAction** *(dict) --*

      Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
        is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **FunctionArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
        function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
        information about AWS Lambda, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

      - **InvocationType** *(string) --*

        The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
        means that the execution of the function will immediately result in a response, and a
        value of ``Event`` means that the function will be invoked asynchronously. The default
        value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
        Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

        .. warning::

          There is a 30-second timeout on ``RequestResponse`` invocations. You should use
          ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
          a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

    - **StopAction** *(dict) --*

      Terminates the evaluation of the receipt rule set and optionally publishes a notification
      to Amazon SNS.

      - **Scope** *(string) --* **[REQUIRED]**

        The scope of the StopAction. The only acceptable value is ``RuleSet`` .

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
        taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **AddHeaderAction** *(dict) --*

      Adds a header to the received email.

      - **HeaderName** *(string) --* **[REQUIRED]**

        The name of the header to add. Must be between 1 and 50 characters, inclusive, and
        consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

      - **HeaderValue** *(string) --* **[REQUIRED]**

        Must be less than 2048 characters, and must not contain newline characters ("\\r" or
        "\\n").

    - **SNSAction** *(dict) --*

      Publishes the email content within a notification to Amazon SNS.

      - **TopicArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
        SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
        about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **Encoding** *(string) --*

        The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
        use, but may not preserve all special characters when a message was encoded with a
        different encoding format. Base64 preserves all special characters. The default value is
        UTF-8.
    """


_RequiredClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": str,
        "Recipients": List[str],
        "Actions": List[ClientCreateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientCreateReceiptRuleRuleTypeDef(
    _RequiredClientCreateReceiptRuleRuleTypeDef,
    _OptionalClientCreateReceiptRuleRuleTypeDef,
):
    """
    Type definition for `ClientCreateReceiptRule` `Rule`

    A data structure that contains the specified rule's name, actions, recipients, domains, enabled
    status, scan status, and TLS policy.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the receipt rule. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      If ``true`` , the receipt rule is active. The default value is ``false`` .

    - **TlsPolicy** *(string) --*

      Specifies whether Amazon SES should require that incoming email is delivered over a connection
      encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon
      SES will bounce emails that are not received over TLS. The default is ``Optional`` .

    - **Recipients** *(list) --*

      The recipient domains and email addresses that the receipt rule applies to. If this field is
      not specified, this rule will match all recipients under all verified domains.

      - *(string) --*

    - **Actions** *(list) --*

      An ordered list of actions to perform on messages that match at least one of the recipient
      email addresses or domains specified in the receipt rule.

      - *(dict) --*

        An action that Amazon SES can take when it receives an email on behalf of one or more email
        addresses or domains that you own. An instance of this data type can represent only one
        action.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **S3Action** *(dict) --*

          Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
          optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
            bucket. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **BucketName** *(string) --* **[REQUIRED]**

            The name of the Amazon S3 bucket that incoming email will be saved to.

          - **ObjectKeyPrefix** *(string) --*

            The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
            that enables you to store similar data under the same directory in a bucket.

          - **KmsKeyArn** *(string) --*

            The customer master key that Amazon SES should use to encrypt your emails before saving
            them to the Amazon S3 bucket. You can use the default master key or a custom master key
            you created in AWS KMS as follows:

            * To use the default master key, provide an ARN in the form of
            ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
            AWS account ID is 123456789012 and you want to use the default master key in the US West
            (Oregon) region, the ARN of the default master key would be
            ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
            you don't need to perform any extra steps to give Amazon SES permission to use the key.

            * To use a custom master key you created in AWS KMS, provide the ARN of the master key
            and ensure that you add a statement to your key's policy to give Amazon SES permission to
            use it. For more information about giving permissions, see the `Amazon SES Developer
            Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
            .

            For more information about key policies, see the `AWS KMS Developer Guide
            <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
            specify a master key, Amazon SES will not encrypt your emails.

            .. warning::

              Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
              mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
              server-side encryption. This means that you must use the Amazon S3 encryption client to
              decrypt the email after retrieving it from Amazon S3, as the service has no access to
              use your AWS KMS keys for decryption. This encryption client is currently available
              with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
              Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
              client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

        - **BounceAction** *(dict) --*

          Rejects the received email by returning a bounce response to the sender and, optionally,
          publishes a notification to Amazon Simple Notification Service (Amazon SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
            is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **SmtpReplyCode** *(string) --* **[REQUIRED]**

            The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

          - **StatusCode** *(string) --*

            The SMTP enhanced status code, as defined by `RFC 3463
            <https://tools.ietf.org/html/rfc3463>`__ .

          - **Message** *(string) --* **[REQUIRED]**

            Human-readable text to include in the bounce message.

          - **Sender** *(string) --* **[REQUIRED]**

            The email address of the sender of the bounced email. This is the address from which the
            bounce message will be sent.

        - **WorkmailAction** *(dict) --*

          Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
            is called. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **OrganizationArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
            organization ARN is
            ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
            . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
            Administrator Guide
            <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

        - **LambdaAction** *(dict) --*

          Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
            is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **FunctionArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
            function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
            information about AWS Lambda, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

          - **InvocationType** *(string) --*

            The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
            means that the execution of the function will immediately result in a response, and a
            value of ``Event`` means that the function will be invoked asynchronously. The default
            value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
            Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

            .. warning::

              There is a 30-second timeout on ``RequestResponse`` invocations. You should use
              ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
              a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

        - **StopAction** *(dict) --*

          Terminates the evaluation of the receipt rule set and optionally publishes a notification
          to Amazon SNS.

          - **Scope** *(string) --* **[REQUIRED]**

            The scope of the StopAction. The only acceptable value is ``RuleSet`` .

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
            taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **AddHeaderAction** *(dict) --*

          Adds a header to the received email.

          - **HeaderName** *(string) --* **[REQUIRED]**

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **HeaderValue** *(string) --* **[REQUIRED]**

            Must be less than 2048 characters, and must not contain newline characters ("\\r" or
            "\\n").

        - **SNSAction** *(dict) --*

          Publishes the email content within a notification to Amazon SNS.

          - **TopicArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
            SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
            about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **Encoding** *(string) --*

            The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
            use, but may not preserve all special characters when a message was encoded with a
            different encoding format. Base64 preserves all special characters. The default value is
            UTF-8.

    - **ScanEnabled** *(boolean) --*

      If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses.
      The default value is ``false`` .
    """


_RequiredClientCreateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientCreateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientCreateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientCreateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientCreateTemplateTemplateTypeDef(
    _RequiredClientCreateTemplateTemplateTypeDef,
    _OptionalClientCreateTemplateTemplateTypeDef,
):
    """
    Type definition for `ClientCreateTemplate` `Template`

    The content of the email, composed of a subject line, an HTML part, and a text-only part.

    - **TemplateName** *(string) --* **[REQUIRED]**

      The name of the template. You will refer to this name when you send email using the
      ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

    - **SubjectPart** *(string) --*

      The subject line of the email.

    - **TextPart** *(string) --*

      The email body that will be visible to recipients whose email clients do not display HTML.

    - **HtmlPart** *(string) --*

      The HTML body of the email.
    """


_ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponse` `Metadata`

    The metadata for the currently active receipt rule set. The metadata consists of the rule set
    name and a timestamp of when the rule set was created.

    - **Name** *(string) --*

      The name of the receipt rule set. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **CreatedTimestamp** *(datetime) --*

      The date and time the receipt rule set was created.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `AddHeaderAction`

    Adds a header to the received email.

    - **HeaderName** *(string) --*

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **HeaderValue** *(string) --*

      Must be less than 2048 characters, and must not contain newline characters ("\\r"
      or "\\n").
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {
        "TopicArn": str,
        "SmtpReplyCode": str,
        "StatusCode": str,
        "Message": str,
        "Sender": str,
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `BounceAction`

    Rejects the received email by returning a bounce response to the sender and,
    optionally, publishes a notification to Amazon Simple Notification Service (Amazon
    SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **SmtpReplyCode** *(string) --*

      The SMTP reply code, as defined by `RFC 5321
      <https://tools.ietf.org/html/rfc5321>`__ .

    - **StatusCode** *(string) --*

      The SMTP enhanced status code, as defined by `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ .

    - **Message** *(string) --*

      Human-readable text to include in the bounce message.

    - **Sender** *(string) --*

      The email address of the sender of the bounced email. This is the address from
      which the bounce message will be sent.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `LambdaAction`

    Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **FunctionArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
      Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
      . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

    - **InvocationType** *(string) --*

      The invocation type of the AWS Lambda function. An invocation type of
      ``RequestResponse`` means that the execution of the function will immediately
      result in a response, and a value of ``Event`` means that the function will be
      invoked asynchronously. The default value is ``Event`` . For information about AWS
      Lambda invocation types, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

      .. warning::

        There is a 30-second timeout on ``RequestResponse`` invocations. You should use
        ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
        make a mail flow decision, such as whether to stop the receipt rule or the
        receipt rule set.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `S3Action`

    Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
    and, optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
      S3 bucket. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket that incoming email will be saved to.

    - **ObjectKeyPrefix** *(string) --*

      The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
      name that enables you to store similar data under the same directory in a bucket.

    - **KmsKeyArn** *(string) --*

      The customer master key that Amazon SES should use to encrypt your emails before
      saving them to the Amazon S3 bucket. You can use the default master key or a custom
      master key you created in AWS KMS as follows:

      * To use the default master key, provide an ARN in the form of
      ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
      your AWS account ID is 123456789012 and you want to use the default master key in
      the US West (Oregon) region, the ARN of the default master key would be
      ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
      master key, you don't need to perform any extra steps to give Amazon SES permission
      to use the key.

      * To use a custom master key you created in AWS KMS, provide the ARN of the master
      key and ensure that you add a statement to your key's policy to give Amazon SES
      permission to use it. For more information about giving permissions, see the
      `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
      .

      For more information about key policies, see the `AWS KMS Developer Guide
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
      do not specify a master key, Amazon SES will not encrypt your emails.

      .. warning::

        Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
        the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
        S3 server-side encryption. This means that you must use the Amazon S3 encryption
        client to decrypt the email after retrieving it from Amazon S3, as the service
        has no access to use your AWS KMS keys for decryption. This encryption client is
        currently available with the `AWS SDK for Java
        <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
        <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
        client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
        Guide
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
        .
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `SNSAction`

    Publishes the email content within a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
      Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
      information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **Encoding** *(string) --*

      The encoding to use for the email within the Amazon SNS notification. UTF-8 is
      easier to use, but may not preserve all special characters when a message was
      encoded with a different encoding format. Base64 preserves all special characters.
      The default value is UTF-8.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `StopAction`

    Terminates the evaluation of the receipt rule set and optionally publishes a
    notification to Amazon SNS.

    - **Scope** *(string) --*

      The scope of the StopAction. The only acceptable value is ``RuleSet`` .

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRulesActions` `WorkmailAction`

    Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
      action is called. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **OrganizationArn** *(string) --*

      The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
      organization ARN is
      ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
      . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
      Administrator Guide
      <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
      .
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponseRules` `Actions`

    An action that Amazon SES can take when it receives an email on behalf of one or more
    email addresses or domains that you own. An instance of this data type can represent
    only one action.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **S3Action** *(dict) --*

      Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
      and, optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
        S3 bucket. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket that incoming email will be saved to.

      - **ObjectKeyPrefix** *(string) --*

        The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
        name that enables you to store similar data under the same directory in a bucket.

      - **KmsKeyArn** *(string) --*

        The customer master key that Amazon SES should use to encrypt your emails before
        saving them to the Amazon S3 bucket. You can use the default master key or a custom
        master key you created in AWS KMS as follows:

        * To use the default master key, provide an ARN in the form of
        ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
        your AWS account ID is 123456789012 and you want to use the default master key in
        the US West (Oregon) region, the ARN of the default master key would be
        ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
        master key, you don't need to perform any extra steps to give Amazon SES permission
        to use the key.

        * To use a custom master key you created in AWS KMS, provide the ARN of the master
        key and ensure that you add a statement to your key's policy to give Amazon SES
        permission to use it. For more information about giving permissions, see the
        `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
        .

        For more information about key policies, see the `AWS KMS Developer Guide
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
        do not specify a master key, Amazon SES will not encrypt your emails.

        .. warning::

          Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
          the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
          S3 server-side encryption. This means that you must use the Amazon S3 encryption
          client to decrypt the email after retrieving it from Amazon S3, as the service
          has no access to use your AWS KMS keys for decryption. This encryption client is
          currently available with the `AWS SDK for Java
          <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
          <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
          client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
          Guide
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
          .

    - **BounceAction** *(dict) --*

      Rejects the received email by returning a bounce response to the sender and,
      optionally, publishes a notification to Amazon Simple Notification Service (Amazon
      SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **SmtpReplyCode** *(string) --*

        The SMTP reply code, as defined by `RFC 5321
        <https://tools.ietf.org/html/rfc5321>`__ .

      - **StatusCode** *(string) --*

        The SMTP enhanced status code, as defined by `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ .

      - **Message** *(string) --*

        Human-readable text to include in the bounce message.

      - **Sender** *(string) --*

        The email address of the sender of the bounced email. This is the address from
        which the bounce message will be sent.

    - **WorkmailAction** *(dict) --*

      Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
        action is called. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **OrganizationArn** *(string) --*

        The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
        organization ARN is
        ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
        . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
        Administrator Guide
        <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
        .

    - **LambdaAction** *(dict) --*

      Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
        Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
        . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

      - **InvocationType** *(string) --*

        The invocation type of the AWS Lambda function. An invocation type of
        ``RequestResponse`` means that the execution of the function will immediately
        result in a response, and a value of ``Event`` means that the function will be
        invoked asynchronously. The default value is ``Event`` . For information about AWS
        Lambda invocation types, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

        .. warning::

          There is a 30-second timeout on ``RequestResponse`` invocations. You should use
          ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
          make a mail flow decision, such as whether to stop the receipt rule or the
          receipt rule set.

    - **StopAction** *(dict) --*

      Terminates the evaluation of the receipt rule set and optionally publishes a
      notification to Amazon SNS.

      - **Scope** *(string) --*

        The scope of the StopAction. The only acceptable value is ``RuleSet`` .

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **AddHeaderAction** *(dict) --*

      Adds a header to the received email.

      - **HeaderName** *(string) --*

        The name of the header to add. Must be between 1 and 50 characters, inclusive, and
        consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

      - **HeaderValue** *(string) --*

        Must be less than 2048 characters, and must not contain newline characters ("\\r"
        or "\\n").

    - **SNSAction** *(dict) --*

      Publishes the email content within a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
        Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
        information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **Encoding** *(string) --*

        The encoding to use for the email within the Amazon SNS notification. UTF-8 is
        easier to use, but may not preserve all special characters when a message was
        encoded with a different encoding format. Base64 preserves all special characters.
        The default value is UTF-8.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": str,
        "Recipients": List[str],
        "Actions": List[ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSetResponse` `Rules`

    Receipt rules enable you to specify which actions Amazon SES should take when it receives
    mail on behalf of one or more email addresses or domains that you own.

    Each receipt rule defines a set of email addresses or domains that it applies to. If the
    email addresses or domains match at least one recipient address of the message, Amazon SES
    executes all of the receipt rule's actions on the message.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **Name** *(string) --*

      The name of the receipt rule. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      If ``true`` , the receipt rule is active. The default value is ``false`` .

    - **TlsPolicy** *(string) --*

      Specifies whether Amazon SES should require that incoming email is delivered over a
      connection encrypted with Transport Layer Security (TLS). If this parameter is set to
      ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default
      is ``Optional`` .

    - **Recipients** *(list) --*

      The recipient domains and email addresses that the receipt rule applies to. If this field
      is not specified, this rule will match all recipients under all verified domains.

      - *(string) --*

    - **Actions** *(list) --*

      An ordered list of actions to perform on messages that match at least one of the
      recipient email addresses or domains specified in the receipt rule.

      - *(dict) --*

        An action that Amazon SES can take when it receives an email on behalf of one or more
        email addresses or domains that you own. An instance of this data type can represent
        only one action.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **S3Action** *(dict) --*

          Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
          and, optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
            S3 bucket. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **BucketName** *(string) --*

            The name of the Amazon S3 bucket that incoming email will be saved to.

          - **ObjectKeyPrefix** *(string) --*

            The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
            name that enables you to store similar data under the same directory in a bucket.

          - **KmsKeyArn** *(string) --*

            The customer master key that Amazon SES should use to encrypt your emails before
            saving them to the Amazon S3 bucket. You can use the default master key or a custom
            master key you created in AWS KMS as follows:

            * To use the default master key, provide an ARN in the form of
            ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
            your AWS account ID is 123456789012 and you want to use the default master key in
            the US West (Oregon) region, the ARN of the default master key would be
            ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
            master key, you don't need to perform any extra steps to give Amazon SES permission
            to use the key.

            * To use a custom master key you created in AWS KMS, provide the ARN of the master
            key and ensure that you add a statement to your key's policy to give Amazon SES
            permission to use it. For more information about giving permissions, see the
            `Amazon SES Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
            .

            For more information about key policies, see the `AWS KMS Developer Guide
            <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
            do not specify a master key, Amazon SES will not encrypt your emails.

            .. warning::

              Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
              the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
              S3 server-side encryption. This means that you must use the Amazon S3 encryption
              client to decrypt the email after retrieving it from Amazon S3, as the service
              has no access to use your AWS KMS keys for decryption. This encryption client is
              currently available with the `AWS SDK for Java
              <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
              <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
              client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
              Guide
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
              .

        - **BounceAction** *(dict) --*

          Rejects the received email by returning a bounce response to the sender and,
          optionally, publishes a notification to Amazon Simple Notification Service (Amazon
          SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **SmtpReplyCode** *(string) --*

            The SMTP reply code, as defined by `RFC 5321
            <https://tools.ietf.org/html/rfc5321>`__ .

          - **StatusCode** *(string) --*

            The SMTP enhanced status code, as defined by `RFC 3463
            <https://tools.ietf.org/html/rfc3463>`__ .

          - **Message** *(string) --*

            Human-readable text to include in the bounce message.

          - **Sender** *(string) --*

            The email address of the sender of the bounced email. This is the address from
            which the bounce message will be sent.

        - **WorkmailAction** *(dict) --*

          Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
            action is called. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **OrganizationArn** *(string) --*

            The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
            organization ARN is
            ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
            . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
            Administrator Guide
            <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
            .

        - **LambdaAction** *(dict) --*

          Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **FunctionArn** *(string) --*

            The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
            Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
            . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

          - **InvocationType** *(string) --*

            The invocation type of the AWS Lambda function. An invocation type of
            ``RequestResponse`` means that the execution of the function will immediately
            result in a response, and a value of ``Event`` means that the function will be
            invoked asynchronously. The default value is ``Event`` . For information about AWS
            Lambda invocation types, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

            .. warning::

              There is a 30-second timeout on ``RequestResponse`` invocations. You should use
              ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
              make a mail flow decision, such as whether to stop the receipt rule or the
              receipt rule set.

        - **StopAction** *(dict) --*

          Terminates the evaluation of the receipt rule set and optionally publishes a
          notification to Amazon SNS.

          - **Scope** *(string) --*

            The scope of the StopAction. The only acceptable value is ``RuleSet`` .

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **AddHeaderAction** *(dict) --*

          Adds a header to the received email.

          - **HeaderName** *(string) --*

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **HeaderValue** *(string) --*

            Must be less than 2048 characters, and must not contain newline characters ("\\r"
            or "\\n").

        - **SNSAction** *(dict) --*

          Publishes the email content within a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
            Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
            information about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **Encoding** *(string) --*

            The encoding to use for the email within the Amazon SNS notification. UTF-8 is
            easier to use, but may not preserve all special characters when a message was
            encoded with a different encoding format. Base64 preserves all special characters.
            The default value is UTF-8.

    - **ScanEnabled** *(boolean) --*

      If ``true`` , then messages that this receipt rule applies to are scanned for spam and
      viruses. The default value is ``false`` .
    """


_ClientDescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseTypeDef
):
    """
    Type definition for `ClientDescribeActiveReceiptRuleSet` `Response`

    Represents the metadata and receipt rules for the receipt rule set that is currently active.

    - **Metadata** *(dict) --*

      The metadata for the currently active receipt rule set. The metadata consists of the rule set
      name and a timestamp of when the rule set was created.

      - **Name** *(string) --*

        The name of the receipt rule set. The name must:

        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).

        * Start and end with a letter or number.

        * Contain less than 64 characters.

      - **CreatedTimestamp** *(datetime) --*

        The date and time the receipt rule set was created.

    - **Rules** *(list) --*

      The receipt rules that belong to the active rule set.

      - *(dict) --*

        Receipt rules enable you to specify which actions Amazon SES should take when it receives
        mail on behalf of one or more email addresses or domains that you own.

        Each receipt rule defines a set of email addresses or domains that it applies to. If the
        email addresses or domains match at least one recipient address of the message, Amazon SES
        executes all of the receipt rule's actions on the message.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **Name** *(string) --*

          The name of the receipt rule. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Start and end with a letter or number.

          * Contain less than 64 characters.

        - **Enabled** *(boolean) --*

          If ``true`` , the receipt rule is active. The default value is ``false`` .

        - **TlsPolicy** *(string) --*

          Specifies whether Amazon SES should require that incoming email is delivered over a
          connection encrypted with Transport Layer Security (TLS). If this parameter is set to
          ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default
          is ``Optional`` .

        - **Recipients** *(list) --*

          The recipient domains and email addresses that the receipt rule applies to. If this field
          is not specified, this rule will match all recipients under all verified domains.

          - *(string) --*

        - **Actions** *(list) --*

          An ordered list of actions to perform on messages that match at least one of the
          recipient email addresses or domains specified in the receipt rule.

          - *(dict) --*

            An action that Amazon SES can take when it receives an email on behalf of one or more
            email addresses or domains that you own. An instance of this data type can represent
            only one action.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
            .

            - **S3Action** *(dict) --*

              Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
              and, optionally, publishes a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
                S3 bucket. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **BucketName** *(string) --*

                The name of the Amazon S3 bucket that incoming email will be saved to.

              - **ObjectKeyPrefix** *(string) --*

                The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
                name that enables you to store similar data under the same directory in a bucket.

              - **KmsKeyArn** *(string) --*

                The customer master key that Amazon SES should use to encrypt your emails before
                saving them to the Amazon S3 bucket. You can use the default master key or a custom
                master key you created in AWS KMS as follows:

                * To use the default master key, provide an ARN in the form of
                ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
                your AWS account ID is 123456789012 and you want to use the default master key in
                the US West (Oregon) region, the ARN of the default master key would be
                ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
                master key, you don't need to perform any extra steps to give Amazon SES permission
                to use the key.

                * To use a custom master key you created in AWS KMS, provide the ARN of the master
                key and ensure that you add a statement to your key's policy to give Amazon SES
                permission to use it. For more information about giving permissions, see the
                `Amazon SES Developer Guide
                <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
                .

                For more information about key policies, see the `AWS KMS Developer Guide
                <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
                do not specify a master key, Amazon SES will not encrypt your emails.

                .. warning::

                  Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
                  the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
                  S3 server-side encryption. This means that you must use the Amazon S3 encryption
                  client to decrypt the email after retrieving it from Amazon S3, as the service
                  has no access to use your AWS KMS keys for decryption. This encryption client is
                  currently available with the `AWS SDK for Java
                  <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
                  <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
                  client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
                  Guide
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
                  .

            - **BounceAction** *(dict) --*

              Rejects the received email by returning a bounce response to the sender and,
              optionally, publishes a notification to Amazon Simple Notification Service (Amazon
              SNS).

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **SmtpReplyCode** *(string) --*

                The SMTP reply code, as defined by `RFC 5321
                <https://tools.ietf.org/html/rfc5321>`__ .

              - **StatusCode** *(string) --*

                The SMTP enhanced status code, as defined by `RFC 3463
                <https://tools.ietf.org/html/rfc3463>`__ .

              - **Message** *(string) --*

                Human-readable text to include in the bounce message.

              - **Sender** *(string) --*

                The email address of the sender of the bounced email. This is the address from
                which the bounce message will be sent.

            - **WorkmailAction** *(dict) --*

              Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
                action is called. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **OrganizationArn** *(string) --*

                The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
                organization ARN is
                ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
                . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
                Administrator Guide
                <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
                .

            - **LambdaAction** *(dict) --*

              Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **FunctionArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
                Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
                . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
                <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

              - **InvocationType** *(string) --*

                The invocation type of the AWS Lambda function. An invocation type of
                ``RequestResponse`` means that the execution of the function will immediately
                result in a response, and a value of ``Event`` means that the function will be
                invoked asynchronously. The default value is ``Event`` . For information about AWS
                Lambda invocation types, see the `AWS Lambda Developer Guide
                <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

                .. warning::

                  There is a 30-second timeout on ``RequestResponse`` invocations. You should use
                  ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
                  make a mail flow decision, such as whether to stop the receipt rule or the
                  receipt rule set.

            - **StopAction** *(dict) --*

              Terminates the evaluation of the receipt rule set and optionally publishes a
              notification to Amazon SNS.

              - **Scope** *(string) --*

                The scope of the StopAction. The only acceptable value is ``RuleSet`` .

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **AddHeaderAction** *(dict) --*

              Adds a header to the received email.

              - **HeaderName** *(string) --*

                The name of the header to add. Must be between 1 and 50 characters, inclusive, and
                consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

              - **HeaderValue** *(string) --*

                Must be less than 2048 characters, and must not contain newline characters ("\\r"
                or "\\n").

            - **SNSAction** *(dict) --*

              Publishes the email content within a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
                Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
                information about Amazon SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **Encoding** *(string) --*

                The encoding to use for the email within the Amazon SNS notification. UTF-8 is
                easier to use, but may not preserve all special characters when a message was
                encoded with a different encoding format. Base64 preserves all special characters.
                The default value is UTF-8.

        - **ScanEnabled** *(boolean) --*

          If ``true`` , then messages that this receipt rule applies to are scanned for spam and
          viruses. The default value is ``false`` .
    """


_ClientDescribeConfigurationSetResponseConfigurationSetTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseConfigurationSetTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseConfigurationSetTypeDef(
    _ClientDescribeConfigurationSetResponseConfigurationSetTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponse` `ConfigurationSet`

    The configuration set object associated with the specified configuration set.

    - **Name** *(string) --*

      The name of the configuration set. The name must meet the following requirements:

      * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

      * Contain 64 characters or fewer.
    """


_ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponse` `DeliveryOptions`

    Specifies whether messages that use the configuration set are required to use Transport Layer
    Security (TLS).

    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport
      Layer Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS
      connection can be established. If the value is ``Optional`` , messages can be delivered in
      plain text if a TLS connection can't be established.
    """


_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {"DimensionName": str, "DimensionValueSource": str, "DefaultDimensionValue": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestination` `DimensionConfigurations`

    Contains the dimension configuration to use when you publish email sending events to
    Amazon CloudWatch.

    For information about publishing email sending events to Amazon CloudWatch, see the
    `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__
    .

    - **DimensionName** *(string) --*

      The name of an Amazon CloudWatch dimension associated with an email sending metric.
      The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
      (_), or dashes (-).

      * Contain less than 256 characters.

    - **DimensionValueSource** *(string) --*

      The place where Amazon SES finds the value of a dimension to publish to Amazon
      CloudWatch. If you want Amazon SES to use the message tags that you specify using
      an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail``
      /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your
      own email headers, choose ``emailHeader`` .

    - **DefaultDimensionValue** *(string) --*

      The default value of the dimension that is published to Amazon CloudWatch if you do
      not provide the value of the dimension when you send an email. The default value
      must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
      (_), or dashes (-).

      * Contain less than 256 characters.
    """


_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponseEventDestinations` `CloudWatchDestination`

    An object that contains the names, default values, and sources of the dimensions
    associated with an Amazon CloudWatch event destination.

    - **DimensionConfigurations** *(list) --*

      A list of dimensions upon which to categorize your emails when you publish email
      sending events to Amazon CloudWatch.

      - *(dict) --*

        Contains the dimension configuration to use when you publish email sending events to
        Amazon CloudWatch.

        For information about publishing email sending events to Amazon CloudWatch, see the
        `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__
        .

        - **DimensionName** *(string) --*

          The name of an Amazon CloudWatch dimension associated with an email sending metric.
          The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
          (_), or dashes (-).

          * Contain less than 256 characters.

        - **DimensionValueSource** *(string) --*

          The place where Amazon SES finds the value of a dimension to publish to Amazon
          CloudWatch. If you want Amazon SES to use the message tags that you specify using
          an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail``
          /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your
          own email headers, choose ``emailHeader`` .

        - **DefaultDimensionValue** *(string) --*

          The default value of the dimension that is published to Amazon CloudWatch if you do
          not provide the value of the dimension when you send an email. The default value
          must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
          (_), or dashes (-).

          * Contain less than 256 characters.
    """


_ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponseEventDestinations` `KinesisFirehoseDestination`

    An object that contains the delivery stream ARN and the IAM role ARN associated with an
    Amazon Kinesis Firehose event destination.

    - **IAMRoleARN** *(string) --*

      The ARN of the IAM role under which Amazon SES publishes email sending events to the
      Amazon Kinesis Firehose stream.

    - **DeliveryStreamARN** *(string) --*

      The ARN of the Amazon Kinesis Firehose stream that email sending events should be
      published to.
    """


_ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponseEventDestinations` `SNSDestination`

    An object that contains the topic ARN associated with an Amazon Simple Notification
    Service (Amazon SNS) event destination.

    - **TopicARN** *(string) --*

      The ARN of the Amazon SNS topic that email sending events will be published to. An
      example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` .
      For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientDescribeConfigurationSetResponseEventDestinationsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[str],
        "KinesisFirehoseDestination": ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SNSDestination": ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponse` `EventDestinations`

    Contains information about the event destination that the specified email sending events
    will be published to.

    .. note::

      When you create or update an event destination, you must provide one, and only one,
      destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon
      Simple Notification Service (Amazon SNS).

    Event destinations are associated with configuration sets, which enable you to publish
    email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple
    Notification Service (Amazon SNS). For information about using configuration sets, see the
    `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --*

      The name of the event destination. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      Sets whether Amazon SES publishes events to this destination when you send an email with
      the associated configuration set. Set to ``true`` to enable publishing to this
      destination; set to ``false`` to prevent publishing to this destination. The default
      value is ``false`` .

    - **MatchingEventTypes** *(list) --*

      The type of email sending events to publish to the event destination.

      - *(string) --*

    - **KinesisFirehoseDestination** *(dict) --*

      An object that contains the delivery stream ARN and the IAM role ARN associated with an
      Amazon Kinesis Firehose event destination.

      - **IAMRoleARN** *(string) --*

        The ARN of the IAM role under which Amazon SES publishes email sending events to the
        Amazon Kinesis Firehose stream.

      - **DeliveryStreamARN** *(string) --*

        The ARN of the Amazon Kinesis Firehose stream that email sending events should be
        published to.

    - **CloudWatchDestination** *(dict) --*

      An object that contains the names, default values, and sources of the dimensions
      associated with an Amazon CloudWatch event destination.

      - **DimensionConfigurations** *(list) --*

        A list of dimensions upon which to categorize your emails when you publish email
        sending events to Amazon CloudWatch.

        - *(dict) --*

          Contains the dimension configuration to use when you publish email sending events to
          Amazon CloudWatch.

          For information about publishing email sending events to Amazon CloudWatch, see the
          `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__
          .

          - **DimensionName** *(string) --*

            The name of an Amazon CloudWatch dimension associated with an email sending metric.
            The name must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
            (_), or dashes (-).

            * Contain less than 256 characters.

          - **DimensionValueSource** *(string) --*

            The place where Amazon SES finds the value of a dimension to publish to Amazon
            CloudWatch. If you want Amazon SES to use the message tags that you specify using
            an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail``
            /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your
            own email headers, choose ``emailHeader`` .

          - **DefaultDimensionValue** *(string) --*

            The default value of the dimension that is published to Amazon CloudWatch if you do
            not provide the value of the dimension when you send an email. The default value
            must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
            (_), or dashes (-).

            * Contain less than 256 characters.

    - **SNSDestination** *(dict) --*

      An object that contains the topic ARN associated with an Amazon Simple Notification
      Service (Amazon SNS) event destination.

      - **TopicARN** *(string) --*

        The ARN of the Amazon SNS topic that email sending events will be published to. An
        example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` .
        For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientDescribeConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    {
        "SendingEnabled": bool,
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": datetime,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseReputationOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseReputationOptionsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponse` `ReputationOptions`

    An object that represents the reputation settings for the configuration set.

    - **SendingEnabled** *(boolean) --*

      Describes whether email sending is enabled or disabled for the configuration set. If the
      value is ``true`` , then Amazon SES will send emails that use the configuration set. If the
      value is ``false`` , Amazon SES will not send emails that use the configuration set. The
      default value is ``true`` . You can change this setting using
      UpdateConfigurationSetSendingEnabled .

    - **ReputationMetricsEnabled** *(boolean) --*

      Describes whether or not Amazon SES publishes reputation metrics for the configuration set,
      such as bounce and complaint rates, to Amazon CloudWatch.

      If the value is ``true`` , reputation metrics are published. If the value is ``false`` ,
      reputation metrics are not published. The default value is ``false`` .

    - **LastFreshStart** *(datetime) --*

      The date and time at which the reputation metrics for the configuration set were last
      reset. Resetting these metrics is known as a *fresh start* .

      When you disable email sending for a configuration set using
      UpdateConfigurationSetSendingEnabled and later re-enable it, the reputation metrics for the
      configuration set (but not for the entire Amazon SES account) are reset.

      If email sending for the configuration set has never been disabled and later re-enabled,
      the value of this attribute is ``null`` .
    """


_ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSetResponse` `TrackingOptions`

    The name of the custom open and click tracking domain associated with the configuration set.

    - **CustomRedirectDomain** *(string) --*

      The custom subdomain that will be used to redirect email recipients to the Amazon SES event
      tracking domain.
    """


_ClientDescribeConfigurationSetResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": ClientDescribeConfigurationSetResponseConfigurationSetTypeDef,
        "EventDestinations": List[
            ClientDescribeConfigurationSetResponseEventDestinationsTypeDef
        ],
        "TrackingOptions": ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientDescribeConfigurationSetResponseReputationOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseTypeDef(
    _ClientDescribeConfigurationSetResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSet` `Response`

    Represents the details of a configuration set. Configuration sets enable you to publish email
    sending events. For information about using configuration sets, see the `Amazon SES Developer
    Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **ConfigurationSet** *(dict) --*

      The configuration set object associated with the specified configuration set.

      - **Name** *(string) --*

        The name of the configuration set. The name must meet the following requirements:

        * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

        * Contain 64 characters or fewer.

    - **EventDestinations** *(list) --*

      A list of event destinations associated with the configuration set.

      - *(dict) --*

        Contains information about the event destination that the specified email sending events
        will be published to.

        .. note::

          When you create or update an event destination, you must provide one, and only one,
          destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon
          Simple Notification Service (Amazon SNS).

        Event destinations are associated with configuration sets, which enable you to publish
        email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple
        Notification Service (Amazon SNS). For information about using configuration sets, see the
        `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        - **Name** *(string) --*

          The name of the event destination. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 64 characters.

        - **Enabled** *(boolean) --*

          Sets whether Amazon SES publishes events to this destination when you send an email with
          the associated configuration set. Set to ``true`` to enable publishing to this
          destination; set to ``false`` to prevent publishing to this destination. The default
          value is ``false`` .

        - **MatchingEventTypes** *(list) --*

          The type of email sending events to publish to the event destination.

          - *(string) --*

        - **KinesisFirehoseDestination** *(dict) --*

          An object that contains the delivery stream ARN and the IAM role ARN associated with an
          Amazon Kinesis Firehose event destination.

          - **IAMRoleARN** *(string) --*

            The ARN of the IAM role under which Amazon SES publishes email sending events to the
            Amazon Kinesis Firehose stream.

          - **DeliveryStreamARN** *(string) --*

            The ARN of the Amazon Kinesis Firehose stream that email sending events should be
            published to.

        - **CloudWatchDestination** *(dict) --*

          An object that contains the names, default values, and sources of the dimensions
          associated with an Amazon CloudWatch event destination.

          - **DimensionConfigurations** *(list) --*

            A list of dimensions upon which to categorize your emails when you publish email
            sending events to Amazon CloudWatch.

            - *(dict) --*

              Contains the dimension configuration to use when you publish email sending events to
              Amazon CloudWatch.

              For information about publishing email sending events to Amazon CloudWatch, see the
              `Amazon SES Developer Guide
              <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__
              .

              - **DimensionName** *(string) --*

                The name of an Amazon CloudWatch dimension associated with an email sending metric.
                The name must:

                * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
                (_), or dashes (-).

                * Contain less than 256 characters.

              - **DimensionValueSource** *(string) --*

                The place where Amazon SES finds the value of a dimension to publish to Amazon
                CloudWatch. If you want Amazon SES to use the message tags that you specify using
                an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail``
                /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your
                own email headers, choose ``emailHeader`` .

              - **DefaultDimensionValue** *(string) --*

                The default value of the dimension that is published to Amazon CloudWatch if you do
                not provide the value of the dimension when you send an email. The default value
                must:

                * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores
                (_), or dashes (-).

                * Contain less than 256 characters.

        - **SNSDestination** *(dict) --*

          An object that contains the topic ARN associated with an Amazon Simple Notification
          Service (Amazon SNS) event destination.

          - **TopicARN** *(string) --*

            The ARN of the Amazon SNS topic that email sending events will be published to. An
            example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` .
            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **TrackingOptions** *(dict) --*

      The name of the custom open and click tracking domain associated with the configuration set.

      - **CustomRedirectDomain** *(string) --*

        The custom subdomain that will be used to redirect email recipients to the Amazon SES event
        tracking domain.

    - **DeliveryOptions** *(dict) --*

      Specifies whether messages that use the configuration set are required to use Transport Layer
      Security (TLS).

      - **TlsPolicy** *(string) --*

        Specifies whether messages that use the configuration set are required to use Transport
        Layer Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS
        connection can be established. If the value is ``Optional`` , messages can be delivered in
        plain text if a TLS connection can't be established.

    - **ReputationOptions** *(dict) --*

      An object that represents the reputation settings for the configuration set.

      - **SendingEnabled** *(boolean) --*

        Describes whether email sending is enabled or disabled for the configuration set. If the
        value is ``true`` , then Amazon SES will send emails that use the configuration set. If the
        value is ``false`` , Amazon SES will not send emails that use the configuration set. The
        default value is ``true`` . You can change this setting using
        UpdateConfigurationSetSendingEnabled .

      - **ReputationMetricsEnabled** *(boolean) --*

        Describes whether or not Amazon SES publishes reputation metrics for the configuration set,
        such as bounce and complaint rates, to Amazon CloudWatch.

        If the value is ``true`` , reputation metrics are published. If the value is ``false`` ,
        reputation metrics are not published. The default value is ``false`` .

      - **LastFreshStart** *(datetime) --*

        The date and time at which the reputation metrics for the configuration set were last
        reset. Resetting these metrics is known as a *fresh start* .

        When you disable email sending for a configuration set using
        UpdateConfigurationSetSendingEnabled and later re-enable it, the reputation metrics for the
        configuration set (but not for the entire Amazon SES account) are reset.

        If email sending for the configuration set has never been disabled and later re-enabled,
        the value of this attribute is ``null`` .
    """


_ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `AddHeaderAction`

    Adds a header to the received email.

    - **HeaderName** *(string) --*

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **HeaderValue** *(string) --*

      Must be less than 2048 characters, and must not contain newline characters ("\\r" or
      "\\n").
    """


_ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    {
        "TopicArn": str,
        "SmtpReplyCode": str,
        "StatusCode": str,
        "Message": str,
        "Sender": str,
    },
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `BounceAction`

    Rejects the received email by returning a bounce response to the sender and,
    optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **SmtpReplyCode** *(string) --*

      The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__
      .

    - **StatusCode** *(string) --*

      The SMTP enhanced status code, as defined by `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ .

    - **Message** *(string) --*

      Human-readable text to include in the bounce message.

    - **Sender** *(string) --*

      The email address of the sender of the bounced email. This is the address from which
      the bounce message will be sent.
    """


_ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `LambdaAction`

    Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **FunctionArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
      Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` .
      For more information about AWS Lambda, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

    - **InvocationType** *(string) --*

      The invocation type of the AWS Lambda function. An invocation type of
      ``RequestResponse`` means that the execution of the function will immediately result
      in a response, and a value of ``Event`` means that the function will be invoked
      asynchronously. The default value is ``Event`` . For information about AWS Lambda
      invocation types, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

      .. warning::

        There is a 30-second timeout on ``RequestResponse`` invocations. You should use
        ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
        make a mail flow decision, such as whether to stop the receipt rule or the receipt
        rule set.
    """


_ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `S3Action`

    Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
    optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
      bucket. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket that incoming email will be saved to.

    - **ObjectKeyPrefix** *(string) --*

      The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
      that enables you to store similar data under the same directory in a bucket.

    - **KmsKeyArn** *(string) --*

      The customer master key that Amazon SES should use to encrypt your emails before
      saving them to the Amazon S3 bucket. You can use the default master key or a custom
      master key you created in AWS KMS as follows:

      * To use the default master key, provide an ARN in the form of
      ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
      your AWS account ID is 123456789012 and you want to use the default master key in the
      US West (Oregon) region, the ARN of the default master key would be
      ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master
      key, you don't need to perform any extra steps to give Amazon SES permission to use
      the key.

      * To use a custom master key you created in AWS KMS, provide the ARN of the master
      key and ensure that you add a statement to your key's policy to give Amazon SES
      permission to use it. For more information about giving permissions, see the `Amazon
      SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
      .

      For more information about key policies, see the `AWS KMS Developer Guide
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do
      not specify a master key, Amazon SES will not encrypt your emails.

      .. warning::

        Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
        the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
        server-side encryption. This means that you must use the Amazon S3 encryption
        client to decrypt the email after retrieving it from Amazon S3, as the service has
        no access to use your AWS KMS keys for decryption. This encryption client is
        currently available with the `AWS SDK for Java
        <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
        <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
        client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
        Guide
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
        .
    """


_ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `SNSAction`

    Publishes the email content within a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
      Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
      information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **Encoding** *(string) --*

      The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier
      to use, but may not preserve all special characters when a message was encoded with a
      different encoding format. Base64 preserves all special characters. The default value
      is UTF-8.
    """


_ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `StopAction`

    Terminates the evaluation of the receipt rule set and optionally publishes a
    notification to Amazon SNS.

    - **Scope** *(string) --*

      The scope of the StopAction. The only acceptable value is ``RuleSet`` .

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action
      is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRuleActions` `WorkmailAction`

    Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
      action is called. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **OrganizationArn** *(string) --*

      The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
      organization ARN is
      ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
      . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
      Administrator Guide
      <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
      .
    """


_ClientDescribeReceiptRuleResponseRuleActionsTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponseRule` `Actions`

    An action that Amazon SES can take when it receives an email on behalf of one or more
    email addresses or domains that you own. An instance of this data type can represent only
    one action.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **S3Action** *(dict) --*

      Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
      optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
        bucket. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket that incoming email will be saved to.

      - **ObjectKeyPrefix** *(string) --*

        The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
        that enables you to store similar data under the same directory in a bucket.

      - **KmsKeyArn** *(string) --*

        The customer master key that Amazon SES should use to encrypt your emails before
        saving them to the Amazon S3 bucket. You can use the default master key or a custom
        master key you created in AWS KMS as follows:

        * To use the default master key, provide an ARN in the form of
        ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
        your AWS account ID is 123456789012 and you want to use the default master key in the
        US West (Oregon) region, the ARN of the default master key would be
        ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master
        key, you don't need to perform any extra steps to give Amazon SES permission to use
        the key.

        * To use a custom master key you created in AWS KMS, provide the ARN of the master
        key and ensure that you add a statement to your key's policy to give Amazon SES
        permission to use it. For more information about giving permissions, see the `Amazon
        SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
        .

        For more information about key policies, see the `AWS KMS Developer Guide
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do
        not specify a master key, Amazon SES will not encrypt your emails.

        .. warning::

          Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
          the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
          server-side encryption. This means that you must use the Amazon S3 encryption
          client to decrypt the email after retrieving it from Amazon S3, as the service has
          no access to use your AWS KMS keys for decryption. This encryption client is
          currently available with the `AWS SDK for Java
          <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
          <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
          client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
          Guide
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
          .

    - **BounceAction** *(dict) --*

      Rejects the received email by returning a bounce response to the sender and,
      optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **SmtpReplyCode** *(string) --*

        The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__
        .

      - **StatusCode** *(string) --*

        The SMTP enhanced status code, as defined by `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ .

      - **Message** *(string) --*

        Human-readable text to include in the bounce message.

      - **Sender** *(string) --*

        The email address of the sender of the bounced email. This is the address from which
        the bounce message will be sent.

    - **WorkmailAction** *(dict) --*

      Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
        action is called. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **OrganizationArn** *(string) --*

        The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
        organization ARN is
        ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
        . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
        Administrator Guide
        <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
        .

    - **LambdaAction** *(dict) --*

      Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
        Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` .
        For more information about AWS Lambda, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

      - **InvocationType** *(string) --*

        The invocation type of the AWS Lambda function. An invocation type of
        ``RequestResponse`` means that the execution of the function will immediately result
        in a response, and a value of ``Event`` means that the function will be invoked
        asynchronously. The default value is ``Event`` . For information about AWS Lambda
        invocation types, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

        .. warning::

          There is a 30-second timeout on ``RequestResponse`` invocations. You should use
          ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
          make a mail flow decision, such as whether to stop the receipt rule or the receipt
          rule set.

    - **StopAction** *(dict) --*

      Terminates the evaluation of the receipt rule set and optionally publishes a
      notification to Amazon SNS.

      - **Scope** *(string) --*

        The scope of the StopAction. The only acceptable value is ``RuleSet`` .

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action
        is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **AddHeaderAction** *(dict) --*

      Adds a header to the received email.

      - **HeaderName** *(string) --*

        The name of the header to add. Must be between 1 and 50 characters, inclusive, and
        consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

      - **HeaderValue** *(string) --*

        Must be less than 2048 characters, and must not contain newline characters ("\\r" or
        "\\n").

    - **SNSAction** *(dict) --*

      Publishes the email content within a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
        Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
        information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **Encoding** *(string) --*

        The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier
        to use, but may not preserve all special characters when a message was encoded with a
        different encoding format. Base64 preserves all special characters. The default value
        is UTF-8.
    """


_ClientDescribeReceiptRuleResponseRuleTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": str,
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleResponseRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleTypeDef(
    _ClientDescribeReceiptRuleResponseRuleTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleResponse` `Rule`

    A data structure that contains the specified receipt rule's name, actions, recipients,
    domains, enabled status, scan status, and Transport Layer Security (TLS) policy.

    - **Name** *(string) --*

      The name of the receipt rule. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      If ``true`` , the receipt rule is active. The default value is ``false`` .

    - **TlsPolicy** *(string) --*

      Specifies whether Amazon SES should require that incoming email is delivered over a
      connection encrypted with Transport Layer Security (TLS). If this parameter is set to
      ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is
      ``Optional`` .

    - **Recipients** *(list) --*

      The recipient domains and email addresses that the receipt rule applies to. If this field
      is not specified, this rule will match all recipients under all verified domains.

      - *(string) --*

    - **Actions** *(list) --*

      An ordered list of actions to perform on messages that match at least one of the recipient
      email addresses or domains specified in the receipt rule.

      - *(dict) --*

        An action that Amazon SES can take when it receives an email on behalf of one or more
        email addresses or domains that you own. An instance of this data type can represent only
        one action.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **S3Action** *(dict) --*

          Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
          optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
            bucket. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **BucketName** *(string) --*

            The name of the Amazon S3 bucket that incoming email will be saved to.

          - **ObjectKeyPrefix** *(string) --*

            The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
            that enables you to store similar data under the same directory in a bucket.

          - **KmsKeyArn** *(string) --*

            The customer master key that Amazon SES should use to encrypt your emails before
            saving them to the Amazon S3 bucket. You can use the default master key or a custom
            master key you created in AWS KMS as follows:

            * To use the default master key, provide an ARN in the form of
            ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
            your AWS account ID is 123456789012 and you want to use the default master key in the
            US West (Oregon) region, the ARN of the default master key would be
            ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master
            key, you don't need to perform any extra steps to give Amazon SES permission to use
            the key.

            * To use a custom master key you created in AWS KMS, provide the ARN of the master
            key and ensure that you add a statement to your key's policy to give Amazon SES
            permission to use it. For more information about giving permissions, see the `Amazon
            SES Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
            .

            For more information about key policies, see the `AWS KMS Developer Guide
            <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do
            not specify a master key, Amazon SES will not encrypt your emails.

            .. warning::

              Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
              the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
              server-side encryption. This means that you must use the Amazon S3 encryption
              client to decrypt the email after retrieving it from Amazon S3, as the service has
              no access to use your AWS KMS keys for decryption. This encryption client is
              currently available with the `AWS SDK for Java
              <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
              <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
              client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
              Guide
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
              .

        - **BounceAction** *(dict) --*

          Rejects the received email by returning a bounce response to the sender and,
          optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **SmtpReplyCode** *(string) --*

            The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__
            .

          - **StatusCode** *(string) --*

            The SMTP enhanced status code, as defined by `RFC 3463
            <https://tools.ietf.org/html/rfc3463>`__ .

          - **Message** *(string) --*

            Human-readable text to include in the bounce message.

          - **Sender** *(string) --*

            The email address of the sender of the bounced email. This is the address from which
            the bounce message will be sent.

        - **WorkmailAction** *(dict) --*

          Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
            action is called. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **OrganizationArn** *(string) --*

            The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
            organization ARN is
            ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
            . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
            Administrator Guide
            <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
            .

        - **LambdaAction** *(dict) --*

          Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **FunctionArn** *(string) --*

            The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
            Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` .
            For more information about AWS Lambda, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

          - **InvocationType** *(string) --*

            The invocation type of the AWS Lambda function. An invocation type of
            ``RequestResponse`` means that the execution of the function will immediately result
            in a response, and a value of ``Event`` means that the function will be invoked
            asynchronously. The default value is ``Event`` . For information about AWS Lambda
            invocation types, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

            .. warning::

              There is a 30-second timeout on ``RequestResponse`` invocations. You should use
              ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
              make a mail flow decision, such as whether to stop the receipt rule or the receipt
              rule set.

        - **StopAction** *(dict) --*

          Terminates the evaluation of the receipt rule set and optionally publishes a
          notification to Amazon SNS.

          - **Scope** *(string) --*

            The scope of the StopAction. The only acceptable value is ``RuleSet`` .

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action
            is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **AddHeaderAction** *(dict) --*

          Adds a header to the received email.

          - **HeaderName** *(string) --*

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **HeaderValue** *(string) --*

            Must be less than 2048 characters, and must not contain newline characters ("\\r" or
            "\\n").

        - **SNSAction** *(dict) --*

          Publishes the email content within a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
            Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
            information about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **Encoding** *(string) --*

            The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier
            to use, but may not preserve all special characters when a message was encoded with a
            different encoding format. Base64 preserves all special characters. The default value
            is UTF-8.

    - **ScanEnabled** *(boolean) --*

      If ``true`` , then messages that this receipt rule applies to are scanned for spam and
      viruses. The default value is ``false`` .
    """


_ClientDescribeReceiptRuleResponseTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseTypeDef",
    {"Rule": ClientDescribeReceiptRuleResponseRuleTypeDef},
    total=False,
)


class ClientDescribeReceiptRuleResponseTypeDef(
    _ClientDescribeReceiptRuleResponseTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRule` `Response`

    Represents the details of a receipt rule.

    - **Rule** *(dict) --*

      A data structure that contains the specified receipt rule's name, actions, recipients,
      domains, enabled status, scan status, and Transport Layer Security (TLS) policy.

      - **Name** *(string) --*

        The name of the receipt rule. The name must:

        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).

        * Start and end with a letter or number.

        * Contain less than 64 characters.

      - **Enabled** *(boolean) --*

        If ``true`` , the receipt rule is active. The default value is ``false`` .

      - **TlsPolicy** *(string) --*

        Specifies whether Amazon SES should require that incoming email is delivered over a
        connection encrypted with Transport Layer Security (TLS). If this parameter is set to
        ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is
        ``Optional`` .

      - **Recipients** *(list) --*

        The recipient domains and email addresses that the receipt rule applies to. If this field
        is not specified, this rule will match all recipients under all verified domains.

        - *(string) --*

      - **Actions** *(list) --*

        An ordered list of actions to perform on messages that match at least one of the recipient
        email addresses or domains specified in the receipt rule.

        - *(dict) --*

          An action that Amazon SES can take when it receives an email on behalf of one or more
          email addresses or domains that you own. An instance of this data type can represent only
          one action.

          For information about setting up receipt rules, see the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
          .

          - **S3Action** *(dict) --*

            Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
            optionally, publishes a notification to Amazon SNS.

            - **TopicArn** *(string) --*

              The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
              bucket. An example of an Amazon SNS topic ARN is
              ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
              SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **BucketName** *(string) --*

              The name of the Amazon S3 bucket that incoming email will be saved to.

            - **ObjectKeyPrefix** *(string) --*

              The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
              that enables you to store similar data under the same directory in a bucket.

            - **KmsKeyArn** *(string) --*

              The customer master key that Amazon SES should use to encrypt your emails before
              saving them to the Amazon S3 bucket. You can use the default master key or a custom
              master key you created in AWS KMS as follows:

              * To use the default master key, provide an ARN in the form of
              ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
              your AWS account ID is 123456789012 and you want to use the default master key in the
              US West (Oregon) region, the ARN of the default master key would be
              ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master
              key, you don't need to perform any extra steps to give Amazon SES permission to use
              the key.

              * To use a custom master key you created in AWS KMS, provide the ARN of the master
              key and ensure that you add a statement to your key's policy to give Amazon SES
              permission to use it. For more information about giving permissions, see the `Amazon
              SES Developer Guide
              <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
              .

              For more information about key policies, see the `AWS KMS Developer Guide
              <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do
              not specify a master key, Amazon SES will not encrypt your emails.

              .. warning::

                Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
                the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
                server-side encryption. This means that you must use the Amazon S3 encryption
                client to decrypt the email after retrieving it from Amazon S3, as the service has
                no access to use your AWS KMS keys for decryption. This encryption client is
                currently available with the `AWS SDK for Java
                <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
                <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
                client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
                Guide
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
                .

          - **BounceAction** *(dict) --*

            Rejects the received email by returning a bounce response to the sender and,
            optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
              action is taken. An example of an Amazon SNS topic ARN is
              ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
              SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **SmtpReplyCode** *(string) --*

              The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__
              .

            - **StatusCode** *(string) --*

              The SMTP enhanced status code, as defined by `RFC 3463
              <https://tools.ietf.org/html/rfc3463>`__ .

            - **Message** *(string) --*

              Human-readable text to include in the bounce message.

            - **Sender** *(string) --*

              The email address of the sender of the bounced email. This is the address from which
              the bounce message will be sent.

          - **WorkmailAction** *(dict) --*

            Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
              action is called. An example of an Amazon SNS topic ARN is
              ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
              SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **OrganizationArn** *(string) --*

              The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
              organization ARN is
              ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
              . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
              Administrator Guide
              <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
              .

          - **LambdaAction** *(dict) --*

            Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
              action is taken. An example of an Amazon SNS topic ARN is
              ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
              SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **FunctionArn** *(string) --*

              The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
              Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` .
              For more information about AWS Lambda, see the `AWS Lambda Developer Guide
              <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

            - **InvocationType** *(string) --*

              The invocation type of the AWS Lambda function. An invocation type of
              ``RequestResponse`` means that the execution of the function will immediately result
              in a response, and a value of ``Event`` means that the function will be invoked
              asynchronously. The default value is ``Event`` . For information about AWS Lambda
              invocation types, see the `AWS Lambda Developer Guide
              <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

              .. warning::

                There is a 30-second timeout on ``RequestResponse`` invocations. You should use
                ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
                make a mail flow decision, such as whether to stop the receipt rule or the receipt
                rule set.

          - **StopAction** *(dict) --*

            Terminates the evaluation of the receipt rule set and optionally publishes a
            notification to Amazon SNS.

            - **Scope** *(string) --*

              The scope of the StopAction. The only acceptable value is ``RuleSet`` .

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action
              is taken. An example of an Amazon SNS topic ARN is
              ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
              SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **AddHeaderAction** *(dict) --*

            Adds a header to the received email.

            - **HeaderName** *(string) --*

              The name of the header to add. Must be between 1 and 50 characters, inclusive, and
              consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

            - **HeaderValue** *(string) --*

              Must be less than 2048 characters, and must not contain newline characters ("\\r" or
              "\\n").

          - **SNSAction** *(dict) --*

            Publishes the email content within a notification to Amazon SNS.

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
              Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
              information about Amazon SNS topics, see the `Amazon SNS Developer Guide
              <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **Encoding** *(string) --*

              The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier
              to use, but may not preserve all special characters when a message was encoded with a
              different encoding format. Base64 preserves all special characters. The default value
              is UTF-8.

      - **ScanEnabled** *(boolean) --*

        If ``true`` , then messages that this receipt rule applies to are scanned for spam and
        viruses. The default value is ``false`` .
    """


_ClientDescribeReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseMetadataTypeDef(
    _ClientDescribeReceiptRuleSetResponseMetadataTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponse` `Metadata`

    The metadata for the receipt rule set, which consists of the rule set name and the timestamp
    of when the rule set was created.

    - **Name** *(string) --*

      The name of the receipt rule set. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **CreatedTimestamp** *(datetime) --*

      The date and time the receipt rule set was created.
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `AddHeaderAction`

    Adds a header to the received email.

    - **HeaderName** *(string) --*

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **HeaderValue** *(string) --*

      Must be less than 2048 characters, and must not contain newline characters ("\\r"
      or "\\n").
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {
        "TopicArn": str,
        "SmtpReplyCode": str,
        "StatusCode": str,
        "Message": str,
        "Sender": str,
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `BounceAction`

    Rejects the received email by returning a bounce response to the sender and,
    optionally, publishes a notification to Amazon Simple Notification Service (Amazon
    SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **SmtpReplyCode** *(string) --*

      The SMTP reply code, as defined by `RFC 5321
      <https://tools.ietf.org/html/rfc5321>`__ .

    - **StatusCode** *(string) --*

      The SMTP enhanced status code, as defined by `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ .

    - **Message** *(string) --*

      Human-readable text to include in the bounce message.

    - **Sender** *(string) --*

      The email address of the sender of the bounced email. This is the address from
      which the bounce message will be sent.
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `LambdaAction`

    Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **FunctionArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
      Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
      . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

    - **InvocationType** *(string) --*

      The invocation type of the AWS Lambda function. An invocation type of
      ``RequestResponse`` means that the execution of the function will immediately
      result in a response, and a value of ``Event`` means that the function will be
      invoked asynchronously. The default value is ``Event`` . For information about AWS
      Lambda invocation types, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

      .. warning::

        There is a 30-second timeout on ``RequestResponse`` invocations. You should use
        ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
        make a mail flow decision, such as whether to stop the receipt rule or the
        receipt rule set.
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `S3Action`

    Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
    and, optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
      S3 bucket. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket that incoming email will be saved to.

    - **ObjectKeyPrefix** *(string) --*

      The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
      name that enables you to store similar data under the same directory in a bucket.

    - **KmsKeyArn** *(string) --*

      The customer master key that Amazon SES should use to encrypt your emails before
      saving them to the Amazon S3 bucket. You can use the default master key or a custom
      master key you created in AWS KMS as follows:

      * To use the default master key, provide an ARN in the form of
      ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
      your AWS account ID is 123456789012 and you want to use the default master key in
      the US West (Oregon) region, the ARN of the default master key would be
      ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
      master key, you don't need to perform any extra steps to give Amazon SES permission
      to use the key.

      * To use a custom master key you created in AWS KMS, provide the ARN of the master
      key and ensure that you add a statement to your key's policy to give Amazon SES
      permission to use it. For more information about giving permissions, see the
      `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
      .

      For more information about key policies, see the `AWS KMS Developer Guide
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
      do not specify a master key, Amazon SES will not encrypt your emails.

      .. warning::

        Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
        the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
        S3 server-side encryption. This means that you must use the Amazon S3 encryption
        client to decrypt the email after retrieving it from Amazon S3, as the service
        has no access to use your AWS KMS keys for decryption. This encryption client is
        currently available with the `AWS SDK for Java
        <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
        <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
        client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
        Guide
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
        .
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `SNSAction`

    Publishes the email content within a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
      Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
      information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **Encoding** *(string) --*

      The encoding to use for the email within the Amazon SNS notification. UTF-8 is
      easier to use, but may not preserve all special characters when a message was
      encoded with a different encoding format. Base64 preserves all special characters.
      The default value is UTF-8.
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `StopAction`

    Terminates the evaluation of the receipt rule set and optionally publishes a
    notification to Amazon SNS.

    - **Scope** *(string) --*

      The scope of the StopAction. The only acceptable value is ``RuleSet`` .

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
      action is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRulesActions` `WorkmailAction`

    Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
      action is called. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
      SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **OrganizationArn** *(string) --*

      The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
      organization ARN is
      ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
      . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
      Administrator Guide
      <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
      .
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponseRules` `Actions`

    An action that Amazon SES can take when it receives an email on behalf of one or more
    email addresses or domains that you own. An instance of this data type can represent
    only one action.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **S3Action** *(dict) --*

      Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
      and, optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
        S3 bucket. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket that incoming email will be saved to.

      - **ObjectKeyPrefix** *(string) --*

        The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
        name that enables you to store similar data under the same directory in a bucket.

      - **KmsKeyArn** *(string) --*

        The customer master key that Amazon SES should use to encrypt your emails before
        saving them to the Amazon S3 bucket. You can use the default master key or a custom
        master key you created in AWS KMS as follows:

        * To use the default master key, provide an ARN in the form of
        ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
        your AWS account ID is 123456789012 and you want to use the default master key in
        the US West (Oregon) region, the ARN of the default master key would be
        ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
        master key, you don't need to perform any extra steps to give Amazon SES permission
        to use the key.

        * To use a custom master key you created in AWS KMS, provide the ARN of the master
        key and ensure that you add a statement to your key's policy to give Amazon SES
        permission to use it. For more information about giving permissions, see the
        `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
        .

        For more information about key policies, see the `AWS KMS Developer Guide
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
        do not specify a master key, Amazon SES will not encrypt your emails.

        .. warning::

          Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
          the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
          S3 server-side encryption. This means that you must use the Amazon S3 encryption
          client to decrypt the email after retrieving it from Amazon S3, as the service
          has no access to use your AWS KMS keys for decryption. This encryption client is
          currently available with the `AWS SDK for Java
          <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
          <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
          client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
          Guide
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
          .

    - **BounceAction** *(dict) --*

      Rejects the received email by returning a bounce response to the sender and,
      optionally, publishes a notification to Amazon Simple Notification Service (Amazon
      SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **SmtpReplyCode** *(string) --*

        The SMTP reply code, as defined by `RFC 5321
        <https://tools.ietf.org/html/rfc5321>`__ .

      - **StatusCode** *(string) --*

        The SMTP enhanced status code, as defined by `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ .

      - **Message** *(string) --*

        Human-readable text to include in the bounce message.

      - **Sender** *(string) --*

        The email address of the sender of the bounced email. This is the address from
        which the bounce message will be sent.

    - **WorkmailAction** *(dict) --*

      Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
        action is called. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **OrganizationArn** *(string) --*

        The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
        organization ARN is
        ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
        . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
        Administrator Guide
        <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
        .

    - **LambdaAction** *(dict) --*

      Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
        Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
        . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

      - **InvocationType** *(string) --*

        The invocation type of the AWS Lambda function. An invocation type of
        ``RequestResponse`` means that the execution of the function will immediately
        result in a response, and a value of ``Event`` means that the function will be
        invoked asynchronously. The default value is ``Event`` . For information about AWS
        Lambda invocation types, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

        .. warning::

          There is a 30-second timeout on ``RequestResponse`` invocations. You should use
          ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
          make a mail flow decision, such as whether to stop the receipt rule or the
          receipt rule set.

    - **StopAction** *(dict) --*

      Terminates the evaluation of the receipt rule set and optionally publishes a
      notification to Amazon SNS.

      - **Scope** *(string) --*

        The scope of the StopAction. The only acceptable value is ``RuleSet`` .

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
        action is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
        SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **AddHeaderAction** *(dict) --*

      Adds a header to the received email.

      - **HeaderName** *(string) --*

        The name of the header to add. Must be between 1 and 50 characters, inclusive, and
        consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

      - **HeaderValue** *(string) --*

        Must be less than 2048 characters, and must not contain newline characters ("\\r"
        or "\\n").

    - **SNSAction** *(dict) --*

      Publishes the email content within a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
        Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
        information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **Encoding** *(string) --*

        The encoding to use for the email within the Amazon SNS notification. UTF-8 is
        easier to use, but may not preserve all special characters when a message was
        encoded with a different encoding format. Base64 preserves all special characters.
        The default value is UTF-8.
    """


_ClientDescribeReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": str,
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSetResponse` `Rules`

    Receipt rules enable you to specify which actions Amazon SES should take when it receives
    mail on behalf of one or more email addresses or domains that you own.

    Each receipt rule defines a set of email addresses or domains that it applies to. If the
    email addresses or domains match at least one recipient address of the message, Amazon SES
    executes all of the receipt rule's actions on the message.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **Name** *(string) --*

      The name of the receipt rule. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      If ``true`` , the receipt rule is active. The default value is ``false`` .

    - **TlsPolicy** *(string) --*

      Specifies whether Amazon SES should require that incoming email is delivered over a
      connection encrypted with Transport Layer Security (TLS). If this parameter is set to
      ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default
      is ``Optional`` .

    - **Recipients** *(list) --*

      The recipient domains and email addresses that the receipt rule applies to. If this field
      is not specified, this rule will match all recipients under all verified domains.

      - *(string) --*

    - **Actions** *(list) --*

      An ordered list of actions to perform on messages that match at least one of the
      recipient email addresses or domains specified in the receipt rule.

      - *(dict) --*

        An action that Amazon SES can take when it receives an email on behalf of one or more
        email addresses or domains that you own. An instance of this data type can represent
        only one action.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **S3Action** *(dict) --*

          Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
          and, optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
            S3 bucket. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **BucketName** *(string) --*

            The name of the Amazon S3 bucket that incoming email will be saved to.

          - **ObjectKeyPrefix** *(string) --*

            The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
            name that enables you to store similar data under the same directory in a bucket.

          - **KmsKeyArn** *(string) --*

            The customer master key that Amazon SES should use to encrypt your emails before
            saving them to the Amazon S3 bucket. You can use the default master key or a custom
            master key you created in AWS KMS as follows:

            * To use the default master key, provide an ARN in the form of
            ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
            your AWS account ID is 123456789012 and you want to use the default master key in
            the US West (Oregon) region, the ARN of the default master key would be
            ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
            master key, you don't need to perform any extra steps to give Amazon SES permission
            to use the key.

            * To use a custom master key you created in AWS KMS, provide the ARN of the master
            key and ensure that you add a statement to your key's policy to give Amazon SES
            permission to use it. For more information about giving permissions, see the
            `Amazon SES Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
            .

            For more information about key policies, see the `AWS KMS Developer Guide
            <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
            do not specify a master key, Amazon SES will not encrypt your emails.

            .. warning::

              Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
              the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
              S3 server-side encryption. This means that you must use the Amazon S3 encryption
              client to decrypt the email after retrieving it from Amazon S3, as the service
              has no access to use your AWS KMS keys for decryption. This encryption client is
              currently available with the `AWS SDK for Java
              <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
              <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
              client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
              Guide
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
              .

        - **BounceAction** *(dict) --*

          Rejects the received email by returning a bounce response to the sender and,
          optionally, publishes a notification to Amazon Simple Notification Service (Amazon
          SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **SmtpReplyCode** *(string) --*

            The SMTP reply code, as defined by `RFC 5321
            <https://tools.ietf.org/html/rfc5321>`__ .

          - **StatusCode** *(string) --*

            The SMTP enhanced status code, as defined by `RFC 3463
            <https://tools.ietf.org/html/rfc3463>`__ .

          - **Message** *(string) --*

            Human-readable text to include in the bounce message.

          - **Sender** *(string) --*

            The email address of the sender of the bounced email. This is the address from
            which the bounce message will be sent.

        - **WorkmailAction** *(dict) --*

          Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
            action is called. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **OrganizationArn** *(string) --*

            The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
            organization ARN is
            ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
            . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
            Administrator Guide
            <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
            .

        - **LambdaAction** *(dict) --*

          Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **FunctionArn** *(string) --*

            The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
            Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
            . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

          - **InvocationType** *(string) --*

            The invocation type of the AWS Lambda function. An invocation type of
            ``RequestResponse`` means that the execution of the function will immediately
            result in a response, and a value of ``Event`` means that the function will be
            invoked asynchronously. The default value is ``Event`` . For information about AWS
            Lambda invocation types, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

            .. warning::

              There is a 30-second timeout on ``RequestResponse`` invocations. You should use
              ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
              make a mail flow decision, such as whether to stop the receipt rule or the
              receipt rule set.

        - **StopAction** *(dict) --*

          Terminates the evaluation of the receipt rule set and optionally publishes a
          notification to Amazon SNS.

          - **Scope** *(string) --*

            The scope of the StopAction. The only acceptable value is ``RuleSet`` .

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
            action is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
            SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **AddHeaderAction** *(dict) --*

          Adds a header to the received email.

          - **HeaderName** *(string) --*

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **HeaderValue** *(string) --*

            Must be less than 2048 characters, and must not contain newline characters ("\\r"
            or "\\n").

        - **SNSAction** *(dict) --*

          Publishes the email content within a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
            Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
            information about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **Encoding** *(string) --*

            The encoding to use for the email within the Amazon SNS notification. UTF-8 is
            easier to use, but may not preserve all special characters when a message was
            encoded with a different encoding format. Base64 preserves all special characters.
            The default value is UTF-8.

    - **ScanEnabled** *(boolean) --*

      If ``true`` , then messages that this receipt rule applies to are scanned for spam and
      viruses. The default value is ``false`` .
    """


_ClientDescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseTypeDef(
    _ClientDescribeReceiptRuleSetResponseTypeDef
):
    """
    Type definition for `ClientDescribeReceiptRuleSet` `Response`

    Represents the details of the specified receipt rule set.

    - **Metadata** *(dict) --*

      The metadata for the receipt rule set, which consists of the rule set name and the timestamp
      of when the rule set was created.

      - **Name** *(string) --*

        The name of the receipt rule set. The name must:

        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).

        * Start and end with a letter or number.

        * Contain less than 64 characters.

      - **CreatedTimestamp** *(datetime) --*

        The date and time the receipt rule set was created.

    - **Rules** *(list) --*

      A list of the receipt rules that belong to the specified receipt rule set.

      - *(dict) --*

        Receipt rules enable you to specify which actions Amazon SES should take when it receives
        mail on behalf of one or more email addresses or domains that you own.

        Each receipt rule defines a set of email addresses or domains that it applies to. If the
        email addresses or domains match at least one recipient address of the message, Amazon SES
        executes all of the receipt rule's actions on the message.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **Name** *(string) --*

          The name of the receipt rule. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Start and end with a letter or number.

          * Contain less than 64 characters.

        - **Enabled** *(boolean) --*

          If ``true`` , the receipt rule is active. The default value is ``false`` .

        - **TlsPolicy** *(string) --*

          Specifies whether Amazon SES should require that incoming email is delivered over a
          connection encrypted with Transport Layer Security (TLS). If this parameter is set to
          ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default
          is ``Optional`` .

        - **Recipients** *(list) --*

          The recipient domains and email addresses that the receipt rule applies to. If this field
          is not specified, this rule will match all recipients under all verified domains.

          - *(string) --*

        - **Actions** *(list) --*

          An ordered list of actions to perform on messages that match at least one of the
          recipient email addresses or domains specified in the receipt rule.

          - *(dict) --*

            An action that Amazon SES can take when it receives an email on behalf of one or more
            email addresses or domains that you own. An instance of this data type can represent
            only one action.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
            .

            - **S3Action** *(dict) --*

              Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket
              and, optionally, publishes a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon
                S3 bucket. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **BucketName** *(string) --*

                The name of the Amazon S3 bucket that incoming email will be saved to.

              - **ObjectKeyPrefix** *(string) --*

                The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory
                name that enables you to store similar data under the same directory in a bucket.

              - **KmsKeyArn** *(string) --*

                The customer master key that Amazon SES should use to encrypt your emails before
                saving them to the Amazon S3 bucket. You can use the default master key or a custom
                master key you created in AWS KMS as follows:

                * To use the default master key, provide an ARN in the form of
                ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if
                your AWS account ID is 123456789012 and you want to use the default master key in
                the US West (Oregon) region, the ARN of the default master key would be
                ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default
                master key, you don't need to perform any extra steps to give Amazon SES permission
                to use the key.

                * To use a custom master key you created in AWS KMS, provide the ARN of the master
                key and ensure that you add a statement to your key's policy to give Amazon SES
                permission to use it. For more information about giving permissions, see the
                `Amazon SES Developer Guide
                <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
                .

                For more information about key policies, see the `AWS KMS Developer Guide
                <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you
                do not specify a master key, Amazon SES will not encrypt your emails.

                .. warning::

                  Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before
                  the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon
                  S3 server-side encryption. This means that you must use the Amazon S3 encryption
                  client to decrypt the email after retrieving it from Amazon S3, as the service
                  has no access to use your AWS KMS keys for decryption. This encryption client is
                  currently available with the `AWS SDK for Java
                  <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for Ruby
                  <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
                  client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer
                  Guide
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__
                  .

            - **BounceAction** *(dict) --*

              Rejects the received email by returning a bounce response to the sender and,
              optionally, publishes a notification to Amazon Simple Notification Service (Amazon
              SNS).

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **SmtpReplyCode** *(string) --*

                The SMTP reply code, as defined by `RFC 5321
                <https://tools.ietf.org/html/rfc5321>`__ .

              - **StatusCode** *(string) --*

                The SMTP enhanced status code, as defined by `RFC 3463
                <https://tools.ietf.org/html/rfc3463>`__ .

              - **Message** *(string) --*

                Human-readable text to include in the bounce message.

              - **Sender** *(string) --*

                The email address of the sender of the bounced email. This is the address from
                which the bounce message will be sent.

            - **WorkmailAction** *(dict) --*

              Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail
                action is called. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **OrganizationArn** *(string) --*

                The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
                organization ARN is
                ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
                . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
                Administrator Guide
                <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__
                .

            - **LambdaAction** *(dict) --*

              Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **FunctionArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS
                Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction``
                . For more information about AWS Lambda, see the `AWS Lambda Developer Guide
                <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

              - **InvocationType** *(string) --*

                The invocation type of the AWS Lambda function. An invocation type of
                ``RequestResponse`` means that the execution of the function will immediately
                result in a response, and a value of ``Event`` means that the function will be
                invoked asynchronously. The default value is ``Event`` . For information about AWS
                Lambda invocation types, see the `AWS Lambda Developer Guide
                <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

                .. warning::

                  There is a 30-second timeout on ``RequestResponse`` invocations. You should use
                  ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to
                  make a mail flow decision, such as whether to stop the receipt rule or the
                  receipt rule set.

            - **StopAction** *(dict) --*

              Terminates the evaluation of the receipt rule set and optionally publishes a
              notification to Amazon SNS.

              - **Scope** *(string) --*

                The scope of the StopAction. The only acceptable value is ``RuleSet`` .

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop
                action is taken. An example of an Amazon SNS topic ARN is
                ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon
                SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

            - **AddHeaderAction** *(dict) --*

              Adds a header to the received email.

              - **HeaderName** *(string) --*

                The name of the header to add. Must be between 1 and 50 characters, inclusive, and
                consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

              - **HeaderValue** *(string) --*

                Must be less than 2048 characters, and must not contain newline characters ("\\r"
                or "\\n").

            - **SNSAction** *(dict) --*

              Publishes the email content within a notification to Amazon SNS.

              - **TopicArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an
                Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
                information about Amazon SNS topics, see the `Amazon SNS Developer Guide
                <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              - **Encoding** *(string) --*

                The encoding to use for the email within the Amazon SNS notification. UTF-8 is
                easier to use, but may not preserve all special characters when a message was
                encoded with a different encoding format. Base64 preserves all special characters.
                The default value is UTF-8.

        - **ScanEnabled** *(boolean) --*

          If ``true`` , then messages that this receipt rule applies to are scanned for spam and
          viruses. The default value is ``false`` .
    """


_ClientGetAccountSendingEnabledResponseTypeDef = TypedDict(
    "_ClientGetAccountSendingEnabledResponseTypeDef", {"Enabled": bool}, total=False
)


class ClientGetAccountSendingEnabledResponseTypeDef(
    _ClientGetAccountSendingEnabledResponseTypeDef
):
    """
    Type definition for `ClientGetAccountSendingEnabled` `Response`

    Represents a request to return the email sending status for your Amazon SES account in the
    current AWS Region.

    - **Enabled** *(boolean) --*

      Describes whether email sending is enabled or disabled for your Amazon SES account in the
      current AWS Region.
    """


_ClientGetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "_ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ClientGetCustomVerificationEmailTemplateResponseTypeDef(
    _ClientGetCustomVerificationEmailTemplateResponseTypeDef
):
    """
    Type definition for `ClientGetCustomVerificationEmailTemplate` `Response`

    The content of the custom verification email template.

    - **TemplateName** *(string) --*

      The name of the custom verification email template.

    - **FromEmailAddress** *(string) --*

      The email address that the custom verification email is sent from.

    - **TemplateSubject** *(string) --*

      The subject line of the custom verification email.

    - **TemplateContent** *(string) --*

      The content of the custom verification email.

    - **SuccessRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is
      successfully verified.

    - **FailureRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is not
      successfully verified.
    """


_ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef = TypedDict(
    "_ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    {"DkimEnabled": bool, "DkimVerificationStatus": str, "DkimTokens": List[str]},
    total=False,
)


class ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef(
    _ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef
):
    """
    Type definition for `ClientGetIdentityDkimAttributesResponse` `DkimAttributes`

    Represents the DKIM attributes of a verified email address or a domain.

    - **DkimEnabled** *(boolean) --*

      Is true if DKIM signing is enabled for email sent from the identity. It's false
      otherwise. The default value is true.

    - **DkimVerificationStatus** *(string) --*

      Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens)
      published in the domain name's DNS. (This only applies to domain identities, not email
      address identities.)

    - **DkimTokens** *(list) --*

      A set of character strings that represent the domain's identity. Using these tokens,
      you need to create DNS CNAME records that point to DKIM public keys that are hosted by
      Amazon SES. Amazon Web Services eventually detects that you've updated your DNS
      records. This detection process might take up to 72 hours. After successful detection,
      Amazon SES is able to DKIM-sign email originating from that domain. (This only applies
      to domain identities, not email address identities.)

      For more information about creating DNS records using DKIM tokens, see the `Amazon SES
      Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html>`__ .

      - *(string) --*
    """


_ClientGetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityDkimAttributesResponseTypeDef",
    {
        "DkimAttributes": Dict[
            str, ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef
        ]
    },
    total=False,
)


class ClientGetIdentityDkimAttributesResponseTypeDef(
    _ClientGetIdentityDkimAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityDkimAttributes` `Response`

    Represents the status of Amazon SES Easy DKIM signing for an identity. For domain identities,
    this response also contains the DKIM tokens that are required for Easy DKIM signing, and
    whether Amazon SES successfully verified that these tokens were published.

    - **DkimAttributes** *(dict) --*

      The DKIM attributes for an email address or a domain.

      - *(string) --*

        - *(dict) --*

          Represents the DKIM attributes of a verified email address or a domain.

          - **DkimEnabled** *(boolean) --*

            Is true if DKIM signing is enabled for email sent from the identity. It's false
            otherwise. The default value is true.

          - **DkimVerificationStatus** *(string) --*

            Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens)
            published in the domain name's DNS. (This only applies to domain identities, not email
            address identities.)

          - **DkimTokens** *(list) --*

            A set of character strings that represent the domain's identity. Using these tokens,
            you need to create DNS CNAME records that point to DKIM public keys that are hosted by
            Amazon SES. Amazon Web Services eventually detects that you've updated your DNS
            records. This detection process might take up to 72 hours. After successful detection,
            Amazon SES is able to DKIM-sign email originating from that domain. (This only applies
            to domain identities, not email address identities.)

            For more information about creating DNS records using DKIM tokens, see the `Amazon SES
            Developer Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html>`__ .

            - *(string) --*
    """


_ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef = TypedDict(
    "_ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    {"MailFromDomain": str, "MailFromDomainStatus": str, "BehaviorOnMXFailure": str},
    total=False,
)


class ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef(
    _ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef
):
    """
    Type definition for `ClientGetIdentityMailFromDomainAttributesResponse` `MailFromDomainAttributes`

    Represents the custom MAIL FROM domain attributes of a verified identity (email address
    or domain).

    - **MailFromDomain** *(string) --*

      The custom MAIL FROM domain that the identity is configured to use.

    - **MailFromDomainStatus** *(string) --*

      The state that indicates whether Amazon SES has successfully read the MX record
      required for custom MAIL FROM domain setup. If the state is ``Success`` , Amazon SES
      uses the specified custom MAIL FROM domain when the verified identity sends an email.
      All other states indicate that Amazon SES takes the action described by
      ``BehaviorOnMXFailure`` .

    - **BehaviorOnMXFailure** *(string) --*

      The action that Amazon SES takes if it cannot successfully read the required MX record
      when you send an email. A value of ``UseDefaultValue`` indicates that if Amazon SES
      cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as
      the MAIL FROM domain. A value of ``RejectMessage`` indicates that if Amazon SES cannot
      read the required MX record, Amazon SES returns a ``MailFromDomainNotVerified`` error
      and does not send the email.

      The custom MAIL FROM setup states that result in this behavior are ``Pending`` ,
      ``Failed`` , and ``TemporaryFailure`` .
    """


_ClientGetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[
            str,
            ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef,
        ]
    },
    total=False,
)


class ClientGetIdentityMailFromDomainAttributesResponseTypeDef(
    _ClientGetIdentityMailFromDomainAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityMailFromDomainAttributes` `Response`

    Represents the custom MAIL FROM attributes for a list of identities.

    - **MailFromDomainAttributes** *(dict) --*

      A map of identities to custom MAIL FROM attributes.

      - *(string) --*

        - *(dict) --*

          Represents the custom MAIL FROM domain attributes of a verified identity (email address
          or domain).

          - **MailFromDomain** *(string) --*

            The custom MAIL FROM domain that the identity is configured to use.

          - **MailFromDomainStatus** *(string) --*

            The state that indicates whether Amazon SES has successfully read the MX record
            required for custom MAIL FROM domain setup. If the state is ``Success`` , Amazon SES
            uses the specified custom MAIL FROM domain when the verified identity sends an email.
            All other states indicate that Amazon SES takes the action described by
            ``BehaviorOnMXFailure`` .

          - **BehaviorOnMXFailure** *(string) --*

            The action that Amazon SES takes if it cannot successfully read the required MX record
            when you send an email. A value of ``UseDefaultValue`` indicates that if Amazon SES
            cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as
            the MAIL FROM domain. A value of ``RejectMessage`` indicates that if Amazon SES cannot
            read the required MX record, Amazon SES returns a ``MailFromDomainNotVerified`` error
            and does not send the email.

            The custom MAIL FROM setup states that result in this behavior are ``Pending`` ,
            ``Failed`` , and ``TemporaryFailure`` .
    """


_ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef = TypedDict(
    "_ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
        "HeadersInBounceNotificationsEnabled": bool,
        "HeadersInComplaintNotificationsEnabled": bool,
        "HeadersInDeliveryNotificationsEnabled": bool,
    },
    total=False,
)


class ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef(
    _ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef
):
    """
    Type definition for `ClientGetIdentityNotificationAttributesResponse` `NotificationAttributes`

    Represents the notification attributes of an identity, including whether an identity has
    Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or
    delivery notifications, and whether feedback forwarding is enabled for bounce and
    complaint notifications.

    - **BounceTopic** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
      bounce notifications.

    - **ComplaintTopic** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
      complaint notifications.

    - **DeliveryTopic** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
      delivery notifications.

    - **ForwardingEnabled** *(boolean) --*

      Describes whether Amazon SES will forward bounce and complaint notifications as email.
      ``true`` indicates that Amazon SES will forward bounce and complaint notifications as
      email, while ``false`` indicates that bounce and complaint notifications will be
      published only to the specified bounce and complaint Amazon SNS topics.

    - **HeadersInBounceNotificationsEnabled** *(boolean) --*

      Describes whether Amazon SES includes the original email headers in Amazon SNS
      notifications of type ``Bounce`` . A value of ``true`` specifies that Amazon SES will
      include headers in bounce notifications, and a value of ``false`` specifies that Amazon
      SES will not include headers in bounce notifications.

    - **HeadersInComplaintNotificationsEnabled** *(boolean) --*

      Describes whether Amazon SES includes the original email headers in Amazon SNS
      notifications of type ``Complaint`` . A value of ``true`` specifies that Amazon SES
      will include headers in complaint notifications, and a value of ``false`` specifies
      that Amazon SES will not include headers in complaint notifications.

    - **HeadersInDeliveryNotificationsEnabled** *(boolean) --*

      Describes whether Amazon SES includes the original email headers in Amazon SNS
      notifications of type ``Delivery`` . A value of ``true`` specifies that Amazon SES will
      include headers in delivery notifications, and a value of ``false`` specifies that
      Amazon SES will not include headers in delivery notifications.
    """


_ClientGetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[
            str,
            ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef,
        ]
    },
    total=False,
)


class ClientGetIdentityNotificationAttributesResponseTypeDef(
    _ClientGetIdentityNotificationAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityNotificationAttributes` `Response`

    Represents the notification attributes for a list of identities.

    - **NotificationAttributes** *(dict) --*

      A map of Identity to IdentityNotificationAttributes.

      - *(string) --*

        - *(dict) --*

          Represents the notification attributes of an identity, including whether an identity has
          Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or
          delivery notifications, and whether feedback forwarding is enabled for bounce and
          complaint notifications.

          - **BounceTopic** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
            bounce notifications.

          - **ComplaintTopic** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
            complaint notifications.

          - **DeliveryTopic** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
            delivery notifications.

          - **ForwardingEnabled** *(boolean) --*

            Describes whether Amazon SES will forward bounce and complaint notifications as email.
            ``true`` indicates that Amazon SES will forward bounce and complaint notifications as
            email, while ``false`` indicates that bounce and complaint notifications will be
            published only to the specified bounce and complaint Amazon SNS topics.

          - **HeadersInBounceNotificationsEnabled** *(boolean) --*

            Describes whether Amazon SES includes the original email headers in Amazon SNS
            notifications of type ``Bounce`` . A value of ``true`` specifies that Amazon SES will
            include headers in bounce notifications, and a value of ``false`` specifies that Amazon
            SES will not include headers in bounce notifications.

          - **HeadersInComplaintNotificationsEnabled** *(boolean) --*

            Describes whether Amazon SES includes the original email headers in Amazon SNS
            notifications of type ``Complaint`` . A value of ``true`` specifies that Amazon SES
            will include headers in complaint notifications, and a value of ``false`` specifies
            that Amazon SES will not include headers in complaint notifications.

          - **HeadersInDeliveryNotificationsEnabled** *(boolean) --*

            Describes whether Amazon SES includes the original email headers in Amazon SNS
            notifications of type ``Delivery`` . A value of ``true`` specifies that Amazon SES will
            include headers in delivery notifications, and a value of ``false`` specifies that
            Amazon SES will not include headers in delivery notifications.
    """


_ClientGetIdentityPoliciesResponseTypeDef = TypedDict(
    "_ClientGetIdentityPoliciesResponseTypeDef",
    {"Policies": Dict[str, str]},
    total=False,
)


class ClientGetIdentityPoliciesResponseTypeDef(
    _ClientGetIdentityPoliciesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityPolicies` `Response`

    Represents the requested sending authorization policies.

    - **Policies** *(dict) --*

      A map of policy names to policies.

      - *(string) --*

        - *(string) --*
    """


_ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef = TypedDict(
    "_ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    {"VerificationStatus": str, "VerificationToken": str},
    total=False,
)


class ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef(
    _ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef
):
    """
    Type definition for `ClientGetIdentityVerificationAttributesResponse` `VerificationAttributes`

    Represents the verification attributes of a single identity.

    - **VerificationStatus** *(string) --*

      The verification status of the identity: "Pending", "Success", "Failed", or
      "TemporaryFailure".

    - **VerificationToken** *(string) --*

      The verification token for a domain identity. Null for email address identities.
    """


_ClientGetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[
            str,
            ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef,
        ]
    },
    total=False,
)


class ClientGetIdentityVerificationAttributesResponseTypeDef(
    _ClientGetIdentityVerificationAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityVerificationAttributes` `Response`

    The Amazon SES verification status of a list of identities. For domain identities, this
    response also contains the verification token.

    - **VerificationAttributes** *(dict) --*

      A map of Identities to IdentityVerificationAttributes objects.

      - *(string) --*

        - *(dict) --*

          Represents the verification attributes of a single identity.

          - **VerificationStatus** *(string) --*

            The verification status of the identity: "Pending", "Success", "Failed", or
            "TemporaryFailure".

          - **VerificationToken** *(string) --*

            The verification token for a domain identity. Null for email address identities.
    """


_ClientGetSendQuotaResponseTypeDef = TypedDict(
    "_ClientGetSendQuotaResponseTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)


class ClientGetSendQuotaResponseTypeDef(_ClientGetSendQuotaResponseTypeDef):
    """
    Type definition for `ClientGetSendQuota` `Response`

    Represents your Amazon SES daily sending quota, maximum send rate, and the number of emails you
    have sent in the last 24 hours.

    - **Max24HourSend** *(float) --*

      The maximum number of emails the user is allowed to send in a 24-hour interval. A value of -1
      signifies an unlimited quota.

    - **MaxSendRate** *(float) --*

      The maximum number of emails that Amazon SES can accept from the user's account per second.

      .. note::

        The rate at which Amazon SES accepts the user's messages might be less than the maximum
        send rate.

    - **SentLast24Hours** *(float) --*

      The number of emails sent during the previous 24 hours.
    """


_ClientGetSendStatisticsResponseSendDataPointsTypeDef = TypedDict(
    "_ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    {
        "Timestamp": datetime,
        "DeliveryAttempts": int,
        "Bounces": int,
        "Complaints": int,
        "Rejects": int,
    },
    total=False,
)


class ClientGetSendStatisticsResponseSendDataPointsTypeDef(
    _ClientGetSendStatisticsResponseSendDataPointsTypeDef
):
    """
    Type definition for `ClientGetSendStatisticsResponse` `SendDataPoints`

    Represents sending statistics data. Each ``SendDataPoint`` contains statistics for a
    15-minute period of sending activity.

    - **Timestamp** *(datetime) --*

      Time of the data point.

    - **DeliveryAttempts** *(integer) --*

      Number of emails that have been sent.

    - **Bounces** *(integer) --*

      Number of emails that have bounced.

    - **Complaints** *(integer) --*

      Number of unwanted emails that were rejected by recipients.

    - **Rejects** *(integer) --*

      Number of emails rejected by Amazon SES.
    """


_ClientGetSendStatisticsResponseTypeDef = TypedDict(
    "_ClientGetSendStatisticsResponseTypeDef",
    {"SendDataPoints": List[ClientGetSendStatisticsResponseSendDataPointsTypeDef]},
    total=False,
)


class ClientGetSendStatisticsResponseTypeDef(_ClientGetSendStatisticsResponseTypeDef):
    """
    Type definition for `ClientGetSendStatistics` `Response`

    Represents a list of data points. This list contains aggregated data from the previous two
    weeks of your sending activity with Amazon SES.

    - **SendDataPoints** *(list) --*

      A list of data points, each of which represents 15 minutes of activity.

      - *(dict) --*

        Represents sending statistics data. Each ``SendDataPoint`` contains statistics for a
        15-minute period of sending activity.

        - **Timestamp** *(datetime) --*

          Time of the data point.

        - **DeliveryAttempts** *(integer) --*

          Number of emails that have been sent.

        - **Bounces** *(integer) --*

          Number of emails that have bounced.

        - **Complaints** *(integer) --*

          Number of unwanted emails that were rejected by recipients.

        - **Rejects** *(integer) --*

          Number of emails rejected by Amazon SES.
    """


_ClientGetTemplateResponseTemplateTypeDef = TypedDict(
    "_ClientGetTemplateResponseTemplateTypeDef",
    {"TemplateName": str, "SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientGetTemplateResponseTemplateTypeDef(
    _ClientGetTemplateResponseTemplateTypeDef
):
    """
    Type definition for `ClientGetTemplateResponse` `Template`

    The content of the email, composed of a subject line, an HTML part, and a text-only part.

    - **TemplateName** *(string) --*

      The name of the template. You will refer to this name when you send email using the
      ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

    - **SubjectPart** *(string) --*

      The subject line of the email.

    - **TextPart** *(string) --*

      The email body that will be visible to recipients whose email clients do not display HTML.

    - **HtmlPart** *(string) --*

      The HTML body of the email.
    """


_ClientGetTemplateResponseTypeDef = TypedDict(
    "_ClientGetTemplateResponseTypeDef",
    {"Template": ClientGetTemplateResponseTemplateTypeDef},
    total=False,
)


class ClientGetTemplateResponseTypeDef(_ClientGetTemplateResponseTypeDef):
    """
    Type definition for `ClientGetTemplate` `Response`

    - **Template** *(dict) --*

      The content of the email, composed of a subject line, an HTML part, and a text-only part.

      - **TemplateName** *(string) --*

        The name of the template. You will refer to this name when you send email using the
        ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

      - **SubjectPart** *(string) --*

        The subject line of the email.

      - **TextPart** *(string) --*

        The email body that will be visible to recipients whose email clients do not display HTML.

      - **HtmlPart** *(string) --*

        The HTML body of the email.
    """


_ClientListConfigurationSetsResponseConfigurationSetsTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseConfigurationSetsTypeDef",
    {"Name": str},
    total=False,
)


class ClientListConfigurationSetsResponseConfigurationSetsTypeDef(
    _ClientListConfigurationSetsResponseConfigurationSetsTypeDef
):
    """
    Type definition for `ClientListConfigurationSetsResponse` `ConfigurationSets`

    The name of the configuration set.

    Configuration sets let you create groups of rules that you can apply to the emails you send
    using Amazon SES. For more information about using configuration sets, see `Using Amazon
    SES Configuration Sets
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
    the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__
    .

    - **Name** *(string) --*

      The name of the configuration set. The name must meet the following requirements:

      * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

      * Contain 64 characters or fewer.
    """


_ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[
            ClientListConfigurationSetsResponseConfigurationSetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationSetsResponseTypeDef(
    _ClientListConfigurationSetsResponseTypeDef
):
    """
    Type definition for `ClientListConfigurationSets` `Response`

    A list of configuration sets associated with your AWS account. Configuration sets enable you to
    publish email sending events. For information about using configuration sets, see the `Amazon
    SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **ConfigurationSets** *(list) --*

      A list of configuration sets.

      - *(dict) --*

        The name of the configuration set.

        Configuration sets let you create groups of rules that you can apply to the emails you send
        using Amazon SES. For more information about using configuration sets, see `Using Amazon
        SES Configuration Sets
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
        the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__
        .

        - **Name** *(string) --*

          The name of the configuration set. The name must meet the following requirements:

          * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

          * Contain 64 characters or fewer.

    - **NextToken** *(string) --*

      A token indicating that there are additional configuration sets available to be listed. Pass
      this token to successive calls of ``ListConfigurationSets`` .
    """


_ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef = TypedDict(
    "_ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef(
    _ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef
):
    """
    Type definition for `ClientListCustomVerificationEmailTemplatesResponse` `CustomVerificationEmailTemplates`

    Contains information about a custom verification email template.

    - **TemplateName** *(string) --*

      The name of the custom verification email template.

    - **FromEmailAddress** *(string) --*

      The email address that the custom verification email is sent from.

    - **TemplateSubject** *(string) --*

      The subject line of the custom verification email.

    - **SuccessRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is
      successfully verified.

    - **FailureRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is
      not successfully verified.
    """


_ClientListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "_ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[
            ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCustomVerificationEmailTemplatesResponseTypeDef(
    _ClientListCustomVerificationEmailTemplatesResponseTypeDef
):
    """
    Type definition for `ClientListCustomVerificationEmailTemplates` `Response`

    A paginated list of custom verification email templates.

    - **CustomVerificationEmailTemplates** *(list) --*

      A list of the custom verification email templates that exist in your account.

      - *(dict) --*

        Contains information about a custom verification email template.

        - **TemplateName** *(string) --*

          The name of the custom verification email template.

        - **FromEmailAddress** *(string) --*

          The email address that the custom verification email is sent from.

        - **TemplateSubject** *(string) --*

          The subject line of the custom verification email.

        - **SuccessRedirectionURL** *(string) --*

          The URL that the recipient of the verification email is sent to if his or her address is
          successfully verified.

        - **FailureRedirectionURL** *(string) --*

          The URL that the recipient of the verification email is sent to if his or her address is
          not successfully verified.

    - **NextToken** *(string) --*

      A token indicating that there are additional custom verification email templates available to
      be listed. Pass this token to a subsequent call to ``ListTemplates`` to retrieve the next 50
      custom verification email templates.
    """


_ClientListIdentitiesResponseTypeDef = TypedDict(
    "_ClientListIdentitiesResponseTypeDef",
    {"Identities": List[str], "NextToken": str},
    total=False,
)


class ClientListIdentitiesResponseTypeDef(_ClientListIdentitiesResponseTypeDef):
    """
    Type definition for `ClientListIdentities` `Response`

    A list of all identities that you have attempted to verify under your AWS account, regardless
    of verification status.

    - **Identities** *(list) --*

      A list of identities.

      - *(string) --*

    - **NextToken** *(string) --*

      The token used for pagination.
    """


_ClientListIdentityPoliciesResponseTypeDef = TypedDict(
    "_ClientListIdentityPoliciesResponseTypeDef",
    {"PolicyNames": List[str]},
    total=False,
)


class ClientListIdentityPoliciesResponseTypeDef(
    _ClientListIdentityPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListIdentityPolicies` `Response`

    A list of names of sending authorization policies that apply to an identity.

    - **PolicyNames** *(list) --*

      A list of names of policies that apply to the specified identity.

      - *(string) --*
    """


_ClientListReceiptFiltersResponseFiltersIpFilterTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    {"Policy": str, "Cidr": str},
    total=False,
)


class ClientListReceiptFiltersResponseFiltersIpFilterTypeDef(
    _ClientListReceiptFiltersResponseFiltersIpFilterTypeDef
):
    """
    Type definition for `ClientListReceiptFiltersResponseFilters` `IpFilter`

    A structure that provides the IP addresses to block or allow, and whether to block or
    allow incoming mail from them.

    - **Policy** *(string) --*

      Indicates whether to block or allow incoming mail from the specified IP addresses.

    - **Cidr** *(string) --*

      A single IP address or a range of IP addresses that you want to block or allow,
      specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single
      email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For
      more information about CIDR notation, see `RFC 2317
      <https://tools.ietf.org/html/rfc2317>`__ .
    """


_ClientListReceiptFiltersResponseFiltersTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseFiltersTypeDef",
    {"Name": str, "IpFilter": ClientListReceiptFiltersResponseFiltersIpFilterTypeDef},
    total=False,
)


class ClientListReceiptFiltersResponseFiltersTypeDef(
    _ClientListReceiptFiltersResponseFiltersTypeDef
):
    """
    Type definition for `ClientListReceiptFiltersResponse` `Filters`

    A receipt IP address filter enables you to specify whether to accept or reject mail
    originating from an IP address or range of IP addresses.

    For information about setting up IP address filters, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__ .

    - **Name** *(string) --*

      The name of the IP address filter. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **IpFilter** *(dict) --*

      A structure that provides the IP addresses to block or allow, and whether to block or
      allow incoming mail from them.

      - **Policy** *(string) --*

        Indicates whether to block or allow incoming mail from the specified IP addresses.

      - **Cidr** *(string) --*

        A single IP address or a range of IP addresses that you want to block or allow,
        specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single
        email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For
        more information about CIDR notation, see `RFC 2317
        <https://tools.ietf.org/html/rfc2317>`__ .
    """


_ClientListReceiptFiltersResponseTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseTypeDef",
    {"Filters": List[ClientListReceiptFiltersResponseFiltersTypeDef]},
    total=False,
)


class ClientListReceiptFiltersResponseTypeDef(_ClientListReceiptFiltersResponseTypeDef):
    """
    Type definition for `ClientListReceiptFilters` `Response`

    A list of IP address filters that exist under your AWS account.

    - **Filters** *(list) --*

      A list of IP address filter data structures, which each consist of a name, an IP address
      range, and whether to allow or block mail from it.

      - *(dict) --*

        A receipt IP address filter enables you to specify whether to accept or reject mail
        originating from an IP address or range of IP addresses.

        For information about setting up IP address filters, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__ .

        - **Name** *(string) --*

          The name of the IP address filter. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Start and end with a letter or number.

          * Contain less than 64 characters.

        - **IpFilter** *(dict) --*

          A structure that provides the IP addresses to block or allow, and whether to block or
          allow incoming mail from them.

          - **Policy** *(string) --*

            Indicates whether to block or allow incoming mail from the specified IP addresses.

          - **Cidr** *(string) --*

            A single IP address or a range of IP addresses that you want to block or allow,
            specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single
            email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For
            more information about CIDR notation, see `RFC 2317
            <https://tools.ietf.org/html/rfc2317>`__ .
    """


_ClientListReceiptRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "_ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientListReceiptRuleSetsResponseRuleSetsTypeDef(
    _ClientListReceiptRuleSetsResponseRuleSetsTypeDef
):
    """
    Type definition for `ClientListReceiptRuleSetsResponse` `RuleSets`

    Information about a receipt rule set.

    A receipt rule set is a collection of rules that specify what Amazon SES should do with
    mail it receives on behalf of your account's verified domains.

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
    .

    - **Name** *(string) --*

      The name of the receipt rule set. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **CreatedTimestamp** *(datetime) --*

      The date and time the receipt rule set was created.
    """


_ClientListReceiptRuleSetsResponseTypeDef = TypedDict(
    "_ClientListReceiptRuleSetsResponseTypeDef",
    {
        "RuleSets": List[ClientListReceiptRuleSetsResponseRuleSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListReceiptRuleSetsResponseTypeDef(
    _ClientListReceiptRuleSetsResponseTypeDef
):
    """
    Type definition for `ClientListReceiptRuleSets` `Response`

    A list of receipt rule sets that exist under your AWS account.

    - **RuleSets** *(list) --*

      The metadata for the currently active receipt rule set. The metadata consists of the rule set
      name and the timestamp of when the rule set was created.

      - *(dict) --*

        Information about a receipt rule set.

        A receipt rule set is a collection of rules that specify what Amazon SES should do with
        mail it receives on behalf of your account's verified domains.

        For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
        .

        - **Name** *(string) --*

          The name of the receipt rule set. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Start and end with a letter or number.

          * Contain less than 64 characters.

        - **CreatedTimestamp** *(datetime) --*

          The date and time the receipt rule set was created.

    - **NextToken** *(string) --*

      A token indicating that there are additional receipt rule sets available to be listed. Pass
      this token to successive calls of ``ListReceiptRuleSets`` to retrieve up to 100 receipt rule
      sets at a time.
    """


_ClientListTemplatesResponseTemplatesMetadataTypeDef = TypedDict(
    "_ClientListTemplatesResponseTemplatesMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientListTemplatesResponseTemplatesMetadataTypeDef(
    _ClientListTemplatesResponseTemplatesMetadataTypeDef
):
    """
    Type definition for `ClientListTemplatesResponse` `TemplatesMetadata`

    Contains information about an email template.

    - **Name** *(string) --*

      The name of the template.

    - **CreatedTimestamp** *(datetime) --*

      The time and date the template was created.
    """


_ClientListTemplatesResponseTypeDef = TypedDict(
    "_ClientListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List[ClientListTemplatesResponseTemplatesMetadataTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTemplatesResponseTypeDef(_ClientListTemplatesResponseTypeDef):
    """
    Type definition for `ClientListTemplates` `Response`

    - **TemplatesMetadata** *(list) --*

      An array the contains the name and creation time stamp for each template in your Amazon SES
      account.

      - *(dict) --*

        Contains information about an email template.

        - **Name** *(string) --*

          The name of the template.

        - **CreatedTimestamp** *(datetime) --*

          The time and date the template was created.

    - **NextToken** *(string) --*

      A token indicating that there are additional email templates available to be listed. Pass
      this token to a subsequent call to ``ListTemplates`` to retrieve the next 50 email templates.
    """


_ClientListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "_ClientListVerifiedEmailAddressesResponseTypeDef",
    {"VerifiedEmailAddresses": List[str]},
    total=False,
)


class ClientListVerifiedEmailAddressesResponseTypeDef(
    _ClientListVerifiedEmailAddressesResponseTypeDef
):
    """
    Type definition for `ClientListVerifiedEmailAddresses` `Response`

    A list of email addresses that you have verified with Amazon SES under your AWS account.

    - **VerifiedEmailAddresses** *(list) --*

      A list of email addresses that have been verified.

      - *(string) --*
    """


_ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef = TypedDict(
    "_ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    {"TlsPolicy": str},
    total=False,
)


class ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef(
    _ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef
):
    """
    Type definition for `ClientPutConfigurationSetDeliveryOptions` `DeliveryOptions`

    Specifies whether messages that use the configuration set are required to use Transport Layer
    Security (TLS).

    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport Layer
      Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS connection
      can be established. If the value is ``Optional`` , messages can be delivered in plain text if a
      TLS connection can't be established.
    """


_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef = TypedDict(
    "_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    {"Name": str, "Value": str},
)


class ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef(
    _ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef
):
    """
    Type definition for `ClientSendBounceBouncedRecipientInfoListRecipientDsnFields` `ExtensionFields`

    Additional X-headers to include in the Delivery Status Notification (DSN) when an email
    that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the `Amazon SES Developer
    Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the header to add. Must be less than 2048 characters, and must not contain
      newline characters ("\\r" or "\\n").
    """


_RequiredClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef = TypedDict(
    "_RequiredClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    {"Action": str, "Status": str},
)
_OptionalClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef = TypedDict(
    "_OptionalClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "RemoteMta": str,
        "DiagnosticCode": str,
        "LastAttemptDate": datetime,
        "ExtensionFields": List[
            ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef
        ],
    },
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef(
    _RequiredClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef,
    _OptionalClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef,
):
    """
    Type definition for `ClientSendBounceBouncedRecipientInfoList` `RecipientDsnFields`

    Recipient-related DSN fields, most of which would normally be filled in automatically when
    provided with a ``BounceType`` . You must provide either this parameter or ``BounceType`` .

    - **FinalRecipient** *(string) --*

      The email address that the message was ultimately delivered to. This corresponds to the
      ``Final-Recipient`` in the DSN. If not specified, ``FinalRecipient`` will be set to the
      ``Recipient`` specified in the ``BouncedRecipientInfo`` structure. Either
      ``FinalRecipient`` or the recipient in ``BouncedRecipientInfo`` must be a recipient of the
      original bounced message.

      .. note::

        Do not prepend the ``FinalRecipient`` email address with ``rfc 822;`` , as described in
        `RFC 3798 <https://tools.ietf.org/html/rfc3798>`__ .

    - **Action** *(string) --* **[REQUIRED]**

      The action performed by the reporting mail transfer agent (MTA) as a result of its attempt
      to deliver the message to the recipient address. This is required by `RFC 3464
      <https://tools.ietf.org/html/rfc3464>`__ .

    - **RemoteMta** *(string) --*

      The MTA to which the remote MTA attempted to deliver the message, formatted as specified in
      `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). This
      parameter typically applies only to propagating synchronous bounces.

    - **Status** *(string) --* **[REQUIRED]**

      The status code that indicates what went wrong. This is required by `RFC 3464
      <https://tools.ietf.org/html/rfc3464>`__ .

    - **DiagnosticCode** *(string) --*

      An extended explanation of what went wrong; this is usually an SMTP response. See `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ for the correct formatting of this parameter.

    - **LastAttemptDate** *(datetime) --*

      The time the final delivery attempt was made, in `RFC 822
      <https://www.ietf.org/rfc/rfc0822.txt>`__ date-time format.

    - **ExtensionFields** *(list) --*

      Additional X-headers to include in the DSN.

      - *(dict) --*

        Additional X-headers to include in the Delivery Status Notification (DSN) when an email
        that Amazon SES receives on your behalf bounces.

        For information about receiving email through Amazon SES, see the `Amazon SES Developer
        Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

        - **Name** *(string) --* **[REQUIRED]**

          The name of the header to add. Must be between 1 and 50 characters, inclusive, and
          consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the header to add. Must be less than 2048 characters, and must not contain
          newline characters ("\\r" or "\\n").
    """


_RequiredClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_RequiredClientSendBounceBouncedRecipientInfoListTypeDef", {"Recipient": str}
)
_OptionalClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_OptionalClientSendBounceBouncedRecipientInfoListTypeDef",
    {
        "RecipientArn": str,
        "BounceType": str,
        "RecipientDsnFields": ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef,
    },
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListTypeDef(
    _RequiredClientSendBounceBouncedRecipientInfoListTypeDef,
    _OptionalClientSendBounceBouncedRecipientInfoListTypeDef,
):
    """
    Type definition for `ClientSendBounce` `BouncedRecipientInfoList`

    Recipient-related information to include in the Delivery Status Notification (DSN) when an
    email that Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

    - **Recipient** *(string) --* **[REQUIRED]**

      The email address of the recipient of the bounced email.

    - **RecipientArn** *(string) --*

      This parameter is used only for sending authorization. It is the ARN of the identity that is
      associated with the sending authorization policy that permits you to receive email for the
      recipient of the bounced email. For more information about sending authorization, see the
      `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

    - **BounceType** *(string) --*

      The reason for the bounce. You must provide either this parameter or ``RecipientDsnFields`` .

    - **RecipientDsnFields** *(dict) --*

      Recipient-related DSN fields, most of which would normally be filled in automatically when
      provided with a ``BounceType`` . You must provide either this parameter or ``BounceType`` .

      - **FinalRecipient** *(string) --*

        The email address that the message was ultimately delivered to. This corresponds to the
        ``Final-Recipient`` in the DSN. If not specified, ``FinalRecipient`` will be set to the
        ``Recipient`` specified in the ``BouncedRecipientInfo`` structure. Either
        ``FinalRecipient`` or the recipient in ``BouncedRecipientInfo`` must be a recipient of the
        original bounced message.

        .. note::

          Do not prepend the ``FinalRecipient`` email address with ``rfc 822;`` , as described in
          `RFC 3798 <https://tools.ietf.org/html/rfc3798>`__ .

      - **Action** *(string) --* **[REQUIRED]**

        The action performed by the reporting mail transfer agent (MTA) as a result of its attempt
        to deliver the message to the recipient address. This is required by `RFC 3464
        <https://tools.ietf.org/html/rfc3464>`__ .

      - **RemoteMta** *(string) --*

        The MTA to which the remote MTA attempted to deliver the message, formatted as specified in
        `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). This
        parameter typically applies only to propagating synchronous bounces.

      - **Status** *(string) --* **[REQUIRED]**

        The status code that indicates what went wrong. This is required by `RFC 3464
        <https://tools.ietf.org/html/rfc3464>`__ .

      - **DiagnosticCode** *(string) --*

        An extended explanation of what went wrong; this is usually an SMTP response. See `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ for the correct formatting of this parameter.

      - **LastAttemptDate** *(datetime) --*

        The time the final delivery attempt was made, in `RFC 822
        <https://www.ietf.org/rfc/rfc0822.txt>`__ date-time format.

      - **ExtensionFields** *(list) --*

        Additional X-headers to include in the DSN.

        - *(dict) --*

          Additional X-headers to include in the Delivery Status Notification (DSN) when an email
          that Amazon SES receives on your behalf bounces.

          For information about receiving email through Amazon SES, see the `Amazon SES Developer
          Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

          - **Name** *(string) --* **[REQUIRED]**

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the header to add. Must be less than 2048 characters, and must not contain
            newline characters ("\\r" or "\\n").
    """


_ClientSendBounceMessageDsnExtensionFieldsTypeDef = TypedDict(
    "_ClientSendBounceMessageDsnExtensionFieldsTypeDef", {"Name": str, "Value": str}
)


class ClientSendBounceMessageDsnExtensionFieldsTypeDef(
    _ClientSendBounceMessageDsnExtensionFieldsTypeDef
):
    """
    Type definition for `ClientSendBounceMessageDsn` `ExtensionFields`

    Additional X-headers to include in the Delivery Status Notification (DSN) when an email that
    Amazon SES receives on your behalf bounces.

    For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist
      of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the header to add. Must be less than 2048 characters, and must not contain
      newline characters ("\\r" or "\\n").
    """


_RequiredClientSendBounceMessageDsnTypeDef = TypedDict(
    "_RequiredClientSendBounceMessageDsnTypeDef", {"ReportingMta": str}
)
_OptionalClientSendBounceMessageDsnTypeDef = TypedDict(
    "_OptionalClientSendBounceMessageDsnTypeDef",
    {
        "ArrivalDate": datetime,
        "ExtensionFields": List[ClientSendBounceMessageDsnExtensionFieldsTypeDef],
    },
    total=False,
)


class ClientSendBounceMessageDsnTypeDef(
    _RequiredClientSendBounceMessageDsnTypeDef,
    _OptionalClientSendBounceMessageDsnTypeDef,
):
    """
    Type definition for `ClientSendBounce` `MessageDsn`

    Message-related DSN fields. If not specified, Amazon SES will choose the values.

    - **ReportingMta** *(string) --* **[REQUIRED]**

      The reporting MTA that attempted to deliver the message, formatted as specified in `RFC 3464
      <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). The default value is
      ``dns; inbound-smtp.[region].amazonaws.com`` .

    - **ArrivalDate** *(datetime) --*

      When the message was received by the reporting mail transfer agent (MTA), in `RFC 822
      <https://www.ietf.org/rfc/rfc0822.txt>`__ date-time format.

    - **ExtensionFields** *(list) --*

      Additional X-headers to include in the DSN.

      - *(dict) --*

        Additional X-headers to include in the Delivery Status Notification (DSN) when an email that
        Amazon SES receives on your behalf bounces.

        For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

        - **Name** *(string) --* **[REQUIRED]**

          The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist
          of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the header to add. Must be less than 2048 characters, and must not contain
          newline characters ("\\r" or "\\n").
    """


_ClientSendBounceResponseTypeDef = TypedDict(
    "_ClientSendBounceResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendBounceResponseTypeDef(_ClientSendBounceResponseTypeDef):
    """
    Type definition for `ClientSendBounce` `Response`

    Represents a unique message ID.

    - **MessageId** *(string) --*

      The message ID of the bounce message.
    """


_ClientSendBulkTemplatedEmailDefaultTagsTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailDefaultTagsTypeDef", {"Name": str, "Value": str}
)


class ClientSendBulkTemplatedEmailDefaultTagsTypeDef(
    _ClientSendBulkTemplatedEmailDefaultTagsTypeDef
):
    """
    Type definition for `ClientSendBulkTemplatedEmail` `DefaultTags`

    Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
    to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email sending
    events. For information about using configuration sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the tag. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag. The value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.
    """


_ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef(
    _ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef
):
    """
    Type definition for `ClientSendBulkTemplatedEmailDestinations` `Destination`

    Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

    .. note::

      Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531
      <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a
      destination email address (the part of the email address that precedes the @ sign) may only
      contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__
      . If the *domain part* of an address (the part after the @ sign) contains non-ASCII
      characters, they must be encoded using Punycode, as described in `RFC3492
      <https://tools.ietf.org/html/rfc3492.html>`__ .

    - **ToAddresses** *(list) --*

      The recipients to place on the To: line of the message.

      - *(string) --*

    - **CcAddresses** *(list) --*

      The recipients to place on the CC: line of the message.

      - *(string) --*

    - **BccAddresses** *(list) --*

      The recipients to place on the BCC: line of the message.

      - *(string) --*
    """


_ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    {"Name": str, "Value": str},
)


class ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef(
    _ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef
):
    """
    Type definition for `ClientSendBulkTemplatedEmailDestinations` `ReplacementTags`

    Contains the name and value of a tag that you can provide to ``SendEmail`` or
    ``SendRawEmail`` to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email sending
    events. For information about using configuration sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the tag. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag. The value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.
    """


_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef",
    {"Destination": ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef},
)
_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef",
    {
        "ReplacementTags": List[
            ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef
        ],
        "ReplacementTemplateData": str,
    },
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsTypeDef(
    _RequiredClientSendBulkTemplatedEmailDestinationsTypeDef,
    _OptionalClientSendBulkTemplatedEmailDestinationsTypeDef,
):
    """
    Type definition for `ClientSendBulkTemplatedEmail` `Destinations`

    An array that contains one or more Destinations, as well as the tags and replacement data
    associated with each of those Destinations.

    - **Destination** *(dict) --* **[REQUIRED]**

      Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

      .. note::

        Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531
        <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a
        destination email address (the part of the email address that precedes the @ sign) may only
        contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__
        . If the *domain part* of an address (the part after the @ sign) contains non-ASCII
        characters, they must be encoded using Punycode, as described in `RFC3492
        <https://tools.ietf.org/html/rfc3492.html>`__ .

      - **ToAddresses** *(list) --*

        The recipients to place on the To: line of the message.

        - *(string) --*

      - **CcAddresses** *(list) --*

        The recipients to place on the CC: line of the message.

        - *(string) --*

      - **BccAddresses** *(list) --*

        The recipients to place on the BCC: line of the message.

        - *(string) --*

    - **ReplacementTags** *(list) --*

      A list of tags, in the form of name/value pairs, to apply to an email that you send using
      ``SendBulkTemplatedEmail`` . Tags correspond to characteristics of the email that you define,
      so that you can publish email sending events.

      - *(dict) --*

        Contains the name and value of a tag that you can provide to ``SendEmail`` or
        ``SendRawEmail`` to apply to an email.

        Message tags, which you use with configuration sets, enable you to publish email sending
        events. For information about using configuration sets, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        - **Name** *(string) --* **[REQUIRED]**

          The name of the tag. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the tag. The value must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.

    - **ReplacementTemplateData** *(string) --*

      A list of replacement values to apply to the template. This parameter is a JSON object,
      typically consisting of key-value pairs in which the keys correspond to replacement tags in
      the email template.
    """


_ClientSendBulkTemplatedEmailResponseStatusTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    {"Status": str, "Error": str, "MessageId": str},
    total=False,
)


class ClientSendBulkTemplatedEmailResponseStatusTypeDef(
    _ClientSendBulkTemplatedEmailResponseStatusTypeDef
):
    """
    Type definition for `ClientSendBulkTemplatedEmailResponse` `Status`

    An object that contains the response from the ``SendBulkTemplatedEmail`` operation.

    - **Status** *(string) --*

      The status of a message sent using the ``SendBulkTemplatedEmail`` operation.

      Possible values for this parameter include:

      * ``Success`` : Amazon SES accepted the message, and will attempt to deliver it to the
      recipients.

      * ``MessageRejected`` : The message was rejected because it contained a virus.

      * ``MailFromDomainNotVerified`` : The sender's email address or domain was not verified.

      * ``ConfigurationSetDoesNotExist`` : The configuration set you specified does not exist.

      * ``TemplateDoesNotExist`` : The template you specified does not exist.

      * ``AccountSuspended`` : Your account has been shut down because of issues related to
      your email sending practices.

      * ``AccountThrottled`` : The number of emails you can send has been reduced because your
      account has exceeded its allocated sending limit.

      * ``AccountDailyQuotaExceeded`` : You have reached or exceeded the maximum number of
      emails you can send from your account in a 24-hour period.

      * ``InvalidSendingPoolName`` : The configuration set you specified refers to an IP pool
      that does not exist.

      * ``AccountSendingPaused`` : Email sending for the Amazon SES account was disabled using
      the  UpdateAccountSendingEnabled operation.

      * ``ConfigurationSetSendingPaused`` : Email sending for this configuration set was
      disabled using the  UpdateConfigurationSetSendingEnabled operation.

      * ``InvalidParameterValue`` : One or more of the parameters you specified when calling
      this operation was invalid. See the error message for additional information.

      * ``TransientFailure`` : Amazon SES was unable to process your request because of a
      temporary issue.

      * ``Failed`` : Amazon SES was unable to process your request. See the error message for
      additional information.

    - **Error** *(string) --*

      A description of an error that prevented a message being sent using the
      ``SendBulkTemplatedEmail`` operation.

    - **MessageId** *(string) --*

      The unique message identifier returned from the ``SendBulkTemplatedEmail`` operation.
    """


_ClientSendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailResponseTypeDef",
    {"Status": List[ClientSendBulkTemplatedEmailResponseStatusTypeDef]},
    total=False,
)


class ClientSendBulkTemplatedEmailResponseTypeDef(
    _ClientSendBulkTemplatedEmailResponseTypeDef
):
    """
    Type definition for `ClientSendBulkTemplatedEmail` `Response`

    - **Status** *(list) --*

      The unique message identifier returned from the ``SendBulkTemplatedEmail`` action.

      - *(dict) --*

        An object that contains the response from the ``SendBulkTemplatedEmail`` operation.

        - **Status** *(string) --*

          The status of a message sent using the ``SendBulkTemplatedEmail`` operation.

          Possible values for this parameter include:

          * ``Success`` : Amazon SES accepted the message, and will attempt to deliver it to the
          recipients.

          * ``MessageRejected`` : The message was rejected because it contained a virus.

          * ``MailFromDomainNotVerified`` : The sender's email address or domain was not verified.

          * ``ConfigurationSetDoesNotExist`` : The configuration set you specified does not exist.

          * ``TemplateDoesNotExist`` : The template you specified does not exist.

          * ``AccountSuspended`` : Your account has been shut down because of issues related to
          your email sending practices.

          * ``AccountThrottled`` : The number of emails you can send has been reduced because your
          account has exceeded its allocated sending limit.

          * ``AccountDailyQuotaExceeded`` : You have reached or exceeded the maximum number of
          emails you can send from your account in a 24-hour period.

          * ``InvalidSendingPoolName`` : The configuration set you specified refers to an IP pool
          that does not exist.

          * ``AccountSendingPaused`` : Email sending for the Amazon SES account was disabled using
          the  UpdateAccountSendingEnabled operation.

          * ``ConfigurationSetSendingPaused`` : Email sending for this configuration set was
          disabled using the  UpdateConfigurationSetSendingEnabled operation.

          * ``InvalidParameterValue`` : One or more of the parameters you specified when calling
          this operation was invalid. See the error message for additional information.

          * ``TransientFailure`` : Amazon SES was unable to process your request because of a
          temporary issue.

          * ``Failed`` : Amazon SES was unable to process your request. See the error message for
          additional information.

        - **Error** *(string) --*

          A description of an error that prevented a message being sent using the
          ``SendBulkTemplatedEmail`` operation.

        - **MessageId** *(string) --*

          The unique message identifier returned from the ``SendBulkTemplatedEmail`` operation.
    """


_ClientSendCustomVerificationEmailResponseTypeDef = TypedDict(
    "_ClientSendCustomVerificationEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendCustomVerificationEmailResponseTypeDef(
    _ClientSendCustomVerificationEmailResponseTypeDef
):
    """
    Type definition for `ClientSendCustomVerificationEmail` `Response`

    The response received when attempting to send the custom verification email.

    - **MessageId** *(string) --*

      The unique message identifier returned from the ``SendCustomVerificationEmail`` operation.
    """


_ClientSendEmailDestinationTypeDef = TypedDict(
    "_ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendEmailDestinationTypeDef(_ClientSendEmailDestinationTypeDef):
    """
    Type definition for `ClientSendEmail` `Destination`

    The destination for this email, composed of To:, CC:, and BCC: fields.

    - **ToAddresses** *(list) --*

      The recipients to place on the To: line of the message.

      - *(string) --*

    - **CcAddresses** *(list) --*

      The recipients to place on the CC: line of the message.

      - *(string) --*

    - **BccAddresses** *(list) --*

      The recipients to place on the BCC: line of the message.

      - *(string) --*
    """


_RequiredClientSendEmailMessageBodyHtmlTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageBodyHtmlTypeDef", {"Data": str}
)
_OptionalClientSendEmailMessageBodyHtmlTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageBodyHtmlTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailMessageBodyHtmlTypeDef(
    _RequiredClientSendEmailMessageBodyHtmlTypeDef,
    _OptionalClientSendEmailMessageBodyHtmlTypeDef,
):
    """
    Type definition for `ClientSendEmailMessageBody` `Html`

    The content of the message, in HTML format. Use this for email clients that can process HTML.
    You can include clickable links, formatted text, and much more in an HTML message.

    - **Data** *(string) --* **[REQUIRED]**

      The textual data of the content.

    - **Charset** *(string) --*

      The character set of the content.
    """


_RequiredClientSendEmailMessageBodyTextTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageBodyTextTypeDef", {"Data": str}
)
_OptionalClientSendEmailMessageBodyTextTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageBodyTextTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailMessageBodyTextTypeDef(
    _RequiredClientSendEmailMessageBodyTextTypeDef,
    _OptionalClientSendEmailMessageBodyTextTypeDef,
):
    """
    Type definition for `ClientSendEmailMessageBody` `Text`

    The content of the message, in text format. Use this for text-based email clients, or clients
    on high-latency networks (such as mobile devices).

    - **Data** *(string) --* **[REQUIRED]**

      The textual data of the content.

    - **Charset** *(string) --*

      The character set of the content.
    """


_ClientSendEmailMessageBodyTypeDef = TypedDict(
    "_ClientSendEmailMessageBodyTypeDef",
    {
        "Text": ClientSendEmailMessageBodyTextTypeDef,
        "Html": ClientSendEmailMessageBodyHtmlTypeDef,
    },
    total=False,
)


class ClientSendEmailMessageBodyTypeDef(_ClientSendEmailMessageBodyTypeDef):
    """
    Type definition for `ClientSendEmailMessage` `Body`

    The message body.

    - **Text** *(dict) --*

      The content of the message, in text format. Use this for text-based email clients, or clients
      on high-latency networks (such as mobile devices).

      - **Data** *(string) --* **[REQUIRED]**

        The textual data of the content.

      - **Charset** *(string) --*

        The character set of the content.

    - **Html** *(dict) --*

      The content of the message, in HTML format. Use this for email clients that can process HTML.
      You can include clickable links, formatted text, and much more in an HTML message.

      - **Data** *(string) --* **[REQUIRED]**

        The textual data of the content.

      - **Charset** *(string) --*

        The character set of the content.
    """


_RequiredClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailMessageSubjectTypeDef(
    _RequiredClientSendEmailMessageSubjectTypeDef,
    _OptionalClientSendEmailMessageSubjectTypeDef,
):
    """
    Type definition for `ClientSendEmailMessage` `Subject`

    The subject of the message: A short summary of the content, which will appear in the
    recipient's inbox.

    - **Data** *(string) --* **[REQUIRED]**

      The textual data of the content.

    - **Charset** *(string) --*

      The character set of the content.
    """


_ClientSendEmailMessageTypeDef = TypedDict(
    "_ClientSendEmailMessageTypeDef",
    {
        "Subject": ClientSendEmailMessageSubjectTypeDef,
        "Body": ClientSendEmailMessageBodyTypeDef,
    },
)


class ClientSendEmailMessageTypeDef(_ClientSendEmailMessageTypeDef):
    """
    Type definition for `ClientSendEmail` `Message`

    The message to be sent.

    - **Subject** *(dict) --* **[REQUIRED]**

      The subject of the message: A short summary of the content, which will appear in the
      recipient's inbox.

      - **Data** *(string) --* **[REQUIRED]**

        The textual data of the content.

      - **Charset** *(string) --*

        The character set of the content.

    - **Body** *(dict) --* **[REQUIRED]**

      The message body.

      - **Text** *(dict) --*

        The content of the message, in text format. Use this for text-based email clients, or clients
        on high-latency networks (such as mobile devices).

        - **Data** *(string) --* **[REQUIRED]**

          The textual data of the content.

        - **Charset** *(string) --*

          The character set of the content.

      - **Html** *(dict) --*

        The content of the message, in HTML format. Use this for email clients that can process HTML.
        You can include clickable links, formatted text, and much more in an HTML message.

        - **Data** *(string) --* **[REQUIRED]**

          The textual data of the content.

        - **Charset** *(string) --*

          The character set of the content.
    """


_ClientSendEmailResponseTypeDef = TypedDict(
    "_ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendEmailResponseTypeDef(_ClientSendEmailResponseTypeDef):
    """
    Type definition for `ClientSendEmail` `Response`

    Represents a unique message ID.

    - **MessageId** *(string) --*

      The unique message identifier returned from the ``SendEmail`` action.
    """


_ClientSendEmailTagsTypeDef = TypedDict(
    "_ClientSendEmailTagsTypeDef", {"Name": str, "Value": str}
)


class ClientSendEmailTagsTypeDef(_ClientSendEmailTagsTypeDef):
    """
    Type definition for `ClientSendEmail` `Tags`

    Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
    to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email sending
    events. For information about using configuration sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the tag. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag. The value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.
    """


_ClientSendRawEmailRawMessageTypeDef = TypedDict(
    "_ClientSendRawEmailRawMessageTypeDef", {"Data": bytes}
)


class ClientSendRawEmailRawMessageTypeDef(_ClientSendRawEmailRawMessageTypeDef):
    """
    Type definition for `ClientSendRawEmail` `RawMessage`

    The raw email message itself. The message has to meet the following criteria:

    * The message has to contain a header and a body, separated by a blank line.

    * All of the required header fields must be present in the message.

    * Each part of a multipart MIME message must be formatted properly.

    * Attachments must be of a content type that Amazon SES supports. For a list on unsupported
    content types, see `Unsupported Attachment Types
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types.html>`__ in the *Amazon SES
    Developer Guide* .

    * The entire message must be base64-encoded.

    * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
    character range, we highly recommend that you encode that content. For more information, see
    `Sending Raw Email <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html>`__
    in the *Amazon SES Developer Guide* .

    * Per `RFC 5321 <https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6>`__ , the maximum length
    of each line of text, including the <CRLF>, must not exceed 1,000 characters.

    - **Data** *(bytes) --* **[REQUIRED]**

      The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES
      directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK
      takes care of the base 64-encoding for you. In all cases, the client must ensure that the
      message format complies with Internet email standards regarding email header fields, MIME
      types, and MIME encoding.

      The To:, CC:, and BCC: headers in the raw message can contain a group list.

      If you are using ``SendRawEmail`` with sending authorization, you can include X-headers in the
      raw message to specify the "Source," "From," and "Return-Path" addresses. For more information,
      see the documentation for ``SendRawEmail`` .

      .. warning::

        Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES
        before sending the email.

      For more information, go to the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html>`__ .
    """


_ClientSendRawEmailResponseTypeDef = TypedDict(
    "_ClientSendRawEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendRawEmailResponseTypeDef(_ClientSendRawEmailResponseTypeDef):
    """
    Type definition for `ClientSendRawEmail` `Response`

    Represents a unique message ID.

    - **MessageId** *(string) --*

      The unique message identifier returned from the ``SendRawEmail`` action.
    """


_ClientSendRawEmailTagsTypeDef = TypedDict(
    "_ClientSendRawEmailTagsTypeDef", {"Name": str, "Value": str}
)


class ClientSendRawEmailTagsTypeDef(_ClientSendRawEmailTagsTypeDef):
    """
    Type definition for `ClientSendRawEmail` `Tags`

    Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
    to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email sending
    events. For information about using configuration sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the tag. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag. The value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.
    """


_ClientSendTemplatedEmailDestinationTypeDef = TypedDict(
    "_ClientSendTemplatedEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendTemplatedEmailDestinationTypeDef(
    _ClientSendTemplatedEmailDestinationTypeDef
):
    """
    Type definition for `ClientSendTemplatedEmail` `Destination`

    The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include
    up to 50 recipients across these three fields.

    - **ToAddresses** *(list) --*

      The recipients to place on the To: line of the message.

      - *(string) --*

    - **CcAddresses** *(list) --*

      The recipients to place on the CC: line of the message.

      - *(string) --*

    - **BccAddresses** *(list) --*

      The recipients to place on the BCC: line of the message.

      - *(string) --*
    """


_ClientSendTemplatedEmailResponseTypeDef = TypedDict(
    "_ClientSendTemplatedEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendTemplatedEmailResponseTypeDef(_ClientSendTemplatedEmailResponseTypeDef):
    """
    Type definition for `ClientSendTemplatedEmail` `Response`

    - **MessageId** *(string) --*

      The unique message identifier returned from the ``SendTemplatedEmail`` action.
    """


_ClientSendTemplatedEmailTagsTypeDef = TypedDict(
    "_ClientSendTemplatedEmailTagsTypeDef", {"Name": str, "Value": str}
)


class ClientSendTemplatedEmailTagsTypeDef(_ClientSendTemplatedEmailTagsTypeDef):
    """
    Type definition for `ClientSendTemplatedEmail` `Tags`

    Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
    to apply to an email.

    Message tags, which you use with configuration sets, enable you to publish email sending
    events. For information about using configuration sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the tag. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag. The value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 256 characters.
    """


_ClientTestRenderTemplateResponseTypeDef = TypedDict(
    "_ClientTestRenderTemplateResponseTypeDef", {"RenderedTemplate": str}, total=False
)


class ClientTestRenderTemplateResponseTypeDef(_ClientTestRenderTemplateResponseTypeDef):
    """
    Type definition for `ClientTestRenderTemplate` `Response`

    - **RenderedTemplate** *(string) --*

      The complete MIME message rendered by applying the data in the TemplateData parameter to the
      template specified in the TemplateName parameter.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {"DimensionName": str, "DimensionValueSource": str, "DefaultDimensionValue": str},
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestination` `DimensionConfigurations`

    Contains the dimension configuration to use when you publish email sending events to Amazon
    CloudWatch.

    For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
    SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **DimensionName** *(string) --* **[REQUIRED]**

      The name of an Amazon CloudWatch dimension associated with an email sending metric. The
      name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.

    - **DimensionValueSource** *(string) --* **[REQUIRED]**

      The place where Amazon SES finds the value of a dimension to publish to Amazon
      CloudWatch. If you want Amazon SES to use the message tags that you specify using an
      ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
      choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
      ``emailHeader`` .

    - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

      The default value of the dimension that is published to Amazon CloudWatch if you do not
      provide the value of the dimension when you send an email. The default value must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Contain less than 256 characters.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `CloudWatchDestination`

    An object that contains the names, default values, and sources of the dimensions associated
    with an Amazon CloudWatch event destination.

    - **DimensionConfigurations** *(list) --* **[REQUIRED]**

      A list of dimensions upon which to categorize your emails when you publish email sending
      events to Amazon CloudWatch.

      - *(dict) --*

        Contains the dimension configuration to use when you publish email sending events to Amazon
        CloudWatch.

        For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
        SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        - **DimensionName** *(string) --* **[REQUIRED]**

          The name of an Amazon CloudWatch dimension associated with an email sending metric. The
          name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.

        - **DimensionValueSource** *(string) --* **[REQUIRED]**

          The place where Amazon SES finds the value of a dimension to publish to Amazon
          CloudWatch. If you want Amazon SES to use the message tags that you specify using an
          ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
          choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
          ``emailHeader`` .

        - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

          The default value of the dimension that is published to Amazon CloudWatch if you do not
          provide the value of the dimension when you send an email. The default value must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Contain less than 256 characters.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `KinesisFirehoseDestination`

    An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon
    Kinesis Firehose event destination.

    - **IAMRoleARN** *(string) --* **[REQUIRED]**

      The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon
      Kinesis Firehose stream.

    - **DeliveryStreamARN** *(string) --* **[REQUIRED]**

      The ARN of the Amazon Kinesis Firehose stream that email sending events should be published
      to.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `SNSDestination`

    An object that contains the topic ARN associated with an Amazon Simple Notification Service
    (Amazon SNS) event destination.

    - **TopicARN** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS topic that email sending events will be published to. An example of
      an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
      information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {"Name": str, "MatchingEventTypes": List[str]},
)
_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestination` `EventDestination`

    The event destination object that you want to apply to the specified configuration set.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the event destination. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      Sets whether Amazon SES publishes events to this destination when you send an email with the
      associated configuration set. Set to ``true`` to enable publishing to this destination; set to
      ``false`` to prevent publishing to this destination. The default value is ``false`` .

    - **MatchingEventTypes** *(list) --* **[REQUIRED]**

      The type of email sending events to publish to the event destination.

      - *(string) --*

    - **KinesisFirehoseDestination** *(dict) --*

      An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon
      Kinesis Firehose event destination.

      - **IAMRoleARN** *(string) --* **[REQUIRED]**

        The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon
        Kinesis Firehose stream.

      - **DeliveryStreamARN** *(string) --* **[REQUIRED]**

        The ARN of the Amazon Kinesis Firehose stream that email sending events should be published
        to.

    - **CloudWatchDestination** *(dict) --*

      An object that contains the names, default values, and sources of the dimensions associated
      with an Amazon CloudWatch event destination.

      - **DimensionConfigurations** *(list) --* **[REQUIRED]**

        A list of dimensions upon which to categorize your emails when you publish email sending
        events to Amazon CloudWatch.

        - *(dict) --*

          Contains the dimension configuration to use when you publish email sending events to Amazon
          CloudWatch.

          For information about publishing email sending events to Amazon CloudWatch, see the `Amazon
          SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

          - **DimensionName** *(string) --* **[REQUIRED]**

            The name of an Amazon CloudWatch dimension associated with an email sending metric. The
            name must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).

            * Contain less than 256 characters.

          - **DimensionValueSource** *(string) --* **[REQUIRED]**

            The place where Amazon SES finds the value of a dimension to publish to Amazon
            CloudWatch. If you want Amazon SES to use the message tags that you specify using an
            ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API,
            choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose
            ``emailHeader`` .

          - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

            The default value of the dimension that is published to Amazon CloudWatch if you do not
            provide the value of the dimension when you send an email. The default value must:

            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).

            * Contain less than 256 characters.

    - **SNSDestination** *(dict) --*

      An object that contains the topic ARN associated with an Amazon Simple Notification Service
      (Amazon SNS) event destination.

      - **TopicARN** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS topic that email sending events will be published to. An example of
        an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more
        information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef(
    _ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetTrackingOptions` `TrackingOptions`

    A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain
    captures open and click events generated by Amazon SES emails.

    For more information, see `Configuring Custom Domains to Handle Open and Click Tracking
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__
    in the *Amazon SES Developer Guide* .

    - **CustomRedirectDomain** *(string) --*

      The custom subdomain that will be used to redirect email recipients to the Amazon SES event
      tracking domain.
    """


_ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
)


class ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `AddHeaderAction`

    Adds a header to the received email.

    - **HeaderName** *(string) --* **[REQUIRED]**

      The name of the header to add. Must be between 1 and 50 characters, inclusive, and
      consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

    - **HeaderValue** *(string) --* **[REQUIRED]**

      Must be less than 2048 characters, and must not contain newline characters ("\\r" or
      "\\n").
    """


_RequiredClientUpdateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    {"SmtpReplyCode": str, "Message": str, "Sender": str},
)
_OptionalClientUpdateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "StatusCode": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsBounceActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsBounceActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `BounceAction`

    Rejects the received email by returning a bounce response to the sender and, optionally,
    publishes a notification to Amazon Simple Notification Service (Amazon SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
      is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **SmtpReplyCode** *(string) --* **[REQUIRED]**

      The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **StatusCode** *(string) --*

      The SMTP enhanced status code, as defined by `RFC 3463
      <https://tools.ietf.org/html/rfc3463>`__ .

    - **Message** *(string) --* **[REQUIRED]**

      Human-readable text to include in the bounce message.

    - **Sender** *(string) --* **[REQUIRED]**

      The email address of the sender of the bounced email. This is the address from which the
      bounce message will be sent.
    """


_RequiredClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"FunctionArn": str},
)
_OptionalClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "InvocationType": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `LambdaAction`

    Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
      is taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **FunctionArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
      function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
      information about AWS Lambda, see the `AWS Lambda Developer Guide
      <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

    - **InvocationType** *(string) --*

      The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
      means that the execution of the function will immediately result in a response, and a
      value of ``Event`` means that the function will be invoked asynchronously. The default
      value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
      Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

      .. warning::

        There is a 30-second timeout on ``RequestResponse`` invocations. You should use
        ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
        a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
    """


_RequiredClientUpdateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsS3ActionTypeDef", {"BucketName": str}
)
_OptionalClientUpdateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsS3ActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsS3ActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `S3Action`

    Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
    optionally, publishes a notification to Amazon SNS.

    - **TopicArn** *(string) --*

      The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
      bucket. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **BucketName** *(string) --* **[REQUIRED]**

      The name of the Amazon S3 bucket that incoming email will be saved to.

    - **ObjectKeyPrefix** *(string) --*

      The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
      that enables you to store similar data under the same directory in a bucket.

    - **KmsKeyArn** *(string) --*

      The customer master key that Amazon SES should use to encrypt your emails before saving
      them to the Amazon S3 bucket. You can use the default master key or a custom master key
      you created in AWS KMS as follows:

      * To use the default master key, provide an ARN in the form of
      ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
      AWS account ID is 123456789012 and you want to use the default master key in the US West
      (Oregon) region, the ARN of the default master key would be
      ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
      you don't need to perform any extra steps to give Amazon SES permission to use the key.

      * To use a custom master key you created in AWS KMS, provide the ARN of the master key
      and ensure that you add a statement to your key's policy to give Amazon SES permission to
      use it. For more information about giving permissions, see the `Amazon SES Developer
      Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
      .

      For more information about key policies, see the `AWS KMS Developer Guide
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
      specify a master key, Amazon SES will not encrypt your emails.

      .. warning::

        Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
        mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
        server-side encryption. This means that you must use the Amazon S3 encryption client to
        decrypt the email after retrieving it from Amazon S3, as the service has no access to
        use your AWS KMS keys for decryption. This encryption client is currently available
        with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
        Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
        client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .
    """


_RequiredClientUpdateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsSNSActionTypeDef", {"TopicArn": str}
)
_OptionalClientUpdateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    {"Encoding": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsSNSActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsSNSActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `SNSAction`

    Publishes the email content within a notification to Amazon SNS.

    - **TopicArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
      SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
      about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **Encoding** *(string) --*

      The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
      use, but may not preserve all special characters when a message was encoded with a
      different encoding format. Base64 preserves all special characters. The default value is
      UTF-8.
    """


_RequiredClientUpdateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsStopActionTypeDef", {"Scope": str}
)
_OptionalClientUpdateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsStopActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsStopActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsStopActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `StopAction`

    Terminates the evaluation of the receipt rule set and optionally publishes a notification
    to Amazon SNS.

    - **Scope** *(string) --* **[REQUIRED]**

      The scope of the StopAction. The only acceptable value is ``RuleSet`` .

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
      taken. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_RequiredClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"OrganizationArn": str},
)
_OptionalClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef(
    _RequiredClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef,
    _OptionalClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRuleRuleActions` `WorkmailAction`

    Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
      is called. An example of an Amazon SNS topic ARN is
      ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
      topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **OrganizationArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
      organization ARN is
      ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
      . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
      Administrator Guide
      <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .
    """


_ClientUpdateReceiptRuleRuleActionsTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientUpdateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsTypeDef(
    _ClientUpdateReceiptRuleRuleActionsTypeDef
):
    """
    Type definition for `ClientUpdateReceiptRuleRule` `Actions`

    An action that Amazon SES can take when it receives an email on behalf of one or more email
    addresses or domains that you own. An instance of this data type can represent only one
    action.

    For information about setting up receipt rules, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
    .

    - **S3Action** *(dict) --*

      Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
      optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
        bucket. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **BucketName** *(string) --* **[REQUIRED]**

        The name of the Amazon S3 bucket that incoming email will be saved to.

      - **ObjectKeyPrefix** *(string) --*

        The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
        that enables you to store similar data under the same directory in a bucket.

      - **KmsKeyArn** *(string) --*

        The customer master key that Amazon SES should use to encrypt your emails before saving
        them to the Amazon S3 bucket. You can use the default master key or a custom master key
        you created in AWS KMS as follows:

        * To use the default master key, provide an ARN in the form of
        ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
        AWS account ID is 123456789012 and you want to use the default master key in the US West
        (Oregon) region, the ARN of the default master key would be
        ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
        you don't need to perform any extra steps to give Amazon SES permission to use the key.

        * To use a custom master key you created in AWS KMS, provide the ARN of the master key
        and ensure that you add a statement to your key's policy to give Amazon SES permission to
        use it. For more information about giving permissions, see the `Amazon SES Developer
        Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
        .

        For more information about key policies, see the `AWS KMS Developer Guide
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
        specify a master key, Amazon SES will not encrypt your emails.

        .. warning::

          Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
          mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
          server-side encryption. This means that you must use the Amazon S3 encryption client to
          decrypt the email after retrieving it from Amazon S3, as the service has no access to
          use your AWS KMS keys for decryption. This encryption client is currently available
          with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
          Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
          client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

    - **BounceAction** *(dict) --*

      Rejects the received email by returning a bounce response to the sender and, optionally,
      publishes a notification to Amazon Simple Notification Service (Amazon SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
        is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **SmtpReplyCode** *(string) --* **[REQUIRED]**

        The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

      - **StatusCode** *(string) --*

        The SMTP enhanced status code, as defined by `RFC 3463
        <https://tools.ietf.org/html/rfc3463>`__ .

      - **Message** *(string) --* **[REQUIRED]**

        Human-readable text to include in the bounce message.

      - **Sender** *(string) --* **[REQUIRED]**

        The email address of the sender of the bounced email. This is the address from which the
        bounce message will be sent.

    - **WorkmailAction** *(dict) --*

      Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
        is called. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **OrganizationArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
        organization ARN is
        ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
        . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
        Administrator Guide
        <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

    - **LambdaAction** *(dict) --*

      Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
        is taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **FunctionArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
        function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
        information about AWS Lambda, see the `AWS Lambda Developer Guide
        <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

      - **InvocationType** *(string) --*

        The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
        means that the execution of the function will immediately result in a response, and a
        value of ``Event`` means that the function will be invoked asynchronously. The default
        value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
        Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

        .. warning::

          There is a 30-second timeout on ``RequestResponse`` invocations. You should use
          ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
          a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

    - **StopAction** *(dict) --*

      Terminates the evaluation of the receipt rule set and optionally publishes a notification
      to Amazon SNS.

      - **Scope** *(string) --* **[REQUIRED]**

        The scope of the StopAction. The only acceptable value is ``RuleSet`` .

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
        taken. An example of an Amazon SNS topic ARN is
        ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
        topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **AddHeaderAction** *(dict) --*

      Adds a header to the received email.

      - **HeaderName** *(string) --* **[REQUIRED]**

        The name of the header to add. Must be between 1 and 50 characters, inclusive, and
        consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

      - **HeaderValue** *(string) --* **[REQUIRED]**

        Must be less than 2048 characters, and must not contain newline characters ("\\r" or
        "\\n").

    - **SNSAction** *(dict) --*

      Publishes the email content within a notification to Amazon SNS.

      - **TopicArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
        SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
        about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

      - **Encoding** *(string) --*

        The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
        use, but may not preserve all special characters when a message was encoded with a
        different encoding format. Base64 preserves all special characters. The default value is
        UTF-8.
    """


_RequiredClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": str,
        "Recipients": List[str],
        "Actions": List[ClientUpdateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientUpdateReceiptRuleRuleTypeDef(
    _RequiredClientUpdateReceiptRuleRuleTypeDef,
    _OptionalClientUpdateReceiptRuleRuleTypeDef,
):
    """
    Type definition for `ClientUpdateReceiptRule` `Rule`

    A data structure that contains the updated receipt rule information.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the receipt rule. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **Enabled** *(boolean) --*

      If ``true`` , the receipt rule is active. The default value is ``false`` .

    - **TlsPolicy** *(string) --*

      Specifies whether Amazon SES should require that incoming email is delivered over a connection
      encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon
      SES will bounce emails that are not received over TLS. The default is ``Optional`` .

    - **Recipients** *(list) --*

      The recipient domains and email addresses that the receipt rule applies to. If this field is
      not specified, this rule will match all recipients under all verified domains.

      - *(string) --*

    - **Actions** *(list) --*

      An ordered list of actions to perform on messages that match at least one of the recipient
      email addresses or domains specified in the receipt rule.

      - *(dict) --*

        An action that Amazon SES can take when it receives an email on behalf of one or more email
        addresses or domains that you own. An instance of this data type can represent only one
        action.

        For information about setting up receipt rules, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__
        .

        - **S3Action** *(dict) --*

          Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and,
          optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3
            bucket. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **BucketName** *(string) --* **[REQUIRED]**

            The name of the Amazon S3 bucket that incoming email will be saved to.

          - **ObjectKeyPrefix** *(string) --*

            The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name
            that enables you to store similar data under the same directory in a bucket.

          - **KmsKeyArn** *(string) --*

            The customer master key that Amazon SES should use to encrypt your emails before saving
            them to the Amazon S3 bucket. You can use the default master key or a custom master key
            you created in AWS KMS as follows:

            * To use the default master key, provide an ARN in the form of
            ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your
            AWS account ID is 123456789012 and you want to use the default master key in the US West
            (Oregon) region, the ARN of the default master key would be
            ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key,
            you don't need to perform any extra steps to give Amazon SES permission to use the key.

            * To use a custom master key you created in AWS KMS, provide the ARN of the master key
            and ensure that you add a statement to your key's policy to give Amazon SES permission to
            use it. For more information about giving permissions, see the `Amazon SES Developer
            Guide
            <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__
            .

            For more information about key policies, see the `AWS KMS Developer Guide
            <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not
            specify a master key, Amazon SES will not encrypt your emails.

            .. warning::

              Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the
              mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3
              server-side encryption. This means that you must use the Amazon S3 encryption client to
              decrypt the email after retrieving it from Amazon S3, as the service has no access to
              use your AWS KMS keys for decryption. This encryption client is currently available
              with the `AWS SDK for Java <http://aws.amazon.com/sdk-for-java/>`__ and `AWS SDK for
              Ruby <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about
              client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

        - **BounceAction** *(dict) --*

          Rejects the received email by returning a bounce response to the sender and, optionally,
          publishes a notification to Amazon Simple Notification Service (Amazon SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action
            is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **SmtpReplyCode** *(string) --* **[REQUIRED]**

            The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

          - **StatusCode** *(string) --*

            The SMTP enhanced status code, as defined by `RFC 3463
            <https://tools.ietf.org/html/rfc3463>`__ .

          - **Message** *(string) --* **[REQUIRED]**

            Human-readable text to include in the bounce message.

          - **Sender** *(string) --* **[REQUIRED]**

            The email address of the sender of the bounced email. This is the address from which the
            bounce message will be sent.

        - **WorkmailAction** *(dict) --*

          Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action
            is called. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **OrganizationArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail
            organization ARN is
            ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7``
            . For information about Amazon WorkMail organizations, see the `Amazon WorkMail
            Administrator Guide
            <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

        - **LambdaAction** *(dict) --*

          Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action
            is taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **FunctionArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda
            function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more
            information about AWS Lambda, see the `AWS Lambda Developer Guide
            <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

          - **InvocationType** *(string) --*

            The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse``
            means that the execution of the function will immediately result in a response, and a
            value of ``Event`` means that the function will be invoked asynchronously. The default
            value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS
            Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

            .. warning::

              There is a 30-second timeout on ``RequestResponse`` invocations. You should use
              ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make
              a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

        - **StopAction** *(dict) --*

          Terminates the evaluation of the receipt rule set and optionally publishes a notification
          to Amazon SNS.

          - **Scope** *(string) --* **[REQUIRED]**

            The scope of the StopAction. The only acceptable value is ``RuleSet`` .

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is
            taken. An example of an Amazon SNS topic ARN is
            ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS
            topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **AddHeaderAction** *(dict) --*

          Adds a header to the received email.

          - **HeaderName** *(string) --* **[REQUIRED]**

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and
            consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

          - **HeaderValue** *(string) --* **[REQUIRED]**

            Must be less than 2048 characters, and must not contain newline characters ("\\r" or
            "\\n").

        - **SNSAction** *(dict) --*

          Publishes the email content within a notification to Amazon SNS.

          - **TopicArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon
            SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information
            about Amazon SNS topics, see the `Amazon SNS Developer Guide
            <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          - **Encoding** *(string) --*

            The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to
            use, but may not preserve all special characters when a message was encoded with a
            different encoding format. Base64 preserves all special characters. The default value is
            UTF-8.

    - **ScanEnabled** *(boolean) --*

      If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses.
      The default value is ``false`` .
    """


_RequiredClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientUpdateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientUpdateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientUpdateTemplateTemplateTypeDef(
    _RequiredClientUpdateTemplateTemplateTypeDef,
    _OptionalClientUpdateTemplateTemplateTypeDef,
):
    """
    Type definition for `ClientUpdateTemplate` `Template`

    The content of the email, composed of a subject line, an HTML part, and a text-only part.

    - **TemplateName** *(string) --* **[REQUIRED]**

      The name of the template. You will refer to this name when you send email using the
      ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

    - **SubjectPart** *(string) --*

      The subject line of the email.

    - **TextPart** *(string) --*

      The email body that will be visible to recipients whose email clients do not display HTML.

    - **HtmlPart** *(string) --*

      The HTML body of the email.
    """


_ClientVerifyDomainDkimResponseTypeDef = TypedDict(
    "_ClientVerifyDomainDkimResponseTypeDef", {"DkimTokens": List[str]}, total=False
)


class ClientVerifyDomainDkimResponseTypeDef(_ClientVerifyDomainDkimResponseTypeDef):
    """
    Type definition for `ClientVerifyDomainDkim` `Response`

    Returns CNAME records that you must publish to the DNS server of your domain to set up Easy
    DKIM with Amazon SES.

    - **DkimTokens** *(list) --*

      A set of character strings that represent the domain's identity. If the identity is an email
      address, the tokens represent the domain of that address.

      Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that
      are hosted by Amazon SES. Amazon Web Services eventually detects that you've updated your DNS
      records. This detection process might take up to 72 hours. After successful detection, Amazon
      SES is able to DKIM-sign email originating from that domain. (This only applies to domain
      identities, not email address identities.)

      For more information about creating DNS records using DKIM tokens, see the `Amazon SES
      Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html>`__ .

      - *(string) --*
    """


_ClientVerifyDomainIdentityResponseTypeDef = TypedDict(
    "_ClientVerifyDomainIdentityResponseTypeDef",
    {"VerificationToken": str},
    total=False,
)


class ClientVerifyDomainIdentityResponseTypeDef(
    _ClientVerifyDomainIdentityResponseTypeDef
):
    """
    Type definition for `ClientVerifyDomainIdentity` `Response`

    Returns a TXT record that you must publish to the DNS server of your domain to complete domain
    verification with Amazon SES.

    - **VerificationToken** *(string) --*

      A TXT record that you must place in the DNS settings of the domain to complete domain
      verification with Amazon SES.

      As Amazon SES searches for the TXT record, the domain's verification status is "Pending".
      When Amazon SES detects the record, the domain's verification status changes to "Success". If
      Amazon SES is unable to detect the record within 72 hours, the domain's verification status
      changes to "Failed." In that case, if you still want to verify the domain, you must restart
      the verification process from the beginning.
    """


_IdentityExistsWaitWaiterConfigTypeDef = TypedDict(
    "_IdentityExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class IdentityExistsWaitWaiterConfigTypeDef(_IdentityExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `IdentityExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """


_ListConfigurationSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationSetsPaginatePaginationConfigTypeDef(
    _ListConfigurationSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConfigurationSetsPaginate` `PaginationConfig`

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


_ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef",
    {"Name": str},
    total=False,
)


class ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef(
    _ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef
):
    """
    Type definition for `ListConfigurationSetsPaginateResponse` `ConfigurationSets`

    The name of the configuration set.

    Configuration sets let you create groups of rules that you can apply to the emails you send
    using Amazon SES. For more information about using configuration sets, see `Using Amazon
    SES Configuration Sets
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
    the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__
    .

    - **Name** *(string) --*

      The name of the configuration set. The name must meet the following requirements:

      * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

      * Contain 64 characters or fewer.
    """


_ListConfigurationSetsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseTypeDef",
    {
        "ConfigurationSets": List[
            ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef
        ]
    },
    total=False,
)


class ListConfigurationSetsPaginateResponseTypeDef(
    _ListConfigurationSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListConfigurationSetsPaginate` `Response`

    A list of configuration sets associated with your AWS account. Configuration sets enable you to
    publish email sending events. For information about using configuration sets, see the `Amazon
    SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

    - **ConfigurationSets** *(list) --*

      A list of configuration sets.

      - *(dict) --*

        The name of the configuration set.

        Configuration sets let you create groups of rules that you can apply to the emails you send
        using Amazon SES. For more information about using configuration sets, see `Using Amazon
        SES Configuration Sets
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
        the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__
        .

        - **Name** *(string) --*

          The name of the configuration set. The name must meet the following requirements:

          * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).

          * Contain 64 characters or fewer.
    """


_ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef(
    _ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCustomVerificationEmailTemplatesPaginate` `PaginationConfig`

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


_ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef(
    _ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef
):
    """
    Type definition for `ListCustomVerificationEmailTemplatesPaginateResponse` `CustomVerificationEmailTemplates`

    Contains information about a custom verification email template.

    - **TemplateName** *(string) --*

      The name of the custom verification email template.

    - **FromEmailAddress** *(string) --*

      The email address that the custom verification email is sent from.

    - **TemplateSubject** *(string) --*

      The subject line of the custom verification email.

    - **SuccessRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is
      successfully verified.

    - **FailureRedirectionURL** *(string) --*

      The URL that the recipient of the verification email is sent to if his or her address is
      not successfully verified.
    """


_ListCustomVerificationEmailTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginateResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[
            ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef
        ]
    },
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginateResponseTypeDef(
    _ListCustomVerificationEmailTemplatesPaginateResponseTypeDef
):
    """
    Type definition for `ListCustomVerificationEmailTemplatesPaginate` `Response`

    A paginated list of custom verification email templates.

    - **CustomVerificationEmailTemplates** *(list) --*

      A list of the custom verification email templates that exist in your account.

      - *(dict) --*

        Contains information about a custom verification email template.

        - **TemplateName** *(string) --*

          The name of the custom verification email template.

        - **FromEmailAddress** *(string) --*

          The email address that the custom verification email is sent from.

        - **TemplateSubject** *(string) --*

          The subject line of the custom verification email.

        - **SuccessRedirectionURL** *(string) --*

          The URL that the recipient of the verification email is sent to if his or her address is
          successfully verified.

        - **FailureRedirectionURL** *(string) --*

          The URL that the recipient of the verification email is sent to if his or her address is
          not successfully verified.
    """


_ListIdentitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentitiesPaginatePaginationConfigTypeDef(
    _ListIdentitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIdentitiesPaginate` `PaginationConfig`

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


_ListIdentitiesPaginateResponseTypeDef = TypedDict(
    "_ListIdentitiesPaginateResponseTypeDef", {"Identities": List[str]}, total=False
)


class ListIdentitiesPaginateResponseTypeDef(_ListIdentitiesPaginateResponseTypeDef):
    """
    Type definition for `ListIdentitiesPaginate` `Response`

    A list of all identities that you have attempted to verify under your AWS account, regardless
    of verification status.

    - **Identities** *(list) --*

      A list of identities.

      - *(string) --*
    """


_ListReceiptRuleSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListReceiptRuleSetsPaginatePaginationConfigTypeDef(
    _ListReceiptRuleSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListReceiptRuleSetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef(
    _ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef
):
    """
    Type definition for `ListReceiptRuleSetsPaginateResponse` `RuleSets`

    Information about a receipt rule set.

    A receipt rule set is a collection of rules that specify what Amazon SES should do with
    mail it receives on behalf of your account's verified domains.

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
    .

    - **Name** *(string) --*

      The name of the receipt rule set. The name must:

      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
      or dashes (-).

      * Start and end with a letter or number.

      * Contain less than 64 characters.

    - **CreatedTimestamp** *(datetime) --*

      The date and time the receipt rule set was created.
    """


_ListReceiptRuleSetsPaginateResponseTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginateResponseTypeDef",
    {"RuleSets": List[ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef]},
    total=False,
)


class ListReceiptRuleSetsPaginateResponseTypeDef(
    _ListReceiptRuleSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListReceiptRuleSetsPaginate` `Response`

    A list of receipt rule sets that exist under your AWS account.

    - **RuleSets** *(list) --*

      The metadata for the currently active receipt rule set. The metadata consists of the rule set
      name and the timestamp of when the rule set was created.

      - *(dict) --*

        Information about a receipt rule set.

        A receipt rule set is a collection of rules that specify what Amazon SES should do with
        mail it receives on behalf of your account's verified domains.

        For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
        <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
        .

        - **Name** *(string) --*

          The name of the receipt rule set. The name must:

          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
          or dashes (-).

          * Start and end with a letter or number.

          * Contain less than 64 characters.

        - **CreatedTimestamp** *(datetime) --*

          The date and time the receipt rule set was created.
    """


_ListTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTemplatesPaginatePaginationConfigTypeDef(
    _ListTemplatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTemplatesPaginate` `PaginationConfig`

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


_ListTemplatesPaginateResponseTemplatesMetadataTypeDef = TypedDict(
    "_ListTemplatesPaginateResponseTemplatesMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ListTemplatesPaginateResponseTemplatesMetadataTypeDef(
    _ListTemplatesPaginateResponseTemplatesMetadataTypeDef
):
    """
    Type definition for `ListTemplatesPaginateResponse` `TemplatesMetadata`

    Contains information about an email template.

    - **Name** *(string) --*

      The name of the template.

    - **CreatedTimestamp** *(datetime) --*

      The time and date the template was created.
    """


_ListTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListTemplatesPaginateResponseTypeDef",
    {"TemplatesMetadata": List[ListTemplatesPaginateResponseTemplatesMetadataTypeDef]},
    total=False,
)


class ListTemplatesPaginateResponseTypeDef(_ListTemplatesPaginateResponseTypeDef):
    """
    Type definition for `ListTemplatesPaginate` `Response`

    - **TemplatesMetadata** *(list) --*

      An array the contains the name and creation time stamp for each template in your Amazon SES
      account.

      - *(dict) --*

        Contains information about an email template.

        - **Name** *(string) --*

          The name of the template.

        - **CreatedTimestamp** *(datetime) --*

          The time and date the template was created.
    """
