# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rds.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rds](index.md#rds) / Paginator
    - [DescribeCertificates](#describecertificates)
        - [DescribeCertificates().paginate](#describecertificatespaginate)
    - [DescribeCustomAvailabilityZones](#describecustomavailabilityzones)
        - [DescribeCustomAvailabilityZones().paginate](#describecustomavailabilityzonespaginate)
    - [DescribeDBClusterBacktracks](#describedbclusterbacktracks)
        - [DescribeDBClusterBacktracks().paginate](#describedbclusterbacktrackspaginate)
    - [DescribeDBClusterEndpoints](#describedbclusterendpoints)
        - [DescribeDBClusterEndpoints().paginate](#describedbclusterendpointspaginate)
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
    - [DescribeDBInstanceAutomatedBackups](#describedbinstanceautomatedbackups)
        - [DescribeDBInstanceAutomatedBackups().paginate](#describedbinstanceautomatedbackupspaginate)
    - [DescribeDBInstances](#describedbinstances)
        - [DescribeDBInstances().paginate](#describedbinstancespaginate)
    - [DescribeDBLogFiles](#describedblogfiles)
        - [DescribeDBLogFiles().paginate](#describedblogfilespaginate)
    - [DescribeDBParameterGroups](#describedbparametergroups)
        - [DescribeDBParameterGroups().paginate](#describedbparametergroupspaginate)
    - [DescribeDBParameters](#describedbparameters)
        - [DescribeDBParameters().paginate](#describedbparameterspaginate)
    - [DescribeDBSecurityGroups](#describedbsecuritygroups)
        - [DescribeDBSecurityGroups().paginate](#describedbsecuritygroupspaginate)
    - [DescribeDBSnapshots](#describedbsnapshots)
        - [DescribeDBSnapshots().paginate](#describedbsnapshotspaginate)
    - [DescribeDBSubnetGroups](#describedbsubnetgroups)
        - [DescribeDBSubnetGroups().paginate](#describedbsubnetgroupspaginate)
    - [DescribeEngineDefaultClusterParameters](#describeenginedefaultclusterparameters)
        - [DescribeEngineDefaultClusterParameters().paginate](#describeenginedefaultclusterparameterspaginate)
    - [DescribeEngineDefaultParameters](#describeenginedefaultparameters)
        - [DescribeEngineDefaultParameters().paginate](#describeenginedefaultparameterspaginate)
    - [DescribeEventSubscriptions](#describeeventsubscriptions)
        - [DescribeEventSubscriptions().paginate](#describeeventsubscriptionspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeGlobalClusters](#describeglobalclusters)
        - [DescribeGlobalClusters().paginate](#describeglobalclusterspaginate)
    - [DescribeInstallationMedia](#describeinstallationmedia)
        - [DescribeInstallationMedia().paginate](#describeinstallationmediapaginate)
    - [DescribeOptionGroupOptions](#describeoptiongroupoptions)
        - [DescribeOptionGroupOptions().paginate](#describeoptiongroupoptionspaginate)
    - [DescribeOptionGroups](#describeoptiongroups)
        - [DescribeOptionGroups().paginate](#describeoptiongroupspaginate)
    - [DescribeOrderableDBInstanceOptions](#describeorderabledbinstanceoptions)
        - [DescribeOrderableDBInstanceOptions().paginate](#describeorderabledbinstanceoptionspaginate)
    - [DescribePendingMaintenanceActions](#describependingmaintenanceactions)
        - [DescribePendingMaintenanceActions().paginate](#describependingmaintenanceactionspaginate)
    - [DescribeReservedDBInstances](#describereserveddbinstances)
        - [DescribeReservedDBInstances().paginate](#describereserveddbinstancespaginate)
    - [DescribeReservedDBInstancesOfferings](#describereserveddbinstancesofferings)
        - [DescribeReservedDBInstancesOfferings().paginate](#describereserveddbinstancesofferingspaginate)
    - [DescribeSourceRegions](#describesourceregions)
        - [DescribeSourceRegions().paginate](#describesourceregionspaginate)
    - [DownloadDBLogFilePortion](#downloaddblogfileportion)
        - [DownloadDBLogFilePortion().paginate](#downloaddblogfileportionpaginate)

## DescribeCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L11)

```python
class DescribeCertificates(Paginator):
```

### DescribeCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L14)

```python
def paginate(
    CertificateIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeCustomAvailabilityZones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L23)

```python
class DescribeCustomAvailabilityZones(Paginator):
```

### DescribeCustomAvailabilityZones().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L26)

```python
def paginate(
    CustomAvailabilityZoneId: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterBacktracks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L35)

```python
class DescribeDBClusterBacktracks(Paginator):
```

### DescribeDBClusterBacktracks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L38)

```python
def paginate(
    DBClusterIdentifier: str,
    BacktrackIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterEndpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L48)

```python
class DescribeDBClusterEndpoints(Paginator):
```

### DescribeDBClusterEndpoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L51)

```python
def paginate(
    DBClusterIdentifier: str = None,
    DBClusterEndpointIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L61)

```python
class DescribeDBClusterParameterGroups(Paginator):
```

### DescribeDBClusterParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L64)

```python
def paginate(
    DBClusterParameterGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L73)

```python
class DescribeDBClusterParameters(Paginator):
```

### DescribeDBClusterParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L76)

```python
def paginate(
    DBClusterParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBClusterSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L86)

```python
class DescribeDBClusterSnapshots(Paginator):
```

### DescribeDBClusterSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L89)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L102)

```python
class DescribeDBClusters(Paginator):
```

### DescribeDBClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L105)

```python
def paginate(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    IncludeShared: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBEngineVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L115)

```python
class DescribeDBEngineVersions(Paginator):
```

### DescribeDBEngineVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L118)

```python
def paginate(
    Engine: str = None,
    EngineVersion: str = None,
    DBParameterGroupFamily: str = None,
    Filters: List[Any] = None,
    DefaultOnly: bool = None,
    ListSupportedCharacterSets: bool = None,
    ListSupportedTimezones: bool = None,
    IncludeAll: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBInstanceAutomatedBackups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L133)

```python
class DescribeDBInstanceAutomatedBackups(Paginator):
```

### DescribeDBInstanceAutomatedBackups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L136)

```python
def paginate(
    DbiResourceId: str = None,
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L146)

```python
class DescribeDBInstances(Paginator):
```

### DescribeDBInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L149)

```python
def paginate(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBLogFiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L158)

```python
class DescribeDBLogFiles(Paginator):
```

### DescribeDBLogFiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L161)

```python
def paginate(
    DBInstanceIdentifier: str,
    FilenameContains: str = None,
    FileLastWritten: int = None,
    FileSize: int = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L173)

```python
class DescribeDBParameterGroups(Paginator):
```

### DescribeDBParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L176)

```python
def paginate(
    DBParameterGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L185)

```python
class DescribeDBParameters(Paginator):
```

### DescribeDBParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L188)

```python
def paginate(
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBSecurityGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L198)

```python
class DescribeDBSecurityGroups(Paginator):
```

### DescribeDBSecurityGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L201)

```python
def paginate(
    DBSecurityGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L210)

```python
class DescribeDBSnapshots(Paginator):
```

### DescribeDBSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L213)

```python
def paginate(
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L227)

```python
class DescribeDBSubnetGroups(Paginator):
```

### DescribeDBSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L230)

```python
def paginate(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEngineDefaultClusterParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L239)

```python
class DescribeEngineDefaultClusterParameters(Paginator):
```

### DescribeEngineDefaultClusterParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L242)

```python
def paginate(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEngineDefaultParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L251)

```python
class DescribeEngineDefaultParameters(Paginator):
```

### DescribeEngineDefaultParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L254)

```python
def paginate(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEventSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L263)

```python
class DescribeEventSubscriptions(Paginator):
```

### DescribeEventSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L266)

```python
def paginate(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L275)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L278)

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

## DescribeGlobalClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L292)

```python
class DescribeGlobalClusters(Paginator):
```

### DescribeGlobalClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L295)

```python
def paginate(
    GlobalClusterIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeInstallationMedia

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L304)

```python
class DescribeInstallationMedia(Paginator):
```

### DescribeInstallationMedia().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L307)

```python
def paginate(
    InstallationMediaId: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeOptionGroupOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L316)

```python
class DescribeOptionGroupOptions(Paginator):
```

### DescribeOptionGroupOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L319)

```python
def paginate(
    EngineName: str,
    MajorEngineVersion: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeOptionGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L329)

```python
class DescribeOptionGroups(Paginator):
```

### DescribeOptionGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L332)

```python
def paginate(
    OptionGroupName: str = None,
    Filters: List[Any] = None,
    EngineName: str = None,
    MajorEngineVersion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeOrderableDBInstanceOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L343)

```python
class DescribeOrderableDBInstanceOptions(Paginator):
```

### DescribeOrderableDBInstanceOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L346)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L359)

```python
class DescribePendingMaintenanceActions(Paginator):
```

### DescribePendingMaintenanceActions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L362)

```python
def paginate(
    ResourceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReservedDBInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L371)

```python
class DescribeReservedDBInstances(Paginator):
```

### DescribeReservedDBInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L374)

```python
def paginate(
    ReservedDBInstanceId: str = None,
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    LeaseId: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeReservedDBInstancesOfferings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L390)

```python
class DescribeReservedDBInstancesOfferings(Paginator):
```

### DescribeReservedDBInstancesOfferings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L393)

```python
def paginate(
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSourceRegions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L407)

```python
class DescribeSourceRegions(Paginator):
```

### DescribeSourceRegions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L410)

```python
def paginate(
    RegionName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DownloadDBLogFilePortion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L419)

```python
class DownloadDBLogFilePortion(Paginator):
```

### DownloadDBLogFilePortion().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/paginator.py#L422)

```python
def paginate(
    DBInstanceIdentifier: str,
    LogFileName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
