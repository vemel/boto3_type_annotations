# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iam.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iam](index.md#iam) / Waiter
    - [InstanceProfileExists](#instanceprofileexists)
        - [InstanceProfileExists().wait](#instanceprofileexistswait)
    - [PolicyExists](#policyexists)
        - [PolicyExists().wait](#policyexistswait)
    - [RoleExists](#roleexists)
        - [RoleExists().wait](#roleexistswait)
    - [UserExists](#userexists)
        - [UserExists().wait](#userexistswait)

## InstanceProfileExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L9)

```python
class InstanceProfileExists(Waiter):
```

### InstanceProfileExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L12)

```python
def wait(
    InstanceProfileName: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## PolicyExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L18)

```python
class PolicyExists(Waiter):
```

### PolicyExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L21)

```python
def wait(PolicyArn: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## RoleExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L25)

```python
class RoleExists(Waiter):
```

### RoleExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L28)

```python
def wait(RoleName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## UserExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L32)

```python
class UserExists(Waiter):
```

### UserExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/waiter.py#L35)

```python
def wait(UserName: str = None, WaiterConfig: Dict[str, Any] = None) -> None:
```
