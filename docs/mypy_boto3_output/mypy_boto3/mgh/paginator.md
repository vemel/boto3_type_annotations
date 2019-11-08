# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mgh.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mgh](index.md#mgh) / Paginator
    - [ListCreatedArtifacts](#listcreatedartifacts)
        - [ListCreatedArtifacts().paginate](#listcreatedartifactspaginate)
    - [ListDiscoveredResources](#listdiscoveredresources)
        - [ListDiscoveredResources().paginate](#listdiscoveredresourcespaginate)
    - [ListMigrationTasks](#listmigrationtasks)
        - [ListMigrationTasks().paginate](#listmigrationtaskspaginate)
    - [ListProgressUpdateStreams](#listprogressupdatestreams)
        - [ListProgressUpdateStreams().paginate](#listprogressupdatestreamspaginate)

## ListCreatedArtifacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L9)

```python
class ListCreatedArtifacts(Paginator):
```

### ListCreatedArtifacts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L12)

```python
def paginate(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDiscoveredResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L21)

```python
class ListDiscoveredResources(Paginator):
```

### ListDiscoveredResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L24)

```python
def paginate(
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMigrationTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L33)

```python
class ListMigrationTasks(Paginator):
```

### ListMigrationTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L36)

```python
def paginate(
    ResourceName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListProgressUpdateStreams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L42)

```python
class ListProgressUpdateStreams(Paginator):
```

### ListProgressUpdateStreams().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mgh/paginator.py#L45)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
