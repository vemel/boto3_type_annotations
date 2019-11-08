# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.resource_groups.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Resource Groups](index.md#resource-groups) / Paginator
    - [ListGroupResources](#listgroupresources)
        - [ListGroupResources().paginate](#listgroupresourcespaginate)
    - [ListGroups](#listgroups)
        - [ListGroups().paginate](#listgroupspaginate)
    - [SearchResources](#searchresources)
        - [SearchResources().paginate](#searchresourcespaginate)

## ListGroupResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L10)

```python
class ListGroupResources(Paginator):
```

### ListGroupResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L13)

```python
def paginate(
    GroupName: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L22)

```python
class ListGroups(Paginator):
```

### ListGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L25)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L31)

```python
class SearchResources(Paginator):
```

### SearchResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resource_groups/paginator.py#L34)

```python
def paginate(
    ResourceQuery: Dict[str, Any],
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
