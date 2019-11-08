# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworkscm.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworkscm](index.md#opsworkscm) / Waiter
    - [NodeAssociated](#nodeassociated)
        - [NodeAssociated().wait](#nodeassociatedwait)

## NodeAssociated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/waiter.py#L9)

```python
class NodeAssociated(Waiter):
```

### NodeAssociated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/waiter.py#L12)

```python
def wait(
    NodeAssociationStatusToken: str,
    ServerName: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
