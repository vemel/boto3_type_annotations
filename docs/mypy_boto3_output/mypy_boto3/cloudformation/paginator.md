# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudformation.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudformation](index.md#cloudformation) / Paginator
    - [DescribeAccountLimits](#describeaccountlimits)
        - [DescribeAccountLimits().paginate](#describeaccountlimitspaginate)
    - [DescribeChangeSet](#describechangeset)
        - [DescribeChangeSet().paginate](#describechangesetpaginate)
    - [DescribeStackEvents](#describestackevents)
        - [DescribeStackEvents().paginate](#describestackeventspaginate)
    - [DescribeStacks](#describestacks)
        - [DescribeStacks().paginate](#describestackspaginate)
    - [ListChangeSets](#listchangesets)
        - [ListChangeSets().paginate](#listchangesetspaginate)
    - [ListExports](#listexports)
        - [ListExports().paginate](#listexportspaginate)
    - [ListImports](#listimports)
        - [ListImports().paginate](#listimportspaginate)
    - [ListStackInstances](#liststackinstances)
        - [ListStackInstances().paginate](#liststackinstancespaginate)
    - [ListStackResources](#liststackresources)
        - [ListStackResources().paginate](#liststackresourcespaginate)
    - [ListStackSetOperationResults](#liststacksetoperationresults)
        - [ListStackSetOperationResults().paginate](#liststacksetoperationresultspaginate)
    - [ListStackSetOperations](#liststacksetoperations)
        - [ListStackSetOperations().paginate](#liststacksetoperationspaginate)
    - [ListStackSets](#liststacksets)
        - [ListStackSets().paginate](#liststacksetspaginate)
    - [ListStacks](#liststacks)
        - [ListStacks().paginate](#liststackspaginate)

## DescribeAccountLimits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L10)

```python
class DescribeAccountLimits(Paginator):
```

### DescribeAccountLimits().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeChangeSet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L17)

```python
class DescribeChangeSet(Paginator):
```

### DescribeChangeSet().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L20)

```python
def paginate(
    ChangeSetName: str,
    StackName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeStackEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L29)

```python
class DescribeStackEvents(Paginator):
```

### DescribeStackEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L32)

```python
def paginate(
    StackName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeStacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L38)

```python
class DescribeStacks(Paginator):
```

### DescribeStacks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L41)

```python
def paginate(
    StackName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListChangeSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L47)

```python
class ListChangeSets(Paginator):
```

### ListChangeSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L50)

```python
def paginate(
    StackName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListExports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L56)

```python
class ListExports(Paginator):
```

### ListExports().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L59)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListImports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L63)

```python
class ListImports(Paginator):
```

### ListImports().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L66)

```python
def paginate(
    ExportName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStackInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L72)

```python
class ListStackInstances(Paginator):
```

### ListStackInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L75)

```python
def paginate(
    StackSetName: str,
    StackInstanceAccount: str = None,
    StackInstanceRegion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStackResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L85)

```python
class ListStackResources(Paginator):
```

### ListStackResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L88)

```python
def paginate(
    StackName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStackSetOperationResults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L94)

```python
class ListStackSetOperationResults(Paginator):
```

### ListStackSetOperationResults().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L97)

```python
def paginate(
    StackSetName: str,
    OperationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStackSetOperations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L106)

```python
class ListStackSetOperations(Paginator):
```

### ListStackSetOperations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L109)

```python
def paginate(
    StackSetName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStackSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L115)

```python
class ListStackSets(Paginator):
```

### ListStackSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L118)

```python
def paginate(
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L124)

```python
class ListStacks(Paginator):
```

### ListStacks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/paginator.py#L127)

```python
def paginate(
    StackStatusFilter: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
