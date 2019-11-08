# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iam.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iam](index.md#iam) / ServiceResource
    - [AccessKey](#accesskey)
        - [AccessKey().activate](#accesskeyactivate)
        - [AccessKey().deactivate](#accesskeydeactivate)
        - [AccessKey().delete](#accesskeydelete)
        - [AccessKey().get_available_subresources](#accesskeyget_available_subresources)
    - [AccessKeyPair](#accesskeypair)
        - [AccessKeyPair().activate](#accesskeypairactivate)
        - [AccessKeyPair().deactivate](#accesskeypairdeactivate)
        - [AccessKeyPair().delete](#accesskeypairdelete)
        - [AccessKeyPair().get_available_subresources](#accesskeypairget_available_subresources)
    - [AccountPasswordPolicy](#accountpasswordpolicy)
        - [AccountPasswordPolicy().delete](#accountpasswordpolicydelete)
        - [AccountPasswordPolicy().get_available_subresources](#accountpasswordpolicyget_available_subresources)
        - [AccountPasswordPolicy().load](#accountpasswordpolicyload)
        - [AccountPasswordPolicy().reload](#accountpasswordpolicyreload)
        - [AccountPasswordPolicy().update](#accountpasswordpolicyupdate)
    - [AccountSummary](#accountsummary)
        - [AccountSummary().get_available_subresources](#accountsummaryget_available_subresources)
        - [AccountSummary().load](#accountsummaryload)
        - [AccountSummary().reload](#accountsummaryreload)
    - [AssumeRolePolicy](#assumerolepolicy)
        - [AssumeRolePolicy().get_available_subresources](#assumerolepolicyget_available_subresources)
        - [AssumeRolePolicy().update](#assumerolepolicyupdate)
    - [CurrentUser](#currentuser)
        - [CurrentUser().get_available_subresources](#currentuserget_available_subresources)
        - [CurrentUser().load](#currentuserload)
        - [CurrentUser().reload](#currentuserreload)
    - [Group](#group)
        - [Group().add_user](#groupadd_user)
        - [Group().attach_policy](#groupattach_policy)
        - [Group().create](#groupcreate)
        - [Group().create_policy](#groupcreate_policy)
        - [Group().delete](#groupdelete)
        - [Group().detach_policy](#groupdetach_policy)
        - [Group().get_available_subresources](#groupget_available_subresources)
        - [Group().load](#groupload)
        - [Group().reload](#groupreload)
        - [Group().remove_user](#groupremove_user)
        - [Group().update](#groupupdate)
    - [GroupPolicy](#grouppolicy)
        - [GroupPolicy().delete](#grouppolicydelete)
        - [GroupPolicy().get_available_subresources](#grouppolicyget_available_subresources)
        - [GroupPolicy().load](#grouppolicyload)
        - [GroupPolicy().put](#grouppolicyput)
        - [GroupPolicy().reload](#grouppolicyreload)
    - [InstanceProfile](#instanceprofile)
        - [InstanceProfile().add_role](#instanceprofileadd_role)
        - [InstanceProfile().delete](#instanceprofiledelete)
        - [InstanceProfile().get_available_subresources](#instanceprofileget_available_subresources)
        - [InstanceProfile().load](#instanceprofileload)
        - [InstanceProfile().reload](#instanceprofilereload)
        - [InstanceProfile().remove_role](#instanceprofileremove_role)
    - [LoginProfile](#loginprofile)
        - [LoginProfile().create](#loginprofilecreate)
        - [LoginProfile().delete](#loginprofiledelete)
        - [LoginProfile().get_available_subresources](#loginprofileget_available_subresources)
        - [LoginProfile().load](#loginprofileload)
        - [LoginProfile().reload](#loginprofilereload)
        - [LoginProfile().update](#loginprofileupdate)
    - [MfaDevice](#mfadevice)
        - [MfaDevice().associate](#mfadeviceassociate)
        - [MfaDevice().disassociate](#mfadevicedisassociate)
        - [MfaDevice().get_available_subresources](#mfadeviceget_available_subresources)
        - [MfaDevice().resync](#mfadeviceresync)
    - [Policy](#policy)
        - [Policy().attach_group](#policyattach_group)
        - [Policy().attach_role](#policyattach_role)
        - [Policy().attach_user](#policyattach_user)
        - [Policy().create_version](#policycreate_version)
        - [Policy().delete](#policydelete)
        - [Policy().detach_group](#policydetach_group)
        - [Policy().detach_role](#policydetach_role)
        - [Policy().detach_user](#policydetach_user)
        - [Policy().get_available_subresources](#policyget_available_subresources)
        - [Policy().load](#policyload)
        - [Policy().reload](#policyreload)
    - [PolicyVersion](#policyversion)
        - [PolicyVersion().delete](#policyversiondelete)
        - [PolicyVersion().get_available_subresources](#policyversionget_available_subresources)
        - [PolicyVersion().load](#policyversionload)
        - [PolicyVersion().reload](#policyversionreload)
        - [PolicyVersion().set_as_default](#policyversionset_as_default)
    - [Role](#role)
        - [Role().attach_policy](#roleattach_policy)
        - [Role().delete](#roledelete)
        - [Role().detach_policy](#roledetach_policy)
        - [Role().get_available_subresources](#roleget_available_subresources)
        - [Role().load](#roleload)
        - [Role().reload](#rolereload)
    - [RolePolicy](#rolepolicy)
        - [RolePolicy().delete](#rolepolicydelete)
        - [RolePolicy().get_available_subresources](#rolepolicyget_available_subresources)
        - [RolePolicy().load](#rolepolicyload)
        - [RolePolicy().put](#rolepolicyput)
        - [RolePolicy().reload](#rolepolicyreload)
    - [SamlProvider](#samlprovider)
        - [SamlProvider().delete](#samlproviderdelete)
        - [SamlProvider().get_available_subresources](#samlproviderget_available_subresources)
        - [SamlProvider().load](#samlproviderload)
        - [SamlProvider().reload](#samlproviderreload)
        - [SamlProvider().update](#samlproviderupdate)
    - [ServerCertificate](#servercertificate)
        - [ServerCertificate().delete](#servercertificatedelete)
        - [ServerCertificate().get_available_subresources](#servercertificateget_available_subresources)
        - [ServerCertificate().load](#servercertificateload)
        - [ServerCertificate().reload](#servercertificatereload)
        - [ServerCertificate().update](#servercertificateupdate)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().AccessKey](#serviceresourceaccesskey)
        - [ServiceResource().AccessKeyPair](#serviceresourceaccesskeypair)
        - [ServiceResource().AccountPasswordPolicy](#serviceresourceaccountpasswordpolicy)
        - [ServiceResource().AccountSummary](#serviceresourceaccountsummary)
        - [ServiceResource().AssumeRolePolicy](#serviceresourceassumerolepolicy)
        - [ServiceResource().CurrentUser](#serviceresourcecurrentuser)
        - [ServiceResource().Group](#serviceresourcegroup)
        - [ServiceResource().GroupPolicy](#serviceresourcegrouppolicy)
        - [ServiceResource().InstanceProfile](#serviceresourceinstanceprofile)
        - [ServiceResource().LoginProfile](#serviceresourceloginprofile)
        - [ServiceResource().MfaDevice](#serviceresourcemfadevice)
        - [ServiceResource().Policy](#serviceresourcepolicy)
        - [ServiceResource().PolicyVersion](#serviceresourcepolicyversion)
        - [ServiceResource().Role](#serviceresourcerole)
        - [ServiceResource().RolePolicy](#serviceresourcerolepolicy)
        - [ServiceResource().SamlProvider](#serviceresourcesamlprovider)
        - [ServiceResource().ServerCertificate](#serviceresourceservercertificate)
        - [ServiceResource().SigningCertificate](#serviceresourcesigningcertificate)
        - [ServiceResource().User](#serviceresourceuser)
        - [ServiceResource().UserPolicy](#serviceresourceuserpolicy)
        - [ServiceResource().VirtualMfaDevice](#serviceresourcevirtualmfadevice)
        - [ServiceResource().change_password](#serviceresourcechange_password)
        - [ServiceResource().create_account_alias](#serviceresourcecreate_account_alias)
        - [ServiceResource().create_account_password_policy](#serviceresourcecreate_account_password_policy)
        - [ServiceResource().create_group](#serviceresourcecreate_group)
        - [ServiceResource().create_instance_profile](#serviceresourcecreate_instance_profile)
        - [ServiceResource().create_policy](#serviceresourcecreate_policy)
        - [ServiceResource().create_role](#serviceresourcecreate_role)
        - [ServiceResource().create_saml_provider](#serviceresourcecreate_saml_provider)
        - [ServiceResource().create_server_certificate](#serviceresourcecreate_server_certificate)
        - [ServiceResource().create_signing_certificate](#serviceresourcecreate_signing_certificate)
        - [ServiceResource().create_user](#serviceresourcecreate_user)
        - [ServiceResource().create_virtual_mfa_device](#serviceresourcecreate_virtual_mfa_device)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [SigningCertificate](#signingcertificate)
        - [SigningCertificate().activate](#signingcertificateactivate)
        - [SigningCertificate().deactivate](#signingcertificatedeactivate)
        - [SigningCertificate().delete](#signingcertificatedelete)
        - [SigningCertificate().get_available_subresources](#signingcertificateget_available_subresources)
    - [User](#user)
        - [User().add_group](#useradd_group)
        - [User().attach_policy](#userattach_policy)
        - [User().create](#usercreate)
        - [User().create_access_key_pair](#usercreate_access_key_pair)
        - [User().create_login_profile](#usercreate_login_profile)
        - [User().create_policy](#usercreate_policy)
        - [User().delete](#userdelete)
        - [User().detach_policy](#userdetach_policy)
        - [User().enable_mfa](#userenable_mfa)
        - [User().get_available_subresources](#userget_available_subresources)
        - [User().load](#userload)
        - [User().reload](#userreload)
        - [User().remove_group](#userremove_group)
        - [User().update](#userupdate)
    - [UserPolicy](#userpolicy)
        - [UserPolicy().delete](#userpolicydelete)
        - [UserPolicy().get_available_subresources](#userpolicyget_available_subresources)
        - [UserPolicy().load](#userpolicyload)
        - [UserPolicy().put](#userpolicyput)
        - [UserPolicy().reload](#userpolicyreload)
    - [VirtualMfaDevice](#virtualmfadevice)
        - [VirtualMfaDevice().delete](#virtualmfadevicedelete)
        - [VirtualMfaDevice().get_available_subresources](#virtualmfadeviceget_available_subresources)
    - [access_keys](#access_keys)
        - [access_keys.all](#access_keysall)
        - [access_keys.filter](#access_keysfilter)
        - [access_keys.iterator](#access_keysiterator)
        - [access_keys.limit](#access_keyslimit)
        - [access_keys.page_size](#access_keyspage_size)
        - [access_keys.pages](#access_keyspages)
    - [attached_groups](#attached_groups)
        - [attached_groups.all](#attached_groupsall)
        - [attached_groups.filter](#attached_groupsfilter)
        - [attached_groups.iterator](#attached_groupsiterator)
        - [attached_groups.limit](#attached_groupslimit)
        - [attached_groups.page_size](#attached_groupspage_size)
        - [attached_groups.pages](#attached_groupspages)
    - [attached_policies](#attached_policies)
        - [attached_policies.all](#attached_policiesall)
        - [attached_policies.filter](#attached_policiesfilter)
        - [attached_policies.iterator](#attached_policiesiterator)
        - [attached_policies.limit](#attached_policieslimit)
        - [attached_policies.page_size](#attached_policiespage_size)
        - [attached_policies.pages](#attached_policiespages)
    - [attached_roles](#attached_roles)
        - [attached_roles.all](#attached_rolesall)
        - [attached_roles.filter](#attached_rolesfilter)
        - [attached_roles.iterator](#attached_rolesiterator)
        - [attached_roles.limit](#attached_roleslimit)
        - [attached_roles.page_size](#attached_rolespage_size)
        - [attached_roles.pages](#attached_rolespages)
    - [attached_users](#attached_users)
        - [attached_users.all](#attached_usersall)
        - [attached_users.filter](#attached_usersfilter)
        - [attached_users.iterator](#attached_usersiterator)
        - [attached_users.limit](#attached_userslimit)
        - [attached_users.page_size](#attached_userspage_size)
        - [attached_users.pages](#attached_userspages)
    - [groups](#groups)
        - [groups.all](#groupsall)
        - [groups.filter](#groupsfilter)
        - [groups.iterator](#groupsiterator)
        - [groups.limit](#groupslimit)
        - [groups.page_size](#groupspage_size)
        - [groups.pages](#groupspages)
    - [instance_profiles](#instance_profiles)
        - [instance_profiles.all](#instance_profilesall)
        - [instance_profiles.filter](#instance_profilesfilter)
        - [instance_profiles.iterator](#instance_profilesiterator)
        - [instance_profiles.limit](#instance_profileslimit)
        - [instance_profiles.page_size](#instance_profilespage_size)
        - [instance_profiles.pages](#instance_profilespages)
    - [mfa_devices](#mfa_devices)
        - [mfa_devices.all](#mfa_devicesall)
        - [mfa_devices.filter](#mfa_devicesfilter)
        - [mfa_devices.iterator](#mfa_devicesiterator)
        - [mfa_devices.limit](#mfa_deviceslimit)
        - [mfa_devices.page_size](#mfa_devicespage_size)
        - [mfa_devices.pages](#mfa_devicespages)
    - [policies](#policies)
        - [policies.all](#policiesall)
        - [policies.filter](#policiesfilter)
        - [policies.iterator](#policiesiterator)
        - [policies.limit](#policieslimit)
        - [policies.page_size](#policiespage_size)
        - [policies.pages](#policiespages)
    - [roles](#roles)
        - [roles.all](#rolesall)
        - [roles.filter](#rolesfilter)
        - [roles.iterator](#rolesiterator)
        - [roles.limit](#roleslimit)
        - [roles.page_size](#rolespage_size)
        - [roles.pages](#rolespages)
    - [saml_providers](#saml_providers)
        - [saml_providers.all](#saml_providersall)
        - [saml_providers.filter](#saml_providersfilter)
        - [saml_providers.iterator](#saml_providersiterator)
        - [saml_providers.limit](#saml_providerslimit)
        - [saml_providers.page_size](#saml_providerspage_size)
        - [saml_providers.pages](#saml_providerspages)
    - [server_certificates](#server_certificates)
        - [server_certificates.all](#server_certificatesall)
        - [server_certificates.filter](#server_certificatesfilter)
        - [server_certificates.iterator](#server_certificatesiterator)
        - [server_certificates.limit](#server_certificateslimit)
        - [server_certificates.page_size](#server_certificatespage_size)
        - [server_certificates.pages](#server_certificatespages)
    - [signing_certificates](#signing_certificates)
        - [signing_certificates.all](#signing_certificatesall)
        - [signing_certificates.filter](#signing_certificatesfilter)
        - [signing_certificates.iterator](#signing_certificatesiterator)
        - [signing_certificates.limit](#signing_certificateslimit)
        - [signing_certificates.page_size](#signing_certificatespage_size)
        - [signing_certificates.pages](#signing_certificatespages)
    - [users](#users)
        - [users.all](#usersall)
        - [users.filter](#usersfilter)
        - [users.iterator](#usersiterator)
        - [users.limit](#userslimit)
        - [users.page_size](#userspage_size)
        - [users.pages](#userspages)
    - [versions](#versions)
        - [versions.all](#versionsall)
        - [versions.filter](#versionsfilter)
        - [versions.iterator](#versionsiterator)
        - [versions.limit](#versionslimit)
        - [versions.page_size](#versionspage_size)
        - [versions.pages](#versionspages)
    - [virtual_mfa_devices](#virtual_mfa_devices)
        - [virtual_mfa_devices.all](#virtual_mfa_devicesall)
        - [virtual_mfa_devices.filter](#virtual_mfa_devicesfilter)
        - [virtual_mfa_devices.iterator](#virtual_mfa_devicesiterator)
        - [virtual_mfa_devices.limit](#virtual_mfa_deviceslimit)
        - [virtual_mfa_devices.page_size](#virtual_mfa_devicespage_size)
        - [virtual_mfa_devices.pages](#virtual_mfa_devicespages)

## AccessKey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L237)

```python
class AccessKey(Boto3ServiceResource):
```

### AccessKey().activate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L245)

```python
def activate() -> None:
```

### AccessKey().deactivate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L249)

```python
def deactivate() -> None:
```

### AccessKey().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L253)

```python
def delete() -> None:
```

### AccessKey().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L257)

```python
def get_available_subresources() -> List[str]:
```

## AccessKeyPair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L261)

```python
class AccessKeyPair(Boto3ServiceResource):
```

### AccessKeyPair().activate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L271)

```python
def activate() -> None:
```

### AccessKeyPair().deactivate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L275)

```python
def deactivate() -> None:
```

### AccessKeyPair().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L279)

```python
def delete() -> None:
```

### AccessKeyPair().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L283)

```python
def get_available_subresources() -> List[str]:
```

## AccountPasswordPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L287)

```python
class AccountPasswordPolicy(Boto3ServiceResource):
```

### AccountPasswordPolicy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L300)

```python
def delete() -> None:
```

### AccountPasswordPolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L304)

```python
def get_available_subresources() -> List[str]:
```

### AccountPasswordPolicy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L308)

```python
def load() -> None:
```

### AccountPasswordPolicy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L312)

```python
def reload() -> None:
```

### AccountPasswordPolicy().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L316)

```python
def update(
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

## AccountSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L331)

```python
class AccountSummary(Boto3ServiceResource):
```

### AccountSummary().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L335)

```python
def get_available_subresources() -> List[str]:
```

### AccountSummary().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L339)

```python
def load() -> None:
```

### AccountSummary().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L343)

```python
def reload() -> None:
```

## AssumeRolePolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L347)

```python
class AssumeRolePolicy(Boto3ServiceResource):
```

### AssumeRolePolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L351)

```python
def get_available_subresources() -> List[str]:
```

### AssumeRolePolicy().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L355)

```python
def update(PolicyDocument: str) -> None:
```

## CurrentUser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L359)

```python
class CurrentUser(Boto3ServiceResource):
```

### CurrentUser().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L373)

```python
def get_available_subresources() -> List[str]:
```

### CurrentUser().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L377)

```python
def load() -> None:
```

### CurrentUser().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L381)

```python
def reload() -> None:
```

## Group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L385)

```python
class Group(Boto3ServiceResource):
```

### Group().add_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L397)

```python
def add_user(UserName: str) -> None:
```

### Group().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L401)

```python
def attach_policy(PolicyArn: str) -> None:
```

### Group().create

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L405)

```python
def create(Path: str = None) -> List[iam_service_resource_scope.Group]:
```

### Group().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L409)

```python
def create_policy(
    PolicyName: str,
    PolicyDocument: str,
) -> iam_service_resource_scope.GroupPolicy:
```

### Group().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L415)

```python
def delete() -> None:
```

### Group().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L419)

```python
def detach_policy(PolicyArn: str) -> None:
```

### Group().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L423)

```python
def get_available_subresources() -> List[str]:
```

### Group().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L427)

```python
def load() -> None:
```

### Group().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L431)

```python
def reload() -> None:
```

### Group().remove_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L435)

```python
def remove_user(UserName: str) -> None:
```

### Group().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L439)

```python
def update(
    NewPath: str = None,
    NewGroupName: str = None,
) -> List[iam_service_resource_scope.Group]:
```

## GroupPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L445)

```python
class GroupPolicy(Boto3ServiceResource):
```

### GroupPolicy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L452)

```python
def delete() -> None:
```

### GroupPolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L456)

```python
def get_available_subresources() -> List[str]:
```

### GroupPolicy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L460)

```python
def load() -> None:
```

### GroupPolicy().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L464)

```python
def put(PolicyDocument: str) -> None:
```

### GroupPolicy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L468)

```python
def reload() -> None:
```

## InstanceProfile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L472)

```python
class InstanceProfile(Boto3ServiceResource):
```

### InstanceProfile().add_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L482)

```python
def add_role(RoleName: str) -> None:
```

### InstanceProfile().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L486)

```python
def delete() -> None:
```

### InstanceProfile().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L490)

```python
def get_available_subresources() -> List[str]:
```

### InstanceProfile().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L494)

```python
def load() -> None:
```

### InstanceProfile().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L498)

```python
def reload() -> None:
```

### InstanceProfile().remove_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L502)

```python
def remove_role(RoleName: str) -> None:
```

## LoginProfile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L506)

```python
class LoginProfile(Boto3ServiceResource):
```

### LoginProfile().create

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L512)

```python
def create(
    Password: str,
    PasswordResetRequired: bool = None,
) -> iam_service_resource_scope.LoginProfile:
```

### LoginProfile().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L518)

```python
def delete() -> None:
```

### LoginProfile().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L522)

```python
def get_available_subresources() -> List[str]:
```

### LoginProfile().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L526)

```python
def load() -> None:
```

### LoginProfile().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L530)

```python
def reload() -> None:
```

### LoginProfile().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L534)

```python
def update(Password: str = None, PasswordResetRequired: bool = None) -> None:
```

## MfaDevice

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L538)

```python
class MfaDevice(Boto3ServiceResource):
```

### MfaDevice().associate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L544)

```python
def associate(AuthenticationCode1: str, AuthenticationCode2: str) -> None:
```

### MfaDevice().disassociate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L548)

```python
def disassociate() -> None:
```

### MfaDevice().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L552)

```python
def get_available_subresources() -> List[str]:
```

### MfaDevice().resync

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L556)

```python
def resync(AuthenticationCode1: str, AuthenticationCode2: str) -> None:
```

## Policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L560)

```python
class Policy(Boto3ServiceResource):
```

### Policy().attach_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L578)

```python
def attach_group(GroupName: str) -> None:
```

### Policy().attach_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L582)

```python
def attach_role(RoleName: str) -> None:
```

### Policy().attach_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L586)

```python
def attach_user(UserName: str) -> None:
```

### Policy().create_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L590)

```python
def create_version(
    PolicyDocument: str,
    SetAsDefault: bool = None,
) -> iam_service_resource_scope.PolicyVersion:
```

### Policy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L596)

```python
def delete() -> None:
```

### Policy().detach_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L600)

```python
def detach_group(GroupName: str) -> None:
```

### Policy().detach_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L604)

```python
def detach_role(RoleName: str) -> None:
```

### Policy().detach_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L608)

```python
def detach_user(UserName: str) -> None:
```

### Policy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L612)

```python
def get_available_subresources() -> List[str]:
```

### Policy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L616)

```python
def load() -> None:
```

### Policy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L620)

```python
def reload() -> None:
```

## PolicyVersion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L624)

```python
class PolicyVersion(Boto3ServiceResource):
```

### PolicyVersion().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L632)

```python
def delete() -> None:
```

### PolicyVersion().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L636)

```python
def get_available_subresources() -> List[str]:
```

### PolicyVersion().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L640)

```python
def load() -> None:
```

### PolicyVersion().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L644)

```python
def reload() -> None:
```

### PolicyVersion().set_as_default

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L648)

```python
def set_as_default() -> None:
```

## Role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L652)

```python
class Role(Boto3ServiceResource):
```

### Role().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L669)

```python
def attach_policy(PolicyArn: str) -> None:
```

### Role().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L673)

```python
def delete() -> None:
```

### Role().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L677)

```python
def detach_policy(PolicyArn: str) -> None:
```

### Role().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L681)

```python
def get_available_subresources() -> List[str]:
```

### Role().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L685)

```python
def load() -> None:
```

### Role().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L689)

```python
def reload() -> None:
```

## RolePolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L693)

```python
class RolePolicy(Boto3ServiceResource):
```

### RolePolicy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L700)

```python
def delete() -> None:
```

### RolePolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L704)

```python
def get_available_subresources() -> List[str]:
```

### RolePolicy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L708)

```python
def load() -> None:
```

### RolePolicy().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L712)

```python
def put(PolicyDocument: str) -> None:
```

### RolePolicy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L716)

```python
def reload() -> None:
```

## SamlProvider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L720)

```python
class SamlProvider(Boto3ServiceResource):
```

### SamlProvider().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L727)

```python
def delete() -> None:
```

### SamlProvider().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L731)

```python
def get_available_subresources() -> List[str]:
```

### SamlProvider().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L735)

```python
def load() -> None:
```

### SamlProvider().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L739)

```python
def reload() -> None:
```

### SamlProvider().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L743)

```python
def update(SAMLMetadataDocument: str) -> Dict[str, Any]:
```

## ServerCertificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L747)

```python
class ServerCertificate(Boto3ServiceResource):
```

### ServerCertificate().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L754)

```python
def delete() -> None:
```

### ServerCertificate().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L758)

```python
def get_available_subresources() -> List[str]:
```

### ServerCertificate().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L762)

```python
def load() -> None:
```

### ServerCertificate().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L766)

```python
def reload() -> None:
```

### ServerCertificate().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L770)

```python
def update(
    NewPath: str = None,
    NewServerCertificateName: str = None,
) -> iam_service_resource_scope.ServerCertificate:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L15)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().AccessKey

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L26)

```python
def AccessKey(
    user_name: str = None,
    id: str = None,
) -> iam_service_resource_scope.AccessKey:
```

### ServiceResource().AccessKeyPair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L32)

```python
def AccessKeyPair(
    user_name: str = None,
    id: str = None,
    secret: str = None,
) -> iam_service_resource_scope.AccessKeyPair:
```

### ServiceResource().AccountPasswordPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L38)

```python
def AccountPasswordPolicy() -> iam_service_resource_scope.AccountPasswordPolicy:
```

### ServiceResource().AccountSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L42)

```python
def AccountSummary() -> iam_service_resource_scope.AccountSummary:
```

### ServiceResource().AssumeRolePolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L46)

```python
def AssumeRolePolicy(
    role_name: str = None,
) -> iam_service_resource_scope.AssumeRolePolicy:
```

### ServiceResource().CurrentUser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L52)

```python
def CurrentUser() -> iam_service_resource_scope.CurrentUser:
```

### ServiceResource().Group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L56)

```python
def Group(name: str = None) -> iam_service_resource_scope.Group:
```

### ServiceResource().GroupPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L60)

```python
def GroupPolicy(
    group_name: str = None,
    name: str = None,
) -> iam_service_resource_scope.GroupPolicy:
```

### ServiceResource().InstanceProfile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L66)

```python
def InstanceProfile(
    name: str = None,
) -> iam_service_resource_scope.InstanceProfile:
```

### ServiceResource().LoginProfile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L72)

```python
def LoginProfile(
    user_name: str = None,
) -> iam_service_resource_scope.LoginProfile:
```

### ServiceResource().MfaDevice

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L78)

```python
def MfaDevice(
    user_name: str = None,
    serial_number: str = None,
) -> iam_service_resource_scope.MfaDevice:
```

### ServiceResource().Policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L84)

```python
def Policy(policy_arn: str = None) -> iam_service_resource_scope.Policy:
```

### ServiceResource().PolicyVersion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L88)

```python
def PolicyVersion(
    arn: str = None,
    version_id: str = None,
) -> iam_service_resource_scope.PolicyVersion:
```

### ServiceResource().Role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L94)

```python
def Role(name: str = None) -> iam_service_resource_scope.Role:
```

### ServiceResource().RolePolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L98)

```python
def RolePolicy(
    role_name: str = None,
    name: str = None,
) -> iam_service_resource_scope.RolePolicy:
```

### ServiceResource().SamlProvider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L104)

```python
def SamlProvider(arn: str = None) -> iam_service_resource_scope.SamlProvider:
```

### ServiceResource().ServerCertificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L108)

```python
def ServerCertificate(
    name: str = None,
) -> iam_service_resource_scope.ServerCertificate:
```

### ServiceResource().SigningCertificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L114)

```python
def SigningCertificate(
    user_name: str = None,
    id: str = None,
) -> iam_service_resource_scope.SigningCertificate:
```

### ServiceResource().User

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L120)

```python
def User(name: str = None) -> iam_service_resource_scope.User:
```

### ServiceResource().UserPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L124)

```python
def UserPolicy(
    user_name: str = None,
    name: str = None,
) -> iam_service_resource_scope.UserPolicy:
```

### ServiceResource().VirtualMfaDevice

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L130)

```python
def VirtualMfaDevice(
    serial_number: str = None,
) -> iam_service_resource_scope.VirtualMfaDevice:
```

### ServiceResource().change_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L136)

```python
def change_password(OldPassword: str, NewPassword: str) -> None:
```

### ServiceResource().create_account_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L140)

```python
def create_account_alias(AccountAlias: str) -> None:
```

### ServiceResource().create_account_password_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L144)

```python
def create_account_password_policy(
    MinimumPasswordLength: int = None,
    RequireSymbols: bool = None,
    RequireNumbers: bool = None,
    RequireUppercaseCharacters: bool = None,
    RequireLowercaseCharacters: bool = None,
    AllowUsersToChangePassword: bool = None,
    MaxPasswordAge: int = None,
    PasswordReusePrevention: int = None,
    HardExpiry: bool = None,
) -> iam_service_resource_scope.AccountPasswordPolicy:
```

### ServiceResource().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L159)

```python
def create_group(
    GroupName: str,
    Path: str = None,
) -> List[iam_service_resource_scope.Group]:
```

### ServiceResource().create_instance_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L165)

```python
def create_instance_profile(
    InstanceProfileName: str,
    Path: str = None,
) -> iam_service_resource_scope.InstanceProfile:
```

### ServiceResource().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L171)

```python
def create_policy(
    PolicyName: str,
    PolicyDocument: str,
    Path: str = None,
    Description: str = None,
) -> iam_service_resource_scope.Policy:
```

### ServiceResource().create_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L181)

```python
def create_role(
    RoleName: str,
    AssumeRolePolicyDocument: str,
    Path: str = None,
    Description: str = None,
    MaxSessionDuration: int = None,
    PermissionsBoundary: str = None,
    Tags: List[Any] = None,
) -> iam_service_resource_scope.Role:
```

### ServiceResource().create_saml_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L194)

```python
def create_saml_provider(
    SAMLMetadataDocument: str,
    Name: str,
) -> iam_service_resource_scope.SamlProvider:
```

### ServiceResource().create_server_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L200)

```python
def create_server_certificate(
    ServerCertificateName: str,
    CertificateBody: str,
    PrivateKey: str,
    Path: str = None,
    CertificateChain: str = None,
) -> iam_service_resource_scope.ServerCertificate:
```

### ServiceResource().create_signing_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L211)

```python
def create_signing_certificate(
    CertificateBody: str,
    UserName: str = None,
) -> iam_service_resource_scope.SigningCertificate:
```

### ServiceResource().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L217)

```python
def create_user(
    UserName: str,
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List[Any] = None,
) -> iam_service_resource_scope.User:
```

### ServiceResource().create_virtual_mfa_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L227)

```python
def create_virtual_mfa_device(
    VirtualMFADeviceName: str,
    Path: str = None,
) -> iam_service_resource_scope.VirtualMfaDevice:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L233)

```python
def get_available_subresources() -> List[str]:
```

## SigningCertificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L776)

```python
class SigningCertificate(Boto3ServiceResource):
```

### SigningCertificate().activate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L785)

```python
def activate() -> None:
```

### SigningCertificate().deactivate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L789)

```python
def deactivate() -> None:
```

### SigningCertificate().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L793)

```python
def delete() -> None:
```

### SigningCertificate().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L797)

```python
def get_available_subresources() -> List[str]:
```

## User

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L801)

```python
class User(Boto3ServiceResource):
```

### User().add_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L819)

```python
def add_group(GroupName: str) -> None:
```

### User().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L823)

```python
def attach_policy(PolicyArn: str) -> None:
```

### User().create

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L827)

```python
def create(
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List[Any] = None,
) -> iam_service_resource_scope.User:
```

### User().create_access_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L833)

```python
def create_access_key_pair() -> iam_service_resource_scope.AccessKeyPair:
```

### User().create_login_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L837)

```python
def create_login_profile(
    Password: str,
    PasswordResetRequired: bool = None,
) -> iam_service_resource_scope.LoginProfile:
```

### User().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L843)

```python
def create_policy(
    PolicyName: str,
    PolicyDocument: str,
) -> iam_service_resource_scope.UserPolicy:
```

### User().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L849)

```python
def delete() -> None:
```

### User().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L853)

```python
def detach_policy(PolicyArn: str) -> None:
```

### User().enable_mfa

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L857)

```python
def enable_mfa(
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str,
) -> iam_service_resource_scope.MfaDevice:
```

### User().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L863)

```python
def get_available_subresources() -> List[str]:
```

### User().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L867)

```python
def load() -> None:
```

### User().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L871)

```python
def reload() -> None:
```

### User().remove_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L875)

```python
def remove_group(GroupName: str) -> None:
```

### User().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L879)

```python
def update(
    NewPath: str = None,
    NewUserName: str = None,
) -> iam_service_resource_scope.User:
```

## UserPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L885)

```python
class UserPolicy(Boto3ServiceResource):
```

### UserPolicy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L892)

```python
def delete() -> None:
```

### UserPolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L896)

```python
def get_available_subresources() -> List[str]:
```

### UserPolicy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L900)

```python
def load() -> None:
```

### UserPolicy().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L904)

```python
def put(PolicyDocument: str) -> None:
```

### UserPolicy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L908)

```python
def reload() -> None:
```

## VirtualMfaDevice

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L912)

```python
class VirtualMfaDevice(Boto3ServiceResource):
```

### VirtualMfaDevice().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L920)

```python
def delete() -> None:
```

### VirtualMfaDevice().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L924)

```python
def get_available_subresources() -> List[str]:
```

## access_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1218)

```python
class access_keys(ResourceCollection):
```

### access_keys.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1219)

```python
@classmethod
def all() -> List[iam_service_resource_scope.AccessKey]:
```

### access_keys.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1224)

```python
@classmethod
def filter(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.AccessKey]:
```

### access_keys.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1231)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### access_keys.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1236)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.AccessKey]:
```

### access_keys.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1241)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.AccessKey]:
```

### access_keys.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1246)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## attached_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1358)

```python
class attached_groups(ResourceCollection):
```

### attached_groups.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1359)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Group]:
```

### attached_groups.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1364)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Group]:
```

### attached_groups.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1375)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### attached_groups.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1380)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Group]:
```

### attached_groups.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1385)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Group]:
```

### attached_groups.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1390)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## attached_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1324)

```python
class attached_policies(ResourceCollection):
```

### attached_policies.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1325)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Policy]:
```

### attached_policies.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1330)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Policy]:
```

### attached_policies.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1337)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### attached_policies.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1342)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Policy]:
```

### attached_policies.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1347)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Policy]:
```

### attached_policies.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1352)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## attached_roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1396)

```python
class attached_roles(ResourceCollection):
```

### attached_roles.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1397)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Role]:
```

### attached_roles.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1402)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Role]:
```

### attached_roles.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1413)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### attached_roles.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1418)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Role]:
```

### attached_roles.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1423)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Role]:
```

### attached_roles.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1428)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## attached_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1434)

```python
class attached_users(ResourceCollection):
```

### attached_users.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1435)

```python
@classmethod
def all() -> List[iam_service_resource_scope.User]:
```

### attached_users.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1440)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.User]:
```

### attached_users.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1451)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### attached_users.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1456)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.User]:
```

### attached_users.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1461)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.User]:
```

### attached_users.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1466)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L928)

```python
class groups(ResourceCollection):
```

### groups.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L929)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Group]:
```

### groups.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L934)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Group]:
```

### groups.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L941)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### groups.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L946)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Group]:
```

### groups.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L951)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Group]:
```

### groups.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L956)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## instance_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L962)

```python
class instance_profiles(ResourceCollection):
```

### instance_profiles.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L963)

```python
@classmethod
def all() -> List[iam_service_resource_scope.InstanceProfile]:
```

### instance_profiles.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L968)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.InstanceProfile]:
```

### instance_profiles.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L975)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### instance_profiles.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L980)

```python
@classmethod
def limit(
    count: int = None,
) -> List[iam_service_resource_scope.InstanceProfile]:
```

### instance_profiles.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L987)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.InstanceProfile]:
```

### instance_profiles.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L994)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## mfa_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1252)

```python
class mfa_devices(ResourceCollection):
```

### mfa_devices.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1253)

```python
@classmethod
def all() -> List[iam_service_resource_scope.MfaDevice]:
```

### mfa_devices.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1258)

```python
@classmethod
def filter(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.MfaDevice]:
```

### mfa_devices.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1265)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### mfa_devices.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1270)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.MfaDevice]:
```

### mfa_devices.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1275)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.MfaDevice]:
```

### mfa_devices.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1280)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1000)

```python
class policies(ResourceCollection):
```

### policies.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1001)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Policy]:
```

### policies.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1006)

```python
@classmethod
def filter(
    Scope: str = None,
    OnlyAttached: bool = None,
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Policy]:
```

### policies.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1019)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### policies.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1024)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Policy]:
```

### policies.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1029)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Policy]:
```

### policies.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1034)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1040)

```python
class roles(ResourceCollection):
```

### roles.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1041)

```python
@classmethod
def all() -> List[iam_service_resource_scope.Role]:
```

### roles.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1046)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.Role]:
```

### roles.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1053)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### roles.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1058)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.Role]:
```

### roles.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1063)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.Role]:
```

### roles.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1068)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## saml_providers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1074)

```python
class saml_providers(ResourceCollection):
```

### saml_providers.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1075)

```python
@classmethod
def all() -> List[iam_service_resource_scope.SamlProvider]:
```

### saml_providers.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1080)

```python
@classmethod
def filter() -> List[iam_service_resource_scope.SamlProvider]:
```

### saml_providers.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1085)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### saml_providers.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1090)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.SamlProvider]:
```

### saml_providers.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1095)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.SamlProvider]:
```

### saml_providers.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1102)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## server_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1108)

```python
class server_certificates(ResourceCollection):
```

### server_certificates.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1109)

```python
@classmethod
def all() -> List[iam_service_resource_scope.ServerCertificate]:
```

### server_certificates.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1114)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.ServerCertificate]:
```

### server_certificates.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1121)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### server_certificates.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1126)

```python
@classmethod
def limit(
    count: int = None,
) -> List[iam_service_resource_scope.ServerCertificate]:
```

### server_certificates.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1133)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.ServerCertificate]:
```

### server_certificates.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1140)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## signing_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1286)

```python
class signing_certificates(ResourceCollection):
```

### signing_certificates.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1287)

```python
@classmethod
def all() -> List[iam_service_resource_scope.SigningCertificate]:
```

### signing_certificates.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1292)

```python
@classmethod
def filter(
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.SigningCertificate]:
```

### signing_certificates.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1299)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### signing_certificates.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1304)

```python
@classmethod
def limit(
    count: int = None,
) -> List[iam_service_resource_scope.SigningCertificate]:
```

### signing_certificates.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1311)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.SigningCertificate]:
```

### signing_certificates.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1318)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1146)

```python
class users(ResourceCollection):
```

### users.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1147)

```python
@classmethod
def all() -> List[iam_service_resource_scope.User]:
```

### users.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1152)

```python
@classmethod
def filter(
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.User]:
```

### users.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1159)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### users.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1164)

```python
@classmethod
def limit(count: int = None) -> List[iam_service_resource_scope.User]:
```

### users.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1169)

```python
@classmethod
def page_size(count: int = None) -> List[iam_service_resource_scope.User]:
```

### users.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1174)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1472)

```python
class versions(ResourceCollection):
```

### versions.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1473)

```python
@classmethod
def all() -> List[iam_service_resource_scope.PolicyVersion]:
```

### versions.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1478)

```python
@classmethod
def filter(
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.PolicyVersion]:
```

### versions.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1485)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### versions.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1490)

```python
@classmethod
def limit(
    count: int = None,
) -> List[iam_service_resource_scope.PolicyVersion]:
```

### versions.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1495)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.PolicyVersion]:
```

### versions.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1502)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## virtual_mfa_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1180)

```python
class virtual_mfa_devices(ResourceCollection):
```

### virtual_mfa_devices.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1181)

```python
@classmethod
def all() -> List[iam_service_resource_scope.VirtualMfaDevice]:
```

### virtual_mfa_devices.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1186)

```python
@classmethod
def filter(
    AssignmentStatus: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> List[iam_service_resource_scope.VirtualMfaDevice]:
```

### virtual_mfa_devices.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1193)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### virtual_mfa_devices.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1198)

```python
@classmethod
def limit(
    count: int = None,
) -> List[iam_service_resource_scope.VirtualMfaDevice]:
```

### virtual_mfa_devices.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1205)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[iam_service_resource_scope.VirtualMfaDevice]:
```

### virtual_mfa_devices.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/service_resource.py#L1212)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
