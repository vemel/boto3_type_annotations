# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.support.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Support](index.md#support) / Paginator
    - [DescribeCases](#describecases)
        - [DescribeCases().paginate](#describecasespaginate)
    - [DescribeCommunications](#describecommunications)
        - [DescribeCommunications().paginate](#describecommunicationspaginate)

## DescribeCases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/paginator.py#L10)

```python
class DescribeCases(Paginator):
```

### DescribeCases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/paginator.py#L13)

```python
def paginate(
    caseIdList: List[Any] = None,
    displayId: str = None,
    afterTime: str = None,
    beforeTime: str = None,
    includeResolvedCases: bool = None,
    language: str = None,
    includeCommunications: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeCommunications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/paginator.py#L27)

```python
class DescribeCommunications(Paginator):
```

### DescribeCommunications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/support/paginator.py#L30)

```python
def paginate(
    caseId: str,
    beforeTime: str = None,
    afterTime: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
