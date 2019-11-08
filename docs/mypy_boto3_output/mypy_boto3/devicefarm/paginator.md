# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.devicefarm.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Devicefarm](index.md#devicefarm) / Paginator
    - [GetOfferingStatus](#getofferingstatus)
        - [GetOfferingStatus().paginate](#getofferingstatuspaginate)
    - [ListArtifacts](#listartifacts)
        - [ListArtifacts().paginate](#listartifactspaginate)
    - [ListDeviceInstances](#listdeviceinstances)
        - [ListDeviceInstances().paginate](#listdeviceinstancespaginate)
    - [ListDevicePools](#listdevicepools)
        - [ListDevicePools().paginate](#listdevicepoolspaginate)
    - [ListDevices](#listdevices)
        - [ListDevices().paginate](#listdevicespaginate)
    - [ListInstanceProfiles](#listinstanceprofiles)
        - [ListInstanceProfiles().paginate](#listinstanceprofilespaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)
    - [ListNetworkProfiles](#listnetworkprofiles)
        - [ListNetworkProfiles().paginate](#listnetworkprofilespaginate)
    - [ListOfferingPromotions](#listofferingpromotions)
        - [ListOfferingPromotions().paginate](#listofferingpromotionspaginate)
    - [ListOfferingTransactions](#listofferingtransactions)
        - [ListOfferingTransactions().paginate](#listofferingtransactionspaginate)
    - [ListOfferings](#listofferings)
        - [ListOfferings().paginate](#listofferingspaginate)
    - [ListProjects](#listprojects)
        - [ListProjects().paginate](#listprojectspaginate)
    - [ListRemoteAccessSessions](#listremoteaccesssessions)
        - [ListRemoteAccessSessions().paginate](#listremoteaccesssessionspaginate)
    - [ListRuns](#listruns)
        - [ListRuns().paginate](#listrunspaginate)
    - [ListSamples](#listsamples)
        - [ListSamples().paginate](#listsamplespaginate)
    - [ListSuites](#listsuites)
        - [ListSuites().paginate](#listsuitespaginate)
    - [ListTests](#listtests)
        - [ListTests().paginate](#listtestspaginate)
    - [ListUniqueProblems](#listuniqueproblems)
        - [ListUniqueProblems().paginate](#listuniqueproblemspaginate)
    - [ListUploads](#listuploads)
        - [ListUploads().paginate](#listuploadspaginate)
    - [ListVPCEConfigurations](#listvpceconfigurations)
        - [ListVPCEConfigurations().paginate](#listvpceconfigurationspaginate)

## GetOfferingStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L10)

```python
class GetOfferingStatus(Paginator):
```

### GetOfferingStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListArtifacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L17)

```python
class ListArtifacts(Paginator):
```

### ListArtifacts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L20)

```python
def paginate(
    arn: str,
    type: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDeviceInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L26)

```python
class ListDeviceInstances(Paginator):
```

### ListDeviceInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L29)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDevicePools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L33)

```python
class ListDevicePools(Paginator):
```

### ListDevicePools().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L36)

```python
def paginate(
    arn: str,
    type: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L42)

```python
class ListDevices(Paginator):
```

### ListDevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L45)

```python
def paginate(
    arn: str = None,
    filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstanceProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L54)

```python
class ListInstanceProfiles(Paginator):
```

### ListInstanceProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L57)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L61)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L64)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListNetworkProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L70)

```python
class ListNetworkProfiles(Paginator):
```

### ListNetworkProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L73)

```python
def paginate(
    arn: str,
    type: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOfferingPromotions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L79)

```python
class ListOfferingPromotions(Paginator):
```

### ListOfferingPromotions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L82)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListOfferingTransactions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L86)

```python
class ListOfferingTransactions(Paginator):
```

### ListOfferingTransactions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L89)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L93)

```python
class ListOfferings(Paginator):
```

### ListOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L96)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListProjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L100)

```python
class ListProjects(Paginator):
```

### ListProjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L103)

```python
def paginate(
    arn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRemoteAccessSessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L109)

```python
class ListRemoteAccessSessions(Paginator):
```

### ListRemoteAccessSessions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L112)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRuns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L118)

```python
class ListRuns(Paginator):
```

### ListRuns().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L121)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSamples

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L127)

```python
class ListSamples(Paginator):
```

### ListSamples().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L130)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSuites

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L136)

```python
class ListSuites(Paginator):
```

### ListSuites().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L139)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L145)

```python
class ListTests(Paginator):
```

### ListTests().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L148)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUniqueProblems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L154)

```python
class ListUniqueProblems(Paginator):
```

### ListUniqueProblems().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L157)

```python
def paginate(
    arn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L163)

```python
class ListUploads(Paginator):
```

### ListUploads().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L166)

```python
def paginate(
    arn: str,
    type: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListVPCEConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L172)

```python
class ListVPCEConfigurations(Paginator):
```

### ListVPCEConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/devicefarm/paginator.py#L175)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
