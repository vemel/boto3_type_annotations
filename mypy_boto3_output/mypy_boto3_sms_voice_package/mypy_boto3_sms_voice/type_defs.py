"Main interface for sms-voice type defs"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientSendVoiceMessageResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
)


_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": Dict[str, Any],
        "Enabled": bool,
        "KinesisFirehoseDestination": Dict[str, Any],
        "MatchingEventTypes": List[Any],
        "SnsDestination": Dict[str, Any],
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationSetEventDestination` `EventDestination`

    - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.

      - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want to
      record events in.

    - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If the
    event destination is enabled, then Amazon Pinpoint sends response data to the specified event
    destination.

    - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an event
    destination that sends data to Amazon Kinesis Data Firehose.

      - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that can
      write data to an Amazon Kinesis Data Firehose stream.

      - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
      Firehose destination that you want to use in the event destination.

    - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each EventDestination
    object includes ARNs and other information that define an event destination.

      - *(string) --* The types of events that are sent to the event destination.

    - **SnsDestination** *(dict) --* An object that contains information about an event destination
    that sends data to Amazon SNS.

      - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that you
      want to publish events to.
    """


_ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {"EventDestinations": List[Any]},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseTypeDef
):
    """
    Type definition for `ClientGetConfigurationSetEventDestinations` `Response`

    - **EventDestinations** *(list) --* An array of EventDestination objects. Each EventDestination
    object includes ARNs and other information that define an event destination.

      - *(dict) --* An object that defines an event destination.

        - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an
        event destination that sends data to Amazon CloudWatch Logs.

          - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and
          Access Management (IAM) role that is able to write event data to an Amazon CloudWatch
          destination.

          - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want
          to record events in.

        - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If
        the event destination is enabled, then Amazon Pinpoint sends response data to the specified
        event destination.

        - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an
        event destination that sends data to Amazon Kinesis Data Firehose.

          - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that
          can write data to an Amazon Kinesis Data Firehose stream.

          - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
          Firehose destination that you want to use in the event destination.

        - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each
        EventDestination object includes ARNs and other information that define an event
        destination.

          - *(string) --* The types of events that are sent to the event destination.

        - **Name** *(string) --* A name that identifies the event destination configuration.

        - **SnsDestination** *(dict) --* An object that contains information about an event
        destination that sends data to Amazon SNS.

          - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that
          you want to publish events to.
    """


_ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[Any], "NextToken": str},
    total=False,
)


class ClientListConfigurationSetsResponseTypeDef(
    _ClientListConfigurationSetsResponseTypeDef
):
    """
    Type definition for `ClientListConfigurationSets` `Response`

    - **ConfigurationSets** *(list) --* An object that contains a list of configuration sets for
    your account in the current region.

      - *(string) --*

    - **NextToken** *(string) --* A token returned from a previous call to ListConfigurationSets to
    indicate the position in the list of configuration sets.
    """


_ClientSendVoiceMessageResponseTypeDef = TypedDict(
    "_ClientSendVoiceMessageResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendVoiceMessageResponseTypeDef(_ClientSendVoiceMessageResponseTypeDef):
    """
    Type definition for `ClientSendVoiceMessage` `Response`

    - **MessageId** *(string) --* A unique identifier for the voice message.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": Dict[str, Any],
        "Enabled": bool,
        "KinesisFirehoseDestination": Dict[str, Any],
        "MatchingEventTypes": List[Any],
        "SnsDestination": Dict[str, Any],
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationSetEventDestination` `EventDestination`

    - **CloudWatchLogsDestination** *(dict) --* An object that contains information about an event
    destination that sends data to Amazon CloudWatch Logs.

      - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of an Amazon Identity and Access
      Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.

      - **LogGroupArn** *(string) --* The name of the Amazon CloudWatch Log Group that you want to
      record events in.

    - **Enabled** *(boolean) --* Indicates whether or not the event destination is enabled. If the
    event destination is enabled, then Amazon Pinpoint sends response data to the specified event
    destination.

    - **KinesisFirehoseDestination** *(dict) --* An object that contains information about an event
    destination that sends data to Amazon Kinesis Data Firehose.

      - **DeliveryStreamArn** *(string) --* The Amazon Resource Name (ARN) of an IAM role that can
      write data to an Amazon Kinesis Data Firehose stream.

      - **IamRoleArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon Kinesis Data
      Firehose destination that you want to use in the event destination.

    - **MatchingEventTypes** *(list) --* An array of EventDestination objects. Each EventDestination
    object includes ARNs and other information that define an event destination.

      - *(string) --* The types of events that are sent to the event destination.

    - **SnsDestination** *(dict) --* An object that contains information about an event destination
    that sends data to Amazon SNS.

      - **TopicArn** *(string) --* The Amazon Resource Name (ARN) of the Amazon SNS topic that you
      want to publish events to.
    """
