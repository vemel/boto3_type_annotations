# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.service_quotas.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Service Quotas](index.md#service-quotas) / Client
    - [Client](#client)
        - [Client().associate_service_quota_template](#clientassociate_service_quota_template)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_service_quota_increase_request_from_template](#clientdelete_service_quota_increase_request_from_template)
        - [Client().disassociate_service_quota_template](#clientdisassociate_service_quota_template)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_association_for_service_quota_template](#clientget_association_for_service_quota_template)
        - [Client().get_aws_default_service_quota](#clientget_aws_default_service_quota)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_requested_service_quota_change](#clientget_requested_service_quota_change)
        - [Client().get_service_quota](#clientget_service_quota)
        - [Client().get_service_quota_increase_request_from_template](#clientget_service_quota_increase_request_from_template)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_aws_default_service_quotas](#clientlist_aws_default_service_quotas)
        - [Client().list_requested_service_quota_change_history](#clientlist_requested_service_quota_change_history)
        - [Client().list_requested_service_quota_change_history_by_quota](#clientlist_requested_service_quota_change_history_by_quota)
        - [Client().list_service_quota_increase_requests_in_template](#clientlist_service_quota_increase_requests_in_template)
        - [Client().list_service_quotas](#clientlist_service_quotas)
        - [Client().list_services](#clientlist_services)
        - [Client().put_service_quota_increase_request_into_template](#clientput_service_quota_increase_request_into_template)
        - [Client().request_service_quota_increase](#clientrequest_service_quota_increase)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L11)

```python
class Client(BaseClient):
```

### Client().associate_service_quota_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L14)

```python
def associate_service_quota_template() -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L18)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_service_quota_increase_request_from_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L22)

```python
def delete_service_quota_increase_request_from_template(
    ServiceCode: str,
    QuotaCode: str,
    AwsRegion: str,
) -> Dict[str, Any]:
```

### Client().disassociate_service_quota_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L28)

```python
def disassociate_service_quota_template() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L32)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_association_for_service_quota_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L42)

```python
def get_association_for_service_quota_template() -> Dict[str, Any]:
```

### Client().get_aws_default_service_quota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L46)

```python
def get_aws_default_service_quota(
    ServiceCode: str,
    QuotaCode: str,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L52)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_requested_service_quota_change

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L56)

```python
def get_requested_service_quota_change(RequestId: str) -> Dict[str, Any]:
```

### Client().get_service_quota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L60)

```python
def get_service_quota(ServiceCode: str, QuotaCode: str) -> Dict[str, Any]:
```

### Client().get_service_quota_increase_request_from_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L64)

```python
def get_service_quota_increase_request_from_template(
    ServiceCode: str,
    QuotaCode: str,
    AwsRegion: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L70)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_aws_default_service_quotas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L74)

```python
def list_aws_default_service_quotas(
    ServiceCode: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_requested_service_quota_change_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L80)

```python
def list_requested_service_quota_change_history(
    ServiceCode: str = None,
    Status: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_requested_service_quota_change_history_by_quota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L90)

```python
def list_requested_service_quota_change_history_by_quota(
    ServiceCode: str,
    QuotaCode: str,
    Status: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_service_quota_increase_requests_in_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L101)

```python
def list_service_quota_increase_requests_in_template(
    ServiceCode: str = None,
    AwsRegion: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_service_quotas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L111)

```python
def list_service_quotas(
    ServiceCode: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L117)

```python
def list_services(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_service_quota_increase_request_into_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L123)

```python
def put_service_quota_increase_request_into_template(
    QuotaCode: str,
    ServiceCode: str,
    AwsRegion: str,
    DesiredValue: float,
) -> Dict[str, Any]:
```

### Client().request_service_quota_increase

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/service_quotas/client.py#L129)

```python
def request_service_quota_increase(
    ServiceCode: str,
    QuotaCode: str,
    DesiredValue: float,
) -> Dict[str, Any]:
```
