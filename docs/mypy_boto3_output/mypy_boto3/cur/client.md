# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cur.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cur](index.md#cur) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_report_definition](#clientdelete_report_definition)
        - [Client().describe_report_definitions](#clientdescribe_report_definitions)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().modify_report_definition](#clientmodify_report_definition)
        - [Client().put_report_definition](#clientput_report_definition)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_report_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L18)

```python
def delete_report_definition(ReportName: str = None) -> Dict[str, Any]:
```

### Client().describe_report_definitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L22)

```python
def describe_report_definitions(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L28)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L38)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L42)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().modify_report_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L46)

```python
def modify_report_definition(
    ReportName: str,
    ReportDefinition: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_report_definition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cur/client.py#L52)

```python
def put_report_definition(ReportDefinition: Dict[str, Any]) -> Dict[str, Any]:
```
