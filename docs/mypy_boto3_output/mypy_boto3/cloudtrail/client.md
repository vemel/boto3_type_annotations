# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudtrail.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudtrail](index.md#cloudtrail) / Client
    - [Client](#client)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_trail](#clientcreate_trail)
        - [Client().delete_trail](#clientdelete_trail)
        - [Client().describe_trails](#clientdescribe_trails)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_event_selectors](#clientget_event_selectors)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_trail](#clientget_trail)
        - [Client().get_trail_status](#clientget_trail_status)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_public_keys](#clientlist_public_keys)
        - [Client().list_tags](#clientlist_tags)
        - [Client().list_trails](#clientlist_trails)
        - [Client().lookup_events](#clientlookup_events)
        - [Client().put_event_selectors](#clientput_event_selectors)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().start_logging](#clientstart_logging)
        - [Client().stop_logging](#clientstop_logging)
        - [Client().update_trail](#clientupdate_trail)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L16)

```python
def add_tags(ResourceId: str, TagsList: List[Any] = None) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L20)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_trail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L24)

```python
def create_trail(
    Name: str,
    S3BucketName: str,
    S3KeyPrefix: str = None,
    SnsTopicName: str = None,
    IncludeGlobalServiceEvents: bool = None,
    IsMultiRegionTrail: bool = None,
    EnableLogFileValidation: bool = None,
    CloudWatchLogsLogGroupArn: str = None,
    CloudWatchLogsRoleArn: str = None,
    KmsKeyId: str = None,
    IsOrganizationTrail: bool = None,
    TagsList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_trail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L42)

```python
def delete_trail(Name: str) -> Dict[str, Any]:
```

### Client().describe_trails

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L46)

```python
def describe_trails(
    trailNameList: List[Any] = None,
    includeShadowTrails: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L52)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_event_selectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L62)

```python
def get_event_selectors(TrailName: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L66)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_trail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L70)

```python
def get_trail(Name: str) -> Dict[str, Any]:
```

### Client().get_trail_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L74)

```python
def get_trail_status(Name: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L78)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_public_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L82)

```python
def list_public_keys(
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L91)

```python
def list_tags(
    ResourceIdList: List[Any],
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_trails

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L97)

```python
def list_trails(NextToken: str = None) -> Dict[str, Any]:
```

### Client().lookup_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L101)

```python
def lookup_events(
    LookupAttributes: List[Any] = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_event_selectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L112)

```python
def put_event_selectors(
    TrailName: str,
    EventSelectors: List[Any],
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L118)

```python
def remove_tags(
    ResourceId: str,
    TagsList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().start_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L124)

```python
def start_logging(Name: str) -> Dict[str, Any]:
```

### Client().stop_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L128)

```python
def stop_logging(Name: str) -> Dict[str, Any]:
```

### Client().update_trail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/client.py#L132)

```python
def update_trail(
    Name: str,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    SnsTopicName: str = None,
    IncludeGlobalServiceEvents: bool = None,
    IsMultiRegionTrail: bool = None,
    EnableLogFileValidation: bool = None,
    CloudWatchLogsLogGroupArn: str = None,
    CloudWatchLogsRoleArn: str = None,
    KmsKeyId: str = None,
    IsOrganizationTrail: bool = None,
) -> Dict[str, Any]:
```
