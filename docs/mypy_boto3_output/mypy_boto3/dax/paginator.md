# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dax.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dax](index.md#dax) / Paginator
    - [DescribeClusters](#describeclusters)
        - [DescribeClusters().paginate](#describeclusterspaginate)
    - [DescribeDefaultParameters](#describedefaultparameters)
        - [DescribeDefaultParameters().paginate](#describedefaultparameterspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeParameterGroups](#describeparametergroups)
        - [DescribeParameterGroups().paginate](#describeparametergroupspaginate)
    - [DescribeParameters](#describeparameters)
        - [DescribeParameters().paginate](#describeparameterspaginate)
    - [DescribeSubnetGroups](#describesubnetgroups)
        - [DescribeSubnetGroups().paginate](#describesubnetgroupspaginate)
    - [ListTags](#listtags)
        - [ListTags().paginate](#listtagspaginate)

## DescribeClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L11)

```python
class DescribeClusters(Paginator):
```

### DescribeClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L14)

```python
def paginate(
    ClusterNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDefaultParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L20)

```python
class DescribeDefaultParameters(Paginator):
```

### DescribeDefaultParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L23)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L27)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L30)

```python
def paginate(
    SourceName: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeParameterGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L42)

```python
class DescribeParameterGroups(Paginator):
```

### DescribeParameterGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L45)

```python
def paginate(
    ParameterGroupNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeParameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L53)

```python
class DescribeParameters(Paginator):
```

### DescribeParameters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L56)

```python
def paginate(
    ParameterGroupName: str,
    Source: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeSubnetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L65)

```python
class DescribeSubnetGroups(Paginator):
```

### DescribeSubnetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L68)

```python
def paginate(
    SubnetGroupNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L76)

```python
class ListTags(Paginator):
```

### ListTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dax/paginator.py#L79)

```python
def paginate(
    ResourceName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
