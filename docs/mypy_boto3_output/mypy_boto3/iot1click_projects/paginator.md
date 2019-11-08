# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot1click_projects.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot1click Projects](index.md#iot1click-projects) / Paginator
    - [ListPlacements](#listplacements)
        - [ListPlacements().paginate](#listplacementspaginate)
    - [ListProjects](#listprojects)
        - [ListProjects().paginate](#listprojectspaginate)

## ListPlacements

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/paginator.py#L9)

```python
class ListPlacements(Paginator):
```

### ListPlacements().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/paginator.py#L12)

```python
def paginate(
    projectName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListProjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/paginator.py#L18)

```python
class ListProjects(Paginator):
```

### ListProjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot1click_projects/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
