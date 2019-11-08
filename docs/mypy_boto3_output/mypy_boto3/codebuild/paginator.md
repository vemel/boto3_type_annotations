# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codebuild.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codebuild](index.md#codebuild) / Paginator
    - [ListBuilds](#listbuilds)
        - [ListBuilds().paginate](#listbuildspaginate)
    - [ListBuildsForProject](#listbuildsforproject)
        - [ListBuildsForProject().paginate](#listbuildsforprojectpaginate)
    - [ListProjects](#listprojects)
        - [ListProjects().paginate](#listprojectspaginate)

## ListBuilds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L9)

```python
class ListBuilds(Paginator):
```

### ListBuilds().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L12)

```python
def paginate(
    sortOrder: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListBuildsForProject

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L18)

```python
class ListBuildsForProject(Paginator):
```

### ListBuildsForProject().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L21)

```python
def paginate(
    projectName: str,
    sortOrder: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListProjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L30)

```python
class ListProjects(Paginator):
```

### ListProjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/paginator.py#L33)

```python
def paginate(
    sortBy: str = None,
    sortOrder: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
