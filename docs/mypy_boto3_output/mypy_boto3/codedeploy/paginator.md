# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codedeploy.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codedeploy](index.md#codedeploy) / Paginator
    - [ListApplicationRevisions](#listapplicationrevisions)
        - [ListApplicationRevisions().paginate](#listapplicationrevisionspaginate)
    - [ListApplications](#listapplications)
        - [ListApplications().paginate](#listapplicationspaginate)
    - [ListDeploymentConfigs](#listdeploymentconfigs)
        - [ListDeploymentConfigs().paginate](#listdeploymentconfigspaginate)
    - [ListDeploymentGroups](#listdeploymentgroups)
        - [ListDeploymentGroups().paginate](#listdeploymentgroupspaginate)
    - [ListDeploymentInstances](#listdeploymentinstances)
        - [ListDeploymentInstances().paginate](#listdeploymentinstancespaginate)
    - [ListDeploymentTargets](#listdeploymenttargets)
        - [ListDeploymentTargets().paginate](#listdeploymenttargetspaginate)
    - [ListDeployments](#listdeployments)
        - [ListDeployments().paginate](#listdeploymentspaginate)
    - [ListGitHubAccountTokenNames](#listgithubaccounttokennames)
        - [ListGitHubAccountTokenNames().paginate](#listgithubaccounttokennamespaginate)
    - [ListOnPremisesInstances](#listonpremisesinstances)
        - [ListOnPremisesInstances().paginate](#listonpremisesinstancespaginate)

## ListApplicationRevisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L10)

```python
class ListApplicationRevisions(Paginator):
```

### ListApplicationRevisions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L13)

```python
def paginate(
    applicationName: str,
    sortBy: str = None,
    sortOrder: str = None,
    s3Bucket: str = None,
    s3KeyPrefix: str = None,
    deployed: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListApplications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L26)

```python
class ListApplications(Paginator):
```

### ListApplications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L29)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDeploymentConfigs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L33)

```python
class ListDeploymentConfigs(Paginator):
```

### ListDeploymentConfigs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L36)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDeploymentGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L40)

```python
class ListDeploymentGroups(Paginator):
```

### ListDeploymentGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L43)

```python
def paginate(
    applicationName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDeploymentInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L49)

```python
class ListDeploymentInstances(Paginator):
```

### ListDeploymentInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L52)

```python
def paginate(
    deploymentId: str,
    instanceStatusFilter: List[Any] = None,
    instanceTypeFilter: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDeploymentTargets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L62)

```python
class ListDeploymentTargets(Paginator):
```

### ListDeploymentTargets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L65)

```python
def paginate(
    deploymentId: str = None,
    targetFilters: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDeployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L74)

```python
class ListDeployments(Paginator):
```

### ListDeployments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L77)

```python
def paginate(
    applicationName: str = None,
    deploymentGroupName: str = None,
    includeOnlyStatuses: List[Any] = None,
    createTimeRange: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGitHubAccountTokenNames

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L88)

```python
class ListGitHubAccountTokenNames(Paginator):
```

### ListGitHubAccountTokenNames().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L91)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListOnPremisesInstances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L95)

```python
class ListOnPremisesInstances(Paginator):
```

### ListOnPremisesInstances().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codedeploy/paginator.py#L98)

```python
def paginate(
    registrationStatus: str = None,
    tagFilters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
