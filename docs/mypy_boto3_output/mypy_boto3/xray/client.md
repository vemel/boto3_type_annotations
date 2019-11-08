# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.xray.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Xray](index.md#xray) / Client
    - [Client](#client)
        - [Client().batch_get_traces](#clientbatch_get_traces)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_sampling_rule](#clientcreate_sampling_rule)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_sampling_rule](#clientdelete_sampling_rule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_encryption_config](#clientget_encryption_config)
        - [Client().get_group](#clientget_group)
        - [Client().get_groups](#clientget_groups)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_sampling_rules](#clientget_sampling_rules)
        - [Client().get_sampling_statistic_summaries](#clientget_sampling_statistic_summaries)
        - [Client().get_sampling_targets](#clientget_sampling_targets)
        - [Client().get_service_graph](#clientget_service_graph)
        - [Client().get_time_series_service_statistics](#clientget_time_series_service_statistics)
        - [Client().get_trace_graph](#clientget_trace_graph)
        - [Client().get_trace_summaries](#clientget_trace_summaries)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().put_encryption_config](#clientput_encryption_config)
        - [Client().put_telemetry_records](#clientput_telemetry_records)
        - [Client().put_trace_segments](#clientput_trace_segments)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_sampling_rule](#clientupdate_sampling_rule)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L13)

```python
class Client(BaseClient):
```

### Client().batch_get_traces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L16)

```python
def batch_get_traces(
    TraceIds: List[Any],
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L26)

```python
def create_group(
    GroupName: str,
    FilterExpression: str = None,
) -> Dict[str, Any]:
```

### Client().create_sampling_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L32)

```python
def create_sampling_rule(SamplingRule: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L36)

```python
def delete_group(
    GroupName: str = None,
    GroupARN: str = None,
) -> Dict[str, Any]:
```

### Client().delete_sampling_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L42)

```python
def delete_sampling_rule(
    RuleName: str = None,
    RuleARN: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L48)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L58)

```python
def get_encryption_config() -> Dict[str, Any]:
```

### Client().get_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L62)

```python
def get_group(GroupName: str = None, GroupARN: str = None) -> Dict[str, Any]:
```

### Client().get_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L66)

```python
def get_groups(NextToken: str = None) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L70)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_sampling_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L74)

```python
def get_sampling_rules(NextToken: str = None) -> Dict[str, Any]:
```

### Client().get_sampling_statistic_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L78)

```python
def get_sampling_statistic_summaries(NextToken: str = None) -> Dict[str, Any]:
```

### Client().get_sampling_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L82)

```python
def get_sampling_targets(
    SamplingStatisticsDocuments: List[Any],
) -> Dict[str, Any]:
```

### Client().get_service_graph

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L88)

```python
def get_service_graph(
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_time_series_service_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L99)

```python
def get_time_series_service_statistics(
    StartTime: datetime,
    EndTime: datetime,
    GroupName: str = None,
    GroupARN: str = None,
    EntitySelectorExpression: str = None,
    Period: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_trace_graph

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L112)

```python
def get_trace_graph(
    TraceIds: List[Any],
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_trace_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L118)

```python
def get_trace_summaries(
    StartTime: datetime,
    EndTime: datetime,
    TimeRangeType: str = None,
    Sampling: bool = None,
    SamplingStrategy: Dict[str, Any] = None,
    FilterExpression: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L131)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().put_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L135)

```python
def put_encryption_config(Type: str, KeyId: str = None) -> Dict[str, Any]:
```

### Client().put_telemetry_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L139)

```python
def put_telemetry_records(
    TelemetryRecords: List[Any],
    EC2InstanceId: str = None,
    Hostname: str = None,
    ResourceARN: str = None,
) -> Dict[str, Any]:
```

### Client().put_trace_segments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L149)

```python
def put_trace_segments(TraceSegmentDocuments: List[Any]) -> Dict[str, Any]:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L153)

```python
def update_group(
    GroupName: str = None,
    GroupARN: str = None,
    FilterExpression: str = None,
) -> Dict[str, Any]:
```

### Client().update_sampling_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/xray/client.py#L159)

```python
def update_sampling_rule(
    SamplingRuleUpdate: Dict[str, Any],
) -> Dict[str, Any]:
```
