# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesis_video_archived_media.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesis Video Archived Media](index.md#kinesis-video-archived-media) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_dash_streaming_session_url](#clientget_dash_streaming_session_url)
        - [Client().get_hls_streaming_session_url](#clientget_hls_streaming_session_url)
        - [Client().get_media_for_fragment_list](#clientget_media_for_fragment_list)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_fragments](#clientlist_fragments)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L19)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_dash_streaming_session_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L29)

```python
def get_dash_streaming_session_url(
    StreamName: str = None,
    StreamARN: str = None,
    PlaybackMode: str = None,
    DisplayFragmentTimestamp: str = None,
    DisplayFragmentNumber: str = None,
    DASHFragmentSelector: Dict[str, Any] = None,
    Expires: int = None,
    MaxManifestFragmentResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_hls_streaming_session_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L43)

```python
def get_hls_streaming_session_url(
    StreamName: str = None,
    StreamARN: str = None,
    PlaybackMode: str = None,
    HLSFragmentSelector: Dict[str, Any] = None,
    ContainerFormat: str = None,
    DiscontinuityMode: str = None,
    DisplayFragmentTimestamp: str = None,
    Expires: int = None,
    MaxMediaPlaylistFragmentResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_media_for_fragment_list

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L58)

```python
def get_media_for_fragment_list(
    StreamName: str,
    Fragments: List[Any],
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L64)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L68)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_fragments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis_video_archived_media/client.py#L72)

```python
def list_fragments(
    StreamName: str,
    MaxResults: int = None,
    NextToken: str = None,
    FragmentSelector: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
