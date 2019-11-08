# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.snowball.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Snowball](index.md#snowball) / Paginator
    - [DescribeAddresses](#describeaddresses)
        - [DescribeAddresses().paginate](#describeaddressespaginate)
    - [ListClusterJobs](#listclusterjobs)
        - [ListClusterJobs().paginate](#listclusterjobspaginate)
    - [ListClusters](#listclusters)
        - [ListClusters().paginate](#listclusterspaginate)
    - [ListCompatibleImages](#listcompatibleimages)
        - [ListCompatibleImages().paginate](#listcompatibleimagespaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)

## DescribeAddresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L9)

```python
class DescribeAddresses(Paginator):
```

### DescribeAddresses().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListClusterJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L16)

```python
class ListClusterJobs(Paginator):
```

### ListClusterJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L19)

```python
def paginate(
    ClusterId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L25)

```python
class ListClusters(Paginator):
```

### ListClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListCompatibleImages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L32)

```python
class ListCompatibleImages(Paginator):
```

### ListCompatibleImages().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L35)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L39)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/snowball/paginator.py#L42)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
