# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ecs.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ecs](index.md#ecs) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_service](#clientcreate_service)
        - [Client().create_task_set](#clientcreate_task_set)
        - [Client().delete_account_setting](#clientdelete_account_setting)
        - [Client().delete_attributes](#clientdelete_attributes)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().delete_service](#clientdelete_service)
        - [Client().delete_task_set](#clientdelete_task_set)
        - [Client().deregister_container_instance](#clientderegister_container_instance)
        - [Client().deregister_task_definition](#clientderegister_task_definition)
        - [Client().describe_clusters](#clientdescribe_clusters)
        - [Client().describe_container_instances](#clientdescribe_container_instances)
        - [Client().describe_services](#clientdescribe_services)
        - [Client().describe_task_definition](#clientdescribe_task_definition)
        - [Client().describe_task_sets](#clientdescribe_task_sets)
        - [Client().describe_tasks](#clientdescribe_tasks)
        - [Client().discover_poll_endpoint](#clientdiscover_poll_endpoint)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_account_settings](#clientlist_account_settings)
        - [Client().list_attributes](#clientlist_attributes)
        - [Client().list_clusters](#clientlist_clusters)
        - [Client().list_container_instances](#clientlist_container_instances)
        - [Client().list_services](#clientlist_services)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_task_definition_families](#clientlist_task_definition_families)
        - [Client().list_task_definitions](#clientlist_task_definitions)
        - [Client().list_tasks](#clientlist_tasks)
        - [Client().put_account_setting](#clientput_account_setting)
        - [Client().put_account_setting_default](#clientput_account_setting_default)
        - [Client().put_attributes](#clientput_attributes)
        - [Client().register_container_instance](#clientregister_container_instance)
        - [Client().register_task_definition](#clientregister_task_definition)
        - [Client().run_task](#clientrun_task)
        - [Client().start_task](#clientstart_task)
        - [Client().stop_task](#clientstop_task)
        - [Client().submit_attachment_state_changes](#clientsubmit_attachment_state_changes)
        - [Client().submit_container_state_change](#clientsubmit_container_state_change)
        - [Client().submit_task_state_change](#clientsubmit_task_state_change)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_cluster_settings](#clientupdate_cluster_settings)
        - [Client().update_container_agent](#clientupdate_container_agent)
        - [Client().update_container_instances_state](#clientupdate_container_instances_state)
        - [Client().update_service](#clientupdate_service)
        - [Client().update_service_primary_task_set](#clientupdate_service_primary_task_set)
        - [Client().update_task_set](#clientupdate_task_set)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L20)

```python
def create_cluster(
    clusterName: str = None,
    tags: List[Any] = None,
    settings: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L29)

```python
def create_service(
    serviceName: str,
    cluster: str = None,
    taskDefinition: str = None,
    loadBalancers: List[Any] = None,
    serviceRegistries: List[Any] = None,
    desiredCount: int = None,
    clientToken: str = None,
    launchType: str = None,
    platformVersion: str = None,
    role: str = None,
    deploymentConfiguration: Dict[str, Any] = None,
    placementConstraints: List[Any] = None,
    placementStrategy: List[Any] = None,
    networkConfiguration: Dict[str, Any] = None,
    healthCheckGracePeriodSeconds: int = None,
    schedulingStrategy: str = None,
    deploymentController: Dict[str, Any] = None,
    tags: List[Any] = None,
    enableECSManagedTags: bool = None,
    propagateTags: str = None,
) -> Dict[str, Any]:
```

### Client().create_task_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L55)

```python
def create_task_set(
    service: str,
    cluster: str,
    taskDefinition: str,
    externalId: str = None,
    networkConfiguration: Dict[str, Any] = None,
    loadBalancers: List[Any] = None,
    serviceRegistries: List[Any] = None,
    launchType: str = None,
    platformVersion: str = None,
    scale: Dict[str, Any] = None,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().delete_account_setting

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L72)

```python
def delete_account_setting(
    name: str,
    principalArn: str = None,
) -> Dict[str, Any]:
```

### Client().delete_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L78)

```python
def delete_attributes(
    attributes: List[Any],
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L84)

```python
def delete_cluster(cluster: str) -> Dict[str, Any]:
```

### Client().delete_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L88)

```python
def delete_service(
    service: str,
    cluster: str = None,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_task_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L94)

```python
def delete_task_set(
    cluster: str,
    service: str,
    taskSet: str,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().deregister_container_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L100)

```python
def deregister_container_instance(
    containerInstance: str,
    cluster: str = None,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().deregister_task_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L106)

```python
def deregister_task_definition(taskDefinition: str) -> Dict[str, Any]:
```

### Client().describe_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L110)

```python
def describe_clusters(
    clusters: List[Any] = None,
    include: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_container_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L116)

```python
def describe_container_instances(
    containerInstances: List[Any],
    cluster: str = None,
    include: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L125)

```python
def describe_services(
    services: List[Any],
    cluster: str = None,
    include: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_task_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L131)

```python
def describe_task_definition(
    taskDefinition: str,
    include: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_task_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L137)

```python
def describe_task_sets(
    cluster: str,
    service: str,
    taskSets: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L143)

```python
def describe_tasks(
    tasks: List[Any],
    cluster: str = None,
    include: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().discover_poll_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L149)

```python
def discover_poll_endpoint(
    containerInstance: str = None,
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L155)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L165)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L169)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_account_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L173)

```python
def list_account_settings(
    name: str = None,
    value: str = None,
    principalArn: str = None,
    effectiveSettings: bool = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L185)

```python
def list_attributes(
    targetType: str,
    cluster: str = None,
    attributeName: str = None,
    attributeValue: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L197)

```python
def list_clusters(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_container_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L203)

```python
def list_container_instances(
    cluster: str = None,
    filter: str = None,
    nextToken: str = None,
    maxResults: int = None,
    status: str = None,
) -> Dict[str, Any]:
```

### Client().list_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L214)

```python
def list_services(
    cluster: str = None,
    nextToken: str = None,
    maxResults: int = None,
    launchType: str = None,
    schedulingStrategy: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L225)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().list_task_definition_families

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L229)

```python
def list_task_definition_families(
    familyPrefix: str = None,
    status: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_task_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L239)

```python
def list_task_definitions(
    familyPrefix: str = None,
    status: str = None,
    sort: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L250)

```python
def list_tasks(
    cluster: str = None,
    containerInstance: str = None,
    family: str = None,
    nextToken: str = None,
    maxResults: int = None,
    startedBy: str = None,
    serviceName: str = None,
    desiredStatus: str = None,
    launchType: str = None,
) -> Dict[str, Any]:
```

### Client().put_account_setting

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L265)

```python
def put_account_setting(
    name: str,
    value: str,
    principalArn: str = None,
) -> Dict[str, Any]:
```

### Client().put_account_setting_default

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L271)

```python
def put_account_setting_default(name: str, value: str) -> Dict[str, Any]:
```

### Client().put_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L275)

```python
def put_attributes(
    attributes: List[Any],
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().register_container_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L281)

```python
def register_container_instance(
    cluster: str = None,
    instanceIdentityDocument: str = None,
    instanceIdentityDocumentSignature: str = None,
    totalResources: List[Any] = None,
    versionInfo: Dict[str, Any] = None,
    containerInstanceArn: str = None,
    attributes: List[Any] = None,
    platformDevices: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().register_task_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L296)

```python
def register_task_definition(
    family: str,
    containerDefinitions: List[Any],
    taskRoleArn: str = None,
    executionRoleArn: str = None,
    networkMode: str = None,
    volumes: List[Any] = None,
    placementConstraints: List[Any] = None,
    requiresCompatibilities: List[Any] = None,
    cpu: str = None,
    memory: str = None,
    tags: List[Any] = None,
    pidMode: str = None,
    ipcMode: str = None,
    proxyConfiguration: Dict[str, Any] = None,
    inferenceAccelerators: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().run_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L317)

```python
def run_task(
    taskDefinition: str,
    cluster: str = None,
    overrides: Dict[str, Any] = None,
    count: int = None,
    startedBy: str = None,
    group: str = None,
    placementConstraints: List[Any] = None,
    placementStrategy: List[Any] = None,
    launchType: str = None,
    platformVersion: str = None,
    networkConfiguration: Dict[str, Any] = None,
    tags: List[Any] = None,
    enableECSManagedTags: bool = None,
    propagateTags: str = None,
) -> Dict[str, Any]:
```

### Client().start_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L337)

```python
def start_task(
    taskDefinition: str,
    containerInstances: List[Any],
    cluster: str = None,
    overrides: Dict[str, Any] = None,
    startedBy: str = None,
    group: str = None,
    networkConfiguration: Dict[str, Any] = None,
    tags: List[Any] = None,
    enableECSManagedTags: bool = None,
    propagateTags: str = None,
) -> Dict[str, Any]:
```

### Client().stop_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L353)

```python
def stop_task(
    task: str,
    cluster: str = None,
    reason: str = None,
) -> Dict[str, Any]:
```

### Client().submit_attachment_state_changes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L359)

```python
def submit_attachment_state_changes(
    attachments: List[Any],
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().submit_container_state_change

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L365)

```python
def submit_container_state_change(
    cluster: str = None,
    task: str = None,
    containerName: str = None,
    runtimeId: str = None,
    status: str = None,
    exitCode: int = None,
    reason: str = None,
    networkBindings: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().submit_task_state_change

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L379)

```python
def submit_task_state_change(
    cluster: str = None,
    task: str = None,
    status: str = None,
    reason: str = None,
    containers: List[Any] = None,
    attachments: List[Any] = None,
    pullStartedAt: datetime = None,
    pullStoppedAt: datetime = None,
    executionStoppedAt: datetime = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L394)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L398)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_cluster_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L402)

```python
def update_cluster_settings(
    cluster: str,
    settings: List[Any],
) -> Dict[str, Any]:
```

### Client().update_container_agent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L408)

```python
def update_container_agent(
    containerInstance: str,
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().update_container_instances_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L414)

```python
def update_container_instances_state(
    containerInstances: List[Any],
    status: str,
    cluster: str = None,
) -> Dict[str, Any]:
```

### Client().update_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L420)

```python
def update_service(
    service: str,
    cluster: str = None,
    desiredCount: int = None,
    taskDefinition: str = None,
    deploymentConfiguration: Dict[str, Any] = None,
    networkConfiguration: Dict[str, Any] = None,
    platformVersion: str = None,
    forceNewDeployment: bool = None,
    healthCheckGracePeriodSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().update_service_primary_task_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L435)

```python
def update_service_primary_task_set(
    cluster: str,
    service: str,
    primaryTaskSet: str,
) -> Dict[str, Any]:
```

### Client().update_task_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/client.py#L441)

```python
def update_task_set(
    cluster: str,
    service: str,
    taskSet: str,
    scale: Dict[str, Any],
) -> Dict[str, Any]:
```
