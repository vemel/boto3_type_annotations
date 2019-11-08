# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudformation.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudformation](index.md#cloudformation) / Waiter
    - [ChangeSetCreateComplete](#changesetcreatecomplete)
        - [ChangeSetCreateComplete().wait](#changesetcreatecompletewait)
    - [StackCreateComplete](#stackcreatecomplete)
        - [StackCreateComplete().wait](#stackcreatecompletewait)
    - [StackDeleteComplete](#stackdeletecomplete)
        - [StackDeleteComplete().wait](#stackdeletecompletewait)
    - [StackExists](#stackexists)
        - [StackExists().wait](#stackexistswait)
    - [StackUpdateComplete](#stackupdatecomplete)
        - [StackUpdateComplete().wait](#stackupdatecompletewait)

## ChangeSetCreateComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L9)

```python
class ChangeSetCreateComplete(Waiter):
```

### ChangeSetCreateComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L12)

```python
def wait(
    ChangeSetName: str,
    StackName: str = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StackCreateComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L22)

```python
class StackCreateComplete(Waiter):
```

### StackCreateComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L25)

```python
def wait(
    StackName: str = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StackDeleteComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L34)

```python
class StackDeleteComplete(Waiter):
```

### StackDeleteComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L37)

```python
def wait(
    StackName: str = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StackExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L46)

```python
class StackExists(Waiter):
```

### StackExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L49)

```python
def wait(
    StackName: str = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StackUpdateComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L58)

```python
class StackUpdateComplete(Waiter):
```

### StackUpdateComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/waiter.py#L61)

```python
def wait(
    StackName: str = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
