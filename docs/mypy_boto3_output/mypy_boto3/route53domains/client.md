# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.route53domains.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Route53domains](index.md#route53domains) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().check_domain_availability](#clientcheck_domain_availability)
        - [Client().check_domain_transferability](#clientcheck_domain_transferability)
        - [Client().delete_tags_for_domain](#clientdelete_tags_for_domain)
        - [Client().disable_domain_auto_renew](#clientdisable_domain_auto_renew)
        - [Client().disable_domain_transfer_lock](#clientdisable_domain_transfer_lock)
        - [Client().enable_domain_auto_renew](#clientenable_domain_auto_renew)
        - [Client().enable_domain_transfer_lock](#clientenable_domain_transfer_lock)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_contact_reachability_status](#clientget_contact_reachability_status)
        - [Client().get_domain_detail](#clientget_domain_detail)
        - [Client().get_domain_suggestions](#clientget_domain_suggestions)
        - [Client().get_operation_detail](#clientget_operation_detail)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_domains](#clientlist_domains)
        - [Client().list_operations](#clientlist_operations)
        - [Client().list_tags_for_domain](#clientlist_tags_for_domain)
        - [Client().register_domain](#clientregister_domain)
        - [Client().renew_domain](#clientrenew_domain)
        - [Client().resend_contact_reachability_email](#clientresend_contact_reachability_email)
        - [Client().retrieve_domain_auth_code](#clientretrieve_domain_auth_code)
        - [Client().transfer_domain](#clienttransfer_domain)
        - [Client().update_domain_contact](#clientupdate_domain_contact)
        - [Client().update_domain_contact_privacy](#clientupdate_domain_contact_privacy)
        - [Client().update_domain_nameservers](#clientupdate_domain_nameservers)
        - [Client().update_tags_for_domain](#clientupdate_tags_for_domain)
        - [Client().view_billing](#clientview_billing)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().check_domain_availability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L20)

```python
def check_domain_availability(
    DomainName: str,
    IdnLangCode: str = None,
) -> Dict[str, Any]:
```

### Client().check_domain_transferability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L26)

```python
def check_domain_transferability(
    DomainName: str,
    AuthCode: str = None,
) -> Dict[str, Any]:
```

### Client().delete_tags_for_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L32)

```python
def delete_tags_for_domain(
    DomainName: str,
    TagsToDelete: List[Any],
) -> Dict[str, Any]:
```

### Client().disable_domain_auto_renew

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L38)

```python
def disable_domain_auto_renew(DomainName: str) -> Dict[str, Any]:
```

### Client().disable_domain_transfer_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L42)

```python
def disable_domain_transfer_lock(DomainName: str) -> Dict[str, Any]:
```

### Client().enable_domain_auto_renew

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L46)

```python
def enable_domain_auto_renew(DomainName: str) -> Dict[str, Any]:
```

### Client().enable_domain_transfer_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L50)

```python
def enable_domain_transfer_lock(DomainName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L54)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_contact_reachability_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L64)

```python
def get_contact_reachability_status(domainName: str = None) -> Dict[str, Any]:
```

### Client().get_domain_detail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L68)

```python
def get_domain_detail(DomainName: str) -> Dict[str, Any]:
```

### Client().get_domain_suggestions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L72)

```python
def get_domain_suggestions(
    DomainName: str,
    SuggestionCount: int,
    OnlyAvailable: bool,
) -> Dict[str, Any]:
```

### Client().get_operation_detail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L78)

```python
def get_operation_detail(OperationId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L82)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L86)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L90)

```python
def list_domains(Marker: str = None, MaxItems: int = None) -> Dict[str, Any]:
```

### Client().list_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L94)

```python
def list_operations(
    SubmittedSince: datetime = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L100)

```python
def list_tags_for_domain(DomainName: str) -> Dict[str, Any]:
```

### Client().register_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L104)

```python
def register_domain(
    DomainName: str,
    DurationInYears: int,
    AdminContact: Dict[str, Any],
    RegistrantContact: Dict[str, Any],
    TechContact: Dict[str, Any],
    IdnLangCode: str = None,
    AutoRenew: bool = None,
    PrivacyProtectAdminContact: bool = None,
    PrivacyProtectRegistrantContact: bool = None,
    PrivacyProtectTechContact: bool = None,
) -> Dict[str, Any]:
```

### Client().renew_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L120)

```python
def renew_domain(
    DomainName: str,
    CurrentExpiryYear: int,
    DurationInYears: int = None,
) -> Dict[str, Any]:
```

### Client().resend_contact_reachability_email

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L126)

```python
def resend_contact_reachability_email(
    domainName: str = None,
) -> Dict[str, Any]:
```

### Client().retrieve_domain_auth_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L132)

```python
def retrieve_domain_auth_code(DomainName: str) -> Dict[str, Any]:
```

### Client().transfer_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L136)

```python
def transfer_domain(
    DomainName: str,
    DurationInYears: int,
    AdminContact: Dict[str, Any],
    RegistrantContact: Dict[str, Any],
    TechContact: Dict[str, Any],
    IdnLangCode: str = None,
    Nameservers: List[Any] = None,
    AuthCode: str = None,
    AutoRenew: bool = None,
    PrivacyProtectAdminContact: bool = None,
    PrivacyProtectRegistrantContact: bool = None,
    PrivacyProtectTechContact: bool = None,
) -> Dict[str, Any]:
```

### Client().update_domain_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L154)

```python
def update_domain_contact(
    DomainName: str,
    AdminContact: Dict[str, Any] = None,
    RegistrantContact: Dict[str, Any] = None,
    TechContact: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_domain_contact_privacy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L164)

```python
def update_domain_contact_privacy(
    DomainName: str,
    AdminPrivacy: bool = None,
    RegistrantPrivacy: bool = None,
    TechPrivacy: bool = None,
) -> Dict[str, Any]:
```

### Client().update_domain_nameservers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L174)

```python
def update_domain_nameservers(
    DomainName: str,
    Nameservers: List[Any],
    FIAuthKey: str = None,
) -> Dict[str, Any]:
```

### Client().update_tags_for_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L180)

```python
def update_tags_for_domain(
    DomainName: str,
    TagsToUpdate: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().view_billing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/route53domains/client.py#L186)

```python
def view_billing(
    Start: datetime = None,
    End: datetime = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```
