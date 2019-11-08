# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elastictranscoder.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elastictranscoder](index.md#elastictranscoder) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_job](#clientcancel_job)
        - [Client().create_job](#clientcreate_job)
        - [Client().create_pipeline](#clientcreate_pipeline)
        - [Client().create_preset](#clientcreate_preset)
        - [Client().delete_pipeline](#clientdelete_pipeline)
        - [Client().delete_preset](#clientdelete_preset)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_jobs_by_pipeline](#clientlist_jobs_by_pipeline)
        - [Client().list_jobs_by_status](#clientlist_jobs_by_status)
        - [Client().list_pipelines](#clientlist_pipelines)
        - [Client().list_presets](#clientlist_presets)
        - [Client().read_job](#clientread_job)
        - [Client().read_pipeline](#clientread_pipeline)
        - [Client().read_preset](#clientread_preset)
        - [Client().test_role](#clienttest_role)
        - [Client().update_pipeline](#clientupdate_pipeline)
        - [Client().update_pipeline_notifications](#clientupdate_pipeline_notifications)
        - [Client().update_pipeline_status](#clientupdate_pipeline_status)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L19)

```python
def cancel_job(Id: str) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L23)

```python
def create_job(
    PipelineId: str,
    Input: Dict[str, Any] = None,
    Inputs: List[Any] = None,
    Output: Dict[str, Any] = None,
    Outputs: List[Any] = None,
    OutputKeyPrefix: str = None,
    Playlists: List[Any] = None,
    UserMetadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L37)

```python
def create_pipeline(
    Name: str,
    InputBucket: str,
    Role: str,
    OutputBucket: str = None,
    AwsKmsKeyArn: str = None,
    Notifications: Dict[str, Any] = None,
    ContentConfig: Dict[str, Any] = None,
    ThumbnailConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L51)

```python
def create_preset(
    Name: str,
    Container: str,
    Description: str = None,
    Video: Dict[str, Any] = None,
    Audio: Dict[str, Any] = None,
    Thumbnails: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L63)

```python
def delete_pipeline(Id: str) -> Dict[str, Any]:
```

### Client().delete_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L67)

```python
def delete_preset(Id: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L71)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L81)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L85)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_jobs_by_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L89)

```python
def list_jobs_by_pipeline(
    PipelineId: str,
    Ascending: str = None,
    PageToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_jobs_by_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L95)

```python
def list_jobs_by_status(
    Status: str,
    Ascending: str = None,
    PageToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_pipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L101)

```python
def list_pipelines(
    Ascending: str = None,
    PageToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_presets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L107)

```python
def list_presets(
    Ascending: str = None,
    PageToken: str = None,
) -> Dict[str, Any]:
```

### Client().read_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L113)

```python
def read_job(Id: str) -> Dict[str, Any]:
```

### Client().read_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L117)

```python
def read_pipeline(Id: str) -> Dict[str, Any]:
```

### Client().read_preset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L121)

```python
def read_preset(Id: str) -> Dict[str, Any]:
```

### Client().test_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L125)

```python
def test_role(
    Role: str,
    InputBucket: str,
    OutputBucket: str,
    Topics: List[Any],
) -> Dict[str, Any]:
```

### Client().update_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L131)

```python
def update_pipeline(
    Id: str,
    Name: str = None,
    InputBucket: str = None,
    Role: str = None,
    AwsKmsKeyArn: str = None,
    Notifications: Dict[str, Any] = None,
    ContentConfig: Dict[str, Any] = None,
    ThumbnailConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_pipeline_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L145)

```python
def update_pipeline_notifications(
    Id: str,
    Notifications: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_pipeline_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elastictranscoder/client.py#L151)

```python
def update_pipeline_status(Id: str, Status: str) -> Dict[str, Any]:
```
