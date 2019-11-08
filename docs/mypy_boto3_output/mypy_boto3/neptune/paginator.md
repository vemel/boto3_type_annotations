# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.neptune.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Neptune](index.md#neptune) / Paginator
    - [DescribeDBClusterParameterGroups](#describedbclusterparametergroups)
        - [DescribeDBClusterParameterGroups().paginate](#describedbclusterparametergroupspaginate)
    - [DescribeDBClusterParameters](#describedbclusterparameters)
        - [DescribeDBClusterParameters().paginate](#describedbclusterparameterspaginate)
    - [DescribeDBClusterSnapshots](#describedbclustersnapshots)
        - [DescribeDBClusterSnapshots().paginate](#describedbclustersnapshotspaginate)
    - [DescribeDBClusters](#describedbclusters)
        - [DescribeDBClusters().paginate](#describedbclusterspaginate)
    - [DescribeDBEngineVersions](#describedbengineversions)
        - [DescribeDBEngineVersions().paginate](#describedbengineversionspaginate)
    - [DescribeDBInstances](#describedbinstances)
        - [DescribeDBInstances().paginate](#describedbinstancespaginate)
    - [DescribeDBParameterGroups](#describedbparametergroups)
        - [DescribeDBParameterGroups().paginate](#describedbparametergroupspaginate)
    - [DescribeDBParameters](#describedbparameters)
        - [DescribeDBParameters().paginate](#describedbparameterspaginate)
    - [DescribeDBSubnetGroups](#describedbsubnetgroups)
        - [DescribeDBSubnetGroups().paginate](#describedbsubnetgroupspaginate)
    - [DescribeEngineDefaultParameters](#describeenginedefaultparameters)
        - [DescribeEngineDefaultParameters().paginate](#describeenginedefaultparameterspaginate)
    - [DescribeEventSubscriptions](#describeeventsubscriptions)
        - [DescribeEventSubscriptions().paginate](#describeeventsubscriptionspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeOrderableDBInstanceOptions](#describeorderabledbinstanceoptions)
        - [DescribeOrderableDBInstanceOptions().paginate](#describeorderabledbinstanceoptionspaginate)
    - [DescribePendingMaintenanceActions](#describependingmaintenanceactions)
        - [DescribePendingMaintenanceActions().paginate](#describependingmaintenanceactionspaginate)

## DescribeDBClusterParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L11)

```python
class DescribeDBClusterParameterGroups(Paginator):
```

### DescribeDBClusterParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L14)

```python
def paginate(
    DBClusterParameterGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L23)

```python
class DescribeDBClusterParameters(Paginator):
```

### DescribeDBClusterParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L26)

```python
def paginate(
    DBClusterParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L36)

```python
class DescribeDBClusterSnapshots(Paginator):
```

### DescribeDBClusterSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L39)

```python
def paginate(
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L52)

```python
class DescribeDBClusters(Paginator):
```

### DescribeDBClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L55)

```python
def paginate(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBEngineVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L64)

```python
class DescribeDBEngineVersions(Paginator):
```

### DescribeDBEngineVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L67)

```python
def paginate(
    Engine: str = None,
    EngineVersion: str = None,
    DBParameterGroupFamily: str = None,
    Filters: List[Any] = None,
    DefaultOnly: bool = None,
    ListSupportedCharacterSets: bool = None,
    ListSupportedTimezones: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L81)

```python
class DescribeDBInstances(Paginator):
```

### DescribeDBInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L84)

```python
def paginate(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L93)

```python
class DescribeDBParameterGroups(Paginator):
```

### DescribeDBParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L96)

```python
def paginate(
    DBParameterGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L105)

```python
class DescribeDBParameters(Paginator):
```

### DescribeDBParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L108)

```python
def paginate(
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L118)

```python
class DescribeDBSubnetGroups(Paginator):
```

### DescribeDBSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L121)

```python
def paginate(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEngineDefaultParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L130)

```python
class DescribeEngineDefaultParameters(Paginator):
```

### DescribeEngineDefaultParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L133)

```python
def paginate(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L142)

```python
class DescribeEventSubscriptions(Paginator):
```

### DescribeEventSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L145)

```python
def paginate(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L154)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L157)

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

## DescribeOrderableDBInstanceOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L171)

```python
class DescribeOrderableDBInstanceOptions(Paginator):
```

### DescribeOrderableDBInstanceOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L174)

```python
def paginate(
    Engine: str,
    EngineVersion: str = None,
    DBInstanceClass: str = None,
    LicenseModel: str = None,
    Vpc: bool = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribePendingMaintenanceActions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L187)

```python
class DescribePendingMaintenanceActions(Paginator):
```

### DescribePendingMaintenanceActions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/paginator.py#L190)

```python
def paginate(
    ResourceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
