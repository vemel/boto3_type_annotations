# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.acm_pca.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Acm Pca](index.md#acm-pca) / Waiter
    - [AuditReportCreated](#auditreportcreated)
        - [AuditReportCreated().wait](#auditreportcreatedwait)
    - [CertificateAuthorityCSRCreated](#certificateauthoritycsrcreated)
        - [CertificateAuthorityCSRCreated().wait](#certificateauthoritycsrcreatedwait)
    - [CertificateIssued](#certificateissued)
        - [CertificateIssued().wait](#certificateissuedwait)

## AuditReportCreated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L9)

```python
class AuditReportCreated(Waiter):
```

### AuditReportCreated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L12)

```python
def wait(
    CertificateAuthorityArn: str,
    AuditReportId: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## CertificateAuthorityCSRCreated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L21)

```python
class CertificateAuthorityCSRCreated(Waiter):
```

### CertificateAuthorityCSRCreated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L24)

```python
def wait(
    CertificateAuthorityArn: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## CertificateIssued

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L30)

```python
class CertificateIssued(Waiter):
```

### CertificateIssued().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/acm_pca/waiter.py#L33)

```python
def wait(
    CertificateAuthorityArn: str,
    CertificateArn: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
