# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.acm_pca.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Acm Pca](index.md#acm-pca) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_certificate_authority](#clientcreate_certificate_authority)
        - [Client().create_certificate_authority_audit_report](#clientcreate_certificate_authority_audit_report)
        - [Client().create_permission](#clientcreate_permission)
        - [Client().delete_certificate_authority](#clientdelete_certificate_authority)
        - [Client().delete_permission](#clientdelete_permission)
        - [Client().describe_certificate_authority](#clientdescribe_certificate_authority)
        - [Client().describe_certificate_authority_audit_report](#clientdescribe_certificate_authority_audit_report)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_certificate](#clientget_certificate)
        - [Client().get_certificate_authority_certificate](#clientget_certificate_authority_certificate)
        - [Client().get_certificate_authority_csr](#clientget_certificate_authority_csr)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_certificate_authority_certificate](#clientimport_certificate_authority_certificate)
        - [Client().issue_certificate](#clientissue_certificate)
        - [Client().list_certificate_authorities](#clientlist_certificate_authorities)
        - [Client().list_permissions](#clientlist_permissions)
        - [Client().list_tags](#clientlist_tags)
        - [Client().restore_certificate_authority](#clientrestore_certificate_authority)
        - [Client().revoke_certificate](#clientrevoke_certificate)
        - [Client().tag_certificate_authority](#clienttag_certificate_authority)
        - [Client().untag_certificate_authority](#clientuntag_certificate_authority)
        - [Client().update_certificate_authority](#clientupdate_certificate_authority)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L19)

```python
def create_certificate_authority(
    CertificateAuthorityConfiguration: Dict[str, Any],
    CertificateAuthorityType: str,
    RevocationConfiguration: Dict[str, Any] = None,
    IdempotencyToken: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_certificate_authority_audit_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L30)

```python
def create_certificate_authority_audit_report(
    CertificateAuthorityArn: str,
    S3BucketName: str,
    AuditReportResponseFormat: str,
) -> Dict[str, Any]:
```

### Client().create_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L39)

```python
def create_permission(
    CertificateAuthorityArn: str,
    Principal: str,
    Actions: List[Any],
    SourceAccount: str = None,
) -> None:
```

### Client().delete_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L49)

```python
def delete_certificate_authority(
    CertificateAuthorityArn: str,
    PermanentDeletionTimeInDays: int = None,
) -> None:
```

### Client().delete_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L55)

```python
def delete_permission(
    CertificateAuthorityArn: str,
    Principal: str,
    SourceAccount: str = None,
) -> None:
```

### Client().describe_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L61)

```python
def describe_certificate_authority(
    CertificateAuthorityArn: str,
) -> Dict[str, Any]:
```

### Client().describe_certificate_authority_audit_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L67)

```python
def describe_certificate_authority_audit_report(
    CertificateAuthorityArn: str,
    AuditReportId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L73)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L83)

```python
def get_certificate(
    CertificateAuthorityArn: str,
    CertificateArn: str,
) -> Dict[str, Any]:
```

### Client().get_certificate_authority_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L89)

```python
def get_certificate_authority_certificate(
    CertificateAuthorityArn: str,
) -> Dict[str, Any]:
```

### Client().get_certificate_authority_csr

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L95)

```python
def get_certificate_authority_csr(
    CertificateAuthorityArn: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L101)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L105)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_certificate_authority_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L109)

```python
def import_certificate_authority_certificate(
    CertificateAuthorityArn: str,
    Certificate: bytes,
    CertificateChain: bytes = None,
) -> None:
```

### Client().issue_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L118)

```python
def issue_certificate(
    CertificateAuthorityArn: str,
    Csr: bytes,
    SigningAlgorithm: str,
    Validity: Dict[str, Any],
    TemplateArn: str = None,
    IdempotencyToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_certificate_authorities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L130)

```python
def list_certificate_authorities(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L136)

```python
def list_permissions(
    CertificateAuthorityArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L145)

```python
def list_tags(
    CertificateAuthorityArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().restore_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L154)

```python
def restore_certificate_authority(CertificateAuthorityArn: str) -> None:
```

### Client().revoke_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L158)

```python
def revoke_certificate(
    CertificateAuthorityArn: str,
    CertificateSerial: str,
    RevocationReason: str,
) -> None:
```

### Client().tag_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L167)

```python
def tag_certificate_authority(
    CertificateAuthorityArn: str,
    Tags: List[Any],
) -> None:
```

### Client().untag_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L173)

```python
def untag_certificate_authority(
    CertificateAuthorityArn: str,
    Tags: List[Any],
) -> None:
```

### Client().update_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/client.py#L179)

```python
def update_certificate_authority(
    CertificateAuthorityArn: str,
    RevocationConfiguration: Dict[str, Any] = None,
    Status: str = None,
) -> None:
```
