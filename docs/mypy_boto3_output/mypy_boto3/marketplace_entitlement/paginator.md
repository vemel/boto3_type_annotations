# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.marketplace_entitlement.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplace_entitlement/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Marketplace Entitlement](index.md#marketplace-entitlement) / Paginator
    - [GetEntitlements](#getentitlements)
        - [GetEntitlements().paginate](#getentitlementspaginate)

## GetEntitlements

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplace_entitlement/paginator.py#L9)

```python
class GetEntitlements(Paginator):
```

### GetEntitlements().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplace_entitlement/paginator.py#L12)

```python
def paginate(
    ProductCode: str,
    Filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
