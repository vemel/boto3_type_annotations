# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codestar.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codestar](index.md#codestar) / Paginator
    - [ListProjects](#listprojects)
        - [ListProjects().paginate](#listprojectspaginate)
    - [ListResources](#listresources)
        - [ListResources().paginate](#listresourcespaginate)
    - [ListTeamMembers](#listteammembers)
        - [ListTeamMembers().paginate](#listteammemberspaginate)
    - [ListUserProfiles](#listuserprofiles)
        - [ListUserProfiles().paginate](#listuserprofilespaginate)

## ListProjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L9)

```python
class ListProjects(Paginator):
```

### ListProjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L16)

```python
class ListResources(Paginator):
```

### ListResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L19)

```python
def paginate(
    projectId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTeamMembers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L25)

```python
class ListTeamMembers(Paginator):
```

### ListTeamMembers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L28)

```python
def paginate(
    projectId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUserProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L34)

```python
class ListUserProfiles(Paginator):
```

### ListUserProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar/paginator.py#L37)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
