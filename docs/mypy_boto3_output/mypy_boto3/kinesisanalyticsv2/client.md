# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesisanalyticsv2.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesisanalyticsv2](index.md#kinesisanalyticsv2) / Client
    - [Client](#client)
        - [Client().add_application_cloud_watch_logging_option](#clientadd_application_cloud_watch_logging_option)
        - [Client().add_application_input](#clientadd_application_input)
        - [Client().add_application_input_processing_configuration](#clientadd_application_input_processing_configuration)
        - [Client().add_application_output](#clientadd_application_output)
        - [Client().add_application_reference_data_source](#clientadd_application_reference_data_source)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_application_snapshot](#clientcreate_application_snapshot)
        - [Client().delete_application](#clientdelete_application)
        - [Client().delete_application_cloud_watch_logging_option](#clientdelete_application_cloud_watch_logging_option)
        - [Client().delete_application_input_processing_configuration](#clientdelete_application_input_processing_configuration)
        - [Client().delete_application_output](#clientdelete_application_output)
        - [Client().delete_application_reference_data_source](#clientdelete_application_reference_data_source)
        - [Client().delete_application_snapshot](#clientdelete_application_snapshot)
        - [Client().describe_application](#clientdescribe_application)
        - [Client().describe_application_snapshot](#clientdescribe_application_snapshot)
        - [Client().discover_input_schema](#clientdiscover_input_schema)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_application_snapshots](#clientlist_application_snapshots)
        - [Client().list_applications](#clientlist_applications)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().start_application](#clientstart_application)
        - [Client().stop_application](#clientstop_application)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_application](#clientupdate_application)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_application_cloud_watch_logging_option

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L16)

```python
def add_application_cloud_watch_logging_option(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    CloudWatchLoggingOption: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().add_application_input

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L25)

```python
def add_application_input(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    Input: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().add_application_input_processing_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L34)

```python
def add_application_input_processing_configuration(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    InputId: str,
    InputProcessingConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().add_application_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L44)

```python
def add_application_output(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    Output: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().add_application_reference_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L53)

```python
def add_application_reference_data_source(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ReferenceDataSource: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L62)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L66)

```python
def create_application(
    ApplicationName: str,
    RuntimeEnvironment: str,
    ServiceExecutionRole: str,
    ApplicationDescription: str = None,
    ApplicationConfiguration: Dict[str, Any] = None,
    CloudWatchLoggingOptions: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_application_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L79)

```python
def create_application_snapshot(
    ApplicationName: str,
    SnapshotName: str,
) -> Dict[str, Any]:
```

### Client().delete_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L85)

```python
def delete_application(
    ApplicationName: str,
    CreateTimestamp: datetime,
) -> Dict[str, Any]:
```

### Client().delete_application_cloud_watch_logging_option

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L91)

```python
def delete_application_cloud_watch_logging_option(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    CloudWatchLoggingOptionId: str,
) -> Dict[str, Any]:
```

### Client().delete_application_input_processing_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L100)

```python
def delete_application_input_processing_configuration(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    InputId: str,
) -> Dict[str, Any]:
```

### Client().delete_application_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L106)

```python
def delete_application_output(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    OutputId: str,
) -> Dict[str, Any]:
```

### Client().delete_application_reference_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L112)

```python
def delete_application_reference_data_source(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ReferenceId: str,
) -> Dict[str, Any]:
```

### Client().delete_application_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L118)

```python
def delete_application_snapshot(
    ApplicationName: str,
    SnapshotName: str,
    SnapshotCreationTimestamp: datetime,
) -> Dict[str, Any]:
```

### Client().describe_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L127)

```python
def describe_application(
    ApplicationName: str,
    IncludeAdditionalDetails: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_application_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L133)

```python
def describe_application_snapshot(
    ApplicationName: str,
    SnapshotName: str,
) -> Dict[str, Any]:
```

### Client().discover_input_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L139)

```python
def discover_input_schema(
    ServiceExecutionRole: str,
    ResourceARN: str = None,
    InputStartingPositionConfiguration: Dict[str, Any] = None,
    S3Configuration: Dict[str, Any] = None,
    InputProcessingConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L150)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L160)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L164)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_application_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L168)

```python
def list_application_snapshots(
    ApplicationName: str,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L174)

```python
def list_applications(
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L180)

```python
def list_tags_for_resource(ResourceARN: str) -> Dict[str, Any]:
```

### Client().start_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L184)

```python
def start_application(
    ApplicationName: str,
    RunConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().stop_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L190)

```python
def stop_application(ApplicationName: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L194)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L198)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/client.py#L202)

```python
def update_application(
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ApplicationConfigurationUpdate: Dict[str, Any] = None,
    ServiceExecutionRoleUpdate: str = None,
    RunConfigurationUpdate: Dict[str, Any] = None,
    CloudWatchLoggingOptionUpdates: List[Any] = None,
) -> Dict[str, Any]:
```
