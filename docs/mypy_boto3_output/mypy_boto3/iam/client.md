# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iam.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iam](index.md#iam) / Client
    - [Client](#client)
        - [Client().add_client_id_to_open_id_connect_provider](#clientadd_client_id_to_open_id_connect_provider)
        - [Client().add_role_to_instance_profile](#clientadd_role_to_instance_profile)
        - [Client().add_user_to_group](#clientadd_user_to_group)
        - [Client().attach_group_policy](#clientattach_group_policy)
        - [Client().attach_role_policy](#clientattach_role_policy)
        - [Client().attach_user_policy](#clientattach_user_policy)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().change_password](#clientchange_password)
        - [Client().create_access_key](#clientcreate_access_key)
        - [Client().create_account_alias](#clientcreate_account_alias)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_instance_profile](#clientcreate_instance_profile)
        - [Client().create_login_profile](#clientcreate_login_profile)
        - [Client().create_open_id_connect_provider](#clientcreate_open_id_connect_provider)
        - [Client().create_policy](#clientcreate_policy)
        - [Client().create_policy_version](#clientcreate_policy_version)
        - [Client().create_role](#clientcreate_role)
        - [Client().create_saml_provider](#clientcreate_saml_provider)
        - [Client().create_service_linked_role](#clientcreate_service_linked_role)
        - [Client().create_service_specific_credential](#clientcreate_service_specific_credential)
        - [Client().create_user](#clientcreate_user)
        - [Client().create_virtual_mfa_device](#clientcreate_virtual_mfa_device)
        - [Client().deactivate_mfa_device](#clientdeactivate_mfa_device)
        - [Client().delete_access_key](#clientdelete_access_key)
        - [Client().delete_account_alias](#clientdelete_account_alias)
        - [Client().delete_account_password_policy](#clientdelete_account_password_policy)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_group_policy](#clientdelete_group_policy)
        - [Client().delete_instance_profile](#clientdelete_instance_profile)
        - [Client().delete_login_profile](#clientdelete_login_profile)
        - [Client().delete_open_id_connect_provider](#clientdelete_open_id_connect_provider)
        - [Client().delete_policy](#clientdelete_policy)
        - [Client().delete_policy_version](#clientdelete_policy_version)
        - [Client().delete_role](#clientdelete_role)
        - [Client().delete_role_permissions_boundary](#clientdelete_role_permissions_boundary)
        - [Client().delete_role_policy](#clientdelete_role_policy)
        - [Client().delete_saml_provider](#clientdelete_saml_provider)
        - [Client().delete_server_certificate](#clientdelete_server_certificate)
        - [Client().delete_service_linked_role](#clientdelete_service_linked_role)
        - [Client().delete_service_specific_credential](#clientdelete_service_specific_credential)
        - [Client().delete_signing_certificate](#clientdelete_signing_certificate)
        - [Client().delete_ssh_public_key](#clientdelete_ssh_public_key)
        - [Client().delete_user](#clientdelete_user)
        - [Client().delete_user_permissions_boundary](#clientdelete_user_permissions_boundary)
        - [Client().delete_user_policy](#clientdelete_user_policy)
        - [Client().delete_virtual_mfa_device](#clientdelete_virtual_mfa_device)
        - [Client().detach_group_policy](#clientdetach_group_policy)
        - [Client().detach_role_policy](#clientdetach_role_policy)
        - [Client().detach_user_policy](#clientdetach_user_policy)
        - [Client().enable_mfa_device](#clientenable_mfa_device)
        - [Client().generate_credential_report](#clientgenerate_credential_report)
        - [Client().generate_organizations_access_report](#clientgenerate_organizations_access_report)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().generate_service_last_accessed_details](#clientgenerate_service_last_accessed_details)
        - [Client().get_access_key_last_used](#clientget_access_key_last_used)
        - [Client().get_account_authorization_details](#clientget_account_authorization_details)
        - [Client().get_account_password_policy](#clientget_account_password_policy)
        - [Client().get_account_summary](#clientget_account_summary)
        - [Client().get_context_keys_for_custom_policy](#clientget_context_keys_for_custom_policy)
        - [Client().get_context_keys_for_principal_policy](#clientget_context_keys_for_principal_policy)
        - [Client().get_credential_report](#clientget_credential_report)
        - [Client().get_group](#clientget_group)
        - [Client().get_group_policy](#clientget_group_policy)
        - [Client().get_instance_profile](#clientget_instance_profile)
        - [Client().get_login_profile](#clientget_login_profile)
        - [Client().get_open_id_connect_provider](#clientget_open_id_connect_provider)
        - [Client().get_organizations_access_report](#clientget_organizations_access_report)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_policy](#clientget_policy)
        - [Client().get_policy_version](#clientget_policy_version)
        - [Client().get_role](#clientget_role)
        - [Client().get_role_policy](#clientget_role_policy)
        - [Client().get_saml_provider](#clientget_saml_provider)
        - [Client().get_server_certificate](#clientget_server_certificate)
        - [Client().get_service_last_accessed_details](#clientget_service_last_accessed_details)
        - [Client().get_service_last_accessed_details_with_entities](#clientget_service_last_accessed_details_with_entities)
        - [Client().get_service_linked_role_deletion_status](#clientget_service_linked_role_deletion_status)
        - [Client().get_ssh_public_key](#clientget_ssh_public_key)
        - [Client().get_user](#clientget_user)
        - [Client().get_user_policy](#clientget_user_policy)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_access_keys](#clientlist_access_keys)
        - [Client().list_account_aliases](#clientlist_account_aliases)
        - [Client().list_attached_group_policies](#clientlist_attached_group_policies)
        - [Client().list_attached_role_policies](#clientlist_attached_role_policies)
        - [Client().list_attached_user_policies](#clientlist_attached_user_policies)
        - [Client().list_entities_for_policy](#clientlist_entities_for_policy)
        - [Client().list_group_policies](#clientlist_group_policies)
        - [Client().list_groups](#clientlist_groups)
        - [Client().list_groups_for_user](#clientlist_groups_for_user)
        - [Client().list_instance_profiles](#clientlist_instance_profiles)
        - [Client().list_instance_profiles_for_role](#clientlist_instance_profiles_for_role)
        - [Client().list_mfa_devices](#clientlist_mfa_devices)
        - [Client().list_open_id_connect_providers](#clientlist_open_id_connect_providers)
        - [Client().list_policies](#clientlist_policies)
        - [Client().list_policies_granting_service_access](#clientlist_policies_granting_service_access)
        - [Client().list_policy_versions](#clientlist_policy_versions)
        - [Client().list_role_policies](#clientlist_role_policies)
        - [Client().list_role_tags](#clientlist_role_tags)
        - [Client().list_roles](#clientlist_roles)
        - [Client().list_saml_providers](#clientlist_saml_providers)
        - [Client().list_server_certificates](#clientlist_server_certificates)
        - [Client().list_service_specific_credentials](#clientlist_service_specific_credentials)
        - [Client().list_signing_certificates](#clientlist_signing_certificates)
        - [Client().list_ssh_public_keys](#clientlist_ssh_public_keys)
        - [Client().list_user_policies](#clientlist_user_policies)
        - [Client().list_user_tags](#clientlist_user_tags)
        - [Client().list_users](#clientlist_users)
        - [Client().list_virtual_mfa_devices](#clientlist_virtual_mfa_devices)
        - [Client().put_group_policy](#clientput_group_policy)
        - [Client().put_role_permissions_boundary](#clientput_role_permissions_boundary)
        - [Client().put_role_policy](#clientput_role_policy)
        - [Client().put_user_permissions_boundary](#clientput_user_permissions_boundary)
        - [Client().put_user_policy](#clientput_user_policy)
        - [Client().remove_client_id_from_open_id_connect_provider](#clientremove_client_id_from_open_id_connect_provider)
        - [Client().remove_role_from_instance_profile](#clientremove_role_from_instance_profile)
        - [Client().remove_user_from_group](#clientremove_user_from_group)
        - [Client().reset_service_specific_credential](#clientreset_service_specific_credential)
        - [Client().resync_mfa_device](#clientresync_mfa_device)
        - [Client().set_default_policy_version](#clientset_default_policy_version)
        - [Client().set_security_token_service_preferences](#clientset_security_token_service_preferences)
        - [Client().simulate_custom_policy](#clientsimulate_custom_policy)
        - [Client().simulate_principal_policy](#clientsimulate_principal_policy)
        - [Client().tag_role](#clienttag_role)
        - [Client().tag_user](#clienttag_user)
        - [Client().untag_role](#clientuntag_role)
        - [Client().untag_user](#clientuntag_user)
        - [Client().update_access_key](#clientupdate_access_key)
        - [Client().update_account_password_policy](#clientupdate_account_password_policy)
        - [Client().update_assume_role_policy](#clientupdate_assume_role_policy)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_login_profile](#clientupdate_login_profile)
        - [Client().update_open_id_connect_provider_thumbprint](#clientupdate_open_id_connect_provider_thumbprint)
        - [Client().update_role](#clientupdate_role)
        - [Client().update_role_description](#clientupdate_role_description)
        - [Client().update_saml_provider](#clientupdate_saml_provider)
        - [Client().update_server_certificate](#clientupdate_server_certificate)
        - [Client().update_service_specific_credential](#clientupdate_service_specific_credential)
        - [Client().update_signing_certificate](#clientupdate_signing_certificate)
        - [Client().update_ssh_public_key](#clientupdate_ssh_public_key)
        - [Client().update_user](#clientupdate_user)
        - [Client().upload_server_certificate](#clientupload_server_certificate)
        - [Client().upload_signing_certificate](#clientupload_signing_certificate)
        - [Client().upload_ssh_public_key](#clientupload_ssh_public_key)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_client_id_to_open_id_connect_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L15)

```python
def add_client_id_to_open_id_connect_provider(
    OpenIDConnectProviderArn: str,
    ClientID: str,
) -> None:
```

### Client().add_role_to_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L21)

```python
def add_role_to_instance_profile(
    InstanceProfileName: str,
    RoleName: str,
) -> None:
```

### Client().add_user_to_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L27)

```python
def add_user_to_group(GroupName: str, UserName: str) -> None:
```

### Client().attach_group_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L31)

```python
def attach_group_policy(GroupName: str, PolicyArn: str) -> None:
```

### Client().attach_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L35)

```python
def attach_role_policy(RoleName: str, PolicyArn: str) -> None:
```

### Client().attach_user_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L39)

```python
def attach_user_policy(UserName: str, PolicyArn: str) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L43)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().change_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L47)

```python
def change_password(OldPassword: str, NewPassword: str) -> None:
```

### Client().create_access_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L51)

```python
def create_access_key(UserName: str = None) -> Dict[str, Any]:
```

### Client().create_account_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L55)

```python
def create_account_alias(AccountAlias: str) -> None:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L59)

```python
def create_group(GroupName: str, Path: str = None) -> Dict[str, Any]:
```

### Client().create_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L63)

```python
def create_instance_profile(
    InstanceProfileName: str,
    Path: str = None,
) -> Dict[str, Any]:
```

### Client().create_login_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L69)

```python
def create_login_profile(
    UserName: str,
    Password: str,
    PasswordResetRequired: bool = None,
) -> Dict[str, Any]:
```

### Client().create_open_id_connect_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L75)

```python
def create_open_id_connect_provider(
    Url: str,
    ThumbprintList: List[Any],
    ClientIDList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L81)

```python
def create_policy(
    PolicyName: str,
    PolicyDocument: str,
    Path: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L91)

```python
def create_policy_version(
    PolicyArn: str,
    PolicyDocument: str,
    SetAsDefault: bool = None,
) -> Dict[str, Any]:
```

### Client().create_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L97)

```python
def create_role(
    RoleName: str,
    AssumeRolePolicyDocument: str,
    Path: str = None,
    Description: str = None,
    MaxSessionDuration: int = None,
    PermissionsBoundary: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_saml_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L110)

```python
def create_saml_provider(
    SAMLMetadataDocument: str,
    Name: str,
) -> Dict[str, Any]:
```

### Client().create_service_linked_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L116)

```python
def create_service_linked_role(
    AWSServiceName: str,
    Description: str = None,
    CustomSuffix: str = None,
) -> Dict[str, Any]:
```

### Client().create_service_specific_credential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L122)

```python
def create_service_specific_credential(
    UserName: str,
    ServiceName: str,
) -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L128)

```python
def create_user(
    UserName: str,
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_virtual_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L138)

```python
def create_virtual_mfa_device(
    VirtualMFADeviceName: str,
    Path: str = None,
) -> Dict[str, Any]:
```

### Client().deactivate_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L144)

```python
def deactivate_mfa_device(UserName: str, SerialNumber: str) -> None:
```

### Client().delete_access_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L148)

```python
def delete_access_key(AccessKeyId: str, UserName: str = None) -> None:
```

### Client().delete_account_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L152)

```python
def delete_account_alias(AccountAlias: str) -> None:
```

### Client().delete_account_password_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L156)

```python
def delete_account_password_policy() -> None:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L160)

```python
def delete_group(GroupName: str) -> None:
```

### Client().delete_group_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L164)

```python
def delete_group_policy(GroupName: str, PolicyName: str) -> None:
```

### Client().delete_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L168)

```python
def delete_instance_profile(InstanceProfileName: str) -> None:
```

### Client().delete_login_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L172)

```python
def delete_login_profile(UserName: str) -> None:
```

### Client().delete_open_id_connect_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L176)

```python
def delete_open_id_connect_provider(OpenIDConnectProviderArn: str) -> None:
```

### Client().delete_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L180)

```python
def delete_policy(PolicyArn: str) -> None:
```

### Client().delete_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L184)

```python
def delete_policy_version(PolicyArn: str, VersionId: str) -> None:
```

### Client().delete_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L188)

```python
def delete_role(RoleName: str) -> None:
```

### Client().delete_role_permissions_boundary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L192)

```python
def delete_role_permissions_boundary(RoleName: str) -> None:
```

### Client().delete_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L196)

```python
def delete_role_policy(RoleName: str, PolicyName: str) -> None:
```

### Client().delete_saml_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L200)

```python
def delete_saml_provider(SAMLProviderArn: str) -> None:
```

### Client().delete_server_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L204)

```python
def delete_server_certificate(ServerCertificateName: str) -> None:
```

### Client().delete_service_linked_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L208)

```python
def delete_service_linked_role(RoleName: str) -> Dict[str, Any]:
```

### Client().delete_service_specific_credential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L212)

```python
def delete_service_specific_credential(
    ServiceSpecificCredentialId: str,
    UserName: str = None,
) -> None:
```

### Client().delete_signing_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L218)

```python
def delete_signing_certificate(
    CertificateId: str,
    UserName: str = None,
) -> None:
```

### Client().delete_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L224)

```python
def delete_ssh_public_key(UserName: str, SSHPublicKeyId: str) -> None:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L228)

```python
def delete_user(UserName: str) -> None:
```

### Client().delete_user_permissions_boundary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L232)

```python
def delete_user_permissions_boundary(UserName: str) -> None:
```

### Client().delete_user_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L236)

```python
def delete_user_policy(UserName: str, PolicyName: str) -> None:
```

### Client().delete_virtual_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L240)

```python
def delete_virtual_mfa_device(SerialNumber: str) -> None:
```

### Client().detach_group_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L244)

```python
def detach_group_policy(GroupName: str, PolicyArn: str) -> None:
```

### Client().detach_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L248)

```python
def detach_role_policy(RoleName: str, PolicyArn: str) -> None:
```

### Client().detach_user_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L252)

```python
def detach_user_policy(UserName: str, PolicyArn: str) -> None:
```

### Client().enable_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L256)

```python
def enable_mfa_device(
    UserName: str,
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str,
) -> None:
```

### Client().generate_credential_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L266)

```python
def generate_credential_report() -> Dict[str, Any]:
```

### Client().generate_organizations_access_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L270)

```python
def generate_organizations_access_report(
    EntityPath: str,
    OrganizationsPolicyId: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L276)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().generate_service_last_accessed_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L286)

```python
def generate_service_last_accessed_details(Arn: str) -> Dict[str, Any]:
```

### Client().get_access_key_last_used

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L290)

```python
def get_access_key_last_used(AccessKeyId: str) -> Dict[str, Any]:
```

### Client().get_account_authorization_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L294)

```python
def get_account_authorization_details(
    Filter: List[Any] = None,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_account_password_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L300)

```python
def get_account_password_policy() -> Dict[str, Any]:
```

### Client().get_account_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L304)

```python
def get_account_summary() -> Dict[str, Any]:
```

### Client().get_context_keys_for_custom_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L308)

```python
def get_context_keys_for_custom_policy(
    PolicyInputList: List[Any],
) -> Dict[str, Any]:
```

### Client().get_context_keys_for_principal_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L314)

```python
def get_context_keys_for_principal_policy(
    PolicySourceArn: str,
    PolicyInputList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_credential_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L320)

```python
def get_credential_report() -> Dict[str, Any]:
```

### Client().get_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L324)

```python
def get_group(
    GroupName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().get_group_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L330)

```python
def get_group_policy(GroupName: str, PolicyName: str) -> Dict[str, Any]:
```

### Client().get_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L334)

```python
def get_instance_profile(InstanceProfileName: str) -> Dict[str, Any]:
```

### Client().get_login_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L338)

```python
def get_login_profile(UserName: str) -> Dict[str, Any]:
```

### Client().get_open_id_connect_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L342)

```python
def get_open_id_connect_provider(
    OpenIDConnectProviderArn: str,
) -> Dict[str, Any]:
```

### Client().get_organizations_access_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L348)

```python
def get_organizations_access_report(
    JobId: str,
    MaxItems: int = None,
    Marker: str = None,
    SortKey: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L354)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L358)

```python
def get_policy(PolicyArn: str) -> Dict[str, Any]:
```

### Client().get_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L362)

```python
def get_policy_version(PolicyArn: str, VersionId: str) -> Dict[str, Any]:
```

### Client().get_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L366)

```python
def get_role(RoleName: str) -> Dict[str, Any]:
```

### Client().get_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L370)

```python
def get_role_policy(RoleName: str, PolicyName: str) -> Dict[str, Any]:
```

### Client().get_saml_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L374)

```python
def get_saml_provider(SAMLProviderArn: str) -> Dict[str, Any]:
```

### Client().get_server_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L378)

```python
def get_server_certificate(ServerCertificateName: str) -> Dict[str, Any]:
```

### Client().get_service_last_accessed_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L382)

```python
def get_service_last_accessed_details(
    JobId: str,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_service_last_accessed_details_with_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L388)

```python
def get_service_last_accessed_details_with_entities(
    JobId: str,
    ServiceNamespace: str,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_service_linked_role_deletion_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L398)

```python
def get_service_linked_role_deletion_status(
    DeletionTaskId: str,
) -> Dict[str, Any]:
```

### Client().get_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L404)

```python
def get_ssh_public_key(
    UserName: str,
    SSHPublicKeyId: str,
    Encoding: str,
) -> Dict[str, Any]:
```

### Client().get_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L410)

```python
def get_user(UserName: str = None) -> Dict[str, Any]:
```

### Client().get_user_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L414)

```python
def get_user_policy(UserName: str, PolicyName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L418)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_access_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L422)

```python
def list_access_keys(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_account_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L428)

```python
def list_account_aliases(
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_attached_group_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L434)

```python
def list_attached_group_policies(
    GroupName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_attached_role_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L444)

```python
def list_attached_role_policies(
    RoleName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_attached_user_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L454)

```python
def list_attached_user_policies(
    UserName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_entities_for_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L464)

```python
def list_entities_for_policy(
    PolicyArn: str,
    EntityFilter: str = None,
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_group_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L476)

```python
def list_group_policies(
    GroupName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L482)

```python
def list_groups(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_groups_for_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L488)

```python
def list_groups_for_user(
    UserName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_instance_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L494)

```python
def list_instance_profiles(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_instance_profiles_for_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L500)

```python
def list_instance_profiles_for_role(
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_mfa_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L506)

```python
def list_mfa_devices(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_open_id_connect_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L512)

```python
def list_open_id_connect_providers() -> Dict[str, Any]:
```

### Client().list_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L516)

```python
def list_policies(
    Scope: str = None,
    OnlyAttached: bool = None,
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_policies_granting_service_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L528)

```python
def list_policies_granting_service_access(
    Arn: str,
    ServiceNamespaces: List[Any],
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_policy_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L534)

```python
def list_policy_versions(
    PolicyArn: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_role_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L540)

```python
def list_role_policies(
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_role_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L546)

```python
def list_role_tags(
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L552)

```python
def list_roles(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_saml_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L558)

```python
def list_saml_providers() -> Dict[str, Any]:
```

### Client().list_server_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L562)

```python
def list_server_certificates(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_service_specific_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L568)

```python
def list_service_specific_credentials(
    UserName: str = None,
    ServiceName: str = None,
) -> Dict[str, Any]:
```

### Client().list_signing_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L574)

```python
def list_signing_certificates(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_ssh_public_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L580)

```python
def list_ssh_public_keys(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_user_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L586)

```python
def list_user_policies(
    UserName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_user_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L592)

```python
def list_user_tags(
    UserName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L598)

```python
def list_users(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_virtual_mfa_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L604)

```python
def list_virtual_mfa_devices(
    AssignmentStatus: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().put_group_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L610)

```python
def put_group_policy(
    GroupName: str,
    PolicyName: str,
    PolicyDocument: str,
) -> None:
```

### Client().put_role_permissions_boundary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L616)

```python
def put_role_permissions_boundary(
    RoleName: str,
    PermissionsBoundary: str,
) -> None:
```

### Client().put_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L622)

```python
def put_role_policy(
    RoleName: str,
    PolicyName: str,
    PolicyDocument: str,
) -> None:
```

### Client().put_user_permissions_boundary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L628)

```python
def put_user_permissions_boundary(
    UserName: str,
    PermissionsBoundary: str,
) -> None:
```

### Client().put_user_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L634)

```python
def put_user_policy(
    UserName: str,
    PolicyName: str,
    PolicyDocument: str,
) -> None:
```

### Client().remove_client_id_from_open_id_connect_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L640)

```python
def remove_client_id_from_open_id_connect_provider(
    OpenIDConnectProviderArn: str,
    ClientID: str,
) -> None:
```

### Client().remove_role_from_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L646)

```python
def remove_role_from_instance_profile(
    InstanceProfileName: str,
    RoleName: str,
) -> None:
```

### Client().remove_user_from_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L652)

```python
def remove_user_from_group(GroupName: str, UserName: str) -> None:
```

### Client().reset_service_specific_credential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L656)

```python
def reset_service_specific_credential(
    ServiceSpecificCredentialId: str,
    UserName: str = None,
) -> Dict[str, Any]:
```

### Client().resync_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L662)

```python
def resync_mfa_device(
    UserName: str,
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str,
) -> None:
```

### Client().set_default_policy_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L672)

```python
def set_default_policy_version(PolicyArn: str, VersionId: str) -> None:
```

### Client().set_security_token_service_preferences

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L676)

```python
def set_security_token_service_preferences(
    GlobalEndpointTokenVersion: str,
) -> None:
```

### Client().simulate_custom_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L682)

```python
def simulate_custom_policy(
    PolicyInputList: List[Any],
    ActionNames: List[Any],
    ResourceArns: List[Any] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[Any] = None,
    ResourceHandlingOption: str = None,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().simulate_principal_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L698)

```python
def simulate_principal_policy(
    PolicySourceArn: str,
    ActionNames: List[Any],
    PolicyInputList: List[Any] = None,
    ResourceArns: List[Any] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[Any] = None,
    ResourceHandlingOption: str = None,
    MaxItems: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().tag_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L715)

```python
def tag_role(RoleName: str, Tags: List[Any]) -> None:
```

### Client().tag_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L719)

```python
def tag_user(UserName: str, Tags: List[Any]) -> None:
```

### Client().untag_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L723)

```python
def untag_role(RoleName: str, TagKeys: List[Any]) -> None:
```

### Client().untag_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L727)

```python
def untag_user(UserName: str, TagKeys: List[Any]) -> None:
```

### Client().update_access_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L731)

```python
def update_access_key(
    AccessKeyId: str,
    Status: str,
    UserName: str = None,
) -> None:
```

### Client().update_account_password_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L737)

```python
def update_account_password_policy(
    MinimumPasswordLength: int = None,
    RequireSymbols: bool = None,
    RequireNumbers: bool = None,
    RequireUppercaseCharacters: bool = None,
    RequireLowercaseCharacters: bool = None,
    AllowUsersToChangePassword: bool = None,
    MaxPasswordAge: int = None,
    PasswordReusePrevention: int = None,
    HardExpiry: bool = None,
) -> None:
```

### Client().update_assume_role_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L752)

```python
def update_assume_role_policy(RoleName: str, PolicyDocument: str) -> None:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L756)

```python
def update_group(
    GroupName: str,
    NewPath: str = None,
    NewGroupName: str = None,
) -> None:
```

### Client().update_login_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L762)

```python
def update_login_profile(
    UserName: str,
    Password: str = None,
    PasswordResetRequired: bool = None,
) -> None:
```

### Client().update_open_id_connect_provider_thumbprint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L768)

```python
def update_open_id_connect_provider_thumbprint(
    OpenIDConnectProviderArn: str,
    ThumbprintList: List[Any],
) -> None:
```

### Client().update_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L774)

```python
def update_role(
    RoleName: str,
    Description: str = None,
    MaxSessionDuration: int = None,
) -> Dict[str, Any]:
```

### Client().update_role_description

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L780)

```python
def update_role_description(
    RoleName: str,
    Description: str,
) -> Dict[str, Any]:
```

### Client().update_saml_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L786)

```python
def update_saml_provider(
    SAMLMetadataDocument: str,
    SAMLProviderArn: str,
) -> Dict[str, Any]:
```

### Client().update_server_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L792)

```python
def update_server_certificate(
    ServerCertificateName: str,
    NewPath: str = None,
    NewServerCertificateName: str = None,
) -> None:
```

### Client().update_service_specific_credential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L801)

```python
def update_service_specific_credential(
    ServiceSpecificCredentialId: str,
    Status: str,
    UserName: str = None,
) -> None:
```

### Client().update_signing_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L807)

```python
def update_signing_certificate(
    CertificateId: str,
    Status: str,
    UserName: str = None,
) -> None:
```

### Client().update_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L813)

```python
def update_ssh_public_key(
    UserName: str,
    SSHPublicKeyId: str,
    Status: str,
) -> None:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L819)

```python
def update_user(
    UserName: str,
    NewPath: str = None,
    NewUserName: str = None,
) -> None:
```

### Client().upload_server_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L825)

```python
def upload_server_certificate(
    ServerCertificateName: str,
    CertificateBody: str,
    PrivateKey: str,
    Path: str = None,
    CertificateChain: str = None,
) -> Dict[str, Any]:
```

### Client().upload_signing_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L836)

```python
def upload_signing_certificate(
    CertificateBody: str,
    UserName: str = None,
) -> Dict[str, Any]:
```

### Client().upload_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/client.py#L842)

```python
def upload_ssh_public_key(
    UserName: str,
    SSHPublicKeyBody: str,
) -> Dict[str, Any]:
```
