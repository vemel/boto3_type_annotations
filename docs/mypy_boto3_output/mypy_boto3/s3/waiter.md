# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.s3.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [S3](index.md#s3) / Waiter
    - [BucketExists](#bucketexists)
        - [BucketExists().wait](#bucketexistswait)
    - [BucketNotExists](#bucketnotexists)
        - [BucketNotExists().wait](#bucketnotexistswait)
    - [ObjectExists](#objectexists)
        - [ObjectExists().wait](#objectexistswait)
    - [ObjectNotExists](#objectnotexists)
        - [ObjectNotExists().wait](#objectnotexistswait)

## BucketExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L10)

```python
class BucketExists(Waiter):
```

### BucketExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L13)

```python
def wait(Bucket: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## BucketNotExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L17)

```python
class BucketNotExists(Waiter):
```

### BucketNotExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L20)

```python
def wait(Bucket: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ObjectExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L24)

```python
class ObjectExists(Waiter):
```

### ObjectExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L27)

```python
def wait(
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ObjectNotExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L47)

```python
class ObjectNotExists(Waiter):
```

### ObjectNotExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/waiter.py#L50)

```python
def wait(
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
