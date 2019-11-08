# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lambda_.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lambda](index.md#lambda) / Client
    - [Client](#client)
        - [Client().add_layer_version_permission](#clientadd_layer_version_permission)
        - [Client().add_permission](#clientadd_permission)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_alias](#clientcreate_alias)
        - [Client().create_event_source_mapping](#clientcreate_event_source_mapping)
        - [Client().create_function](#clientcreate_function)
        - [Client().delete_alias](#clientdelete_alias)
        - [Client().delete_event_source_mapping](#clientdelete_event_source_mapping)
        - [Client().delete_function](#clientdelete_function)
        - [Client().delete_function_concurrency](#clientdelete_function_concurrency)
        - [Client().delete_layer_version](#clientdelete_layer_version)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account_settings](#clientget_account_settings)
        - [Client().get_alias](#clientget_alias)
        - [Client().get_event_source_mapping](#clientget_event_source_mapping)
        - [Client().get_function](#clientget_function)
        - [Client().get_function_configuration](#clientget_function_configuration)
        - [Client().get_layer_version](#clientget_layer_version)
        - [Client().get_layer_version_by_arn](#clientget_layer_version_by_arn)
        - [Client().get_layer_version_policy](#clientget_layer_version_policy)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_policy](#clientget_policy)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invoke](#clientinvoke)
        - [Client().invoke_async](#clientinvoke_async)
        - [Client().list_aliases](#clientlist_aliases)
        - [Client().list_event_source_mappings](#clientlist_event_source_mappings)
        - [Client().list_functions](#clientlist_functions)
        - [Client().list_layer_versions](#clientlist_layer_versions)
        - [Client().list_layers](#clientlist_layers)
        - [Client().list_tags](#clientlist_tags)
        - [Client().list_versions_by_function](#clientlist_versions_by_function)
        - [Client().publish_layer_version](#clientpublish_layer_version)
        - [Client().publish_version](#clientpublish_version)
        - [Client().put_function_concurrency](#clientput_function_concurrency)
        - [Client().remove_layer_version_permission](#clientremove_layer_version_permission)
        - [Client().remove_permission](#clientremove_permission)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_alias](#clientupdate_alias)
        - [Client().update_event_source_mapping](#clientupdate_event_source_mapping)
        - [Client().update_function_code](#clientupdate_function_code)
        - [Client().update_function_configuration](#clientupdate_function_configuration)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L15)

```python
class Client(BaseClient):
```

### Client().add_layer_version_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L18)

```python
def add_layer_version_permission(
    LayerName: str,
    VersionNumber: int,
    StatementId: str,
    Action: str,
    Principal: str,
    OrganizationId: str = None,
    RevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().add_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L31)

```python
def add_permission(
    FunctionName: str,
    StatementId: str,
    Action: str,
    Principal: str,
    SourceArn: str = None,
    SourceAccount: str = None,
    EventSourceToken: str = None,
    Qualifier: str = None,
    RevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L46)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L50)

```python
def create_alias(
    FunctionName: str,
    Name: str,
    FunctionVersion: str,
    Description: str = None,
    RoutingConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_event_source_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L61)

```python
def create_event_source_mapping(
    EventSourceArn: str,
    FunctionName: str,
    Enabled: bool = None,
    BatchSize: int = None,
    MaximumBatchingWindowInSeconds: int = None,
    StartingPosition: str = None,
    StartingPositionTimestamp: datetime = None,
) -> Dict[str, Any]:
```

### Client().create_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L74)

```python
def create_function(
    FunctionName: str,
    Runtime: str,
    Role: str,
    Handler: str,
    Code: Dict[str, Any],
    Description: str = None,
    Timeout: int = None,
    MemorySize: int = None,
    Publish: bool = None,
    VpcConfig: Dict[str, Any] = None,
    DeadLetterConfig: Dict[str, Any] = None,
    Environment: Dict[str, Any] = None,
    KMSKeyArn: str = None,
    TracingConfig: Dict[str, Any] = None,
    Tags: Dict[str, Any] = None,
    Layers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L96)

```python
def delete_alias(FunctionName: str, Name: str) -> None:
```

### Client().delete_event_source_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L100)

```python
def delete_event_source_mapping(UUID: str) -> Dict[str, Any]:
```

### Client().delete_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L104)

```python
def delete_function(FunctionName: str, Qualifier: str = None) -> None:
```

### Client().delete_function_concurrency

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L108)

```python
def delete_function_concurrency(FunctionName: str) -> None:
```

### Client().delete_layer_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L112)

```python
def delete_layer_version(LayerName: str, VersionNumber: int) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L116)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L126)

```python
def get_account_settings() -> Dict[str, Any]:
```

### Client().get_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L130)

```python
def get_alias(FunctionName: str, Name: str) -> Dict[str, Any]:
```

### Client().get_event_source_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L134)

```python
def get_event_source_mapping(UUID: str) -> Dict[str, Any]:
```

### Client().get_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L138)

```python
def get_function(FunctionName: str, Qualifier: str = None) -> Dict[str, Any]:
```

### Client().get_function_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L142)

```python
def get_function_configuration(
    FunctionName: str,
    Qualifier: str = None,
) -> Dict[str, Any]:
```

### Client().get_layer_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L148)

```python
def get_layer_version(LayerName: str, VersionNumber: int) -> Dict[str, Any]:
```

### Client().get_layer_version_by_arn

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L152)

```python
def get_layer_version_by_arn(Arn: str) -> Dict[str, Any]:
```

### Client().get_layer_version_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L156)

```python
def get_layer_version_policy(
    LayerName: str,
    VersionNumber: int,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L162)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L166)

```python
def get_policy(FunctionName: str, Qualifier: str = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L170)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invoke

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L174)

```python
def invoke(
    FunctionName: str,
    InvocationType: str = None,
    LogType: str = None,
    ClientContext: str = None,
    Payload: Union[bytes, IO] = None,
    Qualifier: str = None,
) -> Dict[str, Any]:
```

### Client().invoke_async

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L186)

```python
def invoke_async(
    FunctionName: str,
    InvokeArgs: Union[bytes, IO],
) -> Dict[str, Any]:
```

### Client().list_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L192)

```python
def list_aliases(
    FunctionName: str,
    FunctionVersion: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_event_source_mappings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L202)

```python
def list_event_source_mappings(
    EventSourceArn: str = None,
    FunctionName: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_functions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L212)

```python
def list_functions(
    MasterRegion: str = None,
    FunctionVersion: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_layer_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L222)

```python
def list_layer_versions(
    LayerName: str,
    CompatibleRuntime: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_layers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L232)

```python
def list_layers(
    CompatibleRuntime: str = None,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L238)

```python
def list_tags(Resource: str) -> Dict[str, Any]:
```

### Client().list_versions_by_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L242)

```python
def list_versions_by_function(
    FunctionName: str,
    Marker: str = None,
    MaxItems: int = None,
) -> Dict[str, Any]:
```

### Client().publish_layer_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L248)

```python
def publish_layer_version(
    LayerName: str,
    Content: Dict[str, Any],
    Description: str = None,
    CompatibleRuntimes: List[Any] = None,
    LicenseInfo: str = None,
) -> Dict[str, Any]:
```

### Client().publish_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L259)

```python
def publish_version(
    FunctionName: str,
    CodeSha256: str = None,
    Description: str = None,
    RevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().put_function_concurrency

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L269)

```python
def put_function_concurrency(
    FunctionName: str,
    ReservedConcurrentExecutions: int,
) -> Dict[str, Any]:
```

### Client().remove_layer_version_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L275)

```python
def remove_layer_version_permission(
    LayerName: str,
    VersionNumber: int,
    StatementId: str,
    RevisionId: str = None,
) -> None:
```

### Client().remove_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L285)

```python
def remove_permission(
    FunctionName: str,
    StatementId: str,
    Qualifier: str = None,
    RevisionId: str = None,
) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L295)

```python
def tag_resource(Resource: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L299)

```python
def untag_resource(Resource: str, TagKeys: List[Any]) -> None:
```

### Client().update_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L303)

```python
def update_alias(
    FunctionName: str,
    Name: str,
    FunctionVersion: str = None,
    Description: str = None,
    RoutingConfig: Dict[str, Any] = None,
    RevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().update_event_source_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L315)

```python
def update_event_source_mapping(
    UUID: str,
    FunctionName: str = None,
    Enabled: bool = None,
    BatchSize: int = None,
    MaximumBatchingWindowInSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().update_function_code

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L326)

```python
def update_function_code(
    FunctionName: str,
    ZipFile: bytes = None,
    S3Bucket: str = None,
    S3Key: str = None,
    S3ObjectVersion: str = None,
    Publish: bool = None,
    DryRun: bool = None,
    RevisionId: str = None,
) -> Dict[str, Any]:
```

### Client().update_function_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/client.py#L340)

```python
def update_function_configuration(
    FunctionName: str,
    Role: str = None,
    Handler: str = None,
    Description: str = None,
    Timeout: int = None,
    MemorySize: int = None,
    VpcConfig: Dict[str, Any] = None,
    Environment: Dict[str, Any] = None,
    Runtime: str = None,
    DeadLetterConfig: Dict[str, Any] = None,
    KMSKeyArn: str = None,
    TracingConfig: Dict[str, Any] = None,
    RevisionId: str = None,
    Layers: List[Any] = None,
) -> Dict[str, Any]:
```
