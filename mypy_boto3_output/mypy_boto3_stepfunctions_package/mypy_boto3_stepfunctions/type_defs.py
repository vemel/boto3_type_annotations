"Main interface for stepfunctions type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateActivityResponseTypeDef",
    "ClientCreateActivitytagsTypeDef",
    "ClientCreateStateMachineResponseTypeDef",
    "ClientCreateStateMachinetagsTypeDef",
    "ClientDescribeActivityResponseTypeDef",
    "ClientDescribeExecutionResponseTypeDef",
    "ClientDescribeStateMachineForExecutionResponseTypeDef",
    "ClientDescribeStateMachineResponseTypeDef",
    "ClientGetActivityTaskResponseTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    "ClientGetExecutionHistoryResponseeventsTypeDef",
    "ClientGetExecutionHistoryResponseTypeDef",
    "ClientListActivitiesResponseactivitiesTypeDef",
    "ClientListActivitiesResponseTypeDef",
    "ClientListExecutionsResponseexecutionsTypeDef",
    "ClientListExecutionsResponseTypeDef",
    "ClientListStateMachinesResponsestateMachinesTypeDef",
    "ClientListStateMachinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartExecutionResponseTypeDef",
    "ClientStopExecutionResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateStateMachineResponseTypeDef",
    "GetExecutionHistoryPaginatePaginationConfigTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef",
    "GetExecutionHistoryPaginateResponseeventsTypeDef",
    "GetExecutionHistoryPaginateResponseTypeDef",
    "ListActivitiesPaginatePaginationConfigTypeDef",
    "ListActivitiesPaginateResponseactivitiesTypeDef",
    "ListActivitiesPaginateResponseTypeDef",
    "ListExecutionsPaginatePaginationConfigTypeDef",
    "ListExecutionsPaginateResponseexecutionsTypeDef",
    "ListExecutionsPaginateResponseTypeDef",
    "ListStateMachinesPaginatePaginationConfigTypeDef",
    "ListStateMachinesPaginateResponsestateMachinesTypeDef",
    "ListStateMachinesPaginateResponseTypeDef",
)


_ClientCreateActivityResponseTypeDef = TypedDict(
    "_ClientCreateActivityResponseTypeDef",
    {"activityArn": str, "creationDate": datetime},
    total=False,
)


class ClientCreateActivityResponseTypeDef(_ClientCreateActivityResponseTypeDef):
    """
    Type definition for `ClientCreateActivity` `Response`

    - **activityArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the created activity.

    - **creationDate** *(datetime) --*

      The date the activity is created.
    """


_ClientCreateActivitytagsTypeDef = TypedDict(
    "_ClientCreateActivitytagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateActivitytagsTypeDef(_ClientCreateActivitytagsTypeDef):
    """
    Type definition for `ClientCreateActivity` `tags`

    Tags are key-value pairs that can be associated with Step Functions state machines and
    activities.

    An array of key-value pairs. For more information, see `Using Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
    *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .

    Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / = + -
    @`` .

    - **key** *(string) --*

      The key of a tag.

    - **value** *(string) --*

      The value of a tag.
    """


_ClientCreateStateMachineResponseTypeDef = TypedDict(
    "_ClientCreateStateMachineResponseTypeDef",
    {"stateMachineArn": str, "creationDate": datetime},
    total=False,
)


class ClientCreateStateMachineResponseTypeDef(_ClientCreateStateMachineResponseTypeDef):
    """
    Type definition for `ClientCreateStateMachine` `Response`

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the created state machine.

    - **creationDate** *(datetime) --*

      The date the state machine is created.
    """


_ClientCreateStateMachinetagsTypeDef = TypedDict(
    "_ClientCreateStateMachinetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateStateMachinetagsTypeDef(_ClientCreateStateMachinetagsTypeDef):
    """
    Type definition for `ClientCreateStateMachine` `tags`

    Tags are key-value pairs that can be associated with Step Functions state machines and
    activities.

    An array of key-value pairs. For more information, see `Using Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
    *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .

    Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / = + -
    @`` .

    - **key** *(string) --*

      The key of a tag.

    - **value** *(string) --*

      The value of a tag.
    """


_ClientDescribeActivityResponseTypeDef = TypedDict(
    "_ClientDescribeActivityResponseTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ClientDescribeActivityResponseTypeDef(_ClientDescribeActivityResponseTypeDef):
    """
    Type definition for `ClientDescribeActivity` `Response`

    - **activityArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the activity.

    - **name** *(string) --*

      The name of the activity.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **creationDate** *(datetime) --*

      The date the activity is created.
    """


_ClientDescribeExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeExecutionResponseTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": str,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "output": str,
    },
    total=False,
)


class ClientDescribeExecutionResponseTypeDef(_ClientDescribeExecutionResponseTypeDef):
    """
    Type definition for `ClientDescribeExecution` `Response`

    - **executionArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the execution.

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) of the executed stated machine.

    - **name** *(string) --*

      The name of the execution.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **status** *(string) --*

      The current status of the execution.

    - **startDate** *(datetime) --*

      The date the execution is started.

    - **stopDate** *(datetime) --*

      If the execution has already ended, the date the execution stopped.

    - **input** *(string) --*

      The string that contains the JSON input data of the execution.

    - **output** *(string) --*

      The JSON output data of the execution.

      .. note::

        This field is set only if the execution succeeds. If the execution fails, this field is
        null.
    """


_ClientDescribeStateMachineForExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeStateMachineForExecutionResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
    },
    total=False,
)


class ClientDescribeStateMachineForExecutionResponseTypeDef(
    _ClientDescribeStateMachineForExecutionResponseTypeDef
):
    """
    Type definition for `ClientDescribeStateMachineForExecution` `Response`

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) of the state machine associated with the execution.

    - **name** *(string) --*

      The name of the state machine associated with the execution.

    - **definition** *(string) --*

      The Amazon States Language definition of the state machine. See `Amazon States Language
      <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__
      .

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution.

    - **updateDate** *(datetime) --*

      The date and time the state machine associated with an execution was updated. For a newly
      created state machine, this is the creation date.
    """


_ClientDescribeStateMachineResponseTypeDef = TypedDict(
    "_ClientDescribeStateMachineResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": str,
        "definition": str,
        "roleArn": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientDescribeStateMachineResponseTypeDef(
    _ClientDescribeStateMachineResponseTypeDef
):
    """
    Type definition for `ClientDescribeStateMachine` `Response`

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the state machine.

    - **name** *(string) --*

      The name of the state machine.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **status** *(string) --*

      The current status of the state machine.

    - **definition** *(string) --*

      The Amazon States Language definition of the state machine. See `Amazon States Language
      <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__
      .

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The
      IAM role maintains security by granting Step Functions access to AWS resources.)

    - **creationDate** *(datetime) --*

      The date the state machine is created.
    """


_ClientGetActivityTaskResponseTypeDef = TypedDict(
    "_ClientGetActivityTaskResponseTypeDef",
    {"taskToken": str, "input": str},
    total=False,
)


class ClientGetActivityTaskResponseTypeDef(_ClientGetActivityTaskResponseTypeDef):
    """
    Type definition for `ClientGetActivityTask` `Response`

    - **taskToken** *(string) --*

      A token that identifies the scheduled task. This token must be copied and included in
      subsequent calls to  SendTaskHeartbeat ,  SendTaskSuccess or  SendTaskFailure in order to
      report the progress or completion of the task.

    - **input** *(string) --*

      The string that contains the JSON input data for the task.
    """


_ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activityFailedEventDetails`

    Contains details about an activity that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activityScheduleFailedEventDetails`

    Contains details about an activity schedule event that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activityScheduledEventDetails`

    Contains details about an activity scheduled during an execution.

    - **resource** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled activity.

    - **input** *(string) --*

      The JSON data input to the activity task.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the activity task.

    - **heartbeatInSeconds** *(integer) --*

      The maximum allowed duration between two heartbeats for the activity task.
    """


_ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activityStartedEventDetails`

    Contains details about the start of an activity during an execution.

    - **workerName** *(string) --*

      The name of the worker that the task is assigned to. These names are provided by the
      workers when calling  GetActivityTask .
    """


_ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activitySucceededEventDetails`

    Contains details about an activity that successfully terminated during an execution.

    - **output** *(string) --*

      The JSON data output by the activity task.
    """


_ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `activityTimedOutEventDetails`

    Contains details about an activity timeout that occurred during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `executionAbortedEventDetails`

    Contains details about an abort of an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `executionFailedEventDetails`

    Contains details about an execution failure event.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `executionStartedEventDetails`

    Contains details about the start of the execution.

    - **input** *(string) --*

      The JSON data input to the execution.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.
    """


_ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `executionSucceededEventDetails`

    Contains details about the successful termination of the execution.

    - **output** *(string) --*

      The JSON data output by the execution.
    """


_ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `executionTimedOutEventDetails`

    Contains details about the execution timeout that occurred during the execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionFailedEventDetails`

    Contains details about a lambda function that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionScheduleFailedEventDetails`

    Contains details about a failed lambda function schedule event that occurred during an
    execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionScheduledEventDetails`

    Contains details about a lambda function scheduled during an execution.

    - **resource** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled lambda function.

    - **input** *(string) --*

      The JSON data input to the lambda function.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the lambda function.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionStartFailedEventDetails`

    Contains details about a lambda function that failed to start during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionSucceededEventDetails`

    Contains details about a lambda function that terminated successfully during an execution.

    - **output** *(string) --*

      The JSON data output by the lambda function.
    """


_ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `lambdaFunctionTimedOutEventDetails`

    Contains details about a lambda function timeout that occurred during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `mapIterationAbortedEventDetails`

    Contains details about an iteration of a Map state that was aborted.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `mapIterationFailedEventDetails`

    Contains details about an iteration of a Map state that failed.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `mapIterationStartedEventDetails`

    Contains details about an iteration of a Map state that was started.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `mapIterationSucceededEventDetails`

    Contains details about an iteration of a Map state that succeeded.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `mapStateStartedEventDetails`

    Contains details about Map state that was started.

    - **length** *(integer) --*

      The size of the array for Map state iterations.
    """


_ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `stateEnteredEventDetails`

    Contains details about a state entered during an execution.

    - **name** *(string) --*

      The name of the state.

    - **input** *(string) --*

      The string that contains the JSON input data for the state.
    """


_ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `stateExitedEventDetails`

    Contains details about an exit from a state during an execution.

    - **name** *(string) --*

      The name of the state.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **output** *(string) --*

      The JSON output data of the state.
    """


_ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskFailedEventDetails`

    Contains details about the failure of a task.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskScheduledEventDetails`

    Contains details about a task that was scheduled.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **region** *(string) --*

      The region of the scheduled task

    - **parameters** *(string) --*

      The JSON data passed to the resource referenced in a task state.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the task.
    """


_ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskStartFailedEventDetails`

    Contains details about a task that failed to start.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskStartedEventDetails`

    Contains details about a task that was started.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.
    """


_ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskSubmitFailedEventDetails`

    Contains details about a task that where the submit failed.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskSubmittedEventDetails`

    Contains details about a submitted task.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **output** *(string) --*

      The response from a resource when a task has started.
    """


_ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskSucceededEventDetails`

    Contains details about a task that succeeded.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **output** *(string) --*

      The full JSON response from a resource when a task has succeeded. This response becomes
      the output of the related task.
    """


_ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef(
    _ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponseevents` `taskTimedOutEventDetails`

    Contains details about a task that timed out.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_ClientGetExecutionHistoryResponseeventsTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseeventsTypeDef",
    {
        "timestamp": datetime,
        "type": str,
        "id": int,
        "previousEventId": int,
        "activityFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": ClientGetExecutionHistoryResponseeventsactivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": ClientGetExecutionHistoryResponseeventsactivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": ClientGetExecutionHistoryResponseeventsactivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsactivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": ClientGetExecutionHistoryResponseeventstaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": ClientGetExecutionHistoryResponseeventstaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": ClientGetExecutionHistoryResponseeventstaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": ClientGetExecutionHistoryResponseeventstaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": ClientGetExecutionHistoryResponseeventstaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": ClientGetExecutionHistoryResponseeventsexecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": ClientGetExecutionHistoryResponseeventsexecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventsexecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationStartedEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationSucceededEventDetailsTypeDef,
        "mapIterationFailedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationFailedEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": ClientGetExecutionHistoryResponseeventsmapIterationAbortedEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": ClientGetExecutionHistoryResponseeventslambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": ClientGetExecutionHistoryResponseeventsstateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": ClientGetExecutionHistoryResponseeventsstateExitedEventDetailsTypeDef,
    },
    total=False,
)


class ClientGetExecutionHistoryResponseeventsTypeDef(
    _ClientGetExecutionHistoryResponseeventsTypeDef
):
    """
    Type definition for `ClientGetExecutionHistoryResponse` `events`

    Contains details about the events of an execution.

    - **timestamp** *(datetime) --*

      The date and time the event occurred.

    - **type** *(string) --*

      The type of the event.

    - **id** *(integer) --*

      The id of the event. Events are numbered sequentially, starting at one.

    - **previousEventId** *(integer) --*

      The id of the previous event.

    - **activityFailedEventDetails** *(dict) --*

      Contains details about an activity that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **activityScheduleFailedEventDetails** *(dict) --*

      Contains details about an activity schedule event that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **activityScheduledEventDetails** *(dict) --*

      Contains details about an activity scheduled during an execution.

      - **resource** *(string) --*

        The Amazon Resource Name (ARN) of the scheduled activity.

      - **input** *(string) --*

        The JSON data input to the activity task.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the activity task.

      - **heartbeatInSeconds** *(integer) --*

        The maximum allowed duration between two heartbeats for the activity task.

    - **activityStartedEventDetails** *(dict) --*

      Contains details about the start of an activity during an execution.

      - **workerName** *(string) --*

        The name of the worker that the task is assigned to. These names are provided by the
        workers when calling  GetActivityTask .

    - **activitySucceededEventDetails** *(dict) --*

      Contains details about an activity that successfully terminated during an execution.

      - **output** *(string) --*

        The JSON data output by the activity task.

    - **activityTimedOutEventDetails** *(dict) --*

      Contains details about an activity timeout that occurred during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **taskFailedEventDetails** *(dict) --*

      Contains details about the failure of a task.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskScheduledEventDetails** *(dict) --*

      Contains details about a task that was scheduled.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **region** *(string) --*

        The region of the scheduled task

      - **parameters** *(string) --*

        The JSON data passed to the resource referenced in a task state.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the task.

    - **taskStartFailedEventDetails** *(dict) --*

      Contains details about a task that failed to start.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskStartedEventDetails** *(dict) --*

      Contains details about a task that was started.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

    - **taskSubmitFailedEventDetails** *(dict) --*

      Contains details about a task that where the submit failed.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskSubmittedEventDetails** *(dict) --*

      Contains details about a submitted task.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **output** *(string) --*

        The response from a resource when a task has started.

    - **taskSucceededEventDetails** *(dict) --*

      Contains details about a task that succeeded.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **output** *(string) --*

        The full JSON response from a resource when a task has succeeded. This response becomes
        the output of the related task.

    - **taskTimedOutEventDetails** *(dict) --*

      Contains details about a task that timed out.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionFailedEventDetails** *(dict) --*

      Contains details about an execution failure event.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionStartedEventDetails** *(dict) --*

      Contains details about the start of the execution.

      - **input** *(string) --*

        The JSON data input to the execution.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.

    - **executionSucceededEventDetails** *(dict) --*

      Contains details about the successful termination of the execution.

      - **output** *(string) --*

        The JSON data output by the execution.

    - **executionAbortedEventDetails** *(dict) --*

      Contains details about an abort of an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionTimedOutEventDetails** *(dict) --*

      Contains details about the execution timeout that occurred during the execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **mapStateStartedEventDetails** *(dict) --*

      Contains details about Map state that was started.

      - **length** *(integer) --*

        The size of the array for Map state iterations.

    - **mapIterationStartedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that was started.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationSucceededEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that succeeded.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationFailedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that failed.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationAbortedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that was aborted.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **lambdaFunctionFailedEventDetails** *(dict) --*

      Contains details about a lambda function that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionScheduleFailedEventDetails** *(dict) --*

      Contains details about a failed lambda function schedule event that occurred during an
      execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionScheduledEventDetails** *(dict) --*

      Contains details about a lambda function scheduled during an execution.

      - **resource** *(string) --*

        The Amazon Resource Name (ARN) of the scheduled lambda function.

      - **input** *(string) --*

        The JSON data input to the lambda function.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the lambda function.

    - **lambdaFunctionStartFailedEventDetails** *(dict) --*

      Contains details about a lambda function that failed to start during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionSucceededEventDetails** *(dict) --*

      Contains details about a lambda function that terminated successfully during an execution.

      - **output** *(string) --*

        The JSON data output by the lambda function.

    - **lambdaFunctionTimedOutEventDetails** *(dict) --*

      Contains details about a lambda function timeout that occurred during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **stateEnteredEventDetails** *(dict) --*

      Contains details about a state entered during an execution.

      - **name** *(string) --*

        The name of the state.

      - **input** *(string) --*

        The string that contains the JSON input data for the state.

    - **stateExitedEventDetails** *(dict) --*

      Contains details about an exit from a state during an execution.

      - **name** *(string) --*

        The name of the state.

        A name must *not* contain:

        * white space

        * brackets ``< > { } [ ]``

        * wildcard characters ``? *``

        * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

        * control characters (``U+0000-001F`` , ``U+007F-009F`` )

      - **output** *(string) --*

        The JSON output data of the state.
    """


_ClientGetExecutionHistoryResponseTypeDef = TypedDict(
    "_ClientGetExecutionHistoryResponseTypeDef",
    {"events": List[ClientGetExecutionHistoryResponseeventsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetExecutionHistoryResponseTypeDef(
    _ClientGetExecutionHistoryResponseTypeDef
):
    """
    Type definition for `ClientGetExecutionHistory` `Response`

    - **events** *(list) --*

      The list of events that occurred in the execution.

      - *(dict) --*

        Contains details about the events of an execution.

        - **timestamp** *(datetime) --*

          The date and time the event occurred.

        - **type** *(string) --*

          The type of the event.

        - **id** *(integer) --*

          The id of the event. Events are numbered sequentially, starting at one.

        - **previousEventId** *(integer) --*

          The id of the previous event.

        - **activityFailedEventDetails** *(dict) --*

          Contains details about an activity that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **activityScheduleFailedEventDetails** *(dict) --*

          Contains details about an activity schedule event that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **activityScheduledEventDetails** *(dict) --*

          Contains details about an activity scheduled during an execution.

          - **resource** *(string) --*

            The Amazon Resource Name (ARN) of the scheduled activity.

          - **input** *(string) --*

            The JSON data input to the activity task.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the activity task.

          - **heartbeatInSeconds** *(integer) --*

            The maximum allowed duration between two heartbeats for the activity task.

        - **activityStartedEventDetails** *(dict) --*

          Contains details about the start of an activity during an execution.

          - **workerName** *(string) --*

            The name of the worker that the task is assigned to. These names are provided by the
            workers when calling  GetActivityTask .

        - **activitySucceededEventDetails** *(dict) --*

          Contains details about an activity that successfully terminated during an execution.

          - **output** *(string) --*

            The JSON data output by the activity task.

        - **activityTimedOutEventDetails** *(dict) --*

          Contains details about an activity timeout that occurred during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **taskFailedEventDetails** *(dict) --*

          Contains details about the failure of a task.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskScheduledEventDetails** *(dict) --*

          Contains details about a task that was scheduled.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **region** *(string) --*

            The region of the scheduled task

          - **parameters** *(string) --*

            The JSON data passed to the resource referenced in a task state.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the task.

        - **taskStartFailedEventDetails** *(dict) --*

          Contains details about a task that failed to start.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskStartedEventDetails** *(dict) --*

          Contains details about a task that was started.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

        - **taskSubmitFailedEventDetails** *(dict) --*

          Contains details about a task that where the submit failed.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskSubmittedEventDetails** *(dict) --*

          Contains details about a submitted task.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **output** *(string) --*

            The response from a resource when a task has started.

        - **taskSucceededEventDetails** *(dict) --*

          Contains details about a task that succeeded.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **output** *(string) --*

            The full JSON response from a resource when a task has succeeded. This response becomes
            the output of the related task.

        - **taskTimedOutEventDetails** *(dict) --*

          Contains details about a task that timed out.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionFailedEventDetails** *(dict) --*

          Contains details about an execution failure event.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionStartedEventDetails** *(dict) --*

          Contains details about the start of the execution.

          - **input** *(string) --*

            The JSON data input to the execution.

          - **roleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.

        - **executionSucceededEventDetails** *(dict) --*

          Contains details about the successful termination of the execution.

          - **output** *(string) --*

            The JSON data output by the execution.

        - **executionAbortedEventDetails** *(dict) --*

          Contains details about an abort of an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionTimedOutEventDetails** *(dict) --*

          Contains details about the execution timeout that occurred during the execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **mapStateStartedEventDetails** *(dict) --*

          Contains details about Map state that was started.

          - **length** *(integer) --*

            The size of the array for Map state iterations.

        - **mapIterationStartedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that was started.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationSucceededEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that succeeded.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationFailedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that failed.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationAbortedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that was aborted.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **lambdaFunctionFailedEventDetails** *(dict) --*

          Contains details about a lambda function that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionScheduleFailedEventDetails** *(dict) --*

          Contains details about a failed lambda function schedule event that occurred during an
          execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionScheduledEventDetails** *(dict) --*

          Contains details about a lambda function scheduled during an execution.

          - **resource** *(string) --*

            The Amazon Resource Name (ARN) of the scheduled lambda function.

          - **input** *(string) --*

            The JSON data input to the lambda function.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the lambda function.

        - **lambdaFunctionStartFailedEventDetails** *(dict) --*

          Contains details about a lambda function that failed to start during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionSucceededEventDetails** *(dict) --*

          Contains details about a lambda function that terminated successfully during an execution.

          - **output** *(string) --*

            The JSON data output by the lambda function.

        - **lambdaFunctionTimedOutEventDetails** *(dict) --*

          Contains details about a lambda function timeout that occurred during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **stateEnteredEventDetails** *(dict) --*

          Contains details about a state entered during an execution.

          - **name** *(string) --*

            The name of the state.

          - **input** *(string) --*

            The string that contains the JSON input data for the state.

        - **stateExitedEventDetails** *(dict) --*

          Contains details about an exit from a state during an execution.

          - **name** *(string) --*

            The name of the state.

            A name must *not* contain:

            * white space

            * brackets ``< > { } [ ]``

            * wildcard characters ``? *``

            * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

            * control characters (``U+0000-001F`` , ``U+007F-009F`` )

          - **output** *(string) --*

            The JSON output data of the state.

    - **nextToken** *(string) --*

      If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is
      a unique pagination token for each page. Make the call again using the returned token to
      retrieve the next page. Keep all other arguments unchanged. Each pagination token expires
      after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken*
      error.
    """


_ClientListActivitiesResponseactivitiesTypeDef = TypedDict(
    "_ClientListActivitiesResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ClientListActivitiesResponseactivitiesTypeDef(
    _ClientListActivitiesResponseactivitiesTypeDef
):
    """
    Type definition for `ClientListActivitiesResponse` `activities`

    Contains details about an activity.

    - **activityArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the activity.

    - **name** *(string) --*

      The name of the activity.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **creationDate** *(datetime) --*

      The date the activity is created.
    """


_ClientListActivitiesResponseTypeDef = TypedDict(
    "_ClientListActivitiesResponseTypeDef",
    {
        "activities": List[ClientListActivitiesResponseactivitiesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListActivitiesResponseTypeDef(_ClientListActivitiesResponseTypeDef):
    """
    Type definition for `ClientListActivities` `Response`

    - **activities** *(list) --*

      The list of activities.

      - *(dict) --*

        Contains details about an activity.

        - **activityArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the activity.

        - **name** *(string) --*

          The name of the activity.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **creationDate** *(datetime) --*

          The date the activity is created.

    - **nextToken** *(string) --*

      If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is
      a unique pagination token for each page. Make the call again using the returned token to
      retrieve the next page. Keep all other arguments unchanged. Each pagination token expires
      after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken*
      error.
    """


_ClientListExecutionsResponseexecutionsTypeDef = TypedDict(
    "_ClientListExecutionsResponseexecutionsTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": str,
        "startDate": datetime,
        "stopDate": datetime,
    },
    total=False,
)


class ClientListExecutionsResponseexecutionsTypeDef(
    _ClientListExecutionsResponseexecutionsTypeDef
):
    """
    Type definition for `ClientListExecutionsResponse` `executions`

    Contains details about an execution.

    - **executionArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the execution.

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) of the executed state machine.

    - **name** *(string) --*

      The name of the execution.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **status** *(string) --*

      The current status of the execution.

    - **startDate** *(datetime) --*

      The date the execution started.

    - **stopDate** *(datetime) --*

      If the execution already ended, the date the execution stopped.
    """


_ClientListExecutionsResponseTypeDef = TypedDict(
    "_ClientListExecutionsResponseTypeDef",
    {
        "executions": List[ClientListExecutionsResponseexecutionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListExecutionsResponseTypeDef(_ClientListExecutionsResponseTypeDef):
    """
    Type definition for `ClientListExecutions` `Response`

    - **executions** *(list) --*

      The list of matching executions.

      - *(dict) --*

        Contains details about an execution.

        - **executionArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the execution.

        - **stateMachineArn** *(string) --*

          The Amazon Resource Name (ARN) of the executed state machine.

        - **name** *(string) --*

          The name of the execution.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **status** *(string) --*

          The current status of the execution.

        - **startDate** *(datetime) --*

          The date the execution started.

        - **stopDate** *(datetime) --*

          If the execution already ended, the date the execution stopped.

    - **nextToken** *(string) --*

      If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is
      a unique pagination token for each page. Make the call again using the returned token to
      retrieve the next page. Keep all other arguments unchanged. Each pagination token expires
      after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken*
      error.
    """


_ClientListStateMachinesResponsestateMachinesTypeDef = TypedDict(
    "_ClientListStateMachinesResponsestateMachinesTypeDef",
    {"stateMachineArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ClientListStateMachinesResponsestateMachinesTypeDef(
    _ClientListStateMachinesResponsestateMachinesTypeDef
):
    """
    Type definition for `ClientListStateMachinesResponse` `stateMachines`

    Contains details about the state machine.

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the state machine.

    - **name** *(string) --*

      The name of the state machine.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **creationDate** *(datetime) --*

      The date the state machine is created.
    """


_ClientListStateMachinesResponseTypeDef = TypedDict(
    "_ClientListStateMachinesResponseTypeDef",
    {
        "stateMachines": List[ClientListStateMachinesResponsestateMachinesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListStateMachinesResponseTypeDef(_ClientListStateMachinesResponseTypeDef):
    """
    Type definition for `ClientListStateMachines` `Response`

    - **stateMachines** *(list) --*

      - *(dict) --*

        Contains details about the state machine.

        - **stateMachineArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the state machine.

        - **name** *(string) --*

          The name of the state machine.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **creationDate** *(datetime) --*

          The date the state machine is created.

    - **nextToken** *(string) --*

      If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is
      a unique pagination token for each page. Make the call again using the returned token to
      retrieve the next page. Keep all other arguments unchanged. Each pagination token expires
      after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken*
      error.
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

    Tags are key-value pairs that can be associated with Step Functions state machines and
    activities.

    An array of key-value pairs. For more information, see `Using Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in
    the *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .

    Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / = +
    - @`` .

    - **key** *(string) --*

      The key of a tag.

    - **value** *(string) --*

      The value of a tag.
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

      An array of tags associated with the resource.

      - *(dict) --*

        Tags are key-value pairs that can be associated with Step Functions state machines and
        activities.

        An array of key-value pairs. For more information, see `Using Cost Allocation Tags
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in
        the *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .

        Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / = +
        - @`` .

        - **key** *(string) --*

          The key of a tag.

        - **value** *(string) --*

          The value of a tag.
    """


_ClientStartExecutionResponseTypeDef = TypedDict(
    "_ClientStartExecutionResponseTypeDef",
    {"executionArn": str, "startDate": datetime},
    total=False,
)


class ClientStartExecutionResponseTypeDef(_ClientStartExecutionResponseTypeDef):
    """
    Type definition for `ClientStartExecution` `Response`

    - **executionArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the execution.

    - **startDate** *(datetime) --*

      The date the execution is started.
    """


_ClientStopExecutionResponseTypeDef = TypedDict(
    "_ClientStopExecutionResponseTypeDef", {"stopDate": datetime}, total=False
)


class ClientStopExecutionResponseTypeDef(_ClientStopExecutionResponseTypeDef):
    """
    Type definition for `ClientStopExecution` `Response`

    - **stopDate** *(datetime) --*

      The date the execution is stopped.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    Tags are key-value pairs that can be associated with Step Functions state machines and
    activities.

    An array of key-value pairs. For more information, see `Using Cost Allocation Tags
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the
    *AWS Billing and Cost Management User Guide* , and `Controlling Access Using IAM Tags
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`__ .

    Tags may only contain Unicode letters, digits, white space, or these symbols: ``_ . : / = + -
    @`` .

    - **key** *(string) --*

      The key of a tag.

    - **value** *(string) --*

      The value of a tag.
    """


_ClientUpdateStateMachineResponseTypeDef = TypedDict(
    "_ClientUpdateStateMachineResponseTypeDef", {"updateDate": datetime}, total=False
)


class ClientUpdateStateMachineResponseTypeDef(_ClientUpdateStateMachineResponseTypeDef):
    """
    Type definition for `ClientUpdateStateMachine` `Response`

    - **updateDate** *(datetime) --*

      The date and time the state machine was updated.
    """


_GetExecutionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetExecutionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetExecutionHistoryPaginatePaginationConfigTypeDef(
    _GetExecutionHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginate` `PaginationConfig`

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


_GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activityFailedEventDetails`

    Contains details about an activity that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activityScheduleFailedEventDetails`

    Contains details about an activity schedule event that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activityScheduledEventDetails`

    Contains details about an activity scheduled during an execution.

    - **resource** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled activity.

    - **input** *(string) --*

      The JSON data input to the activity task.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the activity task.

    - **heartbeatInSeconds** *(integer) --*

      The maximum allowed duration between two heartbeats for the activity task.
    """


_GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef",
    {"workerName": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activityStartedEventDetails`

    Contains details about the start of an activity during an execution.

    - **workerName** *(string) --*

      The name of the worker that the task is assigned to. These names are provided by the
      workers when calling  GetActivityTask .
    """


_GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activitySucceededEventDetails`

    Contains details about an activity that successfully terminated during an execution.

    - **output** *(string) --*

      The JSON data output by the activity task.
    """


_GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `activityTimedOutEventDetails`

    Contains details about an activity timeout that occurred during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `executionAbortedEventDetails`

    Contains details about an abort of an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `executionFailedEventDetails`

    Contains details about an execution failure event.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef",
    {"input": str, "roleArn": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `executionStartedEventDetails`

    Contains details about the start of the execution.

    - **input** *(string) --*

      The JSON data input to the execution.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.
    """


_GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `executionSucceededEventDetails`

    Contains details about the successful termination of the execution.

    - **output** *(string) --*

      The JSON data output by the execution.
    """


_GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `executionTimedOutEventDetails`

    Contains details about the execution timeout that occurred during the execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionFailedEventDetails`

    Contains details about a lambda function that failed during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionScheduleFailedEventDetails`

    Contains details about a failed lambda function schedule event that occurred during an
    execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef",
    {"resource": str, "input": str, "timeoutInSeconds": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionScheduledEventDetails`

    Contains details about a lambda function scheduled during an execution.

    - **resource** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled lambda function.

    - **input** *(string) --*

      The JSON data input to the lambda function.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the lambda function.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionStartFailedEventDetails`

    Contains details about a lambda function that failed to start during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionSucceededEventDetails`

    Contains details about a lambda function that terminated successfully during an execution.

    - **output** *(string) --*

      The JSON data output by the lambda function.
    """


_GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef",
    {"error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `lambdaFunctionTimedOutEventDetails`

    Contains details about a lambda function timeout that occurred during an execution.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the timeout.
    """


_GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `mapIterationAbortedEventDetails`

    Contains details about an iteration of a Map state that was aborted.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `mapIterationFailedEventDetails`

    Contains details about an iteration of a Map state that failed.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `mapIterationStartedEventDetails`

    Contains details about an iteration of a Map state that was started.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef",
    {"name": str, "index": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `mapIterationSucceededEventDetails`

    Contains details about an iteration of a Map state that succeeded.

    - **name** *(string) --*

      The name of the iteration’s parent Map state.

    - **index** *(integer) --*

      The index of the array belonging to the Map state iteration.
    """


_GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef",
    {"length": int},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `mapStateStartedEventDetails`

    Contains details about Map state that was started.

    - **length** *(integer) --*

      The size of the array for Map state iterations.
    """


_GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef",
    {"name": str, "input": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `stateEnteredEventDetails`

    Contains details about a state entered during an execution.

    - **name** *(string) --*

      The name of the state.

    - **input** *(string) --*

      The string that contains the JSON input data for the state.
    """


_GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef",
    {"name": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `stateExitedEventDetails`

    Contains details about an exit from a state during an execution.

    - **name** *(string) --*

      The name of the state.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **output** *(string) --*

      The JSON output data of the state.
    """


_GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskFailedEventDetails`

    Contains details about the failure of a task.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": int,
    },
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskScheduledEventDetails`

    Contains details about a task that was scheduled.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **region** *(string) --*

      The region of the scheduled task

    - **parameters** *(string) --*

      The JSON data passed to the resource referenced in a task state.

    - **timeoutInSeconds** *(integer) --*

      The maximum allowed duration of the task.
    """


_GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskStartFailedEventDetails`

    Contains details about a task that failed to start.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef",
    {"resourceType": str, "resource": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskStartedEventDetails`

    Contains details about a task that was started.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.
    """


_GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskSubmitFailedEventDetails`

    Contains details about a task that where the submit failed.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskSubmittedEventDetails`

    Contains details about a submitted task.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **output** *(string) --*

      The response from a resource when a task has started.
    """


_GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "output": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskSucceededEventDetails`

    Contains details about a task that succeeded.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **output** *(string) --*

      The full JSON response from a resource when a task has succeeded. This response becomes
      the output of the related task.
    """


_GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "error": str, "cause": str},
    total=False,
)


class GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef(
    _GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponseevents` `taskTimedOutEventDetails`

    Contains details about a task that timed out.

    - **resourceType** *(string) --*

      The action of the resource called by a task state.

    - **resource** *(string) --*

      The service name of the resource in a task state.

    - **error** *(string) --*

      The error code of the failure.

    - **cause** *(string) --*

      A more detailed explanation of the cause of the failure.
    """


_GetExecutionHistoryPaginateResponseeventsTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseeventsTypeDef",
    {
        "timestamp": datetime,
        "type": str,
        "id": int,
        "previousEventId": int,
        "activityFailedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": GetExecutionHistoryPaginateResponseeventsactivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": GetExecutionHistoryPaginateResponseeventsactivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": GetExecutionHistoryPaginateResponseeventsactivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventsactivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": GetExecutionHistoryPaginateResponseeventstaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": GetExecutionHistoryPaginateResponseeventstaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": GetExecutionHistoryPaginateResponseeventstaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": GetExecutionHistoryPaginateResponseeventstaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": GetExecutionHistoryPaginateResponseeventstaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventstaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventsexecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": GetExecutionHistoryPaginateResponseeventsmapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationStartedEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationSucceededEventDetailsTypeDef,
        "mapIterationFailedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationFailedEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": GetExecutionHistoryPaginateResponseeventsmapIterationAbortedEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": GetExecutionHistoryPaginateResponseeventslambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": GetExecutionHistoryPaginateResponseeventsstateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": GetExecutionHistoryPaginateResponseeventsstateExitedEventDetailsTypeDef,
    },
    total=False,
)


class GetExecutionHistoryPaginateResponseeventsTypeDef(
    _GetExecutionHistoryPaginateResponseeventsTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginateResponse` `events`

    Contains details about the events of an execution.

    - **timestamp** *(datetime) --*

      The date and time the event occurred.

    - **type** *(string) --*

      The type of the event.

    - **id** *(integer) --*

      The id of the event. Events are numbered sequentially, starting at one.

    - **previousEventId** *(integer) --*

      The id of the previous event.

    - **activityFailedEventDetails** *(dict) --*

      Contains details about an activity that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **activityScheduleFailedEventDetails** *(dict) --*

      Contains details about an activity schedule event that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **activityScheduledEventDetails** *(dict) --*

      Contains details about an activity scheduled during an execution.

      - **resource** *(string) --*

        The Amazon Resource Name (ARN) of the scheduled activity.

      - **input** *(string) --*

        The JSON data input to the activity task.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the activity task.

      - **heartbeatInSeconds** *(integer) --*

        The maximum allowed duration between two heartbeats for the activity task.

    - **activityStartedEventDetails** *(dict) --*

      Contains details about the start of an activity during an execution.

      - **workerName** *(string) --*

        The name of the worker that the task is assigned to. These names are provided by the
        workers when calling  GetActivityTask .

    - **activitySucceededEventDetails** *(dict) --*

      Contains details about an activity that successfully terminated during an execution.

      - **output** *(string) --*

        The JSON data output by the activity task.

    - **activityTimedOutEventDetails** *(dict) --*

      Contains details about an activity timeout that occurred during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **taskFailedEventDetails** *(dict) --*

      Contains details about the failure of a task.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskScheduledEventDetails** *(dict) --*

      Contains details about a task that was scheduled.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **region** *(string) --*

        The region of the scheduled task

      - **parameters** *(string) --*

        The JSON data passed to the resource referenced in a task state.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the task.

    - **taskStartFailedEventDetails** *(dict) --*

      Contains details about a task that failed to start.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskStartedEventDetails** *(dict) --*

      Contains details about a task that was started.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

    - **taskSubmitFailedEventDetails** *(dict) --*

      Contains details about a task that where the submit failed.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **taskSubmittedEventDetails** *(dict) --*

      Contains details about a submitted task.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **output** *(string) --*

        The response from a resource when a task has started.

    - **taskSucceededEventDetails** *(dict) --*

      Contains details about a task that succeeded.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **output** *(string) --*

        The full JSON response from a resource when a task has succeeded. This response becomes
        the output of the related task.

    - **taskTimedOutEventDetails** *(dict) --*

      Contains details about a task that timed out.

      - **resourceType** *(string) --*

        The action of the resource called by a task state.

      - **resource** *(string) --*

        The service name of the resource in a task state.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionFailedEventDetails** *(dict) --*

      Contains details about an execution failure event.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionStartedEventDetails** *(dict) --*

      Contains details about the start of the execution.

      - **input** *(string) --*

        The JSON data input to the execution.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.

    - **executionSucceededEventDetails** *(dict) --*

      Contains details about the successful termination of the execution.

      - **output** *(string) --*

        The JSON data output by the execution.

    - **executionAbortedEventDetails** *(dict) --*

      Contains details about an abort of an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **executionTimedOutEventDetails** *(dict) --*

      Contains details about the execution timeout that occurred during the execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **mapStateStartedEventDetails** *(dict) --*

      Contains details about Map state that was started.

      - **length** *(integer) --*

        The size of the array for Map state iterations.

    - **mapIterationStartedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that was started.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationSucceededEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that succeeded.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationFailedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that failed.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **mapIterationAbortedEventDetails** *(dict) --*

      Contains details about an iteration of a Map state that was aborted.

      - **name** *(string) --*

        The name of the iteration’s parent Map state.

      - **index** *(integer) --*

        The index of the array belonging to the Map state iteration.

    - **lambdaFunctionFailedEventDetails** *(dict) --*

      Contains details about a lambda function that failed during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionScheduleFailedEventDetails** *(dict) --*

      Contains details about a failed lambda function schedule event that occurred during an
      execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionScheduledEventDetails** *(dict) --*

      Contains details about a lambda function scheduled during an execution.

      - **resource** *(string) --*

        The Amazon Resource Name (ARN) of the scheduled lambda function.

      - **input** *(string) --*

        The JSON data input to the lambda function.

      - **timeoutInSeconds** *(integer) --*

        The maximum allowed duration of the lambda function.

    - **lambdaFunctionStartFailedEventDetails** *(dict) --*

      Contains details about a lambda function that failed to start during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the failure.

    - **lambdaFunctionSucceededEventDetails** *(dict) --*

      Contains details about a lambda function that terminated successfully during an execution.

      - **output** *(string) --*

        The JSON data output by the lambda function.

    - **lambdaFunctionTimedOutEventDetails** *(dict) --*

      Contains details about a lambda function timeout that occurred during an execution.

      - **error** *(string) --*

        The error code of the failure.

      - **cause** *(string) --*

        A more detailed explanation of the cause of the timeout.

    - **stateEnteredEventDetails** *(dict) --*

      Contains details about a state entered during an execution.

      - **name** *(string) --*

        The name of the state.

      - **input** *(string) --*

        The string that contains the JSON input data for the state.

    - **stateExitedEventDetails** *(dict) --*

      Contains details about an exit from a state during an execution.

      - **name** *(string) --*

        The name of the state.

        A name must *not* contain:

        * white space

        * brackets ``< > { } [ ]``

        * wildcard characters ``? *``

        * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

        * control characters (``U+0000-001F`` , ``U+007F-009F`` )

      - **output** *(string) --*

        The JSON output data of the state.
    """


_GetExecutionHistoryPaginateResponseTypeDef = TypedDict(
    "_GetExecutionHistoryPaginateResponseTypeDef",
    {
        "events": List[GetExecutionHistoryPaginateResponseeventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetExecutionHistoryPaginateResponseTypeDef(
    _GetExecutionHistoryPaginateResponseTypeDef
):
    """
    Type definition for `GetExecutionHistoryPaginate` `Response`

    - **events** *(list) --*

      The list of events that occurred in the execution.

      - *(dict) --*

        Contains details about the events of an execution.

        - **timestamp** *(datetime) --*

          The date and time the event occurred.

        - **type** *(string) --*

          The type of the event.

        - **id** *(integer) --*

          The id of the event. Events are numbered sequentially, starting at one.

        - **previousEventId** *(integer) --*

          The id of the previous event.

        - **activityFailedEventDetails** *(dict) --*

          Contains details about an activity that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **activityScheduleFailedEventDetails** *(dict) --*

          Contains details about an activity schedule event that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **activityScheduledEventDetails** *(dict) --*

          Contains details about an activity scheduled during an execution.

          - **resource** *(string) --*

            The Amazon Resource Name (ARN) of the scheduled activity.

          - **input** *(string) --*

            The JSON data input to the activity task.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the activity task.

          - **heartbeatInSeconds** *(integer) --*

            The maximum allowed duration between two heartbeats for the activity task.

        - **activityStartedEventDetails** *(dict) --*

          Contains details about the start of an activity during an execution.

          - **workerName** *(string) --*

            The name of the worker that the task is assigned to. These names are provided by the
            workers when calling  GetActivityTask .

        - **activitySucceededEventDetails** *(dict) --*

          Contains details about an activity that successfully terminated during an execution.

          - **output** *(string) --*

            The JSON data output by the activity task.

        - **activityTimedOutEventDetails** *(dict) --*

          Contains details about an activity timeout that occurred during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **taskFailedEventDetails** *(dict) --*

          Contains details about the failure of a task.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskScheduledEventDetails** *(dict) --*

          Contains details about a task that was scheduled.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **region** *(string) --*

            The region of the scheduled task

          - **parameters** *(string) --*

            The JSON data passed to the resource referenced in a task state.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the task.

        - **taskStartFailedEventDetails** *(dict) --*

          Contains details about a task that failed to start.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskStartedEventDetails** *(dict) --*

          Contains details about a task that was started.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

        - **taskSubmitFailedEventDetails** *(dict) --*

          Contains details about a task that where the submit failed.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **taskSubmittedEventDetails** *(dict) --*

          Contains details about a submitted task.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **output** *(string) --*

            The response from a resource when a task has started.

        - **taskSucceededEventDetails** *(dict) --*

          Contains details about a task that succeeded.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **output** *(string) --*

            The full JSON response from a resource when a task has succeeded. This response becomes
            the output of the related task.

        - **taskTimedOutEventDetails** *(dict) --*

          Contains details about a task that timed out.

          - **resourceType** *(string) --*

            The action of the resource called by a task state.

          - **resource** *(string) --*

            The service name of the resource in a task state.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionFailedEventDetails** *(dict) --*

          Contains details about an execution failure event.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionStartedEventDetails** *(dict) --*

          Contains details about the start of the execution.

          - **input** *(string) --*

            The JSON data input to the execution.

          - **roleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.

        - **executionSucceededEventDetails** *(dict) --*

          Contains details about the successful termination of the execution.

          - **output** *(string) --*

            The JSON data output by the execution.

        - **executionAbortedEventDetails** *(dict) --*

          Contains details about an abort of an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **executionTimedOutEventDetails** *(dict) --*

          Contains details about the execution timeout that occurred during the execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **mapStateStartedEventDetails** *(dict) --*

          Contains details about Map state that was started.

          - **length** *(integer) --*

            The size of the array for Map state iterations.

        - **mapIterationStartedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that was started.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationSucceededEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that succeeded.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationFailedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that failed.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **mapIterationAbortedEventDetails** *(dict) --*

          Contains details about an iteration of a Map state that was aborted.

          - **name** *(string) --*

            The name of the iteration’s parent Map state.

          - **index** *(integer) --*

            The index of the array belonging to the Map state iteration.

        - **lambdaFunctionFailedEventDetails** *(dict) --*

          Contains details about a lambda function that failed during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionScheduleFailedEventDetails** *(dict) --*

          Contains details about a failed lambda function schedule event that occurred during an
          execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionScheduledEventDetails** *(dict) --*

          Contains details about a lambda function scheduled during an execution.

          - **resource** *(string) --*

            The Amazon Resource Name (ARN) of the scheduled lambda function.

          - **input** *(string) --*

            The JSON data input to the lambda function.

          - **timeoutInSeconds** *(integer) --*

            The maximum allowed duration of the lambda function.

        - **lambdaFunctionStartFailedEventDetails** *(dict) --*

          Contains details about a lambda function that failed to start during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the failure.

        - **lambdaFunctionSucceededEventDetails** *(dict) --*

          Contains details about a lambda function that terminated successfully during an execution.

          - **output** *(string) --*

            The JSON data output by the lambda function.

        - **lambdaFunctionTimedOutEventDetails** *(dict) --*

          Contains details about a lambda function timeout that occurred during an execution.

          - **error** *(string) --*

            The error code of the failure.

          - **cause** *(string) --*

            A more detailed explanation of the cause of the timeout.

        - **stateEnteredEventDetails** *(dict) --*

          Contains details about a state entered during an execution.

          - **name** *(string) --*

            The name of the state.

          - **input** *(string) --*

            The string that contains the JSON input data for the state.

        - **stateExitedEventDetails** *(dict) --*

          Contains details about an exit from a state during an execution.

          - **name** *(string) --*

            The name of the state.

            A name must *not* contain:

            * white space

            * brackets ``< > { } [ ]``

            * wildcard characters ``? *``

            * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

            * control characters (``U+0000-001F`` , ``U+007F-009F`` )

          - **output** *(string) --*

            The JSON output data of the state.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActivitiesPaginatePaginationConfigTypeDef(
    _ListActivitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListActivitiesPaginate` `PaginationConfig`

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


_ListActivitiesPaginateResponseactivitiesTypeDef = TypedDict(
    "_ListActivitiesPaginateResponseactivitiesTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ListActivitiesPaginateResponseactivitiesTypeDef(
    _ListActivitiesPaginateResponseactivitiesTypeDef
):
    """
    Type definition for `ListActivitiesPaginateResponse` `activities`

    Contains details about an activity.

    - **activityArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the activity.

    - **name** *(string) --*

      The name of the activity.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **creationDate** *(datetime) --*

      The date the activity is created.
    """


_ListActivitiesPaginateResponseTypeDef = TypedDict(
    "_ListActivitiesPaginateResponseTypeDef",
    {
        "activities": List[ListActivitiesPaginateResponseactivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListActivitiesPaginateResponseTypeDef(_ListActivitiesPaginateResponseTypeDef):
    """
    Type definition for `ListActivitiesPaginate` `Response`

    - **activities** *(list) --*

      The list of activities.

      - *(dict) --*

        Contains details about an activity.

        - **activityArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the activity.

        - **name** *(string) --*

          The name of the activity.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **creationDate** *(datetime) --*

          The date the activity is created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListExecutionsPaginatePaginationConfigTypeDef(
    _ListExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListExecutionsPaginate` `PaginationConfig`

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


_ListExecutionsPaginateResponseexecutionsTypeDef = TypedDict(
    "_ListExecutionsPaginateResponseexecutionsTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": str,
        "startDate": datetime,
        "stopDate": datetime,
    },
    total=False,
)


class ListExecutionsPaginateResponseexecutionsTypeDef(
    _ListExecutionsPaginateResponseexecutionsTypeDef
):
    """
    Type definition for `ListExecutionsPaginateResponse` `executions`

    Contains details about an execution.

    - **executionArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the execution.

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) of the executed state machine.

    - **name** *(string) --*

      The name of the execution.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **status** *(string) --*

      The current status of the execution.

    - **startDate** *(datetime) --*

      The date the execution started.

    - **stopDate** *(datetime) --*

      If the execution already ended, the date the execution stopped.
    """


_ListExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListExecutionsPaginateResponseTypeDef",
    {
        "executions": List[ListExecutionsPaginateResponseexecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListExecutionsPaginateResponseTypeDef(_ListExecutionsPaginateResponseTypeDef):
    """
    Type definition for `ListExecutionsPaginate` `Response`

    - **executions** *(list) --*

      The list of matching executions.

      - *(dict) --*

        Contains details about an execution.

        - **executionArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the execution.

        - **stateMachineArn** *(string) --*

          The Amazon Resource Name (ARN) of the executed state machine.

        - **name** *(string) --*

          The name of the execution.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **status** *(string) --*

          The current status of the execution.

        - **startDate** *(datetime) --*

          The date the execution started.

        - **stopDate** *(datetime) --*

          If the execution already ended, the date the execution stopped.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListStateMachinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStateMachinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStateMachinesPaginatePaginationConfigTypeDef(
    _ListStateMachinesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStateMachinesPaginate` `PaginationConfig`

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


_ListStateMachinesPaginateResponsestateMachinesTypeDef = TypedDict(
    "_ListStateMachinesPaginateResponsestateMachinesTypeDef",
    {"stateMachineArn": str, "name": str, "creationDate": datetime},
    total=False,
)


class ListStateMachinesPaginateResponsestateMachinesTypeDef(
    _ListStateMachinesPaginateResponsestateMachinesTypeDef
):
    """
    Type definition for `ListStateMachinesPaginateResponse` `stateMachines`

    Contains details about the state machine.

    - **stateMachineArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the state machine.

    - **name** *(string) --*

      The name of the state machine.

      A name must *not* contain:

      * white space

      * brackets ``< > { } [ ]``

      * wildcard characters ``? *``

      * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

      * control characters (``U+0000-001F`` , ``U+007F-009F`` )

    - **creationDate** *(datetime) --*

      The date the state machine is created.
    """


_ListStateMachinesPaginateResponseTypeDef = TypedDict(
    "_ListStateMachinesPaginateResponseTypeDef",
    {
        "stateMachines": List[ListStateMachinesPaginateResponsestateMachinesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListStateMachinesPaginateResponseTypeDef(
    _ListStateMachinesPaginateResponseTypeDef
):
    """
    Type definition for `ListStateMachinesPaginate` `Response`

    - **stateMachines** *(list) --*

      - *(dict) --*

        Contains details about the state machine.

        - **stateMachineArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the state machine.

        - **name** *(string) --*

          The name of the state machine.

          A name must *not* contain:

          * white space

          * brackets ``< > { } [ ]``

          * wildcard characters ``? *``

          * special characters ``" # % \\ ^ | ~ ` $ & , ; : /``

          * control characters (``U+0000-001F`` , ``U+007F-009F`` )

        - **creationDate** *(datetime) --*

          The date the state machine is created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
