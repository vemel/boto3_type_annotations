# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.securityhub.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Securityhub](index.md#securityhub) / Client
    - [Client](#client)
        - [Client().accept_invitation](#clientaccept_invitation)
        - [Client().batch_disable_standards](#clientbatch_disable_standards)
        - [Client().batch_enable_standards](#clientbatch_enable_standards)
        - [Client().batch_import_findings](#clientbatch_import_findings)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_action_target](#clientcreate_action_target)
        - [Client().create_insight](#clientcreate_insight)
        - [Client().create_members](#clientcreate_members)
        - [Client().decline_invitations](#clientdecline_invitations)
        - [Client().delete_action_target](#clientdelete_action_target)
        - [Client().delete_insight](#clientdelete_insight)
        - [Client().delete_invitations](#clientdelete_invitations)
        - [Client().delete_members](#clientdelete_members)
        - [Client().describe_action_targets](#clientdescribe_action_targets)
        - [Client().describe_hub](#clientdescribe_hub)
        - [Client().describe_products](#clientdescribe_products)
        - [Client().disable_import_findings_for_product](#clientdisable_import_findings_for_product)
        - [Client().disable_security_hub](#clientdisable_security_hub)
        - [Client().disassociate_from_master_account](#clientdisassociate_from_master_account)
        - [Client().disassociate_members](#clientdisassociate_members)
        - [Client().enable_import_findings_for_product](#clientenable_import_findings_for_product)
        - [Client().enable_security_hub](#clientenable_security_hub)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_enabled_standards](#clientget_enabled_standards)
        - [Client().get_findings](#clientget_findings)
        - [Client().get_insight_results](#clientget_insight_results)
        - [Client().get_insights](#clientget_insights)
        - [Client().get_invitations_count](#clientget_invitations_count)
        - [Client().get_master_account](#clientget_master_account)
        - [Client().get_members](#clientget_members)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invite_members](#clientinvite_members)
        - [Client().list_enabled_products_for_import](#clientlist_enabled_products_for_import)
        - [Client().list_invitations](#clientlist_invitations)
        - [Client().list_members](#clientlist_members)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_action_target](#clientupdate_action_target)
        - [Client().update_findings](#clientupdate_findings)
        - [Client().update_insight](#clientupdate_insight)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L15)

```python
def accept_invitation(MasterId: str, InvitationId: str) -> Dict[str, Any]:
```

### Client().batch_disable_standards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L19)

```python
def batch_disable_standards(
    StandardsSubscriptionArns: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_enable_standards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L25)

```python
def batch_enable_standards(
    StandardsSubscriptionRequests: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_import_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L31)

```python
def batch_import_findings(Findings: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L35)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_action_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L39)

```python
def create_action_target(
    Name: str,
    Description: str,
    Id: str,
) -> Dict[str, Any]:
```

### Client().create_insight

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L45)

```python
def create_insight(
    Name: str,
    Filters: Dict[str, Any],
    GroupByAttribute: str,
) -> Dict[str, Any]:
```

### Client().create_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L51)

```python
def create_members(AccountDetails: List[Any] = None) -> Dict[str, Any]:
```

### Client().decline_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L55)

```python
def decline_invitations(AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_action_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L59)

```python
def delete_action_target(ActionTargetArn: str) -> Dict[str, Any]:
```

### Client().delete_insight

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L63)

```python
def delete_insight(InsightArn: str) -> Dict[str, Any]:
```

### Client().delete_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L67)

```python
def delete_invitations(AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L71)

```python
def delete_members(AccountIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_action_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L75)

```python
def describe_action_targets(
    ActionTargetArns: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_hub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L84)

```python
def describe_hub(HubArn: str = None) -> Dict[str, Any]:
```

### Client().describe_products

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L88)

```python
def describe_products(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().disable_import_findings_for_product

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L94)

```python
def disable_import_findings_for_product(
    ProductSubscriptionArn: str,
) -> Dict[str, Any]:
```

### Client().disable_security_hub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L100)

```python
def disable_security_hub() -> Dict[str, Any]:
```

### Client().disassociate_from_master_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L104)

```python
def disassociate_from_master_account() -> Dict[str, Any]:
```

### Client().disassociate_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L108)

```python
def disassociate_members(AccountIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().enable_import_findings_for_product

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L112)

```python
def enable_import_findings_for_product(ProductArn: str) -> Dict[str, Any]:
```

### Client().enable_security_hub

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L116)

```python
def enable_security_hub(Tags: Dict[str, Any] = None) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L120)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_enabled_standards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L130)

```python
def get_enabled_standards(
    StandardsSubscriptionArns: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L139)

```python
def get_findings(
    Filters: Dict[str, Any] = None,
    SortCriteria: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_insight_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L149)

```python
def get_insight_results(InsightArn: str) -> Dict[str, Any]:
```

### Client().get_insights

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L153)

```python
def get_insights(
    InsightArns: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_invitations_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L162)

```python
def get_invitations_count() -> Dict[str, Any]:
```

### Client().get_master_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L166)

```python
def get_master_account() -> Dict[str, Any]:
```

### Client().get_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L170)

```python
def get_members(AccountIds: List[Any]) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L174)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L178)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invite_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L182)

```python
def invite_members(AccountIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().list_enabled_products_for_import

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L186)

```python
def list_enabled_products_for_import(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L192)

```python
def list_invitations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L198)

```python
def list_members(
    OnlyAssociated: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L204)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L208)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L212)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_action_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L216)

```python
def update_action_target(
    ActionTargetArn: str,
    Name: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L222)

```python
def update_findings(
    Filters: Dict[str, Any],
    Note: Dict[str, Any] = None,
    RecordState: str = None,
) -> Dict[str, Any]:
```

### Client().update_insight

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/client.py#L231)

```python
def update_insight(
    InsightArn: str,
    Name: str = None,
    Filters: Dict[str, Any] = None,
    GroupByAttribute: str = None,
) -> Dict[str, Any]:
```
