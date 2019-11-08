# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.signer.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Signer](index.md#signer) / Paginator
    - [ListSigningJobs](#listsigningjobs)
        - [ListSigningJobs().paginate](#listsigningjobspaginate)
    - [ListSigningPlatforms](#listsigningplatforms)
        - [ListSigningPlatforms().paginate](#listsigningplatformspaginate)
    - [ListSigningProfiles](#listsigningprofiles)
        - [ListSigningProfiles().paginate](#listsigningprofilespaginate)

## ListSigningJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L9)

```python
class ListSigningJobs(Paginator):
```

### ListSigningJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L12)

```python
def paginate(
    status: str = None,
    platformId: str = None,
    requestedBy: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSigningPlatforms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L22)

```python
class ListSigningPlatforms(Paginator):
```

### ListSigningPlatforms().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L25)

```python
def paginate(
    category: str = None,
    partner: str = None,
    target: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSigningProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L35)

```python
class ListSigningProfiles(Paginator):
```

### ListSigningProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/signer/paginator.py#L38)

```python
def paginate(
    includeCanceled: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
