# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ds.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ds](index.md#ds) / Paginator
    - [DescribeDirectories](#describedirectories)
        - [DescribeDirectories().paginate](#describedirectoriespaginate)
    - [DescribeDomainControllers](#describedomaincontrollers)
        - [DescribeDomainControllers().paginate](#describedomaincontrollerspaginate)
    - [DescribeSharedDirectories](#describeshareddirectories)
        - [DescribeSharedDirectories().paginate](#describeshareddirectoriespaginate)
    - [DescribeSnapshots](#describesnapshots)
        - [DescribeSnapshots().paginate](#describesnapshotspaginate)
    - [DescribeTrusts](#describetrusts)
        - [DescribeTrusts().paginate](#describetrustspaginate)
    - [ListIpRoutes](#listiproutes)
        - [ListIpRoutes().paginate](#listiproutespaginate)
    - [ListLogSubscriptions](#listlogsubscriptions)
        - [ListLogSubscriptions().paginate](#listlogsubscriptionspaginate)
    - [ListSchemaExtensions](#listschemaextensions)
        - [ListSchemaExtensions().paginate](#listschemaextensionspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)

## DescribeDirectories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L10)

```python
class DescribeDirectories(Paginator):
```

### DescribeDirectories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L13)

```python
def paginate(
    DirectoryIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDomainControllers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L19)

```python
class DescribeDomainControllers(Paginator):
```

### DescribeDomainControllers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L22)

```python
def paginate(
    DirectoryId: str,
    DomainControllerIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSharedDirectories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L31)

```python
class DescribeSharedDirectories(Paginator):
```

### DescribeSharedDirectories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L34)

```python
def paginate(
    OwnerDirectoryId: str,
    SharedDirectoryIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L43)

```python
class DescribeSnapshots(Paginator):
```

### DescribeSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L46)

```python
def paginate(
    DirectoryId: str = None,
    SnapshotIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTrusts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L55)

```python
class DescribeTrusts(Paginator):
```

### DescribeTrusts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L58)

```python
def paginate(
    DirectoryId: str = None,
    TrustIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListIpRoutes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L67)

```python
class ListIpRoutes(Paginator):
```

### ListIpRoutes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L70)

```python
def paginate(
    DirectoryId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListLogSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L76)

```python
class ListLogSubscriptions(Paginator):
```

### ListLogSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L79)

```python
def paginate(
    DirectoryId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSchemaExtensions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L85)

```python
class ListSchemaExtensions(Paginator):
```

### ListSchemaExtensions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L88)

```python
def paginate(
    DirectoryId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L94)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ds/paginator.py#L97)

```python
def paginate(
    ResourceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
