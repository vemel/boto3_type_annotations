# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.datapipeline.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Datapipeline](index.md#datapipeline) / Client
    - [Client](#client)
        - [Client().activate_pipeline](#clientactivate_pipeline)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_pipeline](#clientcreate_pipeline)
        - [Client().deactivate_pipeline](#clientdeactivate_pipeline)
        - [Client().delete_pipeline](#clientdelete_pipeline)
        - [Client().describe_objects](#clientdescribe_objects)
        - [Client().describe_pipelines](#clientdescribe_pipelines)
        - [Client().evaluate_expression](#clientevaluate_expression)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_pipeline_definition](#clientget_pipeline_definition)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_pipelines](#clientlist_pipelines)
        - [Client().poll_for_task](#clientpoll_for_task)
        - [Client().put_pipeline_definition](#clientput_pipeline_definition)
        - [Client().query_objects](#clientquery_objects)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().report_task_progress](#clientreport_task_progress)
        - [Client().report_task_runner_heartbeat](#clientreport_task_runner_heartbeat)
        - [Client().set_status](#clientset_status)
        - [Client().set_task_status](#clientset_task_status)
        - [Client().validate_pipeline_definition](#clientvalidate_pipeline_definition)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L13)

```python
class Client(BaseClient):
```

### Client().activate_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L16)

```python
def activate_pipeline(
    pipelineId: str,
    parameterValues: List[Any] = None,
    startTimestamp: datetime = None,
) -> Dict[str, Any]:
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L25)

```python
def add_tags(pipelineId: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L29)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L33)

```python
def create_pipeline(
    name: str,
    uniqueId: str,
    description: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().deactivate_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L39)

```python
def deactivate_pipeline(
    pipelineId: str,
    cancelActive: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L45)

```python
def delete_pipeline(pipelineId: str) -> None:
```

### Client().describe_objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L49)

```python
def describe_objects(
    pipelineId: str,
    objectIds: List[Any],
    evaluateExpressions: bool = None,
    marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_pipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L59)

```python
def describe_pipelines(pipelineIds: List[Any]) -> Dict[str, Any]:
```

### Client().evaluate_expression

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L63)

```python
def evaluate_expression(
    pipelineId: str,
    objectId: str,
    expression: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L79)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_pipeline_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L83)

```python
def get_pipeline_definition(
    pipelineId: str,
    version: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L89)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_pipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L93)

```python
def list_pipelines(marker: str = None) -> Dict[str, Any]:
```

### Client().poll_for_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L97)

```python
def poll_for_task(
    workerGroup: str,
    hostname: str = None,
    instanceIdentity: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_pipeline_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L106)

```python
def put_pipeline_definition(
    pipelineId: str,
    pipelineObjects: List[Any],
    parameterObjects: List[Any] = None,
    parameterValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().query_objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L116)

```python
def query_objects(
    pipelineId: str,
    sphere: str,
    query: Dict[str, Any] = None,
    marker: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L127)

```python
def remove_tags(pipelineId: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().report_task_progress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L131)

```python
def report_task_progress(
    taskId: str,
    fields: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().report_task_runner_heartbeat

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L137)

```python
def report_task_runner_heartbeat(
    taskrunnerId: str,
    workerGroup: str = None,
    hostname: str = None,
) -> Dict[str, Any]:
```

### Client().set_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L143)

```python
def set_status(pipelineId: str, objectIds: List[Any], status: str) -> None:
```

### Client().set_task_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L147)

```python
def set_task_status(
    taskId: str,
    taskStatus: str,
    errorId: str = None,
    errorMessage: str = None,
    errorStackTrace: str = None,
) -> Dict[str, Any]:
```

### Client().validate_pipeline_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/client.py#L158)

```python
def validate_pipeline_definition(
    pipelineId: str,
    pipelineObjects: List[Any],
    parameterObjects: List[Any] = None,
    parameterValues: List[Any] = None,
) -> Dict[str, Any]:
```
