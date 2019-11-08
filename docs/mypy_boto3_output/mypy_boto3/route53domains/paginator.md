# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.route53domains.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Route53domains](index.md#route53domains) / Paginator
    - [ListDomains](#listdomains)
        - [ListDomains().paginate](#listdomainspaginate)
    - [ListOperations](#listoperations)
        - [ListOperations().paginate](#listoperationspaginate)
    - [ViewBilling](#viewbilling)
        - [ViewBilling().paginate](#viewbillingpaginate)

## ListDomains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L10)

```python
class ListDomains(Paginator):
```

### ListDomains().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListOperations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L17)

```python
class ListOperations(Paginator):
```

### ListOperations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L20)

```python
def paginate(
    SubmittedSince: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ViewBilling

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L26)

```python
class ViewBilling(Paginator):
```

### ViewBilling().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/paginator.py#L29)

```python
def paginate(
    Start: datetime = None,
    End: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
