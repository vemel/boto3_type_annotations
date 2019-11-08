# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.servicediscovery.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Servicediscovery](index.md#servicediscovery) / Paginator
    - [ListInstances](#listinstances)
        - [ListInstances().paginate](#listinstancespaginate)
    - [ListNamespaces](#listnamespaces)
        - [ListNamespaces().paginate](#listnamespacespaginate)
    - [ListOperations](#listoperations)
        - [ListOperations().paginate](#listoperationspaginate)
    - [ListServices](#listservices)
        - [ListServices().paginate](#listservicespaginate)

## ListInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L10)

```python
class ListInstances(Paginator):
```

### ListInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L13)

```python
def paginate(
    ServiceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListNamespaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L19)

```python
class ListNamespaces(Paginator):
```

### ListNamespaces().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L22)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOperations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L28)

```python
class ListOperations(Paginator):
```

### ListOperations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L31)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L37)

```python
class ListServices(Paginator):
```

### ListServices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/paginator.py#L40)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
