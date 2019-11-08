# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workdocs.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workdocs](index.md#workdocs) / Paginator
    - [DescribeActivities](#describeactivities)
        - [DescribeActivities().paginate](#describeactivitiespaginate)
    - [DescribeComments](#describecomments)
        - [DescribeComments().paginate](#describecommentspaginate)
    - [DescribeDocumentVersions](#describedocumentversions)
        - [DescribeDocumentVersions().paginate](#describedocumentversionspaginate)
    - [DescribeFolderContents](#describefoldercontents)
        - [DescribeFolderContents().paginate](#describefoldercontentspaginate)
    - [DescribeGroups](#describegroups)
        - [DescribeGroups().paginate](#describegroupspaginate)
    - [DescribeNotificationSubscriptions](#describenotificationsubscriptions)
        - [DescribeNotificationSubscriptions().paginate](#describenotificationsubscriptionspaginate)
    - [DescribeResourcePermissions](#describeresourcepermissions)
        - [DescribeResourcePermissions().paginate](#describeresourcepermissionspaginate)
    - [DescribeRootFolders](#describerootfolders)
        - [DescribeRootFolders().paginate](#describerootfolderspaginate)
    - [DescribeUsers](#describeusers)
        - [DescribeUsers().paginate](#describeuserspaginate)

## DescribeActivities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L10)

```python
class DescribeActivities(Paginator):
```

### DescribeActivities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L13)

```python
def paginate(
    AuthenticationToken: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    OrganizationId: str = None,
    ActivityTypes: str = None,
    ResourceId: str = None,
    UserId: str = None,
    IncludeIndirectActivities: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeComments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L28)

```python
class DescribeComments(Paginator):
```

### DescribeComments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L31)

```python
def paginate(
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDocumentVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L41)

```python
class DescribeDocumentVersions(Paginator):
```

### DescribeDocumentVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L44)

```python
def paginate(
    DocumentId: str,
    AuthenticationToken: str = None,
    Include: str = None,
    Fields: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeFolderContents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L55)

```python
class DescribeFolderContents(Paginator):
```

### DescribeFolderContents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L58)

```python
def paginate(
    FolderId: str,
    AuthenticationToken: str = None,
    Sort: str = None,
    Order: str = None,
    Type: str = None,
    Include: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L71)

```python
class DescribeGroups(Paginator):
```

### DescribeGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L74)

```python
def paginate(
    SearchQuery: str,
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeNotificationSubscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L84)

```python
class DescribeNotificationSubscriptions(Paginator):
```

### DescribeNotificationSubscriptions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L87)

```python
def paginate(
    OrganizationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeResourcePermissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L93)

```python
class DescribeResourcePermissions(Paginator):
```

### DescribeResourcePermissions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L96)

```python
def paginate(
    ResourceId: str,
    AuthenticationToken: str = None,
    PrincipalId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeRootFolders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L106)

```python
class DescribeRootFolders(Paginator):
```

### DescribeRootFolders().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L109)

```python
def paginate(
    AuthenticationToken: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L115)

```python
class DescribeUsers(Paginator):
```

### DescribeUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workdocs/paginator.py#L118)

```python
def paginate(
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    UserIds: str = None,
    Query: str = None,
    Include: str = None,
    Order: str = None,
    Sort: str = None,
    Fields: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
