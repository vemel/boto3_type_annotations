# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudwatch.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudwatch](index.md#cloudwatch) / Paginator
    - [DescribeAlarmHistory](#describealarmhistory)
        - [DescribeAlarmHistory().paginate](#describealarmhistorypaginate)
    - [DescribeAlarms](#describealarms)
        - [DescribeAlarms().paginate](#describealarmspaginate)
    - [GetMetricData](#getmetricdata)
        - [GetMetricData().paginate](#getmetricdatapaginate)
    - [ListDashboards](#listdashboards)
        - [ListDashboards().paginate](#listdashboardspaginate)
    - [ListMetrics](#listmetrics)
        - [ListMetrics().paginate](#listmetricspaginate)

## DescribeAlarmHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L11)

```python
class DescribeAlarmHistory(Paginator):
```

### DescribeAlarmHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L14)

```python
def paginate(
    AlarmName: str = None,
    HistoryItemType: str = None,
    StartDate: datetime = None,
    EndDate: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeAlarms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L25)

```python
class DescribeAlarms(Paginator):
```

### DescribeAlarms().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L28)

```python
def paginate(
    AlarmNames: List[Any] = None,
    AlarmNamePrefix: str = None,
    StateValue: str = None,
    ActionPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetMetricData

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L39)

```python
class GetMetricData(Paginator):
```

### GetMetricData().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L42)

```python
def paginate(
    MetricDataQueries: List[Any],
    StartTime: datetime,
    EndTime: datetime,
    ScanBy: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDashboards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L53)

```python
class ListDashboards(Paginator):
```

### ListDashboards().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L56)

```python
def paginate(
    DashboardNamePrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMetrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L62)

```python
class ListMetrics(Paginator):
```

### ListMetrics().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/paginator.py#L65)

```python
def paginate(
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
