# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.medialive.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Medialive](index.md#medialive) / Waiter
    - [ChannelCreated](#channelcreated)
        - [ChannelCreated().wait](#channelcreatedwait)
    - [ChannelDeleted](#channeldeleted)
        - [ChannelDeleted().wait](#channeldeletedwait)
    - [ChannelRunning](#channelrunning)
        - [ChannelRunning().wait](#channelrunningwait)
    - [ChannelStopped](#channelstopped)
        - [ChannelStopped().wait](#channelstoppedwait)

## ChannelCreated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L9)

```python
class ChannelCreated(Waiter):
```

### ChannelCreated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L12)

```python
def wait(ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ChannelDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L16)

```python
class ChannelDeleted(Waiter):
```

### ChannelDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L19)

```python
def wait(ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ChannelRunning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L23)

```python
class ChannelRunning(Waiter):
```

### ChannelRunning().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L26)

```python
def wait(ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ChannelStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L30)

```python
class ChannelStopped(Waiter):
```

### ChannelStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/medialive/waiter.py#L33)

```python
def wait(ChannelId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```
