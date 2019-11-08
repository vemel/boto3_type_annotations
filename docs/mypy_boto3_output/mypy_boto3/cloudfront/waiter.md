# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudfront.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudfront](index.md#cloudfront) / Waiter
    - [DistributionDeployed](#distributiondeployed)
        - [DistributionDeployed().wait](#distributiondeployedwait)
    - [InvalidationCompleted](#invalidationcompleted)
        - [InvalidationCompleted().wait](#invalidationcompletedwait)
    - [StreamingDistributionDeployed](#streamingdistributiondeployed)
        - [StreamingDistributionDeployed().wait](#streamingdistributiondeployedwait)

## DistributionDeployed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L9)

```python
class DistributionDeployed(Waiter):
```

### DistributionDeployed().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L12)

```python
def wait(Id: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## InvalidationCompleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L16)

```python
class InvalidationCompleted(Waiter):
```

### InvalidationCompleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L19)

```python
def wait(
    DistributionId: str,
    Id: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StreamingDistributionDeployed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L25)

```python
class StreamingDistributionDeployed(Waiter):
```

### StreamingDistributionDeployed().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/waiter.py#L28)

```python
def wait(Id: str, WaiterConfig: Dict[str, Any] = None) -> None:
```
