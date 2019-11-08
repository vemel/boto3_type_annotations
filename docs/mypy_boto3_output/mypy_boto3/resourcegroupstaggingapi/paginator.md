# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.resourcegroupstaggingapi.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Resourcegroupstaggingapi](index.md#resourcegroupstaggingapi) / Paginator
    - [GetResources](#getresources)
        - [GetResources().paginate](#getresourcespaginate)
    - [GetTagKeys](#gettagkeys)
        - [GetTagKeys().paginate](#gettagkeyspaginate)
    - [GetTagValues](#gettagvalues)
        - [GetTagValues().paginate](#gettagvaluespaginate)

## GetResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L10)

```python
class GetResources(Paginator):
```

### GetResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L13)

```python
def paginate(
    TagFilters: List[Any] = None,
    TagsPerPage: int = None,
    ResourceTypeFilters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTagKeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L23)

```python
class GetTagKeys(Paginator):
```

### GetTagKeys().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L26)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetTagValues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L30)

```python
class GetTagValues(Paginator):
```

### GetTagValues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/resourcegroupstaggingapi/paginator.py#L33)

```python
def paginate(
    Key: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
