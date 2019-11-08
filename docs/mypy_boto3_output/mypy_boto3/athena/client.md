# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.athena.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Athena](index.md#athena) / Client
    - [Client](#client)
        - [Client().batch_get_named_query](#clientbatch_get_named_query)
        - [Client().batch_get_query_execution](#clientbatch_get_query_execution)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_named_query](#clientcreate_named_query)
        - [Client().create_work_group](#clientcreate_work_group)
        - [Client().delete_named_query](#clientdelete_named_query)
        - [Client().delete_work_group](#clientdelete_work_group)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_named_query](#clientget_named_query)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_query_execution](#clientget_query_execution)
        - [Client().get_query_results](#clientget_query_results)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().get_work_group](#clientget_work_group)
        - [Client().list_named_queries](#clientlist_named_queries)
        - [Client().list_query_executions](#clientlist_query_executions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_work_groups](#clientlist_work_groups)
        - [Client().start_query_execution](#clientstart_query_execution)
        - [Client().stop_query_execution](#clientstop_query_execution)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_work_group](#clientupdate_work_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_get_named_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L15)

```python
def batch_get_named_query(NamedQueryIds: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_query_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L19)

```python
def batch_get_query_execution(QueryExecutionIds: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_named_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L27)

```python
def create_named_query(
    Name: str,
    Database: str,
    QueryString: str,
    Description: str = None,
    ClientRequestToken: str = None,
    WorkGroup: str = None,
) -> Dict[str, Any]:
```

### Client().create_work_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L39)

```python
def create_work_group(
    Name: str,
    Configuration: Dict[str, Any] = None,
    Description: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_named_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L49)

```python
def delete_named_query(NamedQueryId: str) -> Dict[str, Any]:
```

### Client().delete_work_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L53)

```python
def delete_work_group(
    WorkGroup: str,
    RecursiveDeleteOption: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L59)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_named_query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L69)

```python
def get_named_query(NamedQueryId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L73)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_query_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L77)

```python
def get_query_execution(QueryExecutionId: str) -> Dict[str, Any]:
```

### Client().get_query_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L81)

```python
def get_query_results(
    QueryExecutionId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L87)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().get_work_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L91)

```python
def get_work_group(WorkGroup: str) -> Dict[str, Any]:
```

### Client().list_named_queries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L95)

```python
def list_named_queries(
    NextToken: str = None,
    MaxResults: int = None,
    WorkGroup: str = None,
) -> Dict[str, Any]:
```

### Client().list_query_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L101)

```python
def list_query_executions(
    NextToken: str = None,
    MaxResults: int = None,
    WorkGroup: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L107)

```python
def list_tags_for_resource(
    ResourceARN: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_work_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L113)

```python
def list_work_groups(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_query_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L119)

```python
def start_query_execution(
    QueryString: str,
    ClientRequestToken: str = None,
    QueryExecutionContext: Dict[str, Any] = None,
    ResultConfiguration: Dict[str, Any] = None,
    WorkGroup: str = None,
) -> Dict[str, Any]:
```

### Client().stop_query_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L130)

```python
def stop_query_execution(QueryExecutionId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L134)

```python
def tag_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L138)

```python
def untag_resource(ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_work_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/client.py#L142)

```python
def update_work_group(
    WorkGroup: str,
    Description: str = None,
    ConfigurationUpdates: Dict[str, Any] = None,
    State: str = None,
) -> Dict[str, Any]:
```
