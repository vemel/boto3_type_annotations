"Main interface for iotevents-data type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientBatchPutMessagemessagesTypeDef",
    "ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    "ClientBatchUpdateDetectorResponseTypeDef",
    "ClientBatchUpdateDetectordetectorsstatetimersTypeDef",
    "ClientBatchUpdateDetectordetectorsstatevariablesTypeDef",
    "ClientBatchUpdateDetectordetectorsstateTypeDef",
    "ClientBatchUpdateDetectordetectorsTypeDef",
    "ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    "ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    "ClientDescribeDetectorResponsedetectorstateTypeDef",
    "ClientDescribeDetectorResponsedetectorTypeDef",
    "ClientDescribeDetectorResponseTypeDef",
    "ClientListDetectorsResponsedetectorSummariesstateTypeDef",
    "ClientListDetectorsResponsedetectorSummariesTypeDef",
    "ClientListDetectorsResponseTypeDef",
)


_ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef(
    _ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef
):
    """
    Type definition for `ClientBatchPutMessageResponse` `BatchPutMessageErrorEntries`

    Contains information about the errors encountered.

    - **messageId** *(string) --*

      The ID of the message that caused the error. (See the value corresponding to the
      ``"messageId"`` key in the ``"message"`` object.)

    - **errorCode** *(string) --*

      The code associated with the error.

    - **errorMessage** *(string) --*

      More information about the error.
    """


_ClientBatchPutMessageResponseTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutMessageResponseTypeDef(_ClientBatchPutMessageResponseTypeDef):
    """
    Type definition for `ClientBatchPutMessage` `Response`

    - **BatchPutMessageErrorEntries** *(list) --*

      A list of any errors encountered when sending the messages.

      - *(dict) --*

        Contains information about the errors encountered.

        - **messageId** *(string) --*

          The ID of the message that caused the error. (See the value corresponding to the
          ``"messageId"`` key in the ``"message"`` object.)

        - **errorCode** *(string) --*

          The code associated with the error.

        - **errorMessage** *(string) --*

          More information about the error.
    """


_ClientBatchPutMessagemessagesTypeDef = TypedDict(
    "_ClientBatchPutMessagemessagesTypeDef",
    {"messageId": str, "inputName": str, "payload": bytes},
)


class ClientBatchPutMessagemessagesTypeDef(_ClientBatchPutMessagemessagesTypeDef):
    """
    Type definition for `ClientBatchPutMessage` `messages`

    Information about a message.

    - **messageId** *(string) --* **[REQUIRED]**

      The ID to assign to the message. Within each batch sent, each ``"messageId"`` must be unique.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the input into which the message payload is transformed.

    - **payload** *(bytes) --* **[REQUIRED]**

      The payload of the message. This can be a JSON string or a Base-64-encoded string
      representing binary data (in which case you must decode it).
    """


_ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef(
    _ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef
):
    """
    Type definition for `ClientBatchUpdateDetectorResponse` `batchUpdateDetectorErrorEntries`

    Information about the error that occured when attempting to update a detector.

    - **messageId** *(string) --*

      The ``"messageId"`` of the update request that caused the error. (The value of the
      ``"messageId"`` in the update request ``"Detector"`` object.)

    - **errorCode** *(string) --*

      The code of the error.

    - **errorMessage** *(string) --*

      A message describing the error.
    """


_ClientBatchUpdateDetectorResponseTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List[
            ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchUpdateDetectorResponseTypeDef(
    _ClientBatchUpdateDetectorResponseTypeDef
):
    """
    Type definition for `ClientBatchUpdateDetector` `Response`

    - **batchUpdateDetectorErrorEntries** *(list) --*

      A list of those detector updates that resulted in errors. (If an error is listed here, the
      specific update did not occur.)

      - *(dict) --*

        Information about the error that occured when attempting to update a detector.

        - **messageId** *(string) --*

          The ``"messageId"`` of the update request that caused the error. (The value of the
          ``"messageId"`` in the update request ``"Detector"`` object.)

        - **errorCode** *(string) --*

          The code of the error.

        - **errorMessage** *(string) --*

          A message describing the error.
    """


_ClientBatchUpdateDetectordetectorsstatetimersTypeDef = TypedDict(
    "_ClientBatchUpdateDetectordetectorsstatetimersTypeDef",
    {"name": str, "seconds": int},
)


class ClientBatchUpdateDetectordetectorsstatetimersTypeDef(
    _ClientBatchUpdateDetectordetectorsstatetimersTypeDef
):
    """
    Type definition for `ClientBatchUpdateDetectordetectorsstate` `timers`

    The new setting of a timer.

    - **name** *(string) --* **[REQUIRED]**

      The name of the timer.

    - **seconds** *(integer) --* **[REQUIRED]**

      The new setting of the timer (the number of seconds before the timer elapses).
    """


_ClientBatchUpdateDetectordetectorsstatevariablesTypeDef = TypedDict(
    "_ClientBatchUpdateDetectordetectorsstatevariablesTypeDef",
    {"name": str, "value": str},
)


class ClientBatchUpdateDetectordetectorsstatevariablesTypeDef(
    _ClientBatchUpdateDetectordetectorsstatevariablesTypeDef
):
    """
    Type definition for `ClientBatchUpdateDetectordetectorsstate` `variables`

    The new value of the variable.

    - **name** *(string) --* **[REQUIRED]**

      The name of the variable.

    - **value** *(string) --* **[REQUIRED]**

      The new value of the variable.
    """


_ClientBatchUpdateDetectordetectorsstateTypeDef = TypedDict(
    "_ClientBatchUpdateDetectordetectorsstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientBatchUpdateDetectordetectorsstatevariablesTypeDef],
        "timers": List[ClientBatchUpdateDetectordetectorsstatetimersTypeDef],
    },
)


class ClientBatchUpdateDetectordetectorsstateTypeDef(
    _ClientBatchUpdateDetectordetectorsstateTypeDef
):
    """
    Type definition for `ClientBatchUpdateDetectordetectors` `state`

    The new state, variable values, and timer settings of the detector (instance).

    - **stateName** *(string) --* **[REQUIRED]**

      The name of the new state of the detector (instance).

    - **variables** *(list) --* **[REQUIRED]**

      The new values of the detector's variables. Any variable whose value isn't specified is
      cleared.

      - *(dict) --*

        The new value of the variable.

        - **name** *(string) --* **[REQUIRED]**

          The name of the variable.

        - **value** *(string) --* **[REQUIRED]**

          The new value of the variable.

    - **timers** *(list) --* **[REQUIRED]**

      The new values of the detector's timers. Any timer whose value isn't specified is cleared,
      and its timeout event won't occur.

      - *(dict) --*

        The new setting of a timer.

        - **name** *(string) --* **[REQUIRED]**

          The name of the timer.

        - **seconds** *(integer) --* **[REQUIRED]**

          The new setting of the timer (the number of seconds before the timer elapses).
    """


_RequiredClientBatchUpdateDetectordetectorsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateDetectordetectorsTypeDef",
    {
        "messageId": str,
        "detectorModelName": str,
        "state": ClientBatchUpdateDetectordetectorsstateTypeDef,
    },
)
_OptionalClientBatchUpdateDetectordetectorsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateDetectordetectorsTypeDef", {"keyValue": str}, total=False
)


class ClientBatchUpdateDetectordetectorsTypeDef(
    _RequiredClientBatchUpdateDetectordetectorsTypeDef,
    _OptionalClientBatchUpdateDetectordetectorsTypeDef,
):
    """
    Type definition for `ClientBatchUpdateDetector` `detectors`

    Information used to update the detector (instance).

    - **messageId** *(string) --* **[REQUIRED]**

      The ID to assign to the detector update ``"message"`` . Each ``"messageId"`` must be unique
      within each batch sent.

    - **detectorModelName** *(string) --* **[REQUIRED]**

      The name of the detector model that created the detectors (instances).

    - **keyValue** *(string) --*

      The value of the input key attribute (identifying the device or system) that caused the
      creation of this detector (instance).

    - **state** *(dict) --* **[REQUIRED]**

      The new state, variable values, and timer settings of the detector (instance).

      - **stateName** *(string) --* **[REQUIRED]**

        The name of the new state of the detector (instance).

      - **variables** *(list) --* **[REQUIRED]**

        The new values of the detector's variables. Any variable whose value isn't specified is
        cleared.

        - *(dict) --*

          The new value of the variable.

          - **name** *(string) --* **[REQUIRED]**

            The name of the variable.

          - **value** *(string) --* **[REQUIRED]**

            The new value of the variable.

      - **timers** *(list) --* **[REQUIRED]**

        The new values of the detector's timers. Any timer whose value isn't specified is cleared,
        and its timeout event won't occur.

        - *(dict) --*

          The new setting of a timer.

          - **name** *(string) --* **[REQUIRED]**

            The name of the timer.

          - **seconds** *(integer) --* **[REQUIRED]**

            The new setting of the timer (the number of seconds before the timer elapses).
    """


_ClientDescribeDetectorResponsedetectorstatetimersTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    {"name": str, "timestamp": datetime},
    total=False,
)


class ClientDescribeDetectorResponsedetectorstatetimersTypeDef(
    _ClientDescribeDetectorResponsedetectorstatetimersTypeDef
):
    """
    Type definition for `ClientDescribeDetectorResponsedetectorstate` `timers`

    The current state of a timer.

    - **name** *(string) --*

      The name of the timer.

    - **timestamp** *(datetime) --*

      The number of seconds which have elapsed on the timer.
    """


_ClientDescribeDetectorResponsedetectorstatevariablesTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeDetectorResponsedetectorstatevariablesTypeDef(
    _ClientDescribeDetectorResponsedetectorstatevariablesTypeDef
):
    """
    Type definition for `ClientDescribeDetectorResponsedetectorstate` `variables`

    The current state of the variable.

    - **name** *(string) --*

      The name of the variable.

    - **value** *(string) --*

      The current value of the variable.
    """


_ClientDescribeDetectorResponsedetectorstateTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientDescribeDetectorResponsedetectorstatevariablesTypeDef],
        "timers": List[ClientDescribeDetectorResponsedetectorstatetimersTypeDef],
    },
    total=False,
)


class ClientDescribeDetectorResponsedetectorstateTypeDef(
    _ClientDescribeDetectorResponsedetectorstateTypeDef
):
    """
    Type definition for `ClientDescribeDetectorResponsedetector` `state`

    The current state of the detector (instance).

    - **stateName** *(string) --*

      The name of the state.

    - **variables** *(list) --*

      The current values of the detector's variables.

      - *(dict) --*

        The current state of the variable.

        - **name** *(string) --*

          The name of the variable.

        - **value** *(string) --*

          The current value of the variable.

    - **timers** *(list) --*

      The current state of the detector's timers.

      - *(dict) --*

        The current state of a timer.

        - **name** *(string) --*

          The name of the timer.

        - **timestamp** *(datetime) --*

          The number of seconds which have elapsed on the timer.
    """


_ClientDescribeDetectorResponsedetectorTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientDescribeDetectorResponsedetectorstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeDetectorResponsedetectorTypeDef(
    _ClientDescribeDetectorResponsedetectorTypeDef
):
    """
    Type definition for `ClientDescribeDetectorResponse` `detector`

    Information about the detector (instance).

    - **detectorModelName** *(string) --*

      The name of the detector model that created this detector (instance).

    - **keyValue** *(string) --*

      The value of the key (identifying the device or system) that caused the creation of this
      detector (instance).

    - **detectorModelVersion** *(string) --*

      The version of the detector model that created this detector (instance).

    - **state** *(dict) --*

      The current state of the detector (instance).

      - **stateName** *(string) --*

        The name of the state.

      - **variables** *(list) --*

        The current values of the detector's variables.

        - *(dict) --*

          The current state of the variable.

          - **name** *(string) --*

            The name of the variable.

          - **value** *(string) --*

            The current value of the variable.

      - **timers** *(list) --*

        The current state of the detector's timers.

        - *(dict) --*

          The current state of a timer.

          - **name** *(string) --*

            The name of the timer.

          - **timestamp** *(datetime) --*

            The number of seconds which have elapsed on the timer.

    - **creationTime** *(datetime) --*

      The time the detector (instance) was created.

    - **lastUpdateTime** *(datetime) --*

      The time the detector (instance) was last updated.
    """


_ClientDescribeDetectorResponseTypeDef = TypedDict(
    "_ClientDescribeDetectorResponseTypeDef",
    {"detector": ClientDescribeDetectorResponsedetectorTypeDef},
    total=False,
)


class ClientDescribeDetectorResponseTypeDef(_ClientDescribeDetectorResponseTypeDef):
    """
    Type definition for `ClientDescribeDetector` `Response`

    - **detector** *(dict) --*

      Information about the detector (instance).

      - **detectorModelName** *(string) --*

        The name of the detector model that created this detector (instance).

      - **keyValue** *(string) --*

        The value of the key (identifying the device or system) that caused the creation of this
        detector (instance).

      - **detectorModelVersion** *(string) --*

        The version of the detector model that created this detector (instance).

      - **state** *(dict) --*

        The current state of the detector (instance).

        - **stateName** *(string) --*

          The name of the state.

        - **variables** *(list) --*

          The current values of the detector's variables.

          - *(dict) --*

            The current state of the variable.

            - **name** *(string) --*

              The name of the variable.

            - **value** *(string) --*

              The current value of the variable.

        - **timers** *(list) --*

          The current state of the detector's timers.

          - *(dict) --*

            The current state of a timer.

            - **name** *(string) --*

              The name of the timer.

            - **timestamp** *(datetime) --*

              The number of seconds which have elapsed on the timer.

      - **creationTime** *(datetime) --*

        The time the detector (instance) was created.

      - **lastUpdateTime** *(datetime) --*

        The time the detector (instance) was last updated.
    """


_ClientListDetectorsResponsedetectorSummariesstateTypeDef = TypedDict(
    "_ClientListDetectorsResponsedetectorSummariesstateTypeDef",
    {"stateName": str},
    total=False,
)


class ClientListDetectorsResponsedetectorSummariesstateTypeDef(
    _ClientListDetectorsResponsedetectorSummariesstateTypeDef
):
    """
    Type definition for `ClientListDetectorsResponsedetectorSummaries` `state`

    The current state of the detector (instance).

    - **stateName** *(string) --*

      The name of the state.
    """


_ClientListDetectorsResponsedetectorSummariesTypeDef = TypedDict(
    "_ClientListDetectorsResponsedetectorSummariesTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientListDetectorsResponsedetectorSummariesstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListDetectorsResponsedetectorSummariesTypeDef(
    _ClientListDetectorsResponsedetectorSummariesTypeDef
):
    """
    Type definition for `ClientListDetectorsResponse` `detectorSummaries`

    Information about the detector (instance).

    - **detectorModelName** *(string) --*

      The name of the detector model that created this detector (instance).

    - **keyValue** *(string) --*

      The value of the key (identifying the device or system) that caused the creation of this
      detector (instance).

    - **detectorModelVersion** *(string) --*

      The version of the detector model that created this detector (instance).

    - **state** *(dict) --*

      The current state of the detector (instance).

      - **stateName** *(string) --*

        The name of the state.

    - **creationTime** *(datetime) --*

      The time the detector (instance) was created.

    - **lastUpdateTime** *(datetime) --*

      The time the detector (instance) was last updated.
    """


_ClientListDetectorsResponseTypeDef = TypedDict(
    "_ClientListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List[ClientListDetectorsResponsedetectorSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorsResponseTypeDef(_ClientListDetectorsResponseTypeDef):
    """
    Type definition for `ClientListDetectors` `Response`

    - **detectorSummaries** *(list) --*

      A list of summary information about the detectors (instances).

      - *(dict) --*

        Information about the detector (instance).

        - **detectorModelName** *(string) --*

          The name of the detector model that created this detector (instance).

        - **keyValue** *(string) --*

          The value of the key (identifying the device or system) that caused the creation of this
          detector (instance).

        - **detectorModelVersion** *(string) --*

          The version of the detector model that created this detector (instance).

        - **state** *(dict) --*

          The current state of the detector (instance).

          - **stateName** *(string) --*

            The name of the state.

        - **creationTime** *(datetime) --*

          The time the detector (instance) was created.

        - **lastUpdateTime** *(datetime) --*

          The time the detector (instance) was last updated.

    - **nextToken** *(string) --*

      A token to retrieve the next set of results, or ``null`` if there are no additional results.
    """
