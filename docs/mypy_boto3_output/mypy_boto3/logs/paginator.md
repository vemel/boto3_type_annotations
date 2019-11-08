# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.logs.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Logs](index.md#logs) / Paginator
    - [DescribeDestinations](#describedestinations)
        - [DescribeDestinations().paginate](#describedestinationspaginate)
    - [DescribeExportTasks](#describeexporttasks)
        - [DescribeExportTasks().paginate](#describeexporttaskspaginate)
    - [DescribeLogGroups](#describeloggroups)
        - [DescribeLogGroups().paginate](#describeloggroupspaginate)
    - [DescribeLogStreams](#describelogstreams)
        - [DescribeLogStreams().paginate](#describelogstreamspaginate)
    - [DescribeMetricFilters](#describemetricfilters)
        - [DescribeMetricFilters().paginate](#describemetricfilterspaginate)
    - [DescribeQueries](#describequeries)
        - [DescribeQueries().paginate](#describequeriespaginate)
    - [DescribeResourcePolicies](#describeresourcepolicies)
        - [DescribeResourcePolicies().paginate](#describeresourcepoliciespaginate)
    - [DescribeSubscriptionFilters](#describesubscriptionfilters)
        - [DescribeSubscriptionFilters().paginate](#describesubscriptionfilterspaginate)
    - [FilterLogEvents](#filterlogevents)
        - [FilterLogEvents().paginate](#filterlogeventspaginate)

## DescribeDestinations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L10)

```python
class DescribeDestinations(Paginator):
```

### DescribeDestinations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L13)

```python
def paginate(
    DestinationNamePrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeExportTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L19)

```python
class DescribeExportTasks(Paginator):
```

### DescribeExportTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L22)

```python
def paginate(
    taskId: str = None,
    statusCode: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeLogGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L31)

```python
class DescribeLogGroups(Paginator):
```

### DescribeLogGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L34)

```python
def paginate(
    logGroupNamePrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeLogStreams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L40)

```python
class DescribeLogStreams(Paginator):
```

### DescribeLogStreams().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L43)

```python
def paginate(
    logGroupName: str,
    logStreamNamePrefix: str = None,
    orderBy: str = None,
    descending: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeMetricFilters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L54)

```python
class DescribeMetricFilters(Paginator):
```

### DescribeMetricFilters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L57)

```python
def paginate(
    logGroupName: str = None,
    filterNamePrefix: str = None,
    metricName: str = None,
    metricNamespace: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeQueries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L68)

```python
class DescribeQueries(Paginator):
```

### DescribeQueries().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L71)

```python
def paginate(
    logGroupName: str = None,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeResourcePolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L80)

```python
class DescribeResourcePolicies(Paginator):
```

### DescribeResourcePolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L83)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeSubscriptionFilters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L87)

```python
class DescribeSubscriptionFilters(Paginator):
```

### DescribeSubscriptionFilters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L90)

```python
def paginate(
    logGroupName: str,
    filterNamePrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## FilterLogEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L99)

```python
class FilterLogEvents(Paginator):
```

### FilterLogEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/logs/paginator.py#L102)

```python
def paginate(
    logGroupName: str,
    logStreamNames: List[Any] = None,
    logStreamNamePrefix: str = None,
    startTime: int = None,
    endTime: int = None,
    filterPattern: str = None,
    interleaved: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
