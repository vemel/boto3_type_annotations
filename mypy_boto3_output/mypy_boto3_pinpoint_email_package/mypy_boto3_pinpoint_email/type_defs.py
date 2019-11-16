"Main interface for pinpoint-email type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetReputationOptionsTypeDef",
    "ClientCreateConfigurationSetSendingOptionsTypeDef",
    "ClientCreateConfigurationSetTagsTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTypeDef",
    "ClientCreateDedicatedIpPoolTagsTypeDef",
    "ClientCreateDeliverabilityTestReportContentRawTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    "ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    "ClientCreateDeliverabilityTestReportContentTypeDef",
    "ClientCreateDeliverabilityTestReportResponseTypeDef",
    "ClientCreateDeliverabilityTestReportTagsTypeDef",
    "ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    "ClientCreateEmailIdentityResponseTypeDef",
    "ClientCreateEmailIdentityTagsTypeDef",
    "ClientGetAccountResponseSendQuotaTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    "ClientGetBlacklistReportsResponseTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    "ClientGetConfigurationSetResponseSendingOptionsTypeDef",
    "ClientGetConfigurationSetResponseTagsTypeDef",
    "ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientGetConfigurationSetResponseTypeDef",
    "ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    "ClientGetDedicatedIpResponseTypeDef",
    "ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    "ClientGetDedicatedIpsResponseTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    "ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    "ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    "ClientGetDeliverabilityTestReportResponseTagsTypeDef",
    "ClientGetDeliverabilityTestReportResponseTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    "ClientGetDomainStatisticsReportResponseTypeDef",
    "ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    "ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    "ClientGetEmailIdentityResponseTagsTypeDef",
    "ClientGetEmailIdentityResponseTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListDedicatedIpPoolsResponseTypeDef",
    "ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    "ClientListDeliverabilityTestReportsResponseTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    "ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    "ClientListEmailIdentitiesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    "ClientSendEmailContentRawTypeDef",
    "ClientSendEmailContentSimpleBodyHtmlTypeDef",
    "ClientSendEmailContentSimpleBodyTextTypeDef",
    "ClientSendEmailContentSimpleBodyTypeDef",
    "ClientSendEmailContentSimpleSubjectTypeDef",
    "ClientSendEmailContentSimpleTypeDef",
    "ClientSendEmailContentTemplateTypeDef",
    "ClientSendEmailContentTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailEmailTagsTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    "GetDedicatedIpsPaginatePaginationConfigTypeDef",
    "GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef",
    "GetDedicatedIpsPaginateResponseTypeDef",
    "ListConfigurationSetsPaginatePaginationConfigTypeDef",
    "ListConfigurationSetsPaginateResponseTypeDef",
    "ListDedicatedIpPoolsPaginatePaginationConfigTypeDef",
    "ListDedicatedIpPoolsPaginateResponseTypeDef",
    "ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef",
    "ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef",
    "ListDeliverabilityTestReportsPaginateResponseTypeDef",
    "ListEmailIdentitiesPaginatePaginationConfigTypeDef",
    "ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef",
    "ListEmailIdentitiesPaginateResponseTypeDef",
)


_ClientCreateConfigurationSetDeliveryOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    {"TlsPolicy": str, "SendingPoolName": str},
    total=False,
)


class ClientCreateConfigurationSetDeliveryOptionsTypeDef(
    _ClientCreateConfigurationSetDeliveryOptionsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSet` `DeliveryOptions`

    An object that defines the dedicated IP pool that is used to send emails that you send using the
    configuration set.

    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport Layer
      Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS connection
      can be established. If the value is ``Optional`` , messages can be delivered in plain text if a
      TLS connection can't be established.

    - **SendingPoolName** *(string) --*

      The name of the dedicated IP pool that you want to associate with the configuration set.
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

    An object that defines the dimension configuration to use when you send Amazon Pinpoint
    email events to Amazon CloudWatch.

    - **DimensionName** *(string) --* **[REQUIRED]**

      The name of an Amazon CloudWatch dimension associated with an email sending metric. The
      name has to meet the following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
      (-).

      * It can contain no more than 256 characters.

    - **DimensionValueSource** *(string) --* **[REQUIRED]**

      The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
      CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
      X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
      ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
      ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

    - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

      The default value of the dimension that is published to Amazon CloudWatch if you don't
      provide the value of the dimension when you send an email. This value has to meet the
      following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
      (-).

      * It can contain no more than 256 characters.
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

    An object that defines an Amazon CloudWatch destination for email events. You can use Amazon
    CloudWatch to monitor and gain insights on your email sending metrics.

    - **DimensionConfigurations** *(list) --* **[REQUIRED]**

      An array of objects that define the dimensions to use when you send email events to Amazon
      CloudWatch.

      - *(dict) --*

        An object that defines the dimension configuration to use when you send Amazon Pinpoint
        email events to Amazon CloudWatch.

        - **DimensionName** *(string) --* **[REQUIRED]**

          The name of an Amazon CloudWatch dimension associated with an email sending metric. The
          name has to meet the following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
          (-).

          * It can contain no more than 256 characters.

        - **DimensionValueSource** *(string) --* **[REQUIRED]**

          The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
          CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
          X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
          ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
          ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

        - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

          The default value of the dimension that is published to Amazon CloudWatch if you don't
          provide the value of the dimension when you send an email. This value has to meet the
          following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
          (-).

          * It can contain no more than 256 characters.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IamRoleArn": str, "DeliveryStreamArn": str},
)


class ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `KinesisFirehoseDestination`

    An object that defines an Amazon Kinesis Data Firehose destination for email events. You can
    use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon
    Redshift.

    - **IamRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email
      events to the Amazon Kinesis Data Firehose stream.

    - **DeliveryStreamArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
      Pinpoint sends email events to.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `PinpointDestination`

    An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
    Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes
    to create segments for your campaigns.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email
      events to.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
)


class ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestinationEventDestination` `SnsDestination`

    An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to
    send notification when certain email events occur.

    - **TopicArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events
      to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[str],
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestination` `EventDestination`

    An object that defines the event destination.

    - **Enabled** *(boolean) --*

      If ``true`` , the event destination is enabled. When the event destination is enabled, the
      specified event types are sent to the destinations in this ``EventDestinationDefinition`` .

      If ``false`` , the event destination is disabled. When the event destination is disabled,
      events aren't sent to the specified destinations.

    - **MatchingEventTypes** *(list) --*

      An array that specifies which events Amazon Pinpoint should send to the destinations in this
      ``EventDestinationDefinition`` .

      - *(string) --*

        An email sending event type. For example, email sends, opens, and bounces are all email
        events.

    - **KinesisFirehoseDestination** *(dict) --*

      An object that defines an Amazon Kinesis Data Firehose destination for email events. You can
      use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon
      Redshift.

      - **IamRoleArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email
        events to the Amazon Kinesis Data Firehose stream.

      - **DeliveryStreamArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
        Pinpoint sends email events to.

    - **CloudWatchDestination** *(dict) --*

      An object that defines an Amazon CloudWatch destination for email events. You can use Amazon
      CloudWatch to monitor and gain insights on your email sending metrics.

      - **DimensionConfigurations** *(list) --* **[REQUIRED]**

        An array of objects that define the dimensions to use when you send email events to Amazon
        CloudWatch.

        - *(dict) --*

          An object that defines the dimension configuration to use when you send Amazon Pinpoint
          email events to Amazon CloudWatch.

          - **DimensionName** *(string) --* **[REQUIRED]**

            The name of an Amazon CloudWatch dimension associated with an email sending metric. The
            name has to meet the following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
            (-).

            * It can contain no more than 256 characters.

          - **DimensionValueSource** *(string) --* **[REQUIRED]**

            The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
            CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
            X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
            ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
            ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

          - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

            The default value of the dimension that is published to Amazon CloudWatch if you don't
            provide the value of the dimension when you send an email. This value has to meet the
            following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
            (-).

            * It can contain no more than 256 characters.

    - **SnsDestination** *(dict) --*

      An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to
      send notification when certain email events occur.

      - **TopicArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events
        to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **PinpointDestination** *(dict) --*

      An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
      Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes
      to create segments for your campaigns.

      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email
        events to.
    """


_ClientCreateConfigurationSetReputationOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)


class ClientCreateConfigurationSetReputationOptionsTypeDef(
    _ClientCreateConfigurationSetReputationOptionsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSet` `ReputationOptions`

    An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails
    that you send that use the configuration set.

    - **ReputationMetricsEnabled** *(boolean) --*

      If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false``
      , tracking of reputation metrics is disabled for the configuration set.

    - **LastFreshStart** *(datetime) --*

      The date and time (in Unix time) when the reputation metrics were last given a fresh start.
      When your account is given a fresh start, your reputation metrics are calculated starting from
      the date of the fresh start.
    """


_ClientCreateConfigurationSetSendingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetSendingOptionsTypeDef",
    {"SendingEnabled": bool},
    total=False,
)


class ClientCreateConfigurationSetSendingOptionsTypeDef(
    _ClientCreateConfigurationSetSendingOptionsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSet` `SendingOptions`

    An object that defines whether or not Amazon Pinpoint can send email that you send using the
    configuration set.

    - **SendingEnabled** *(boolean) --*

      If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending
      is disabled for the configuration set.
    """


_ClientCreateConfigurationSetTagsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateConfigurationSetTagsTypeDef(_ClientCreateConfigurationSetTagsTypeDef):
    """
    Type definition for `ClientCreateConfigurationSet` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label that
    you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
    categorize and manage resources in different ways, such as by purpose, owner, environment, or
    other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value. A
    tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be Unicode
    letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
    additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
    that you define. In addition, you can't edit or remove tag keys or values that use this prefix.
    Tags that use this prefix don’t count against the limit of 50 tags per resource.

    * You can associate tags with public or shared resources, but the tags are available only for
    your AWS account, not any other accounts that share the resource. In addition, the tags are
    available only for resources that are located in the specified AWS Region for your AWS account.

    - **Key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --* **[REQUIRED]**

      The optional part of a key-value pair that defines a tag. The maximum length of a tag value
      is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a
      specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the
      value to an empty string.
    """


_ClientCreateConfigurationSetTrackingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetTrackingOptionsTypeDef", {"CustomRedirectDomain": str}
)


class ClientCreateConfigurationSetTrackingOptionsTypeDef(
    _ClientCreateConfigurationSetTrackingOptionsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSet` `TrackingOptions`

    An object that defines the open and click tracking options for emails that you send using the
    configuration set.

    - **CustomRedirectDomain** *(string) --* **[REQUIRED]**

      The domain that you want to use for tracking open and click events.
    """


_ClientCreateDedicatedIpPoolTagsTypeDef = TypedDict(
    "_ClientCreateDedicatedIpPoolTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateDedicatedIpPoolTagsTypeDef(_ClientCreateDedicatedIpPoolTagsTypeDef):
    """
    Type definition for `ClientCreateDedicatedIpPool` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label that
    you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
    categorize and manage resources in different ways, such as by purpose, owner, environment, or
    other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value. A
    tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be Unicode
    letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
    additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
    that you define. In addition, you can't edit or remove tag keys or values that use this prefix.
    Tags that use this prefix don’t count against the limit of 50 tags per resource.

    * You can associate tags with public or shared resources, but the tags are available only for
    your AWS account, not any other accounts that share the resource. In addition, the tags are
    available only for resources that are located in the specified AWS Region for your AWS account.

    - **Key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --* **[REQUIRED]**

      The optional part of a key-value pair that defines a tag. The maximum length of a tag value
      is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a
      specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the
      value to an empty string.
    """


_ClientCreateDeliverabilityTestReportContentRawTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentRawTypeDef", {"Data": bytes}
)


class ClientCreateDeliverabilityTestReportContentRawTypeDef(
    _ClientCreateDeliverabilityTestReportContentRawTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContent` `Raw`

    The raw email message. The message has to meet the following criteria:

    * The message has to contain a header and a body, separated by one blank line.

    * All of the required header fields must be present in the message.

    * Each part of a multipart MIME message must be formatted properly.

    * If you include attachments, they must be in a file format that Amazon Pinpoint supports.

    * The entire message must be Base64 encoded.

    * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
    character range, you should encode that content to ensure that recipients' email clients render
    the message properly.

    * The length of any single line of text in the message can't exceed 1,000 characters. This
    restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **Data** *(bytes) --* **[REQUIRED]**

      The raw email message. The message has to meet the following criteria:

      * The message has to contain a header and a body, separated by one blank line.

      * All of the required header fields must be present in the message.

      * Each part of a multipart MIME message must be formatted properly.

      * Attachments must be in a file format that Amazon Pinpoint supports.

      * The entire message must be Base64 encoded.

      * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
      character range, you should encode that content to ensure that recipients' email clients
      render the message properly.

      * The length of any single line of text in the message can't exceed 1,000 characters. This
      restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .
    """


_RequiredClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    {"Data": str},
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    {"Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef,
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContentSimpleBody` `Html`

    An object that represents the version of the message that is displayed in email clients
    that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol,
      Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
      the ASCII range, you have to specify a character set. For example, you could specify
      ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_RequiredClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    {"Data": str},
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    {"Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef,
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContentSimpleBody` `Text`

    An object that represents the version of the message that is displayed in email clients
    that don't support HTML, or clients where the recipient has disabled HTML rendering.

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol,
      Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
      the ASCII range, you have to specify a character set. For example, you could specify
      ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    {
        "Text": ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef,
        "Html": ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef(
    _ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContentSimple` `Body`

    The body of the message. You can specify an HTML version of the message, a text-only version
    of the message, or both.

    - **Text** *(dict) --*

      An object that represents the version of the message that is displayed in email clients
      that don't support HTML, or clients where the recipient has disabled HTML rendering.

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol,
        Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
        the ASCII range, you have to specify a character set. For example, you could specify
        ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Html** *(dict) --*

      An object that represents the version of the message that is displayed in email clients
      that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol,
        Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
        the ASCII range, you have to specify a character set. For example, you could specify
        ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    {"Data": str},
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    {"Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContentSimple` `Subject`

    The subject line of the email. The subject line can only contain 7-bit ASCII characters.
    However, you can specify non-ASCII characters in the subject line by using encoded-word
    syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol, Amazon
      Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
      range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
      ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientCreateDeliverabilityTestReportContentSimpleTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    {
        "Subject": ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
        "Body": ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef,
    },
)


class ClientCreateDeliverabilityTestReportContentSimpleTypeDef(
    _ClientCreateDeliverabilityTestReportContentSimpleTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContent` `Simple`

    The simple email message. The message consists of a subject and a message body.

    - **Subject** *(dict) --* **[REQUIRED]**

      The subject line of the email. The subject line can only contain 7-bit ASCII characters.
      However, you can specify non-ASCII characters in the subject line by using encoded-word
      syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol, Amazon
        Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
        range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
        ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Body** *(dict) --* **[REQUIRED]**

      The body of the message. You can specify an HTML version of the message, a text-only version
      of the message, or both.

      - **Text** *(dict) --*

        An object that represents the version of the message that is displayed in email clients
        that don't support HTML, or clients where the recipient has disabled HTML rendering.

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol,
          Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
          the ASCII range, you have to specify a character set. For example, you could specify
          ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

      - **Html** *(dict) --*

        An object that represents the version of the message that is displayed in email clients
        that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol,
          Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
          the ASCII range, you have to specify a character set. For example, you could specify
          ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientCreateDeliverabilityTestReportContentTemplateTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    {"TemplateArn": str, "TemplateData": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentTemplateTypeDef(
    _ClientCreateDeliverabilityTestReportContentTemplateTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReportContent` `Template`

    The template to use for the email message.

    - **TemplateArn** *(string) --*

      The Amazon Resource Name (ARN) of the template.

    - **TemplateData** *(string) --*

      An object that defines the values to use for message variables in the template. This object
      is a set of key-value pairs. Each key defines a message variable in the template. The
      corresponding value defines the value to use for that variable.
    """


_ClientCreateDeliverabilityTestReportContentTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentTypeDef",
    {
        "Simple": ClientCreateDeliverabilityTestReportContentSimpleTypeDef,
        "Raw": ClientCreateDeliverabilityTestReportContentRawTypeDef,
        "Template": ClientCreateDeliverabilityTestReportContentTemplateTypeDef,
    },
    total=False,
)


class ClientCreateDeliverabilityTestReportContentTypeDef(
    _ClientCreateDeliverabilityTestReportContentTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReport` `Content`

    The HTML body of the message that you sent when you performed the predictive inbox placement test.

    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.

      - **Subject** *(dict) --* **[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol, Amazon
          Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
          range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
          ``ISO-8859-1`` , or ``Shift_JIS`` .

      - **Body** *(dict) --* **[REQUIRED]**

        The body of the message. You can specify an HTML version of the message, a text-only version
        of the message, or both.

        - **Text** *(dict) --*

          An object that represents the version of the message that is displayed in email clients
          that don't support HTML, or clients where the recipient has disabled HTML rendering.

          - **Data** *(string) --* **[REQUIRED]**

            The content of the message itself.

          - **Charset** *(string) --*

            The character set for the content. Because of the constraints of the SMTP protocol,
            Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
            the ASCII range, you have to specify a character set. For example, you could specify
            ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

        - **Html** *(dict) --*

          An object that represents the version of the message that is displayed in email clients
          that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

          - **Data** *(string) --* **[REQUIRED]**

            The content of the message itself.

          - **Charset** *(string) --*

            The character set for the content. Because of the constraints of the SMTP protocol,
            Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
            the ASCII range, you have to specify a character set. For example, you could specify
            ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Raw** *(dict) --*

      The raw email message. The message has to meet the following criteria:

      * The message has to contain a header and a body, separated by one blank line.

      * All of the required header fields must be present in the message.

      * Each part of a multipart MIME message must be formatted properly.

      * If you include attachments, they must be in a file format that Amazon Pinpoint supports.

      * The entire message must be Base64 encoded.

      * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
      character range, you should encode that content to ensure that recipients' email clients render
      the message properly.

      * The length of any single line of text in the message can't exceed 1,000 characters. This
      restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

      - **Data** *(bytes) --* **[REQUIRED]**

        The raw email message. The message has to meet the following criteria:

        * The message has to contain a header and a body, separated by one blank line.

        * All of the required header fields must be present in the message.

        * Each part of a multipart MIME message must be formatted properly.

        * Attachments must be in a file format that Amazon Pinpoint supports.

        * The entire message must be Base64 encoded.

        * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
        character range, you should encode that content to ensure that recipients' email clients
        render the message properly.

        * The length of any single line of text in the message can't exceed 1,000 characters. This
        restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **Template** *(dict) --*

      The template to use for the email message.

      - **TemplateArn** *(string) --*

        The Amazon Resource Name (ARN) of the template.

      - **TemplateData** *(string) --*

        An object that defines the values to use for message variables in the template. This object
        is a set of key-value pairs. Each key defines a message variable in the template. The
        corresponding value defines the value to use for that variable.
    """


_ClientCreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportResponseTypeDef",
    {"ReportId": str, "DeliverabilityTestStatus": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportResponseTypeDef(
    _ClientCreateDeliverabilityTestReportResponseTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReport` `Response`

    Information about the predictive inbox placement test that you created.

    - **ReportId** *(string) --*

      A unique string that identifies the predictive inbox placement test.

    - **DeliverabilityTestStatus** *(string) --*

      The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then
      the predictive inbox placement test is currently running. Predictive inbox placement tests
      are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` ,
      then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the
      results of the test.
    """


_ClientCreateDeliverabilityTestReportTagsTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateDeliverabilityTestReportTagsTypeDef(
    _ClientCreateDeliverabilityTestReportTagsTypeDef
):
    """
    Type definition for `ClientCreateDeliverabilityTestReport` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label that
    you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
    categorize and manage resources in different ways, such as by purpose, owner, environment, or
    other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value. A
    tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be Unicode
    letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
    additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
    that you define. In addition, you can't edit or remove tag keys or values that use this prefix.
    Tags that use this prefix don’t count against the limit of 50 tags per resource.

    * You can associate tags with public or shared resources, but the tags are available only for
    your AWS account, not any other accounts that share the resource. In addition, the tags are
    available only for resources that are located in the specified AWS Region for your AWS account.

    - **Key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --* **[REQUIRED]**

      The optional part of a key-value pair that defines a tag. The maximum length of a tag value
      is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a
      specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the
      value to an empty string.
    """


_ClientCreateEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "_ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    {"SigningEnabled": bool, "Status": str, "Tokens": List[str]},
    total=False,
)


class ClientCreateEmailIdentityResponseDkimAttributesTypeDef(
    _ClientCreateEmailIdentityResponseDkimAttributesTypeDef
):
    """
    Type definition for `ClientCreateEmailIdentityResponse` `DkimAttributes`

    An object that contains information about the DKIM attributes for the identity. This object
    includes the tokens that you use to create the CNAME records that are required to complete
    the DKIM verification process.

    - **SigningEnabled** *(boolean) --*

      If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity
      are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends
      from the identity aren't DKIM-signed.

    - **Status** *(string) --*

      Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the
      DNS records for the domain. The status can be one of the following:

      * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS
      configuration for the domain, but will continue to attempt to locate them.

      * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the
      domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email
      from the identity.

      * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings
      for the domain, and won't continue to search for them.

      * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
      determining the DKIM status for the domain.

      * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in
      the DKIM records for the domain.

    - **Tokens** *(list) --*

      A set of unique strings that you use to create a set of CNAME records that you add to the
      DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS
      configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint
      usually detects these records within about 72 hours of adding them to the DNS configuration
      for your domain.

      - *(string) --*
    """


_ClientCreateEmailIdentityResponseTypeDef = TypedDict(
    "_ClientCreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": str,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientCreateEmailIdentityResponseDkimAttributesTypeDef,
    },
    total=False,
)


class ClientCreateEmailIdentityResponseTypeDef(
    _ClientCreateEmailIdentityResponseTypeDef
):
    """
    Type definition for `ClientCreateEmailIdentity` `Response`

    If the email identity is a domain, this object contains tokens that you can use to create a set
    of CNAME records. To sucessfully verify your domain, you have to add these records to the DNS
    configuration for your domain.

    If the email identity is an email address, this object is empty.

    - **IdentityType** *(string) --*

      The email identity type.

    - **VerifiedForSendingStatus** *(boolean) --*

      Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send
      email from verified email addresses or domains. For more information about verifying
      identities, see the `Amazon Pinpoint User Guide
      <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .

    - **DkimAttributes** *(dict) --*

      An object that contains information about the DKIM attributes for the identity. This object
      includes the tokens that you use to create the CNAME records that are required to complete
      the DKIM verification process.

      - **SigningEnabled** *(boolean) --*

        If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity
        are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends
        from the identity aren't DKIM-signed.

      - **Status** *(string) --*

        Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the
        DNS records for the domain. The status can be one of the following:

        * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS
        configuration for the domain, but will continue to attempt to locate them.

        * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the
        domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email
        from the identity.

        * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings
        for the domain, and won't continue to search for them.

        * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
        determining the DKIM status for the domain.

        * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in
        the DKIM records for the domain.

      - **Tokens** *(list) --*

        A set of unique strings that you use to create a set of CNAME records that you add to the
        DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS
        configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint
        usually detects these records within about 72 hours of adding them to the DNS configuration
        for your domain.

        - *(string) --*
    """


_ClientCreateEmailIdentityTagsTypeDef = TypedDict(
    "_ClientCreateEmailIdentityTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateEmailIdentityTagsTypeDef(_ClientCreateEmailIdentityTagsTypeDef):
    """
    Type definition for `ClientCreateEmailIdentity` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label that
    you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
    categorize and manage resources in different ways, such as by purpose, owner, environment, or
    other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value. A
    tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be Unicode
    letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
    additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
    that you define. In addition, you can't edit or remove tag keys or values that use this prefix.
    Tags that use this prefix don’t count against the limit of 50 tags per resource.

    * You can associate tags with public or shared resources, but the tags are available only for
    your AWS account, not any other accounts that share the resource. In addition, the tags are
    available only for resources that are located in the specified AWS Region for your AWS account.

    - **Key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --* **[REQUIRED]**

      The optional part of a key-value pair that defines a tag. The maximum length of a tag value
      is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a
      specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the
      value to an empty string.
    """


_ClientGetAccountResponseSendQuotaTypeDef = TypedDict(
    "_ClientGetAccountResponseSendQuotaTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)


class ClientGetAccountResponseSendQuotaTypeDef(
    _ClientGetAccountResponseSendQuotaTypeDef
):
    """
    Type definition for `ClientGetAccountResponse` `SendQuota`

    An object that contains information about the per-day and per-second sending limits for your
    Amazon Pinpoint account in the current AWS Region.

    - **Max24HourSend** *(float) --*

      The maximum number of emails that you can send in the current AWS Region over a 24-hour
      period. This value is also called your *sending quota* .

    - **MaxSendRate** *(float) --*

      The maximum number of emails that you can send per second in the current AWS Region. This
      value is also called your *maximum sending rate* or your *maximum TPS (transactions per
      second) rate* .

    - **SentLast24Hours** *(float) --*

      The number of emails sent from your Amazon Pinpoint account in the current AWS Region over
      the past 24 hours.
    """


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {
        "SendQuota": ClientGetAccountResponseSendQuotaTypeDef,
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
    },
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    Type definition for `ClientGetAccount` `Response`

    A list of details about the email-sending capabilities of your Amazon Pinpoint account in the
    current AWS Region.

    - **SendQuota** *(dict) --*

      An object that contains information about the per-day and per-second sending limits for your
      Amazon Pinpoint account in the current AWS Region.

      - **Max24HourSend** *(float) --*

        The maximum number of emails that you can send in the current AWS Region over a 24-hour
        period. This value is also called your *sending quota* .

      - **MaxSendRate** *(float) --*

        The maximum number of emails that you can send per second in the current AWS Region. This
        value is also called your *maximum sending rate* or your *maximum TPS (transactions per
        second) rate* .

      - **SentLast24Hours** *(float) --*

        The number of emails sent from your Amazon Pinpoint account in the current AWS Region over
        the past 24 hours.

    - **SendingEnabled** *(boolean) --*

      Indicates whether or not email sending is enabled for your Amazon Pinpoint account in the
      current AWS Region.

    - **DedicatedIpAutoWarmupEnabled** *(boolean) --*

      Indicates whether or not the automatic warm-up feature is enabled for dedicated IP addresses
      that are associated with your account.

    - **EnforcementStatus** *(string) --*

      The reputation status of your Amazon Pinpoint account. The status can be one of the following:

      * ``HEALTHY`` – There are no reputation-related issues that currently impact your account.

      * ``PROBATION`` – We've identified some issues with your Amazon Pinpoint account. We're
      placing your account under review while you work on correcting these issues.

      * ``SHUTDOWN`` – Your account's ability to send email is currently paused because of an issue
      with the email sent from your account. When you correct the issue, you can contact us and
      request that your account's ability to send email is resumed.

    - **ProductionAccessEnabled** *(boolean) --*

      Indicates whether or not your account has production access in the current AWS Region.

      If the value is ``false`` , then your account is in the *sandbox* . When your account is in
      the sandbox, you can only send email to verified identities. Additionally, the maximum number
      of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum
      number of emails you can send per second (your maximum sending rate) is 1.

      If the value is ``true`` , then your account has production access. When your account has
      production access, you can send email to any address. The sending quota and maximum sending
      rate for your account vary based on your specific use case.
    """


_ClientGetBlacklistReportsResponseBlacklistReportTypeDef = TypedDict(
    "_ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    {"RblName": str, "ListingTime": datetime, "Description": str},
    total=False,
)


class ClientGetBlacklistReportsResponseBlacklistReportTypeDef(
    _ClientGetBlacklistReportsResponseBlacklistReportTypeDef
):
    """
    Type definition for `ClientGetBlacklistReportsResponse` `BlacklistReport`

    An object that contains information about a blacklisting event that impacts one of the
    dedicated IP addresses that is associated with your account.

    - **RblName** *(string) --*

      The name of the blacklist that the IP address appears on.

    - **ListingTime** *(datetime) --*

      The time when the blacklisting event occurred, shown in Unix time format.

    - **Description** *(string) --*

      Additional information about the blacklisting event, as provided by the blacklist
      maintainer.
    """


_ClientGetBlacklistReportsResponseTypeDef = TypedDict(
    "_ClientGetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[
            str, List[ClientGetBlacklistReportsResponseBlacklistReportTypeDef]
        ]
    },
    total=False,
)


class ClientGetBlacklistReportsResponseTypeDef(
    _ClientGetBlacklistReportsResponseTypeDef
):
    """
    Type definition for `ClientGetBlacklistReports` `Response`

    An object that contains information about blacklist events.

    - **BlacklistReport** *(dict) --*

      An object that contains information about a blacklist that one of your dedicated IP addresses
      appears on.

      - *(string) --*

        An IP address that you want to obtain blacklist information for.

        - *(list) --*

          - *(dict) --*

            An object that contains information about a blacklisting event that impacts one of the
            dedicated IP addresses that is associated with your account.

            - **RblName** *(string) --*

              The name of the blacklist that the IP address appears on.

            - **ListingTime** *(datetime) --*

              The time when the blacklisting event occurred, shown in Unix time format.

            - **Description** *(string) --*

              Additional information about the blacklisting event, as provided by the blacklist
              maintainer.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {"DimensionName": str, "DimensionValueSource": str, "DefaultDimensionValue": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestination` `DimensionConfigurations`

    An object that defines the dimension configuration to use when you send Amazon
    Pinpoint email events to Amazon CloudWatch.

    - **DimensionName** *(string) --*

      The name of an Amazon CloudWatch dimension associated with an email sending metric.
      The name has to meet the following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * It can contain no more than 256 characters.

    - **DimensionValueSource** *(string) --*

      The location where Amazon Pinpoint finds the value of a dimension to publish to
      Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you
      specify using an X-SES-MESSAGE-TAGS header or a parameter to the
      SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to
      use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to
      use link tags, choose ``linkTags`` .

    - **DefaultDimensionValue** *(string) --*

      The default value of the dimension that is published to Amazon CloudWatch if you
      don't provide the value of the dimension when you send an email. This value has to
      meet the following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).

      * It can contain no more than 256 characters.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponseEventDestinations` `CloudWatchDestination`

    An object that defines an Amazon CloudWatch destination for email events. You can use
    Amazon CloudWatch to monitor and gain insights on your email sending metrics.

    - **DimensionConfigurations** *(list) --*

      An array of objects that define the dimensions to use when you send email events to
      Amazon CloudWatch.

      - *(dict) --*

        An object that defines the dimension configuration to use when you send Amazon
        Pinpoint email events to Amazon CloudWatch.

        - **DimensionName** *(string) --*

          The name of an Amazon CloudWatch dimension associated with an email sending metric.
          The name has to meet the following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
          dashes (-).

          * It can contain no more than 256 characters.

        - **DimensionValueSource** *(string) --*

          The location where Amazon Pinpoint finds the value of a dimension to publish to
          Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you
          specify using an X-SES-MESSAGE-TAGS header or a parameter to the
          SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to
          use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to
          use link tags, choose ``linkTags`` .

        - **DefaultDimensionValue** *(string) --*

          The default value of the dimension that is published to Amazon CloudWatch if you
          don't provide the value of the dimension when you send an email. This value has to
          meet the following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
          dashes (-).

          * It can contain no more than 256 characters.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponseEventDestinations` `KinesisFirehoseDestination`

    An object that defines an Amazon Kinesis Data Firehose destination for email events. You
    can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3
    and Amazon Redshift.

    - **IamRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending
      email events to the Amazon Kinesis Data Firehose stream.

    - **DeliveryStreamArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
      Pinpoint sends email events to.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponseEventDestinations` `PinpointDestination`

    An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
    Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these
    attributes to create segments for your campaigns.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send
      email events to.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponseEventDestinations` `SnsDestination`

    An object that defines an Amazon SNS destination for email events. You can use Amazon SNS
    to send notification when certain email events occur.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email
      events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer
      Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[str],
        "KinesisFirehoseDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SnsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef,
        "PinpointDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinationsResponse` `EventDestinations`

    In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and
    complaints. *Event destinations* are places that you can send information about these
    events to. For example, you can send event data to Amazon SNS to receive notifications when
    you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream
    data to Amazon S3 for long-term storage.

    - **Name** *(string) --*

      A name that identifies the event destination.

    - **Enabled** *(boolean) --*

      If ``true`` , the event destination is enabled. When the event destination is enabled,
      the specified event types are sent to the destinations in this
      ``EventDestinationDefinition`` .

      If ``false`` , the event destination is disabled. When the event destination is disabled,
      events aren't sent to the specified destinations.

    - **MatchingEventTypes** *(list) --*

      The types of events that Amazon Pinpoint sends to the specified event destinations.

      - *(string) --*

        An email sending event type. For example, email sends, opens, and bounces are all email
        events.

    - **KinesisFirehoseDestination** *(dict) --*

      An object that defines an Amazon Kinesis Data Firehose destination for email events. You
      can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3
      and Amazon Redshift.

      - **IamRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending
        email events to the Amazon Kinesis Data Firehose stream.

      - **DeliveryStreamArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
        Pinpoint sends email events to.

    - **CloudWatchDestination** *(dict) --*

      An object that defines an Amazon CloudWatch destination for email events. You can use
      Amazon CloudWatch to monitor and gain insights on your email sending metrics.

      - **DimensionConfigurations** *(list) --*

        An array of objects that define the dimensions to use when you send email events to
        Amazon CloudWatch.

        - *(dict) --*

          An object that defines the dimension configuration to use when you send Amazon
          Pinpoint email events to Amazon CloudWatch.

          - **DimensionName** *(string) --*

            The name of an Amazon CloudWatch dimension associated with an email sending metric.
            The name has to meet the following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
            dashes (-).

            * It can contain no more than 256 characters.

          - **DimensionValueSource** *(string) --*

            The location where Amazon Pinpoint finds the value of a dimension to publish to
            Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you
            specify using an X-SES-MESSAGE-TAGS header or a parameter to the
            SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to
            use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to
            use link tags, choose ``linkTags`` .

          - **DefaultDimensionValue** *(string) --*

            The default value of the dimension that is published to Amazon CloudWatch if you
            don't provide the value of the dimension when you send an email. This value has to
            meet the following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
            dashes (-).

            * It can contain no more than 256 characters.

    - **SnsDestination** *(dict) --*

      An object that defines an Amazon SNS destination for email events. You can use Amazon SNS
      to send notification when certain email events occur.

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email
        events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer
        Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **PinpointDestination** *(dict) --*

      An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
      Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these
      attributes to create segments for your campaigns.

      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send
        email events to.
    """


_ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
        ]
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinations` `Response`

    Information about an event destination for a configuration set.

    - **EventDestinations** *(list) --*

      An array that includes all of the events destinations that have been configured for the
      configuration set.

      - *(dict) --*

        In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and
        complaints. *Event destinations* are places that you can send information about these
        events to. For example, you can send event data to Amazon SNS to receive notifications when
        you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream
        data to Amazon S3 for long-term storage.

        - **Name** *(string) --*

          A name that identifies the event destination.

        - **Enabled** *(boolean) --*

          If ``true`` , the event destination is enabled. When the event destination is enabled,
          the specified event types are sent to the destinations in this
          ``EventDestinationDefinition`` .

          If ``false`` , the event destination is disabled. When the event destination is disabled,
          events aren't sent to the specified destinations.

        - **MatchingEventTypes** *(list) --*

          The types of events that Amazon Pinpoint sends to the specified event destinations.

          - *(string) --*

            An email sending event type. For example, email sends, opens, and bounces are all email
            events.

        - **KinesisFirehoseDestination** *(dict) --*

          An object that defines an Amazon Kinesis Data Firehose destination for email events. You
          can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3
          and Amazon Redshift.

          - **IamRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending
            email events to the Amazon Kinesis Data Firehose stream.

          - **DeliveryStreamArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
            Pinpoint sends email events to.

        - **CloudWatchDestination** *(dict) --*

          An object that defines an Amazon CloudWatch destination for email events. You can use
          Amazon CloudWatch to monitor and gain insights on your email sending metrics.

          - **DimensionConfigurations** *(list) --*

            An array of objects that define the dimensions to use when you send email events to
            Amazon CloudWatch.

            - *(dict) --*

              An object that defines the dimension configuration to use when you send Amazon
              Pinpoint email events to Amazon CloudWatch.

              - **DimensionName** *(string) --*

                The name of an Amazon CloudWatch dimension associated with an email sending metric.
                The name has to meet the following criteria:

                * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
                dashes (-).

                * It can contain no more than 256 characters.

              - **DimensionValueSource** *(string) --*

                The location where Amazon Pinpoint finds the value of a dimension to publish to
                Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you
                specify using an X-SES-MESSAGE-TAGS header or a parameter to the
                SendEmail/SendRawEmail API, choose ``messageTag`` . If you want Amazon Pinpoint to
                use your own email headers, choose ``emailHeader`` . If you want Amazon Pinpoint to
                use link tags, choose ``linkTags`` .

              - **DefaultDimensionValue** *(string) --*

                The default value of the dimension that is published to Amazon CloudWatch if you
                don't provide the value of the dimension when you send an email. This value has to
                meet the following criteria:

                * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
                dashes (-).

                * It can contain no more than 256 characters.

        - **SnsDestination** *(dict) --*

          An object that defines an Amazon SNS destination for email events. You can use Amazon SNS
          to send notification when certain email events occur.

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email
            events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer
            Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

        - **PinpointDestination** *(dict) --*

          An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
          Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these
          attributes to create segments for your campaigns.

          - **ApplicationArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send
            email events to.
    """


_ClientGetConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": str, "SendingPoolName": str},
    total=False,
)


class ClientGetConfigurationSetResponseDeliveryOptionsTypeDef(
    _ClientGetConfigurationSetResponseDeliveryOptionsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetResponse` `DeliveryOptions`

    An object that defines the dedicated IP pool that is used to send emails that you send using
    the configuration set.

    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport
      Layer Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS
      connection can be established. If the value is ``Optional`` , messages can be delivered in
      plain text if a TLS connection can't be established.

    - **SendingPoolName** *(string) --*

      The name of the dedicated IP pool that you want to associate with the configuration set.
    """


_ClientGetConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)


class ClientGetConfigurationSetResponseReputationOptionsTypeDef(
    _ClientGetConfigurationSetResponseReputationOptionsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetResponse` `ReputationOptions`

    An object that defines whether or not Amazon Pinpoint collects reputation metrics for the
    emails that you send that use the configuration set.

    - **ReputationMetricsEnabled** *(boolean) --*

      If ``true`` , tracking of reputation metrics is enabled for the configuration set. If
      ``false`` , tracking of reputation metrics is disabled for the configuration set.

    - **LastFreshStart** *(datetime) --*

      The date and time (in Unix time) when the reputation metrics were last given a fresh start.
      When your account is given a fresh start, your reputation metrics are calculated starting
      from the date of the fresh start.
    """


_ClientGetConfigurationSetResponseSendingOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseSendingOptionsTypeDef",
    {"SendingEnabled": bool},
    total=False,
)


class ClientGetConfigurationSetResponseSendingOptionsTypeDef(
    _ClientGetConfigurationSetResponseSendingOptionsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetResponse` `SendingOptions`

    An object that defines whether or not Amazon Pinpoint can send email that you send using the
    configuration set.

    - **SendingEnabled** *(boolean) --*

      If ``true`` , email sending is enabled for the configuration set. If ``false`` , email
      sending is disabled for the configuration set.
    """


_ClientGetConfigurationSetResponseTagsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetConfigurationSetResponseTagsTypeDef(
    _ClientGetConfigurationSetResponseTagsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetResponse` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label
    that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
    you categorize and manage resources in different ways, such as by purpose, owner,
    environment, or other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value.
    A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be
    Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
    following additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
    values that you define. In addition, you can't edit or remove tag keys or values that use
    this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
    resource.

    * You can associate tags with public or shared resources, but the tags are available only
    for your AWS account, not any other accounts that share the resource. In addition, the tags
    are available only for resources that are located in the specified AWS Region for your AWS
    account.

    - **Key** *(string) --*

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --*

      The optional part of a key-value pair that defines a tag. The maximum length of a tag
      value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
      to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
      will set the value to an empty string.
    """


_ClientGetConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientGetConfigurationSetResponseTrackingOptionsTypeDef(
    _ClientGetConfigurationSetResponseTrackingOptionsTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetResponse` `TrackingOptions`

    An object that defines the open and click tracking options for emails that you send using the
    configuration set.

    - **CustomRedirectDomain** *(string) --*

      The domain that you want to use for tracking open and click events.
    """


_ClientGetConfigurationSetResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": ClientGetConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientGetConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientGetConfigurationSetResponseReputationOptionsTypeDef,
        "SendingOptions": ClientGetConfigurationSetResponseSendingOptionsTypeDef,
        "Tags": List[ClientGetConfigurationSetResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetConfigurationSetResponseTypeDef(
    _ClientGetConfigurationSetResponseTypeDef
):
    """
    Type definition for `ClientGetConfigurationSet` `Response`

    Information about a configuration set.

    - **ConfigurationSetName** *(string) --*

      The name of the configuration set.

    - **TrackingOptions** *(dict) --*

      An object that defines the open and click tracking options for emails that you send using the
      configuration set.

      - **CustomRedirectDomain** *(string) --*

        The domain that you want to use for tracking open and click events.

    - **DeliveryOptions** *(dict) --*

      An object that defines the dedicated IP pool that is used to send emails that you send using
      the configuration set.

      - **TlsPolicy** *(string) --*

        Specifies whether messages that use the configuration set are required to use Transport
        Layer Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS
        connection can be established. If the value is ``Optional`` , messages can be delivered in
        plain text if a TLS connection can't be established.

      - **SendingPoolName** *(string) --*

        The name of the dedicated IP pool that you want to associate with the configuration set.

    - **ReputationOptions** *(dict) --*

      An object that defines whether or not Amazon Pinpoint collects reputation metrics for the
      emails that you send that use the configuration set.

      - **ReputationMetricsEnabled** *(boolean) --*

        If ``true`` , tracking of reputation metrics is enabled for the configuration set. If
        ``false`` , tracking of reputation metrics is disabled for the configuration set.

      - **LastFreshStart** *(datetime) --*

        The date and time (in Unix time) when the reputation metrics were last given a fresh start.
        When your account is given a fresh start, your reputation metrics are calculated starting
        from the date of the fresh start.

    - **SendingOptions** *(dict) --*

      An object that defines whether or not Amazon Pinpoint can send email that you send using the
      configuration set.

      - **SendingEnabled** *(boolean) --*

        If ``true`` , email sending is enabled for the configuration set. If ``false`` , email
        sending is disabled for the configuration set.

    - **Tags** *(list) --*

      An array of objects that define the tags (keys and values) that are associated with the
      configuration set.

      - *(dict) --*

        An object that defines the tags that are associated with a resource. A *tag* is a label
        that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
        you categorize and manage resources in different ways, such as by purpose, owner,
        environment, or other criteria. A resource can have as many as 50 tags.

        Each tag consists of a required *tag key* and an associated *tag value* , both of which you
        define. A tag key is a general label that acts as a category for a more specific tag value.
        A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
        characters. A tag value can contain as many as 256 characters. The characters can be
        Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
        following additional restrictions apply to tags:

        * Tag keys and values are case sensitive.

        * For each associated resource, each tag key must be unique and it can have only one value.

        * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
        values that you define. In addition, you can't edit or remove tag keys or values that use
        this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
        resource.

        * You can associate tags with public or shared resources, but the tags are available only
        for your AWS account, not any other accounts that share the resource. In addition, the tags
        are available only for resources that are located in the specified AWS Region for your AWS
        account.

        - **Key** *(string) --*

          One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
          characters. The minimum length is 1 character.

        - **Value** *(string) --*

          The optional part of a key-value pair that defines a tag. The maximum length of a tag
          value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
          to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
          will set the value to an empty string.
    """


_ClientGetDedicatedIpResponseDedicatedIpTypeDef = TypedDict(
    "_ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    {"Ip": str, "WarmupStatus": str, "WarmupPercentage": int, "PoolName": str},
    total=False,
)


class ClientGetDedicatedIpResponseDedicatedIpTypeDef(
    _ClientGetDedicatedIpResponseDedicatedIpTypeDef
):
    """
    Type definition for `ClientGetDedicatedIpResponse` `DedicatedIp`

    An object that contains information about a dedicated IP address.

    - **Ip** *(string) --*

      An IP address that is reserved for use by your Amazon Pinpoint account.

    - **WarmupStatus** *(string) --*

      The warm-up status of a dedicated IP address. The status can have one of the following
      values:

      * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
      process is ongoing.

      * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
      use.

    - **WarmupPercentage** *(integer) --*

      Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
      address has completed the warm-up process and is ready for use.

    - **PoolName** *(string) --*

      The name of the dedicated IP pool that the IP address is associated with.
    """


_ClientGetDedicatedIpResponseTypeDef = TypedDict(
    "_ClientGetDedicatedIpResponseTypeDef",
    {"DedicatedIp": ClientGetDedicatedIpResponseDedicatedIpTypeDef},
    total=False,
)


class ClientGetDedicatedIpResponseTypeDef(_ClientGetDedicatedIpResponseTypeDef):
    """
    Type definition for `ClientGetDedicatedIp` `Response`

    Information about a dedicated IP address.

    - **DedicatedIp** *(dict) --*

      An object that contains information about a dedicated IP address.

      - **Ip** *(string) --*

        An IP address that is reserved for use by your Amazon Pinpoint account.

      - **WarmupStatus** *(string) --*

        The warm-up status of a dedicated IP address. The status can have one of the following
        values:

        * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
        process is ongoing.

        * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
        use.

      - **WarmupPercentage** *(integer) --*

        Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
        address has completed the warm-up process and is ready for use.

      - **PoolName** *(string) --*

        The name of the dedicated IP pool that the IP address is associated with.
    """


_ClientGetDedicatedIpsResponseDedicatedIpsTypeDef = TypedDict(
    "_ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    {"Ip": str, "WarmupStatus": str, "WarmupPercentage": int, "PoolName": str},
    total=False,
)


class ClientGetDedicatedIpsResponseDedicatedIpsTypeDef(
    _ClientGetDedicatedIpsResponseDedicatedIpsTypeDef
):
    """
    Type definition for `ClientGetDedicatedIpsResponse` `DedicatedIps`

    Contains information about a dedicated IP address that is associated with your Amazon
    Pinpoint account.

    - **Ip** *(string) --*

      An IP address that is reserved for use by your Amazon Pinpoint account.

    - **WarmupStatus** *(string) --*

      The warm-up status of a dedicated IP address. The status can have one of the following
      values:

      * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
      process is ongoing.

      * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
      use.

    - **WarmupPercentage** *(integer) --*

      Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
      address has completed the warm-up process and is ready for use.

    - **PoolName** *(string) --*

      The name of the dedicated IP pool that the IP address is associated with.
    """


_ClientGetDedicatedIpsResponseTypeDef = TypedDict(
    "_ClientGetDedicatedIpsResponseTypeDef",
    {
        "DedicatedIps": List[ClientGetDedicatedIpsResponseDedicatedIpsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetDedicatedIpsResponseTypeDef(_ClientGetDedicatedIpsResponseTypeDef):
    """
    Type definition for `ClientGetDedicatedIps` `Response`

    Information about the dedicated IP addresses that are associated with your Amazon Pinpoint
    account.

    - **DedicatedIps** *(list) --*

      A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.

      - *(dict) --*

        Contains information about a dedicated IP address that is associated with your Amazon
        Pinpoint account.

        - **Ip** *(string) --*

          An IP address that is reserved for use by your Amazon Pinpoint account.

        - **WarmupStatus** *(string) --*

          The warm-up status of a dedicated IP address. The status can have one of the following
          values:

          * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
          process is ongoing.

          * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
          use.

        - **WarmupPercentage** *(integer) --*

          Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
          address has completed the warm-up process and is ready for use.

        - **PoolName** *(string) --*

          The name of the dedicated IP pool that the IP address is associated with.

    - **NextToken** *(string) --*

      A token that indicates that there are additional dedicated IP addresses to list. To view
      additional addresses, issue another request to ``GetDedicatedIps`` , passing this token in
      the ``NextToken`` parameter.
    """


_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomains` `InboxPlacementTrackingOption`

    An object that contains information about the inbox placement data settings for the
    domain.

    - **Global** *(boolean) --*

      Specifies whether inbox placement data is being tracked for the domain.

    - **TrackedIsps** *(list) --*

      An array of strings, one for each major email provider that the inbox placement data
      applies to.

      - *(string) --*

        The name of an email provider.
    """


_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityDashboardOptionsResponse` `ActiveSubscribedDomains`

    An object that contains information about the Deliverability dashboard subscription for a
    verified domain that you use to send email and currently has an active Deliverability
    dashboard subscription. If a Deliverability dashboard subscription is active for a domain,
    you gain access to reputation, inbox placement, and other metrics for the domain.

    - **Domain** *(string) --*

      A verified domain that’s associated with your AWS account and currently has an active
      Deliverability dashboard subscription.

    - **SubscriptionStartDate** *(datetime) --*

      The date, in Unix time format, when you enabled the Deliverability dashboard for the
      domain.

    - **InboxPlacementTrackingOption** *(dict) --*

      An object that contains information about the inbox placement data settings for the
      domain.

      - **Global** *(boolean) --*

        Specifies whether inbox placement data is being tracked for the domain.

      - **TrackedIsps** *(list) --*

        An array of strings, one for each major email provider that the inbox placement data
        applies to.

        - *(string) --*

          The name of an email provider.
    """


_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomains` `InboxPlacementTrackingOption`

    An object that contains information about the inbox placement data settings for the
    domain.

    - **Global** *(boolean) --*

      Specifies whether inbox placement data is being tracked for the domain.

    - **TrackedIsps** *(list) --*

      An array of strings, one for each major email provider that the inbox placement data
      applies to.

      - *(string) --*

        The name of an email provider.
    """


_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityDashboardOptionsResponse` `PendingExpirationSubscribedDomains`

    An object that contains information about the Deliverability dashboard subscription for a
    verified domain that you use to send email and currently has an active Deliverability
    dashboard subscription. If a Deliverability dashboard subscription is active for a domain,
    you gain access to reputation, inbox placement, and other metrics for the domain.

    - **Domain** *(string) --*

      A verified domain that’s associated with your AWS account and currently has an active
      Deliverability dashboard subscription.

    - **SubscriptionStartDate** *(datetime) --*

      The date, in Unix time format, when you enabled the Deliverability dashboard for the
      domain.

    - **InboxPlacementTrackingOption** *(dict) --*

      An object that contains information about the inbox placement data settings for the
      domain.

      - **Global** *(boolean) --*

        Specifies whether inbox placement data is being tracked for the domain.

      - **TrackedIsps** *(list) --*

        An array of strings, one for each major email provider that the inbox placement data
        applies to.

        - *(string) --*

          The name of an email provider.
    """


_ClientGetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": str,
        "ActiveSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef
        ],
        "PendingExpirationSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef
        ],
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityDashboardOptions` `Response`

    An object that shows the status of the Deliverability dashboard for your Amazon Pinpoint
    account.

    - **DashboardEnabled** *(boolean) --*

      Specifies whether the Deliverability dashboard is enabled for your Amazon Pinpoint account.
      If this value is ``true`` , the dashboard is enabled.

    - **SubscriptionExpiryDate** *(datetime) --*

      The date, in Unix time format, when your current subscription to the Deliverability dashboard
      is scheduled to expire, if your subscription is scheduled to expire at the end of the current
      calendar month. This value is null if you have an active subscription that isn’t due to
      expire at the end of the month.

    - **AccountStatus** *(string) --*

      The current status of your Deliverability dashboard subscription. If this value is
      ``PENDING_EXPIRATION`` , your subscription is scheduled to expire at the end of the current
      calendar month.

    - **ActiveSubscribedDomains** *(list) --*

      An array of objects, one for each verified domain that you use to send email and currently
      has an active Deliverability dashboard subscription that isn’t scheduled to expire at the end
      of the current calendar month.

      - *(dict) --*

        An object that contains information about the Deliverability dashboard subscription for a
        verified domain that you use to send email and currently has an active Deliverability
        dashboard subscription. If a Deliverability dashboard subscription is active for a domain,
        you gain access to reputation, inbox placement, and other metrics for the domain.

        - **Domain** *(string) --*

          A verified domain that’s associated with your AWS account and currently has an active
          Deliverability dashboard subscription.

        - **SubscriptionStartDate** *(datetime) --*

          The date, in Unix time format, when you enabled the Deliverability dashboard for the
          domain.

        - **InboxPlacementTrackingOption** *(dict) --*

          An object that contains information about the inbox placement data settings for the
          domain.

          - **Global** *(boolean) --*

            Specifies whether inbox placement data is being tracked for the domain.

          - **TrackedIsps** *(list) --*

            An array of strings, one for each major email provider that the inbox placement data
            applies to.

            - *(string) --*

              The name of an email provider.

    - **PendingExpirationSubscribedDomains** *(list) --*

      An array of objects, one for each verified domain that you use to send email and currently
      has an active Deliverability dashboard subscription that's scheduled to expire at the end of
      the current calendar month.

      - *(dict) --*

        An object that contains information about the Deliverability dashboard subscription for a
        verified domain that you use to send email and currently has an active Deliverability
        dashboard subscription. If a Deliverability dashboard subscription is active for a domain,
        you gain access to reputation, inbox placement, and other metrics for the domain.

        - **Domain** *(string) --*

          A verified domain that’s associated with your AWS account and currently has an active
          Deliverability dashboard subscription.

        - **SubscriptionStartDate** *(datetime) --*

          The date, in Unix time format, when you enabled the Deliverability dashboard for the
          domain.

        - **InboxPlacementTrackingOption** *(dict) --*

          An object that contains information about the inbox placement data settings for the
          domain.

          - **Global** *(boolean) --*

            Specifies whether inbox placement data is being tracked for the domain.

          - **TrackedIsps** *(list) --*

            An array of strings, one for each major email provider that the inbox placement data
            applies to.

            - *(string) --*

              The name of an email provider.
    """


_ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": str,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef(
    _ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReportResponse` `DeliverabilityTestReport`

    An object that contains the results of the predictive inbox placement test.

    - **ReportId** *(string) --*

      A unique string that identifies the predictive inbox placement test.

    - **ReportName** *(string) --*

      A name that helps you identify a predictive inbox placement test report.

    - **Subject** *(string) --*

      The subject line for an email that you submitted in a predictive inbox placement test.

    - **FromEmailAddress** *(string) --*

      The sender address that you specified for the predictive inbox placement test.

    - **CreateDate** *(datetime) --*

      The date and time when the predictive inbox placement test was created, in Unix time format.

    - **DeliverabilityTestStatus** *(string) --*

      The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then
      the predictive inbox placement test is currently running. Predictive inbox placement tests
      are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` ,
      then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the
      results of the test.
    """


_ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef(
    _ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReportResponseIspPlacements` `PlacementStatistics`

    An object that contains inbox placement metrics for a specific email provider.

    - **InboxPercentage** *(float) --*

      The percentage of emails that arrived in recipients' inboxes during the predictive
      inbox placement test.

    - **SpamPercentage** *(float) --*

      The percentage of emails that arrived in recipients' spam or junk mail folders during
      the predictive inbox placement test.

    - **MissingPercentage** *(float) --*

      The percentage of emails that didn't arrive in recipients' inboxes at all during the
      predictive inbox placement test.

    - **SpfPercentage** *(float) --*

      The percentage of emails that were authenticated by using Sender Policy Framework (SPF)
      during the predictive inbox placement test.

    - **DkimPercentage** *(float) --*

      The percentage of emails that were authenticated by using DomainKeys Identified Mail
      (DKIM) during the predictive inbox placement test.
    """


_ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef(
    _ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReportResponse` `IspPlacements`

    An object that describes how email sent during the predictive inbox placement test was
    handled by a certain email provider.

    - **IspName** *(string) --*

      The name of the email provider that the inbox placement data applies to.

    - **PlacementStatistics** *(dict) --*

      An object that contains inbox placement metrics for a specific email provider.

      - **InboxPercentage** *(float) --*

        The percentage of emails that arrived in recipients' inboxes during the predictive
        inbox placement test.

      - **SpamPercentage** *(float) --*

        The percentage of emails that arrived in recipients' spam or junk mail folders during
        the predictive inbox placement test.

      - **MissingPercentage** *(float) --*

        The percentage of emails that didn't arrive in recipients' inboxes at all during the
        predictive inbox placement test.

      - **SpfPercentage** *(float) --*

        The percentage of emails that were authenticated by using Sender Policy Framework (SPF)
        during the predictive inbox placement test.

      - **DkimPercentage** *(float) --*

        The percentage of emails that were authenticated by using DomainKeys Identified Mail
        (DKIM) during the predictive inbox placement test.
    """


_ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef(
    _ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReportResponse` `OverallPlacement`

    An object that specifies how many test messages that were sent during the predictive inbox
    placement test were delivered to recipients' inboxes, how many were sent to recipients' spam
    folders, and how many weren't delivered.

    - **InboxPercentage** *(float) --*

      The percentage of emails that arrived in recipients' inboxes during the predictive inbox
      placement test.

    - **SpamPercentage** *(float) --*

      The percentage of emails that arrived in recipients' spam or junk mail folders during the
      predictive inbox placement test.

    - **MissingPercentage** *(float) --*

      The percentage of emails that didn't arrive in recipients' inboxes at all during the
      predictive inbox placement test.

    - **SpfPercentage** *(float) --*

      The percentage of emails that were authenticated by using Sender Policy Framework (SPF)
      during the predictive inbox placement test.

    - **DkimPercentage** *(float) --*

      The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM)
      during the predictive inbox placement test.
    """


_ClientGetDeliverabilityTestReportResponseTagsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetDeliverabilityTestReportResponseTagsTypeDef(
    _ClientGetDeliverabilityTestReportResponseTagsTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReportResponse` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label
    that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
    you categorize and manage resources in different ways, such as by purpose, owner,
    environment, or other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value.
    A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be
    Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
    following additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
    values that you define. In addition, you can't edit or remove tag keys or values that use
    this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
    resource.

    * You can associate tags with public or shared resources, but the tags are available only
    for your AWS account, not any other accounts that share the resource. In addition, the tags
    are available only for resources that are located in the specified AWS Region for your AWS
    account.

    - **Key** *(string) --*

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --*

      The optional part of a key-value pair that defines a tag. The maximum length of a tag
      value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
      to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
      will set the value to an empty string.
    """


_ClientGetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef,
        "OverallPlacement": ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef,
        "IspPlacements": List[
            ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef
        ],
        "Message": str,
        "Tags": List[ClientGetDeliverabilityTestReportResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseTypeDef(
    _ClientGetDeliverabilityTestReportResponseTypeDef
):
    """
    Type definition for `ClientGetDeliverabilityTestReport` `Response`

    The results of the predictive inbox placement test.

    - **DeliverabilityTestReport** *(dict) --*

      An object that contains the results of the predictive inbox placement test.

      - **ReportId** *(string) --*

        A unique string that identifies the predictive inbox placement test.

      - **ReportName** *(string) --*

        A name that helps you identify a predictive inbox placement test report.

      - **Subject** *(string) --*

        The subject line for an email that you submitted in a predictive inbox placement test.

      - **FromEmailAddress** *(string) --*

        The sender address that you specified for the predictive inbox placement test.

      - **CreateDate** *(datetime) --*

        The date and time when the predictive inbox placement test was created, in Unix time format.

      - **DeliverabilityTestStatus** *(string) --*

        The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then
        the predictive inbox placement test is currently running. Predictive inbox placement tests
        are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` ,
        then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the
        results of the test.

    - **OverallPlacement** *(dict) --*

      An object that specifies how many test messages that were sent during the predictive inbox
      placement test were delivered to recipients' inboxes, how many were sent to recipients' spam
      folders, and how many weren't delivered.

      - **InboxPercentage** *(float) --*

        The percentage of emails that arrived in recipients' inboxes during the predictive inbox
        placement test.

      - **SpamPercentage** *(float) --*

        The percentage of emails that arrived in recipients' spam or junk mail folders during the
        predictive inbox placement test.

      - **MissingPercentage** *(float) --*

        The percentage of emails that didn't arrive in recipients' inboxes at all during the
        predictive inbox placement test.

      - **SpfPercentage** *(float) --*

        The percentage of emails that were authenticated by using Sender Policy Framework (SPF)
        during the predictive inbox placement test.

      - **DkimPercentage** *(float) --*

        The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM)
        during the predictive inbox placement test.

    - **IspPlacements** *(list) --*

      An object that describes how the test email was handled by several email providers, including
      Gmail, Hotmail, Yahoo, AOL, and others.

      - *(dict) --*

        An object that describes how email sent during the predictive inbox placement test was
        handled by a certain email provider.

        - **IspName** *(string) --*

          The name of the email provider that the inbox placement data applies to.

        - **PlacementStatistics** *(dict) --*

          An object that contains inbox placement metrics for a specific email provider.

          - **InboxPercentage** *(float) --*

            The percentage of emails that arrived in recipients' inboxes during the predictive
            inbox placement test.

          - **SpamPercentage** *(float) --*

            The percentage of emails that arrived in recipients' spam or junk mail folders during
            the predictive inbox placement test.

          - **MissingPercentage** *(float) --*

            The percentage of emails that didn't arrive in recipients' inboxes at all during the
            predictive inbox placement test.

          - **SpfPercentage** *(float) --*

            The percentage of emails that were authenticated by using Sender Policy Framework (SPF)
            during the predictive inbox placement test.

          - **DkimPercentage** *(float) --*

            The percentage of emails that were authenticated by using DomainKeys Identified Mail
            (DKIM) during the predictive inbox placement test.

    - **Message** *(string) --*

      An object that contains the message that you sent when you performed this predictive inbox
      placement test.

    - **Tags** *(list) --*

      An array of objects that define the tags (keys and values) that are associated with the
      predictive inbox placement test.

      - *(dict) --*

        An object that defines the tags that are associated with a resource. A *tag* is a label
        that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
        you categorize and manage resources in different ways, such as by purpose, owner,
        environment, or other criteria. A resource can have as many as 50 tags.

        Each tag consists of a required *tag key* and an associated *tag value* , both of which you
        define. A tag key is a general label that acts as a category for a more specific tag value.
        A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
        characters. A tag value can contain as many as 256 characters. The characters can be
        Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
        following additional restrictions apply to tags:

        * Tag keys and values are case sensitive.

        * For each associated resource, each tag key must be unique and it can have only one value.

        * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
        values that you define. In addition, you can't edit or remove tag keys or values that use
        this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
        resource.

        * You can associate tags with public or shared resources, but the tags are available only
        for your AWS account, not any other accounts that share the resource. In addition, the tags
        are available only for resources that are located in the specified AWS Region for your AWS
        account.

        - **Key** *(string) --*

          One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
          characters. The minimum length is 1 character.

        - **Value** *(string) --*

          The optional part of a key-value pair that defines a tag. The maximum length of a tag
          value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
          to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
          will set the value to an empty string.
    """


_ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef = TypedDict(
    "_ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)


class ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef(
    _ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef
):
    """
    Type definition for `ClientGetDomainDeliverabilityCampaignResponse` `DomainDeliverabilityCampaign`

    An object that contains the deliverability data for the campaign.

    - **CampaignId** *(string) --*

      The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns
      this identifier to a campaign. This value is not the same as the campaign identifier that
      Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon
      Pinpoint API or the Amazon Pinpoint console.

    - **ImageUrl** *(string) --*

      The URL of an image that contains a snapshot of the email message that was sent.

    - **Subject** *(string) --*

      The subject line, or title, of the email message.

    - **FromAddress** *(string) --*

      The verified email address that the email message was sent from.

    - **SendingIps** *(list) --*

      The IP addresses that were used to send the email message.

      - *(string) --*

        A dedicated IP address that is associated with your Amazon Pinpoint account.

    - **FirstSeenDateTime** *(datetime) --*

      The first time, in Unix time format, when the email message was delivered to any
      recipient's inbox. This value can help you determine how long it took for a campaign to
      deliver an email message.

    - **LastSeenDateTime** *(datetime) --*

      The last time, in Unix time format, when the email message was delivered to any recipient's
      inbox. This value can help you determine how long it took for a campaign to deliver an
      email message.

    - **InboxCount** *(integer) --*

      The number of email messages that were delivered to recipients’ inboxes.

    - **SpamCount** *(integer) --*

      The number of email messages that were delivered to recipients' spam or junk mail folders.

    - **ReadRate** *(float) --*

      The percentage of email messages that were opened by recipients. Due to technical
      limitations, this value only includes recipients who opened the message by using an email
      client that supports images.

    - **DeleteRate** *(float) --*

      The percentage of email messages that were deleted by recipients, without being opened
      first. Due to technical limitations, this value only includes recipients who opened the
      message by using an email client that supports images.

    - **ReadDeleteRate** *(float) --*

      The percentage of email messages that were opened and then deleted by recipients. Due to
      technical limitations, this value only includes recipients who opened the message by using
      an email client that supports images.

    - **ProjectedVolume** *(integer) --*

      The projected number of recipients that the email message was sent to.

    - **Esps** *(list) --*

      The major email providers who handled the email message.

      - *(string) --*
    """


_ClientGetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "_ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef
    },
    total=False,
)


class ClientGetDomainDeliverabilityCampaignResponseTypeDef(
    _ClientGetDomainDeliverabilityCampaignResponseTypeDef
):
    """
    Type definition for `ClientGetDomainDeliverabilityCampaign` `Response`

    An object that contains all the deliverability data for a specific campaign. This data is
    available for a campaign only if the campaign sent email by using a domain that the
    Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).

    - **DomainDeliverabilityCampaign** *(dict) --*

      An object that contains the deliverability data for the campaign.

      - **CampaignId** *(string) --*

        The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns
        this identifier to a campaign. This value is not the same as the campaign identifier that
        Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon
        Pinpoint API or the Amazon Pinpoint console.

      - **ImageUrl** *(string) --*

        The URL of an image that contains a snapshot of the email message that was sent.

      - **Subject** *(string) --*

        The subject line, or title, of the email message.

      - **FromAddress** *(string) --*

        The verified email address that the email message was sent from.

      - **SendingIps** *(list) --*

        The IP addresses that were used to send the email message.

        - *(string) --*

          A dedicated IP address that is associated with your Amazon Pinpoint account.

      - **FirstSeenDateTime** *(datetime) --*

        The first time, in Unix time format, when the email message was delivered to any
        recipient's inbox. This value can help you determine how long it took for a campaign to
        deliver an email message.

      - **LastSeenDateTime** *(datetime) --*

        The last time, in Unix time format, when the email message was delivered to any recipient's
        inbox. This value can help you determine how long it took for a campaign to deliver an
        email message.

      - **InboxCount** *(integer) --*

        The number of email messages that were delivered to recipients’ inboxes.

      - **SpamCount** *(integer) --*

        The number of email messages that were delivered to recipients' spam or junk mail folders.

      - **ReadRate** *(float) --*

        The percentage of email messages that were opened by recipients. Due to technical
        limitations, this value only includes recipients who opened the message by using an email
        client that supports images.

      - **DeleteRate** *(float) --*

        The percentage of email messages that were deleted by recipients, without being opened
        first. Due to technical limitations, this value only includes recipients who opened the
        message by using an email client that supports images.

      - **ReadDeleteRate** *(float) --*

        The percentage of email messages that were opened and then deleted by recipients. Due to
        technical limitations, this value only includes recipients who opened the message by using
        an email client that supports images.

      - **ProjectedVolume** *(integer) --*

        The projected number of recipients that the email message was sent to.

      - **Esps** *(list) --*

        The major email providers who handled the email message.

        - *(string) --*
    """


_ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponseDailyVolumes` `DomainIspPlacements`

    An object that contains inbox placement data for email sent from one of your email
    domains to a specific email provider.

    - **IspName** *(string) --*

      The name of the email provider that the inbox placement data applies to.

    - **InboxRawCount** *(integer) --*

      The total number of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' inboxes.

    - **SpamRawCount** *(integer) --*

      The total number of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' spam or junk mail folders.

    - **InboxPercentage** *(float) --*

      The percentage of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' inboxes.

    - **SpamPercentage** *(float) --*

      The percentage of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    {
        "InboxRawCount": int,
        "SpamRawCount": int,
        "ProjectedInbox": int,
        "ProjectedSpam": int,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponseDailyVolumes` `VolumeStatistics`

    An object that contains inbox placement metrics for a specific day in the analysis period.

    - **InboxRawCount** *(integer) --*

      The total number of emails that arrived in recipients' inboxes.

    - **SpamRawCount** *(integer) --*

      The total number of emails that arrived in recipients' spam or junk mail folders.

    - **ProjectedInbox** *(integer) --*

      An estimate of the percentage of emails sent from the current domain that will arrive
      in recipients' inboxes.

    - **ProjectedSpam** *(integer) --*

      An estimate of the percentage of emails sent from the current domain that will arrive
      in recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponse` `DailyVolumes`

    An object that contains information about the volume of email sent on each day of the
    analysis period.

    - **StartDate** *(datetime) --*

      The date that the DailyVolume metrics apply to, in Unix time.

    - **VolumeStatistics** *(dict) --*

      An object that contains inbox placement metrics for a specific day in the analysis period.

      - **InboxRawCount** *(integer) --*

        The total number of emails that arrived in recipients' inboxes.

      - **SpamRawCount** *(integer) --*

        The total number of emails that arrived in recipients' spam or junk mail folders.

      - **ProjectedInbox** *(integer) --*

        An estimate of the percentage of emails sent from the current domain that will arrive
        in recipients' inboxes.

      - **ProjectedSpam** *(integer) --*

        An estimate of the percentage of emails sent from the current domain that will arrive
        in recipients' spam or junk mail folders.

    - **DomainIspPlacements** *(list) --*

      An object that contains inbox placement metrics for a specified day in the analysis
      period, broken out by the recipient's email provider.

      - *(dict) --*

        An object that contains inbox placement data for email sent from one of your email
        domains to a specific email provider.

        - **IspName** *(string) --*

          The name of the email provider that the inbox placement data applies to.

        - **InboxRawCount** *(integer) --*

          The total number of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' inboxes.

        - **SpamRawCount** *(integer) --*

          The total number of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' spam or junk mail folders.

        - **InboxPercentage** *(float) --*

          The percentage of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' inboxes.

        - **SpamPercentage** *(float) --*

          The percentage of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponseOverallVolume` `DomainIspPlacements`

    An object that contains inbox placement data for email sent from one of your email
    domains to a specific email provider.

    - **IspName** *(string) --*

      The name of the email provider that the inbox placement data applies to.

    - **InboxRawCount** *(integer) --*

      The total number of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' inboxes.

    - **SpamRawCount** *(integer) --*

      The total number of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' spam or junk mail folders.

    - **InboxPercentage** *(float) --*

      The percentage of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' inboxes.

    - **SpamPercentage** *(float) --*

      The percentage of messages that were sent from the selected domain to the specified
      email provider that arrived in recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    {
        "InboxRawCount": int,
        "SpamRawCount": int,
        "ProjectedInbox": int,
        "ProjectedSpam": int,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponseOverallVolume` `VolumeStatistics`

    An object that contains information about the numbers of messages that arrived in
    recipients' inboxes and junk mail folders.

    - **InboxRawCount** *(integer) --*

      The total number of emails that arrived in recipients' inboxes.

    - **SpamRawCount** *(integer) --*

      The total number of emails that arrived in recipients' spam or junk mail folders.

    - **ProjectedInbox** *(integer) --*

      An estimate of the percentage of emails sent from the current domain that will arrive in
      recipients' inboxes.

    - **ProjectedSpam** *(integer) --*

      An estimate of the percentage of emails sent from the current domain that will arrive in
      recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    {
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef,
        "ReadRatePercent": float,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReportResponse` `OverallVolume`

    An object that contains deliverability metrics for the domain that you specified. The data in
    this object is a summary of all of the data that was collected from the ``StartDate`` to the
    ``EndDate`` .

    - **VolumeStatistics** *(dict) --*

      An object that contains information about the numbers of messages that arrived in
      recipients' inboxes and junk mail folders.

      - **InboxRawCount** *(integer) --*

        The total number of emails that arrived in recipients' inboxes.

      - **SpamRawCount** *(integer) --*

        The total number of emails that arrived in recipients' spam or junk mail folders.

      - **ProjectedInbox** *(integer) --*

        An estimate of the percentage of emails sent from the current domain that will arrive in
        recipients' inboxes.

      - **ProjectedSpam** *(integer) --*

        An estimate of the percentage of emails sent from the current domain that will arrive in
        recipients' spam or junk mail folders.

    - **ReadRatePercent** *(float) --*

      The percentage of emails that were sent from the domain that were read by their recipients.

    - **DomainIspPlacements** *(list) --*

      An object that contains inbox and junk mail placement metrics for individual email
      providers.

      - *(dict) --*

        An object that contains inbox placement data for email sent from one of your email
        domains to a specific email provider.

        - **IspName** *(string) --*

          The name of the email provider that the inbox placement data applies to.

        - **InboxRawCount** *(integer) --*

          The total number of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' inboxes.

        - **SpamRawCount** *(integer) --*

          The total number of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' spam or junk mail folders.

        - **InboxPercentage** *(float) --*

          The percentage of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' inboxes.

        - **SpamPercentage** *(float) --*

          The percentage of messages that were sent from the selected domain to the specified
          email provider that arrived in recipients' spam or junk mail folders.
    """


_ClientGetDomainStatisticsReportResponseTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef,
        "DailyVolumes": List[
            ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseTypeDef(
    _ClientGetDomainStatisticsReportResponseTypeDef
):
    """
    Type definition for `ClientGetDomainStatisticsReport` `Response`

    An object that includes statistics that are related to the domain that you specified.

    - **OverallVolume** *(dict) --*

      An object that contains deliverability metrics for the domain that you specified. The data in
      this object is a summary of all of the data that was collected from the ``StartDate`` to the
      ``EndDate`` .

      - **VolumeStatistics** *(dict) --*

        An object that contains information about the numbers of messages that arrived in
        recipients' inboxes and junk mail folders.

        - **InboxRawCount** *(integer) --*

          The total number of emails that arrived in recipients' inboxes.

        - **SpamRawCount** *(integer) --*

          The total number of emails that arrived in recipients' spam or junk mail folders.

        - **ProjectedInbox** *(integer) --*

          An estimate of the percentage of emails sent from the current domain that will arrive in
          recipients' inboxes.

        - **ProjectedSpam** *(integer) --*

          An estimate of the percentage of emails sent from the current domain that will arrive in
          recipients' spam or junk mail folders.

      - **ReadRatePercent** *(float) --*

        The percentage of emails that were sent from the domain that were read by their recipients.

      - **DomainIspPlacements** *(list) --*

        An object that contains inbox and junk mail placement metrics for individual email
        providers.

        - *(dict) --*

          An object that contains inbox placement data for email sent from one of your email
          domains to a specific email provider.

          - **IspName** *(string) --*

            The name of the email provider that the inbox placement data applies to.

          - **InboxRawCount** *(integer) --*

            The total number of messages that were sent from the selected domain to the specified
            email provider that arrived in recipients' inboxes.

          - **SpamRawCount** *(integer) --*

            The total number of messages that were sent from the selected domain to the specified
            email provider that arrived in recipients' spam or junk mail folders.

          - **InboxPercentage** *(float) --*

            The percentage of messages that were sent from the selected domain to the specified
            email provider that arrived in recipients' inboxes.

          - **SpamPercentage** *(float) --*

            The percentage of messages that were sent from the selected domain to the specified
            email provider that arrived in recipients' spam or junk mail folders.

    - **DailyVolumes** *(list) --*

      An object that contains deliverability metrics for the domain that you specified. This object
      contains data for each day, starting on the ``StartDate`` and ending on the ``EndDate`` .

      - *(dict) --*

        An object that contains information about the volume of email sent on each day of the
        analysis period.

        - **StartDate** *(datetime) --*

          The date that the DailyVolume metrics apply to, in Unix time.

        - **VolumeStatistics** *(dict) --*

          An object that contains inbox placement metrics for a specific day in the analysis period.

          - **InboxRawCount** *(integer) --*

            The total number of emails that arrived in recipients' inboxes.

          - **SpamRawCount** *(integer) --*

            The total number of emails that arrived in recipients' spam or junk mail folders.

          - **ProjectedInbox** *(integer) --*

            An estimate of the percentage of emails sent from the current domain that will arrive
            in recipients' inboxes.

          - **ProjectedSpam** *(integer) --*

            An estimate of the percentage of emails sent from the current domain that will arrive
            in recipients' spam or junk mail folders.

        - **DomainIspPlacements** *(list) --*

          An object that contains inbox placement metrics for a specified day in the analysis
          period, broken out by the recipient's email provider.

          - *(dict) --*

            An object that contains inbox placement data for email sent from one of your email
            domains to a specific email provider.

            - **IspName** *(string) --*

              The name of the email provider that the inbox placement data applies to.

            - **InboxRawCount** *(integer) --*

              The total number of messages that were sent from the selected domain to the specified
              email provider that arrived in recipients' inboxes.

            - **SpamRawCount** *(integer) --*

              The total number of messages that were sent from the selected domain to the specified
              email provider that arrived in recipients' spam or junk mail folders.

            - **InboxPercentage** *(float) --*

              The percentage of messages that were sent from the selected domain to the specified
              email provider that arrived in recipients' inboxes.

            - **SpamPercentage** *(float) --*

              The percentage of messages that were sent from the selected domain to the specified
              email provider that arrived in recipients' spam or junk mail folders.
    """


_ClientGetEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    {"SigningEnabled": bool, "Status": str, "Tokens": List[str]},
    total=False,
)


class ClientGetEmailIdentityResponseDkimAttributesTypeDef(
    _ClientGetEmailIdentityResponseDkimAttributesTypeDef
):
    """
    Type definition for `ClientGetEmailIdentityResponse` `DkimAttributes`

    An object that contains information about the DKIM attributes for the identity. This object
    includes the tokens that you use to create the CNAME records that are required to complete
    the DKIM verification process.

    - **SigningEnabled** *(boolean) --*

      If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity
      are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends
      from the identity aren't DKIM-signed.

    - **Status** *(string) --*

      Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the
      DNS records for the domain. The status can be one of the following:

      * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS
      configuration for the domain, but will continue to attempt to locate them.

      * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the
      domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email
      from the identity.

      * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings
      for the domain, and won't continue to search for them.

      * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
      determining the DKIM status for the domain.

      * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in
      the DKIM records for the domain.

    - **Tokens** *(list) --*

      A set of unique strings that you use to create a set of CNAME records that you add to the
      DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS
      configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint
      usually detects these records within about 72 hours of adding them to the DNS configuration
      for your domain.

      - *(string) --*
    """


_ClientGetEmailIdentityResponseMailFromAttributesTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    {"MailFromDomain": str, "MailFromDomainStatus": str, "BehaviorOnMxFailure": str},
    total=False,
)


class ClientGetEmailIdentityResponseMailFromAttributesTypeDef(
    _ClientGetEmailIdentityResponseMailFromAttributesTypeDef
):
    """
    Type definition for `ClientGetEmailIdentityResponse` `MailFromAttributes`

    An object that contains information about the Mail-From attributes for the email identity.

    - **MailFromDomain** *(string) --*

      The name of a domain that an email identity uses as a custom MAIL FROM domain.

    - **MailFromDomainStatus** *(string) --*

      The status of the MAIL FROM domain. This status can have the following values:

      * ``PENDING`` – Amazon Pinpoint hasn't started searching for the MX record yet.

      * ``SUCCESS`` – Amazon Pinpoint detected the required MX record for the MAIL FROM domain.

      * ``FAILED`` – Amazon Pinpoint can't find the required MX record, or the record no longer
      exists.

      * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
      determining the status of the MAIL FROM domain.

    - **BehaviorOnMxFailure** *(string) --*

      The action that Amazon Pinpoint to takes if it can't read the required MX record for a
      custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint
      uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage``
      , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to
      deliver the email.

      These behaviors are taken when the custom MAIL FROM domain configuration is in the
      ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
    """


_ClientGetEmailIdentityResponseTagsTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetEmailIdentityResponseTagsTypeDef(
    _ClientGetEmailIdentityResponseTagsTypeDef
):
    """
    Type definition for `ClientGetEmailIdentityResponse` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label
    that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
    you categorize and manage resources in different ways, such as by purpose, owner,
    environment, or other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value.
    A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be
    Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
    following additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
    values that you define. In addition, you can't edit or remove tag keys or values that use
    this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
    resource.

    * You can associate tags with public or shared resources, but the tags are available only
    for your AWS account, not any other accounts that share the resource. In addition, the tags
    are available only for resources that are located in the specified AWS Region for your AWS
    account.

    - **Key** *(string) --*

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --*

      The optional part of a key-value pair that defines a tag. The maximum length of a tag
      value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
      to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
      will set the value to an empty string.
    """


_ClientGetEmailIdentityResponseTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseTypeDef",
    {
        "IdentityType": str,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientGetEmailIdentityResponseDkimAttributesTypeDef,
        "MailFromAttributes": ClientGetEmailIdentityResponseMailFromAttributesTypeDef,
        "Tags": List[ClientGetEmailIdentityResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetEmailIdentityResponseTypeDef(_ClientGetEmailIdentityResponseTypeDef):
    """
    Type definition for `ClientGetEmailIdentity` `Response`

    Details about an email identity.

    - **IdentityType** *(string) --*

      The email identity type.

    - **FeedbackForwardingStatus** *(boolean) --*

      The feedback forwarding configuration for the identity.

      If the value is ``true`` , Amazon Pinpoint sends you email notifications when bounce or
      complaint events occur. Amazon Pinpoint sends this notification to the address that you
      specified in the Return-Path header of the original email.

      When you set this value to ``false`` , Amazon Pinpoint sends notifications through other
      mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're
      required to have a method of tracking bounces and complaints. If you haven't set up another
      mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email
      notification when these events occur (even if this setting is disabled).

    - **VerifiedForSendingStatus** *(boolean) --*

      Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send
      email from verified email addresses or domains. For more information about verifying
      identities, see the `Amazon Pinpoint User Guide
      <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html>`__ .

    - **DkimAttributes** *(dict) --*

      An object that contains information about the DKIM attributes for the identity. This object
      includes the tokens that you use to create the CNAME records that are required to complete
      the DKIM verification process.

      - **SigningEnabled** *(boolean) --*

        If the value is ``true`` , then the messages that Amazon Pinpoint sends from the identity
        are DKIM-signed. If the value is ``false`` , then the messages that Amazon Pinpoint sends
        from the identity aren't DKIM-signed.

      - **Status** *(string) --*

        Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the
        DNS records for the domain. The status can be one of the following:

        * ``PENDING`` – Amazon Pinpoint hasn't yet located the DKIM records in the DNS
        configuration for the domain, but will continue to attempt to locate them.

        * ``SUCCESS`` – Amazon Pinpoint located the DKIM records in the DNS configuration for the
        domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email
        from the identity.

        * ``FAILED`` – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings
        for the domain, and won't continue to search for them.

        * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
        determining the DKIM status for the domain.

        * ``NOT_STARTED`` – Amazon Pinpoint hasn't yet started searching for the DKIM records in
        the DKIM records for the domain.

      - **Tokens** *(list) --*

        A set of unique strings that you use to create a set of CNAME records that you add to the
        DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS
        configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint
        usually detects these records within about 72 hours of adding them to the DNS configuration
        for your domain.

        - *(string) --*

    - **MailFromAttributes** *(dict) --*

      An object that contains information about the Mail-From attributes for the email identity.

      - **MailFromDomain** *(string) --*

        The name of a domain that an email identity uses as a custom MAIL FROM domain.

      - **MailFromDomainStatus** *(string) --*

        The status of the MAIL FROM domain. This status can have the following values:

        * ``PENDING`` – Amazon Pinpoint hasn't started searching for the MX record yet.

        * ``SUCCESS`` – Amazon Pinpoint detected the required MX record for the MAIL FROM domain.

        * ``FAILED`` – Amazon Pinpoint can't find the required MX record, or the record no longer
        exists.

        * ``TEMPORARY_FAILURE`` – A temporary issue occurred, which prevented Amazon Pinpoint from
        determining the status of the MAIL FROM domain.

      - **BehaviorOnMxFailure** *(string) --*

        The action that Amazon Pinpoint to takes if it can't read the required MX record for a
        custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint
        uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage``
        , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to
        deliver the email.

        These behaviors are taken when the custom MAIL FROM domain configuration is in the
        ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.

    - **Tags** *(list) --*

      An array of objects that define the tags (keys and values) that are associated with the email
      identity.

      - *(dict) --*

        An object that defines the tags that are associated with a resource. A *tag* is a label
        that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
        you categorize and manage resources in different ways, such as by purpose, owner,
        environment, or other criteria. A resource can have as many as 50 tags.

        Each tag consists of a required *tag key* and an associated *tag value* , both of which you
        define. A tag key is a general label that acts as a category for a more specific tag value.
        A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
        characters. A tag value can contain as many as 256 characters. The characters can be
        Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
        following additional restrictions apply to tags:

        * Tag keys and values are case sensitive.

        * For each associated resource, each tag key must be unique and it can have only one value.

        * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
        values that you define. In addition, you can't edit or remove tag keys or values that use
        this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
        resource.

        * You can associate tags with public or shared resources, but the tags are available only
        for your AWS account, not any other accounts that share the resource. In addition, the tags
        are available only for resources that are located in the specified AWS Region for your AWS
        account.

        - **Key** *(string) --*

          One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
          characters. The minimum length is 1 character.

        - **Value** *(string) --*

          The optional part of a key-value pair that defines a tag. The maximum length of a tag
          value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
          to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
          will set the value to an empty string.
    """


_ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)


class ClientListConfigurationSetsResponseTypeDef(
    _ClientListConfigurationSetsResponseTypeDef
):
    """
    Type definition for `ClientListConfigurationSets` `Response`

    A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.

    - **ConfigurationSets** *(list) --*

      An array that contains all of the configuration sets in your Amazon Pinpoint account in the
      current AWS Region.

      - *(string) --*

        The name of a configuration set.

        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the
        emails you send. You apply a configuration set to an email by including a reference to the
        configuration set in the headers of the email. When you apply a configuration set to an
        email, all of the rules in that configuration set are applied to the email.

    - **NextToken** *(string) --*

      A token that indicates that there are additional configuration sets to list. To view
      additional configuration sets, issue another request to ``ListConfigurationSets`` , and pass
      this token in the ``NextToken`` parameter.
    """


_ClientListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "_ClientListDedicatedIpPoolsResponseTypeDef",
    {"DedicatedIpPools": List[str], "NextToken": str},
    total=False,
)


class ClientListDedicatedIpPoolsResponseTypeDef(
    _ClientListDedicatedIpPoolsResponseTypeDef
):
    """
    Type definition for `ClientListDedicatedIpPools` `Response`

    A list of dedicated IP pools.

    - **DedicatedIpPools** *(list) --*

      A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.

      - *(string) --*

        The name of a dedicated IP pool.

    - **NextToken** *(string) --*

      A token that indicates that there are additional IP pools to list. To view additional IP
      pools, issue another request to ``ListDedicatedIpPools`` , passing this token in the
      ``NextToken`` parameter.
    """


_ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef = TypedDict(
    "_ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": str,
    },
    total=False,
)


class ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef(
    _ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef
):
    """
    Type definition for `ClientListDeliverabilityTestReportsResponse` `DeliverabilityTestReports`

    An object that contains metadata related to a predictive inbox placement test.

    - **ReportId** *(string) --*

      A unique string that identifies the predictive inbox placement test.

    - **ReportName** *(string) --*

      A name that helps you identify a predictive inbox placement test report.

    - **Subject** *(string) --*

      The subject line for an email that you submitted in a predictive inbox placement test.

    - **FromEmailAddress** *(string) --*

      The sender address that you specified for the predictive inbox placement test.

    - **CreateDate** *(datetime) --*

      The date and time when the predictive inbox placement test was created, in Unix time
      format.

    - **DeliverabilityTestStatus** *(string) --*

      The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` ,
      then the predictive inbox placement test is currently running. Predictive inbox placement
      tests are usually complete within 24 hours of creating the test. If the status is
      ``COMPLETE`` , then the test is finished, and you can use the
      ``GetDeliverabilityTestReport`` to view the results of the test.
    """


_ClientListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "_ClientListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List[
            ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDeliverabilityTestReportsResponseTypeDef(
    _ClientListDeliverabilityTestReportsResponseTypeDef
):
    """
    Type definition for `ClientListDeliverabilityTestReports` `Response`

    A list of the predictive inbox placement test reports that are available for your account,
    regardless of whether or not those tests are complete.

    - **DeliverabilityTestReports** *(list) --*

      An object that contains a lists of predictive inbox placement tests that you've performed.

      - *(dict) --*

        An object that contains metadata related to a predictive inbox placement test.

        - **ReportId** *(string) --*

          A unique string that identifies the predictive inbox placement test.

        - **ReportName** *(string) --*

          A name that helps you identify a predictive inbox placement test report.

        - **Subject** *(string) --*

          The subject line for an email that you submitted in a predictive inbox placement test.

        - **FromEmailAddress** *(string) --*

          The sender address that you specified for the predictive inbox placement test.

        - **CreateDate** *(datetime) --*

          The date and time when the predictive inbox placement test was created, in Unix time
          format.

        - **DeliverabilityTestStatus** *(string) --*

          The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` ,
          then the predictive inbox placement test is currently running. Predictive inbox placement
          tests are usually complete within 24 hours of creating the test. If the status is
          ``COMPLETE`` , then the test is finished, and you can use the
          ``GetDeliverabilityTestReport`` to view the results of the test.

    - **NextToken** *(string) --*

      A token that indicates that there are additional predictive inbox placement tests to list. To
      view additional predictive inbox placement tests, issue another request to
      ``ListDeliverabilityTestReports`` , and pass this token in the ``NextToken`` parameter.
    """


_ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef = TypedDict(
    "_ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)


class ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef(
    _ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef
):
    """
    Type definition for `ClientListDomainDeliverabilityCampaignsResponse` `DomainDeliverabilityCampaigns`

    An object that contains the deliverability data for a specific campaign. This data is
    available for a campaign only if the campaign sent email by using a domain that the
    Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).

    - **CampaignId** *(string) --*

      The unique identifier for the campaign. Amazon Pinpoint automatically generates and
      assigns this identifier to a campaign. This value is not the same as the campaign
      identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using
      the Amazon Pinpoint API or the Amazon Pinpoint console.

    - **ImageUrl** *(string) --*

      The URL of an image that contains a snapshot of the email message that was sent.

    - **Subject** *(string) --*

      The subject line, or title, of the email message.

    - **FromAddress** *(string) --*

      The verified email address that the email message was sent from.

    - **SendingIps** *(list) --*

      The IP addresses that were used to send the email message.

      - *(string) --*

        A dedicated IP address that is associated with your Amazon Pinpoint account.

    - **FirstSeenDateTime** *(datetime) --*

      The first time, in Unix time format, when the email message was delivered to any
      recipient's inbox. This value can help you determine how long it took for a campaign to
      deliver an email message.

    - **LastSeenDateTime** *(datetime) --*

      The last time, in Unix time format, when the email message was delivered to any
      recipient's inbox. This value can help you determine how long it took for a campaign to
      deliver an email message.

    - **InboxCount** *(integer) --*

      The number of email messages that were delivered to recipients’ inboxes.

    - **SpamCount** *(integer) --*

      The number of email messages that were delivered to recipients' spam or junk mail folders.

    - **ReadRate** *(float) --*

      The percentage of email messages that were opened by recipients. Due to technical
      limitations, this value only includes recipients who opened the message by using an email
      client that supports images.

    - **DeleteRate** *(float) --*

      The percentage of email messages that were deleted by recipients, without being opened
      first. Due to technical limitations, this value only includes recipients who opened the
      message by using an email client that supports images.

    - **ReadDeleteRate** *(float) --*

      The percentage of email messages that were opened and then deleted by recipients. Due to
      technical limitations, this value only includes recipients who opened the message by
      using an email client that supports images.

    - **ProjectedVolume** *(integer) --*

      The projected number of recipients that the email message was sent to.

    - **Esps** *(list) --*

      The major email providers who handled the email message.

      - *(string) --*
    """


_ClientListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "_ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List[
            ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDomainDeliverabilityCampaignsResponseTypeDef(
    _ClientListDomainDeliverabilityCampaignsResponseTypeDef
):
    """
    Type definition for `ClientListDomainDeliverabilityCampaigns` `Response`

    An array of objects that provide deliverability data for all the campaigns that used a specific
    domain to send email during a specified time range. This data is available for a domain only if
    you enabled the Deliverability dashboard (``PutDeliverabilityDashboardOption`` operation) for
    the domain.

    - **DomainDeliverabilityCampaigns** *(list) --*

      An array of responses, one for each campaign that used the domain to send email during the
      specified time range.

      - *(dict) --*

        An object that contains the deliverability data for a specific campaign. This data is
        available for a campaign only if the campaign sent email by using a domain that the
        Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).

        - **CampaignId** *(string) --*

          The unique identifier for the campaign. Amazon Pinpoint automatically generates and
          assigns this identifier to a campaign. This value is not the same as the campaign
          identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using
          the Amazon Pinpoint API or the Amazon Pinpoint console.

        - **ImageUrl** *(string) --*

          The URL of an image that contains a snapshot of the email message that was sent.

        - **Subject** *(string) --*

          The subject line, or title, of the email message.

        - **FromAddress** *(string) --*

          The verified email address that the email message was sent from.

        - **SendingIps** *(list) --*

          The IP addresses that were used to send the email message.

          - *(string) --*

            A dedicated IP address that is associated with your Amazon Pinpoint account.

        - **FirstSeenDateTime** *(datetime) --*

          The first time, in Unix time format, when the email message was delivered to any
          recipient's inbox. This value can help you determine how long it took for a campaign to
          deliver an email message.

        - **LastSeenDateTime** *(datetime) --*

          The last time, in Unix time format, when the email message was delivered to any
          recipient's inbox. This value can help you determine how long it took for a campaign to
          deliver an email message.

        - **InboxCount** *(integer) --*

          The number of email messages that were delivered to recipients’ inboxes.

        - **SpamCount** *(integer) --*

          The number of email messages that were delivered to recipients' spam or junk mail folders.

        - **ReadRate** *(float) --*

          The percentage of email messages that were opened by recipients. Due to technical
          limitations, this value only includes recipients who opened the message by using an email
          client that supports images.

        - **DeleteRate** *(float) --*

          The percentage of email messages that were deleted by recipients, without being opened
          first. Due to technical limitations, this value only includes recipients who opened the
          message by using an email client that supports images.

        - **ReadDeleteRate** *(float) --*

          The percentage of email messages that were opened and then deleted by recipients. Due to
          technical limitations, this value only includes recipients who opened the message by
          using an email client that supports images.

        - **ProjectedVolume** *(integer) --*

          The projected number of recipients that the email message was sent to.

        - **Esps** *(list) --*

          The major email providers who handled the email message.

          - *(string) --*

    - **NextToken** *(string) --*

      A token that’s returned from a previous call to the ``ListDomainDeliverabilityCampaigns``
      operation. This token indicates the position of the campaign in the list of campaigns.
    """


_ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef = TypedDict(
    "_ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    {"IdentityType": str, "IdentityName": str, "SendingEnabled": bool},
    total=False,
)


class ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef(
    _ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef
):
    """
    Type definition for `ClientListEmailIdentitiesResponse` `EmailIdentities`

    Information about an email identity.

    - **IdentityType** *(string) --*

      The email identity type. The identity type can be one of the following:

      * ``EMAIL_ADDRESS`` – The identity is an email address.

      * ``DOMAIN`` – The identity is a domain.

      * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.

    - **IdentityName** *(string) --*

      The address or domain of the identity.

    - **SendingEnabled** *(boolean) --*

      Indicates whether or not you can send email from the identity.

      In Amazon Pinpoint, an identity is an email address or domain that you send email from.
      Before you can send email from an identity, you have to demostrate that you own the
      identity, and that you authorize Amazon Pinpoint to send email from that identity.
    """


_ClientListEmailIdentitiesResponseTypeDef = TypedDict(
    "_ClientListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List[
            ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEmailIdentitiesResponseTypeDef(
    _ClientListEmailIdentitiesResponseTypeDef
):
    """
    Type definition for `ClientListEmailIdentities` `Response`

    A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint,
    regardless of whether or not those identities were successfully verified.

    - **EmailIdentities** *(list) --*

      An array that includes all of the identities associated with your Amazon Pinpoint account.

      - *(dict) --*

        Information about an email identity.

        - **IdentityType** *(string) --*

          The email identity type. The identity type can be one of the following:

          * ``EMAIL_ADDRESS`` – The identity is an email address.

          * ``DOMAIN`` – The identity is a domain.

          * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.

        - **IdentityName** *(string) --*

          The address or domain of the identity.

        - **SendingEnabled** *(boolean) --*

          Indicates whether or not you can send email from the identity.

          In Amazon Pinpoint, an identity is an email address or domain that you send email from.
          Before you can send email from an identity, you have to demostrate that you own the
          identity, and that you authorize Amazon Pinpoint to send email from that identity.

    - **NextToken** *(string) --*

      A token that indicates that there are additional configuration sets to list. To view
      additional configuration sets, issue another request to ``ListEmailIdentities`` , and pass
      this token in the ``NextToken`` parameter.
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

    An object that defines the tags that are associated with a resource. A *tag* is a label
    that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
    you categorize and manage resources in different ways, such as by purpose, owner,
    environment, or other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value.
    A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be
    Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
    following additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
    values that you define. In addition, you can't edit or remove tag keys or values that use
    this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
    resource.

    * You can associate tags with public or shared resources, but the tags are available only
    for your AWS account, not any other accounts that share the resource. In addition, the tags
    are available only for resources that are located in the specified AWS Region for your AWS
    account.

    - **Key** *(string) --*

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --*

      The optional part of a key-value pair that defines a tag. The maximum length of a tag
      value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
      to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
      will set the value to an empty string.
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

      An array that lists all the tags that are associated with the resource. Each tag consists of
      a required tag key (``Key`` ) and an associated tag value (``Value`` )

      - *(dict) --*

        An object that defines the tags that are associated with a resource. A *tag* is a label
        that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
        you categorize and manage resources in different ways, such as by purpose, owner,
        environment, or other criteria. A resource can have as many as 50 tags.

        Each tag consists of a required *tag key* and an associated *tag value* , both of which you
        define. A tag key is a general label that acts as a category for a more specific tag value.
        A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
        characters. A tag value can contain as many as 256 characters. The characters can be
        Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The
        following additional restrictions apply to tags:

        * Tag keys and values are case sensitive.

        * For each associated resource, each tag key must be unique and it can have only one value.

        * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
        values that you define. In addition, you can't edit or remove tag keys or values that use
        this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
        resource.

        * You can associate tags with public or shared resources, but the tags are available only
        for your AWS account, not any other accounts that share the resource. In addition, the tags
        are available only for resources that are located in the specified AWS Region for your AWS
        account.

        - **Key** *(string) --*

          One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
          characters. The minimum length is 1 character.

        - **Value** *(string) --*

          The optional part of a key-value pair that defines a tag. The maximum length of a tag
          value is 256 characters. The minimum length is 0 characters. If you don’t want a resource
          to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint
          will set the value to an empty string.
    """


_ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    """
    Type definition for `ClientPutDeliverabilityDashboardOptionSubscribedDomains` `InboxPlacementTrackingOption`

    An object that contains information about the inbox placement data settings for the domain.

    - **Global** *(boolean) --*

      Specifies whether inbox placement data is being tracked for the domain.

    - **TrackedIsps** *(list) --*

      An array of strings, one for each major email provider that the inbox placement data
      applies to.

      - *(string) --*

        The name of an email provider.
    """


_ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef = TypedDict(
    "_ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef(
    _ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef
):
    """
    Type definition for `ClientPutDeliverabilityDashboardOption` `SubscribedDomains`

    An object that contains information about the Deliverability dashboard subscription for a
    verified domain that you use to send email and currently has an active Deliverability dashboard
    subscription. If a Deliverability dashboard subscription is active for a domain, you gain
    access to reputation, inbox placement, and other metrics for the domain.

    - **Domain** *(string) --*

      A verified domain that’s associated with your AWS account and currently has an active
      Deliverability dashboard subscription.

    - **SubscriptionStartDate** *(datetime) --*

      The date, in Unix time format, when you enabled the Deliverability dashboard for the domain.

    - **InboxPlacementTrackingOption** *(dict) --*

      An object that contains information about the inbox placement data settings for the domain.

      - **Global** *(boolean) --*

        Specifies whether inbox placement data is being tracked for the domain.

      - **TrackedIsps** *(list) --*

        An array of strings, one for each major email provider that the inbox placement data
        applies to.

        - *(string) --*

          The name of an email provider.
    """


_ClientSendEmailContentRawTypeDef = TypedDict(
    "_ClientSendEmailContentRawTypeDef", {"Data": bytes}
)


class ClientSendEmailContentRawTypeDef(_ClientSendEmailContentRawTypeDef):
    """
    Type definition for `ClientSendEmailContent` `Raw`

    The raw email message. The message has to meet the following criteria:

    * The message has to contain a header and a body, separated by one blank line.

    * All of the required header fields must be present in the message.

    * Each part of a multipart MIME message must be formatted properly.

    * If you include attachments, they must be in a file format that Amazon Pinpoint supports.

    * The entire message must be Base64 encoded.

    * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
    character range, you should encode that content to ensure that recipients' email clients render
    the message properly.

    * The length of any single line of text in the message can't exceed 1,000 characters. This
    restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **Data** *(bytes) --* **[REQUIRED]**

      The raw email message. The message has to meet the following criteria:

      * The message has to contain a header and a body, separated by one blank line.

      * All of the required header fields must be present in the message.

      * Each part of a multipart MIME message must be formatted properly.

      * Attachments must be in a file format that Amazon Pinpoint supports.

      * The entire message must be Base64 encoded.

      * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
      character range, you should encode that content to ensure that recipients' email clients
      render the message properly.

      * The length of any single line of text in the message can't exceed 1,000 characters. This
      restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .
    """


_RequiredClientSendEmailContentSimpleBodyHtmlTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleBodyHtmlTypeDef", {"Data": str}
)
_OptionalClientSendEmailContentSimpleBodyHtmlTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleBodyHtmlTypeDef",
    {"Charset": str},
    total=False,
)


class ClientSendEmailContentSimpleBodyHtmlTypeDef(
    _RequiredClientSendEmailContentSimpleBodyHtmlTypeDef,
    _OptionalClientSendEmailContentSimpleBodyHtmlTypeDef,
):
    """
    Type definition for `ClientSendEmailContentSimpleBody` `Html`

    An object that represents the version of the message that is displayed in email clients
    that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol,
      Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
      the ASCII range, you have to specify a character set. For example, you could specify
      ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_RequiredClientSendEmailContentSimpleBodyTextTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleBodyTextTypeDef", {"Data": str}
)
_OptionalClientSendEmailContentSimpleBodyTextTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleBodyTextTypeDef",
    {"Charset": str},
    total=False,
)


class ClientSendEmailContentSimpleBodyTextTypeDef(
    _RequiredClientSendEmailContentSimpleBodyTextTypeDef,
    _OptionalClientSendEmailContentSimpleBodyTextTypeDef,
):
    """
    Type definition for `ClientSendEmailContentSimpleBody` `Text`

    An object that represents the version of the message that is displayed in email clients
    that don't support HTML, or clients where the recipient has disabled HTML rendering.

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol,
      Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
      the ASCII range, you have to specify a character set. For example, you could specify
      ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientSendEmailContentSimpleBodyTypeDef = TypedDict(
    "_ClientSendEmailContentSimpleBodyTypeDef",
    {
        "Text": ClientSendEmailContentSimpleBodyTextTypeDef,
        "Html": ClientSendEmailContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)


class ClientSendEmailContentSimpleBodyTypeDef(_ClientSendEmailContentSimpleBodyTypeDef):
    """
    Type definition for `ClientSendEmailContentSimple` `Body`

    The body of the message. You can specify an HTML version of the message, a text-only version
    of the message, or both.

    - **Text** *(dict) --*

      An object that represents the version of the message that is displayed in email clients
      that don't support HTML, or clients where the recipient has disabled HTML rendering.

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol,
        Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
        the ASCII range, you have to specify a character set. For example, you could specify
        ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Html** *(dict) --*

      An object that represents the version of the message that is displayed in email clients
      that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol,
        Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
        the ASCII range, you have to specify a character set. For example, you could specify
        ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_RequiredClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailContentSimpleSubjectTypeDef(
    _RequiredClientSendEmailContentSimpleSubjectTypeDef,
    _OptionalClientSendEmailContentSimpleSubjectTypeDef,
):
    """
    Type definition for `ClientSendEmailContentSimple` `Subject`

    The subject line of the email. The subject line can only contain 7-bit ASCII characters.
    However, you can specify non-ASCII characters in the subject line by using encoded-word
    syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

    - **Data** *(string) --* **[REQUIRED]**

      The content of the message itself.

    - **Charset** *(string) --*

      The character set for the content. Because of the constraints of the SMTP protocol, Amazon
      Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
      range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
      ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientSendEmailContentSimpleTypeDef = TypedDict(
    "_ClientSendEmailContentSimpleTypeDef",
    {
        "Subject": ClientSendEmailContentSimpleSubjectTypeDef,
        "Body": ClientSendEmailContentSimpleBodyTypeDef,
    },
)


class ClientSendEmailContentSimpleTypeDef(_ClientSendEmailContentSimpleTypeDef):
    """
    Type definition for `ClientSendEmailContent` `Simple`

    The simple email message. The message consists of a subject and a message body.

    - **Subject** *(dict) --* **[REQUIRED]**

      The subject line of the email. The subject line can only contain 7-bit ASCII characters.
      However, you can specify non-ASCII characters in the subject line by using encoded-word
      syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

      - **Data** *(string) --* **[REQUIRED]**

        The content of the message itself.

      - **Charset** *(string) --*

        The character set for the content. Because of the constraints of the SMTP protocol, Amazon
        Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
        range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
        ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Body** *(dict) --* **[REQUIRED]**

      The body of the message. You can specify an HTML version of the message, a text-only version
      of the message, or both.

      - **Text** *(dict) --*

        An object that represents the version of the message that is displayed in email clients
        that don't support HTML, or clients where the recipient has disabled HTML rendering.

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol,
          Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
          the ASCII range, you have to specify a character set. For example, you could specify
          ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

      - **Html** *(dict) --*

        An object that represents the version of the message that is displayed in email clients
        that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol,
          Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
          the ASCII range, you have to specify a character set. For example, you could specify
          ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .
    """


_ClientSendEmailContentTemplateTypeDef = TypedDict(
    "_ClientSendEmailContentTemplateTypeDef",
    {"TemplateArn": str, "TemplateData": str},
    total=False,
)


class ClientSendEmailContentTemplateTypeDef(_ClientSendEmailContentTemplateTypeDef):
    """
    Type definition for `ClientSendEmailContent` `Template`

    The template to use for the email message.

    - **TemplateArn** *(string) --*

      The Amazon Resource Name (ARN) of the template.

    - **TemplateData** *(string) --*

      An object that defines the values to use for message variables in the template. This object
      is a set of key-value pairs. Each key defines a message variable in the template. The
      corresponding value defines the value to use for that variable.
    """


_ClientSendEmailContentTypeDef = TypedDict(
    "_ClientSendEmailContentTypeDef",
    {
        "Simple": ClientSendEmailContentSimpleTypeDef,
        "Raw": ClientSendEmailContentRawTypeDef,
        "Template": ClientSendEmailContentTemplateTypeDef,
    },
    total=False,
)


class ClientSendEmailContentTypeDef(_ClientSendEmailContentTypeDef):
    """
    Type definition for `ClientSendEmail` `Content`

    An object that contains the body of the message. You can send either a Simple message or a Raw
    message.

    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.

      - **Subject** *(dict) --* **[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .

        - **Data** *(string) --* **[REQUIRED]**

          The content of the message itself.

        - **Charset** *(string) --*

          The character set for the content. Because of the constraints of the SMTP protocol, Amazon
          Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII
          range, you have to specify a character set. For example, you could specify ``UTF-8`` ,
          ``ISO-8859-1`` , or ``Shift_JIS`` .

      - **Body** *(dict) --* **[REQUIRED]**

        The body of the message. You can specify an HTML version of the message, a text-only version
        of the message, or both.

        - **Text** *(dict) --*

          An object that represents the version of the message that is displayed in email clients
          that don't support HTML, or clients where the recipient has disabled HTML rendering.

          - **Data** *(string) --* **[REQUIRED]**

            The content of the message itself.

          - **Charset** *(string) --*

            The character set for the content. Because of the constraints of the SMTP protocol,
            Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
            the ASCII range, you have to specify a character set. For example, you could specify
            ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

        - **Html** *(dict) --*

          An object that represents the version of the message that is displayed in email clients
          that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

          - **Data** *(string) --* **[REQUIRED]**

            The content of the message itself.

          - **Charset** *(string) --*

            The character set for the content. Because of the constraints of the SMTP protocol,
            Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of
            the ASCII range, you have to specify a character set. For example, you could specify
            ``UTF-8`` , ``ISO-8859-1`` , or ``Shift_JIS`` .

    - **Raw** *(dict) --*

      The raw email message. The message has to meet the following criteria:

      * The message has to contain a header and a body, separated by one blank line.

      * All of the required header fields must be present in the message.

      * Each part of a multipart MIME message must be formatted properly.

      * If you include attachments, they must be in a file format that Amazon Pinpoint supports.

      * The entire message must be Base64 encoded.

      * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
      character range, you should encode that content to ensure that recipients' email clients render
      the message properly.

      * The length of any single line of text in the message can't exceed 1,000 characters. This
      restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

      - **Data** *(bytes) --* **[REQUIRED]**

        The raw email message. The message has to meet the following criteria:

        * The message has to contain a header and a body, separated by one blank line.

        * All of the required header fields must be present in the message.

        * Each part of a multipart MIME message must be formatted properly.

        * Attachments must be in a file format that Amazon Pinpoint supports.

        * The entire message must be Base64 encoded.

        * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
        character range, you should encode that content to ensure that recipients' email clients
        render the message properly.

        * The length of any single line of text in the message can't exceed 1,000 characters. This
        restriction is defined in `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

    - **Template** *(dict) --*

      The template to use for the email message.

      - **TemplateArn** *(string) --*

        The Amazon Resource Name (ARN) of the template.

      - **TemplateData** *(string) --*

        An object that defines the values to use for message variables in the template. This object
        is a set of key-value pairs. Each key defines a message variable in the template. The
        corresponding value defines the value to use for that variable.
    """


_ClientSendEmailDestinationTypeDef = TypedDict(
    "_ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendEmailDestinationTypeDef(_ClientSendEmailDestinationTypeDef):
    """
    Type definition for `ClientSendEmail` `Destination`

    An object that contains the recipients of the email message.

    - **ToAddresses** *(list) --*

      An array that contains the email addresses of the "To" recipients for the email.

      - *(string) --*

    - **CcAddresses** *(list) --*

      An array that contains the email addresses of the "CC" (carbon copy) recipients for the email.

      - *(string) --*

    - **BccAddresses** *(list) --*

      An array that contains the email addresses of the "BCC" (blind carbon copy) recipients for the
      email.

      - *(string) --*
    """


_ClientSendEmailEmailTagsTypeDef = TypedDict(
    "_ClientSendEmailEmailTagsTypeDef", {"Name": str, "Value": str}
)


class ClientSendEmailEmailTagsTypeDef(_ClientSendEmailEmailTagsTypeDef):
    """
    Type definition for `ClientSendEmail` `EmailTags`

    Contains the name and value of a tag that you apply to an email. You can use message tags when
    you publish email sending events.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the message tag. The message tag name has to meet the following criteria:

      * It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).

      * It can contain no more than 256 characters.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the message tag. The message tag value has to meet the following criteria:

      * It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).

      * It can contain no more than 256 characters.
    """


_ClientSendEmailResponseTypeDef = TypedDict(
    "_ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendEmailResponseTypeDef(_ClientSendEmailResponseTypeDef):
    """
    Type definition for `ClientSendEmail` `Response`

    A unique message ID that you receive when Amazon Pinpoint accepts an email for sending.

    - **MessageId** *(string) --*

      A unique identifier for the message that is generated when Amazon Pinpoint accepts the
      message.

      .. note::

        It is possible for Amazon Pinpoint to accept a message without sending it. This can happen
        when the message you're trying to send has an attachment doesn't pass a virus check, or
        when you send a templated email that contains invalid personalization content, for example.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    An object that defines the tags that are associated with a resource. A *tag* is a label that
    you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
    categorize and manage resources in different ways, such as by purpose, owner, environment, or
    other criteria. A resource can have as many as 50 tags.

    Each tag consists of a required *tag key* and an associated *tag value* , both of which you
    define. A tag key is a general label that acts as a category for a more specific tag value. A
    tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
    characters. A tag value can contain as many as 256 characters. The characters can be Unicode
    letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
    additional restrictions apply to tags:

    * Tag keys and values are case sensitive.

    * For each associated resource, each tag key must be unique and it can have only one value.

    * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
    that you define. In addition, you can't edit or remove tag keys or values that use this prefix.
    Tags that use this prefix don’t count against the limit of 50 tags per resource.

    * You can associate tags with public or shared resources, but the tags are available only for
    your AWS account, not any other accounts that share the resource. In addition, the tags are
    available only for resources that are located in the specified AWS Region for your AWS account.

    - **Key** *(string) --* **[REQUIRED]**

      One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
      characters. The minimum length is 1 character.

    - **Value** *(string) --* **[REQUIRED]**

      The optional part of a key-value pair that defines a tag. The maximum length of a tag value
      is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a
      specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the
      value to an empty string.
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

    An object that defines the dimension configuration to use when you send Amazon Pinpoint
    email events to Amazon CloudWatch.

    - **DimensionName** *(string) --* **[REQUIRED]**

      The name of an Amazon CloudWatch dimension associated with an email sending metric. The
      name has to meet the following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
      (-).

      * It can contain no more than 256 characters.

    - **DimensionValueSource** *(string) --* **[REQUIRED]**

      The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
      CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
      X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
      ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
      ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

    - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

      The default value of the dimension that is published to Amazon CloudWatch if you don't
      provide the value of the dimension when you send an email. This value has to meet the
      following criteria:

      * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
      (-).

      * It can contain no more than 256 characters.
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

    An object that defines an Amazon CloudWatch destination for email events. You can use Amazon
    CloudWatch to monitor and gain insights on your email sending metrics.

    - **DimensionConfigurations** *(list) --* **[REQUIRED]**

      An array of objects that define the dimensions to use when you send email events to Amazon
      CloudWatch.

      - *(dict) --*

        An object that defines the dimension configuration to use when you send Amazon Pinpoint
        email events to Amazon CloudWatch.

        - **DimensionName** *(string) --* **[REQUIRED]**

          The name of an Amazon CloudWatch dimension associated with an email sending metric. The
          name has to meet the following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
          (-).

          * It can contain no more than 256 characters.

        - **DimensionValueSource** *(string) --* **[REQUIRED]**

          The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
          CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
          X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
          ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
          ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

        - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

          The default value of the dimension that is published to Amazon CloudWatch if you don't
          provide the value of the dimension when you send an email. This value has to meet the
          following criteria:

          * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
          (-).

          * It can contain no more than 256 characters.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IamRoleArn": str, "DeliveryStreamArn": str},
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `KinesisFirehoseDestination`

    An object that defines an Amazon Kinesis Data Firehose destination for email events. You can
    use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon
    Redshift.

    - **IamRoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email
      events to the Amazon Kinesis Data Firehose stream.

    - **DeliveryStreamArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
      Pinpoint sends email events to.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `PinpointDestination`

    An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
    Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes
    to create segments for your campaigns.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email
      events to.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestinationEventDestination` `SnsDestination`

    An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to
    send notification when certain email events occur.

    - **TopicArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events
      to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
      <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[str],
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestination` `EventDestination`

    An object that defines the event destination.

    - **Enabled** *(boolean) --*

      If ``true`` , the event destination is enabled. When the event destination is enabled, the
      specified event types are sent to the destinations in this ``EventDestinationDefinition`` .

      If ``false`` , the event destination is disabled. When the event destination is disabled,
      events aren't sent to the specified destinations.

    - **MatchingEventTypes** *(list) --*

      An array that specifies which events Amazon Pinpoint should send to the destinations in this
      ``EventDestinationDefinition`` .

      - *(string) --*

        An email sending event type. For example, email sends, opens, and bounces are all email
        events.

    - **KinesisFirehoseDestination** *(dict) --*

      An object that defines an Amazon Kinesis Data Firehose destination for email events. You can
      use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon
      Redshift.

      - **IamRoleArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email
        events to the Amazon Kinesis Data Firehose stream.

      - **DeliveryStreamArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon
        Pinpoint sends email events to.

    - **CloudWatchDestination** *(dict) --*

      An object that defines an Amazon CloudWatch destination for email events. You can use Amazon
      CloudWatch to monitor and gain insights on your email sending metrics.

      - **DimensionConfigurations** *(list) --* **[REQUIRED]**

        An array of objects that define the dimensions to use when you send email events to Amazon
        CloudWatch.

        - *(dict) --*

          An object that defines the dimension configuration to use when you send Amazon Pinpoint
          email events to Amazon CloudWatch.

          - **DimensionName** *(string) --* **[REQUIRED]**

            The name of an Amazon CloudWatch dimension associated with an email sending metric. The
            name has to meet the following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
            (-).

            * It can contain no more than 256 characters.

          - **DimensionValueSource** *(string) --* **[REQUIRED]**

            The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon
            CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an
            X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose
            ``messageTag`` . If you want Amazon Pinpoint to use your own email headers, choose
            ``emailHeader`` . If you want Amazon Pinpoint to use link tags, choose ``linkTags`` .

          - **DefaultDimensionValue** *(string) --* **[REQUIRED]**

            The default value of the dimension that is published to Amazon CloudWatch if you don't
            provide the value of the dimension when you send an email. This value has to meet the
            following criteria:

            * It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes
            (-).

            * It can contain no more than 256 characters.

    - **SnsDestination** *(dict) --*

      An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to
      send notification when certain email events occur.

      - **TopicArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events
        to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide
        <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

    - **PinpointDestination** *(dict) --*

      An object that defines a Amazon Pinpoint destination for email events. You can use Amazon
      Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes
      to create segments for your campaigns.

      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email
        events to.
    """


_GetDedicatedIpsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDedicatedIpsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDedicatedIpsPaginatePaginationConfigTypeDef(
    _GetDedicatedIpsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDedicatedIpsPaginate` `PaginationConfig`

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


_GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef = TypedDict(
    "_GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef",
    {"Ip": str, "WarmupStatus": str, "WarmupPercentage": int, "PoolName": str},
    total=False,
)


class GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef(
    _GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef
):
    """
    Type definition for `GetDedicatedIpsPaginateResponse` `DedicatedIps`

    Contains information about a dedicated IP address that is associated with your Amazon
    Pinpoint account.

    - **Ip** *(string) --*

      An IP address that is reserved for use by your Amazon Pinpoint account.

    - **WarmupStatus** *(string) --*

      The warm-up status of a dedicated IP address. The status can have one of the following
      values:

      * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
      process is ongoing.

      * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
      use.

    - **WarmupPercentage** *(integer) --*

      Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
      address has completed the warm-up process and is ready for use.

    - **PoolName** *(string) --*

      The name of the dedicated IP pool that the IP address is associated with.
    """


_GetDedicatedIpsPaginateResponseTypeDef = TypedDict(
    "_GetDedicatedIpsPaginateResponseTypeDef",
    {"DedicatedIps": List[GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef]},
    total=False,
)


class GetDedicatedIpsPaginateResponseTypeDef(_GetDedicatedIpsPaginateResponseTypeDef):
    """
    Type definition for `GetDedicatedIpsPaginate` `Response`

    Information about the dedicated IP addresses that are associated with your Amazon Pinpoint
    account.

    - **DedicatedIps** *(list) --*

      A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.

      - *(dict) --*

        Contains information about a dedicated IP address that is associated with your Amazon
        Pinpoint account.

        - **Ip** *(string) --*

          An IP address that is reserved for use by your Amazon Pinpoint account.

        - **WarmupStatus** *(string) --*

          The warm-up status of a dedicated IP address. The status can have one of the following
          values:

          * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up
          process is ongoing.

          * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to
          use.

        - **WarmupPercentage** *(integer) --*

          Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the
          address has completed the warm-up process and is ready for use.

        - **PoolName** *(string) --*

          The name of the dedicated IP pool that the IP address is associated with.
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


_ListConfigurationSetsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseTypeDef",
    {"ConfigurationSets": List[str]},
    total=False,
)


class ListConfigurationSetsPaginateResponseTypeDef(
    _ListConfigurationSetsPaginateResponseTypeDef
):
    """
    Type definition for `ListConfigurationSetsPaginate` `Response`

    A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.

    - **ConfigurationSets** *(list) --*

      An array that contains all of the configuration sets in your Amazon Pinpoint account in the
      current AWS Region.

      - *(string) --*

        The name of a configuration set.

        In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the
        emails you send. You apply a configuration set to an email by including a reference to the
        configuration set in the headers of the email. When you apply a configuration set to an
        email, all of the rules in that configuration set are applied to the email.
    """


_ListDedicatedIpPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDedicatedIpPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDedicatedIpPoolsPaginatePaginationConfigTypeDef(
    _ListDedicatedIpPoolsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDedicatedIpPoolsPaginate` `PaginationConfig`

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


_ListDedicatedIpPoolsPaginateResponseTypeDef = TypedDict(
    "_ListDedicatedIpPoolsPaginateResponseTypeDef",
    {"DedicatedIpPools": List[str]},
    total=False,
)


class ListDedicatedIpPoolsPaginateResponseTypeDef(
    _ListDedicatedIpPoolsPaginateResponseTypeDef
):
    """
    Type definition for `ListDedicatedIpPoolsPaginate` `Response`

    A list of dedicated IP pools.

    - **DedicatedIpPools** *(list) --*

      A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.

      - *(string) --*

        The name of a dedicated IP pool.
    """


_ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef(
    _ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeliverabilityTestReportsPaginate` `PaginationConfig`

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


_ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": str,
    },
    total=False,
)


class ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef(
    _ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef
):
    """
    Type definition for `ListDeliverabilityTestReportsPaginateResponse` `DeliverabilityTestReports`

    An object that contains metadata related to a predictive inbox placement test.

    - **ReportId** *(string) --*

      A unique string that identifies the predictive inbox placement test.

    - **ReportName** *(string) --*

      A name that helps you identify a predictive inbox placement test report.

    - **Subject** *(string) --*

      The subject line for an email that you submitted in a predictive inbox placement test.

    - **FromEmailAddress** *(string) --*

      The sender address that you specified for the predictive inbox placement test.

    - **CreateDate** *(datetime) --*

      The date and time when the predictive inbox placement test was created, in Unix time
      format.

    - **DeliverabilityTestStatus** *(string) --*

      The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` ,
      then the predictive inbox placement test is currently running. Predictive inbox placement
      tests are usually complete within 24 hours of creating the test. If the status is
      ``COMPLETE`` , then the test is finished, and you can use the
      ``GetDeliverabilityTestReport`` to view the results of the test.
    """


_ListDeliverabilityTestReportsPaginateResponseTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginateResponseTypeDef",
    {
        "DeliverabilityTestReports": List[
            ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef
        ]
    },
    total=False,
)


class ListDeliverabilityTestReportsPaginateResponseTypeDef(
    _ListDeliverabilityTestReportsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeliverabilityTestReportsPaginate` `Response`

    A list of the predictive inbox placement test reports that are available for your account,
    regardless of whether or not those tests are complete.

    - **DeliverabilityTestReports** *(list) --*

      An object that contains a lists of predictive inbox placement tests that you've performed.

      - *(dict) --*

        An object that contains metadata related to a predictive inbox placement test.

        - **ReportId** *(string) --*

          A unique string that identifies the predictive inbox placement test.

        - **ReportName** *(string) --*

          A name that helps you identify a predictive inbox placement test report.

        - **Subject** *(string) --*

          The subject line for an email that you submitted in a predictive inbox placement test.

        - **FromEmailAddress** *(string) --*

          The sender address that you specified for the predictive inbox placement test.

        - **CreateDate** *(datetime) --*

          The date and time when the predictive inbox placement test was created, in Unix time
          format.

        - **DeliverabilityTestStatus** *(string) --*

          The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` ,
          then the predictive inbox placement test is currently running. Predictive inbox placement
          tests are usually complete within 24 hours of creating the test. If the status is
          ``COMPLETE`` , then the test is finished, and you can use the
          ``GetDeliverabilityTestReport`` to view the results of the test.
    """


_ListEmailIdentitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEmailIdentitiesPaginatePaginationConfigTypeDef(
    _ListEmailIdentitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEmailIdentitiesPaginate` `PaginationConfig`

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


_ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef",
    {"IdentityType": str, "IdentityName": str, "SendingEnabled": bool},
    total=False,
)


class ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef(
    _ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef
):
    """
    Type definition for `ListEmailIdentitiesPaginateResponse` `EmailIdentities`

    Information about an email identity.

    - **IdentityType** *(string) --*

      The email identity type. The identity type can be one of the following:

      * ``EMAIL_ADDRESS`` – The identity is an email address.

      * ``DOMAIN`` – The identity is a domain.

      * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.

    - **IdentityName** *(string) --*

      The address or domain of the identity.

    - **SendingEnabled** *(boolean) --*

      Indicates whether or not you can send email from the identity.

      In Amazon Pinpoint, an identity is an email address or domain that you send email from.
      Before you can send email from an identity, you have to demostrate that you own the
      identity, and that you authorize Amazon Pinpoint to send email from that identity.
    """


_ListEmailIdentitiesPaginateResponseTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginateResponseTypeDef",
    {
        "EmailIdentities": List[
            ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef
        ]
    },
    total=False,
)


class ListEmailIdentitiesPaginateResponseTypeDef(
    _ListEmailIdentitiesPaginateResponseTypeDef
):
    """
    Type definition for `ListEmailIdentitiesPaginate` `Response`

    A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint,
    regardless of whether or not those identities were successfully verified.

    - **EmailIdentities** *(list) --*

      An array that includes all of the identities associated with your Amazon Pinpoint account.

      - *(dict) --*

        Information about an email identity.

        - **IdentityType** *(string) --*

          The email identity type. The identity type can be one of the following:

          * ``EMAIL_ADDRESS`` – The identity is an email address.

          * ``DOMAIN`` – The identity is a domain.

          * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.

        - **IdentityName** *(string) --*

          The address or domain of the identity.

        - **SendingEnabled** *(boolean) --*

          Indicates whether or not you can send email from the identity.

          In Amazon Pinpoint, an identity is an email address or domain that you send email from.
          Before you can send email from an identity, you have to demostrate that you own the
          identity, and that you authorize Amazon Pinpoint to send email from that identity.
    """
