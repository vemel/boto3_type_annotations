# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iam.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iam](index.md#iam) / Paginator
    - [GetAccountAuthorizationDetails](#getaccountauthorizationdetails)
        - [GetAccountAuthorizationDetails().paginate](#getaccountauthorizationdetailspaginate)
    - [GetGroup](#getgroup)
        - [GetGroup().paginate](#getgrouppaginate)
    - [ListAccessKeys](#listaccesskeys)
        - [ListAccessKeys().paginate](#listaccesskeyspaginate)
    - [ListAccountAliases](#listaccountaliases)
        - [ListAccountAliases().paginate](#listaccountaliasespaginate)
    - [ListAttachedGroupPolicies](#listattachedgrouppolicies)
        - [ListAttachedGroupPolicies().paginate](#listattachedgrouppoliciespaginate)
    - [ListAttachedRolePolicies](#listattachedrolepolicies)
        - [ListAttachedRolePolicies().paginate](#listattachedrolepoliciespaginate)
    - [ListAttachedUserPolicies](#listattacheduserpolicies)
        - [ListAttachedUserPolicies().paginate](#listattacheduserpoliciespaginate)
    - [ListEntitiesForPolicy](#listentitiesforpolicy)
        - [ListEntitiesForPolicy().paginate](#listentitiesforpolicypaginate)
    - [ListGroupPolicies](#listgrouppolicies)
        - [ListGroupPolicies().paginate](#listgrouppoliciespaginate)
    - [ListGroups](#listgroups)
        - [ListGroups().paginate](#listgroupspaginate)
    - [ListGroupsForUser](#listgroupsforuser)
        - [ListGroupsForUser().paginate](#listgroupsforuserpaginate)
    - [ListInstanceProfiles](#listinstanceprofiles)
        - [ListInstanceProfiles().paginate](#listinstanceprofilespaginate)
    - [ListInstanceProfilesForRole](#listinstanceprofilesforrole)
        - [ListInstanceProfilesForRole().paginate](#listinstanceprofilesforrolepaginate)
    - [ListMFADevices](#listmfadevices)
        - [ListMFADevices().paginate](#listmfadevicespaginate)
    - [ListPolicies](#listpolicies)
        - [ListPolicies().paginate](#listpoliciespaginate)
    - [ListPolicyVersions](#listpolicyversions)
        - [ListPolicyVersions().paginate](#listpolicyversionspaginate)
    - [ListRolePolicies](#listrolepolicies)
        - [ListRolePolicies().paginate](#listrolepoliciespaginate)
    - [ListRoles](#listroles)
        - [ListRoles().paginate](#listrolespaginate)
    - [ListSSHPublicKeys](#listsshpublickeys)
        - [ListSSHPublicKeys().paginate](#listsshpublickeyspaginate)
    - [ListServerCertificates](#listservercertificates)
        - [ListServerCertificates().paginate](#listservercertificatespaginate)
    - [ListSigningCertificates](#listsigningcertificates)
        - [ListSigningCertificates().paginate](#listsigningcertificatespaginate)
    - [ListUserPolicies](#listuserpolicies)
        - [ListUserPolicies().paginate](#listuserpoliciespaginate)
    - [ListUsers](#listusers)
        - [ListUsers().paginate](#listuserspaginate)
    - [ListVirtualMFADevices](#listvirtualmfadevices)
        - [ListVirtualMFADevices().paginate](#listvirtualmfadevicespaginate)
    - [SimulateCustomPolicy](#simulatecustompolicy)
        - [SimulateCustomPolicy().paginate](#simulatecustompolicypaginate)
    - [SimulatePrincipalPolicy](#simulateprincipalpolicy)
        - [SimulatePrincipalPolicy().paginate](#simulateprincipalpolicypaginate)

## GetAccountAuthorizationDetails

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L10)

```python
class GetAccountAuthorizationDetails(Paginator):
```

### GetAccountAuthorizationDetails().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L13)

```python
def paginate(
    Filter: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L19)

```python
class GetGroup(Paginator):
```

### GetGroup().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L22)

```python
def paginate(
    GroupName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAccessKeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L28)

```python
class ListAccessKeys(Paginator):
```

### ListAccessKeys().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L31)

```python
def paginate(
    UserName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAccountAliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L37)

```python
class ListAccountAliases(Paginator):
```

### ListAccountAliases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L40)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListAttachedGroupPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L44)

```python
class ListAttachedGroupPolicies(Paginator):
```

### ListAttachedGroupPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L47)

```python
def paginate(
    GroupName: str,
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAttachedRolePolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L56)

```python
class ListAttachedRolePolicies(Paginator):
```

### ListAttachedRolePolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L59)

```python
def paginate(
    RoleName: str,
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAttachedUserPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L68)

```python
class ListAttachedUserPolicies(Paginator):
```

### ListAttachedUserPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L71)

```python
def paginate(
    UserName: str,
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListEntitiesForPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L80)

```python
class ListEntitiesForPolicy(Paginator):
```

### ListEntitiesForPolicy().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L83)

```python
def paginate(
    PolicyArn: str,
    EntityFilter: str = None,
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroupPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L94)

```python
class ListGroupPolicies(Paginator):
```

### ListGroupPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L97)

```python
def paginate(
    GroupName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L103)

```python
class ListGroups(Paginator):
```

### ListGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L106)

```python
def paginate(
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroupsForUser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L112)

```python
class ListGroupsForUser(Paginator):
```

### ListGroupsForUser().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L115)

```python
def paginate(
    UserName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstanceProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L121)

```python
class ListInstanceProfiles(Paginator):
```

### ListInstanceProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L124)

```python
def paginate(
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListInstanceProfilesForRole

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L130)

```python
class ListInstanceProfilesForRole(Paginator):
```

### ListInstanceProfilesForRole().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L133)

```python
def paginate(
    RoleName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMFADevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L139)

```python
class ListMFADevices(Paginator):
```

### ListMFADevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L142)

```python
def paginate(
    UserName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L148)

```python
class ListPolicies(Paginator):
```

### ListPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L151)

```python
def paginate(
    Scope: str = None,
    OnlyAttached: bool = None,
    PathPrefix: str = None,
    PolicyUsageFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPolicyVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L162)

```python
class ListPolicyVersions(Paginator):
```

### ListPolicyVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L165)

```python
def paginate(
    PolicyArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRolePolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L171)

```python
class ListRolePolicies(Paginator):
```

### ListRolePolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L174)

```python
def paginate(
    RoleName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRoles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L180)

```python
class ListRoles(Paginator):
```

### ListRoles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L183)

```python
def paginate(
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSSHPublicKeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L189)

```python
class ListSSHPublicKeys(Paginator):
```

### ListSSHPublicKeys().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L192)

```python
def paginate(
    UserName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListServerCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L198)

```python
class ListServerCertificates(Paginator):
```

### ListServerCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L201)

```python
def paginate(
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSigningCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L207)

```python
class ListSigningCertificates(Paginator):
```

### ListSigningCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L210)

```python
def paginate(
    UserName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUserPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L216)

```python
class ListUserPolicies(Paginator):
```

### ListUserPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L219)

```python
def paginate(
    UserName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L225)

```python
class ListUsers(Paginator):
```

### ListUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L228)

```python
def paginate(
    PathPrefix: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListVirtualMFADevices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L234)

```python
class ListVirtualMFADevices(Paginator):
```

### ListVirtualMFADevices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L237)

```python
def paginate(
    AssignmentStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SimulateCustomPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L243)

```python
class SimulateCustomPolicy(Paginator):
```

### SimulateCustomPolicy().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L246)

```python
def paginate(
    PolicyInputList: List[Any],
    ActionNames: List[Any],
    ResourceArns: List[Any] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[Any] = None,
    ResourceHandlingOption: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## SimulatePrincipalPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L261)

```python
class SimulatePrincipalPolicy(Paginator):
```

### SimulatePrincipalPolicy().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iam/paginator.py#L264)

```python
def paginate(
    PolicySourceArn: str,
    ActionNames: List[Any],
    PolicyInputList: List[Any] = None,
    ResourceArns: List[Any] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[Any] = None,
    ResourceHandlingOption: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
