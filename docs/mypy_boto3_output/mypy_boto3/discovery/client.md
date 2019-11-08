# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.discovery.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Discovery](index.md#discovery) / Client
    - [Client](#client)
        - [Client().associate_configuration_items_to_application](#clientassociate_configuration_items_to_application)
        - [Client().batch_delete_import_data](#clientbatch_delete_import_data)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_application](#clientcreate_application)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().delete_applications](#clientdelete_applications)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_agents](#clientdescribe_agents)
        - [Client().describe_configurations](#clientdescribe_configurations)
        - [Client().describe_continuous_exports](#clientdescribe_continuous_exports)
        - [Client().describe_export_configurations](#clientdescribe_export_configurations)
        - [Client().describe_export_tasks](#clientdescribe_export_tasks)
        - [Client().describe_import_tasks](#clientdescribe_import_tasks)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().disassociate_configuration_items_from_application](#clientdisassociate_configuration_items_from_application)
        - [Client().export_configurations](#clientexport_configurations)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_discovery_summary](#clientget_discovery_summary)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_configurations](#clientlist_configurations)
        - [Client().list_server_neighbors](#clientlist_server_neighbors)
        - [Client().start_continuous_export](#clientstart_continuous_export)
        - [Client().start_data_collection_by_agent_ids](#clientstart_data_collection_by_agent_ids)
        - [Client().start_export_task](#clientstart_export_task)
        - [Client().start_import_task](#clientstart_import_task)
        - [Client().stop_continuous_export](#clientstop_continuous_export)
        - [Client().stop_data_collection_by_agent_ids](#clientstop_data_collection_by_agent_ids)
        - [Client().update_application](#clientupdate_application)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L13)

```python
class Client(BaseClient):
```

### Client().associate_configuration_items_to_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L16)

```python
def associate_configuration_items_to_application(
    applicationConfigurationId: str,
    configurationIds: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_delete_import_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L22)

```python
def batch_delete_import_data(importTaskIds: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L30)

```python
def create_application(name: str, description: str = None) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L34)

```python
def create_tags(
    configurationIds: List[Any],
    tags: List[Any],
) -> Dict[str, Any]:
```

### Client().delete_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L40)

```python
def delete_applications(configurationIds: List[Any]) -> Dict[str, Any]:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L44)

```python
def delete_tags(
    configurationIds: List[Any],
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_agents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L50)

```python
def describe_agents(
    agentIds: List[Any] = None,
    filters: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L60)

```python
def describe_configurations(configurationIds: List[Any]) -> Dict[str, Any]:
```

### Client().describe_continuous_exports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L64)

```python
def describe_continuous_exports(
    exportIds: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_export_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L70)

```python
def describe_export_configurations(
    exportIds: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_export_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L76)

```python
def describe_export_tasks(
    exportIds: List[Any] = None,
    filters: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_import_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L86)

```python
def describe_import_tasks(
    filters: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L92)

```python
def describe_tags(
    filters: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_configuration_items_from_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L98)

```python
def disassociate_configuration_items_from_application(
    applicationConfigurationId: str,
    configurationIds: List[Any],
) -> Dict[str, Any]:
```

### Client().export_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L104)

```python
def export_configurations() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L108)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_discovery_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L118)

```python
def get_discovery_summary() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L122)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L126)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L130)

```python
def list_configurations(
    configurationType: str,
    filters: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
    orderBy: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_server_neighbors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L141)

```python
def list_server_neighbors(
    configurationId: str,
    portInformationNeeded: bool = None,
    neighborConfigurationIds: List[Any] = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_continuous_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L152)

```python
def start_continuous_export() -> Dict[str, Any]:
```

### Client().start_data_collection_by_agent_ids

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L156)

```python
def start_data_collection_by_agent_ids(agentIds: List[Any]) -> Dict[str, Any]:
```

### Client().start_export_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L160)

```python
def start_export_task(
    exportDataFormat: List[Any] = None,
    filters: List[Any] = None,
    startTime: datetime = None,
    endTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().start_import_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L170)

```python
def start_import_task(
    name: str,
    importUrl: str,
    clientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().stop_continuous_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L176)

```python
def stop_continuous_export(exportId: str) -> Dict[str, Any]:
```

### Client().stop_data_collection_by_agent_ids

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L180)

```python
def stop_data_collection_by_agent_ids(agentIds: List[Any]) -> Dict[str, Any]:
```

### Client().update_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/client.py#L184)

```python
def update_application(
    configurationId: str,
    name: str = None,
    description: str = None,
) -> Dict[str, Any]:
```
