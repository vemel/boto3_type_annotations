# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.acm.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Acm](index.md#acm) / Paginator
    - [ListCertificates](#listcertificates)
        - [ListCertificates().paginate](#listcertificatespaginate)

## ListCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/paginator.py#L10)

```python
class ListCertificates(Paginator):
```

### ListCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/paginator.py#L13)

```python
def paginate(
    CertificateStatuses: List[Any] = None,
    Includes: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
