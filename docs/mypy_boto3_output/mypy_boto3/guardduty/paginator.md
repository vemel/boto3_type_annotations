# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.guardduty.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Guardduty](index.md#guardduty) / Paginator
    - [ListDetectors](#listdetectors)
        - [ListDetectors().paginate](#listdetectorspaginate)
    - [ListFilters](#listfilters)
        - [ListFilters().paginate](#listfilterspaginate)
    - [ListFindings](#listfindings)
        - [ListFindings().paginate](#listfindingspaginate)
    - [ListIPSets](#listipsets)
        - [ListIPSets().paginate](#listipsetspaginate)
    - [ListInvitations](#listinvitations)
        - [ListInvitations().paginate](#listinvitationspaginate)
    - [ListMembers](#listmembers)
        - [ListMembers().paginate](#listmemberspaginate)
    - [ListThreatIntelSets](#listthreatintelsets)
        - [ListThreatIntelSets().paginate](#listthreatintelsetspaginate)

## ListDetectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L9)

```python
class ListDetectors(Paginator):
```

### ListDetectors().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListFilters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L16)

```python
class ListFilters(Paginator):
```

### ListFilters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L19)

```python
def paginate(
    DetectorId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListFindings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L25)

```python
class ListFindings(Paginator):
```

### ListFindings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L28)

```python
def paginate(
    DetectorId: str,
    FindingCriteria: Dict[str, Any] = None,
    SortCriteria: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListIPSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L38)

```python
class ListIPSets(Paginator):
```

### ListIPSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L41)

```python
def paginate(
    DetectorId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInvitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L47)

```python
class ListInvitations(Paginator):
```

### ListInvitations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L50)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListMembers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L54)

```python
class ListMembers(Paginator):
```

### ListMembers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L57)

```python
def paginate(
    DetectorId: str,
    OnlyAssociated: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThreatIntelSets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L66)

```python
class ListThreatIntelSets(Paginator):
```

### ListThreatIntelSets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/paginator.py#L69)

```python
def paginate(
    DetectorId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
