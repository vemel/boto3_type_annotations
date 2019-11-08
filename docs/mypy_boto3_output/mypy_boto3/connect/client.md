# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.connect.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Connect](index.md#connect) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_user](#clientdelete_user)
        - [Client().describe_user](#clientdescribe_user)
        - [Client().describe_user_hierarchy_group](#clientdescribe_user_hierarchy_group)
        - [Client().describe_user_hierarchy_structure](#clientdescribe_user_hierarchy_structure)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_contact_attributes](#clientget_contact_attributes)
        - [Client().get_current_metric_data](#clientget_current_metric_data)
        - [Client().get_federation_token](#clientget_federation_token)
        - [Client().get_metric_data](#clientget_metric_data)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_contact_flows](#clientlist_contact_flows)
        - [Client().list_hours_of_operations](#clientlist_hours_of_operations)
        - [Client().list_phone_numbers](#clientlist_phone_numbers)
        - [Client().list_queues](#clientlist_queues)
        - [Client().list_routing_profiles](#clientlist_routing_profiles)
        - [Client().list_security_profiles](#clientlist_security_profiles)
        - [Client().list_user_hierarchy_groups](#clientlist_user_hierarchy_groups)
        - [Client().list_users](#clientlist_users)
        - [Client().start_outbound_voice_contact](#clientstart_outbound_voice_contact)
        - [Client().stop_contact](#clientstop_contact)
        - [Client().update_contact_attributes](#clientupdate_contact_attributes)
        - [Client().update_user_hierarchy](#clientupdate_user_hierarchy)
        - [Client().update_user_identity_info](#clientupdate_user_identity_info)
        - [Client().update_user_phone_config](#clientupdate_user_phone_config)
        - [Client().update_user_routing_profile](#clientupdate_user_routing_profile)
        - [Client().update_user_security_profiles](#clientupdate_user_security_profiles)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L20)

```python
def create_user(
    Username: str,
    PhoneConfig: Dict[str, Any],
    SecurityProfileIds: List[Any],
    RoutingProfileId: str,
    InstanceId: str,
    Password: str = None,
    IdentityInfo: Dict[str, Any] = None,
    DirectoryUserId: str = None,
    HierarchyGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L35)

```python
def delete_user(InstanceId: str, UserId: str) -> None:
```

### Client().describe_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L39)

```python
def describe_user(UserId: str, InstanceId: str) -> Dict[str, Any]:
```

### Client().describe_user_hierarchy_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L43)

```python
def describe_user_hierarchy_group(
    HierarchyGroupId: str,
    InstanceId: str,
) -> Dict[str, Any]:
```

### Client().describe_user_hierarchy_structure

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L49)

```python
def describe_user_hierarchy_structure(InstanceId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L53)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_contact_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L63)

```python
def get_contact_attributes(
    InstanceId: str,
    InitialContactId: str,
) -> Dict[str, Any]:
```

### Client().get_current_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L69)

```python
def get_current_metric_data(
    InstanceId: str,
    Filters: Dict[str, Any],
    CurrentMetrics: List[Any],
    Groupings: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_federation_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L81)

```python
def get_federation_token(InstanceId: str) -> Dict[str, Any]:
```

### Client().get_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L85)

```python
def get_metric_data(
    InstanceId: str,
    StartTime: datetime,
    EndTime: datetime,
    Filters: Dict[str, Any],
    HistoricalMetrics: List[Any],
    Groupings: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L99)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L103)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_contact_flows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L107)

```python
def list_contact_flows(
    InstanceId: str,
    ContactFlowTypes: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_hours_of_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L117)

```python
def list_hours_of_operations(
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_phone_numbers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L123)

```python
def list_phone_numbers(
    InstanceId: str,
    PhoneNumberTypes: List[Any] = None,
    PhoneNumberCountryCodes: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L134)

```python
def list_queues(
    InstanceId: str,
    QueueTypes: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_routing_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L144)

```python
def list_routing_profiles(
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_security_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L150)

```python
def list_security_profiles(
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_user_hierarchy_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L156)

```python
def list_user_hierarchy_groups(
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L162)

```python
def list_users(
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_outbound_voice_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L168)

```python
def start_outbound_voice_contact(
    DestinationPhoneNumber: str,
    ContactFlowId: str,
    InstanceId: str,
    ClientToken: str = None,
    SourcePhoneNumber: str = None,
    QueueId: str = None,
    Attributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().stop_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L181)

```python
def stop_contact(ContactId: str, InstanceId: str) -> Dict[str, Any]:
```

### Client().update_contact_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L185)

```python
def update_contact_attributes(
    InitialContactId: str,
    InstanceId: str,
    Attributes: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_user_hierarchy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L191)

```python
def update_user_hierarchy(
    UserId: str,
    InstanceId: str,
    HierarchyGroupId: str = None,
) -> None:
```

### Client().update_user_identity_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L197)

```python
def update_user_identity_info(
    IdentityInfo: Dict[str, Any],
    UserId: str,
    InstanceId: str,
) -> None:
```

### Client().update_user_phone_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L203)

```python
def update_user_phone_config(
    PhoneConfig: Dict[str, Any],
    UserId: str,
    InstanceId: str,
) -> None:
```

### Client().update_user_routing_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L209)

```python
def update_user_routing_profile(
    RoutingProfileId: str,
    UserId: str,
    InstanceId: str,
) -> None:
```

### Client().update_user_security_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/connect/client.py#L215)

```python
def update_user_security_profiles(
    SecurityProfileIds: List[Any],
    UserId: str,
    InstanceId: str,
) -> None:
```
