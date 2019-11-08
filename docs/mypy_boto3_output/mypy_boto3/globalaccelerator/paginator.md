# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.globalaccelerator.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Globalaccelerator](index.md#globalaccelerator) / Paginator
    - [ListAccelerators](#listaccelerators)
        - [ListAccelerators().paginate](#listacceleratorspaginate)
    - [ListEndpointGroups](#listendpointgroups)
        - [ListEndpointGroups().paginate](#listendpointgroupspaginate)
    - [ListListeners](#listlisteners)
        - [ListListeners().paginate](#listlistenerspaginate)

## ListAccelerators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L9)

```python
class ListAccelerators(Paginator):
```

### ListAccelerators().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListEndpointGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L16)

```python
class ListEndpointGroups(Paginator):
```

### ListEndpointGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L19)

```python
def paginate(
    ListenerArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListListeners

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L25)

```python
class ListListeners(Paginator):
```

### ListListeners().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/globalaccelerator/paginator.py#L28)

```python
def paginate(
    AcceleratorArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
