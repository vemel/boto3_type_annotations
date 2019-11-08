# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.datasync.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Datasync](index.md#datasync) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_task_execution](#clientcancel_task_execution)
        - [Client().create_agent](#clientcreate_agent)
        - [Client().create_location_efs](#clientcreate_location_efs)
        - [Client().create_location_nfs](#clientcreate_location_nfs)
        - [Client().create_location_s3](#clientcreate_location_s3)
        - [Client().create_location_smb](#clientcreate_location_smb)
        - [Client().create_task](#clientcreate_task)
        - [Client().delete_agent](#clientdelete_agent)
        - [Client().delete_location](#clientdelete_location)
        - [Client().delete_task](#clientdelete_task)
        - [Client().describe_agent](#clientdescribe_agent)
        - [Client().describe_location_efs](#clientdescribe_location_efs)
        - [Client().describe_location_nfs](#clientdescribe_location_nfs)
        - [Client().describe_location_s3](#clientdescribe_location_s3)
        - [Client().describe_location_smb](#clientdescribe_location_smb)
        - [Client().describe_task](#clientdescribe_task)
        - [Client().describe_task_execution](#clientdescribe_task_execution)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_agents](#clientlist_agents)
        - [Client().list_locations](#clientlist_locations)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_task_executions](#clientlist_task_executions)
        - [Client().list_tasks](#clientlist_tasks)
        - [Client().start_task_execution](#clientstart_task_execution)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_agent](#clientupdate_agent)
        - [Client().update_task](#clientupdate_task)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_task_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L19)

```python
def cancel_task_execution(TaskExecutionArn: str) -> Dict[str, Any]:
```

### Client().create_agent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L23)

```python
def create_agent(
    ActivationKey: str,
    AgentName: str = None,
    Tags: List[Any] = None,
    VpcEndpointId: str = None,
    SubnetArns: List[Any] = None,
    SecurityGroupArns: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_location_efs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L35)

```python
def create_location_efs(
    EfsFilesystemArn: str,
    Ec2Config: Dict[str, Any],
    Subdirectory: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_location_nfs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L45)

```python
def create_location_nfs(
    Subdirectory: str,
    ServerHostname: str,
    OnPremConfig: Dict[str, Any],
    MountOptions: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_location_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L56)

```python
def create_location_s3(
    S3BucketArn: str,
    S3Config: Dict[str, Any],
    Subdirectory: str = None,
    S3StorageClass: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_location_smb

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L67)

```python
def create_location_smb(
    Subdirectory: str,
    ServerHostname: str,
    User: str,
    Password: str,
    AgentArns: List[Any],
    Domain: str = None,
    MountOptions: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L81)

```python
def create_task(
    SourceLocationArn: str,
    DestinationLocationArn: str,
    CloudWatchLogGroupArn: str = None,
    Name: str = None,
    Options: Dict[str, Any] = None,
    Excludes: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_agent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L94)

```python
def delete_agent(AgentArn: str) -> Dict[str, Any]:
```

### Client().delete_location

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L98)

```python
def delete_location(LocationArn: str) -> Dict[str, Any]:
```

### Client().delete_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L102)

```python
def delete_task(TaskArn: str) -> Dict[str, Any]:
```

### Client().describe_agent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L106)

```python
def describe_agent(AgentArn: str) -> Dict[str, Any]:
```

### Client().describe_location_efs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L110)

```python
def describe_location_efs(LocationArn: str) -> Dict[str, Any]:
```

### Client().describe_location_nfs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L114)

```python
def describe_location_nfs(LocationArn: str) -> Dict[str, Any]:
```

### Client().describe_location_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L118)

```python
def describe_location_s3(LocationArn: str) -> Dict[str, Any]:
```

### Client().describe_location_smb

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L122)

```python
def describe_location_smb(LocationArn: str) -> Dict[str, Any]:
```

### Client().describe_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L126)

```python
def describe_task(TaskArn: str) -> Dict[str, Any]:
```

### Client().describe_task_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L130)

```python
def describe_task_execution(TaskExecutionArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L134)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L144)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L148)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_agents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L152)

```python
def list_agents(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_locations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L158)

```python
def list_locations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L164)

```python
def list_tags_for_resource(
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_task_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L170)

```python
def list_task_executions(
    TaskArn: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L176)

```python
def list_tasks(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_task_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L182)

```python
def start_task_execution(
    TaskArn: str,
    OverrideOptions: Dict[str, Any] = None,
    Includes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L191)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L195)

```python
def untag_resource(ResourceArn: str, Keys: List[Any]) -> Dict[str, Any]:
```

### Client().update_agent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L199)

```python
def update_agent(AgentArn: str, Name: str = None) -> Dict[str, Any]:
```

### Client().update_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datasync/client.py#L203)

```python
def update_task(
    TaskArn: str,
    Options: Dict[str, Any] = None,
    Excludes: List[Any] = None,
    Name: str = None,
    CloudWatchLogGroupArn: str = None,
) -> Dict[str, Any]:
```
