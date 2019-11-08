# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.glue.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Glue](index.md#glue) / Paginator
    - [GetClassifiers](#getclassifiers)
        - [GetClassifiers().paginate](#getclassifierspaginate)
    - [GetConnections](#getconnections)
        - [GetConnections().paginate](#getconnectionspaginate)
    - [GetCrawlerMetrics](#getcrawlermetrics)
        - [GetCrawlerMetrics().paginate](#getcrawlermetricspaginate)
    - [GetCrawlers](#getcrawlers)
        - [GetCrawlers().paginate](#getcrawlerspaginate)
    - [GetDatabases](#getdatabases)
        - [GetDatabases().paginate](#getdatabasespaginate)
    - [GetDevEndpoints](#getdevendpoints)
        - [GetDevEndpoints().paginate](#getdevendpointspaginate)
    - [GetJobRuns](#getjobruns)
        - [GetJobRuns().paginate](#getjobrunspaginate)
    - [GetJobs](#getjobs)
        - [GetJobs().paginate](#getjobspaginate)
    - [GetPartitions](#getpartitions)
        - [GetPartitions().paginate](#getpartitionspaginate)
    - [GetSecurityConfigurations](#getsecurityconfigurations)
        - [GetSecurityConfigurations().paginate](#getsecurityconfigurationspaginate)
    - [GetTableVersions](#gettableversions)
        - [GetTableVersions().paginate](#gettableversionspaginate)
    - [GetTables](#gettables)
        - [GetTables().paginate](#gettablespaginate)
    - [GetTriggers](#gettriggers)
        - [GetTriggers().paginate](#gettriggerspaginate)
    - [GetUserDefinedFunctions](#getuserdefinedfunctions)
        - [GetUserDefinedFunctions().paginate](#getuserdefinedfunctionspaginate)

## GetClassifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L10)

```python
class GetClassifiers(Paginator):
```

### GetClassifiers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetConnections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L17)

```python
class GetConnections(Paginator):
```

### GetConnections().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L20)

```python
def paginate(
    CatalogId: str = None,
    Filter: Dict[str, Any] = None,
    HidePassword: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetCrawlerMetrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L30)

```python
class GetCrawlerMetrics(Paginator):
```

### GetCrawlerMetrics().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L33)

```python
def paginate(
    CrawlerNameList: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetCrawlers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L39)

```python
class GetCrawlers(Paginator):
```

### GetCrawlers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L42)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetDatabases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L46)

```python
class GetDatabases(Paginator):
```

### GetDatabases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L49)

```python
def paginate(
    CatalogId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetDevEndpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L55)

```python
class GetDevEndpoints(Paginator):
```

### GetDevEndpoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L58)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetJobRuns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L62)

```python
class GetJobRuns(Paginator):
```

### GetJobRuns().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L65)

```python
def paginate(
    JobName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L71)

```python
class GetJobs(Paginator):
```

### GetJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L74)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetPartitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L78)

```python
class GetPartitions(Paginator):
```

### GetPartitions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L81)

```python
def paginate(
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    Expression: str = None,
    Segment: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetSecurityConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L93)

```python
class GetSecurityConfigurations(Paginator):
```

### GetSecurityConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L96)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetTableVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L100)

```python
class GetTableVersions(Paginator):
```

### GetTableVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L103)

```python
def paginate(
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L113)

```python
class GetTables(Paginator):
```

### GetTables().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L116)

```python
def paginate(
    DatabaseName: str,
    CatalogId: str = None,
    Expression: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetTriggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L126)

```python
class GetTriggers(Paginator):
```

### GetTriggers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L129)

```python
def paginate(
    DependentJobName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetUserDefinedFunctions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L135)

```python
class GetUserDefinedFunctions(Paginator):
```

### GetUserDefinedFunctions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/paginator.py#L138)

```python
def paginate(
    DatabaseName: str,
    Pattern: str,
    CatalogId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
