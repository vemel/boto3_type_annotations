# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codepipeline.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codepipeline](index.md#codepipeline) / Client
    - [Client](#client)
        - [Client().acknowledge_job](#clientacknowledge_job)
        - [Client().acknowledge_third_party_job](#clientacknowledge_third_party_job)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_custom_action_type](#clientcreate_custom_action_type)
        - [Client().create_pipeline](#clientcreate_pipeline)
        - [Client().delete_custom_action_type](#clientdelete_custom_action_type)
        - [Client().delete_pipeline](#clientdelete_pipeline)
        - [Client().delete_webhook](#clientdelete_webhook)
        - [Client().deregister_webhook_with_third_party](#clientderegister_webhook_with_third_party)
        - [Client().disable_stage_transition](#clientdisable_stage_transition)
        - [Client().enable_stage_transition](#clientenable_stage_transition)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_job_details](#clientget_job_details)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_pipeline](#clientget_pipeline)
        - [Client().get_pipeline_execution](#clientget_pipeline_execution)
        - [Client().get_pipeline_state](#clientget_pipeline_state)
        - [Client().get_third_party_job_details](#clientget_third_party_job_details)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_action_executions](#clientlist_action_executions)
        - [Client().list_action_types](#clientlist_action_types)
        - [Client().list_pipeline_executions](#clientlist_pipeline_executions)
        - [Client().list_pipelines](#clientlist_pipelines)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_webhooks](#clientlist_webhooks)
        - [Client().poll_for_jobs](#clientpoll_for_jobs)
        - [Client().poll_for_third_party_jobs](#clientpoll_for_third_party_jobs)
        - [Client().put_action_revision](#clientput_action_revision)
        - [Client().put_approval_result](#clientput_approval_result)
        - [Client().put_job_failure_result](#clientput_job_failure_result)
        - [Client().put_job_success_result](#clientput_job_success_result)
        - [Client().put_third_party_job_failure_result](#clientput_third_party_job_failure_result)
        - [Client().put_third_party_job_success_result](#clientput_third_party_job_success_result)
        - [Client().put_webhook](#clientput_webhook)
        - [Client().register_webhook_with_third_party](#clientregister_webhook_with_third_party)
        - [Client().retry_stage_execution](#clientretry_stage_execution)
        - [Client().start_pipeline_execution](#clientstart_pipeline_execution)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_pipeline](#clientupdate_pipeline)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L12)

```python
class Client(BaseClient):
```

### Client().acknowledge_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L15)

```python
def acknowledge_job(jobId: str, nonce: str) -> Dict[str, Any]:
```

### Client().acknowledge_third_party_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L19)

```python
def acknowledge_third_party_job(
    jobId: str,
    nonce: str,
    clientToken: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L25)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_custom_action_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L29)

```python
def create_custom_action_type(
    category: str,
    provider: str,
    version: str,
    inputArtifactDetails: Dict[str, Any],
    outputArtifactDetails: Dict[str, Any],
    settings: Dict[str, Any] = None,
    configurationProperties: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L43)

```python
def create_pipeline(
    pipeline: Dict[str, Any],
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_custom_action_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L49)

```python
def delete_custom_action_type(
    category: str,
    provider: str,
    version: str,
) -> None:
```

### Client().delete_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L55)

```python
def delete_pipeline(name: str) -> None:
```

### Client().delete_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L59)

```python
def delete_webhook(name: str) -> Dict[str, Any]:
```

### Client().deregister_webhook_with_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L63)

```python
def deregister_webhook_with_third_party(
    webhookName: str = None,
) -> Dict[str, Any]:
```

### Client().disable_stage_transition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L69)

```python
def disable_stage_transition(
    pipelineName: str,
    stageName: str,
    transitionType: str,
    reason: str,
) -> None:
```

### Client().enable_stage_transition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L75)

```python
def enable_stage_transition(
    pipelineName: str,
    stageName: str,
    transitionType: str,
) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L81)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_job_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L91)

```python
def get_job_details(jobId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L95)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L99)

```python
def get_pipeline(name: str, version: int = None) -> Dict[str, Any]:
```

### Client().get_pipeline_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L103)

```python
def get_pipeline_execution(
    pipelineName: str,
    pipelineExecutionId: str,
) -> Dict[str, Any]:
```

### Client().get_pipeline_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L109)

```python
def get_pipeline_state(name: str) -> Dict[str, Any]:
```

### Client().get_third_party_job_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L113)

```python
def get_third_party_job_details(
    jobId: str,
    clientToken: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L119)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_action_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L123)

```python
def list_action_executions(
    pipelineName: str,
    filter: Dict[str, Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_action_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L133)

```python
def list_action_types(
    actionOwnerFilter: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_pipeline_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L139)

```python
def list_pipeline_executions(
    pipelineName: str,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_pipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L145)

```python
def list_pipelines(nextToken: str = None) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L149)

```python
def list_tags_for_resource(
    resourceArn: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_webhooks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L155)

```python
def list_webhooks(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().poll_for_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L161)

```python
def poll_for_jobs(
    actionTypeId: Dict[str, Any],
    maxBatchSize: int = None,
    queryParam: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().poll_for_third_party_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L170)

```python
def poll_for_third_party_jobs(
    actionTypeId: Dict[str, Any],
    maxBatchSize: int = None,
) -> Dict[str, Any]:
```

### Client().put_action_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L176)

```python
def put_action_revision(
    pipelineName: str,
    stageName: str,
    actionName: str,
    actionRevision: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_approval_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L186)

```python
def put_approval_result(
    pipelineName: str,
    stageName: str,
    actionName: str,
    result: Dict[str, Any],
    token: str,
) -> Dict[str, Any]:
```

### Client().put_job_failure_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L197)

```python
def put_job_failure_result(
    jobId: str,
    failureDetails: Dict[str, Any],
) -> None:
```

### Client().put_job_success_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L203)

```python
def put_job_success_result(
    jobId: str,
    currentRevision: Dict[str, Any] = None,
    continuationToken: str = None,
    executionDetails: Dict[str, Any] = None,
) -> None:
```

### Client().put_third_party_job_failure_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L213)

```python
def put_third_party_job_failure_result(
    jobId: str,
    clientToken: str,
    failureDetails: Dict[str, Any],
) -> None:
```

### Client().put_third_party_job_success_result

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L219)

```python
def put_third_party_job_success_result(
    jobId: str,
    clientToken: str,
    currentRevision: Dict[str, Any] = None,
    continuationToken: str = None,
    executionDetails: Dict[str, Any] = None,
) -> None:
```

### Client().put_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L230)

```python
def put_webhook(
    webhook: Dict[str, Any],
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().register_webhook_with_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L236)

```python
def register_webhook_with_third_party(
    webhookName: str = None,
) -> Dict[str, Any]:
```

### Client().retry_stage_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L242)

```python
def retry_stage_execution(
    pipelineName: str,
    stageName: str,
    pipelineExecutionId: str,
    retryMode: str,
) -> Dict[str, Any]:
```

### Client().start_pipeline_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L252)

```python
def start_pipeline_execution(
    name: str,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L258)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L262)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codepipeline/client.py#L266)

```python
def update_pipeline(pipeline: Dict[str, Any]) -> Dict[str, Any]:
```
