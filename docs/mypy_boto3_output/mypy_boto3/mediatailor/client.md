# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediatailor.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediatailor](index.md#mediatailor) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_playback_configuration](#clientdelete_playback_configuration)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_playback_configuration](#clientget_playback_configuration)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_playback_configurations](#clientlist_playback_configurations)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_playback_configuration](#clientput_playback_configuration)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_playback_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L19)

```python
def delete_playback_configuration(Name: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L23)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L33)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_playback_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L37)

```python
def get_playback_configuration(Name: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L41)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_playback_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L45)

```python
def list_playback_configurations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L51)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().put_playback_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L55)

```python
def put_playback_configuration(
    AdDecisionServerUrl: str = None,
    CdnConfiguration: Dict[str, Any] = None,
    DashConfiguration: Dict[str, Any] = None,
    Name: str = None,
    SlateAdUrl: str = None,
    Tags: Dict[str, Any] = None,
    TranscodeProfileName: str = None,
    VideoContentSourceUrl: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L69)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediatailor/client.py#L73)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```
