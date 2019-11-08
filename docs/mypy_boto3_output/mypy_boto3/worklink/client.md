# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.worklink.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Worklink](index.md#worklink) / Client
    - [Client](#client)
        - [Client().associate_domain](#clientassociate_domain)
        - [Client().associate_website_authorization_provider](#clientassociate_website_authorization_provider)
        - [Client().associate_website_certificate_authority](#clientassociate_website_certificate_authority)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_fleet](#clientcreate_fleet)
        - [Client().delete_fleet](#clientdelete_fleet)
        - [Client().describe_audit_stream_configuration](#clientdescribe_audit_stream_configuration)
        - [Client().describe_company_network_configuration](#clientdescribe_company_network_configuration)
        - [Client().describe_device](#clientdescribe_device)
        - [Client().describe_device_policy_configuration](#clientdescribe_device_policy_configuration)
        - [Client().describe_domain](#clientdescribe_domain)
        - [Client().describe_fleet_metadata](#clientdescribe_fleet_metadata)
        - [Client().describe_identity_provider_configuration](#clientdescribe_identity_provider_configuration)
        - [Client().describe_website_certificate_authority](#clientdescribe_website_certificate_authority)
        - [Client().disassociate_domain](#clientdisassociate_domain)
        - [Client().disassociate_website_authorization_provider](#clientdisassociate_website_authorization_provider)
        - [Client().disassociate_website_certificate_authority](#clientdisassociate_website_certificate_authority)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_devices](#clientlist_devices)
        - [Client().list_domains](#clientlist_domains)
        - [Client().list_fleets](#clientlist_fleets)
        - [Client().list_website_authorization_providers](#clientlist_website_authorization_providers)
        - [Client().list_website_certificate_authorities](#clientlist_website_certificate_authorities)
        - [Client().restore_domain_access](#clientrestore_domain_access)
        - [Client().revoke_domain_access](#clientrevoke_domain_access)
        - [Client().sign_out_user](#clientsign_out_user)
        - [Client().update_audit_stream_configuration](#clientupdate_audit_stream_configuration)
        - [Client().update_company_network_configuration](#clientupdate_company_network_configuration)
        - [Client().update_device_policy_configuration](#clientupdate_device_policy_configuration)
        - [Client().update_domain_metadata](#clientupdate_domain_metadata)
        - [Client().update_fleet_metadata](#clientupdate_fleet_metadata)
        - [Client().update_identity_provider_configuration](#clientupdate_identity_provider_configuration)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L15)

```python
def associate_domain(
    FleetArn: str,
    DomainName: str,
    AcmCertificateArn: str,
    DisplayName: str = None,
) -> Dict[str, Any]:
```

### Client().associate_website_authorization_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L25)

```python
def associate_website_authorization_provider(
    FleetArn: str,
    AuthorizationProviderType: str,
    DomainName: str = None,
) -> Dict[str, Any]:
```

### Client().associate_website_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L31)

```python
def associate_website_certificate_authority(
    FleetArn: str,
    Certificate: str,
    DisplayName: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L37)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L41)

```python
def create_fleet(
    FleetName: str,
    DisplayName: str = None,
    OptimizeForEndUserLocation: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L50)

```python
def delete_fleet(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_audit_stream_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L54)

```python
def describe_audit_stream_configuration(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_company_network_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L58)

```python
def describe_company_network_configuration(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L62)

```python
def describe_device(FleetArn: str, DeviceId: str) -> Dict[str, Any]:
```

### Client().describe_device_policy_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L66)

```python
def describe_device_policy_configuration(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L70)

```python
def describe_domain(FleetArn: str, DomainName: str) -> Dict[str, Any]:
```

### Client().describe_fleet_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L74)

```python
def describe_fleet_metadata(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_identity_provider_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L78)

```python
def describe_identity_provider_configuration(FleetArn: str) -> Dict[str, Any]:
```

### Client().describe_website_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L82)

```python
def describe_website_certificate_authority(
    FleetArn: str,
    WebsiteCaId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L88)

```python
def disassociate_domain(FleetArn: str, DomainName: str) -> Dict[str, Any]:
```

### Client().disassociate_website_authorization_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L92)

```python
def disassociate_website_authorization_provider(
    FleetArn: str,
    AuthorizationProviderId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_website_certificate_authority

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L98)

```python
def disassociate_website_certificate_authority(
    FleetArn: str,
    WebsiteCaId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L104)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L114)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L118)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L122)

```python
def list_devices(
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L128)

```python
def list_domains(
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L134)

```python
def list_fleets(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_website_authorization_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L140)

```python
def list_website_authorization_providers(
    FleetArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_website_certificate_authorities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L146)

```python
def list_website_certificate_authorities(
    FleetArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().restore_domain_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L152)

```python
def restore_domain_access(FleetArn: str, DomainName: str) -> Dict[str, Any]:
```

### Client().revoke_domain_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L156)

```python
def revoke_domain_access(FleetArn: str, DomainName: str) -> Dict[str, Any]:
```

### Client().sign_out_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L160)

```python
def sign_out_user(FleetArn: str, Username: str) -> Dict[str, Any]:
```

### Client().update_audit_stream_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L164)

```python
def update_audit_stream_configuration(
    FleetArn: str,
    AuditStreamArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_company_network_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L170)

```python
def update_company_network_configuration(
    FleetArn: str,
    VpcId: str,
    SubnetIds: List[Any],
    SecurityGroupIds: List[Any],
) -> Dict[str, Any]:
```

### Client().update_device_policy_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L180)

```python
def update_device_policy_configuration(
    FleetArn: str,
    DeviceCaCertificate: str = None,
) -> Dict[str, Any]:
```

### Client().update_domain_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L186)

```python
def update_domain_metadata(
    FleetArn: str,
    DomainName: str,
    DisplayName: str = None,
) -> Dict[str, Any]:
```

### Client().update_fleet_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L192)

```python
def update_fleet_metadata(
    FleetArn: str,
    DisplayName: str = None,
    OptimizeForEndUserLocation: bool = None,
) -> Dict[str, Any]:
```

### Client().update_identity_provider_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/worklink/client.py#L201)

```python
def update_identity_provider_configuration(
    FleetArn: str,
    IdentityProviderType: str,
    IdentityProviderSamlMetadata: str = None,
) -> Dict[str, Any]:
```
