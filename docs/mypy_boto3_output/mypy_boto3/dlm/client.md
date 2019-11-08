# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dlm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dlm](index.md#dlm) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_lifecycle_policy](#clientcreate_lifecycle_policy)
        - [Client().delete_lifecycle_policy](#clientdelete_lifecycle_policy)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_lifecycle_policies](#clientget_lifecycle_policies)
        - [Client().get_lifecycle_policy](#clientget_lifecycle_policy)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().update_lifecycle_policy](#clientupdate_lifecycle_policy)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L19)

```python
def create_lifecycle_policy(
    ExecutionRoleArn: str,
    Description: str,
    State: str,
    PolicyDetails: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L29)

```python
def delete_lifecycle_policy(PolicyId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L33)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_lifecycle_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L43)

```python
def get_lifecycle_policies(
    PolicyIds: List[Any] = None,
    State: str = None,
    ResourceTypes: List[Any] = None,
    TargetTags: List[Any] = None,
    TagsToAdd: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L54)

```python
def get_lifecycle_policy(PolicyId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L58)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L62)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().update_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dlm/client.py#L66)

```python
def update_lifecycle_policy(
    PolicyId: str,
    ExecutionRoleArn: str = None,
    State: str = None,
    Description: str = None,
    PolicyDetails: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
