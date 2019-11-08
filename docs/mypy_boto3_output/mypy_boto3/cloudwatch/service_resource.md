# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudwatch.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudwatch](index.md#cloudwatch) / ServiceResource
    - [Alarm](#alarm)
        - [Alarm().delete](#alarmdelete)
        - [Alarm().describe_history](#alarmdescribe_history)
        - [Alarm().disable_actions](#alarmdisable_actions)
        - [Alarm().enable_actions](#alarmenable_actions)
        - [Alarm().get_available_subresources](#alarmget_available_subresources)
        - [Alarm().load](#alarmload)
        - [Alarm().reload](#alarmreload)
        - [Alarm().set_state](#alarmset_state)
    - [Metric](#metric)
        - [Metric().get_available_subresources](#metricget_available_subresources)
        - [Metric().get_statistics](#metricget_statistics)
        - [Metric().load](#metricload)
        - [Metric().put_alarm](#metricput_alarm)
        - [Metric().put_data](#metricput_data)
        - [Metric().reload](#metricreload)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Alarm](#serviceresourcealarm)
        - [ServiceResource().Metric](#serviceresourcemetric)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [alarms](#alarms)
        - [alarms.all](#alarmsall)
        - [alarms.delete](#alarmsdelete)
        - [alarms.disable_actions](#alarmsdisable_actions)
        - [alarms.enable_actions](#alarmsenable_actions)
        - [alarms.filter](#alarmsfilter)
        - [alarms.iterator](#alarmsiterator)
        - [alarms.limit](#alarmslimit)
        - [alarms.page_size](#alarmspage_size)
        - [alarms.pages](#alarmspages)
    - [metrics](#metrics)
        - [metrics.all](#metricsall)
        - [metrics.filter](#metricsfilter)
        - [metrics.iterator](#metricsiterator)
        - [metrics.limit](#metricslimit)
        - [metrics.page_size](#metricspage_size)
        - [metrics.pages](#metricspages)

## Alarm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L34)

```python
class Alarm(Boto3ServiceResource):
```

### Alarm().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L65)

```python
def delete() -> None:
```

### Alarm().describe_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L69)

```python
def describe_history(
    HistoryItemType: str = None,
    StartDate: datetime = None,
    EndDate: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Alarm().disable_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L80)

```python
def disable_actions() -> None:
```

### Alarm().enable_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L84)

```python
def enable_actions() -> None:
```

### Alarm().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L88)

```python
def get_available_subresources() -> List[str]:
```

### Alarm().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L92)

```python
def load() -> None:
```

### Alarm().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L96)

```python
def reload() -> None:
```

### Alarm().set_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L100)

```python
def set_state(
    StateValue: str,
    StateReason: str,
    StateReasonData: str = None,
) -> None:
```

## Metric

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L106)

```python
class Metric(Boto3ServiceResource):
```

### Metric().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L114)

```python
def get_available_subresources() -> List[str]:
```

### Metric().get_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L118)

```python
def get_statistics(
    StartTime: datetime,
    EndTime: datetime,
    Period: int,
    Dimensions: List[Any] = None,
    Statistics: List[Any] = None,
    ExtendedStatistics: List[Any] = None,
    Unit: str = None,
) -> Dict[str, Any]:
```

### Metric().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L131)

```python
def load() -> None:
```

### Metric().put_alarm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L135)

```python
def put_alarm(
    AlarmName: str,
    EvaluationPeriods: int,
    ComparisonOperator: str,
    AlarmDescription: str = None,
    ActionsEnabled: bool = None,
    OKActions: List[Any] = None,
    AlarmActions: List[Any] = None,
    InsufficientDataActions: List[Any] = None,
    Statistic: str = None,
    ExtendedStatistic: str = None,
    Dimensions: List[Any] = None,
    Period: int = None,
    Unit: str = None,
    DatapointsToAlarm: int = None,
    Threshold: float = None,
    TreatMissingData: str = None,
    EvaluateLowSampleCountPercentile: str = None,
    Metrics: List[Any] = None,
    Tags: List[Any] = None,
    ThresholdMetricId: str = None,
) -> cloudwatch_service_resource_scope.Alarm:
```

### Metric().put_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L161)

```python
def put_data() -> None:
```

### Metric().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L165)

```python
def reload() -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L15)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Alarm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L20)

```python
def Alarm(name: str = None) -> cloudwatch_service_resource_scope.Alarm:
```

### ServiceResource().Metric

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L24)

```python
def Metric(
    namespace: str = None,
    name: str = None,
) -> cloudwatch_service_resource_scope.Metric:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L30)

```python
def get_available_subresources() -> List[str]:
```

## alarms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L169)

```python
class alarms(ResourceCollection):
```

### alarms.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L170)

```python
@classmethod
def all() -> List[cloudwatch_service_resource_scope.Alarm]:
```

### alarms.delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L175)

```python
@classmethod
def delete() -> None:
```

### alarms.disable_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L180)

```python
@classmethod
def disable_actions() -> None:
```

### alarms.enable_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L185)

```python
@classmethod
def enable_actions() -> None:
```

### alarms.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L190)

```python
@classmethod
def filter(
    AlarmNames: List[Any] = None,
    AlarmNamePrefix: str = None,
    StateValue: str = None,
    ActionPrefix: str = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> List[cloudwatch_service_resource_scope.Alarm]:
```

### alarms.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L203)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### alarms.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L208)

```python
@classmethod
def limit(count: int = None) -> List[cloudwatch_service_resource_scope.Alarm]:
```

### alarms.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L213)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[cloudwatch_service_resource_scope.Alarm]:
```

### alarms.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L220)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L226)

```python
class metrics(ResourceCollection):
```

### metrics.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L227)

```python
@classmethod
def all() -> List[cloudwatch_service_resource_scope.Metric]:
```

### metrics.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L232)

```python
@classmethod
def filter(
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List[Any] = None,
    NextToken: str = None,
) -> List[cloudwatch_service_resource_scope.Metric]:
```

### metrics.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L243)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### metrics.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L248)

```python
@classmethod
def limit(
    count: int = None,
) -> List[cloudwatch_service_resource_scope.Metric]:
```

### metrics.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L253)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[cloudwatch_service_resource_scope.Metric]:
```

### metrics.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/service_resource.py#L260)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
