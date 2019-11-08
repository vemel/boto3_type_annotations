# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.events.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Events](index.md#events) / Client
    - [Client](#client)
        - [Client().activate_event_source](#clientactivate_event_source)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_event_bus](#clientcreate_event_bus)
        - [Client().create_partner_event_source](#clientcreate_partner_event_source)
        - [Client().deactivate_event_source](#clientdeactivate_event_source)
        - [Client().delete_event_bus](#clientdelete_event_bus)
        - [Client().delete_partner_event_source](#clientdelete_partner_event_source)
        - [Client().delete_rule](#clientdelete_rule)
        - [Client().describe_event_bus](#clientdescribe_event_bus)
        - [Client().describe_event_source](#clientdescribe_event_source)
        - [Client().describe_partner_event_source](#clientdescribe_partner_event_source)
        - [Client().describe_rule](#clientdescribe_rule)
        - [Client().disable_rule](#clientdisable_rule)
        - [Client().enable_rule](#clientenable_rule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_event_buses](#clientlist_event_buses)
        - [Client().list_event_sources](#clientlist_event_sources)
        - [Client().list_partner_event_source_accounts](#clientlist_partner_event_source_accounts)
        - [Client().list_partner_event_sources](#clientlist_partner_event_sources)
        - [Client().list_rule_names_by_target](#clientlist_rule_names_by_target)
        - [Client().list_rules](#clientlist_rules)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_targets_by_rule](#clientlist_targets_by_rule)
        - [Client().put_events](#clientput_events)
        - [Client().put_partner_events](#clientput_partner_events)
        - [Client().put_permission](#clientput_permission)
        - [Client().put_rule](#clientput_rule)
        - [Client().put_targets](#clientput_targets)
        - [Client().remove_permission](#clientremove_permission)
        - [Client().remove_targets](#clientremove_targets)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().test_event_pattern](#clienttest_event_pattern)
        - [Client().untag_resource](#clientuntag_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L12)

```python
class Client(BaseClient):
```

### Client().activate_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L15)

```python
def activate_event_source(Name: str) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_event_bus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L23)

```python
def create_event_bus(
    Name: str,
    EventSourceName: str = None,
) -> Dict[str, Any]:
```

### Client().create_partner_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L29)

```python
def create_partner_event_source(Name: str, Account: str) -> Dict[str, Any]:
```

### Client().deactivate_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L33)

```python
def deactivate_event_source(Name: str) -> None:
```

### Client().delete_event_bus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L37)

```python
def delete_event_bus(Name: str) -> None:
```

### Client().delete_partner_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L41)

```python
def delete_partner_event_source(Name: str, Account: str) -> None:
```

### Client().delete_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L45)

```python
def delete_rule(
    Name: str,
    EventBusName: str = None,
    Force: bool = None,
) -> None:
```

### Client().describe_event_bus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L51)

```python
def describe_event_bus(Name: str = None) -> Dict[str, Any]:
```

### Client().describe_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L55)

```python
def describe_event_source(Name: str) -> Dict[str, Any]:
```

### Client().describe_partner_event_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L59)

```python
def describe_partner_event_source(Name: str) -> Dict[str, Any]:
```

### Client().describe_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L63)

```python
def describe_rule(Name: str, EventBusName: str = None) -> Dict[str, Any]:
```

### Client().disable_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L67)

```python
def disable_rule(Name: str, EventBusName: str = None) -> None:
```

### Client().enable_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L71)

```python
def enable_rule(Name: str, EventBusName: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L75)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L85)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L89)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_event_buses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L93)

```python
def list_event_buses(
    NamePrefix: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_event_sources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L99)

```python
def list_event_sources(
    NamePrefix: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_partner_event_source_accounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L105)

```python
def list_partner_event_source_accounts(
    EventSourceName: str,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_partner_event_sources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L111)

```python
def list_partner_event_sources(
    NamePrefix: str,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_rule_names_by_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L117)

```python
def list_rule_names_by_target(
    TargetArn: str,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L127)

```python
def list_rules(
    NamePrefix: str = None,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L137)

```python
def list_tags_for_resource(ResourceARN: str) -> Dict[str, Any]:
```

### Client().list_targets_by_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L141)

```python
def list_targets_by_rule(
    Rule: str,
    EventBusName: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().put_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L151)

```python
def put_events(Entries: List[Any]) -> Dict[str, Any]:
```

### Client().put_partner_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L155)

```python
def put_partner_events(Entries: List[Any]) -> Dict[str, Any]:
```

### Client().put_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L159)

```python
def put_permission(
    Action: str,
    Principal: str,
    StatementId: str,
    EventBusName: str = None,
    Condition: Dict[str, Any] = None,
) -> None:
```

### Client().put_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L170)

```python
def put_rule(
    Name: str,
    ScheduleExpression: str = None,
    EventPattern: str = None,
    State: str = None,
    Description: str = None,
    RoleArn: str = None,
    Tags: List[Any] = None,
    EventBusName: str = None,
) -> Dict[str, Any]:
```

### Client().put_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L184)

```python
def put_targets(
    Rule: str,
    Targets: List[Any],
    EventBusName: str = None,
) -> Dict[str, Any]:
```

### Client().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L190)

```python
def remove_permission(StatementId: str, EventBusName: str = None) -> None:
```

### Client().remove_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L194)

```python
def remove_targets(
    Rule: str,
    Ids: List[Any],
    EventBusName: str = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L200)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().test_event_pattern

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L204)

```python
def test_event_pattern(EventPattern: str, Event: str) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/events/client.py#L208)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```
