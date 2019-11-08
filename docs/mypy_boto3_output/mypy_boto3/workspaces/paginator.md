# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workspaces.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workspaces](index.md#workspaces) / Paginator
    - [DescribeAccountModifications](#describeaccountmodifications)
        - [DescribeAccountModifications().paginate](#describeaccountmodificationspaginate)
    - [DescribeIpGroups](#describeipgroups)
        - [DescribeIpGroups().paginate](#describeipgroupspaginate)
    - [DescribeWorkspaceBundles](#describeworkspacebundles)
        - [DescribeWorkspaceBundles().paginate](#describeworkspacebundlespaginate)
    - [DescribeWorkspaceDirectories](#describeworkspacedirectories)
        - [DescribeWorkspaceDirectories().paginate](#describeworkspacedirectoriespaginate)
    - [DescribeWorkspaceImages](#describeworkspaceimages)
        - [DescribeWorkspaceImages().paginate](#describeworkspaceimagespaginate)
    - [DescribeWorkspaces](#describeworkspaces)
        - [DescribeWorkspaces().paginate](#describeworkspacespaginate)
    - [DescribeWorkspacesConnectionStatus](#describeworkspacesconnectionstatus)
        - [DescribeWorkspacesConnectionStatus().paginate](#describeworkspacesconnectionstatuspaginate)
    - [ListAvailableManagementCidrRanges](#listavailablemanagementcidrranges)
        - [ListAvailableManagementCidrRanges().paginate](#listavailablemanagementcidrrangespaginate)

## DescribeAccountModifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L10)

```python
class DescribeAccountModifications(Paginator):
```

### DescribeAccountModifications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeIpGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L17)

```python
class DescribeIpGroups(Paginator):
```

### DescribeIpGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L20)

```python
def paginate(
    GroupIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeWorkspaceBundles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L26)

```python
class DescribeWorkspaceBundles(Paginator):
```

### DescribeWorkspaceBundles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L29)

```python
def paginate(
    BundleIds: List[Any] = None,
    Owner: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeWorkspaceDirectories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L38)

```python
class DescribeWorkspaceDirectories(Paginator):
```

### DescribeWorkspaceDirectories().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L41)

```python
def paginate(
    DirectoryIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeWorkspaceImages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L47)

```python
class DescribeWorkspaceImages(Paginator):
```

### DescribeWorkspaceImages().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L50)

```python
def paginate(
    ImageIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeWorkspaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L56)

```python
class DescribeWorkspaces(Paginator):
```

### DescribeWorkspaces().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L59)

```python
def paginate(
    WorkspaceIds: List[Any] = None,
    DirectoryId: str = None,
    UserName: str = None,
    BundleId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeWorkspacesConnectionStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L70)

```python
class DescribeWorkspacesConnectionStatus(Paginator):
```

### DescribeWorkspacesConnectionStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L73)

```python
def paginate(
    WorkspaceIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAvailableManagementCidrRanges

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L79)

```python
class ListAvailableManagementCidrRanges(Paginator):
```

### ListAvailableManagementCidrRanges().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workspaces/paginator.py#L82)

```python
def paginate(
    ManagementCidrRangeConstraint: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
