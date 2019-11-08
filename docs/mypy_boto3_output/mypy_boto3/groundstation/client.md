# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.groundstation.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Groundstation](index.md#groundstation) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_contact](#clientcancel_contact)
        - [Client().create_config](#clientcreate_config)
        - [Client().create_dataflow_endpoint_group](#clientcreate_dataflow_endpoint_group)
        - [Client().create_mission_profile](#clientcreate_mission_profile)
        - [Client().delete_config](#clientdelete_config)
        - [Client().delete_dataflow_endpoint_group](#clientdelete_dataflow_endpoint_group)
        - [Client().delete_mission_profile](#clientdelete_mission_profile)
        - [Client().describe_contact](#clientdescribe_contact)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_config](#clientget_config)
        - [Client().get_dataflow_endpoint_group](#clientget_dataflow_endpoint_group)
        - [Client().get_minute_usage](#clientget_minute_usage)
        - [Client().get_mission_profile](#clientget_mission_profile)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_satellite](#clientget_satellite)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_configs](#clientlist_configs)
        - [Client().list_contacts](#clientlist_contacts)
        - [Client().list_dataflow_endpoint_groups](#clientlist_dataflow_endpoint_groups)
        - [Client().list_ground_stations](#clientlist_ground_stations)
        - [Client().list_mission_profiles](#clientlist_mission_profiles)
        - [Client().list_satellites](#clientlist_satellites)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().reserve_contact](#clientreserve_contact)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_config](#clientupdate_config)
        - [Client().update_mission_profile](#clientupdate_mission_profile)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L20)

```python
def cancel_contact(contactId: str) -> Dict[str, Any]:
```

### Client().create_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L24)

```python
def create_config(
    configData: Dict[str, Any],
    name: str,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_dataflow_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L30)

```python
def create_dataflow_endpoint_group(
    endpointDetails: List[Any],
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_mission_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L36)

```python
def create_mission_profile(
    dataflowEdges: List[Any],
    minimumViableContactDurationSeconds: int,
    name: str,
    trackingConfigArn: str,
    contactPostPassDurationSeconds: int = None,
    contactPrePassDurationSeconds: int = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L49)

```python
def delete_config(configId: str, configType: str) -> Dict[str, Any]:
```

### Client().delete_dataflow_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L53)

```python
def delete_dataflow_endpoint_group(
    dataflowEndpointGroupId: str,
) -> Dict[str, Any]:
```

### Client().delete_mission_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L59)

```python
def delete_mission_profile(missionProfileId: str) -> Dict[str, Any]:
```

### Client().describe_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L63)

```python
def describe_contact(contactId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L67)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L77)

```python
def get_config(configId: str, configType: str) -> Dict[str, Any]:
```

### Client().get_dataflow_endpoint_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L81)

```python
def get_dataflow_endpoint_group(
    dataflowEndpointGroupId: str,
) -> Dict[str, Any]:
```

### Client().get_minute_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L87)

```python
def get_minute_usage(month: int, year: int) -> Dict[str, Any]:
```

### Client().get_mission_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L91)

```python
def get_mission_profile(missionProfileId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L95)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_satellite

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L99)

```python
def get_satellite(satelliteId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L103)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L107)

```python
def list_configs(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_contacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L113)

```python
def list_contacts(
    endTime: datetime,
    startTime: datetime,
    statusList: List[Any],
    groundStation: str = None,
    maxResults: int = None,
    missionProfileArn: str = None,
    nextToken: str = None,
    satelliteArn: str = None,
) -> Dict[str, Any]:
```

### Client().list_dataflow_endpoint_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L127)

```python
def list_dataflow_endpoint_groups(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_ground_stations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L133)

```python
def list_ground_stations(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_mission_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L139)

```python
def list_mission_profiles(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_satellites

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L145)

```python
def list_satellites(
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L151)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().reserve_contact

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L155)

```python
def reserve_contact(
    endTime: datetime,
    groundStation: str,
    missionProfileArn: str,
    satelliteArn: str,
    startTime: datetime,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L167)

```python
def tag_resource(
    resourceArn: str,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L173)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L177)

```python
def update_config(
    configData: Dict[str, Any],
    configId: str,
    configType: str,
    name: str,
) -> Dict[str, Any]:
```

### Client().update_mission_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/groundstation/client.py#L183)

```python
def update_mission_profile(
    missionProfileId: str,
    contactPostPassDurationSeconds: int = None,
    contactPrePassDurationSeconds: int = None,
    dataflowEdges: List[Any] = None,
    minimumViableContactDurationSeconds: int = None,
    name: str = None,
    trackingConfigArn: str = None,
) -> Dict[str, Any]:
```
