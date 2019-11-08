# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mturk.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mturk](index.md#mturk) / Paginator
    - [ListAssignmentsForHIT](#listassignmentsforhit)
        - [ListAssignmentsForHIT().paginate](#listassignmentsforhitpaginate)
    - [ListBonusPayments](#listbonuspayments)
        - [ListBonusPayments().paginate](#listbonuspaymentspaginate)
    - [ListHITs](#listhits)
        - [ListHITs().paginate](#listhitspaginate)
    - [ListHITsForQualificationType](#listhitsforqualificationtype)
        - [ListHITsForQualificationType().paginate](#listhitsforqualificationtypepaginate)
    - [ListQualificationRequests](#listqualificationrequests)
        - [ListQualificationRequests().paginate](#listqualificationrequestspaginate)
    - [ListQualificationTypes](#listqualificationtypes)
        - [ListQualificationTypes().paginate](#listqualificationtypespaginate)
    - [ListReviewableHITs](#listreviewablehits)
        - [ListReviewableHITs().paginate](#listreviewablehitspaginate)
    - [ListWorkerBlocks](#listworkerblocks)
        - [ListWorkerBlocks().paginate](#listworkerblockspaginate)
    - [ListWorkersWithQualificationType](#listworkerswithqualificationtype)
        - [ListWorkersWithQualificationType().paginate](#listworkerswithqualificationtypepaginate)

## ListAssignmentsForHIT

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L10)

```python
class ListAssignmentsForHIT(Paginator):
```

### ListAssignmentsForHIT().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L13)

```python
def paginate(
    HITId: str,
    AssignmentStatuses: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListBonusPayments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L22)

```python
class ListBonusPayments(Paginator):
```

### ListBonusPayments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L25)

```python
def paginate(
    HITId: str = None,
    AssignmentId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListHITs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L34)

```python
class ListHITs(Paginator):
```

### ListHITs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L37)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListHITsForQualificationType

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L41)

```python
class ListHITsForQualificationType(Paginator):
```

### ListHITsForQualificationType().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L44)

```python
def paginate(
    QualificationTypeId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQualificationRequests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L50)

```python
class ListQualificationRequests(Paginator):
```

### ListQualificationRequests().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L53)

```python
def paginate(
    QualificationTypeId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQualificationTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L59)

```python
class ListQualificationTypes(Paginator):
```

### ListQualificationTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L62)

```python
def paginate(
    MustBeRequestable: bool,
    Query: str = None,
    MustBeOwnedByCaller: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListReviewableHITs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L72)

```python
class ListReviewableHITs(Paginator):
```

### ListReviewableHITs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L75)

```python
def paginate(
    HITTypeId: str = None,
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListWorkerBlocks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L84)

```python
class ListWorkerBlocks(Paginator):
```

### ListWorkerBlocks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L87)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListWorkersWithQualificationType

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L91)

```python
class ListWorkersWithQualificationType(Paginator):
```

### ListWorkersWithQualificationType().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mturk/paginator.py#L94)

```python
def paginate(
    QualificationTypeId: str,
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
