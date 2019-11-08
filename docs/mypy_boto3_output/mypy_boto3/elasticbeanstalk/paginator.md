# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elasticbeanstalk.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elasticbeanstalk](index.md#elasticbeanstalk) / Paginator
    - [DescribeApplicationVersions](#describeapplicationversions)
        - [DescribeApplicationVersions().paginate](#describeapplicationversionspaginate)
    - [DescribeEnvironmentManagedActionHistory](#describeenvironmentmanagedactionhistory)
        - [DescribeEnvironmentManagedActionHistory().paginate](#describeenvironmentmanagedactionhistorypaginate)
    - [DescribeEnvironments](#describeenvironments)
        - [DescribeEnvironments().paginate](#describeenvironmentspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [ListPlatformVersions](#listplatformversions)
        - [ListPlatformVersions().paginate](#listplatformversionspaginate)

## DescribeApplicationVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L11)

```python
class DescribeApplicationVersions(Paginator):
```

### DescribeApplicationVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L14)

```python
def paginate(
    ApplicationName: str = None,
    VersionLabels: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEnvironmentManagedActionHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L23)

```python
class DescribeEnvironmentManagedActionHistory(Paginator):
```

### DescribeEnvironmentManagedActionHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L26)

```python
def paginate(
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEnvironments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L35)

```python
class DescribeEnvironments(Paginator):
```

### DescribeEnvironments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L38)

```python
def paginate(
    ApplicationName: str = None,
    VersionLabel: str = None,
    EnvironmentIds: List[Any] = None,
    EnvironmentNames: List[Any] = None,
    IncludeDeleted: bool = None,
    IncludedDeletedBackTo: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L51)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L54)

```python
def paginate(
    ApplicationName: str = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    PlatformArn: str = None,
    RequestId: str = None,
    Severity: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPlatformVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L71)

```python
class ListPlatformVersions(Paginator):
```

### ListPlatformVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticbeanstalk/paginator.py#L74)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
