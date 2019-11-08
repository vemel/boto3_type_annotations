# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mgh.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mgh](index.md#mgh) / Client
    - [Client](#client)
        - [Client().associate_created_artifact](#clientassociate_created_artifact)
        - [Client().associate_discovered_resource](#clientassociate_discovered_resource)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_progress_update_stream](#clientcreate_progress_update_stream)
        - [Client().delete_progress_update_stream](#clientdelete_progress_update_stream)
        - [Client().describe_application_state](#clientdescribe_application_state)
        - [Client().describe_migration_task](#clientdescribe_migration_task)
        - [Client().disassociate_created_artifact](#clientdisassociate_created_artifact)
        - [Client().disassociate_discovered_resource](#clientdisassociate_discovered_resource)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_migration_task](#clientimport_migration_task)
        - [Client().list_created_artifacts](#clientlist_created_artifacts)
        - [Client().list_discovered_resources](#clientlist_discovered_resources)
        - [Client().list_migration_tasks](#clientlist_migration_tasks)
        - [Client().list_progress_update_streams](#clientlist_progress_update_streams)
        - [Client().notify_application_state](#clientnotify_application_state)
        - [Client().notify_migration_task_state](#clientnotify_migration_task_state)
        - [Client().put_resource_attributes](#clientput_resource_attributes)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L13)

```python
class Client(BaseClient):
```

### Client().associate_created_artifact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L16)

```python
def associate_created_artifact(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    CreatedArtifact: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().associate_discovered_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L26)

```python
def associate_discovered_resource(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    DiscoveredResource: Dict[str, Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L36)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_progress_update_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L40)

```python
def create_progress_update_stream(
    ProgressUpdateStreamName: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_progress_update_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L46)

```python
def delete_progress_update_stream(
    ProgressUpdateStreamName: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_application_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L52)

```python
def describe_application_state(ApplicationId: str) -> Dict[str, Any]:
```

### Client().describe_migration_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L56)

```python
def describe_migration_task(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
) -> Dict[str, Any]:
```

### Client().disassociate_created_artifact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L62)

```python
def disassociate_created_artifact(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    CreatedArtifactName: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().disassociate_discovered_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L72)

```python
def disassociate_discovered_resource(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    ConfigurationId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L82)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L92)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L96)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_migration_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L100)

```python
def import_migration_task(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().list_created_artifacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L106)

```python
def list_created_artifacts(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_discovered_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L116)

```python
def list_discovered_resources(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_migration_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L126)

```python
def list_migration_tasks(
    NextToken: str = None,
    MaxResults: int = None,
    ResourceName: str = None,
) -> Dict[str, Any]:
```

### Client().list_progress_update_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L132)

```python
def list_progress_update_streams(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().notify_application_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L138)

```python
def notify_application_state(
    ApplicationId: str,
    Status: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().notify_migration_task_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L144)

```python
def notify_migration_task_state(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    Task: Dict[str, Any],
    UpdateDateTime: datetime,
    NextUpdateSeconds: int,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().put_resource_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/client.py#L156)

```python
def put_resource_attributes(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    ResourceAttributeList: List[Any],
    DryRun: bool = None,
) -> Dict[str, Any]:
```
