# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.stepfunctions.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Stepfunctions](index.md#stepfunctions) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_activity](#clientcreate_activity)
        - [Client().create_state_machine](#clientcreate_state_machine)
        - [Client().delete_activity](#clientdelete_activity)
        - [Client().delete_state_machine](#clientdelete_state_machine)
        - [Client().describe_activity](#clientdescribe_activity)
        - [Client().describe_execution](#clientdescribe_execution)
        - [Client().describe_state_machine](#clientdescribe_state_machine)
        - [Client().describe_state_machine_for_execution](#clientdescribe_state_machine_for_execution)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_activity_task](#clientget_activity_task)
        - [Client().get_execution_history](#clientget_execution_history)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_activities](#clientlist_activities)
        - [Client().list_executions](#clientlist_executions)
        - [Client().list_state_machines](#clientlist_state_machines)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().send_task_failure](#clientsend_task_failure)
        - [Client().send_task_heartbeat](#clientsend_task_heartbeat)
        - [Client().send_task_success](#clientsend_task_success)
        - [Client().start_execution](#clientstart_execution)
        - [Client().stop_execution](#clientstop_execution)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_state_machine](#clientupdate_state_machine)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_activity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L19)

```python
def create_activity(name: str, tags: List[Any] = None) -> Dict[str, Any]:
```

### Client().create_state_machine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L23)

```python
def create_state_machine(
    name: str,
    definition: str,
    roleArn: str,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_activity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L29)

```python
def delete_activity(activityArn: str) -> Dict[str, Any]:
```

### Client().delete_state_machine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L33)

```python
def delete_state_machine(stateMachineArn: str) -> Dict[str, Any]:
```

### Client().describe_activity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L37)

```python
def describe_activity(activityArn: str) -> Dict[str, Any]:
```

### Client().describe_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L41)

```python
def describe_execution(executionArn: str) -> Dict[str, Any]:
```

### Client().describe_state_machine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L45)

```python
def describe_state_machine(stateMachineArn: str) -> Dict[str, Any]:
```

### Client().describe_state_machine_for_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L49)

```python
def describe_state_machine_for_execution(executionArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L53)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_activity_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L63)

```python
def get_activity_task(
    activityArn: str,
    workerName: str = None,
) -> Dict[str, Any]:
```

### Client().get_execution_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L69)

```python
def get_execution_history(
    executionArn: str,
    maxResults: int = None,
    reverseOrder: bool = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L79)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L83)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_activities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L87)

```python
def list_activities(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L93)

```python
def list_executions(
    stateMachineArn: str,
    statusFilter: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_state_machines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L103)

```python
def list_state_machines(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L109)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().send_task_failure

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L113)

```python
def send_task_failure(
    taskToken: str,
    error: str = None,
    cause: str = None,
) -> Dict[str, Any]:
```

### Client().send_task_heartbeat

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L119)

```python
def send_task_heartbeat(taskToken: str) -> Dict[str, Any]:
```

### Client().send_task_success

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L123)

```python
def send_task_success(taskToken: str, output: str) -> Dict[str, Any]:
```

### Client().start_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L127)

```python
def start_execution(
    stateMachineArn: str,
    name: str = None,
    input: str = None,
) -> Dict[str, Any]:
```

### Client().stop_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L133)

```python
def stop_execution(
    executionArn: str,
    error: str = None,
    cause: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L139)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L143)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_state_machine

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/client.py#L147)

```python
def update_state_machine(
    stateMachineArn: str,
    definition: str = None,
    roleArn: str = None,
) -> Dict[str, Any]:
```
