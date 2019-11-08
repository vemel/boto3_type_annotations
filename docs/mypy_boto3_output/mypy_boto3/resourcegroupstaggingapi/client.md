# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.resourcegroupstaggingapi.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Resourcegroupstaggingapi](index.md#resourcegroupstaggingapi) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resources](#clientget_resources)
        - [Client().get_tag_keys](#clientget_tag_keys)
        - [Client().get_tag_values](#clientget_tag_values)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().tag_resources](#clienttag_resources)
        - [Client().untag_resources](#clientuntag_resources)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L19)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L29)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L33)

```python
def get_resources(
    PaginationToken: str = None,
    TagFilters: List[Any] = None,
    ResourcesPerPage: int = None,
    TagsPerPage: int = None,
    ResourceTypeFilters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_tag_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L44)

```python
def get_tag_keys(PaginationToken: str = None) -> Dict[str, Any]:
```

### Client().get_tag_values

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L48)

```python
def get_tag_values(Key: str, PaginationToken: str = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L52)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().tag_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L56)

```python
def tag_resources(
    ResourceARNList: List[Any],
    Tags: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().untag_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/client.py#L62)

```python
def untag_resources(
    ResourceARNList: List[Any],
    TagKeys: List[Any],
) -> Dict[str, Any]:
```
