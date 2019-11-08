# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudhsm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudhsm](index.md#cloudhsm) / Client
    - [Client](#client)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_hapg](#clientcreate_hapg)
        - [Client().create_hsm](#clientcreate_hsm)
        - [Client().create_luna_client](#clientcreate_luna_client)
        - [Client().delete_hapg](#clientdelete_hapg)
        - [Client().delete_hsm](#clientdelete_hsm)
        - [Client().delete_luna_client](#clientdelete_luna_client)
        - [Client().describe_hapg](#clientdescribe_hapg)
        - [Client().describe_hsm](#clientdescribe_hsm)
        - [Client().describe_luna_client](#clientdescribe_luna_client)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_config](#clientget_config)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_available_zones](#clientlist_available_zones)
        - [Client().list_hapgs](#clientlist_hapgs)
        - [Client().list_hsms](#clientlist_hsms)
        - [Client().list_luna_clients](#clientlist_luna_clients)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_hapg](#clientmodify_hapg)
        - [Client().modify_hsm](#clientmodify_hsm)
        - [Client().modify_luna_client](#clientmodify_luna_client)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L15)

```python
def add_tags_to_resource(
    ResourceArn: str,
    TagList: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_hapg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L25)

```python
def create_hapg(Label: str) -> Dict[str, Any]:
```

### Client().create_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L29)

```python
def create_hsm(
    SubnetId: str,
    SshKey: str,
    IamRoleArn: str,
    SubscriptionType: str,
    EniIp: str = None,
    ExternalId: str = None,
    ClientToken: str = None,
    SyslogIp: str = None,
) -> Dict[str, Any]:
```

### Client().create_luna_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L43)

```python
def create_luna_client(Certificate: str, Label: str = None) -> Dict[str, Any]:
```

### Client().delete_hapg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L47)

```python
def delete_hapg(HapgArn: str) -> Dict[str, Any]:
```

### Client().delete_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L51)

```python
def delete_hsm(HsmArn: str) -> Dict[str, Any]:
```

### Client().delete_luna_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L55)

```python
def delete_luna_client(ClientArn: str) -> Dict[str, Any]:
```

### Client().describe_hapg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L59)

```python
def describe_hapg(HapgArn: str) -> Dict[str, Any]:
```

### Client().describe_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L63)

```python
def describe_hsm(
    HsmArn: str = None,
    HsmSerialNumber: str = None,
) -> Dict[str, Any]:
```

### Client().describe_luna_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L69)

```python
def describe_luna_client(
    ClientArn: str = None,
    CertificateFingerprint: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L75)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L85)

```python
def get_config(
    ClientArn: str,
    ClientVersion: str,
    HapgList: List[Any],
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L91)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L95)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_available_zones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L99)

```python
def list_available_zones() -> Dict[str, Any]:
```

### Client().list_hapgs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L103)

```python
def list_hapgs(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_hsms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L107)

```python
def list_hsms(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_luna_clients

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L111)

```python
def list_luna_clients(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L115)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().modify_hapg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L119)

```python
def modify_hapg(
    HapgArn: str,
    Label: str = None,
    PartitionSerialList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_hsm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L125)

```python
def modify_hsm(
    HsmArn: str,
    SubnetId: str = None,
    EniIp: str = None,
    IamRoleArn: str = None,
    ExternalId: str = None,
    SyslogIp: str = None,
) -> Dict[str, Any]:
```

### Client().modify_luna_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L137)

```python
def modify_luna_client(ClientArn: str, Certificate: str) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsm/client.py#L141)

```python
def remove_tags_from_resource(
    ResourceArn: str,
    TagKeyList: List[Any],
) -> Dict[str, Any]:
```
