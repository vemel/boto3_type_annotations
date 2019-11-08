# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.emr.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Emr](index.md#emr) / Paginator
    - [ListBootstrapActions](#listbootstrapactions)
        - [ListBootstrapActions().paginate](#listbootstrapactionspaginate)
    - [ListClusters](#listclusters)
        - [ListClusters().paginate](#listclusterspaginate)
    - [ListInstanceFleets](#listinstancefleets)
        - [ListInstanceFleets().paginate](#listinstancefleetspaginate)
    - [ListInstanceGroups](#listinstancegroups)
        - [ListInstanceGroups().paginate](#listinstancegroupspaginate)
    - [ListInstances](#listinstances)
        - [ListInstances().paginate](#listinstancespaginate)
    - [ListSecurityConfigurations](#listsecurityconfigurations)
        - [ListSecurityConfigurations().paginate](#listsecurityconfigurationspaginate)
    - [ListSteps](#liststeps)
        - [ListSteps().paginate](#liststepspaginate)

## ListBootstrapActions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L11)

```python
class ListBootstrapActions(Paginator):
```

### ListBootstrapActions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L14)

```python
def paginate(
    ClusterId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L20)

```python
class ListClusters(Paginator):
```

### ListClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L23)

```python
def paginate(
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    ClusterStates: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstanceFleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L33)

```python
class ListInstanceFleets(Paginator):
```

### ListInstanceFleets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L36)

```python
def paginate(
    ClusterId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstanceGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L42)

```python
class ListInstanceGroups(Paginator):
```

### ListInstanceGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L45)

```python
def paginate(
    ClusterId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L51)

```python
class ListInstances(Paginator):
```

### ListInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L54)

```python
def paginate(
    ClusterId: str,
    InstanceGroupId: str = None,
    InstanceGroupTypes: List[Any] = None,
    InstanceFleetId: str = None,
    InstanceFleetType: str = None,
    InstanceStates: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSecurityConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L67)

```python
class ListSecurityConfigurations(Paginator):
```

### ListSecurityConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L70)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSteps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L74)

```python
class ListSteps(Paginator):
```

### ListSteps().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/paginator.py#L77)

```python
def paginate(
    ClusterId: str,
    StepStates: List[Any] = None,
    StepIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
