# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.xray.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Xray](index.md#xray) / Paginator
    - [BatchGetTraces](#batchgettraces)
        - [BatchGetTraces().paginate](#batchgettracespaginate)
    - [GetGroups](#getgroups)
        - [GetGroups().paginate](#getgroupspaginate)
    - [GetSamplingRules](#getsamplingrules)
        - [GetSamplingRules().paginate](#getsamplingrulespaginate)
    - [GetSamplingStatisticSummaries](#getsamplingstatisticsummaries)
        - [GetSamplingStatisticSummaries().paginate](#getsamplingstatisticsummariespaginate)
    - [GetServiceGraph](#getservicegraph)
        - [GetServiceGraph().paginate](#getservicegraphpaginate)
    - [GetTimeSeriesServiceStatistics](#gettimeseriesservicestatistics)
        - [GetTimeSeriesServiceStatistics().paginate](#gettimeseriesservicestatisticspaginate)
    - [GetTraceGraph](#gettracegraph)
        - [GetTraceGraph().paginate](#gettracegraphpaginate)
    - [GetTraceSummaries](#gettracesummaries)
        - [GetTraceSummaries().paginate](#gettracesummariespaginate)

## BatchGetTraces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L11)

```python
class BatchGetTraces(Paginator):
```

### BatchGetTraces().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L14)

```python
def paginate(
    TraceIds: List[Any],
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L20)

```python
class GetGroups(Paginator):
```

### GetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L23)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetSamplingRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L27)

```python
class GetSamplingRules(Paginator):
```

### GetSamplingRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L30)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetSamplingStatisticSummaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L34)

```python
class GetSamplingStatisticSummaries(Paginator):
```

### GetSamplingStatisticSummaries().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L37)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetServiceGraph

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L41)

```python
class GetServiceGraph(Paginator):
```

### GetServiceGraph().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L44)

```python
def paginate(
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTimeSeriesServiceStatistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L55)

```python
class GetTimeSeriesServiceStatistics(Paginator):
```

### GetTimeSeriesServiceStatistics().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L58)

```python
def paginate(
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    EntitySelectorExpression: str = None,
    Period: int = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTraceGraph

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L71)

```python
class GetTraceGraph(Paginator):
```

### GetTraceGraph().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L74)

```python
def paginate(
    TraceIds: List[Any],
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTraceSummaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L80)

```python
class GetTraceSummaries(Paginator):
```

### GetTraceSummaries().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/paginator.py#L83)

```python
def paginate(
    StartTime: datetime,
    EndTime: datetime,
    TimeRangeType: str = None,
    Sampling: bool = None,
    SamplingStrategy: Dict[str, Any] = None,
    FilterExpression: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
