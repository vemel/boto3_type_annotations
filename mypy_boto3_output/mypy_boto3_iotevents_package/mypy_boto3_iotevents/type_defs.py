"Main interface for iotevents type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientCreateDetectorModelResponseTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef",
    "ClientCreateDetectorModeldetectorModelDefinitionTypeDef",
    "ClientCreateDetectorModeltagsTypeDef",
    "ClientCreateInputResponseinputConfigurationTypeDef",
    "ClientCreateInputResponseTypeDef",
    "ClientCreateInputinputDefinitionattributesTypeDef",
    "ClientCreateInputinputDefinitionTypeDef",
    "ClientCreateInputtagsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    "ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    "ClientDescribeDetectorModelResponseTypeDef",
    "ClientDescribeInputResponseinputinputConfigurationTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    "ClientDescribeInputResponseinputinputDefinitionTypeDef",
    "ClientDescribeInputResponseinputTypeDef",
    "ClientDescribeInputResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    "ClientListDetectorModelVersionsResponseTypeDef",
    "ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    "ClientListDetectorModelsResponseTypeDef",
    "ClientListInputsResponseinputSummariesTypeDef",
    "ClientListInputsResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef",
    "ClientPutLoggingOptionsloggingOptionsTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    "ClientUpdateDetectorModelResponseTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef",
    "ClientUpdateDetectorModeldetectorModelDefinitionTypeDef",
    "ClientUpdateInputResponseinputConfigurationTypeDef",
    "ClientUpdateInputResponseTypeDef",
    "ClientUpdateInputinputDefinitionattributesTypeDef",
    "ClientUpdateInputinputDefinitionTypeDef",
)


_ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "_ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "key": str,
        "evaluationMethod": str,
    },
    total=False,
)


class ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef(
    _ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDetectorModelResponse` `detectorModelConfiguration`

    Information about how the detector model is configured.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **detectorModelVersion** *(string) --*

      The version of the detector model.

    - **detectorModelDescription** *(string) --*

      A brief description of the detector model.

    - **detectorModelArn** *(string) --*

      The ARN of the detector model.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT Events to perform its operations.

    - **creationTime** *(datetime) --*

      The time the detector model was created.

    - **lastUpdateTime** *(datetime) --*

      The time the detector model was last updated.

    - **status** *(string) --*

      The status of the detector model.

    - **key** *(string) --*

      The input attribute key used to identify a device or system to create a detector (an
      instance of the detector model) and then to route each input received to the appropriate
      detector (instance). This parameter uses a JSON-path expression to specify the
      attribute-value pair in the message payload of each input that is used to identify the
      device associated with the input.

    - **evaluationMethod** *(string) --*

      When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
      that the events are defined. When set to ``BATCH`` , variables are updated and events
      performed only after all event conditions are evaluated.
    """


_ClientCreateDetectorModelResponseTypeDef = TypedDict(
    "_ClientCreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientCreateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)


class ClientCreateDetectorModelResponseTypeDef(
    _ClientCreateDetectorModelResponseTypeDef
):
    """
    Type definition for `ClientCreateDetectorModel` `Response`

    - **detectorModelConfiguration** *(dict) --*

      Information about how the detector model is configured.

      - **detectorModelName** *(string) --*

        The name of the detector model.

      - **detectorModelVersion** *(string) --*

        The version of the detector model.

      - **detectorModelDescription** *(string) --*

        A brief description of the detector model.

      - **detectorModelArn** *(string) --*

        The ARN of the detector model.

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Events to perform its operations.

      - **creationTime** *(datetime) --*

        The time the detector model was created.

      - **lastUpdateTime** *(datetime) --*

        The time the detector model was last updated.

      - **status** *(string) --*

        The status of the detector model.

      - **key** *(string) --*

        The input attribute key used to identify a device or system to create a detector (an
        instance of the detector model) and then to route each input received to the appropriate
        detector (instance). This parameter uses a JSON-path expression to specify the
        attribute-value pair in the message payload of each input that is used to identify the
        device associated with the input.

      - **evaluationMethod** *(string) --*

        When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
        that the events are defined. When set to ``BATCH`` , variables are updated and events
        performed only after all event conditions are evaluated.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {"eventName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonEnter` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    {
        "events": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstates` `onEnter`

    When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

    - **events** *(list) --*

      Specifies the actions that are performed when the state is entered and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExitevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {"eventName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonExit` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    {
        "events": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstates` `onExit`

    When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
    TRUE.

    - **events** *(list) --*

      Specifies the ``"actions"`` that are performed when the state is exited and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {"eventName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInput` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEvents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {"eventName": str, "condition": str, "nextState": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "actions": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstatesonInput` `transitionEvents`

    Specifies the actions performed and the next state entered when a ``"condition"``
    evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the transition event.

    - **condition** *(string) --* **[REQUIRED]**

      [Required] A Boolean expression that when TRUE causes the actions to be performed and
      the ``"nextState"`` to be entered.

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).

    - **nextState** *(string) --* **[REQUIRED]**

      The next state to enter.
    """


_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
        ],
        "transitionEvents": List[
            ClientCreateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinitionstates` `onInput`

    When an input is received and the ``"condition"`` is TRUE, perform the specified
    ``"actions"`` .

    - **events** *(list) --*

      Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).

    - **transitionEvents** *(list) --*

      Specifies the actions performed, and the next state entered, when a ``"condition"``
      evaluates to TRUE.

      - *(dict) --*

        Specifies the actions performed and the next state entered when a ``"condition"``
        evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the transition event.

        - **condition** *(string) --* **[REQUIRED]**

          [Required] A Boolean expression that when TRUE causes the actions to be performed and
          the ``"nextState"`` to be entered.

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).

        - **nextState** *(string) --* **[REQUIRED]**

          The next state to enter.
    """


_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef",
    {"stateName": str},
)
_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientCreateDetectorModeldetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientCreateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientCreateDetectorModeldetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef(
    _RequiredClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef,
    _OptionalClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef,
):
    """
    Type definition for `ClientCreateDetectorModeldetectorModelDefinition` `states`

    Information that defines a state of a detector.

    - **stateName** *(string) --* **[REQUIRED]**

      The name of the state.

    - **onInput** *(dict) --*

      When an input is received and the ``"condition"`` is TRUE, perform the specified
      ``"actions"`` .

      - **events** *(list) --*

        Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

      - **transitionEvents** *(list) --*

        Specifies the actions performed, and the next state entered, when a ``"condition"``
        evaluates to TRUE.

        - *(dict) --*

          Specifies the actions performed and the next state entered when a ``"condition"``
          evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the transition event.

          - **condition** *(string) --* **[REQUIRED]**

            [Required] A Boolean expression that when TRUE causes the actions to be performed and
            the ``"nextState"`` to be entered.

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

          - **nextState** *(string) --* **[REQUIRED]**

            The next state to enter.

    - **onEnter** *(dict) --*

      When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

      - **events** *(list) --*

        Specifies the actions that are performed when the state is entered and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

    - **onExit** *(dict) --*

      When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
      TRUE.

      - **events** *(list) --*

        Specifies the ``"actions"`` that are performed when the state is exited and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateDetectorModeldetectorModelDefinitionTypeDef = TypedDict(
    "_ClientCreateDetectorModeldetectorModelDefinitionTypeDef",
    {
        "states": List[ClientCreateDetectorModeldetectorModelDefinitionstatesTypeDef],
        "initialStateName": str,
    },
)


class ClientCreateDetectorModeldetectorModelDefinitionTypeDef(
    _ClientCreateDetectorModeldetectorModelDefinitionTypeDef
):
    """
    Type definition for `ClientCreateDetectorModel` `detectorModelDefinition`

    Information that defines how the detectors operate.

    - **states** *(list) --* **[REQUIRED]**

      Information about the states of the detector.

      - *(dict) --*

        Information that defines a state of a detector.

        - **stateName** *(string) --* **[REQUIRED]**

          The name of the state.

        - **onInput** *(dict) --*

          When an input is received and the ``"condition"`` is TRUE, perform the specified
          ``"actions"`` .

          - **events** *(list) --*

            Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

          - **transitionEvents** *(list) --*

            Specifies the actions performed, and the next state entered, when a ``"condition"``
            evaluates to TRUE.

            - *(dict) --*

              Specifies the actions performed and the next state entered when a ``"condition"``
              evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the transition event.

              - **condition** *(string) --* **[REQUIRED]**

                [Required] A Boolean expression that when TRUE causes the actions to be performed and
                the ``"nextState"`` to be entered.

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

              - **nextState** *(string) --* **[REQUIRED]**

                The next state to enter.

        - **onEnter** *(dict) --*

          When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

          - **events** *(list) --*

            Specifies the actions that are performed when the state is entered and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

        - **onExit** *(dict) --*

          When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
          TRUE.

          - **events** *(list) --*

            Specifies the ``"actions"`` that are performed when the state is exited and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

    - **initialStateName** *(string) --* **[REQUIRED]**

      The state that is entered at the creation of each detector (instance).
    """


_ClientCreateDetectorModeltagsTypeDef = TypedDict(
    "_ClientCreateDetectorModeltagsTypeDef", {"key": str, "value": str}
)


class ClientCreateDetectorModeltagsTypeDef(_ClientCreateDetectorModeltagsTypeDef):
    """
    Type definition for `ClientCreateDetectorModel` `tags`

    Metadata that can be used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientCreateInputResponseinputConfigurationTypeDef = TypedDict(
    "_ClientCreateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientCreateInputResponseinputConfigurationTypeDef(
    _ClientCreateInputResponseinputConfigurationTypeDef
):
    """
    Type definition for `ClientCreateInputResponse` `inputConfiguration`

    Information about the configuration of the input.

    - **inputName** *(string) --*

      The name of the input.

    - **inputDescription** *(string) --*

      A brief description of the input.

    - **inputArn** *(string) --*

      The ARN of the input.

    - **creationTime** *(datetime) --*

      The time the input was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the input was updated.

    - **status** *(string) --*

      The status of the input.
    """


_ClientCreateInputResponseTypeDef = TypedDict(
    "_ClientCreateInputResponseTypeDef",
    {"inputConfiguration": ClientCreateInputResponseinputConfigurationTypeDef},
    total=False,
)


class ClientCreateInputResponseTypeDef(_ClientCreateInputResponseTypeDef):
    """
    Type definition for `ClientCreateInput` `Response`

    - **inputConfiguration** *(dict) --*

      Information about the configuration of the input.

      - **inputName** *(string) --*

        The name of the input.

      - **inputDescription** *(string) --*

        A brief description of the input.

      - **inputArn** *(string) --*

        The ARN of the input.

      - **creationTime** *(datetime) --*

        The time the input was created.

      - **lastUpdateTime** *(datetime) --*

        The last time the input was updated.

      - **status** *(string) --*

        The status of the input.
    """


_ClientCreateInputinputDefinitionattributesTypeDef = TypedDict(
    "_ClientCreateInputinputDefinitionattributesTypeDef", {"jsonPath": str}
)


class ClientCreateInputinputDefinitionattributesTypeDef(
    _ClientCreateInputinputDefinitionattributesTypeDef
):
    """
    Type definition for `ClientCreateInputinputDefinition` `attributes`

    The attributes from the JSON payload that are made available by the input. Inputs are derived
    from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
    contains a JSON payload, and those attributes (and their paired values) specified here are
    available for use in the ``condition`` expressions used by detectors.

    - **jsonPath** *(string) --* **[REQUIRED]**

      An expression that specifies an attribute-value pair in a JSON structure. Use this to
      specify an attribute from the JSON payload that is made available by the input. Inputs are
      derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
      message contains a JSON payload, and the attribute (and its paired value) specified here
      are available for use in the ``"condition"`` expressions used by detectors.

      Syntax: ``<field-name>.<field-name>...``
    """


_ClientCreateInputinputDefinitionTypeDef = TypedDict(
    "_ClientCreateInputinputDefinitionTypeDef",
    {"attributes": List[ClientCreateInputinputDefinitionattributesTypeDef]},
)


class ClientCreateInputinputDefinitionTypeDef(_ClientCreateInputinputDefinitionTypeDef):
    """
    Type definition for `ClientCreateInput` `inputDefinition`

    The definition of the input.

    - **attributes** *(list) --* **[REQUIRED]**

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``"condition"`` expressions used by detectors that monitor this input.

      - *(dict) --*

        The attributes from the JSON payload that are made available by the input. Inputs are derived
        from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
        contains a JSON payload, and those attributes (and their paired values) specified here are
        available for use in the ``condition`` expressions used by detectors.

        - **jsonPath** *(string) --* **[REQUIRED]**

          An expression that specifies an attribute-value pair in a JSON structure. Use this to
          specify an attribute from the JSON payload that is made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
          message contains a JSON payload, and the attribute (and its paired value) specified here
          are available for use in the ``"condition"`` expressions used by detectors.

          Syntax: ``<field-name>.<field-name>...``
    """


_ClientCreateInputtagsTypeDef = TypedDict(
    "_ClientCreateInputtagsTypeDef", {"key": str, "value": str}
)


class ClientCreateInputtagsTypeDef(_ClientCreateInputtagsTypeDef):
    """
    Type definition for `ClientCreateInput` `tags`

    Metadata that can be used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "key": str,
        "evaluationMethod": str,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModel` `detectorModelConfiguration`

    Information about how the detector is configured.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **detectorModelVersion** *(string) --*

      The version of the detector model.

    - **detectorModelDescription** *(string) --*

      A brief description of the detector model.

    - **detectorModelArn** *(string) --*

      The ARN of the detector model.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT Events to perform its operations.

    - **creationTime** *(datetime) --*

      The time the detector model was created.

    - **lastUpdateTime** *(datetime) --*

      The time the detector model was last updated.

    - **status** *(string) --*

      The status of the detector model.

    - **key** *(string) --*

      The input attribute key used to identify a device or system to create a detector (an
      instance of the detector model) and then to route each input received to the appropriate
      detector (instance). This parameter uses a JSON-path expression to specify the
      attribute-value pair in the message payload of each input that is used to identify the
      device associated with the input.

    - **evaluationMethod** *(string) --*

      When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
      order that the events are defined. When set to ``BATCH`` , variables are updated and
      events performed only after all event conditions are evaluated.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --*

      The name of the timer to clear.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `firehose`

    Sends information about the detector model instance and the event which
    triggered the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --*

      The name of the Kinesis Data Firehose delivery stream where the data is
      written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the
      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message
    broker.

    - **mqttTopic** *(string) --*

      The MQTT topic of the message.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector
    model instance and the event which triggered the action.

    - **functionArn** *(string) --*

      The ARN of the AWS Lambda function which is executed.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --*

      The name of the timer to reset.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --*

      The name of the timer.

    - **seconds** *(integer) --*

      The number of seconds until the timer expires. The minimum value is 60
      seconds to ensure accuracy.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --*

      The name of the variable.

    - **value** *(string) --*

      The new value of the variable.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --*

      The ARN of the Amazon SNS target where the message is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sqs`

    Sends information about the detector model instance and the event which
    triggered the action to an Amazon SQS queue.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --*

        The name of the variable.

      - **value** *(string) --*

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --*

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message
      broker.

      - **mqttTopic** *(string) --*

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --*

        The name of the timer.

      - **seconds** *(integer) --*

        The number of seconds until the timer expires. The minimum value is 60
        seconds to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --*

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --*

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector
      model instance and the event which triggered the action.

      - **functionArn** *(string) --*

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to an Amazon SQS queue.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --*

        The name of the Kinesis Data Firehose delivery stream where the data is
        written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the
        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnter` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
    TRUE.

    - **eventName** *(string) --*

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --*

            The name of the variable.

          - **value** *(string) --*

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --*

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message
          broker.

          - **mqttTopic** *(string) --*

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --*

            The name of the timer.

          - **seconds** *(integer) --*

            The number of seconds until the timer expires. The minimum value is 60
            seconds to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --*

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --*

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector
          model instance and the event which triggered the action.

          - **functionArn** *(string) --*

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to an Amazon SQS queue.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --*

            The name of the Kinesis Data Firehose delivery stream where the data is
            written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the
            Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
            '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstates` `onEnter`

    When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

    - **events** *(list) --*

      Specifies the actions that are performed when the state is entered and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
        TRUE.

        - **eventName** *(string) --*

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --*

                The name of the variable.

              - **value** *(string) --*

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --*

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message
              broker.

              - **mqttTopic** *(string) --*

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --*

                The name of the timer.

              - **seconds** *(integer) --*

                The number of seconds until the timer expires. The minimum value is 60
                seconds to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --*

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --*

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector
              model instance and the event which triggered the action.

              - **functionArn** *(string) --*

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --*

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to an Amazon SQS queue.

              - **queueUrl** *(string) --*

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --*

                The name of the Kinesis Data Firehose delivery stream where the data is
                written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the
                Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --*

      The name of the timer to clear.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `firehose`

    Sends information about the detector model instance and the event which
    triggered the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --*

      The name of the Kinesis Data Firehose delivery stream where the data is
      written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the
      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message
    broker.

    - **mqttTopic** *(string) --*

      The MQTT topic of the message.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector
    model instance and the event which triggered the action.

    - **functionArn** *(string) --*

      The ARN of the AWS Lambda function which is executed.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --*

      The name of the timer to reset.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --*

      The name of the timer.

    - **seconds** *(integer) --*

      The number of seconds until the timer expires. The minimum value is 60
      seconds to ensure accuracy.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --*

      The name of the variable.

    - **value** *(string) --*

      The new value of the variable.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --*

      The ARN of the Amazon SNS target where the message is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sqs`

    Sends information about the detector model instance and the event which
    triggered the action to an Amazon SQS queue.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --*

        The name of the variable.

      - **value** *(string) --*

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --*

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message
      broker.

      - **mqttTopic** *(string) --*

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --*

        The name of the timer.

      - **seconds** *(integer) --*

        The number of seconds until the timer expires. The minimum value is 60
        seconds to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --*

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --*

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector
      model instance and the event which triggered the action.

      - **functionArn** *(string) --*

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to an Amazon SQS queue.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --*

        The name of the Kinesis Data Firehose delivery stream where the data is
        written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the
        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExit` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
    TRUE.

    - **eventName** *(string) --*

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --*

            The name of the variable.

          - **value** *(string) --*

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --*

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message
          broker.

          - **mqttTopic** *(string) --*

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --*

            The name of the timer.

          - **seconds** *(integer) --*

            The number of seconds until the timer expires. The minimum value is 60
            seconds to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --*

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --*

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector
          model instance and the event which triggered the action.

          - **functionArn** *(string) --*

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to an Amazon SQS queue.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --*

            The name of the Kinesis Data Firehose delivery stream where the data is
            written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the
            Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
            '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstates` `onExit`

    When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
    is TRUE.

    - **events** *(list) --*

      Specifies the ``"actions"`` that are performed when the state is exited and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
        TRUE.

        - **eventName** *(string) --*

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --*

                The name of the variable.

              - **value** *(string) --*

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --*

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message
              broker.

              - **mqttTopic** *(string) --*

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --*

                The name of the timer.

              - **seconds** *(integer) --*

                The number of seconds until the timer expires. The minimum value is 60
                seconds to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --*

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --*

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector
              model instance and the event which triggered the action.

              - **functionArn** *(string) --*

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --*

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to an Amazon SQS queue.

              - **queueUrl** *(string) --*

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --*

                The name of the Kinesis Data Firehose delivery stream where the data is
                written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the
                Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --*

      The name of the timer to clear.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `firehose`

    Sends information about the detector model instance and the event which
    triggered the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --*

      The name of the Kinesis Data Firehose delivery stream where the data is
      written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the
      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message
    broker.

    - **mqttTopic** *(string) --*

      The MQTT topic of the message.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector
    model instance and the event which triggered the action.

    - **functionArn** *(string) --*

      The ARN of the AWS Lambda function which is executed.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --*

      The name of the timer to reset.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --*

      The name of the timer.

    - **seconds** *(integer) --*

      The number of seconds until the timer expires. The minimum value is 60
      seconds to ensure accuracy.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --*

      The name of the variable.

    - **value** *(string) --*

      The new value of the variable.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --*

      The ARN of the Amazon SNS target where the message is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sqs`

    Sends information about the detector model instance and the event which
    triggered the action to an Amazon SQS queue.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --*

        The name of the variable.

      - **value** *(string) --*

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --*

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message
      broker.

      - **mqttTopic** *(string) --*

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --*

        The name of the timer.

      - **seconds** *(integer) --*

        The number of seconds until the timer expires. The minimum value is 60
        seconds to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --*

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --*

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector
      model instance and the event which triggered the action.

      - **functionArn** *(string) --*

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to an Amazon SQS queue.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --*

        The name of the Kinesis Data Firehose delivery stream where the data is
        written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the
        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInput` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
    TRUE.

    - **eventName** *(string) --*

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --*

            The name of the variable.

          - **value** *(string) --*

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --*

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message
          broker.

          - **mqttTopic** *(string) --*

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --*

            The name of the timer.

          - **seconds** *(integer) --*

            The number of seconds until the timer expires. The minimum value is 60
            seconds to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --*

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --*

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector
          model instance and the event which triggered the action.

          - **functionArn** *(string) --*

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to an Amazon SQS queue.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --*

            The name of the Kinesis Data Firehose delivery stream where the data is
            written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the
            Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
            '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --*

      The name of the timer to clear.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `firehose`

    Sends information about the detector model instance and the event which
    triggered the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --*

      The name of the Kinesis Data Firehose delivery stream where the data is
      written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the
      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message
    broker.

    - **mqttTopic** *(string) --*

      The MQTT topic of the message.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector
    model instance and the event which triggered the action.

    - **functionArn** *(string) --*

      The ARN of the AWS Lambda function which is executed.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --*

      The name of the timer to reset.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --*

      The name of the timer.

    - **seconds** *(integer) --*

      The number of seconds until the timer expires. The minimum value is 60
      seconds to ensure accuracy.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --*

      The name of the variable.

    - **value** *(string) --*

      The new value of the variable.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --*

      The ARN of the Amazon SNS target where the message is sent.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sqs`

    Sends information about the detector model instance and the event which
    triggered the action to an Amazon SQS queue.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEvents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --*

        The name of the variable.

      - **value** *(string) --*

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --*

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message
      broker.

      - **mqttTopic** *(string) --*

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --*

        The name of the timer.

      - **seconds** *(integer) --*

        The number of seconds until the timer expires. The minimum value is 60
        seconds to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --*

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --*

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector
      model instance and the event which triggered the action.

      - **functionArn** *(string) --*

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to an Amazon SQS queue.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which
      triggered the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --*

        The name of the Kinesis Data Firehose delivery stream where the data is
        written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the
        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "eventName": str,
        "condition": str,
        "actions": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ],
        "nextState": str,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInput` `transitionEvents`

    Specifies the actions performed and the next state entered when a ``"condition"``
    evaluates to TRUE.

    - **eventName** *(string) --*

      The name of the transition event.

    - **condition** *(string) --*

      [Required] A Boolean expression that when TRUE causes the actions to be
      performed and the ``"nextState"`` to be entered.

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --*

            The name of the variable.

          - **value** *(string) --*

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --*

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message
          broker.

          - **mqttTopic** *(string) --*

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --*

            The name of the timer.

          - **seconds** *(integer) --*

            The number of seconds until the timer expires. The minimum value is 60
            seconds to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --*

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --*

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector
          model instance and the event which triggered the action.

          - **functionArn** *(string) --*

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to an Amazon SQS queue.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which
          triggered the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --*

            The name of the Kinesis Data Firehose delivery stream where the data is
            written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the
            Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
            '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **nextState** *(string) --*

      The next state to enter.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
        ],
        "transitionEvents": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstates` `onInput`

    When an input is received and the ``"condition"`` is TRUE, perform the specified
    ``"actions"`` .

    - **events** *(list) --*

      Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
        TRUE.

        - **eventName** *(string) --*

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --*

                The name of the variable.

              - **value** *(string) --*

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --*

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message
              broker.

              - **mqttTopic** *(string) --*

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --*

                The name of the timer.

              - **seconds** *(integer) --*

                The number of seconds until the timer expires. The minimum value is 60
                seconds to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --*

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --*

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector
              model instance and the event which triggered the action.

              - **functionArn** *(string) --*

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --*

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to an Amazon SQS queue.

              - **queueUrl** *(string) --*

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --*

                The name of the Kinesis Data Firehose delivery stream where the data is
                written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the
                Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **transitionEvents** *(list) --*

      Specifies the actions performed, and the next state entered, when a ``"condition"``
      evaluates to TRUE.

      - *(dict) --*

        Specifies the actions performed and the next state entered when a ``"condition"``
        evaluates to TRUE.

        - **eventName** *(string) --*

          The name of the transition event.

        - **condition** *(string) --*

          [Required] A Boolean expression that when TRUE causes the actions to be
          performed and the ``"nextState"`` to be entered.

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --*

                The name of the variable.

              - **value** *(string) --*

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --*

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message
              broker.

              - **mqttTopic** *(string) --*

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --*

                The name of the timer.

              - **seconds** *(integer) --*

                The number of seconds until the timer expires. The minimum value is 60
                seconds to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --*

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --*

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector
              model instance and the event which triggered the action.

              - **functionArn** *(string) --*

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --*

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to an Amazon SQS queue.

              - **queueUrl** *(string) --*

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which
              triggered the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --*

                The name of the Kinesis Data Firehose delivery stream where the data is
                written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the
                Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

        - **nextState** *(string) --*

          The next state to enter.
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef",
    {
        "stateName": str,
        "onInput": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinition` `states`

    Information that defines a state of a detector.

    - **stateName** *(string) --*

      The name of the state.

    - **onInput** *(dict) --*

      When an input is received and the ``"condition"`` is TRUE, perform the specified
      ``"actions"`` .

      - **events** *(list) --*

        Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
          TRUE.

          - **eventName** *(string) --*

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --*

                  The name of the variable.

                - **value** *(string) --*

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --*

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message
                broker.

                - **mqttTopic** *(string) --*

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --*

                  The name of the timer.

                - **seconds** *(integer) --*

                  The number of seconds until the timer expires. The minimum value is 60
                  seconds to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --*

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --*

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector
                model instance and the event which triggered the action.

                - **functionArn** *(string) --*

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --*

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to an Amazon SQS queue.

                - **queueUrl** *(string) --*

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --*

                  The name of the Kinesis Data Firehose delivery stream where the data is
                  written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the
                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

      - **transitionEvents** *(list) --*

        Specifies the actions performed, and the next state entered, when a ``"condition"``
        evaluates to TRUE.

        - *(dict) --*

          Specifies the actions performed and the next state entered when a ``"condition"``
          evaluates to TRUE.

          - **eventName** *(string) --*

            The name of the transition event.

          - **condition** *(string) --*

            [Required] A Boolean expression that when TRUE causes the actions to be
            performed and the ``"nextState"`` to be entered.

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --*

                  The name of the variable.

                - **value** *(string) --*

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --*

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message
                broker.

                - **mqttTopic** *(string) --*

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --*

                  The name of the timer.

                - **seconds** *(integer) --*

                  The number of seconds until the timer expires. The minimum value is 60
                  seconds to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --*

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --*

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector
                model instance and the event which triggered the action.

                - **functionArn** *(string) --*

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --*

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to an Amazon SQS queue.

                - **queueUrl** *(string) --*

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --*

                  The name of the Kinesis Data Firehose delivery stream where the data is
                  written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the
                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

          - **nextState** *(string) --*

            The next state to enter.

    - **onEnter** *(dict) --*

      When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

      - **events** *(list) --*

        Specifies the actions that are performed when the state is entered and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
          TRUE.

          - **eventName** *(string) --*

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --*

                  The name of the variable.

                - **value** *(string) --*

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --*

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message
                broker.

                - **mqttTopic** *(string) --*

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --*

                  The name of the timer.

                - **seconds** *(integer) --*

                  The number of seconds until the timer expires. The minimum value is 60
                  seconds to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --*

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --*

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector
                model instance and the event which triggered the action.

                - **functionArn** *(string) --*

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --*

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to an Amazon SQS queue.

                - **queueUrl** *(string) --*

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --*

                  The name of the Kinesis Data Firehose delivery stream where the data is
                  written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the
                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **onExit** *(dict) --*

      When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
      is TRUE.

      - **events** *(list) --*

        Specifies the ``"actions"`` that are performed when the state is exited and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
          TRUE.

          - **eventName** *(string) --*

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --*

                  The name of the variable.

                - **value** *(string) --*

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --*

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message
                broker.

                - **mqttTopic** *(string) --*

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --*

                  The name of the timer.

                - **seconds** *(integer) --*

                  The number of seconds until the timer expires. The minimum value is 60
                  seconds to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --*

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --*

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector
                model instance and the event which triggered the action.

                - **functionArn** *(string) --*

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --*

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to an Amazon SQS queue.

                - **queueUrl** *(string) --*

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which
                triggered the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --*

                  The name of the Kinesis Data Firehose delivery stream where the data is
                  written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the
                  Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                  '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef",
    {
        "states": List[
            ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionstatesTypeDef
        ],
        "initialStateName": str,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponsedetectorModel` `detectorModelDefinition`

    Information that defines how a detector operates.

    - **states** *(list) --*

      Information about the states of the detector.

      - *(dict) --*

        Information that defines a state of a detector.

        - **stateName** *(string) --*

          The name of the state.

        - **onInput** *(dict) --*

          When an input is received and the ``"condition"`` is TRUE, perform the specified
          ``"actions"`` .

          - **events** *(list) --*

            Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
              TRUE.

              - **eventName** *(string) --*

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --*

                      The name of the variable.

                    - **value** *(string) --*

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --*

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message
                    broker.

                    - **mqttTopic** *(string) --*

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --*

                      The name of the timer.

                    - **seconds** *(integer) --*

                      The number of seconds until the timer expires. The minimum value is 60
                      seconds to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --*

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --*

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector
                    model instance and the event which triggered the action.

                    - **functionArn** *(string) --*

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --*

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --*

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --*

                      The name of the Kinesis Data Firehose delivery stream where the data is
                      written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the
                      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

          - **transitionEvents** *(list) --*

            Specifies the actions performed, and the next state entered, when a ``"condition"``
            evaluates to TRUE.

            - *(dict) --*

              Specifies the actions performed and the next state entered when a ``"condition"``
              evaluates to TRUE.

              - **eventName** *(string) --*

                The name of the transition event.

              - **condition** *(string) --*

                [Required] A Boolean expression that when TRUE causes the actions to be
                performed and the ``"nextState"`` to be entered.

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --*

                      The name of the variable.

                    - **value** *(string) --*

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --*

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message
                    broker.

                    - **mqttTopic** *(string) --*

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --*

                      The name of the timer.

                    - **seconds** *(integer) --*

                      The number of seconds until the timer expires. The minimum value is 60
                      seconds to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --*

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --*

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector
                    model instance and the event which triggered the action.

                    - **functionArn** *(string) --*

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --*

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --*

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --*

                      The name of the Kinesis Data Firehose delivery stream where the data is
                      written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the
                      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

              - **nextState** *(string) --*

                The next state to enter.

        - **onEnter** *(dict) --*

          When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

          - **events** *(list) --*

            Specifies the actions that are performed when the state is entered and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
              TRUE.

              - **eventName** *(string) --*

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --*

                      The name of the variable.

                    - **value** *(string) --*

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --*

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message
                    broker.

                    - **mqttTopic** *(string) --*

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --*

                      The name of the timer.

                    - **seconds** *(integer) --*

                      The number of seconds until the timer expires. The minimum value is 60
                      seconds to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --*

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --*

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector
                    model instance and the event which triggered the action.

                    - **functionArn** *(string) --*

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --*

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --*

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --*

                      The name of the Kinesis Data Firehose delivery stream where the data is
                      written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the
                      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

        - **onExit** *(dict) --*

          When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
          is TRUE.

          - **events** *(list) --*

            Specifies the ``"actions"`` that are performed when the state is exited and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
              TRUE.

              - **eventName** *(string) --*

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --*

                      The name of the variable.

                    - **value** *(string) --*

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --*

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message
                    broker.

                    - **mqttTopic** *(string) --*

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --*

                      The name of the timer.

                    - **seconds** *(integer) --*

                      The number of seconds until the timer expires. The minimum value is 60
                      seconds to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --*

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --*

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector
                    model instance and the event which triggered the action.

                    - **functionArn** *(string) --*

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --*

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --*

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which
                    triggered the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --*

                      The name of the Kinesis Data Firehose delivery stream where the data is
                      written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the
                      Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                      '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **initialStateName** *(string) --*

      The state that is entered at the creation of each detector (instance).
    """


_ClientDescribeDetectorModelResponsedetectorModelTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponsedetectorModelTypeDef",
    {
        "detectorModelDefinition": ClientDescribeDetectorModelResponsedetectorModeldetectorModelDefinitionTypeDef,
        "detectorModelConfiguration": ClientDescribeDetectorModelResponsedetectorModeldetectorModelConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeDetectorModelResponsedetectorModelTypeDef(
    _ClientDescribeDetectorModelResponsedetectorModelTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModelResponse` `detectorModel`

    Information about the detector model.

    - **detectorModelDefinition** *(dict) --*

      Information that defines how a detector operates.

      - **states** *(list) --*

        Information about the states of the detector.

        - *(dict) --*

          Information that defines a state of a detector.

          - **stateName** *(string) --*

            The name of the state.

          - **onInput** *(dict) --*

            When an input is received and the ``"condition"`` is TRUE, perform the specified
            ``"actions"`` .

            - **events** *(list) --*

              Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

              - *(dict) --*

                Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                TRUE.

                - **eventName** *(string) --*

                  The name of the event.

                - **condition** *(string) --*

                  [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                  performed. If not present, the actions are performed (=TRUE); if the expression
                  result is not a Boolean value, the actions are NOT performed (=FALSE).

                - **actions** *(list) --*

                  The actions to be performed.

                  - *(dict) --*

                    An action to be performed when the ``"condition"`` is TRUE.

                    - **setVariable** *(dict) --*

                      Sets a variable to a specified value.

                      - **variableName** *(string) --*

                        The name of the variable.

                      - **value** *(string) --*

                        The new value of the variable.

                    - **sns** *(dict) --*

                      Sends an Amazon SNS message.

                      - **targetArn** *(string) --*

                        The ARN of the Amazon SNS target where the message is sent.

                    - **iotTopicPublish** *(dict) --*

                      Publishes an MQTT message with the given topic to the AWS IoT message
                      broker.

                      - **mqttTopic** *(string) --*

                        The MQTT topic of the message.

                    - **setTimer** *(dict) --*

                      Information needed to set the timer.

                      - **timerName** *(string) --*

                        The name of the timer.

                      - **seconds** *(integer) --*

                        The number of seconds until the timer expires. The minimum value is 60
                        seconds to ensure accuracy.

                    - **clearTimer** *(dict) --*

                      Information needed to clear the timer.

                      - **timerName** *(string) --*

                        The name of the timer to clear.

                    - **resetTimer** *(dict) --*

                      Information needed to reset the timer.

                      - **timerName** *(string) --*

                        The name of the timer to reset.

                    - **lambda** *(dict) --*

                      Calls an AWS Lambda function, passing in information about the detector
                      model instance and the event which triggered the action.

                      - **functionArn** *(string) --*

                        The ARN of the AWS Lambda function which is executed.

                    - **iotEvents** *(dict) --*

                      Sends an IoT Events input, passing in information about the detector model
                      instance and the event which triggered the action.

                      - **inputName** *(string) --*

                        The name of the AWS IoT Events input where the data is sent.

                    - **sqs** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to an Amazon SQS queue.

                      - **queueUrl** *(string) --*

                        The URL of the Amazon SQS queue where the data is written.

                      - **useBase64** *(boolean) --*

                        Set this to TRUE if you want the data to be Base-64 encoded before it is
                        written to the queue. Otherwise, set this to FALSE.

                    - **firehose** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to a Kinesis Data Firehose delivery stream.

                      - **deliveryStreamName** *(string) --*

                        The name of the Kinesis Data Firehose delivery stream where the data is
                        written.

                      - **separator** *(string) --*

                        A character separator that is used to separate records written to the
                        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            - **transitionEvents** *(list) --*

              Specifies the actions performed, and the next state entered, when a ``"condition"``
              evaluates to TRUE.

              - *(dict) --*

                Specifies the actions performed and the next state entered when a ``"condition"``
                evaluates to TRUE.

                - **eventName** *(string) --*

                  The name of the transition event.

                - **condition** *(string) --*

                  [Required] A Boolean expression that when TRUE causes the actions to be
                  performed and the ``"nextState"`` to be entered.

                - **actions** *(list) --*

                  The actions to be performed.

                  - *(dict) --*

                    An action to be performed when the ``"condition"`` is TRUE.

                    - **setVariable** *(dict) --*

                      Sets a variable to a specified value.

                      - **variableName** *(string) --*

                        The name of the variable.

                      - **value** *(string) --*

                        The new value of the variable.

                    - **sns** *(dict) --*

                      Sends an Amazon SNS message.

                      - **targetArn** *(string) --*

                        The ARN of the Amazon SNS target where the message is sent.

                    - **iotTopicPublish** *(dict) --*

                      Publishes an MQTT message with the given topic to the AWS IoT message
                      broker.

                      - **mqttTopic** *(string) --*

                        The MQTT topic of the message.

                    - **setTimer** *(dict) --*

                      Information needed to set the timer.

                      - **timerName** *(string) --*

                        The name of the timer.

                      - **seconds** *(integer) --*

                        The number of seconds until the timer expires. The minimum value is 60
                        seconds to ensure accuracy.

                    - **clearTimer** *(dict) --*

                      Information needed to clear the timer.

                      - **timerName** *(string) --*

                        The name of the timer to clear.

                    - **resetTimer** *(dict) --*

                      Information needed to reset the timer.

                      - **timerName** *(string) --*

                        The name of the timer to reset.

                    - **lambda** *(dict) --*

                      Calls an AWS Lambda function, passing in information about the detector
                      model instance and the event which triggered the action.

                      - **functionArn** *(string) --*

                        The ARN of the AWS Lambda function which is executed.

                    - **iotEvents** *(dict) --*

                      Sends an IoT Events input, passing in information about the detector model
                      instance and the event which triggered the action.

                      - **inputName** *(string) --*

                        The name of the AWS IoT Events input where the data is sent.

                    - **sqs** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to an Amazon SQS queue.

                      - **queueUrl** *(string) --*

                        The URL of the Amazon SQS queue where the data is written.

                      - **useBase64** *(boolean) --*

                        Set this to TRUE if you want the data to be Base-64 encoded before it is
                        written to the queue. Otherwise, set this to FALSE.

                    - **firehose** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to a Kinesis Data Firehose delivery stream.

                      - **deliveryStreamName** *(string) --*

                        The name of the Kinesis Data Firehose delivery stream where the data is
                        written.

                      - **separator** *(string) --*

                        A character separator that is used to separate records written to the
                        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                - **nextState** *(string) --*

                  The next state to enter.

          - **onEnter** *(dict) --*

            When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

            - **events** *(list) --*

              Specifies the actions that are performed when the state is entered and the
              ``"condition"`` is TRUE.

              - *(dict) --*

                Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                TRUE.

                - **eventName** *(string) --*

                  The name of the event.

                - **condition** *(string) --*

                  [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                  performed. If not present, the actions are performed (=TRUE); if the expression
                  result is not a Boolean value, the actions are NOT performed (=FALSE).

                - **actions** *(list) --*

                  The actions to be performed.

                  - *(dict) --*

                    An action to be performed when the ``"condition"`` is TRUE.

                    - **setVariable** *(dict) --*

                      Sets a variable to a specified value.

                      - **variableName** *(string) --*

                        The name of the variable.

                      - **value** *(string) --*

                        The new value of the variable.

                    - **sns** *(dict) --*

                      Sends an Amazon SNS message.

                      - **targetArn** *(string) --*

                        The ARN of the Amazon SNS target where the message is sent.

                    - **iotTopicPublish** *(dict) --*

                      Publishes an MQTT message with the given topic to the AWS IoT message
                      broker.

                      - **mqttTopic** *(string) --*

                        The MQTT topic of the message.

                    - **setTimer** *(dict) --*

                      Information needed to set the timer.

                      - **timerName** *(string) --*

                        The name of the timer.

                      - **seconds** *(integer) --*

                        The number of seconds until the timer expires. The minimum value is 60
                        seconds to ensure accuracy.

                    - **clearTimer** *(dict) --*

                      Information needed to clear the timer.

                      - **timerName** *(string) --*

                        The name of the timer to clear.

                    - **resetTimer** *(dict) --*

                      Information needed to reset the timer.

                      - **timerName** *(string) --*

                        The name of the timer to reset.

                    - **lambda** *(dict) --*

                      Calls an AWS Lambda function, passing in information about the detector
                      model instance and the event which triggered the action.

                      - **functionArn** *(string) --*

                        The ARN of the AWS Lambda function which is executed.

                    - **iotEvents** *(dict) --*

                      Sends an IoT Events input, passing in information about the detector model
                      instance and the event which triggered the action.

                      - **inputName** *(string) --*

                        The name of the AWS IoT Events input where the data is sent.

                    - **sqs** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to an Amazon SQS queue.

                      - **queueUrl** *(string) --*

                        The URL of the Amazon SQS queue where the data is written.

                      - **useBase64** *(boolean) --*

                        Set this to TRUE if you want the data to be Base-64 encoded before it is
                        written to the queue. Otherwise, set this to FALSE.

                    - **firehose** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to a Kinesis Data Firehose delivery stream.

                      - **deliveryStreamName** *(string) --*

                        The name of the Kinesis Data Firehose delivery stream where the data is
                        written.

                      - **separator** *(string) --*

                        A character separator that is used to separate records written to the
                        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

          - **onExit** *(dict) --*

            When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
            is TRUE.

            - **events** *(list) --*

              Specifies the ``"actions"`` that are performed when the state is exited and the
              ``"condition"`` is TRUE.

              - *(dict) --*

                Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                TRUE.

                - **eventName** *(string) --*

                  The name of the event.

                - **condition** *(string) --*

                  [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                  performed. If not present, the actions are performed (=TRUE); if the expression
                  result is not a Boolean value, the actions are NOT performed (=FALSE).

                - **actions** *(list) --*

                  The actions to be performed.

                  - *(dict) --*

                    An action to be performed when the ``"condition"`` is TRUE.

                    - **setVariable** *(dict) --*

                      Sets a variable to a specified value.

                      - **variableName** *(string) --*

                        The name of the variable.

                      - **value** *(string) --*

                        The new value of the variable.

                    - **sns** *(dict) --*

                      Sends an Amazon SNS message.

                      - **targetArn** *(string) --*

                        The ARN of the Amazon SNS target where the message is sent.

                    - **iotTopicPublish** *(dict) --*

                      Publishes an MQTT message with the given topic to the AWS IoT message
                      broker.

                      - **mqttTopic** *(string) --*

                        The MQTT topic of the message.

                    - **setTimer** *(dict) --*

                      Information needed to set the timer.

                      - **timerName** *(string) --*

                        The name of the timer.

                      - **seconds** *(integer) --*

                        The number of seconds until the timer expires. The minimum value is 60
                        seconds to ensure accuracy.

                    - **clearTimer** *(dict) --*

                      Information needed to clear the timer.

                      - **timerName** *(string) --*

                        The name of the timer to clear.

                    - **resetTimer** *(dict) --*

                      Information needed to reset the timer.

                      - **timerName** *(string) --*

                        The name of the timer to reset.

                    - **lambda** *(dict) --*

                      Calls an AWS Lambda function, passing in information about the detector
                      model instance and the event which triggered the action.

                      - **functionArn** *(string) --*

                        The ARN of the AWS Lambda function which is executed.

                    - **iotEvents** *(dict) --*

                      Sends an IoT Events input, passing in information about the detector model
                      instance and the event which triggered the action.

                      - **inputName** *(string) --*

                        The name of the AWS IoT Events input where the data is sent.

                    - **sqs** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to an Amazon SQS queue.

                      - **queueUrl** *(string) --*

                        The URL of the Amazon SQS queue where the data is written.

                      - **useBase64** *(boolean) --*

                        Set this to TRUE if you want the data to be Base-64 encoded before it is
                        written to the queue. Otherwise, set this to FALSE.

                    - **firehose** *(dict) --*

                      Sends information about the detector model instance and the event which
                      triggered the action to a Kinesis Data Firehose delivery stream.

                      - **deliveryStreamName** *(string) --*

                        The name of the Kinesis Data Firehose delivery stream where the data is
                        written.

                      - **separator** *(string) --*

                        A character separator that is used to separate records written to the
                        Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                        '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

      - **initialStateName** *(string) --*

        The state that is entered at the creation of each detector (instance).

    - **detectorModelConfiguration** *(dict) --*

      Information about how the detector is configured.

      - **detectorModelName** *(string) --*

        The name of the detector model.

      - **detectorModelVersion** *(string) --*

        The version of the detector model.

      - **detectorModelDescription** *(string) --*

        A brief description of the detector model.

      - **detectorModelArn** *(string) --*

        The ARN of the detector model.

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Events to perform its operations.

      - **creationTime** *(datetime) --*

        The time the detector model was created.

      - **lastUpdateTime** *(datetime) --*

        The time the detector model was last updated.

      - **status** *(string) --*

        The status of the detector model.

      - **key** *(string) --*

        The input attribute key used to identify a device or system to create a detector (an
        instance of the detector model) and then to route each input received to the appropriate
        detector (instance). This parameter uses a JSON-path expression to specify the
        attribute-value pair in the message payload of each input that is used to identify the
        device associated with the input.

      - **evaluationMethod** *(string) --*

        When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
        order that the events are defined. When set to ``BATCH`` , variables are updated and
        events performed only after all event conditions are evaluated.
    """


_ClientDescribeDetectorModelResponseTypeDef = TypedDict(
    "_ClientDescribeDetectorModelResponseTypeDef",
    {"detectorModel": ClientDescribeDetectorModelResponsedetectorModelTypeDef},
    total=False,
)


class ClientDescribeDetectorModelResponseTypeDef(
    _ClientDescribeDetectorModelResponseTypeDef
):
    """
    Type definition for `ClientDescribeDetectorModel` `Response`

    - **detectorModel** *(dict) --*

      Information about the detector model.

      - **detectorModelDefinition** *(dict) --*

        Information that defines how a detector operates.

        - **states** *(list) --*

          Information about the states of the detector.

          - *(dict) --*

            Information that defines a state of a detector.

            - **stateName** *(string) --*

              The name of the state.

            - **onInput** *(dict) --*

              When an input is received and the ``"condition"`` is TRUE, perform the specified
              ``"actions"`` .

              - **events** *(list) --*

                Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

                - *(dict) --*

                  Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                  TRUE.

                  - **eventName** *(string) --*

                    The name of the event.

                  - **condition** *(string) --*

                    [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                    performed. If not present, the actions are performed (=TRUE); if the expression
                    result is not a Boolean value, the actions are NOT performed (=FALSE).

                  - **actions** *(list) --*

                    The actions to be performed.

                    - *(dict) --*

                      An action to be performed when the ``"condition"`` is TRUE.

                      - **setVariable** *(dict) --*

                        Sets a variable to a specified value.

                        - **variableName** *(string) --*

                          The name of the variable.

                        - **value** *(string) --*

                          The new value of the variable.

                      - **sns** *(dict) --*

                        Sends an Amazon SNS message.

                        - **targetArn** *(string) --*

                          The ARN of the Amazon SNS target where the message is sent.

                      - **iotTopicPublish** *(dict) --*

                        Publishes an MQTT message with the given topic to the AWS IoT message
                        broker.

                        - **mqttTopic** *(string) --*

                          The MQTT topic of the message.

                      - **setTimer** *(dict) --*

                        Information needed to set the timer.

                        - **timerName** *(string) --*

                          The name of the timer.

                        - **seconds** *(integer) --*

                          The number of seconds until the timer expires. The minimum value is 60
                          seconds to ensure accuracy.

                      - **clearTimer** *(dict) --*

                        Information needed to clear the timer.

                        - **timerName** *(string) --*

                          The name of the timer to clear.

                      - **resetTimer** *(dict) --*

                        Information needed to reset the timer.

                        - **timerName** *(string) --*

                          The name of the timer to reset.

                      - **lambda** *(dict) --*

                        Calls an AWS Lambda function, passing in information about the detector
                        model instance and the event which triggered the action.

                        - **functionArn** *(string) --*

                          The ARN of the AWS Lambda function which is executed.

                      - **iotEvents** *(dict) --*

                        Sends an IoT Events input, passing in information about the detector model
                        instance and the event which triggered the action.

                        - **inputName** *(string) --*

                          The name of the AWS IoT Events input where the data is sent.

                      - **sqs** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to an Amazon SQS queue.

                        - **queueUrl** *(string) --*

                          The URL of the Amazon SQS queue where the data is written.

                        - **useBase64** *(boolean) --*

                          Set this to TRUE if you want the data to be Base-64 encoded before it is
                          written to the queue. Otherwise, set this to FALSE.

                      - **firehose** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to a Kinesis Data Firehose delivery stream.

                        - **deliveryStreamName** *(string) --*

                          The name of the Kinesis Data Firehose delivery stream where the data is
                          written.

                        - **separator** *(string) --*

                          A character separator that is used to separate records written to the
                          Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                          '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

              - **transitionEvents** *(list) --*

                Specifies the actions performed, and the next state entered, when a ``"condition"``
                evaluates to TRUE.

                - *(dict) --*

                  Specifies the actions performed and the next state entered when a ``"condition"``
                  evaluates to TRUE.

                  - **eventName** *(string) --*

                    The name of the transition event.

                  - **condition** *(string) --*

                    [Required] A Boolean expression that when TRUE causes the actions to be
                    performed and the ``"nextState"`` to be entered.

                  - **actions** *(list) --*

                    The actions to be performed.

                    - *(dict) --*

                      An action to be performed when the ``"condition"`` is TRUE.

                      - **setVariable** *(dict) --*

                        Sets a variable to a specified value.

                        - **variableName** *(string) --*

                          The name of the variable.

                        - **value** *(string) --*

                          The new value of the variable.

                      - **sns** *(dict) --*

                        Sends an Amazon SNS message.

                        - **targetArn** *(string) --*

                          The ARN of the Amazon SNS target where the message is sent.

                      - **iotTopicPublish** *(dict) --*

                        Publishes an MQTT message with the given topic to the AWS IoT message
                        broker.

                        - **mqttTopic** *(string) --*

                          The MQTT topic of the message.

                      - **setTimer** *(dict) --*

                        Information needed to set the timer.

                        - **timerName** *(string) --*

                          The name of the timer.

                        - **seconds** *(integer) --*

                          The number of seconds until the timer expires. The minimum value is 60
                          seconds to ensure accuracy.

                      - **clearTimer** *(dict) --*

                        Information needed to clear the timer.

                        - **timerName** *(string) --*

                          The name of the timer to clear.

                      - **resetTimer** *(dict) --*

                        Information needed to reset the timer.

                        - **timerName** *(string) --*

                          The name of the timer to reset.

                      - **lambda** *(dict) --*

                        Calls an AWS Lambda function, passing in information about the detector
                        model instance and the event which triggered the action.

                        - **functionArn** *(string) --*

                          The ARN of the AWS Lambda function which is executed.

                      - **iotEvents** *(dict) --*

                        Sends an IoT Events input, passing in information about the detector model
                        instance and the event which triggered the action.

                        - **inputName** *(string) --*

                          The name of the AWS IoT Events input where the data is sent.

                      - **sqs** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to an Amazon SQS queue.

                        - **queueUrl** *(string) --*

                          The URL of the Amazon SQS queue where the data is written.

                        - **useBase64** *(boolean) --*

                          Set this to TRUE if you want the data to be Base-64 encoded before it is
                          written to the queue. Otherwise, set this to FALSE.

                      - **firehose** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to a Kinesis Data Firehose delivery stream.

                        - **deliveryStreamName** *(string) --*

                          The name of the Kinesis Data Firehose delivery stream where the data is
                          written.

                        - **separator** *(string) --*

                          A character separator that is used to separate records written to the
                          Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                          '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

                  - **nextState** *(string) --*

                    The next state to enter.

            - **onEnter** *(dict) --*

              When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

              - **events** *(list) --*

                Specifies the actions that are performed when the state is entered and the
                ``"condition"`` is TRUE.

                - *(dict) --*

                  Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                  TRUE.

                  - **eventName** *(string) --*

                    The name of the event.

                  - **condition** *(string) --*

                    [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                    performed. If not present, the actions are performed (=TRUE); if the expression
                    result is not a Boolean value, the actions are NOT performed (=FALSE).

                  - **actions** *(list) --*

                    The actions to be performed.

                    - *(dict) --*

                      An action to be performed when the ``"condition"`` is TRUE.

                      - **setVariable** *(dict) --*

                        Sets a variable to a specified value.

                        - **variableName** *(string) --*

                          The name of the variable.

                        - **value** *(string) --*

                          The new value of the variable.

                      - **sns** *(dict) --*

                        Sends an Amazon SNS message.

                        - **targetArn** *(string) --*

                          The ARN of the Amazon SNS target where the message is sent.

                      - **iotTopicPublish** *(dict) --*

                        Publishes an MQTT message with the given topic to the AWS IoT message
                        broker.

                        - **mqttTopic** *(string) --*

                          The MQTT topic of the message.

                      - **setTimer** *(dict) --*

                        Information needed to set the timer.

                        - **timerName** *(string) --*

                          The name of the timer.

                        - **seconds** *(integer) --*

                          The number of seconds until the timer expires. The minimum value is 60
                          seconds to ensure accuracy.

                      - **clearTimer** *(dict) --*

                        Information needed to clear the timer.

                        - **timerName** *(string) --*

                          The name of the timer to clear.

                      - **resetTimer** *(dict) --*

                        Information needed to reset the timer.

                        - **timerName** *(string) --*

                          The name of the timer to reset.

                      - **lambda** *(dict) --*

                        Calls an AWS Lambda function, passing in information about the detector
                        model instance and the event which triggered the action.

                        - **functionArn** *(string) --*

                          The ARN of the AWS Lambda function which is executed.

                      - **iotEvents** *(dict) --*

                        Sends an IoT Events input, passing in information about the detector model
                        instance and the event which triggered the action.

                        - **inputName** *(string) --*

                          The name of the AWS IoT Events input where the data is sent.

                      - **sqs** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to an Amazon SQS queue.

                        - **queueUrl** *(string) --*

                          The URL of the Amazon SQS queue where the data is written.

                        - **useBase64** *(boolean) --*

                          Set this to TRUE if you want the data to be Base-64 encoded before it is
                          written to the queue. Otherwise, set this to FALSE.

                      - **firehose** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to a Kinesis Data Firehose delivery stream.

                        - **deliveryStreamName** *(string) --*

                          The name of the Kinesis Data Firehose delivery stream where the data is
                          written.

                        - **separator** *(string) --*

                          A character separator that is used to separate records written to the
                          Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                          '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            - **onExit** *(dict) --*

              When exiting this state, perform these ``"actions"`` if the specified ``"condition"``
              is TRUE.

              - **events** *(list) --*

                Specifies the ``"actions"`` that are performed when the state is exited and the
                ``"condition"`` is TRUE.

                - *(dict) --*

                  Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to
                  TRUE.

                  - **eventName** *(string) --*

                    The name of the event.

                  - **condition** *(string) --*

                    [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                    performed. If not present, the actions are performed (=TRUE); if the expression
                    result is not a Boolean value, the actions are NOT performed (=FALSE).

                  - **actions** *(list) --*

                    The actions to be performed.

                    - *(dict) --*

                      An action to be performed when the ``"condition"`` is TRUE.

                      - **setVariable** *(dict) --*

                        Sets a variable to a specified value.

                        - **variableName** *(string) --*

                          The name of the variable.

                        - **value** *(string) --*

                          The new value of the variable.

                      - **sns** *(dict) --*

                        Sends an Amazon SNS message.

                        - **targetArn** *(string) --*

                          The ARN of the Amazon SNS target where the message is sent.

                      - **iotTopicPublish** *(dict) --*

                        Publishes an MQTT message with the given topic to the AWS IoT message
                        broker.

                        - **mqttTopic** *(string) --*

                          The MQTT topic of the message.

                      - **setTimer** *(dict) --*

                        Information needed to set the timer.

                        - **timerName** *(string) --*

                          The name of the timer.

                        - **seconds** *(integer) --*

                          The number of seconds until the timer expires. The minimum value is 60
                          seconds to ensure accuracy.

                      - **clearTimer** *(dict) --*

                        Information needed to clear the timer.

                        - **timerName** *(string) --*

                          The name of the timer to clear.

                      - **resetTimer** *(dict) --*

                        Information needed to reset the timer.

                        - **timerName** *(string) --*

                          The name of the timer to reset.

                      - **lambda** *(dict) --*

                        Calls an AWS Lambda function, passing in information about the detector
                        model instance and the event which triggered the action.

                        - **functionArn** *(string) --*

                          The ARN of the AWS Lambda function which is executed.

                      - **iotEvents** *(dict) --*

                        Sends an IoT Events input, passing in information about the detector model
                        instance and the event which triggered the action.

                        - **inputName** *(string) --*

                          The name of the AWS IoT Events input where the data is sent.

                      - **sqs** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to an Amazon SQS queue.

                        - **queueUrl** *(string) --*

                          The URL of the Amazon SQS queue where the data is written.

                        - **useBase64** *(boolean) --*

                          Set this to TRUE if you want the data to be Base-64 encoded before it is
                          written to the queue. Otherwise, set this to FALSE.

                      - **firehose** *(dict) --*

                        Sends information about the detector model instance and the event which
                        triggered the action to a Kinesis Data Firehose delivery stream.

                        - **deliveryStreamName** *(string) --*

                          The name of the Kinesis Data Firehose delivery stream where the data is
                          written.

                        - **separator** *(string) --*

                          A character separator that is used to separate records written to the
                          Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline),
                          '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

        - **initialStateName** *(string) --*

          The state that is entered at the creation of each detector (instance).

      - **detectorModelConfiguration** *(dict) --*

        Information about how the detector is configured.

        - **detectorModelName** *(string) --*

          The name of the detector model.

        - **detectorModelVersion** *(string) --*

          The version of the detector model.

        - **detectorModelDescription** *(string) --*

          A brief description of the detector model.

        - **detectorModelArn** *(string) --*

          The ARN of the detector model.

        - **roleArn** *(string) --*

          The ARN of the role that grants permission to AWS IoT Events to perform its operations.

        - **creationTime** *(datetime) --*

          The time the detector model was created.

        - **lastUpdateTime** *(datetime) --*

          The time the detector model was last updated.

        - **status** *(string) --*

          The status of the detector model.

        - **key** *(string) --*

          The input attribute key used to identify a device or system to create a detector (an
          instance of the detector model) and then to route each input received to the appropriate
          detector (instance). This parameter uses a JSON-path expression to specify the
          attribute-value pair in the message payload of each input that is used to identify the
          device associated with the input.

        - **evaluationMethod** *(string) --*

          When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
          order that the events are defined. When set to ``BATCH`` , variables are updated and
          events performed only after all event conditions are evaluated.
    """


_ClientDescribeInputResponseinputinputConfigurationTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientDescribeInputResponseinputinputConfigurationTypeDef(
    _ClientDescribeInputResponseinputinputConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeInputResponseinput` `inputConfiguration`

    Information about the configuration of an input.

    - **inputName** *(string) --*

      The name of the input.

    - **inputDescription** *(string) --*

      A brief description of the input.

    - **inputArn** *(string) --*

      The ARN of the input.

    - **creationTime** *(datetime) --*

      The time the input was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the input was updated.

    - **status** *(string) --*

      The status of the input.
    """


_ClientDescribeInputResponseinputinputDefinitionattributesTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputDefinitionattributesTypeDef",
    {"jsonPath": str},
    total=False,
)


class ClientDescribeInputResponseinputinputDefinitionattributesTypeDef(
    _ClientDescribeInputResponseinputinputDefinitionattributesTypeDef
):
    """
    Type definition for `ClientDescribeInputResponseinputinputDefinition` `attributes`

    The attributes from the JSON payload that are made available by the input. Inputs are
    derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` .
    Each such message contains a JSON payload, and those attributes (and their paired
    values) specified here are available for use in the ``condition`` expressions used by
    detectors.

    - **jsonPath** *(string) --*

      An expression that specifies an attribute-value pair in a JSON structure. Use this to
      specify an attribute from the JSON payload that is made available by the input.
      Inputs are derived from messages sent to the AWS IoT Events system
      (``BatchPutMessage`` ). Each such message contains a JSON payload, and the attribute
      (and its paired value) specified here are available for use in the ``"condition"``
      expressions used by detectors.

      Syntax: ``<field-name>.<field-name>...``
    """


_ClientDescribeInputResponseinputinputDefinitionTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputinputDefinitionTypeDef",
    {
        "attributes": List[
            ClientDescribeInputResponseinputinputDefinitionattributesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeInputResponseinputinputDefinitionTypeDef(
    _ClientDescribeInputResponseinputinputDefinitionTypeDef
):
    """
    Type definition for `ClientDescribeInputResponseinput` `inputDefinition`

    The definition of the input.

    - **attributes** *(list) --*

      The attributes from the JSON payload that are made available by the input. Inputs are
      derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
      such message contains a JSON payload, and those attributes (and their paired values)
      specified here are available for use in the ``"condition"`` expressions used by detectors
      that monitor this input.

      - *(dict) --*

        The attributes from the JSON payload that are made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` .
        Each such message contains a JSON payload, and those attributes (and their paired
        values) specified here are available for use in the ``condition`` expressions used by
        detectors.

        - **jsonPath** *(string) --*

          An expression that specifies an attribute-value pair in a JSON structure. Use this to
          specify an attribute from the JSON payload that is made available by the input.
          Inputs are derived from messages sent to the AWS IoT Events system
          (``BatchPutMessage`` ). Each such message contains a JSON payload, and the attribute
          (and its paired value) specified here are available for use in the ``"condition"``
          expressions used by detectors.

          Syntax: ``<field-name>.<field-name>...``
    """


_ClientDescribeInputResponseinputTypeDef = TypedDict(
    "_ClientDescribeInputResponseinputTypeDef",
    {
        "inputConfiguration": ClientDescribeInputResponseinputinputConfigurationTypeDef,
        "inputDefinition": ClientDescribeInputResponseinputinputDefinitionTypeDef,
    },
    total=False,
)


class ClientDescribeInputResponseinputTypeDef(_ClientDescribeInputResponseinputTypeDef):
    """
    Type definition for `ClientDescribeInputResponse` `input`

    Information about the input.

    - **inputConfiguration** *(dict) --*

      Information about the configuration of an input.

      - **inputName** *(string) --*

        The name of the input.

      - **inputDescription** *(string) --*

        A brief description of the input.

      - **inputArn** *(string) --*

        The ARN of the input.

      - **creationTime** *(datetime) --*

        The time the input was created.

      - **lastUpdateTime** *(datetime) --*

        The last time the input was updated.

      - **status** *(string) --*

        The status of the input.

    - **inputDefinition** *(dict) --*

      The definition of the input.

      - **attributes** *(list) --*

        The attributes from the JSON payload that are made available by the input. Inputs are
        derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
        such message contains a JSON payload, and those attributes (and their paired values)
        specified here are available for use in the ``"condition"`` expressions used by detectors
        that monitor this input.

        - *(dict) --*

          The attributes from the JSON payload that are made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` .
          Each such message contains a JSON payload, and those attributes (and their paired
          values) specified here are available for use in the ``condition`` expressions used by
          detectors.

          - **jsonPath** *(string) --*

            An expression that specifies an attribute-value pair in a JSON structure. Use this to
            specify an attribute from the JSON payload that is made available by the input.
            Inputs are derived from messages sent to the AWS IoT Events system
            (``BatchPutMessage`` ). Each such message contains a JSON payload, and the attribute
            (and its paired value) specified here are available for use in the ``"condition"``
            expressions used by detectors.

            Syntax: ``<field-name>.<field-name>...``
    """


_ClientDescribeInputResponseTypeDef = TypedDict(
    "_ClientDescribeInputResponseTypeDef",
    {"input": ClientDescribeInputResponseinputTypeDef},
    total=False,
)


class ClientDescribeInputResponseTypeDef(_ClientDescribeInputResponseTypeDef):
    """
    Type definition for `ClientDescribeInput` `Response`

    - **input** *(dict) --*

      Information about the input.

      - **inputConfiguration** *(dict) --*

        Information about the configuration of an input.

        - **inputName** *(string) --*

          The name of the input.

        - **inputDescription** *(string) --*

          A brief description of the input.

        - **inputArn** *(string) --*

          The ARN of the input.

        - **creationTime** *(datetime) --*

          The time the input was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the input was updated.

        - **status** *(string) --*

          The status of the input.

      - **inputDefinition** *(dict) --*

        The definition of the input.

        - **attributes** *(list) --*

          The attributes from the JSON payload that are made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each
          such message contains a JSON payload, and those attributes (and their paired values)
          specified here are available for use in the ``"condition"`` expressions used by detectors
          that monitor this input.

          - *(dict) --*

            The attributes from the JSON payload that are made available by the input. Inputs are
            derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` .
            Each such message contains a JSON payload, and those attributes (and their paired
            values) specified here are available for use in the ``condition`` expressions used by
            detectors.

            - **jsonPath** *(string) --*

              An expression that specifies an attribute-value pair in a JSON structure. Use this to
              specify an attribute from the JSON payload that is made available by the input.
              Inputs are derived from messages sent to the AWS IoT Events system
              (``BatchPutMessage`` ). Each such message contains a JSON payload, and the attribute
              (and its paired value) specified here are available for use in the ``"condition"``
              expressions used by detectors.

              Syntax: ``<field-name>.<field-name>...``
    """


_ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str, "keyValue": str},
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoggingOptionsResponseloggingOptions` `detectorDebugOptions`

    The detector model and the specific detectors (instances) for which the logging level is
    given.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **keyValue** *(string) --*

      The value of the input attribute key used to create the detector (the instance of the
      detector model).
    """


_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": str,
        "enabled": bool,
        "detectorDebugOptions": List[
            ClientDescribeLoggingOptionsResponseloggingOptionsdetectorDebugOptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoggingOptionsResponse` `loggingOptions`

    The current settings of the AWS IoT Events logging options.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT Events to perform logging.

    - **level** *(string) --*

      The logging level.

    - **enabled** *(boolean) --*

      If TRUE, logging is enabled for AWS IoT Events.

    - **detectorDebugOptions** *(list) --*

      Information that identifies those detector models and their detectors (instances) for which
      the logging level is given.

      - *(dict) --*

        The detector model and the specific detectors (instances) for which the logging level is
        given.

        - **detectorModelName** *(string) --*

          The name of the detector model.

        - **keyValue** *(string) --*

          The value of the input attribute key used to create the detector (the instance of the
          detector model).
    """


_ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)


class ClientDescribeLoggingOptionsResponseTypeDef(
    _ClientDescribeLoggingOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoggingOptions` `Response`

    - **loggingOptions** *(dict) --*

      The current settings of the AWS IoT Events logging options.

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Events to perform logging.

      - **level** *(string) --*

        The logging level.

      - **enabled** *(boolean) --*

        If TRUE, logging is enabled for AWS IoT Events.

      - **detectorDebugOptions** *(list) --*

        Information that identifies those detector models and their detectors (instances) for which
        the logging level is given.

        - *(dict) --*

          The detector model and the specific detectors (instances) for which the logging level is
          given.

          - **detectorModelName** *(string) --*

            The name of the detector model.

          - **keyValue** *(string) --*

            The value of the input attribute key used to create the detector (the instance of the
            detector model).
    """


_ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef = TypedDict(
    "_ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "evaluationMethod": str,
    },
    total=False,
)


class ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef(
    _ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef
):
    """
    Type definition for `ClientListDetectorModelVersionsResponse` `detectorModelVersionSummaries`

    Information about the detector model version.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **detectorModelVersion** *(string) --*

      The ID of the detector model version.

    - **detectorModelArn** *(string) --*

      The ARN of the detector model version.

    - **roleArn** *(string) --*

      The ARN of the role that grants the detector model permission to perform its tasks.

    - **creationTime** *(datetime) --*

      The time the detector model version was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the detector model version was updated.

    - **status** *(string) --*

      The status of the detector model version.

    - **evaluationMethod** *(string) --*

      When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
      order that the events are defined. When set to ``BATCH`` , variables are updated and
      events performed only after all event conditions are evaluated.
    """


_ClientListDetectorModelVersionsResponseTypeDef = TypedDict(
    "_ClientListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[
            ClientListDetectorModelVersionsResponsedetectorModelVersionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorModelVersionsResponseTypeDef(
    _ClientListDetectorModelVersionsResponseTypeDef
):
    """
    Type definition for `ClientListDetectorModelVersions` `Response`

    - **detectorModelVersionSummaries** *(list) --*

      Summary information about the detector model versions.

      - *(dict) --*

        Information about the detector model version.

        - **detectorModelName** *(string) --*

          The name of the detector model.

        - **detectorModelVersion** *(string) --*

          The ID of the detector model version.

        - **detectorModelArn** *(string) --*

          The ARN of the detector model version.

        - **roleArn** *(string) --*

          The ARN of the role that grants the detector model permission to perform its tasks.

        - **creationTime** *(datetime) --*

          The time the detector model version was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the detector model version was updated.

        - **status** *(string) --*

          The status of the detector model version.

        - **evaluationMethod** *(string) --*

          When set to ``SERIAL`` , variables are updated and event conditions evaluated in the
          order that the events are defined. When set to ``BATCH`` , variables are updated and
          events performed only after all event conditions are evaluated.

    - **nextToken** *(string) --*

      A token to retrieve the next set of results, or ``null`` if there are no additional results.
    """


_ClientListDetectorModelsResponsedetectorModelSummariesTypeDef = TypedDict(
    "_ClientListDetectorModelsResponsedetectorModelSummariesTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDescription": str,
        "creationTime": datetime,
    },
    total=False,
)


class ClientListDetectorModelsResponsedetectorModelSummariesTypeDef(
    _ClientListDetectorModelsResponsedetectorModelSummariesTypeDef
):
    """
    Type definition for `ClientListDetectorModelsResponse` `detectorModelSummaries`

    Information about the detector model.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **detectorModelDescription** *(string) --*

      A brief description of the detector model.

    - **creationTime** *(datetime) --*

      The time the detector model was created.
    """


_ClientListDetectorModelsResponseTypeDef = TypedDict(
    "_ClientListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[
            ClientListDetectorModelsResponsedetectorModelSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorModelsResponseTypeDef(_ClientListDetectorModelsResponseTypeDef):
    """
    Type definition for `ClientListDetectorModels` `Response`

    - **detectorModelSummaries** *(list) --*

      Summary information about the detector models.

      - *(dict) --*

        Information about the detector model.

        - **detectorModelName** *(string) --*

          The name of the detector model.

        - **detectorModelDescription** *(string) --*

          A brief description of the detector model.

        - **creationTime** *(datetime) --*

          The time the detector model was created.

    - **nextToken** *(string) --*

      A token to retrieve the next set of results, or ``null`` if there are no additional results.
    """


_ClientListInputsResponseinputSummariesTypeDef = TypedDict(
    "_ClientListInputsResponseinputSummariesTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientListInputsResponseinputSummariesTypeDef(
    _ClientListInputsResponseinputSummariesTypeDef
):
    """
    Type definition for `ClientListInputsResponse` `inputSummaries`

    Information about the input.

    - **inputName** *(string) --*

      The name of the input.

    - **inputDescription** *(string) --*

      A brief description of the input.

    - **inputArn** *(string) --*

      The ARN of the input.

    - **creationTime** *(datetime) --*

      The time the input was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the input was updated.

    - **status** *(string) --*

      The status of the input.
    """


_ClientListInputsResponseTypeDef = TypedDict(
    "_ClientListInputsResponseTypeDef",
    {
        "inputSummaries": List[ClientListInputsResponseinputSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListInputsResponseTypeDef(_ClientListInputsResponseTypeDef):
    """
    Type definition for `ClientListInputs` `Response`

    - **inputSummaries** *(list) --*

      Summary information about the inputs.

      - *(dict) --*

        Information about the input.

        - **inputName** *(string) --*

          The name of the input.

        - **inputDescription** *(string) --*

          A brief description of the input.

        - **inputArn** *(string) --*

          The ARN of the input.

        - **creationTime** *(datetime) --*

          The time the input was created.

        - **lastUpdateTime** *(datetime) --*

          The last time the input was updated.

        - **status** *(string) --*

          The status of the input.

    - **nextToken** *(string) --*

      A token to retrieve the next set of results, or ``null`` if there are no additional results.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    Metadata that can be used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      The list of tags assigned to the resource.

      - *(dict) --*

        Metadata that can be used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_RequiredClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef",
    {"detectorModelName": str},
)
_OptionalClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef",
    {"keyValue": str},
    total=False,
)


class ClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef(
    _RequiredClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef,
    _OptionalClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef,
):
    """
    Type definition for `ClientPutLoggingOptionsloggingOptions` `detectorDebugOptions`

    The detector model and the specific detectors (instances) for which the logging level is
    given.

    - **detectorModelName** *(string) --* **[REQUIRED]**

      The name of the detector model.

    - **keyValue** *(string) --*

      The value of the input attribute key used to create the detector (the instance of the
      detector model).
    """


_RequiredClientPutLoggingOptionsloggingOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsloggingOptionsTypeDef",
    {"roleArn": str, "level": str, "enabled": bool},
)
_OptionalClientPutLoggingOptionsloggingOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsloggingOptionsTypeDef",
    {
        "detectorDebugOptions": List[
            ClientPutLoggingOptionsloggingOptionsdetectorDebugOptionsTypeDef
        ]
    },
    total=False,
)


class ClientPutLoggingOptionsloggingOptionsTypeDef(
    _RequiredClientPutLoggingOptionsloggingOptionsTypeDef,
    _OptionalClientPutLoggingOptionsloggingOptionsTypeDef,
):
    """
    Type definition for `ClientPutLoggingOptions` `loggingOptions`

    The new values of the AWS IoT Events logging options.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants permission to AWS IoT Events to perform logging.

    - **level** *(string) --* **[REQUIRED]**

      The logging level.

    - **enabled** *(boolean) --* **[REQUIRED]**

      If TRUE, logging is enabled for AWS IoT Events.

    - **detectorDebugOptions** *(list) --*

      Information that identifies those detector models and their detectors (instances) for which the
      logging level is given.

      - *(dict) --*

        The detector model and the specific detectors (instances) for which the logging level is
        given.

        - **detectorModelName** *(string) --* **[REQUIRED]**

          The name of the detector model.

        - **keyValue** *(string) --*

          The value of the input attribute key used to create the detector (the instance of the
          detector model).
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    Metadata that can be used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef = TypedDict(
    "_ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "key": str,
        "evaluationMethod": str,
    },
    total=False,
)


class ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef(
    _ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModelResponse` `detectorModelConfiguration`

    Information about how the detector model is configured.

    - **detectorModelName** *(string) --*

      The name of the detector model.

    - **detectorModelVersion** *(string) --*

      The version of the detector model.

    - **detectorModelDescription** *(string) --*

      A brief description of the detector model.

    - **detectorModelArn** *(string) --*

      The ARN of the detector model.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT Events to perform its operations.

    - **creationTime** *(datetime) --*

      The time the detector model was created.

    - **lastUpdateTime** *(datetime) --*

      The time the detector model was last updated.

    - **status** *(string) --*

      The status of the detector model.

    - **key** *(string) --*

      The input attribute key used to identify a device or system to create a detector (an
      instance of the detector model) and then to route each input received to the appropriate
      detector (instance). This parameter uses a JSON-path expression to specify the
      attribute-value pair in the message payload of each input that is used to identify the
      device associated with the input.

    - **evaluationMethod** *(string) --*

      When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
      that the events are defined. When set to ``BATCH`` , variables are updated and events
      performed only after all event conditions are evaluated.
    """


_ClientUpdateDetectorModelResponseTypeDef = TypedDict(
    "_ClientUpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": ClientUpdateDetectorModelResponsedetectorModelConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateDetectorModelResponseTypeDef(
    _ClientUpdateDetectorModelResponseTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModel` `Response`

    - **detectorModelConfiguration** *(dict) --*

      Information about how the detector model is configured.

      - **detectorModelName** *(string) --*

        The name of the detector model.

      - **detectorModelVersion** *(string) --*

        The version of the detector model.

      - **detectorModelDescription** *(string) --*

        A brief description of the detector model.

      - **detectorModelArn** *(string) --*

        The ARN of the detector model.

      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Events to perform its operations.

      - **creationTime** *(datetime) --*

        The time the detector model was created.

      - **lastUpdateTime** *(datetime) --*

        The time the detector model was last updated.

      - **status** *(string) --*

        The status of the detector model.

      - **key** *(string) --*

        The input attribute key used to identify a device or system to create a detector (an
        instance of the detector model) and then to route each input received to the appropriate
        detector (instance). This parameter uses a JSON-path expression to specify the
        attribute-value pair in the message payload of each input that is used to identify the
        device associated with the input.

      - **evaluationMethod** *(string) --*

        When set to ``SERIAL`` , variables are updated and event conditions evaluated in the order
        that the events are defined. When set to ``BATCH`` , variables are updated and events
        performed only after all event conditions are evaluated.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {"eventName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnter` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef",
    {
        "events": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonEntereventsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstates` `onEnter`

    When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

    - **events** *(list) --*

      Specifies the actions that are performed when the state is entered and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {"eventName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonExit` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef",
    {
        "events": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonExiteventsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstates` `onExit`

    When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
    TRUE.

    - **events** *(list) --*

      Specifies the ``"actions"`` that are performed when the state is exited and the
      ``"condition"`` is TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputevents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {"eventName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef",
    {
        "condition": str,
        "actions": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsactionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInput` `events`

    Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the event.

    - **condition** *(string) --*

      [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
      performed. If not present, the actions are performed (=TRUE); if the expression
      result is not a Boolean value, the actions are NOT performed (=FALSE).

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `clearTimer`

    Information needed to clear the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to clear.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"deliveryStreamName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `firehose`

    Sends information about the detector model instance and the event which triggered
    the action to a Kinesis Data Firehose delivery stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The name of the Kinesis Data Firehose delivery stream where the data is written.

    - **separator** *(string) --*

      A character separator that is used to separate records written to the Kinesis
      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
      '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef",
    {"inputName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotEvents`

    Sends an IoT Events input, passing in information about the detector model
    instance and the event which triggered the action.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input where the data is sent.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef",
    {"mqttTopic": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `iotTopicPublish`

    Publishes an MQTT message with the given topic to the AWS IoT message broker.

    - **mqttTopic** *(string) --* **[REQUIRED]**

      The MQTT topic of the message.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef",
    {"functionArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `lambda`

    Calls an AWS Lambda function, passing in information about the detector model
    instance and the event which triggered the action.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the AWS Lambda function which is executed.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef",
    {"timerName": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `resetTimer`

    Information needed to reset the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer to reset.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef",
    {"timerName": str, "seconds": int},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setTimer`

    Information needed to set the timer.

    - **timerName** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The number of seconds until the timer expires. The minimum value is 60 seconds
      to ensure accuracy.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef",
    {"variableName": str, "value": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `setVariable`

    Sets a variable to a specified value.

    - **variableName** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef",
    {"targetArn": str},
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sns`

    Sends an Amazon SNS message.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the Amazon SNS target where the message is sent.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"queueUrl": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactions` `sqs`

    Sends information about the detector model instance and the event which triggered
    the action to an Amazon SQS queue.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue where the data is written.

    - **useBase64** *(boolean) --*

      Set this to TRUE if you want the data to be Base-64 encoded before it is
      written to the queue. Otherwise, set this to FALSE.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef",
    {
        "setVariable": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetVariableTypeDef,
        "sns": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssnsTypeDef,
        "iotTopicPublish": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotTopicPublishTypeDef,
        "setTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssetTimerTypeDef,
        "clearTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsclearTimerTypeDef,
        "resetTimer": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsresetTimerTypeDef,
        "lambda": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionslambdaTypeDef,
        "iotEvents": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsiotEventsTypeDef,
        "sqs": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionssqsTypeDef,
        "firehose": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsfirehoseTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEvents` `actions`

    An action to be performed when the ``"condition"`` is TRUE.

    - **setVariable** *(dict) --*

      Sets a variable to a specified value.

      - **variableName** *(string) --* **[REQUIRED]**

        The name of the variable.

      - **value** *(string) --* **[REQUIRED]**

        The new value of the variable.

    - **sns** *(dict) --*

      Sends an Amazon SNS message.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the Amazon SNS target where the message is sent.

    - **iotTopicPublish** *(dict) --*

      Publishes an MQTT message with the given topic to the AWS IoT message broker.

      - **mqttTopic** *(string) --* **[REQUIRED]**

        The MQTT topic of the message.

    - **setTimer** *(dict) --*

      Information needed to set the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer.

      - **seconds** *(integer) --* **[REQUIRED]**

        The number of seconds until the timer expires. The minimum value is 60 seconds
        to ensure accuracy.

    - **clearTimer** *(dict) --*

      Information needed to clear the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to clear.

    - **resetTimer** *(dict) --*

      Information needed to reset the timer.

      - **timerName** *(string) --* **[REQUIRED]**

        The name of the timer to reset.

    - **lambda** *(dict) --*

      Calls an AWS Lambda function, passing in information about the detector model
      instance and the event which triggered the action.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the AWS Lambda function which is executed.

    - **iotEvents** *(dict) --*

      Sends an IoT Events input, passing in information about the detector model
      instance and the event which triggered the action.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input where the data is sent.

    - **sqs** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to an Amazon SQS queue.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue where the data is written.

      - **useBase64** *(boolean) --*

        Set this to TRUE if you want the data to be Base-64 encoded before it is
        written to the queue. Otherwise, set this to FALSE.

    - **firehose** *(dict) --*

      Sends information about the detector model instance and the event which triggered
      the action to a Kinesis Data Firehose delivery stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The name of the Kinesis Data Firehose delivery stream where the data is written.

      - **separator** *(string) --*

        A character separator that is used to separate records written to the Kinesis
        Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
        '\\r\\n' (Windows newline), ',' (comma).
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {"eventName": str, "condition": str, "nextState": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef",
    {
        "actions": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsactionsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstatesonInput` `transitionEvents`

    Specifies the actions performed and the next state entered when a ``"condition"``
    evaluates to TRUE.

    - **eventName** *(string) --* **[REQUIRED]**

      The name of the transition event.

    - **condition** *(string) --* **[REQUIRED]**

      [Required] A Boolean expression that when TRUE causes the actions to be performed and
      the ``"nextState"`` to be entered.

    - **actions** *(list) --*

      The actions to be performed.

      - *(dict) --*

        An action to be performed when the ``"condition"`` is TRUE.

        - **setVariable** *(dict) --*

          Sets a variable to a specified value.

          - **variableName** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

        - **sns** *(dict) --*

          Sends an Amazon SNS message.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the Amazon SNS target where the message is sent.

        - **iotTopicPublish** *(dict) --*

          Publishes an MQTT message with the given topic to the AWS IoT message broker.

          - **mqttTopic** *(string) --* **[REQUIRED]**

            The MQTT topic of the message.

        - **setTimer** *(dict) --*

          Information needed to set the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The number of seconds until the timer expires. The minimum value is 60 seconds
            to ensure accuracy.

        - **clearTimer** *(dict) --*

          Information needed to clear the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to clear.

        - **resetTimer** *(dict) --*

          Information needed to reset the timer.

          - **timerName** *(string) --* **[REQUIRED]**

            The name of the timer to reset.

        - **lambda** *(dict) --*

          Calls an AWS Lambda function, passing in information about the detector model
          instance and the event which triggered the action.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the AWS Lambda function which is executed.

        - **iotEvents** *(dict) --*

          Sends an IoT Events input, passing in information about the detector model
          instance and the event which triggered the action.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input where the data is sent.

        - **sqs** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to an Amazon SQS queue.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue where the data is written.

          - **useBase64** *(boolean) --*

            Set this to TRUE if you want the data to be Base-64 encoded before it is
            written to the queue. Otherwise, set this to FALSE.

        - **firehose** *(dict) --*

          Sends information about the detector model instance and the event which triggered
          the action to a Kinesis Data Firehose delivery stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The name of the Kinesis Data Firehose delivery stream where the data is written.

          - **separator** *(string) --*

            A character separator that is used to separate records written to the Kinesis
            Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
            '\\r\\n' (Windows newline), ',' (comma).

    - **nextState** *(string) --* **[REQUIRED]**

      The next state to enter.
    """


_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef",
    {
        "events": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputeventsTypeDef
        ],
        "transitionEvents": List[
            ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputtransitionEventsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinitionstates` `onInput`

    When an input is received and the ``"condition"`` is TRUE, perform the specified
    ``"actions"`` .

    - **events** *(list) --*

      Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

      - *(dict) --*

        Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the event.

        - **condition** *(string) --*

          [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
          performed. If not present, the actions are performed (=TRUE); if the expression
          result is not a Boolean value, the actions are NOT performed (=FALSE).

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).

    - **transitionEvents** *(list) --*

      Specifies the actions performed, and the next state entered, when a ``"condition"``
      evaluates to TRUE.

      - *(dict) --*

        Specifies the actions performed and the next state entered when a ``"condition"``
        evaluates to TRUE.

        - **eventName** *(string) --* **[REQUIRED]**

          The name of the transition event.

        - **condition** *(string) --* **[REQUIRED]**

          [Required] A Boolean expression that when TRUE causes the actions to be performed and
          the ``"nextState"`` to be entered.

        - **actions** *(list) --*

          The actions to be performed.

          - *(dict) --*

            An action to be performed when the ``"condition"`` is TRUE.

            - **setVariable** *(dict) --*

              Sets a variable to a specified value.

              - **variableName** *(string) --* **[REQUIRED]**

                The name of the variable.

              - **value** *(string) --* **[REQUIRED]**

                The new value of the variable.

            - **sns** *(dict) --*

              Sends an Amazon SNS message.

              - **targetArn** *(string) --* **[REQUIRED]**

                The ARN of the Amazon SNS target where the message is sent.

            - **iotTopicPublish** *(dict) --*

              Publishes an MQTT message with the given topic to the AWS IoT message broker.

              - **mqttTopic** *(string) --* **[REQUIRED]**

                The MQTT topic of the message.

            - **setTimer** *(dict) --*

              Information needed to set the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer.

              - **seconds** *(integer) --* **[REQUIRED]**

                The number of seconds until the timer expires. The minimum value is 60 seconds
                to ensure accuracy.

            - **clearTimer** *(dict) --*

              Information needed to clear the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to clear.

            - **resetTimer** *(dict) --*

              Information needed to reset the timer.

              - **timerName** *(string) --* **[REQUIRED]**

                The name of the timer to reset.

            - **lambda** *(dict) --*

              Calls an AWS Lambda function, passing in information about the detector model
              instance and the event which triggered the action.

              - **functionArn** *(string) --* **[REQUIRED]**

                The ARN of the AWS Lambda function which is executed.

            - **iotEvents** *(dict) --*

              Sends an IoT Events input, passing in information about the detector model
              instance and the event which triggered the action.

              - **inputName** *(string) --* **[REQUIRED]**

                The name of the AWS IoT Events input where the data is sent.

            - **sqs** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to an Amazon SQS queue.

              - **queueUrl** *(string) --* **[REQUIRED]**

                The URL of the Amazon SQS queue where the data is written.

              - **useBase64** *(boolean) --*

                Set this to TRUE if you want the data to be Base-64 encoded before it is
                written to the queue. Otherwise, set this to FALSE.

            - **firehose** *(dict) --*

              Sends information about the detector model instance and the event which triggered
              the action to a Kinesis Data Firehose delivery stream.

              - **deliveryStreamName** *(string) --* **[REQUIRED]**

                The name of the Kinesis Data Firehose delivery stream where the data is written.

              - **separator** *(string) --*

                A character separator that is used to separate records written to the Kinesis
                Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                '\\r\\n' (Windows newline), ',' (comma).

        - **nextState** *(string) --* **[REQUIRED]**

          The next state to enter.
    """


_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef",
    {"stateName": str},
)
_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef",
    {
        "onInput": ClientUpdateDetectorModeldetectorModelDefinitionstatesonInputTypeDef,
        "onEnter": ClientUpdateDetectorModeldetectorModelDefinitionstatesonEnterTypeDef,
        "onExit": ClientUpdateDetectorModeldetectorModelDefinitionstatesonExitTypeDef,
    },
    total=False,
)


class ClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef(
    _RequiredClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef,
    _OptionalClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef,
):
    """
    Type definition for `ClientUpdateDetectorModeldetectorModelDefinition` `states`

    Information that defines a state of a detector.

    - **stateName** *(string) --* **[REQUIRED]**

      The name of the state.

    - **onInput** *(dict) --*

      When an input is received and the ``"condition"`` is TRUE, perform the specified
      ``"actions"`` .

      - **events** *(list) --*

        Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

      - **transitionEvents** *(list) --*

        Specifies the actions performed, and the next state entered, when a ``"condition"``
        evaluates to TRUE.

        - *(dict) --*

          Specifies the actions performed and the next state entered when a ``"condition"``
          evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the transition event.

          - **condition** *(string) --* **[REQUIRED]**

            [Required] A Boolean expression that when TRUE causes the actions to be performed and
            the ``"nextState"`` to be entered.

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

          - **nextState** *(string) --* **[REQUIRED]**

            The next state to enter.

    - **onEnter** *(dict) --*

      When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

      - **events** *(list) --*

        Specifies the actions that are performed when the state is entered and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).

    - **onExit** *(dict) --*

      When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
      TRUE.

      - **events** *(list) --*

        Specifies the ``"actions"`` that are performed when the state is exited and the
        ``"condition"`` is TRUE.

        - *(dict) --*

          Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

          - **eventName** *(string) --* **[REQUIRED]**

            The name of the event.

          - **condition** *(string) --*

            [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
            performed. If not present, the actions are performed (=TRUE); if the expression
            result is not a Boolean value, the actions are NOT performed (=FALSE).

          - **actions** *(list) --*

            The actions to be performed.

            - *(dict) --*

              An action to be performed when the ``"condition"`` is TRUE.

              - **setVariable** *(dict) --*

                Sets a variable to a specified value.

                - **variableName** *(string) --* **[REQUIRED]**

                  The name of the variable.

                - **value** *(string) --* **[REQUIRED]**

                  The new value of the variable.

              - **sns** *(dict) --*

                Sends an Amazon SNS message.

                - **targetArn** *(string) --* **[REQUIRED]**

                  The ARN of the Amazon SNS target where the message is sent.

              - **iotTopicPublish** *(dict) --*

                Publishes an MQTT message with the given topic to the AWS IoT message broker.

                - **mqttTopic** *(string) --* **[REQUIRED]**

                  The MQTT topic of the message.

              - **setTimer** *(dict) --*

                Information needed to set the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer.

                - **seconds** *(integer) --* **[REQUIRED]**

                  The number of seconds until the timer expires. The minimum value is 60 seconds
                  to ensure accuracy.

              - **clearTimer** *(dict) --*

                Information needed to clear the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to clear.

              - **resetTimer** *(dict) --*

                Information needed to reset the timer.

                - **timerName** *(string) --* **[REQUIRED]**

                  The name of the timer to reset.

              - **lambda** *(dict) --*

                Calls an AWS Lambda function, passing in information about the detector model
                instance and the event which triggered the action.

                - **functionArn** *(string) --* **[REQUIRED]**

                  The ARN of the AWS Lambda function which is executed.

              - **iotEvents** *(dict) --*

                Sends an IoT Events input, passing in information about the detector model
                instance and the event which triggered the action.

                - **inputName** *(string) --* **[REQUIRED]**

                  The name of the AWS IoT Events input where the data is sent.

              - **sqs** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to an Amazon SQS queue.

                - **queueUrl** *(string) --* **[REQUIRED]**

                  The URL of the Amazon SQS queue where the data is written.

                - **useBase64** *(boolean) --*

                  Set this to TRUE if you want the data to be Base-64 encoded before it is
                  written to the queue. Otherwise, set this to FALSE.

              - **firehose** *(dict) --*

                Sends information about the detector model instance and the event which triggered
                the action to a Kinesis Data Firehose delivery stream.

                - **deliveryStreamName** *(string) --* **[REQUIRED]**

                  The name of the Kinesis Data Firehose delivery stream where the data is written.

                - **separator** *(string) --*

                  A character separator that is used to separate records written to the Kinesis
                  Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                  '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientUpdateDetectorModeldetectorModelDefinitionTypeDef = TypedDict(
    "_ClientUpdateDetectorModeldetectorModelDefinitionTypeDef",
    {
        "states": List[ClientUpdateDetectorModeldetectorModelDefinitionstatesTypeDef],
        "initialStateName": str,
    },
)


class ClientUpdateDetectorModeldetectorModelDefinitionTypeDef(
    _ClientUpdateDetectorModeldetectorModelDefinitionTypeDef
):
    """
    Type definition for `ClientUpdateDetectorModel` `detectorModelDefinition`

    Information that defines how a detector operates.

    - **states** *(list) --* **[REQUIRED]**

      Information about the states of the detector.

      - *(dict) --*

        Information that defines a state of a detector.

        - **stateName** *(string) --* **[REQUIRED]**

          The name of the state.

        - **onInput** *(dict) --*

          When an input is received and the ``"condition"`` is TRUE, perform the specified
          ``"actions"`` .

          - **events** *(list) --*

            Specifies the actions performed when the ``"condition"`` evaluates to TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

          - **transitionEvents** *(list) --*

            Specifies the actions performed, and the next state entered, when a ``"condition"``
            evaluates to TRUE.

            - *(dict) --*

              Specifies the actions performed and the next state entered when a ``"condition"``
              evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the transition event.

              - **condition** *(string) --* **[REQUIRED]**

                [Required] A Boolean expression that when TRUE causes the actions to be performed and
                the ``"nextState"`` to be entered.

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

              - **nextState** *(string) --* **[REQUIRED]**

                The next state to enter.

        - **onEnter** *(dict) --*

          When entering this state, perform these ``"actions"`` if the ``"condition"`` is TRUE.

          - **events** *(list) --*

            Specifies the actions that are performed when the state is entered and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

        - **onExit** *(dict) --*

          When exiting this state, perform these ``"actions"`` if the specified ``"condition"`` is
          TRUE.

          - **events** *(list) --*

            Specifies the ``"actions"`` that are performed when the state is exited and the
            ``"condition"`` is TRUE.

            - *(dict) --*

              Specifies the ``"actions"`` to be performed when the ``"condition"`` evaluates to TRUE.

              - **eventName** *(string) --* **[REQUIRED]**

                The name of the event.

              - **condition** *(string) --*

                [Optional] The Boolean expression that when TRUE causes the ``"actions"`` to be
                performed. If not present, the actions are performed (=TRUE); if the expression
                result is not a Boolean value, the actions are NOT performed (=FALSE).

              - **actions** *(list) --*

                The actions to be performed.

                - *(dict) --*

                  An action to be performed when the ``"condition"`` is TRUE.

                  - **setVariable** *(dict) --*

                    Sets a variable to a specified value.

                    - **variableName** *(string) --* **[REQUIRED]**

                      The name of the variable.

                    - **value** *(string) --* **[REQUIRED]**

                      The new value of the variable.

                  - **sns** *(dict) --*

                    Sends an Amazon SNS message.

                    - **targetArn** *(string) --* **[REQUIRED]**

                      The ARN of the Amazon SNS target where the message is sent.

                  - **iotTopicPublish** *(dict) --*

                    Publishes an MQTT message with the given topic to the AWS IoT message broker.

                    - **mqttTopic** *(string) --* **[REQUIRED]**

                      The MQTT topic of the message.

                  - **setTimer** *(dict) --*

                    Information needed to set the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer.

                    - **seconds** *(integer) --* **[REQUIRED]**

                      The number of seconds until the timer expires. The minimum value is 60 seconds
                      to ensure accuracy.

                  - **clearTimer** *(dict) --*

                    Information needed to clear the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to clear.

                  - **resetTimer** *(dict) --*

                    Information needed to reset the timer.

                    - **timerName** *(string) --* **[REQUIRED]**

                      The name of the timer to reset.

                  - **lambda** *(dict) --*

                    Calls an AWS Lambda function, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **functionArn** *(string) --* **[REQUIRED]**

                      The ARN of the AWS Lambda function which is executed.

                  - **iotEvents** *(dict) --*

                    Sends an IoT Events input, passing in information about the detector model
                    instance and the event which triggered the action.

                    - **inputName** *(string) --* **[REQUIRED]**

                      The name of the AWS IoT Events input where the data is sent.

                  - **sqs** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to an Amazon SQS queue.

                    - **queueUrl** *(string) --* **[REQUIRED]**

                      The URL of the Amazon SQS queue where the data is written.

                    - **useBase64** *(boolean) --*

                      Set this to TRUE if you want the data to be Base-64 encoded before it is
                      written to the queue. Otherwise, set this to FALSE.

                  - **firehose** *(dict) --*

                    Sends information about the detector model instance and the event which triggered
                    the action to a Kinesis Data Firehose delivery stream.

                    - **deliveryStreamName** *(string) --* **[REQUIRED]**

                      The name of the Kinesis Data Firehose delivery stream where the data is written.

                    - **separator** *(string) --*

                      A character separator that is used to separate records written to the Kinesis
                      Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab),
                      '\\r\\n' (Windows newline), ',' (comma).

    - **initialStateName** *(string) --* **[REQUIRED]**

      The state that is entered at the creation of each detector (instance).
    """


_ClientUpdateInputResponseinputConfigurationTypeDef = TypedDict(
    "_ClientUpdateInputResponseinputConfigurationTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientUpdateInputResponseinputConfigurationTypeDef(
    _ClientUpdateInputResponseinputConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateInputResponse` `inputConfiguration`

    Information about the configuration of the input.

    - **inputName** *(string) --*

      The name of the input.

    - **inputDescription** *(string) --*

      A brief description of the input.

    - **inputArn** *(string) --*

      The ARN of the input.

    - **creationTime** *(datetime) --*

      The time the input was created.

    - **lastUpdateTime** *(datetime) --*

      The last time the input was updated.

    - **status** *(string) --*

      The status of the input.
    """


_ClientUpdateInputResponseTypeDef = TypedDict(
    "_ClientUpdateInputResponseTypeDef",
    {"inputConfiguration": ClientUpdateInputResponseinputConfigurationTypeDef},
    total=False,
)


class ClientUpdateInputResponseTypeDef(_ClientUpdateInputResponseTypeDef):
    """
    Type definition for `ClientUpdateInput` `Response`

    - **inputConfiguration** *(dict) --*

      Information about the configuration of the input.

      - **inputName** *(string) --*

        The name of the input.

      - **inputDescription** *(string) --*

        A brief description of the input.

      - **inputArn** *(string) --*

        The ARN of the input.

      - **creationTime** *(datetime) --*

        The time the input was created.

      - **lastUpdateTime** *(datetime) --*

        The last time the input was updated.

      - **status** *(string) --*

        The status of the input.
    """


_ClientUpdateInputinputDefinitionattributesTypeDef = TypedDict(
    "_ClientUpdateInputinputDefinitionattributesTypeDef", {"jsonPath": str}
)


class ClientUpdateInputinputDefinitionattributesTypeDef(
    _ClientUpdateInputinputDefinitionattributesTypeDef
):
    """
    Type definition for `ClientUpdateInputinputDefinition` `attributes`

    The attributes from the JSON payload that are made available by the input. Inputs are derived
    from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
    contains a JSON payload, and those attributes (and their paired values) specified here are
    available for use in the ``condition`` expressions used by detectors.

    - **jsonPath** *(string) --* **[REQUIRED]**

      An expression that specifies an attribute-value pair in a JSON structure. Use this to
      specify an attribute from the JSON payload that is made available by the input. Inputs are
      derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
      message contains a JSON payload, and the attribute (and its paired value) specified here
      are available for use in the ``"condition"`` expressions used by detectors.

      Syntax: ``<field-name>.<field-name>...``
    """


_ClientUpdateInputinputDefinitionTypeDef = TypedDict(
    "_ClientUpdateInputinputDefinitionTypeDef",
    {"attributes": List[ClientUpdateInputinputDefinitionattributesTypeDef]},
)


class ClientUpdateInputinputDefinitionTypeDef(_ClientUpdateInputinputDefinitionTypeDef):
    """
    Type definition for `ClientUpdateInput` `inputDefinition`

    The definition of the input.

    - **attributes** *(list) --* **[REQUIRED]**

      The attributes from the JSON payload that are made available by the input. Inputs are derived
      from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
      contains a JSON payload, and those attributes (and their paired values) specified here are
      available for use in the ``"condition"`` expressions used by detectors that monitor this input.

      - *(dict) --*

        The attributes from the JSON payload that are made available by the input. Inputs are derived
        from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message
        contains a JSON payload, and those attributes (and their paired values) specified here are
        available for use in the ``condition`` expressions used by detectors.

        - **jsonPath** *(string) --* **[REQUIRED]**

          An expression that specifies an attribute-value pair in a JSON structure. Use this to
          specify an attribute from the JSON payload that is made available by the input. Inputs are
          derived from messages sent to the AWS IoT Events system (``BatchPutMessage`` ). Each such
          message contains a JSON payload, and the attribute (and its paired value) specified here
          are available for use in the ``"condition"`` expressions used by detectors.

          Syntax: ``<field-name>.<field-name>...``
    """
