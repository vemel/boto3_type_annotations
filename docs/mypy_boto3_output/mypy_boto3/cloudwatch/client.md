# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudwatch.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudwatch](index.md#cloudwatch) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_alarms](#clientdelete_alarms)
        - [Client().delete_anomaly_detector](#clientdelete_anomaly_detector)
        - [Client().delete_dashboards](#clientdelete_dashboards)
        - [Client().describe_alarm_history](#clientdescribe_alarm_history)
        - [Client().describe_alarms](#clientdescribe_alarms)
        - [Client().describe_alarms_for_metric](#clientdescribe_alarms_for_metric)
        - [Client().describe_anomaly_detectors](#clientdescribe_anomaly_detectors)
        - [Client().disable_alarm_actions](#clientdisable_alarm_actions)
        - [Client().enable_alarm_actions](#clientenable_alarm_actions)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_dashboard](#clientget_dashboard)
        - [Client().get_metric_data](#clientget_metric_data)
        - [Client().get_metric_statistics](#clientget_metric_statistics)
        - [Client().get_metric_widget_image](#clientget_metric_widget_image)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_dashboards](#clientlist_dashboards)
        - [Client().list_metrics](#clientlist_metrics)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_anomaly_detector](#clientput_anomaly_detector)
        - [Client().put_dashboard](#clientput_dashboard)
        - [Client().put_metric_alarm](#clientput_metric_alarm)
        - [Client().put_metric_data](#clientput_metric_data)
        - [Client().set_alarm_state](#clientset_alarm_state)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_alarms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L20)

```python
def delete_alarms(AlarmNames: List[Any]) -> None:
```

### Client().delete_anomaly_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L24)

```python
def delete_anomaly_detector(
    Namespace: str,
    MetricName: str,
    Stat: str,
    Dimensions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_dashboards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L30)

```python
def delete_dashboards(DashboardNames: List[Any]) -> Dict[str, Any]:
```

### Client().describe_alarm_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L34)

```python
def describe_alarm_history(
    AlarmName: str = None,
    HistoryItemType: str = None,
    StartDate: datetime = None,
    EndDate: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_alarms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L46)

```python
def describe_alarms(
    AlarmNames: List[Any] = None,
    AlarmNamePrefix: str = None,
    StateValue: str = None,
    ActionPrefix: str = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_alarms_for_metric

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L58)

```python
def describe_alarms_for_metric(
    MetricName: str,
    Namespace: str,
    Statistic: str = None,
    ExtendedStatistic: str = None,
    Dimensions: List[Any] = None,
    Period: int = None,
    Unit: str = None,
) -> Dict[str, Any]:
```

### Client().describe_anomaly_detectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L71)

```python
def describe_anomaly_detectors(
    NextToken: str = None,
    MaxResults: int = None,
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().disable_alarm_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L82)

```python
def disable_alarm_actions(AlarmNames: List[Any]) -> None:
```

### Client().enable_alarm_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L86)

```python
def enable_alarm_actions(AlarmNames: List[Any]) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L90)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_dashboard

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L100)

```python
def get_dashboard(DashboardName: str) -> Dict[str, Any]:
```

### Client().get_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L104)

```python
def get_metric_data(
    MetricDataQueries: List[Any],
    StartTime: datetime,
    EndTime: datetime,
    NextToken: str = None,
    ScanBy: str = None,
    MaxDatapoints: int = None,
) -> Dict[str, Any]:
```

### Client().get_metric_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L116)

```python
def get_metric_statistics(
    Namespace: str,
    MetricName: str,
    StartTime: datetime,
    EndTime: datetime,
    Period: int,
    Dimensions: List[Any] = None,
    Statistics: List[Any] = None,
    ExtendedStatistics: List[Any] = None,
    Unit: str = None,
) -> Dict[str, Any]:
```

### Client().get_metric_widget_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L131)

```python
def get_metric_widget_image(
    MetricWidget: str,
    OutputFormat: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L137)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L141)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_dashboards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L145)

```python
def list_dashboards(
    DashboardNamePrefix: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L151)

```python
def list_metrics(
    Namespace: str = None,
    MetricName: str = None,
    Dimensions: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L161)

```python
def list_tags_for_resource(ResourceARN: str) -> Dict[str, Any]:
```

### Client().put_anomaly_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L165)

```python
def put_anomaly_detector(
    Namespace: str,
    MetricName: str,
    Stat: str,
    Dimensions: List[Any] = None,
    Configuration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_dashboard

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L176)

```python
def put_dashboard(DashboardName: str, DashboardBody: str) -> Dict[str, Any]:
```

### Client().put_metric_alarm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L180)

```python
def put_metric_alarm(
    AlarmName: str,
    EvaluationPeriods: int,
    ComparisonOperator: str,
    AlarmDescription: str = None,
    ActionsEnabled: bool = None,
    OKActions: List[Any] = None,
    AlarmActions: List[Any] = None,
    InsufficientDataActions: List[Any] = None,
    MetricName: str = None,
    Namespace: str = None,
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
) -> None:
```

### Client().put_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L208)

```python
def put_metric_data(Namespace: str, MetricData: List[Any]) -> None:
```

### Client().set_alarm_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L212)

```python
def set_alarm_state(
    AlarmName: str,
    StateValue: str,
    StateReason: str,
    StateReasonData: str = None,
) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L222)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/client.py#L226)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```
