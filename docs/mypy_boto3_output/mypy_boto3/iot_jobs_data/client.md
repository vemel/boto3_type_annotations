# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot_jobs_data.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot Jobs Data](index.md#iot-jobs-data) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_job_execution](#clientdescribe_job_execution)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_pending_job_executions](#clientget_pending_job_executions)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().start_next_pending_job_execution](#clientstart_next_pending_job_execution)
        - [Client().update_job_execution](#clientupdate_job_execution)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L18)

```python
def describe_job_execution(
    jobId: str,
    thingName: str,
    includeJobDocument: bool = None,
    executionNumber: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L28)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L38)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_pending_job_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L42)

```python
def get_pending_job_executions(thingName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L46)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().start_next_pending_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L50)

```python
def start_next_pending_job_execution(
    thingName: str,
    statusDetails: Dict[str, Any] = None,
    stepTimeoutInMinutes: int = None,
) -> Dict[str, Any]:
```

### Client().update_job_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_jobs_data/client.py#L59)

```python
def update_job_execution(
    jobId: str,
    thingName: str,
    status: str,
    statusDetails: Dict[str, Any] = None,
    stepTimeoutInMinutes: int = None,
    expectedVersion: int = None,
    includeJobExecutionState: bool = None,
    includeJobDocument: bool = None,
    executionNumber: int = None,
) -> Dict[str, Any]:
```
