# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.serverlessrepo.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Serverlessrepo](index.md#serverlessrepo) / Paginator
    - [ListApplicationDependencies](#listapplicationdependencies)
        - [ListApplicationDependencies().paginate](#listapplicationdependenciespaginate)
    - [ListApplicationVersions](#listapplicationversions)
        - [ListApplicationVersions().paginate](#listapplicationversionspaginate)
    - [ListApplications](#listapplications)
        - [ListApplications().paginate](#listapplicationspaginate)

## ListApplicationDependencies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L9)

```python
class ListApplicationDependencies(Paginator):
```

### ListApplicationDependencies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L12)

```python
def paginate(
    ApplicationId: str,
    SemanticVersion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListApplicationVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L21)

```python
class ListApplicationVersions(Paginator):
```

### ListApplicationVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L24)

```python
def paginate(
    ApplicationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListApplications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L30)

```python
class ListApplications(Paginator):
```

### ListApplications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/serverlessrepo/paginator.py#L33)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
