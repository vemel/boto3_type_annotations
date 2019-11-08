# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.gamelift.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Gamelift](index.md#gamelift) / Paginator
    - [DescribeFleetAttributes](#describefleetattributes)
        - [DescribeFleetAttributes().paginate](#describefleetattributespaginate)
    - [DescribeFleetCapacity](#describefleetcapacity)
        - [DescribeFleetCapacity().paginate](#describefleetcapacitypaginate)
    - [DescribeFleetEvents](#describefleetevents)
        - [DescribeFleetEvents().paginate](#describefleeteventspaginate)
    - [DescribeFleetUtilization](#describefleetutilization)
        - [DescribeFleetUtilization().paginate](#describefleetutilizationpaginate)
    - [DescribeGameSessionDetails](#describegamesessiondetails)
        - [DescribeGameSessionDetails().paginate](#describegamesessiondetailspaginate)
    - [DescribeGameSessionQueues](#describegamesessionqueues)
        - [DescribeGameSessionQueues().paginate](#describegamesessionqueuespaginate)
    - [DescribeGameSessions](#describegamesessions)
        - [DescribeGameSessions().paginate](#describegamesessionspaginate)
    - [DescribeInstances](#describeinstances)
        - [DescribeInstances().paginate](#describeinstancespaginate)
    - [DescribeMatchmakingConfigurations](#describematchmakingconfigurations)
        - [DescribeMatchmakingConfigurations().paginate](#describematchmakingconfigurationspaginate)
    - [DescribeMatchmakingRuleSets](#describematchmakingrulesets)
        - [DescribeMatchmakingRuleSets().paginate](#describematchmakingrulesetspaginate)
    - [DescribePlayerSessions](#describeplayersessions)
        - [DescribePlayerSessions().paginate](#describeplayersessionspaginate)
    - [DescribeScalingPolicies](#describescalingpolicies)
        - [DescribeScalingPolicies().paginate](#describescalingpoliciespaginate)
    - [ListAliases](#listaliases)
        - [ListAliases().paginate](#listaliasespaginate)
    - [ListBuilds](#listbuilds)
        - [ListBuilds().paginate](#listbuildspaginate)
    - [ListFleets](#listfleets)
        - [ListFleets().paginate](#listfleetspaginate)
    - [SearchGameSessions](#searchgamesessions)
        - [SearchGameSessions().paginate](#searchgamesessionspaginate)

## DescribeFleetAttributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L11)

```python
class DescribeFleetAttributes(Paginator):
```

### DescribeFleetAttributes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L14)

```python
def paginate(
    FleetIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeFleetCapacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L20)

```python
class DescribeFleetCapacity(Paginator):
```

### DescribeFleetCapacity().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L23)

```python
def paginate(
    FleetIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeFleetEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L29)

```python
class DescribeFleetEvents(Paginator):
```

### DescribeFleetEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L32)

```python
def paginate(
    FleetId: str,
    StartTime: datetime = None,
    EndTime: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeFleetUtilization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L42)

```python
class DescribeFleetUtilization(Paginator):
```

### DescribeFleetUtilization().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L45)

```python
def paginate(
    FleetIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeGameSessionDetails

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L51)

```python
class DescribeGameSessionDetails(Paginator):
```

### DescribeGameSessionDetails().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L54)

```python
def paginate(
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    StatusFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeGameSessionQueues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L65)

```python
class DescribeGameSessionQueues(Paginator):
```

### DescribeGameSessionQueues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L68)

```python
def paginate(
    Names: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeGameSessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L74)

```python
class DescribeGameSessions(Paginator):
```

### DescribeGameSessions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L77)

```python
def paginate(
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    StatusFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L88)

```python
class DescribeInstances(Paginator):
```

### DescribeInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L91)

```python
def paginate(
    FleetId: str,
    InstanceId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeMatchmakingConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L100)

```python
class DescribeMatchmakingConfigurations(Paginator):
```

### DescribeMatchmakingConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L103)

```python
def paginate(
    Names: List[Any] = None,
    RuleSetName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeMatchmakingRuleSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L112)

```python
class DescribeMatchmakingRuleSets(Paginator):
```

### DescribeMatchmakingRuleSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L115)

```python
def paginate(
    Names: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribePlayerSessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L121)

```python
class DescribePlayerSessions(Paginator):
```

### DescribePlayerSessions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L124)

```python
def paginate(
    GameSessionId: str = None,
    PlayerId: str = None,
    PlayerSessionId: str = None,
    PlayerSessionStatusFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeScalingPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L135)

```python
class DescribeScalingPolicies(Paginator):
```

### DescribeScalingPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L138)

```python
def paginate(
    FleetId: str,
    StatusFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L147)

```python
class ListAliases(Paginator):
```

### ListAliases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L150)

```python
def paginate(
    RoutingStrategyType: str = None,
    Name: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListBuilds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L159)

```python
class ListBuilds(Paginator):
```

### ListBuilds().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L162)

```python
def paginate(
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListFleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L168)

```python
class ListFleets(Paginator):
```

### ListFleets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L171)

```python
def paginate(
    BuildId: str = None,
    ScriptId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SearchGameSessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L180)

```python
class SearchGameSessions(Paginator):
```

### SearchGameSessions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/paginator.py#L183)

```python
def paginate(
    FleetId: str = None,
    AliasId: str = None,
    FilterExpression: str = None,
    SortExpression: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
