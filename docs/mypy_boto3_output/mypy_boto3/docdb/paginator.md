# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.docdb.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Docdb](index.md#docdb) / Paginator
    - [DescribeDBClusters](#describedbclusters)
        - [DescribeDBClusters().paginate](#describedbclusterspaginate)
    - [DescribeDBEngineVersions](#describedbengineversions)
        - [DescribeDBEngineVersions().paginate](#describedbengineversionspaginate)
    - [DescribeDBInstances](#describedbinstances)
        - [DescribeDBInstances().paginate](#describedbinstancespaginate)
    - [DescribeDBSubnetGroups](#describedbsubnetgroups)
        - [DescribeDBSubnetGroups().paginate](#describedbsubnetgroupspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeOrderableDBInstanceOptions](#describeorderabledbinstanceoptions)
        - [DescribeOrderableDBInstanceOptions().paginate](#describeorderabledbinstanceoptionspaginate)

## DescribeDBClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L11)

```python
class DescribeDBClusters(Paginator):
```

### DescribeDBClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L14)

```python
def paginate(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBEngineVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L23)

```python
class DescribeDBEngineVersions(Paginator):
```

### DescribeDBEngineVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L26)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L40)

```python
class DescribeDBInstances(Paginator):
```

### DescribeDBInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L43)

```python
def paginate(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDBSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L52)

```python
class DescribeDBSubnetGroups(Paginator):
```

### DescribeDBSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L55)

```python
def paginate(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L64)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L67)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L81)

```python
class DescribeOrderableDBInstanceOptions(Paginator):
```

### DescribeOrderableDBInstanceOptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/paginator.py#L84)

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
