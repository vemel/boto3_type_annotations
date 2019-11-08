# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudtrail.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudtrail](index.md#cloudtrail) / Paginator
    - [ListPublicKeys](#listpublickeys)
        - [ListPublicKeys().paginate](#listpublickeyspaginate)
    - [ListTags](#listtags)
        - [ListTags().paginate](#listtagspaginate)
    - [ListTrails](#listtrails)
        - [ListTrails().paginate](#listtrailspaginate)
    - [LookupEvents](#lookupevents)
        - [LookupEvents().paginate](#lookupeventspaginate)

## ListPublicKeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L11)

```python
class ListPublicKeys(Paginator):
```

### ListPublicKeys().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L14)

```python
def paginate(
    StartTime: datetime = None,
    EndTime: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L23)

```python
class ListTags(Paginator):
```

### ListTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L26)

```python
def paginate(
    ResourceIdList: List[Any],
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTrails

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L32)

```python
class ListTrails(Paginator):
```

### ListTrails().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L35)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## LookupEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L39)

```python
class LookupEvents(Paginator):
```

### LookupEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudtrail/paginator.py#L42)

```python
def paginate(
    LookupAttributes: List[Any] = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
