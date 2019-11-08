# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediapackage_vod.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediapackage Vod](index.md#mediapackage-vod) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_asset](#clientcreate_asset)
        - [Client().create_packaging_configuration](#clientcreate_packaging_configuration)
        - [Client().create_packaging_group](#clientcreate_packaging_group)
        - [Client().delete_asset](#clientdelete_asset)
        - [Client().delete_packaging_configuration](#clientdelete_packaging_configuration)
        - [Client().delete_packaging_group](#clientdelete_packaging_group)
        - [Client().describe_asset](#clientdescribe_asset)
        - [Client().describe_packaging_configuration](#clientdescribe_packaging_configuration)
        - [Client().describe_packaging_group](#clientdescribe_packaging_group)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_assets](#clientlist_assets)
        - [Client().list_packaging_configurations](#clientlist_packaging_configurations)
        - [Client().list_packaging_groups](#clientlist_packaging_groups)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_asset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L18)

```python
def create_asset(
    Id: str,
    PackagingGroupId: str,
    SourceArn: str,
    SourceRoleArn: str,
    ResourceId: str = None,
) -> Dict[str, Any]:
```

### Client().create_packaging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L29)

```python
def create_packaging_configuration(
    Id: str,
    PackagingGroupId: str,
    CmafPackage: Dict[str, Any] = None,
    DashPackage: Dict[str, Any] = None,
    HlsPackage: Dict[str, Any] = None,
    MssPackage: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_packaging_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L41)

```python
def create_packaging_group(Id: str) -> Dict[str, Any]:
```

### Client().delete_asset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L45)

```python
def delete_asset(Id: str) -> Dict[str, Any]:
```

### Client().delete_packaging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L49)

```python
def delete_packaging_configuration(Id: str) -> Dict[str, Any]:
```

### Client().delete_packaging_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L53)

```python
def delete_packaging_group(Id: str) -> Dict[str, Any]:
```

### Client().describe_asset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L57)

```python
def describe_asset(Id: str) -> Dict[str, Any]:
```

### Client().describe_packaging_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L61)

```python
def describe_packaging_configuration(Id: str) -> Dict[str, Any]:
```

### Client().describe_packaging_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L65)

```python
def describe_packaging_group(Id: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L79)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L83)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_assets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L87)

```python
def list_assets(
    MaxResults: int = None,
    NextToken: str = None,
    PackagingGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().list_packaging_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L96)

```python
def list_packaging_configurations(
    MaxResults: int = None,
    NextToken: str = None,
    PackagingGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().list_packaging_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediapackage_vod/client.py#L105)

```python
def list_packaging_groups(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```
