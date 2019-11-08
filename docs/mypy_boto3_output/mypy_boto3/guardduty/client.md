# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.guardduty.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Guardduty](index.md#guardduty) / Client
    - [Client](#client)
        - [Client().accept_invitation](#clientaccept_invitation)
        - [Client().archive_findings](#clientarchive_findings)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_detector](#clientcreate_detector)
        - [Client().create_filter](#clientcreate_filter)
        - [Client().create_ip_set](#clientcreate_ip_set)
        - [Client().create_members](#clientcreate_members)
        - [Client().create_sample_findings](#clientcreate_sample_findings)
        - [Client().create_threat_intel_set](#clientcreate_threat_intel_set)
        - [Client().decline_invitations](#clientdecline_invitations)
        - [Client().delete_detector](#clientdelete_detector)
        - [Client().delete_filter](#clientdelete_filter)
        - [Client().delete_invitations](#clientdelete_invitations)
        - [Client().delete_ip_set](#clientdelete_ip_set)
        - [Client().delete_members](#clientdelete_members)
        - [Client().delete_threat_intel_set](#clientdelete_threat_intel_set)
        - [Client().disassociate_from_master_account](#clientdisassociate_from_master_account)
        - [Client().disassociate_members](#clientdisassociate_members)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_detector](#clientget_detector)
        - [Client().get_filter](#clientget_filter)
        - [Client().get_findings](#clientget_findings)
        - [Client().get_findings_statistics](#clientget_findings_statistics)
        - [Client().get_invitations_count](#clientget_invitations_count)
        - [Client().get_ip_set](#clientget_ip_set)
        - [Client().get_master_account](#clientget_master_account)
        - [Client().get_members](#clientget_members)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_threat_intel_set](#clientget_threat_intel_set)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invite_members](#clientinvite_members)
        - [Client().list_detectors](#clientlist_detectors)
        - [Client().list_filters](#clientlist_filters)
        - [Client().list_findings](#clientlist_findings)
        - [Client().list_invitations](#clientlist_invitations)
        - [Client().list_ip_sets](#clientlist_ip_sets)
        - [Client().list_members](#clientlist_members)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_threat_intel_sets](#clientlist_threat_intel_sets)
        - [Client().start_monitoring_members](#clientstart_monitoring_members)
        - [Client().stop_monitoring_members](#clientstop_monitoring_members)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unarchive_findings](#clientunarchive_findings)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_detector](#clientupdate_detector)
        - [Client().update_filter](#clientupdate_filter)
        - [Client().update_findings_feedback](#clientupdate_findings_feedback)
        - [Client().update_ip_set](#clientupdate_ip_set)
        - [Client().update_threat_intel_set](#clientupdate_threat_intel_set)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L15)

```python
def accept_invitation(
    DetectorId: str,
    MasterId: str,
    InvitationId: str,
) -> Dict[str, Any]:
```

### Client().archive_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L21)

```python
def archive_findings(
    DetectorId: str,
    FindingIds: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L27)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L31)

```python
def create_detector(
    Enable: bool,
    ClientToken: str = None,
    FindingPublishingFrequency: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L41)

```python
def create_filter(
    DetectorId: str,
    Name: str,
    FindingCriteria: Dict[str, Any],
    Description: str = None,
    Action: str = None,
    Rank: int = None,
    ClientToken: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L55)

```python
def create_ip_set(
    DetectorId: str,
    Name: str,
    Format: str,
    Location: str,
    Activate: bool,
    ClientToken: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L68)

```python
def create_members(
    DetectorId: str,
    AccountDetails: List[Any],
) -> Dict[str, Any]:
```

### Client().create_sample_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L74)

```python
def create_sample_findings(
    DetectorId: str,
    FindingTypes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_threat_intel_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L80)

```python
def create_threat_intel_set(
    DetectorId: str,
    Name: str,
    Format: str,
    Location: str,
    Activate: bool,
    ClientToken: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().decline_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L93)

```python
def decline_invitations(AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L97)

```python
def delete_detector(DetectorId: str) -> Dict[str, Any]:
```

### Client().delete_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L101)

```python
def delete_filter(DetectorId: str, FilterName: str) -> Dict[str, Any]:
```

### Client().delete_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L105)

```python
def delete_invitations(AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L109)

```python
def delete_ip_set(DetectorId: str, IpSetId: str) -> Dict[str, Any]:
```

### Client().delete_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L113)

```python
def delete_members(DetectorId: str, AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_threat_intel_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L117)

```python
def delete_threat_intel_set(
    DetectorId: str,
    ThreatIntelSetId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_from_master_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L123)

```python
def disassociate_from_master_account(DetectorId: str) -> Dict[str, Any]:
```

### Client().disassociate_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L127)

```python
def disassociate_members(
    DetectorId: str,
    AccountIds: List[Any],
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L133)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L143)

```python
def get_detector(DetectorId: str) -> Dict[str, Any]:
```

### Client().get_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L147)

```python
def get_filter(DetectorId: str, FilterName: str) -> Dict[str, Any]:
```

### Client().get_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L151)

```python
def get_findings(
    DetectorId: str,
    FindingIds: List[Any],
    SortCriteria: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_findings_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L160)

```python
def get_findings_statistics(
    DetectorId: str,
    FindingStatisticTypes: List[Any],
    FindingCriteria: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_invitations_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L169)

```python
def get_invitations_count() -> Dict[str, Any]:
```

### Client().get_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L173)

```python
def get_ip_set(DetectorId: str, IpSetId: str) -> Dict[str, Any]:
```

### Client().get_master_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L177)

```python
def get_master_account(DetectorId: str) -> Dict[str, Any]:
```

### Client().get_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L181)

```python
def get_members(DetectorId: str, AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L185)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_threat_intel_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L189)

```python
def get_threat_intel_set(
    DetectorId: str,
    ThreatIntelSetId: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L195)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invite_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L199)

```python
def invite_members(
    DetectorId: str,
    AccountIds: List[Any],
    DisableEmailNotification: bool = None,
    Message: str = None,
) -> Dict[str, Any]:
```

### Client().list_detectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L209)

```python
def list_detectors(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_filters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L215)

```python
def list_filters(
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L221)

```python
def list_findings(
    DetectorId: str,
    FindingCriteria: Dict[str, Any] = None,
    SortCriteria: Dict[str, Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L232)

```python
def list_invitations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_ip_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L238)

```python
def list_ip_sets(
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L244)

```python
def list_members(
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None,
    OnlyAssociated: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L254)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_threat_intel_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L258)

```python
def list_threat_intel_sets(
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_monitoring_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L264)

```python
def start_monitoring_members(
    DetectorId: str,
    AccountIds: List[Any],
) -> Dict[str, Any]:
```

### Client().stop_monitoring_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L270)

```python
def stop_monitoring_members(
    DetectorId: str,
    AccountIds: List[Any],
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L276)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().unarchive_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L280)

```python
def unarchive_findings(
    DetectorId: str,
    FindingIds: List[Any],
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L286)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_detector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L290)

```python
def update_detector(
    DetectorId: str,
    Enable: bool = None,
    FindingPublishingFrequency: str = None,
) -> Dict[str, Any]:
```

### Client().update_filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L299)

```python
def update_filter(
    DetectorId: str,
    FilterName: str,
    Description: str = None,
    Action: str = None,
    Rank: int = None,
    FindingCriteria: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_findings_feedback

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L311)

```python
def update_findings_feedback(
    DetectorId: str,
    FindingIds: List[Any],
    Feedback: str,
    Comments: str = None,
) -> Dict[str, Any]:
```

### Client().update_ip_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L321)

```python
def update_ip_set(
    DetectorId: str,
    IpSetId: str,
    Name: str = None,
    Location: str = None,
    Activate: bool = None,
) -> Dict[str, Any]:
```

### Client().update_threat_intel_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/guardduty/client.py#L332)

```python
def update_threat_intel_set(
    DetectorId: str,
    ThreatIntelSetId: str,
    Name: str = None,
    Location: str = None,
    Activate: bool = None,
) -> Dict[str, Any]:
```
