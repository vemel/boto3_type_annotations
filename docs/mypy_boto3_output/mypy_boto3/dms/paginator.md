# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dms.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dms](index.md#dms) / Paginator
    - [DescribeCertificates](#describecertificates)
        - [DescribeCertificates().paginate](#describecertificatespaginate)
    - [DescribeConnections](#describeconnections)
        - [DescribeConnections().paginate](#describeconnectionspaginate)
    - [DescribeEndpointTypes](#describeendpointtypes)
        - [DescribeEndpointTypes().paginate](#describeendpointtypespaginate)
    - [DescribeEndpoints](#describeendpoints)
        - [DescribeEndpoints().paginate](#describeendpointspaginate)
    - [DescribeEventSubscriptions](#describeeventsubscriptions)
        - [DescribeEventSubscriptions().paginate](#describeeventsubscriptionspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeOrderableReplicationInstances](#describeorderablereplicationinstances)
        - [DescribeOrderableReplicationInstances().paginate](#describeorderablereplicationinstancespaginate)
    - [DescribeReplicationInstances](#describereplicationinstances)
        - [DescribeReplicationInstances().paginate](#describereplicationinstancespaginate)
    - [DescribeReplicationSubnetGroups](#describereplicationsubnetgroups)
        - [DescribeReplicationSubnetGroups().paginate](#describereplicationsubnetgroupspaginate)
    - [DescribeReplicationTaskAssessmentResults](#describereplicationtaskassessmentresults)
        - [DescribeReplicationTaskAssessmentResults().paginate](#describereplicationtaskassessmentresultspaginate)
    - [DescribeReplicationTasks](#describereplicationtasks)
        - [DescribeReplicationTasks().paginate](#describereplicationtaskspaginate)
    - [DescribeSchemas](#describeschemas)
        - [DescribeSchemas().paginate](#describeschemaspaginate)
    - [DescribeTableStatistics](#describetablestatistics)
        - [DescribeTableStatistics().paginate](#describetablestatisticspaginate)

## DescribeCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L11)

```python
class DescribeCertificates(Paginator):
```

### DescribeCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L14)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeConnections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L20)

```python
class DescribeConnections(Paginator):
```

### DescribeConnections().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L23)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEndpointTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L29)

```python
class DescribeEndpointTypes(Paginator):
```

### DescribeEndpointTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L32)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEndpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L38)

```python
class DescribeEndpoints(Paginator):
```

### DescribeEndpoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L41)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L47)

```python
class DescribeEventSubscriptions(Paginator):
```

### DescribeEventSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L50)

```python
def paginate(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L59)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L62)

```python
def paginate(
    SourceIdentifier: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    EventCategories: List[Any] = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeOrderableReplicationInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L76)

```python
class DescribeOrderableReplicationInstances(Paginator):
```

### DescribeOrderableReplicationInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L79)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeReplicationInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L83)

```python
class DescribeReplicationInstances(Paginator):
```

### DescribeReplicationInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L86)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReplicationSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L92)

```python
class DescribeReplicationSubnetGroups(Paginator):
```

### DescribeReplicationSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L95)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReplicationTaskAssessmentResults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L101)

```python
class DescribeReplicationTaskAssessmentResults(Paginator):
```

### DescribeReplicationTaskAssessmentResults().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L104)

```python
def paginate(
    ReplicationTaskArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReplicationTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L110)

```python
class DescribeReplicationTasks(Paginator):
```

### DescribeReplicationTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L113)

```python
def paginate(
    Filters: List[Any] = None,
    WithoutSettings: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSchemas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L122)

```python
class DescribeSchemas(Paginator):
```

### DescribeSchemas().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L125)

```python
def paginate(
    EndpointArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTableStatistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L131)

```python
class DescribeTableStatistics(Paginator):
```

### DescribeTableStatistics().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/paginator.py#L134)

```python
def paginate(
    ReplicationTaskArn: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
