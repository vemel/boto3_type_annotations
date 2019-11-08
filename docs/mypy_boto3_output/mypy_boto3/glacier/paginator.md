# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.glacier.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Glacier](index.md#glacier) / Paginator
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)
    - [ListMultipartUploads](#listmultipartuploads)
        - [ListMultipartUploads().paginate](#listmultipartuploadspaginate)
    - [ListParts](#listparts)
        - [ListParts().paginate](#listpartspaginate)
    - [ListVaults](#listvaults)
        - [ListVaults().paginate](#listvaultspaginate)

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L9)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L12)

```python
def paginate(
    vaultName: str,
    accountId: str = None,
    statuscode: str = None,
    completed: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMultipartUploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L23)

```python
class ListMultipartUploads(Paginator):
```

### ListMultipartUploads().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L26)

```python
def paginate(
    vaultName: str,
    accountId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListParts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L35)

```python
class ListParts(Paginator):
```

### ListParts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L38)

```python
def paginate(
    vaultName: str,
    uploadId: str,
    accountId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListVaults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L48)

```python
class ListVaults(Paginator):
```

### ListVaults().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/paginator.py#L51)

```python
def paginate(
    accountId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
