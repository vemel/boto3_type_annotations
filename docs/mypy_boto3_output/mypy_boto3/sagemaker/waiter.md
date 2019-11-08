# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sagemaker.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sagemaker](index.md#sagemaker) / Waiter
    - [EndpointDeleted](#endpointdeleted)
        - [EndpointDeleted().wait](#endpointdeletedwait)
    - [EndpointInService](#endpointinservice)
        - [EndpointInService().wait](#endpointinservicewait)
    - [NotebookInstanceDeleted](#notebookinstancedeleted)
        - [NotebookInstanceDeleted().wait](#notebookinstancedeletedwait)
    - [NotebookInstanceInService](#notebookinstanceinservice)
        - [NotebookInstanceInService().wait](#notebookinstanceinservicewait)
    - [NotebookInstanceStopped](#notebookinstancestopped)
        - [NotebookInstanceStopped().wait](#notebookinstancestoppedwait)
    - [TrainingJobCompletedOrStopped](#trainingjobcompletedorstopped)
        - [TrainingJobCompletedOrStopped().wait](#trainingjobcompletedorstoppedwait)
    - [TransformJobCompletedOrStopped](#transformjobcompletedorstopped)
        - [TransformJobCompletedOrStopped().wait](#transformjobcompletedorstoppedwait)

## EndpointDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L9)

```python
class EndpointDeleted(Waiter):
```

### EndpointDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L12)

```python
def wait(EndpointName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## EndpointInService

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L16)

```python
class EndpointInService(Waiter):
```

### EndpointInService().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L19)

```python
def wait(EndpointName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## NotebookInstanceDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L23)

```python
class NotebookInstanceDeleted(Waiter):
```

### NotebookInstanceDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L26)

```python
def wait(
    NotebookInstanceName: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## NotebookInstanceInService

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L32)

```python
class NotebookInstanceInService(Waiter):
```

### NotebookInstanceInService().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L35)

```python
def wait(
    NotebookInstanceName: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## NotebookInstanceStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L41)

```python
class NotebookInstanceStopped(Waiter):
```

### NotebookInstanceStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L44)

```python
def wait(
    NotebookInstanceName: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TrainingJobCompletedOrStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L50)

```python
class TrainingJobCompletedOrStopped(Waiter):
```

### TrainingJobCompletedOrStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L53)

```python
def wait(TrainingJobName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## TransformJobCompletedOrStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L57)

```python
class TransformJobCompletedOrStopped(Waiter):
```

### TransformJobCompletedOrStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/waiter.py#L60)

```python
def wait(TransformJobName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```
