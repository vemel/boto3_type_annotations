# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ecr.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ecr](index.md#ecr) / Paginator
    - [DescribeImageScanFindings](#describeimagescanfindings)
        - [DescribeImageScanFindings().paginate](#describeimagescanfindingspaginate)
    - [DescribeImages](#describeimages)
        - [DescribeImages().paginate](#describeimagespaginate)
    - [DescribeRepositories](#describerepositories)
        - [DescribeRepositories().paginate](#describerepositoriespaginate)
    - [GetLifecyclePolicyPreview](#getlifecyclepolicypreview)
        - [GetLifecyclePolicyPreview().paginate](#getlifecyclepolicypreviewpaginate)
    - [ListImages](#listimages)
        - [ListImages().paginate](#listimagespaginate)

## DescribeImageScanFindings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L10)

```python
class DescribeImageScanFindings(Paginator):
```

### DescribeImageScanFindings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L13)

```python
def paginate(
    repositoryName: str,
    imageId: Dict[str, Any],
    registryId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeImages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L23)

```python
class DescribeImages(Paginator):
```

### DescribeImages().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L26)

```python
def paginate(
    repositoryName: str,
    registryId: str = None,
    imageIds: List[Any] = None,
    filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeRepositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L37)

```python
class DescribeRepositories(Paginator):
```

### DescribeRepositories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L40)

```python
def paginate(
    registryId: str = None,
    repositoryNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetLifecyclePolicyPreview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L49)

```python
class GetLifecyclePolicyPreview(Paginator):
```

### GetLifecyclePolicyPreview().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L52)

```python
def paginate(
    repositoryName: str,
    registryId: str = None,
    imageIds: List[Any] = None,
    filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListImages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L63)

```python
class ListImages(Paginator):
```

### ListImages().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/paginator.py#L66)

```python
def paginate(
    repositoryName: str,
    registryId: str = None,
    filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
