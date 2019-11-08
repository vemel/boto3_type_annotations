# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.acm_pca.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Acm Pca](index.md#acm-pca) / Paginator
    - [ListCertificateAuthorities](#listcertificateauthorities)
        - [ListCertificateAuthorities().paginate](#listcertificateauthoritiespaginate)
    - [ListPermissions](#listpermissions)
        - [ListPermissions().paginate](#listpermissionspaginate)
    - [ListTags](#listtags)
        - [ListTags().paginate](#listtagspaginate)

## ListCertificateAuthorities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L9)

```python
class ListCertificateAuthorities(Paginator):
```

### ListCertificateAuthorities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListPermissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L16)

```python
class ListPermissions(Paginator):
```

### ListPermissions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L19)

```python
def paginate(
    CertificateAuthorityArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L25)

```python
class ListTags(Paginator):
```

### ListTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/paginator.py#L28)

```python
def paginate(
    CertificateAuthorityArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
