# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.servicediscovery.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Servicediscovery](index.md#servicediscovery) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_http_namespace](#clientcreate_http_namespace)
        - [Client().create_private_dns_namespace](#clientcreate_private_dns_namespace)
        - [Client().create_public_dns_namespace](#clientcreate_public_dns_namespace)
        - [Client().create_service](#clientcreate_service)
        - [Client().delete_namespace](#clientdelete_namespace)
        - [Client().delete_service](#clientdelete_service)
        - [Client().deregister_instance](#clientderegister_instance)
        - [Client().discover_instances](#clientdiscover_instances)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_instance](#clientget_instance)
        - [Client().get_instances_health_status](#clientget_instances_health_status)
        - [Client().get_namespace](#clientget_namespace)
        - [Client().get_operation](#clientget_operation)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_service](#clientget_service)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_instances](#clientlist_instances)
        - [Client().list_namespaces](#clientlist_namespaces)
        - [Client().list_operations](#clientlist_operations)
        - [Client().list_services](#clientlist_services)
        - [Client().register_instance](#clientregister_instance)
        - [Client().update_instance_custom_health_status](#clientupdate_instance_custom_health_status)
        - [Client().update_service](#clientupdate_service)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_http_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L19)

```python
def create_http_namespace(
    Name: str,
    CreatorRequestId: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_private_dns_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L25)

```python
def create_private_dns_namespace(
    Name: str,
    Vpc: str,
    CreatorRequestId: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_public_dns_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L31)

```python
def create_public_dns_namespace(
    Name: str,
    CreatorRequestId: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L37)

```python
def create_service(
    Name: str,
    NamespaceId: str = None,
    CreatorRequestId: str = None,
    Description: str = None,
    DnsConfig: Dict[str, Any] = None,
    HealthCheckConfig: Dict[str, Any] = None,
    HealthCheckCustomConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L50)

```python
def delete_namespace(Id: str) -> Dict[str, Any]:
```

### Client().delete_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L54)

```python
def delete_service(Id: str) -> Dict[str, Any]:
```

### Client().deregister_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L58)

```python
def deregister_instance(ServiceId: str, InstanceId: str) -> Dict[str, Any]:
```

### Client().discover_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L62)

```python
def discover_instances(
    NamespaceName: str,
    ServiceName: str,
    MaxResults: int = None,
    QueryParameters: Dict[str, Any] = None,
    HealthStatus: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L73)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L83)

```python
def get_instance(ServiceId: str, InstanceId: str) -> Dict[str, Any]:
```

### Client().get_instances_health_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L87)

```python
def get_instances_health_status(
    ServiceId: str,
    Instances: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_namespace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L97)

```python
def get_namespace(Id: str) -> Dict[str, Any]:
```

### Client().get_operation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L101)

```python
def get_operation(OperationId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L105)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L109)

```python
def get_service(Id: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L113)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L117)

```python
def list_instances(
    ServiceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_namespaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L123)

```python
def list_namespaces(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L129)

```python
def list_operations(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L135)

```python
def list_services(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().register_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L141)

```python
def register_instance(
    ServiceId: str,
    InstanceId: str,
    Attributes: Dict[str, Any],
    CreatorRequestId: str = None,
) -> Dict[str, Any]:
```

### Client().update_instance_custom_health_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L151)

```python
def update_instance_custom_health_status(
    ServiceId: str,
    InstanceId: str,
    Status: str,
) -> None:
```

### Client().update_service

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/servicediscovery/client.py#L157)

```python
def update_service(Id: str, Service: Dict[str, Any]) -> Dict[str, Any]:
```
