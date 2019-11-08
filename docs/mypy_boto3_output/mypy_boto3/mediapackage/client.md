# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediapackage.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediapackage](index.md#mediapackage) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_channel](#clientcreate_channel)
        - [Client().create_harvest_job](#clientcreate_harvest_job)
        - [Client().create_origin_endpoint](#clientcreate_origin_endpoint)
        - [Client().delete_channel](#clientdelete_channel)
        - [Client().delete_origin_endpoint](#clientdelete_origin_endpoint)
        - [Client().describe_channel](#clientdescribe_channel)
        - [Client().describe_harvest_job](#clientdescribe_harvest_job)
        - [Client().describe_origin_endpoint](#clientdescribe_origin_endpoint)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_channels](#clientlist_channels)
        - [Client().list_harvest_jobs](#clientlist_harvest_jobs)
        - [Client().list_origin_endpoints](#clientlist_origin_endpoints)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().rotate_channel_credentials](#clientrotate_channel_credentials)
        - [Client().rotate_ingest_endpoint_credentials](#clientrotate_ingest_endpoint_credentials)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_channel](#clientupdate_channel)
        - [Client().update_origin_endpoint](#clientupdate_origin_endpoint)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L19)

```python
def create_channel(
    Id: str,
    Description: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_harvest_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L25)

```python
def create_harvest_job(
    EndTime: str,
    Id: str,
    OriginEndpointId: str,
    S3Destination: Dict[str, Any],
    StartTime: str,
) -> Dict[str, Any]:
```

### Client().create_origin_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L36)

```python
def create_origin_endpoint(
    ChannelId: str,
    Id: str,
    CmafPackage: Dict[str, Any] = None,
    DashPackage: Dict[str, Any] = None,
    Description: str = None,
    HlsPackage: Dict[str, Any] = None,
    ManifestName: str = None,
    MssPackage: Dict[str, Any] = None,
    Origination: str = None,
    StartoverWindowSeconds: int = None,
    Tags: Dict[str, Any] = None,
    TimeDelaySeconds: int = None,
    Whitelist: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L55)

```python
def delete_channel(Id: str) -> Dict[str, Any]:
```

### Client().delete_origin_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L59)

```python
def delete_origin_endpoint(Id: str) -> Dict[str, Any]:
```

### Client().describe_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L63)

```python
def describe_channel(Id: str) -> Dict[str, Any]:
```

### Client().describe_harvest_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L67)

```python
def describe_harvest_job(Id: str) -> Dict[str, Any]:
```

### Client().describe_origin_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L71)

```python
def describe_origin_endpoint(Id: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L75)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L85)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L89)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_channels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L93)

```python
def list_channels(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_harvest_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L99)

```python
def list_harvest_jobs(
    IncludeChannelId: str = None,
    IncludeStatus: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_origin_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L109)

```python
def list_origin_endpoints(
    ChannelId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L115)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().rotate_channel_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L119)

```python
def rotate_channel_credentials(Id: str) -> Dict[str, Any]:
```

### Client().rotate_ingest_endpoint_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L123)

```python
def rotate_ingest_endpoint_credentials(
    Id: str,
    IngestEndpointId: str,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L129)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L133)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L137)

```python
def update_channel(Id: str, Description: str = None) -> Dict[str, Any]:
```

### Client().update_origin_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage/client.py#L141)

```python
def update_origin_endpoint(
    Id: str,
    CmafPackage: Dict[str, Any] = None,
    DashPackage: Dict[str, Any] = None,
    Description: str = None,
    HlsPackage: Dict[str, Any] = None,
    ManifestName: str = None,
    MssPackage: Dict[str, Any] = None,
    Origination: str = None,
    StartoverWindowSeconds: int = None,
    TimeDelaySeconds: int = None,
    Whitelist: List[Any] = None,
) -> Dict[str, Any]:
```
