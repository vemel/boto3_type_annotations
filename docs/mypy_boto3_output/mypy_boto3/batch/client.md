# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.batch.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Batch](index.md#batch) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().create_compute_environment](#clientcreate_compute_environment)
        - [Client().create_job_queue](#clientcreate_job_queue)
        - [Client().delete_compute_environment](#clientdelete_compute_environment)
        - [Client().delete_job_queue](#clientdelete_job_queue)
        - [Client().deregister_job_definition](#clientderegister_job_definition)
        - [Client().describe_compute_environments](#clientdescribe_compute_environments)
        - [Client().describe_job_definitions](#clientdescribe_job_definitions)
        - [Client().describe_job_queues](#clientdescribe_job_queues)
        - [Client().describe_jobs](#clientdescribe_jobs)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().register_job_definition](#clientregister_job_definition)
        - [Client().submit_job](#clientsubmit_job)
        - [Client().terminate_job](#clientterminate_job)
        - [Client().update_compute_environment](#clientupdate_compute_environment)
        - [Client().update_job_queue](#clientupdate_job_queue)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L19)

```python
def cancel_job(jobId: str, reason: str) -> Dict[str, Any]:
```

### Client().create_compute_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L23)

```python
def create_compute_environment(
    computeEnvironmentName: str,
    type: str,
    serviceRole: str,
    state: str = None,
    computeResources: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_job_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L34)

```python
def create_job_queue(
    jobQueueName: str,
    priority: int,
    computeEnvironmentOrder: List[Any],
    state: str = None,
) -> Dict[str, Any]:
```

### Client().delete_compute_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L44)

```python
def delete_compute_environment(computeEnvironment: str) -> Dict[str, Any]:
```

### Client().delete_job_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L48)

```python
def delete_job_queue(jobQueue: str) -> Dict[str, Any]:
```

### Client().deregister_job_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L52)

```python
def deregister_job_definition(jobDefinition: str) -> Dict[str, Any]:
```

### Client().describe_compute_environments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L56)

```python
def describe_compute_environments(
    computeEnvironments: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_job_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L65)

```python
def describe_job_definitions(
    jobDefinitions: List[Any] = None,
    maxResults: int = None,
    jobDefinitionName: str = None,
    status: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_job_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L76)

```python
def describe_job_queues(
    jobQueues: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L82)

```python
def describe_jobs(jobs: List[Any]) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L86)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L96)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L100)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L104)

```python
def list_jobs(
    jobQueue: str = None,
    arrayJobId: str = None,
    multiNodeJobId: str = None,
    jobStatus: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().register_job_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L116)

```python
def register_job_definition(
    jobDefinitionName: str,
    type: str,
    parameters: Dict[str, Any] = None,
    containerProperties: Dict[str, Any] = None,
    nodeProperties: Dict[str, Any] = None,
    retryStrategy: Dict[str, Any] = None,
    timeout: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().submit_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L129)

```python
def submit_job(
    jobName: str,
    jobQueue: str,
    jobDefinition: str,
    arrayProperties: Dict[str, Any] = None,
    dependsOn: List[Any] = None,
    parameters: Dict[str, Any] = None,
    containerOverrides: Dict[str, Any] = None,
    nodeOverrides: Dict[str, Any] = None,
    retryStrategy: Dict[str, Any] = None,
    timeout: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().terminate_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L145)

```python
def terminate_job(jobId: str, reason: str) -> Dict[str, Any]:
```

### Client().update_compute_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L149)

```python
def update_compute_environment(
    computeEnvironment: str,
    state: str = None,
    computeResources: Dict[str, Any] = None,
    serviceRole: str = None,
) -> Dict[str, Any]:
```

### Client().update_job_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/client.py#L159)

```python
def update_job_queue(
    jobQueue: str,
    state: str = None,
    priority: int = None,
    computeEnvironmentOrder: List[Any] = None,
) -> Dict[str, Any]:
```
