# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.resource_groups.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Resource Groups](index.md#resource-groups) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_group](#clientcreate_group)
        - [Client().delete_group](#clientdelete_group)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_group](#clientget_group)
        - [Client().get_group_query](#clientget_group_query)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_tags](#clientget_tags)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_group_resources](#clientlist_group_resources)
        - [Client().list_groups](#clientlist_groups)
        - [Client().search_resources](#clientsearch_resources)
        - [Client().tag](#clienttag)
        - [Client().untag](#clientuntag)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_group_query](#clientupdate_group_query)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L19)

```python
def create_group(
    Name: str,
    ResourceQuery: Dict[str, Any],
    Description: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L29)

```python
def delete_group(GroupName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L33)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L43)

```python
def get_group(GroupName: str) -> Dict[str, Any]:
```

### Client().get_group_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L47)

```python
def get_group_query(GroupName: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L51)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L55)

```python
def get_tags(Arn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L59)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_group_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L63)

```python
def list_group_resources(
    GroupName: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L73)

```python
def list_groups(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().search_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L79)

```python
def search_resources(
    ResourceQuery: Dict[str, Any],
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L88)

```python
def tag(Arn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L92)

```python
def untag(Arn: str, Keys: List[Any]) -> Dict[str, Any]:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L96)

```python
def update_group(GroupName: str, Description: str = None) -> Dict[str, Any]:
```

### Client().update_group_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/client.py#L100)

```python
def update_group_query(
    GroupName: str,
    ResourceQuery: Dict[str, Any],
) -> Dict[str, Any]:
```
