# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.redshift.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Redshift](index.md#redshift) / Paginator
    - [DescribeClusterDbRevisions](#describeclusterdbrevisions)
        - [DescribeClusterDbRevisions().paginate](#describeclusterdbrevisionspaginate)
    - [DescribeClusterParameterGroups](#describeclusterparametergroups)
        - [DescribeClusterParameterGroups().paginate](#describeclusterparametergroupspaginate)
    - [DescribeClusterParameters](#describeclusterparameters)
        - [DescribeClusterParameters().paginate](#describeclusterparameterspaginate)
    - [DescribeClusterSecurityGroups](#describeclustersecuritygroups)
        - [DescribeClusterSecurityGroups().paginate](#describeclustersecuritygroupspaginate)
    - [DescribeClusterSnapshots](#describeclustersnapshots)
        - [DescribeClusterSnapshots().paginate](#describeclustersnapshotspaginate)
    - [DescribeClusterSubnetGroups](#describeclustersubnetgroups)
        - [DescribeClusterSubnetGroups().paginate](#describeclustersubnetgroupspaginate)
    - [DescribeClusterTracks](#describeclustertracks)
        - [DescribeClusterTracks().paginate](#describeclustertrackspaginate)
    - [DescribeClusterVersions](#describeclusterversions)
        - [DescribeClusterVersions().paginate](#describeclusterversionspaginate)
    - [DescribeClusters](#describeclusters)
        - [DescribeClusters().paginate](#describeclusterspaginate)
    - [DescribeDefaultClusterParameters](#describedefaultclusterparameters)
        - [DescribeDefaultClusterParameters().paginate](#describedefaultclusterparameterspaginate)
    - [DescribeEventSubscriptions](#describeeventsubscriptions)
        - [DescribeEventSubscriptions().paginate](#describeeventsubscriptionspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeHsmClientCertificates](#describehsmclientcertificates)
        - [DescribeHsmClientCertificates().paginate](#describehsmclientcertificatespaginate)
    - [DescribeHsmConfigurations](#describehsmconfigurations)
        - [DescribeHsmConfigurations().paginate](#describehsmconfigurationspaginate)
    - [DescribeNodeConfigurationOptions](#describenodeconfigurationoptions)
        - [DescribeNodeConfigurationOptions().paginate](#describenodeconfigurationoptionspaginate)
    - [DescribeOrderableClusterOptions](#describeorderableclusteroptions)
        - [DescribeOrderableClusterOptions().paginate](#describeorderableclusteroptionspaginate)
    - [DescribeReservedNodeOfferings](#describereservednodeofferings)
        - [DescribeReservedNodeOfferings().paginate](#describereservednodeofferingspaginate)
    - [DescribeReservedNodes](#describereservednodes)
        - [DescribeReservedNodes().paginate](#describereservednodespaginate)
    - [DescribeSnapshotCopyGrants](#describesnapshotcopygrants)
        - [DescribeSnapshotCopyGrants().paginate](#describesnapshotcopygrantspaginate)
    - [DescribeSnapshotSchedules](#describesnapshotschedules)
        - [DescribeSnapshotSchedules().paginate](#describesnapshotschedulespaginate)
    - [DescribeTableRestoreStatus](#describetablerestorestatus)
        - [DescribeTableRestoreStatus().paginate](#describetablerestorestatuspaginate)
    - [DescribeTags](#describetags)
        - [DescribeTags().paginate](#describetagspaginate)
    - [GetReservedNodeExchangeOfferings](#getreservednodeexchangeofferings)
        - [GetReservedNodeExchangeOfferings().paginate](#getreservednodeexchangeofferingspaginate)

## DescribeClusterDbRevisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L11)

```python
class DescribeClusterDbRevisions(Paginator):
```

### DescribeClusterDbRevisions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L14)

```python
def paginate(
    ClusterIdentifier: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L20)

```python
class DescribeClusterParameterGroups(Paginator):
```

### DescribeClusterParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L23)

```python
def paginate(
    ParameterGroupName: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L33)

```python
class DescribeClusterParameters(Paginator):
```

### DescribeClusterParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L36)

```python
def paginate(
    ParameterGroupName: str,
    Source: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterSecurityGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L45)

```python
class DescribeClusterSecurityGroups(Paginator):
```

### DescribeClusterSecurityGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L48)

```python
def paginate(
    ClusterSecurityGroupName: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L58)

```python
class DescribeClusterSnapshots(Paginator):
```

### DescribeClusterSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L61)

```python
def paginate(
    ClusterIdentifier: str = None,
    SnapshotIdentifier: str = None,
    SnapshotType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    OwnerAccount: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    ClusterExists: bool = None,
    SortingEntities: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L78)

```python
class DescribeClusterSubnetGroups(Paginator):
```

### DescribeClusterSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L81)

```python
def paginate(
    ClusterSubnetGroupName: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterTracks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L91)

```python
class DescribeClusterTracks(Paginator):
```

### DescribeClusterTracks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L94)

```python
def paginate(
    MaintenanceTrackName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusterVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L100)

```python
class DescribeClusterVersions(Paginator):
```

### DescribeClusterVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L103)

```python
def paginate(
    ClusterVersion: str = None,
    ClusterParameterGroupFamily: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L112)

```python
class DescribeClusters(Paginator):
```

### DescribeClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L115)

```python
def paginate(
    ClusterIdentifier: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDefaultClusterParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L125)

```python
class DescribeDefaultClusterParameters(Paginator):
```

### DescribeDefaultClusterParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L128)

```python
def paginate(
    ParameterGroupFamily: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L134)

```python
class DescribeEventSubscriptions(Paginator):
```

### DescribeEventSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L137)

```python
def paginate(
    SubscriptionName: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L147)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L150)

```python
def paginate(
    SourceIdentifier: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeHsmClientCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L162)

```python
class DescribeHsmClientCertificates(Paginator):
```

### DescribeHsmClientCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L165)

```python
def paginate(
    HsmClientCertificateIdentifier: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeHsmConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L175)

```python
class DescribeHsmConfigurations(Paginator):
```

### DescribeHsmConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L178)

```python
def paginate(
    HsmConfigurationIdentifier: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeNodeConfigurationOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L188)

```python
class DescribeNodeConfigurationOptions(Paginator):
```

### DescribeNodeConfigurationOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L191)

```python
def paginate(
    ActionType: str,
    SnapshotIdentifier: str = None,
    OwnerAccount: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeOrderableClusterOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L202)

```python
class DescribeOrderableClusterOptions(Paginator):
```

### DescribeOrderableClusterOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L205)

```python
def paginate(
    ClusterVersion: str = None,
    NodeType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReservedNodeOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L214)

```python
class DescribeReservedNodeOfferings(Paginator):
```

### DescribeReservedNodeOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L217)

```python
def paginate(
    ReservedNodeOfferingId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReservedNodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L225)

```python
class DescribeReservedNodes(Paginator):
```

### DescribeReservedNodes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L228)

```python
def paginate(
    ReservedNodeId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSnapshotCopyGrants

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L234)

```python
class DescribeSnapshotCopyGrants(Paginator):
```

### DescribeSnapshotCopyGrants().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L237)

```python
def paginate(
    SnapshotCopyGrantName: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSnapshotSchedules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L247)

```python
class DescribeSnapshotSchedules(Paginator):
```

### DescribeSnapshotSchedules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L250)

```python
def paginate(
    ClusterIdentifier: str = None,
    ScheduleIdentifier: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTableRestoreStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L261)

```python
class DescribeTableRestoreStatus(Paginator):
```

### DescribeTableRestoreStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L264)

```python
def paginate(
    ClusterIdentifier: str = None,
    TableRestoreRequestId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L273)

```python
class DescribeTags(Paginator):
```

### DescribeTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L276)

```python
def paginate(
    ResourceName: str = None,
    ResourceType: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetReservedNodeExchangeOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L287)

```python
class GetReservedNodeExchangeOfferings(Paginator):
```

### GetReservedNodeExchangeOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/paginator.py#L290)

```python
def paginate(
    ReservedNodeId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
