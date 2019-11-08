# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.connect.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Connect](index.md#connect) / Paginator
    - [GetMetricData](#getmetricdata)
        - [GetMetricData().paginate](#getmetricdatapaginate)
    - [ListContactFlows](#listcontactflows)
        - [ListContactFlows().paginate](#listcontactflowspaginate)
    - [ListHoursOfOperations](#listhoursofoperations)
        - [ListHoursOfOperations().paginate](#listhoursofoperationspaginate)
    - [ListPhoneNumbers](#listphonenumbers)
        - [ListPhoneNumbers().paginate](#listphonenumberspaginate)
    - [ListQueues](#listqueues)
        - [ListQueues().paginate](#listqueuespaginate)
    - [ListRoutingProfiles](#listroutingprofiles)
        - [ListRoutingProfiles().paginate](#listroutingprofilespaginate)
    - [ListSecurityProfiles](#listsecurityprofiles)
        - [ListSecurityProfiles().paginate](#listsecurityprofilespaginate)
    - [ListUserHierarchyGroups](#listuserhierarchygroups)
        - [ListUserHierarchyGroups().paginate](#listuserhierarchygroupspaginate)
    - [ListUsers](#listusers)
        - [ListUsers().paginate](#listuserspaginate)

## GetMetricData

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L11)

```python
class GetMetricData(Paginator):
```

### GetMetricData().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L14)

```python
def paginate(
    InstanceId: str,
    StartTime: datetime,
    EndTime: datetime,
    Filters: Dict[str, Any],
    HistoricalMetrics: List[Any],
    Groupings: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListContactFlows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L27)

```python
class ListContactFlows(Paginator):
```

### ListContactFlows().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L30)

```python
def paginate(
    InstanceId: str,
    ContactFlowTypes: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListHoursOfOperations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L39)

```python
class ListHoursOfOperations(Paginator):
```

### ListHoursOfOperations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L42)

```python
def paginate(
    InstanceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPhoneNumbers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L48)

```python
class ListPhoneNumbers(Paginator):
```

### ListPhoneNumbers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L51)

```python
def paginate(
    InstanceId: str,
    PhoneNumberTypes: List[Any] = None,
    PhoneNumberCountryCodes: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQueues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L61)

```python
class ListQueues(Paginator):
```

### ListQueues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L64)

```python
def paginate(
    InstanceId: str,
    QueueTypes: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRoutingProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L73)

```python
class ListRoutingProfiles(Paginator):
```

### ListRoutingProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L76)

```python
def paginate(
    InstanceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSecurityProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L82)

```python
class ListSecurityProfiles(Paginator):
```

### ListSecurityProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L85)

```python
def paginate(
    InstanceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUserHierarchyGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L91)

```python
class ListUserHierarchyGroups(Paginator):
```

### ListUserHierarchyGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L94)

```python
def paginate(
    InstanceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L100)

```python
class ListUsers(Paginator):
```

### ListUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/paginator.py#L103)

```python
def paginate(
    InstanceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
