# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.storagegateway.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Storagegateway](index.md#storagegateway) / Paginator
    - [DescribeTapeArchives](#describetapearchives)
        - [DescribeTapeArchives().paginate](#describetapearchivespaginate)
    - [DescribeTapeRecoveryPoints](#describetaperecoverypoints)
        - [DescribeTapeRecoveryPoints().paginate](#describetaperecoverypointspaginate)
    - [DescribeTapes](#describetapes)
        - [DescribeTapes().paginate](#describetapespaginate)
    - [DescribeVTLDevices](#describevtldevices)
        - [DescribeVTLDevices().paginate](#describevtldevicespaginate)
    - [ListFileShares](#listfileshares)
        - [ListFileShares().paginate](#listfilesharespaginate)
    - [ListGateways](#listgateways)
        - [ListGateways().paginate](#listgatewayspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)
    - [ListTapes](#listtapes)
        - [ListTapes().paginate](#listtapespaginate)
    - [ListVolumes](#listvolumes)
        - [ListVolumes().paginate](#listvolumespaginate)

## DescribeTapeArchives

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L10)

```python
class DescribeTapeArchives(Paginator):
```

### DescribeTapeArchives().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L13)

```python
def paginate(
    TapeARNs: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTapeRecoveryPoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L19)

```python
class DescribeTapeRecoveryPoints(Paginator):
```

### DescribeTapeRecoveryPoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L22)

```python
def paginate(
    GatewayARN: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTapes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L28)

```python
class DescribeTapes(Paginator):
```

### DescribeTapes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L31)

```python
def paginate(
    GatewayARN: str,
    TapeARNs: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeVTLDevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L40)

```python
class DescribeVTLDevices(Paginator):
```

### DescribeVTLDevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L43)

```python
def paginate(
    GatewayARN: str,
    VTLDeviceARNs: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListFileShares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L52)

```python
class ListFileShares(Paginator):
```

### ListFileShares().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L55)

```python
def paginate(
    GatewayARN: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L61)

```python
class ListGateways(Paginator):
```

### ListGateways().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L64)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L68)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L71)

```python
def paginate(
    ResourceARN: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTapes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L77)

```python
class ListTapes(Paginator):
```

### ListTapes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L80)

```python
def paginate(
    TapeARNs: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListVolumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L86)

```python
class ListVolumes(Paginator):
```

### ListVolumes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/paginator.py#L89)

```python
def paginate(
    GatewayARN: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
