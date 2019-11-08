# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediaconvert.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediaconvert](index.md#mediaconvert) / Paginator
    - [DescribeEndpoints](#describeendpoints)
        - [DescribeEndpoints().paginate](#describeendpointspaginate)
    - [ListJobTemplates](#listjobtemplates)
        - [ListJobTemplates().paginate](#listjobtemplatespaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)
    - [ListPresets](#listpresets)
        - [ListPresets().paginate](#listpresetspaginate)
    - [ListQueues](#listqueues)
        - [ListQueues().paginate](#listqueuespaginate)

## DescribeEndpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L9)

```python
class DescribeEndpoints(Paginator):
```

### DescribeEndpoints().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L12)

```python
def paginate(
    Mode: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobTemplates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L18)

```python
class ListJobTemplates(Paginator):
```

### ListJobTemplates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L21)

```python
def paginate(
    Category: str = None,
    ListBy: str = None,
    Order: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L31)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L34)

```python
def paginate(
    Order: str = None,
    Queue: str = None,
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPresets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L44)

```python
class ListPresets(Paginator):
```

### ListPresets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L47)

```python
def paginate(
    Category: str = None,
    ListBy: str = None,
    Order: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQueues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L57)

```python
class ListQueues(Paginator):
```

### ListQueues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediaconvert/paginator.py#L60)

```python
def paginate(
    ListBy: str = None,
    Order: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
