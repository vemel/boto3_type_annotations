"Main interface for iot-jobs-data type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    "ClientDescribeJobExecutionResponseTypeDef",
    "ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    "ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    "ClientGetPendingJobExecutionsResponseTypeDef",
    "ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    "ClientStartNextPendingJobExecutionResponseTypeDef",
    "ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    "ClientUpdateJobExecutionResponseTypeDef",
)


_ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": str,
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionTypeDef(
    _ClientDescribeJobExecutionResponseexecutionTypeDef
):
    """
    Type definition for `ClientDescribeJobExecutionResponse` `execution`

    Contains data about a job execution.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **thingName** *(string) --*

      The name of the thing that is executing the job.

    - **status** *(string) --*

      The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
      "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

    - **statusDetails** *(dict) --*

      A collection of name/value pairs that describe the status of the job execution.

      - *(string) --*

        - *(string) --*

    - **queuedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was enqueued.

    - **startedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was started.

    - **lastUpdatedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was last updated.

    - **approximateSecondsBeforeTimedOut** *(integer) --*

      The estimated number of seconds that remain before the job execution status will be changed
      to ``TIMED_OUT`` .

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time they are
      updated by a device.

    - **executionNumber** *(integer) --*

      A number that identifies a particular job execution on a particular device. It can be used
      later in commands that return or update job execution information.

    - **jobDocument** *(string) --*

      The content of the job document.
    """


_ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientDescribeJobExecutionResponseTypeDef(
    _ClientDescribeJobExecutionResponseTypeDef
):
    """
    Type definition for `ClientDescribeJobExecution` `Response`

    - **execution** *(dict) --*

      Contains data about a job execution.

      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.

      - **thingName** *(string) --*

        The name of the thing that is executing the job.

      - **status** *(string) --*

        The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
        "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

      - **statusDetails** *(dict) --*

        A collection of name/value pairs that describe the status of the job execution.

        - *(string) --*

          - *(string) --*

      - **queuedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was enqueued.

      - **startedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was started.

      - **lastUpdatedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was last updated.

      - **approximateSecondsBeforeTimedOut** *(integer) --*

        The estimated number of seconds that remain before the job execution status will be changed
        to ``TIMED_OUT`` .

      - **versionNumber** *(integer) --*

        The version of the job execution. Job execution versions are incremented each time they are
        updated by a device.

      - **executionNumber** *(integer) --*

        A number that identifies a particular job execution on a particular device. It can be used
        later in commands that return or update job execution information.

      - **jobDocument** *(string) --*

        The content of the job document.
    """


_ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef(
    _ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef
):
    """
    Type definition for `ClientGetPendingJobExecutionsResponse` `inProgressJobs`

    Contains a subset of information about a job execution.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **queuedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was enqueued.

    - **startedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was last updated.

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time AWS
      IoT Jobs receives an update from a device.

    - **executionNumber** *(integer) --*

      A number that identifies a particular job execution on a particular device.
    """


_ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef(
    _ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef
):
    """
    Type definition for `ClientGetPendingJobExecutionsResponse` `queuedJobs`

    Contains a subset of information about a job execution.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **queuedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was enqueued.

    - **startedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was last updated.

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time AWS
      IoT Jobs receives an update from a device.

    - **executionNumber** *(integer) --*

      A number that identifies a particular job execution on a particular device.
    """


_ClientGetPendingJobExecutionsResponseTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List[
            ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef
        ],
        "queuedJobs": List[ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef],
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponseTypeDef(
    _ClientGetPendingJobExecutionsResponseTypeDef
):
    """
    Type definition for `ClientGetPendingJobExecutions` `Response`

    - **inProgressJobs** *(list) --*

      A list of JobExecutionSummary objects with status IN_PROGRESS.

      - *(dict) --*

        Contains a subset of information about a job execution.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **queuedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution was enqueued.

        - **startedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution started.

        - **lastUpdatedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution was last updated.

        - **versionNumber** *(integer) --*

          The version of the job execution. Job execution versions are incremented each time AWS
          IoT Jobs receives an update from a device.

        - **executionNumber** *(integer) --*

          A number that identifies a particular job execution on a particular device.

    - **queuedJobs** *(list) --*

      A list of JobExecutionSummary objects with status QUEUED.

      - *(dict) --*

        Contains a subset of information about a job execution.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **queuedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution was enqueued.

        - **startedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution started.

        - **lastUpdatedAt** *(integer) --*

          The time, in milliseconds since the epoch, when the job execution was last updated.

        - **versionNumber** *(integer) --*

          The version of the job execution. Job execution versions are incremented each time AWS
          IoT Jobs receives an update from a device.

        - **executionNumber** *(integer) --*

          A number that identifies a particular job execution on a particular device.
    """


_ClientStartNextPendingJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": str,
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)


class ClientStartNextPendingJobExecutionResponseexecutionTypeDef(
    _ClientStartNextPendingJobExecutionResponseexecutionTypeDef
):
    """
    Type definition for `ClientStartNextPendingJobExecutionResponse` `execution`

    A JobExecution object.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **thingName** *(string) --*

      The name of the thing that is executing the job.

    - **status** *(string) --*

      The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
      "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

    - **statusDetails** *(dict) --*

      A collection of name/value pairs that describe the status of the job execution.

      - *(string) --*

        - *(string) --*

    - **queuedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was enqueued.

    - **startedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was started.

    - **lastUpdatedAt** *(integer) --*

      The time, in milliseconds since the epoch, when the job execution was last updated.

    - **approximateSecondsBeforeTimedOut** *(integer) --*

      The estimated number of seconds that remain before the job execution status will be changed
      to ``TIMED_OUT`` .

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time they are
      updated by a device.

    - **executionNumber** *(integer) --*

      A number that identifies a particular job execution on a particular device. It can be used
      later in commands that return or update job execution information.

    - **jobDocument** *(string) --*

      The content of the job document.
    """


_ClientStartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "_ClientStartNextPendingJobExecutionResponseTypeDef",
    {"execution": ClientStartNextPendingJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientStartNextPendingJobExecutionResponseTypeDef(
    _ClientStartNextPendingJobExecutionResponseTypeDef
):
    """
    Type definition for `ClientStartNextPendingJobExecution` `Response`

    - **execution** *(dict) --*

      A JobExecution object.

      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.

      - **thingName** *(string) --*

        The name of the thing that is executing the job.

      - **status** *(string) --*

        The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
        "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

      - **statusDetails** *(dict) --*

        A collection of name/value pairs that describe the status of the job execution.

        - *(string) --*

          - *(string) --*

      - **queuedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was enqueued.

      - **startedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was started.

      - **lastUpdatedAt** *(integer) --*

        The time, in milliseconds since the epoch, when the job execution was last updated.

      - **approximateSecondsBeforeTimedOut** *(integer) --*

        The estimated number of seconds that remain before the job execution status will be changed
        to ``TIMED_OUT`` .

      - **versionNumber** *(integer) --*

        The version of the job execution. Job execution versions are incremented each time they are
        updated by a device.

      - **executionNumber** *(integer) --*

        A number that identifies a particular job execution on a particular device. It can be used
        later in commands that return or update job execution information.

      - **jobDocument** *(string) --*

        The content of the job document.
    """


_ClientUpdateJobExecutionResponseexecutionStateTypeDef = TypedDict(
    "_ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    {"status": str, "statusDetails": Dict[str, str], "versionNumber": int},
    total=False,
)


class ClientUpdateJobExecutionResponseexecutionStateTypeDef(
    _ClientUpdateJobExecutionResponseexecutionStateTypeDef
):
    """
    Type definition for `ClientUpdateJobExecutionResponse` `executionState`

    A JobExecutionState object.

    - **status** *(string) --*

      The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
      "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

    - **statusDetails** *(dict) --*

      A collection of name/value pairs that describe the status of the job execution.

      - *(string) --*

        - *(string) --*

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time they are
      updated by a device.
    """


_ClientUpdateJobExecutionResponseTypeDef = TypedDict(
    "_ClientUpdateJobExecutionResponseTypeDef",
    {
        "executionState": ClientUpdateJobExecutionResponseexecutionStateTypeDef,
        "jobDocument": str,
    },
    total=False,
)


class ClientUpdateJobExecutionResponseTypeDef(_ClientUpdateJobExecutionResponseTypeDef):
    """
    Type definition for `ClientUpdateJobExecution` `Response`

    - **executionState** *(dict) --*

      A JobExecutionState object.

      - **status** *(string) --*

        The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
        "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

      - **statusDetails** *(dict) --*

        A collection of name/value pairs that describe the status of the job execution.

        - *(string) --*

          - *(string) --*

      - **versionNumber** *(integer) --*

        The version of the job execution. Job execution versions are incremented each time they are
        updated by a device.

    - **jobDocument** *(string) --*

      The contents of the Job Documents.
    """
