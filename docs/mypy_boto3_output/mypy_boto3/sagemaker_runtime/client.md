# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sagemaker_runtime.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sagemaker Runtime](index.md#sagemaker-runtime) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invoke_endpoint](#clientinvoke_endpoint)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L20)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L30)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L34)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invoke_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker_runtime/client.py#L38)

```python
def invoke_endpoint(
    EndpointName: str,
    Body: Union[bytes, IO],
    ContentType: str = None,
    Accept: str = None,
    CustomAttributes: str = None,
) -> Dict[str, Any]:
```
