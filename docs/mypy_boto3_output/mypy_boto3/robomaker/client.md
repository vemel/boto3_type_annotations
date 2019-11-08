# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.robomaker.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Robomaker](index.md#robomaker) / Client
    - [Client](#client)
        - [Client().batch_describe_simulation_job](#clientbatch_describe_simulation_job)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_deployment_job](#clientcancel_deployment_job)
        - [Client().cancel_simulation_job](#clientcancel_simulation_job)
        - [Client().create_deployment_job](#clientcreate_deployment_job)
        - [Client().create_fleet](#clientcreate_fleet)
        - [Client().create_robot](#clientcreate_robot)
        - [Client().create_robot_application](#clientcreate_robot_application)
        - [Client().create_robot_application_version](#clientcreate_robot_application_version)
        - [Client().create_simulation_application](#clientcreate_simulation_application)
        - [Client().create_simulation_application_version](#clientcreate_simulation_application_version)
        - [Client().create_simulation_job](#clientcreate_simulation_job)
        - [Client().delete_fleet](#clientdelete_fleet)
        - [Client().delete_robot](#clientdelete_robot)
        - [Client().delete_robot_application](#clientdelete_robot_application)
        - [Client().delete_simulation_application](#clientdelete_simulation_application)
        - [Client().deregister_robot](#clientderegister_robot)
        - [Client().describe_deployment_job](#clientdescribe_deployment_job)
        - [Client().describe_fleet](#clientdescribe_fleet)
        - [Client().describe_robot](#clientdescribe_robot)
        - [Client().describe_robot_application](#clientdescribe_robot_application)
        - [Client().describe_simulation_application](#clientdescribe_simulation_application)
        - [Client().describe_simulation_job](#clientdescribe_simulation_job)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_deployment_jobs](#clientlist_deployment_jobs)
        - [Client().list_fleets](#clientlist_fleets)
        - [Client().list_robot_applications](#clientlist_robot_applications)
        - [Client().list_robots](#clientlist_robots)
        - [Client().list_simulation_applications](#clientlist_simulation_applications)
        - [Client().list_simulation_jobs](#clientlist_simulation_jobs)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().register_robot](#clientregister_robot)
        - [Client().restart_simulation_job](#clientrestart_simulation_job)
        - [Client().sync_deployment_job](#clientsync_deployment_job)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_robot_application](#clientupdate_robot_application)
        - [Client().update_simulation_application](#clientupdate_simulation_application)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_describe_simulation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L15)

```python
def batch_describe_simulation_job(jobs: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_deployment_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L23)

```python
def cancel_deployment_job(job: str) -> Dict[str, Any]:
```

### Client().cancel_simulation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L27)

```python
def cancel_simulation_job(job: str) -> Dict[str, Any]:
```

### Client().create_deployment_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L31)

```python
def create_deployment_job(
    clientRequestToken: str,
    fleet: str,
    deploymentApplicationConfigs: List[Any],
    deploymentConfig: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L42)

```python
def create_fleet(name: str, tags: Dict[str, Any] = None) -> Dict[str, Any]:
```

### Client().create_robot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L46)

```python
def create_robot(
    name: str,
    architecture: str,
    greengrassGroupId: str,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_robot_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L56)

```python
def create_robot_application(
    name: str,
    sources: List[Any],
    robotSoftwareSuite: Dict[str, Any],
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_robot_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L66)

```python
def create_robot_application_version(
    application: str,
    currentRevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().create_simulation_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L72)

```python
def create_simulation_application(
    name: str,
    sources: List[Any],
    simulationSoftwareSuite: Dict[str, Any],
    robotSoftwareSuite: Dict[str, Any],
    renderingEngine: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_simulation_application_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L84)

```python
def create_simulation_application_version(
    application: str,
    currentRevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().create_simulation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L90)

```python
def create_simulation_job(
    maxJobDurationInSeconds: int,
    iamRole: str,
    clientRequestToken: str = None,
    outputLocation: Dict[str, Any] = None,
    loggingConfig: Dict[str, Any] = None,
    failureBehavior: str = None,
    robotApplications: List[Any] = None,
    simulationApplications: List[Any] = None,
    dataSources: List[Any] = None,
    tags: Dict[str, Any] = None,
    vpcConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L107)

```python
def delete_fleet(fleet: str) -> Dict[str, Any]:
```

### Client().delete_robot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L111)

```python
def delete_robot(robot: str) -> Dict[str, Any]:
```

### Client().delete_robot_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L115)

```python
def delete_robot_application(
    application: str,
    applicationVersion: str = None,
) -> Dict[str, Any]:
```

### Client().delete_simulation_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L121)

```python
def delete_simulation_application(
    application: str,
    applicationVersion: str = None,
) -> Dict[str, Any]:
```

### Client().deregister_robot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L127)

```python
def deregister_robot(fleet: str, robot: str) -> Dict[str, Any]:
```

### Client().describe_deployment_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L131)

```python
def describe_deployment_job(job: str) -> Dict[str, Any]:
```

### Client().describe_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L135)

```python
def describe_fleet(fleet: str) -> Dict[str, Any]:
```

### Client().describe_robot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L139)

```python
def describe_robot(robot: str) -> Dict[str, Any]:
```

### Client().describe_robot_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L143)

```python
def describe_robot_application(
    application: str,
    applicationVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_simulation_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L149)

```python
def describe_simulation_application(
    application: str,
    applicationVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_simulation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L155)

```python
def describe_simulation_job(job: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L159)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L169)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L173)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_deployment_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L177)

```python
def list_deployment_jobs(
    filters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L183)

```python
def list_fleets(
    nextToken: str = None,
    maxResults: int = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_robot_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L189)

```python
def list_robot_applications(
    versionQualifier: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_robots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L199)

```python
def list_robots(
    nextToken: str = None,
    maxResults: int = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_simulation_applications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L205)

```python
def list_simulation_applications(
    versionQualifier: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_simulation_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L215)

```python
def list_simulation_jobs(
    nextToken: str = None,
    maxResults: int = None,
    filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L221)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().register_robot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L225)

```python
def register_robot(fleet: str, robot: str) -> Dict[str, Any]:
```

### Client().restart_simulation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L229)

```python
def restart_simulation_job(job: str) -> Dict[str, Any]:
```

### Client().sync_deployment_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L233)

```python
def sync_deployment_job(
    clientRequestToken: str,
    fleet: str,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L239)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L243)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_robot_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L247)

```python
def update_robot_application(
    application: str,
    sources: List[Any],
    robotSoftwareSuite: Dict[str, Any],
    currentRevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().update_simulation_application

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/robomaker/client.py#L257)

```python
def update_simulation_application(
    application: str,
    sources: List[Any],
    simulationSoftwareSuite: Dict[str, Any],
    robotSoftwareSuite: Dict[str, Any],
    renderingEngine: Dict[str, Any] = None,
    currentRevisionId: str = None,
) -> Dict[str, Any]:
```
