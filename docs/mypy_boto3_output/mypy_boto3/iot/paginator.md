# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot](index.md#iot) / Paginator
    - [ListActiveViolations](#listactiveviolations)
        - [ListActiveViolations().paginate](#listactiveviolationspaginate)
    - [ListAttachedPolicies](#listattachedpolicies)
        - [ListAttachedPolicies().paginate](#listattachedpoliciespaginate)
    - [ListAuditFindings](#listauditfindings)
        - [ListAuditFindings().paginate](#listauditfindingspaginate)
    - [ListAuditTasks](#listaudittasks)
        - [ListAuditTasks().paginate](#listaudittaskspaginate)
    - [ListAuthorizers](#listauthorizers)
        - [ListAuthorizers().paginate](#listauthorizerspaginate)
    - [ListBillingGroups](#listbillinggroups)
        - [ListBillingGroups().paginate](#listbillinggroupspaginate)
    - [ListCACertificates](#listcacertificates)
        - [ListCACertificates().paginate](#listcacertificatespaginate)
    - [ListCertificates](#listcertificates)
        - [ListCertificates().paginate](#listcertificatespaginate)
    - [ListCertificatesByCA](#listcertificatesbyca)
        - [ListCertificatesByCA().paginate](#listcertificatesbycapaginate)
    - [ListIndices](#listindices)
        - [ListIndices().paginate](#listindicespaginate)
    - [ListJobExecutionsForJob](#listjobexecutionsforjob)
        - [ListJobExecutionsForJob().paginate](#listjobexecutionsforjobpaginate)
    - [ListJobExecutionsForThing](#listjobexecutionsforthing)
        - [ListJobExecutionsForThing().paginate](#listjobexecutionsforthingpaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)
    - [ListOTAUpdates](#listotaupdates)
        - [ListOTAUpdates().paginate](#listotaupdatespaginate)
    - [ListOutgoingCertificates](#listoutgoingcertificates)
        - [ListOutgoingCertificates().paginate](#listoutgoingcertificatespaginate)
    - [ListPolicies](#listpolicies)
        - [ListPolicies().paginate](#listpoliciespaginate)
    - [ListPolicyPrincipals](#listpolicyprincipals)
        - [ListPolicyPrincipals().paginate](#listpolicyprincipalspaginate)
    - [ListPrincipalPolicies](#listprincipalpolicies)
        - [ListPrincipalPolicies().paginate](#listprincipalpoliciespaginate)
    - [ListPrincipalThings](#listprincipalthings)
        - [ListPrincipalThings().paginate](#listprincipalthingspaginate)
    - [ListRoleAliases](#listrolealiases)
        - [ListRoleAliases().paginate](#listrolealiasespaginate)
    - [ListScheduledAudits](#listscheduledaudits)
        - [ListScheduledAudits().paginate](#listscheduledauditspaginate)
    - [ListSecurityProfiles](#listsecurityprofiles)
        - [ListSecurityProfiles().paginate](#listsecurityprofilespaginate)
    - [ListSecurityProfilesForTarget](#listsecurityprofilesfortarget)
        - [ListSecurityProfilesForTarget().paginate](#listsecurityprofilesfortargetpaginate)
    - [ListStreams](#liststreams)
        - [ListStreams().paginate](#liststreamspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)
    - [ListTargetsForPolicy](#listtargetsforpolicy)
        - [ListTargetsForPolicy().paginate](#listtargetsforpolicypaginate)
    - [ListTargetsForSecurityProfile](#listtargetsforsecurityprofile)
        - [ListTargetsForSecurityProfile().paginate](#listtargetsforsecurityprofilepaginate)
    - [ListThingGroups](#listthinggroups)
        - [ListThingGroups().paginate](#listthinggroupspaginate)
    - [ListThingGroupsForThing](#listthinggroupsforthing)
        - [ListThingGroupsForThing().paginate](#listthinggroupsforthingpaginate)
    - [ListThingRegistrationTasks](#listthingregistrationtasks)
        - [ListThingRegistrationTasks().paginate](#listthingregistrationtaskspaginate)
    - [ListThingTypes](#listthingtypes)
        - [ListThingTypes().paginate](#listthingtypespaginate)
    - [ListThings](#listthings)
        - [ListThings().paginate](#listthingspaginate)
    - [ListThingsInBillingGroup](#listthingsinbillinggroup)
        - [ListThingsInBillingGroup().paginate](#listthingsinbillinggrouppaginate)
    - [ListThingsInThingGroup](#listthingsinthinggroup)
        - [ListThingsInThingGroup().paginate](#listthingsinthinggrouppaginate)
    - [ListTopicRules](#listtopicrules)
        - [ListTopicRules().paginate](#listtopicrulespaginate)
    - [ListV2LoggingLevels](#listv2logginglevels)
        - [ListV2LoggingLevels().paginate](#listv2logginglevelspaginate)
    - [ListViolationEvents](#listviolationevents)
        - [ListViolationEvents().paginate](#listviolationeventspaginate)

## ListActiveViolations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L10)

```python
class ListActiveViolations(Paginator):
```

### ListActiveViolations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L13)

```python
def paginate(
    thingName: str = None,
    securityProfileName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAttachedPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L22)

```python
class ListAttachedPolicies(Paginator):
```

### ListAttachedPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L25)

```python
def paginate(
    target: str,
    recursive: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAuditFindings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L34)

```python
class ListAuditFindings(Paginator):
```

### ListAuditFindings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L37)

```python
def paginate(
    taskId: str = None,
    checkName: str = None,
    resourceIdentifier: Dict[str, Any] = None,
    startTime: datetime = None,
    endTime: datetime = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAuditTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L49)

```python
class ListAuditTasks(Paginator):
```

### ListAuditTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L52)

```python
def paginate(
    startTime: datetime,
    endTime: datetime,
    taskType: str = None,
    taskStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAuthorizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L63)

```python
class ListAuthorizers(Paginator):
```

### ListAuthorizers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L66)

```python
def paginate(
    ascendingOrder: bool = None,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListBillingGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L75)

```python
class ListBillingGroups(Paginator):
```

### ListBillingGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L78)

```python
def paginate(
    namePrefixFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListCACertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L84)

```python
class ListCACertificates(Paginator):
```

### ListCACertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L87)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L93)

```python
class ListCertificates(Paginator):
```

### ListCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L96)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListCertificatesByCA

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L102)

```python
class ListCertificatesByCA(Paginator):
```

### ListCertificatesByCA().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L105)

```python
def paginate(
    caCertificateId: str,
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListIndices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L114)

```python
class ListIndices(Paginator):
```

### ListIndices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L117)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListJobExecutionsForJob

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L121)

```python
class ListJobExecutionsForJob(Paginator):
```

### ListJobExecutionsForJob().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L124)

```python
def paginate(
    jobId: str,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobExecutionsForThing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L130)

```python
class ListJobExecutionsForThing(Paginator):
```

### ListJobExecutionsForThing().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L133)

```python
def paginate(
    thingName: str,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L142)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L145)

```python
def paginate(
    status: str = None,
    targetSelection: str = None,
    thingGroupName: str = None,
    thingGroupId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOTAUpdates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L156)

```python
class ListOTAUpdates(Paginator):
```

### ListOTAUpdates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L159)

```python
def paginate(
    otaUpdateStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOutgoingCertificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L165)

```python
class ListOutgoingCertificates(Paginator):
```

### ListOutgoingCertificates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L168)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L174)

```python
class ListPolicies(Paginator):
```

### ListPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L177)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPolicyPrincipals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L183)

```python
class ListPolicyPrincipals(Paginator):
```

### ListPolicyPrincipals().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L186)

```python
def paginate(
    policyName: str,
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPrincipalPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L195)

```python
class ListPrincipalPolicies(Paginator):
```

### ListPrincipalPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L198)

```python
def paginate(
    principal: str,
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPrincipalThings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L207)

```python
class ListPrincipalThings(Paginator):
```

### ListPrincipalThings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L210)

```python
def paginate(
    principal: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRoleAliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L216)

```python
class ListRoleAliases(Paginator):
```

### ListRoleAliases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L219)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListScheduledAudits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L225)

```python
class ListScheduledAudits(Paginator):
```

### ListScheduledAudits().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L228)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSecurityProfiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L232)

```python
class ListSecurityProfiles(Paginator):
```

### ListSecurityProfiles().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L235)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSecurityProfilesForTarget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L239)

```python
class ListSecurityProfilesForTarget(Paginator):
```

### ListSecurityProfilesForTarget().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L242)

```python
def paginate(
    securityProfileTargetArn: str,
    recursive: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStreams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L251)

```python
class ListStreams(Paginator):
```

### ListStreams().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L254)

```python
def paginate(
    ascendingOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L260)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L263)

```python
def paginate(
    resourceArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTargetsForPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L269)

```python
class ListTargetsForPolicy(Paginator):
```

### ListTargetsForPolicy().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L272)

```python
def paginate(
    policyName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTargetsForSecurityProfile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L278)

```python
class ListTargetsForSecurityProfile(Paginator):
```

### ListTargetsForSecurityProfile().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L281)

```python
def paginate(
    securityProfileName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L287)

```python
class ListThingGroups(Paginator):
```

### ListThingGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L290)

```python
def paginate(
    parentGroup: str = None,
    namePrefixFilter: str = None,
    recursive: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingGroupsForThing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L300)

```python
class ListThingGroupsForThing(Paginator):
```

### ListThingGroupsForThing().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L303)

```python
def paginate(
    thingName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingRegistrationTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L309)

```python
class ListThingRegistrationTasks(Paginator):
```

### ListThingRegistrationTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L312)

```python
def paginate(
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L318)

```python
class ListThingTypes(Paginator):
```

### ListThingTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L321)

```python
def paginate(
    thingTypeName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L327)

```python
class ListThings(Paginator):
```

### ListThings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L330)

```python
def paginate(
    attributeName: str = None,
    attributeValue: str = None,
    thingTypeName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingsInBillingGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L340)

```python
class ListThingsInBillingGroup(Paginator):
```

### ListThingsInBillingGroup().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L343)

```python
def paginate(
    billingGroupName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListThingsInThingGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L349)

```python
class ListThingsInThingGroup(Paginator):
```

### ListThingsInThingGroup().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L352)

```python
def paginate(
    thingGroupName: str,
    recursive: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTopicRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L361)

```python
class ListTopicRules(Paginator):
```

### ListTopicRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L364)

```python
def paginate(
    topic: str = None,
    ruleDisabled: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListV2LoggingLevels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L373)

```python
class ListV2LoggingLevels(Paginator):
```

### ListV2LoggingLevels().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L376)

```python
def paginate(
    targetType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListViolationEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L382)

```python
class ListViolationEvents(Paginator):
```

### ListViolationEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot/paginator.py#L385)

```python
def paginate(
    startTime: datetime,
    endTime: datetime,
    thingName: str = None,
    securityProfileName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
