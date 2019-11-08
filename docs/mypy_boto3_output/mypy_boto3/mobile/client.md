# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mobile.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mobile](index.md#mobile) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_project](#clientcreate_project)
        - [Client().delete_project](#clientdelete_project)
        - [Client().describe_bundle](#clientdescribe_bundle)
        - [Client().describe_project](#clientdescribe_project)
        - [Client().export_bundle](#clientexport_bundle)
        - [Client().export_project](#clientexport_project)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_bundles](#clientlist_bundles)
        - [Client().list_projects](#clientlist_projects)
        - [Client().update_project](#clientupdate_project)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L20)

```python
def create_project(
    name: str = None,
    region: str = None,
    contents: Union[bytes, IO] = None,
    snapshotId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L30)

```python
def delete_project(projectId: str) -> Dict[str, Any]:
```

### Client().describe_bundle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L34)

```python
def describe_bundle(bundleId: str) -> Dict[str, Any]:
```

### Client().describe_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L38)

```python
def describe_project(
    projectId: str,
    syncFromResources: bool = None,
) -> Dict[str, Any]:
```

### Client().export_bundle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L44)

```python
def export_bundle(
    bundleId: str,
    projectId: str = None,
    platform: str = None,
) -> Dict[str, Any]:
```

### Client().export_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L50)

```python
def export_project(projectId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L54)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L64)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L68)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_bundles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L72)

```python
def list_bundles(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L78)

```python
def list_projects(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mobile/client.py#L84)

```python
def update_project(
    projectId: str,
    contents: Union[bytes, IO] = None,
) -> Dict[str, Any]:
```
