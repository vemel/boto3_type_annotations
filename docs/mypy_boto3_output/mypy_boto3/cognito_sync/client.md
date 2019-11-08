# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cognito_sync.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cognito Sync](index.md#cognito-sync) / Client
    - [Client](#client)
        - [Client().bulk_publish](#clientbulk_publish)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_dataset](#clientdelete_dataset)
        - [Client().describe_dataset](#clientdescribe_dataset)
        - [Client().describe_identity_pool_usage](#clientdescribe_identity_pool_usage)
        - [Client().describe_identity_usage](#clientdescribe_identity_usage)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_bulk_publish_details](#clientget_bulk_publish_details)
        - [Client().get_cognito_events](#clientget_cognito_events)
        - [Client().get_identity_pool_configuration](#clientget_identity_pool_configuration)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_datasets](#clientlist_datasets)
        - [Client().list_identity_pool_usage](#clientlist_identity_pool_usage)
        - [Client().list_records](#clientlist_records)
        - [Client().register_device](#clientregister_device)
        - [Client().set_cognito_events](#clientset_cognito_events)
        - [Client().set_identity_pool_configuration](#clientset_identity_pool_configuration)
        - [Client().subscribe_to_dataset](#clientsubscribe_to_dataset)
        - [Client().unsubscribe_from_dataset](#clientunsubscribe_from_dataset)
        - [Client().update_records](#clientupdate_records)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L12)

```python
class Client(BaseClient):
```

### Client().bulk_publish

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L15)

```python
def bulk_publish(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L23)

```python
def delete_dataset(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
) -> Dict[str, Any]:
```

### Client().describe_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L29)

```python
def describe_dataset(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
) -> Dict[str, Any]:
```

### Client().describe_identity_pool_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L35)

```python
def describe_identity_pool_usage(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().describe_identity_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L39)

```python
def describe_identity_usage(
    IdentityPoolId: str,
    IdentityId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L45)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_bulk_publish_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L55)

```python
def get_bulk_publish_details(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().get_cognito_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L59)

```python
def get_cognito_events(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().get_identity_pool_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L63)

```python
def get_identity_pool_configuration(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L67)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L71)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_datasets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L75)

```python
def list_datasets(
    IdentityPoolId: str,
    IdentityId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_identity_pool_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L85)

```python
def list_identity_pool_usage(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L91)

```python
def list_records(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    LastSyncCount: int = None,
    NextToken: str = None,
    MaxResults: int = None,
    SyncSessionToken: str = None,
) -> Dict[str, Any]:
```

### Client().register_device

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L104)

```python
def register_device(
    IdentityPoolId: str,
    IdentityId: str,
    Platform: str,
    Token: str,
) -> Dict[str, Any]:
```

### Client().set_cognito_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L110)

```python
def set_cognito_events(IdentityPoolId: str, Events: Dict[str, Any]) -> None:
```

### Client().set_identity_pool_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L114)

```python
def set_identity_pool_configuration(
    IdentityPoolId: str,
    PushSync: Dict[str, Any] = None,
    CognitoStreams: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().subscribe_to_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L123)

```python
def subscribe_to_dataset(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    DeviceId: str,
) -> Dict[str, Any]:
```

### Client().unsubscribe_from_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L129)

```python
def unsubscribe_from_dataset(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    DeviceId: str,
) -> Dict[str, Any]:
```

### Client().update_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_sync/client.py#L135)

```python
def update_records(
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    SyncSessionToken: str,
    DeviceId: str = None,
    RecordPatches: List[Any] = None,
    ClientContext: str = None,
) -> Dict[str, Any]:
```
