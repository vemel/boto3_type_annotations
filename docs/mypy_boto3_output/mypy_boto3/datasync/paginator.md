# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.datasync.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Datasync](index.md#datasync) / Paginator
    - [ListAgents](#listagents)
        - [ListAgents().paginate](#listagentspaginate)
    - [ListLocations](#listlocations)
        - [ListLocations().paginate](#listlocationspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)
    - [ListTaskExecutions](#listtaskexecutions)
        - [ListTaskExecutions().paginate](#listtaskexecutionspaginate)
    - [ListTasks](#listtasks)
        - [ListTasks().paginate](#listtaskspaginate)

## ListAgents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L9)

```python
class ListAgents(Paginator):
```

### ListAgents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListLocations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L16)

```python
class ListLocations(Paginator):
```

### ListLocations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L19)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L23)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L26)

```python
def paginate(
    ResourceArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTaskExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L32)

```python
class ListTaskExecutions(Paginator):
```

### ListTaskExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L35)

```python
def paginate(
    TaskArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L41)

```python
class ListTasks(Paginator):
```

### ListTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/paginator.py#L44)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
