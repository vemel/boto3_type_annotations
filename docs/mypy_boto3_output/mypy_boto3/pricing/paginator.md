# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pricing.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pricing](index.md#pricing) / Paginator
    - [DescribeServices](#describeservices)
        - [DescribeServices().paginate](#describeservicespaginate)
    - [GetAttributeValues](#getattributevalues)
        - [GetAttributeValues().paginate](#getattributevaluespaginate)
    - [GetProducts](#getproducts)
        - [GetProducts().paginate](#getproductspaginate)

## DescribeServices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L10)

```python
class DescribeServices(Paginator):
```

### DescribeServices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L13)

```python
def paginate(
    ServiceCode: str = None,
    FormatVersion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetAttributeValues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L22)

```python
class GetAttributeValues(Paginator):
```

### GetAttributeValues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L25)

```python
def paginate(
    ServiceCode: str,
    AttributeName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetProducts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L34)

```python
class GetProducts(Paginator):
```

### GetProducts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/paginator.py#L37)

```python
def paginate(
    ServiceCode: str = None,
    Filters: List[Any] = None,
    FormatVersion: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
