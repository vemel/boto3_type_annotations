# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sms.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sms](index.md#sms) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_app](#clientcreate_app)
        - [Client().create_replication_job](#clientcreate_replication_job)
        - [Client().delete_app](#clientdelete_app)
        - [Client().delete_app_launch_configuration](#clientdelete_app_launch_configuration)
        - [Client().delete_app_replication_configuration](#clientdelete_app_replication_configuration)
        - [Client().delete_replication_job](#clientdelete_replication_job)
        - [Client().delete_server_catalog](#clientdelete_server_catalog)
        - [Client().disassociate_connector](#clientdisassociate_connector)
        - [Client().generate_change_set](#clientgenerate_change_set)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().generate_template](#clientgenerate_template)
        - [Client().get_app](#clientget_app)
        - [Client().get_app_launch_configuration](#clientget_app_launch_configuration)
        - [Client().get_app_replication_configuration](#clientget_app_replication_configuration)
        - [Client().get_connectors](#clientget_connectors)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_replication_jobs](#clientget_replication_jobs)
        - [Client().get_replication_runs](#clientget_replication_runs)
        - [Client().get_servers](#clientget_servers)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_server_catalog](#clientimport_server_catalog)
        - [Client().launch_app](#clientlaunch_app)
        - [Client().list_apps](#clientlist_apps)
        - [Client().put_app_launch_configuration](#clientput_app_launch_configuration)
        - [Client().put_app_replication_configuration](#clientput_app_replication_configuration)
        - [Client().start_app_replication](#clientstart_app_replication)
        - [Client().start_on_demand_replication_run](#clientstart_on_demand_replication_run)
        - [Client().stop_app_replication](#clientstop_app_replication)
        - [Client().terminate_app](#clientterminate_app)
        - [Client().update_app](#clientupdate_app)
        - [Client().update_replication_job](#clientupdate_replication_job)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L20)

```python
def create_app(
    name: str = None,
    description: str = None,
    roleName: str = None,
    clientToken: str = None,
    serverGroups: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_replication_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L32)

```python
def create_replication_job(
    serverId: str,
    seedReplicationTime: datetime,
    frequency: int = None,
    runOnce: bool = None,
    licenseType: str = None,
    roleName: str = None,
    description: str = None,
    numberOfRecentAmisToKeep: int = None,
    encrypted: bool = None,
    kmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L48)

```python
def delete_app(
    appId: str = None,
    forceStopAppReplication: bool = None,
    forceTerminateApp: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_app_launch_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L57)

```python
def delete_app_launch_configuration(appId: str = None) -> Dict[str, Any]:
```

### Client().delete_app_replication_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L61)

```python
def delete_app_replication_configuration(appId: str = None) -> Dict[str, Any]:
```

### Client().delete_replication_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L65)

```python
def delete_replication_job(replicationJobId: str) -> Dict[str, Any]:
```

### Client().delete_server_catalog

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L69)

```python
def delete_server_catalog() -> Dict[str, Any]:
```

### Client().disassociate_connector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L73)

```python
def disassociate_connector(connectorId: str) -> Dict[str, Any]:
```

### Client().generate_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L77)

```python
def generate_change_set(
    appId: str = None,
    changesetFormat: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L83)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().generate_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L93)

```python
def generate_template(
    appId: str = None,
    templateFormat: str = None,
) -> Dict[str, Any]:
```

### Client().get_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L99)

```python
def get_app(appId: str = None) -> Dict[str, Any]:
```

### Client().get_app_launch_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L103)

```python
def get_app_launch_configuration(appId: str = None) -> Dict[str, Any]:
```

### Client().get_app_replication_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L107)

```python
def get_app_replication_configuration(appId: str = None) -> Dict[str, Any]:
```

### Client().get_connectors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L111)

```python
def get_connectors(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L117)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_replication_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L121)

```python
def get_replication_jobs(
    replicationJobId: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_replication_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L130)

```python
def get_replication_runs(
    replicationJobId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_servers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L136)

```python
def get_servers(
    nextToken: str = None,
    maxResults: int = None,
    vmServerAddressList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L145)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_server_catalog

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L149)

```python
def import_server_catalog() -> Dict[str, Any]:
```

### Client().launch_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L153)

```python
def launch_app(appId: str = None) -> Dict[str, Any]:
```

### Client().list_apps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L157)

```python
def list_apps(
    appIds: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_app_launch_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L163)

```python
def put_app_launch_configuration(
    appId: str = None,
    roleName: str = None,
    serverGroupLaunchConfigurations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_app_replication_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L172)

```python
def put_app_replication_configuration(
    appId: str = None,
    serverGroupReplicationConfigurations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().start_app_replication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L178)

```python
def start_app_replication(appId: str = None) -> Dict[str, Any]:
```

### Client().start_on_demand_replication_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L182)

```python
def start_on_demand_replication_run(
    replicationJobId: str,
    description: str = None,
) -> Dict[str, Any]:
```

### Client().stop_app_replication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L188)

```python
def stop_app_replication(appId: str = None) -> Dict[str, Any]:
```

### Client().terminate_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L192)

```python
def terminate_app(appId: str = None) -> Dict[str, Any]:
```

### Client().update_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L196)

```python
def update_app(
    appId: str = None,
    name: str = None,
    description: str = None,
    roleName: str = None,
    serverGroups: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_replication_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sms/client.py#L208)

```python
def update_replication_job(
    replicationJobId: str,
    frequency: int = None,
    nextReplicationRunStartTime: datetime = None,
    licenseType: str = None,
    roleName: str = None,
    description: str = None,
    numberOfRecentAmisToKeep: int = None,
    encrypted: bool = None,
    kmsKeyId: str = None,
) -> Dict[str, Any]:
```
