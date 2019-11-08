# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.health.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Health](index.md#health) / Paginator
    - [DescribeAffectedEntities](#describeaffectedentities)
        - [DescribeAffectedEntities().paginate](#describeaffectedentitiespaginate)
    - [DescribeEventAggregates](#describeeventaggregates)
        - [DescribeEventAggregates().paginate](#describeeventaggregatespaginate)
    - [DescribeEventTypes](#describeeventtypes)
        - [DescribeEventTypes().paginate](#describeeventtypespaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)

## DescribeAffectedEntities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L9)

```python
class DescribeAffectedEntities(Paginator):
```

### DescribeAffectedEntities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L12)

```python
def paginate(
    filter: Dict[str, Any],
    locale: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventAggregates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L21)

```python
class DescribeEventAggregates(Paginator):
```

### DescribeEventAggregates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L24)

```python
def paginate(
    aggregateField: str,
    filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L33)

```python
class DescribeEventTypes(Paginator):
```

### DescribeEventTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L36)

```python
def paginate(
    filter: Dict[str, Any] = None,
    locale: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L45)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/health/paginator.py#L48)

```python
def paginate(
    filter: Dict[str, Any] = None,
    locale: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
