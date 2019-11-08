# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iotthingsgraph.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iotthingsgraph](index.md#iotthingsgraph) / Client
    - [Client](#client)
        - [Client().associate_entity_to_thing](#clientassociate_entity_to_thing)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_flow_template](#clientcreate_flow_template)
        - [Client().create_system_instance](#clientcreate_system_instance)
        - [Client().create_system_template](#clientcreate_system_template)
        - [Client().delete_flow_template](#clientdelete_flow_template)
        - [Client().delete_namespace](#clientdelete_namespace)
        - [Client().delete_system_instance](#clientdelete_system_instance)
        - [Client().delete_system_template](#clientdelete_system_template)
        - [Client().deploy_system_instance](#clientdeploy_system_instance)
        - [Client().deprecate_flow_template](#clientdeprecate_flow_template)
        - [Client().deprecate_system_template](#clientdeprecate_system_template)
        - [Client().describe_namespace](#clientdescribe_namespace)
        - [Client().dissociate_entity_from_thing](#clientdissociate_entity_from_thing)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_entities](#clientget_entities)
        - [Client().get_flow_template](#clientget_flow_template)
        - [Client().get_flow_template_revisions](#clientget_flow_template_revisions)
        - [Client().get_namespace_deletion_status](#clientget_namespace_deletion_status)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_system_instance](#clientget_system_instance)
        - [Client().get_system_template](#clientget_system_template)
        - [Client().get_system_template_revisions](#clientget_system_template_revisions)
        - [Client().get_upload_status](#clientget_upload_status)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_flow_execution_messages](#clientlist_flow_execution_messages)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().search_entities](#clientsearch_entities)
        - [Client().search_flow_executions](#clientsearch_flow_executions)
        - [Client().search_flow_templates](#clientsearch_flow_templates)
        - [Client().search_system_instances](#clientsearch_system_instances)
        - [Client().search_system_templates](#clientsearch_system_templates)
        - [Client().search_things](#clientsearch_things)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().undeploy_system_instance](#clientundeploy_system_instance)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_flow_template](#clientupdate_flow_template)
        - [Client().update_system_template](#clientupdate_system_template)
        - [Client().upload_entity_definitions](#clientupload_entity_definitions)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L13)

```python
class Client(BaseClient):
```

### Client().associate_entity_to_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L16)

```python
def associate_entity_to_thing(
    thingName: str,
    entityId: str,
    namespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_flow_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L26)

```python
def create_flow_template(
    definition: Dict[str, Any],
    compatibleNamespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().create_system_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L32)

```python
def create_system_instance(
    definition: Dict[str, Any],
    target: str,
    tags: List[Any] = None,
    greengrassGroupName: str = None,
    s3BucketName: str = None,
    metricsConfiguration: Dict[str, Any] = None,
    flowActionsRoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_system_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L45)

```python
def create_system_template(
    definition: Dict[str, Any],
    compatibleNamespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().delete_flow_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L51)

```python
def delete_flow_template(id: str) -> Dict[str, Any]:
```

### Client().delete_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L55)

```python
def delete_namespace() -> Dict[str, Any]:
```

### Client().delete_system_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L59)

```python
def delete_system_instance(id: str = None) -> Dict[str, Any]:
```

### Client().delete_system_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L63)

```python
def delete_system_template(id: str) -> Dict[str, Any]:
```

### Client().deploy_system_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L67)

```python
def deploy_system_instance(id: str = None) -> Dict[str, Any]:
```

### Client().deprecate_flow_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L71)

```python
def deprecate_flow_template(id: str) -> Dict[str, Any]:
```

### Client().deprecate_system_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L75)

```python
def deprecate_system_template(id: str) -> Dict[str, Any]:
```

### Client().describe_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L79)

```python
def describe_namespace(namespaceName: str = None) -> Dict[str, Any]:
```

### Client().dissociate_entity_from_thing

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L83)

```python
def dissociate_entity_from_thing(
    thingName: str,
    entityType: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L89)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L99)

```python
def get_entities(
    ids: List[Any],
    namespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().get_flow_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L105)

```python
def get_flow_template(id: str, revisionNumber: int = None) -> Dict[str, Any]:
```

### Client().get_flow_template_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L109)

```python
def get_flow_template_revisions(
    id: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_namespace_deletion_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L115)

```python
def get_namespace_deletion_status() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L119)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_system_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L123)

```python
def get_system_instance(id: str) -> Dict[str, Any]:
```

### Client().get_system_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L127)

```python
def get_system_template(
    id: str,
    revisionNumber: int = None,
) -> Dict[str, Any]:
```

### Client().get_system_template_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L133)

```python
def get_system_template_revisions(
    id: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_upload_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L139)

```python
def get_upload_status(uploadId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L143)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_flow_execution_messages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L147)

```python
def list_flow_execution_messages(
    flowExecutionId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L153)

```python
def list_tags_for_resource(
    resourceArn: str,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().search_entities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L159)

```python
def search_entities(
    entityTypes: List[Any],
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
    namespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().search_flow_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L170)

```python
def search_flow_executions(
    systemInstanceId: str,
    flowExecutionId: str = None,
    startTime: datetime = None,
    endTime: datetime = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_flow_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L182)

```python
def search_flow_templates(
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_system_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L188)

```python
def search_system_instances(
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_system_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L194)

```python
def search_system_templates(
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().search_things

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L200)

```python
def search_things(
    entityId: str,
    nextToken: str = None,
    maxResults: int = None,
    namespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L210)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().undeploy_system_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L214)

```python
def undeploy_system_instance(id: str = None) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L218)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_flow_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L222)

```python
def update_flow_template(
    id: str,
    definition: Dict[str, Any],
    compatibleNamespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().update_system_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L231)

```python
def update_system_template(
    id: str,
    definition: Dict[str, Any],
    compatibleNamespaceVersion: int = None,
) -> Dict[str, Any]:
```

### Client().upload_entity_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iotthingsgraph/client.py#L240)

```python
def upload_entity_definitions(
    document: Dict[str, Any] = None,
    syncWithPublicNamespace: bool = None,
    deprecateExistingEntities: bool = None,
) -> Dict[str, Any]:
```
