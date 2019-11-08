# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codestar_notifications.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codestar Notifications](index.md#codestar-notifications) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_notification_rule](#clientcreate_notification_rule)
        - [Client().delete_notification_rule](#clientdelete_notification_rule)
        - [Client().delete_target](#clientdelete_target)
        - [Client().describe_notification_rule](#clientdescribe_notification_rule)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_event_types](#clientlist_event_types)
        - [Client().list_notification_rules](#clientlist_notification_rules)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_targets](#clientlist_targets)
        - [Client().subscribe](#clientsubscribe)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unsubscribe](#clientunsubscribe)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_notification_rule](#clientupdate_notification_rule)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_notification_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L19)

```python
def create_notification_rule(
    Name: str,
    EventTypeIds: List[Any],
    Resource: str,
    Targets: List[Any],
    DetailType: str,
    ClientRequestToken: str = None,
    Tags: Dict[str, Any] = None,
    Status: str = None,
) -> Dict[str, Any]:
```

### Client().delete_notification_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L33)

```python
def delete_notification_rule(Arn: str) -> Dict[str, Any]:
```

### Client().delete_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L37)

```python
def delete_target(
    TargetAddress: str,
    ForceUnsubscribeAll: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_notification_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L43)

```python
def describe_notification_rule(Arn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L47)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L57)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L61)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_event_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L65)

```python
def list_event_types(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_notification_rules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L71)

```python
def list_notification_rules(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L77)

```python
def list_tags_for_resource(Arn: str) -> Dict[str, Any]:
```

### Client().list_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L81)

```python
def list_targets(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().subscribe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L87)

```python
def subscribe(
    Arn: str,
    Target: Dict[str, Any],
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L93)

```python
def tag_resource(Arn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().unsubscribe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L97)

```python
def unsubscribe(Arn: str, TargetAddress: str) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L101)

```python
def untag_resource(Arn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_notification_rule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codestar_notifications/client.py#L105)

```python
def update_notification_rule(
    Arn: str,
    Name: str = None,
    Status: str = None,
    EventTypeIds: List[Any] = None,
    Targets: List[Any] = None,
    DetailType: str = None,
) -> Dict[str, Any]:
```
