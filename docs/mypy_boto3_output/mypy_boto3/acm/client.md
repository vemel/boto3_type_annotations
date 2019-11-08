# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.acm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Acm](index.md#acm) / Client
    - [Client](#client)
        - [Client().add_tags_to_certificate](#clientadd_tags_to_certificate)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_certificate](#clientdelete_certificate)
        - [Client().describe_certificate](#clientdescribe_certificate)
        - [Client().export_certificate](#clientexport_certificate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_certificate](#clientget_certificate)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_certificate](#clientimport_certificate)
        - [Client().list_certificates](#clientlist_certificates)
        - [Client().list_tags_for_certificate](#clientlist_tags_for_certificate)
        - [Client().remove_tags_from_certificate](#clientremove_tags_from_certificate)
        - [Client().renew_certificate](#clientrenew_certificate)
        - [Client().request_certificate](#clientrequest_certificate)
        - [Client().resend_validation_email](#clientresend_validation_email)
        - [Client().update_certificate_options](#clientupdate_certificate_options)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags_to_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L15)

```python
def add_tags_to_certificate(CertificateArn: str, Tags: List[Any]) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L23)

```python
def delete_certificate(CertificateArn: str) -> None:
```

### Client().describe_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L27)

```python
def describe_certificate(CertificateArn: str) -> Dict[str, Any]:
```

### Client().export_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L31)

```python
def export_certificate(
    CertificateArn: str,
    Passphrase: bytes,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L37)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L47)

```python
def get_certificate(CertificateArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L51)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L55)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L59)

```python
def import_certificate(
    Certificate: bytes,
    PrivateKey: bytes,
    CertificateArn: str = None,
    CertificateChain: bytes = None,
) -> Dict[str, Any]:
```

### Client().list_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L69)

```python
def list_certificates(
    CertificateStatuses: List[Any] = None,
    Includes: Dict[str, Any] = None,
    NextToken: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L79)

```python
def list_tags_for_certificate(CertificateArn: str) -> Dict[str, Any]:
```

### Client().remove_tags_from_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L83)

```python
def remove_tags_from_certificate(
    CertificateArn: str,
    Tags: List[Any],
) -> None:
```

### Client().renew_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L89)

```python
def renew_certificate(CertificateArn: str) -> None:
```

### Client().request_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L93)

```python
def request_certificate(
    DomainName: str,
    ValidationMethod: str = None,
    SubjectAlternativeNames: List[Any] = None,
    IdempotencyToken: str = None,
    DomainValidationOptions: List[Any] = None,
    Options: Dict[str, Any] = None,
    CertificateAuthorityArn: str = None,
) -> Dict[str, Any]:
```

### Client().resend_validation_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L106)

```python
def resend_validation_email(
    CertificateArn: str,
    Domain: str,
    ValidationDomain: str,
) -> None:
```

### Client().update_certificate_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm/client.py#L112)

```python
def update_certificate_options(
    CertificateArn: str,
    Options: Dict[str, Any],
) -> None:
```
