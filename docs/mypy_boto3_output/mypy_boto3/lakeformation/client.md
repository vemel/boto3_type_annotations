# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lakeformation.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lakeformation](index.md#lakeformation) / Client
    - [Client](#client)
        - [Client().batch_grant_permissions](#clientbatch_grant_permissions)
        - [Client().batch_revoke_permissions](#clientbatch_revoke_permissions)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().deregister_resource](#clientderegister_resource)
        - [Client().describe_resource](#clientdescribe_resource)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_data_lake_settings](#clientget_data_lake_settings)
        - [Client().get_effective_permissions_for_path](#clientget_effective_permissions_for_path)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().grant_permissions](#clientgrant_permissions)
        - [Client().list_permissions](#clientlist_permissions)
        - [Client().list_resources](#clientlist_resources)
        - [Client().put_data_lake_settings](#clientput_data_lake_settings)
        - [Client().register_resource](#clientregister_resource)
        - [Client().revoke_permissions](#clientrevoke_permissions)
        - [Client().update_resource](#clientupdate_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_grant_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L15)

```python
def batch_grant_permissions(
    Entries: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_revoke_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L21)

```python
def batch_revoke_permissions(
    Entries: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L27)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().deregister_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L31)

```python
def deregister_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().describe_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L35)

```python
def describe_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L39)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_data_lake_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L49)

```python
def get_data_lake_settings(CatalogId: str = None) -> Dict[str, Any]:
```

### Client().get_effective_permissions_for_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L53)

```python
def get_effective_permissions_for_path(
    ResourceArn: str,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L63)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L67)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().grant_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L71)

```python
def grant_permissions(
    Principal: Dict[str, Any],
    Resource: Dict[str, Any],
    Permissions: List[Any],
    CatalogId: str = None,
    PermissionsWithGrantOption: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L82)

```python
def list_permissions(
    CatalogId: str = None,
    Principal: Dict[str, Any] = None,
    ResourceType: str = None,
    Resource: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L94)

```python
def list_resources(
    FilterConditionList: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_data_lake_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L103)

```python
def put_data_lake_settings(
    DataLakeSettings: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().register_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L109)

```python
def register_resource(
    ResourceArn: str,
    UseServiceLinkedRole: bool = None,
    RoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().revoke_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L115)

```python
def revoke_permissions(
    Principal: Dict[str, Any],
    Resource: Dict[str, Any],
    Permissions: List[Any],
    CatalogId: str = None,
    PermissionsWithGrantOption: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lakeformation/client.py#L126)

```python
def update_resource(RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
```
