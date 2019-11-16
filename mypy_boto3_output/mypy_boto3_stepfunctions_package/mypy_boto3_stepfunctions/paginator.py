"Main interface for stepfunctions Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_stepfunctions.type_defs import (
    GetExecutionHistoryPaginatePaginationConfigTypeDef,
    GetExecutionHistoryPaginateResponseTypeDef,
    ListActivitiesPaginatePaginationConfigTypeDef,
    ListActivitiesPaginateResponseTypeDef,
    ListExecutionsPaginatePaginationConfigTypeDef,
    ListExecutionsPaginateResponseTypeDef,
    ListStateMachinesPaginatePaginationConfigTypeDef,
    ListStateMachinesPaginateResponseTypeDef,
)


__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
)


class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_execution_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        PaginationConfig: GetExecutionHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetExecutionHistoryPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SFN.Client.get_execution_history`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/GetExecutionHistory>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              executionArn='string',
              reverseOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type executionArn: string
        :param executionArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the execution.

        :type reverseOrder: boolean
        :param reverseOrder:

          Lists events in descending order of their ``timeStamp`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'events': [
                    {
                        'timestamp': datetime(2015, 1, 1),
                        'type':
                        'ActivityFailed'|'ActivityScheduled'|'ActivityScheduleFailed'|'ActivityStarted'
                        |'ActivitySucceeded'|'ActivityTimedOut'|'ChoiceStateEntered'|'ChoiceStateExited'
                        |'ExecutionAborted'|'ExecutionFailed'|'ExecutionStarted'|'ExecutionSucceeded'
                        |'ExecutionTimedOut'|'FailStateEntered'|'LambdaFunctionFailed'
                        |'LambdaFunctionScheduled'|'LambdaFunctionScheduleFailed'|'LambdaFunctionStarted'
                        |'LambdaFunctionStartFailed'|'LambdaFunctionSucceeded'|'LambdaFunctionTimedOut'
                        |'MapIterationAborted'|'MapIterationFailed'|'MapIterationStarted'
                        |'MapIterationSucceeded'|'MapStateAborted'|'MapStateEntered'|'MapStateExited'
                        |'MapStateFailed'|'MapStateStarted'|'MapStateSucceeded'|'ParallelStateAborted'
                        |'ParallelStateEntered'|'ParallelStateExited'|'ParallelStateFailed'
                        |'ParallelStateStarted'|'ParallelStateSucceeded'|'PassStateEntered'
                        |'PassStateExited'|'SucceedStateEntered'|'SucceedStateExited'|'TaskFailed'
                        |'TaskScheduled'|'TaskStarted'|'TaskStartFailed'|'TaskStateAborted'
                        |'TaskStateEntered'|'TaskStateExited'|'TaskSubmitFailed'|'TaskSubmitted'
                        |'TaskSucceeded'|'TaskTimedOut'|'WaitStateAborted'|'WaitStateEntered'
                        |'WaitStateExited',
                        'id': 123,
                        'previousEventId': 123,
                        'activityFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'activityScheduleFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'activityScheduledEventDetails': {
                            'resource': 'string',
                            'input': 'string',
                            'timeoutInSeconds': 123,
                            'heartbeatInSeconds': 123
                        },
                        'activityStartedEventDetails': {
                            'workerName': 'string'
                        },
                        'activitySucceededEventDetails': {
                            'output': 'string'
                        },
                        'activityTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskScheduledEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'region': 'string',
                            'parameters': 'string',
                            'timeoutInSeconds': 123
                        },
                        'taskStartFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskStartedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string'
                        },
                        'taskSubmitFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskSubmittedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'output': 'string'
                        },
                        'taskSucceededEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'output': 'string'
                        },
                        'taskTimedOutEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionStartedEventDetails': {
                            'input': 'string',
                            'roleArn': 'string'
                        },
                        'executionSucceededEventDetails': {
                            'output': 'string'
                        },
                        'executionAbortedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'mapStateStartedEventDetails': {
                            'length': 123
                        },
                        'mapIterationStartedEventDetails': {
                            'name': 'string',
                            'index': 123
                        },
                        'mapIterationSucceededEventDetails': {
                            'name': 'string',
                            'index': 123
                        },
                        'mapIterationFailedEventDetails': {
                            'name': 'string',
                            'index': 123
                        },
                        'mapIterationAbortedEventDetails': {
                            'name': 'string',
                            'index': 123
                        },
                        'lambdaFunctionFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionScheduleFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionScheduledEventDetails': {
                            'resource': 'string',
                            'input': 'string',
                            'timeoutInSeconds': 123
                        },
                        'lambdaFunctionStartFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionSucceededEventDetails': {
                            'output': 'string'
                        },
                        'lambdaFunctionTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'stateEnteredEventDetails': {
                            'name': 'string',
                            'input': 'string'
                        },
                        'stateExitedEventDetails': {
                            'name': 'string',
                            'output': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListActivitiesPaginator(Boto3Paginator):
    """
    Paginator for `list_activities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListActivitiesPaginatePaginationConfigTypeDef = None
    ) -> ListActivitiesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SFN.Client.list_activities`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListActivities>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'activities': [
                    {
                        'activityArn': 'string',
                        'name': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: str = None,
        PaginationConfig: ListExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListExecutionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SFN.Client.list_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              stateMachineArn='string',
              statusFilter='RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the state machine whose executions is listed.

        :type statusFilter: string
        :param statusFilter:

          If specified, only list the executions whose current execution status matches the given filter.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'executions': [
                    {
                        'executionArn': 'string',
                        'stateMachineArn': 'string',
                        'name': 'string',
                        'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
                        'startDate': datetime(2015, 1, 1),
                        'stopDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListStateMachinesPaginator(Boto3Paginator):
    """
    Paginator for `list_state_machines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStateMachinesPaginatePaginationConfigTypeDef = None
    ) -> ListStateMachinesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SFN.Client.list_state_machines`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListStateMachines>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'stateMachines': [
                    {
                        'stateMachineArn': 'string',
                        'name': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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
