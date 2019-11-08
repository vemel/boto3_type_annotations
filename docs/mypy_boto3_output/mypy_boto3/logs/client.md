# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.logs.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Logs](index.md#logs) / Client
    - [Client](#client)
        - [Client().associate_kms_key](#clientassociate_kms_key)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_export_task](#clientcancel_export_task)
        - [Client().create_export_task](#clientcreate_export_task)
        - [Client().create_log_group](#clientcreate_log_group)
        - [Client().create_log_stream](#clientcreate_log_stream)
        - [Client().delete_destination](#clientdelete_destination)
        - [Client().delete_log_group](#clientdelete_log_group)
        - [Client().delete_log_stream](#clientdelete_log_stream)
        - [Client().delete_metric_filter](#clientdelete_metric_filter)
        - [Client().delete_resource_policy](#clientdelete_resource_policy)
        - [Client().delete_retention_policy](#clientdelete_retention_policy)
        - [Client().delete_subscription_filter](#clientdelete_subscription_filter)
        - [Client().describe_destinations](#clientdescribe_destinations)
        - [Client().describe_export_tasks](#clientdescribe_export_tasks)
        - [Client().describe_log_groups](#clientdescribe_log_groups)
        - [Client().describe_log_streams](#clientdescribe_log_streams)
        - [Client().describe_metric_filters](#clientdescribe_metric_filters)
        - [Client().describe_queries](#clientdescribe_queries)
        - [Client().describe_resource_policies](#clientdescribe_resource_policies)
        - [Client().describe_subscription_filters](#clientdescribe_subscription_filters)
        - [Client().disassociate_kms_key](#clientdisassociate_kms_key)
        - [Client().filter_log_events](#clientfilter_log_events)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_log_events](#clientget_log_events)
        - [Client().get_log_group_fields](#clientget_log_group_fields)
        - [Client().get_log_record](#clientget_log_record)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_query_results](#clientget_query_results)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_tags_log_group](#clientlist_tags_log_group)
        - [Client().put_destination](#clientput_destination)
        - [Client().put_destination_policy](#clientput_destination_policy)
        - [Client().put_log_events](#clientput_log_events)
        - [Client().put_metric_filter](#clientput_metric_filter)
        - [Client().put_resource_policy](#clientput_resource_policy)
        - [Client().put_retention_policy](#clientput_retention_policy)
        - [Client().put_subscription_filter](#clientput_subscription_filter)
        - [Client().start_query](#clientstart_query)
        - [Client().stop_query](#clientstop_query)
        - [Client().tag_log_group](#clienttag_log_group)
        - [Client().test_metric_filter](#clienttest_metric_filter)
        - [Client().untag_log_group](#clientuntag_log_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_kms_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L15)

```python
def associate_kms_key(logGroupName: str, kmsKeyId: str) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_export_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L23)

```python
def cancel_export_task(taskId: str) -> None:
```

### Client().create_export_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L27)

```python
def create_export_task(
    logGroupName: str,
    fromTime: int,
    to: int,
    destination: str,
    taskName: str = None,
    logStreamNamePrefix: str = None,
    destinationPrefix: str = None,
) -> Dict[str, Any]:
```

### Client().create_log_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L40)

```python
def create_log_group(
    logGroupName: str,
    kmsKeyId: str = None,
    tags: Dict[str, Any] = None,
) -> None:
```

### Client().create_log_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L46)

```python
def create_log_stream(logGroupName: str, logStreamName: str) -> None:
```

### Client().delete_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L50)

```python
def delete_destination(destinationName: str) -> None:
```

### Client().delete_log_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L54)

```python
def delete_log_group(logGroupName: str) -> None:
```

### Client().delete_log_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L58)

```python
def delete_log_stream(logGroupName: str, logStreamName: str) -> None:
```

### Client().delete_metric_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L62)

```python
def delete_metric_filter(logGroupName: str, filterName: str) -> None:
```

### Client().delete_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L66)

```python
def delete_resource_policy(policyName: str = None) -> None:
```

### Client().delete_retention_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L70)

```python
def delete_retention_policy(logGroupName: str) -> None:
```

### Client().delete_subscription_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L74)

```python
def delete_subscription_filter(logGroupName: str, filterName: str) -> None:
```

### Client().describe_destinations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L78)

```python
def describe_destinations(
    DestinationNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_export_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L87)

```python
def describe_export_tasks(
    taskId: str = None,
    statusCode: str = None,
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_log_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L97)

```python
def describe_log_groups(
    logGroupNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_log_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L103)

```python
def describe_log_streams(
    logGroupName: str,
    logStreamNamePrefix: str = None,
    orderBy: str = None,
    descending: bool = None,
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_metric_filters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L115)

```python
def describe_metric_filters(
    logGroupName: str = None,
    filterNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None,
    metricName: str = None,
    metricNamespace: str = None,
) -> Dict[str, Any]:
```

### Client().describe_queries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L127)

```python
def describe_queries(
    logGroupName: str = None,
    status: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_resource_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L137)

```python
def describe_resource_policies(
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_subscription_filters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L143)

```python
def describe_subscription_filters(
    logGroupName: str,
    filterNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().disassociate_kms_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L153)

```python
def disassociate_kms_key(logGroupName: str) -> None:
```

### Client().filter_log_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L157)

```python
def filter_log_events(
    logGroupName: str,
    logStreamNames: List[Any] = None,
    logStreamNamePrefix: str = None,
    startTime: int = None,
    endTime: int = None,
    filterPattern: str = None,
    nextToken: str = None,
    limit: int = None,
    interleaved: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L172)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_log_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L182)

```python
def get_log_events(
    logGroupName: str,
    logStreamName: str,
    startTime: int = None,
    endTime: int = None,
    nextToken: str = None,
    limit: int = None,
    startFromHead: bool = None,
) -> Dict[str, Any]:
```

### Client().get_log_group_fields

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L195)

```python
def get_log_group_fields(
    logGroupName: str,
    time: int = None,
) -> Dict[str, Any]:
```

### Client().get_log_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L201)

```python
def get_log_record(logRecordPointer: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L205)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_query_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L209)

```python
def get_query_results(queryId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L213)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_tags_log_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L217)

```python
def list_tags_log_group(logGroupName: str) -> Dict[str, Any]:
```

### Client().put_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L221)

```python
def put_destination(
    destinationName: str,
    targetArn: str,
    roleArn: str,
) -> Dict[str, Any]:
```

### Client().put_destination_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L227)

```python
def put_destination_policy(destinationName: str, accessPolicy: str) -> None:
```

### Client().put_log_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L231)

```python
def put_log_events(
    logGroupName: str,
    logStreamName: str,
    logEvents: List[Any],
    sequenceToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_metric_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L241)

```python
def put_metric_filter(
    logGroupName: str,
    filterName: str,
    filterPattern: str,
    metricTransformations: List[Any],
) -> None:
```

### Client().put_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L251)

```python
def put_resource_policy(
    policyName: str = None,
    policyDocument: str = None,
) -> Dict[str, Any]:
```

### Client().put_retention_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L257)

```python
def put_retention_policy(logGroupName: str, retentionInDays: int) -> None:
```

### Client().put_subscription_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L261)

```python
def put_subscription_filter(
    logGroupName: str,
    filterName: str,
    filterPattern: str,
    destinationArn: str,
    roleArn: str = None,
    distribution: str = None,
) -> None:
```

### Client().start_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L273)

```python
def start_query(
    startTime: int,
    endTime: int,
    queryString: str,
    logGroupName: str = None,
    logGroupNames: List[Any] = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().stop_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L285)

```python
def stop_query(queryId: str) -> Dict[str, Any]:
```

### Client().tag_log_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L289)

```python
def tag_log_group(logGroupName: str, tags: Dict[str, Any]) -> None:
```

### Client().test_metric_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L293)

```python
def test_metric_filter(
    filterPattern: str,
    logEventMessages: List[Any],
) -> Dict[str, Any]:
```

### Client().untag_log_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/client.py#L299)

```python
def untag_log_group(logGroupName: str, tags: List[Any]) -> None:
```
