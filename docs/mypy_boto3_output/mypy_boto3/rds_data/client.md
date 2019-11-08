# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rds_data.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rds Data](index.md#rds-data) / Client
    - [Client](#client)
        - [Client().batch_execute_statement](#clientbatch_execute_statement)
        - [Client().begin_transaction](#clientbegin_transaction)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().commit_transaction](#clientcommit_transaction)
        - [Client().execute_sql](#clientexecute_sql)
        - [Client().execute_statement](#clientexecute_statement)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().rollback_transaction](#clientrollback_transaction)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_execute_statement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L15)

```python
def batch_execute_statement(
    resourceArn: str,
    secretArn: str,
    sql: str,
    database: str = None,
    parameterSets: List[Any] = None,
    schema: str = None,
    transactionId: str = None,
) -> Dict[str, Any]:
```

### Client().begin_transaction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L28)

```python
def begin_transaction(
    resourceArn: str,
    secretArn: str,
    database: str = None,
    schema: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L34)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().commit_transaction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L38)

```python
def commit_transaction(
    resourceArn: str,
    secretArn: str,
    transactionId: str,
) -> Dict[str, Any]:
```

### Client().execute_sql

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L44)

```python
def execute_sql(
    awsSecretStoreArn: str,
    dbClusterOrInstanceArn: str,
    sqlStatements: str,
    database: str = None,
    schema: str = None,
) -> Dict[str, Any]:
```

### Client().execute_statement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L55)

```python
def execute_statement(
    resourceArn: str,
    secretArn: str,
    sql: str,
    continueAfterTimeout: bool = None,
    database: str = None,
    includeResultMetadata: bool = None,
    parameters: List[Any] = None,
    resultSetOptions: Dict[str, Any] = None,
    schema: str = None,
    transactionId: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L71)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L81)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L85)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().rollback_transaction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds_data/client.py#L89)

```python
def rollback_transaction(
    resourceArn: str,
    secretArn: str,
    transactionId: str,
) -> Dict[str, Any]:
```
