# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesis.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesis](index.md#kinesis) / Paginator
    - [DescribeStream](#describestream)
        - [DescribeStream().paginate](#describestreampaginate)
    - [ListShards](#listshards)
        - [ListShards().paginate](#listshardspaginate)
    - [ListStreamConsumers](#liststreamconsumers)
        - [ListStreamConsumers().paginate](#liststreamconsumerspaginate)
    - [ListStreams](#liststreams)
        - [ListStreams().paginate](#liststreamspaginate)

## DescribeStream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L10)

```python
class DescribeStream(Paginator):
```

### DescribeStream().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L13)

```python
def paginate(
    StreamName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListShards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L19)

```python
class ListShards(Paginator):
```

### ListShards().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L22)

```python
def paginate(
    StreamName: str = None,
    ExclusiveStartShardId: str = None,
    StreamCreationTimestamp: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStreamConsumers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L32)

```python
class ListStreamConsumers(Paginator):
```

### ListStreamConsumers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L35)

```python
def paginate(
    StreamARN: str,
    StreamCreationTimestamp: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStreams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L44)

```python
class ListStreams(Paginator):
```

### ListStreams().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/paginator.py#L47)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
