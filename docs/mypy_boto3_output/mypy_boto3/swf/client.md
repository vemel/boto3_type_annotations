# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.swf.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Swf](index.md#swf) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().count_closed_workflow_executions](#clientcount_closed_workflow_executions)
        - [Client().count_open_workflow_executions](#clientcount_open_workflow_executions)
        - [Client().count_pending_activity_tasks](#clientcount_pending_activity_tasks)
        - [Client().count_pending_decision_tasks](#clientcount_pending_decision_tasks)
        - [Client().deprecate_activity_type](#clientdeprecate_activity_type)
        - [Client().deprecate_domain](#clientdeprecate_domain)
        - [Client().deprecate_workflow_type](#clientdeprecate_workflow_type)
        - [Client().describe_activity_type](#clientdescribe_activity_type)
        - [Client().describe_domain](#clientdescribe_domain)
        - [Client().describe_workflow_execution](#clientdescribe_workflow_execution)
        - [Client().describe_workflow_type](#clientdescribe_workflow_type)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().get_workflow_execution_history](#clientget_workflow_execution_history)
        - [Client().list_activity_types](#clientlist_activity_types)
        - [Client().list_closed_workflow_executions](#clientlist_closed_workflow_executions)
        - [Client().list_domains](#clientlist_domains)
        - [Client().list_open_workflow_executions](#clientlist_open_workflow_executions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_workflow_types](#clientlist_workflow_types)
        - [Client().poll_for_activity_task](#clientpoll_for_activity_task)
        - [Client().poll_for_decision_task](#clientpoll_for_decision_task)
        - [Client().record_activity_task_heartbeat](#clientrecord_activity_task_heartbeat)
        - [Client().register_activity_type](#clientregister_activity_type)
        - [Client().register_domain](#clientregister_domain)
        - [Client().register_workflow_type](#clientregister_workflow_type)
        - [Client().request_cancel_workflow_execution](#clientrequest_cancel_workflow_execution)
        - [Client().respond_activity_task_canceled](#clientrespond_activity_task_canceled)
        - [Client().respond_activity_task_completed](#clientrespond_activity_task_completed)
        - [Client().respond_activity_task_failed](#clientrespond_activity_task_failed)
        - [Client().respond_decision_task_completed](#clientrespond_decision_task_completed)
        - [Client().signal_workflow_execution](#clientsignal_workflow_execution)
        - [Client().start_workflow_execution](#clientstart_workflow_execution)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().terminate_workflow_execution](#clientterminate_workflow_execution)
        - [Client().undeprecate_activity_type](#clientundeprecate_activity_type)
        - [Client().undeprecate_domain](#clientundeprecate_domain)
        - [Client().undeprecate_workflow_type](#clientundeprecate_workflow_type)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().count_closed_workflow_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L19)

```python
def count_closed_workflow_executions(
    domain: str,
    startTimeFilter: Dict[str, Any] = None,
    closeTimeFilter: Dict[str, Any] = None,
    executionFilter: Dict[str, Any] = None,
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    closeStatusFilter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().count_open_workflow_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L32)

```python
def count_open_workflow_executions(
    domain: str,
    startTimeFilter: Dict[str, Any],
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    executionFilter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().count_pending_activity_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L43)

```python
def count_pending_activity_tasks(
    domain: str,
    taskList: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().count_pending_decision_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L49)

```python
def count_pending_decision_tasks(
    domain: str,
    taskList: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().deprecate_activity_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L55)

```python
def deprecate_activity_type(
    domain: str,
    activityType: Dict[str, Any],
) -> None:
```

### Client().deprecate_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L61)

```python
def deprecate_domain(name: str) -> None:
```

### Client().deprecate_workflow_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L65)

```python
def deprecate_workflow_type(
    domain: str,
    workflowType: Dict[str, Any],
) -> None:
```

### Client().describe_activity_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L71)

```python
def describe_activity_type(
    domain: str,
    activityType: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().describe_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L77)

```python
def describe_domain(name: str) -> Dict[str, Any]:
```

### Client().describe_workflow_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L81)

```python
def describe_workflow_execution(
    domain: str,
    execution: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().describe_workflow_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L87)

```python
def describe_workflow_type(
    domain: str,
    workflowType: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L93)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L103)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L107)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().get_workflow_execution_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L111)

```python
def get_workflow_execution_history(
    domain: str,
    execution: Dict[str, Any],
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_activity_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L122)

```python
def list_activity_types(
    domain: str,
    registrationStatus: str,
    name: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_closed_workflow_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L134)

```python
def list_closed_workflow_executions(
    domain: str,
    startTimeFilter: Dict[str, Any] = None,
    closeTimeFilter: Dict[str, Any] = None,
    executionFilter: Dict[str, Any] = None,
    closeStatusFilter: Dict[str, Any] = None,
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L150)

```python
def list_domains(
    registrationStatus: str,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().list_open_workflow_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L160)

```python
def list_open_workflow_executions(
    domain: str,
    startTimeFilter: Dict[str, Any],
    typeFilter: Dict[str, Any] = None,
    tagFilter: Dict[str, Any] = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
    executionFilter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L174)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().list_workflow_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L178)

```python
def list_workflow_types(
    domain: str,
    registrationStatus: str,
    name: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().poll_for_activity_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L190)

```python
def poll_for_activity_task(
    domain: str,
    taskList: Dict[str, Any],
    identity: str = None,
) -> Dict[str, Any]:
```

### Client().poll_for_decision_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L196)

```python
def poll_for_decision_task(
    domain: str,
    taskList: Dict[str, Any],
    identity: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().record_activity_task_heartbeat

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L208)

```python
def record_activity_task_heartbeat(
    taskToken: str,
    details: str = None,
) -> Dict[str, Any]:
```

### Client().register_activity_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L214)

```python
def register_activity_type(
    domain: str,
    name: str,
    version: str,
    description: str = None,
    defaultTaskStartToCloseTimeout: str = None,
    defaultTaskHeartbeatTimeout: str = None,
    defaultTaskList: Dict[str, Any] = None,
    defaultTaskPriority: str = None,
    defaultTaskScheduleToStartTimeout: str = None,
    defaultTaskScheduleToCloseTimeout: str = None,
) -> None:
```

### Client().register_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L230)

```python
def register_domain(
    name: str,
    workflowExecutionRetentionPeriodInDays: str,
    description: str = None,
    tags: List[Any] = None,
) -> None:
```

### Client().register_workflow_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L240)

```python
def register_workflow_type(
    domain: str,
    name: str,
    version: str,
    description: str = None,
    defaultTaskStartToCloseTimeout: str = None,
    defaultExecutionStartToCloseTimeout: str = None,
    defaultTaskList: Dict[str, Any] = None,
    defaultTaskPriority: str = None,
    defaultChildPolicy: str = None,
    defaultLambdaRole: str = None,
) -> None:
```

### Client().request_cancel_workflow_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L256)

```python
def request_cancel_workflow_execution(
    domain: str,
    workflowId: str,
    runId: str = None,
) -> None:
```

### Client().respond_activity_task_canceled

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L262)

```python
def respond_activity_task_canceled(
    taskToken: str,
    details: str = None,
) -> None:
```

### Client().respond_activity_task_completed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L268)

```python
def respond_activity_task_completed(
    taskToken: str,
    result: str = None,
) -> None:
```

### Client().respond_activity_task_failed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L274)

```python
def respond_activity_task_failed(
    taskToken: str,
    reason: str = None,
    details: str = None,
) -> None:
```

### Client().respond_decision_task_completed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L280)

```python
def respond_decision_task_completed(
    taskToken: str,
    decisions: List[Any] = None,
    executionContext: str = None,
) -> None:
```

### Client().signal_workflow_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L286)

```python
def signal_workflow_execution(
    domain: str,
    workflowId: str,
    signalName: str,
    runId: str = None,
    input: str = None,
) -> None:
```

### Client().start_workflow_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L297)

```python
def start_workflow_execution(
    domain: str,
    workflowId: str,
    workflowType: Dict[str, Any],
    taskList: Dict[str, Any] = None,
    taskPriority: str = None,
    input: str = None,
    executionStartToCloseTimeout: str = None,
    tagList: List[Any] = None,
    taskStartToCloseTimeout: str = None,
    childPolicy: str = None,
    lambdaRole: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L314)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> None:
```

### Client().terminate_workflow_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L318)

```python
def terminate_workflow_execution(
    domain: str,
    workflowId: str,
    runId: str = None,
    reason: str = None,
    details: str = None,
    childPolicy: str = None,
) -> None:
```

### Client().undeprecate_activity_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L330)

```python
def undeprecate_activity_type(
    domain: str,
    activityType: Dict[str, Any],
) -> None:
```

### Client().undeprecate_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L336)

```python
def undeprecate_domain(name: str) -> None:
```

### Client().undeprecate_workflow_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L340)

```python
def undeprecate_workflow_type(
    domain: str,
    workflowType: Dict[str, Any],
) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/swf/client.py#L346)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> None:
```
