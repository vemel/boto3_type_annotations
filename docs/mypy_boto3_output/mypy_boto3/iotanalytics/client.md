# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iotanalytics.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iotanalytics](index.md#iotanalytics) / Client
    - [Client](#client)
        - [Client().batch_put_message](#clientbatch_put_message)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_pipeline_reprocessing](#clientcancel_pipeline_reprocessing)
        - [Client().create_channel](#clientcreate_channel)
        - [Client().create_dataset](#clientcreate_dataset)
        - [Client().create_dataset_content](#clientcreate_dataset_content)
        - [Client().create_datastore](#clientcreate_datastore)
        - [Client().create_pipeline](#clientcreate_pipeline)
        - [Client().delete_channel](#clientdelete_channel)
        - [Client().delete_dataset](#clientdelete_dataset)
        - [Client().delete_dataset_content](#clientdelete_dataset_content)
        - [Client().delete_datastore](#clientdelete_datastore)
        - [Client().delete_pipeline](#clientdelete_pipeline)
        - [Client().describe_channel](#clientdescribe_channel)
        - [Client().describe_dataset](#clientdescribe_dataset)
        - [Client().describe_datastore](#clientdescribe_datastore)
        - [Client().describe_logging_options](#clientdescribe_logging_options)
        - [Client().describe_pipeline](#clientdescribe_pipeline)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_dataset_content](#clientget_dataset_content)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_channels](#clientlist_channels)
        - [Client().list_dataset_contents](#clientlist_dataset_contents)
        - [Client().list_datasets](#clientlist_datasets)
        - [Client().list_datastores](#clientlist_datastores)
        - [Client().list_pipelines](#clientlist_pipelines)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_logging_options](#clientput_logging_options)
        - [Client().run_pipeline_activity](#clientrun_pipeline_activity)
        - [Client().sample_channel_data](#clientsample_channel_data)
        - [Client().start_pipeline_reprocessing](#clientstart_pipeline_reprocessing)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_channel](#clientupdate_channel)
        - [Client().update_dataset](#clientupdate_dataset)
        - [Client().update_datastore](#clientupdate_datastore)
        - [Client().update_pipeline](#clientupdate_pipeline)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L13)

```python
class Client(BaseClient):
```

### Client().batch_put_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L16)

```python
def batch_put_message(
    channelName: str,
    messages: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_pipeline_reprocessing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L26)

```python
def cancel_pipeline_reprocessing(
    pipelineName: str,
    reprocessingId: str,
) -> Dict[str, Any]:
```

### Client().create_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L32)

```python
def create_channel(
    channelName: str,
    channelStorage: Dict[str, Any] = None,
    retentionPeriod: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L42)

```python
def create_dataset(
    datasetName: str,
    actions: List[Any],
    triggers: List[Any] = None,
    contentDeliveryRules: List[Any] = None,
    retentionPeriod: Dict[str, Any] = None,
    versioningConfiguration: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_dataset_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L55)

```python
def create_dataset_content(datasetName: str) -> Dict[str, Any]:
```

### Client().create_datastore

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L59)

```python
def create_datastore(
    datastoreName: str,
    datastoreStorage: Dict[str, Any] = None,
    retentionPeriod: Dict[str, Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L69)

```python
def create_pipeline(
    pipelineName: str,
    pipelineActivities: List[Any],
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L75)

```python
def delete_channel(channelName: str) -> None:
```

### Client().delete_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L79)

```python
def delete_dataset(datasetName: str) -> None:
```

### Client().delete_dataset_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L83)

```python
def delete_dataset_content(datasetName: str, versionId: str = None) -> None:
```

### Client().delete_datastore

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L87)

```python
def delete_datastore(datastoreName: str) -> None:
```

### Client().delete_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L91)

```python
def delete_pipeline(pipelineName: str) -> None:
```

### Client().describe_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L95)

```python
def describe_channel(
    channelName: str,
    includeStatistics: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L101)

```python
def describe_dataset(datasetName: str) -> Dict[str, Any]:
```

### Client().describe_datastore

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L105)

```python
def describe_datastore(
    datastoreName: str,
    includeStatistics: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L111)

```python
def describe_logging_options() -> Dict[str, Any]:
```

### Client().describe_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L115)

```python
def describe_pipeline(pipelineName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L119)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_dataset_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L129)

```python
def get_dataset_content(
    datasetName: str,
    versionId: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L135)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L139)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_channels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L143)

```python
def list_channels(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_dataset_contents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L149)

```python
def list_dataset_contents(
    datasetName: str,
    nextToken: str = None,
    maxResults: int = None,
    scheduledOnOrAfter: datetime = None,
    scheduledBefore: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_datasets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L160)

```python
def list_datasets(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_datastores

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L166)

```python
def list_datastores(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_pipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L172)

```python
def list_pipelines(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L178)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().put_logging_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L182)

```python
def put_logging_options(loggingOptions: Dict[str, Any]) -> None:
```

### Client().run_pipeline_activity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L186)

```python
def run_pipeline_activity(
    pipelineActivity: Dict[str, Any],
    payloads: List[Any],
) -> Dict[str, Any]:
```

### Client().sample_channel_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L192)

```python
def sample_channel_data(
    channelName: str,
    maxMessages: int = None,
    startTime: datetime = None,
    endTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().start_pipeline_reprocessing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L202)

```python
def start_pipeline_reprocessing(
    pipelineName: str,
    startTime: datetime = None,
    endTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L208)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L212)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L216)

```python
def update_channel(
    channelName: str,
    channelStorage: Dict[str, Any] = None,
    retentionPeriod: Dict[str, Any] = None,
) -> None:
```

### Client().update_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L225)

```python
def update_dataset(
    datasetName: str,
    actions: List[Any],
    triggers: List[Any] = None,
    contentDeliveryRules: List[Any] = None,
    retentionPeriod: Dict[str, Any] = None,
    versioningConfiguration: Dict[str, Any] = None,
) -> None:
```

### Client().update_datastore

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L237)

```python
def update_datastore(
    datastoreName: str,
    retentionPeriod: Dict[str, Any] = None,
    datastoreStorage: Dict[str, Any] = None,
) -> None:
```

### Client().update_pipeline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotanalytics/client.py#L246)

```python
def update_pipeline(pipelineName: str, pipelineActivities: List[Any]) -> None:
```
