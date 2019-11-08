# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.es.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Es](index.md#es) / Client
    - [Client](#client)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_elasticsearch_service_software_update](#clientcancel_elasticsearch_service_software_update)
        - [Client().create_elasticsearch_domain](#clientcreate_elasticsearch_domain)
        - [Client().delete_elasticsearch_domain](#clientdelete_elasticsearch_domain)
        - [Client().delete_elasticsearch_service_role](#clientdelete_elasticsearch_service_role)
        - [Client().describe_elasticsearch_domain](#clientdescribe_elasticsearch_domain)
        - [Client().describe_elasticsearch_domain_config](#clientdescribe_elasticsearch_domain_config)
        - [Client().describe_elasticsearch_domains](#clientdescribe_elasticsearch_domains)
        - [Client().describe_elasticsearch_instance_type_limits](#clientdescribe_elasticsearch_instance_type_limits)
        - [Client().describe_reserved_elasticsearch_instance_offerings](#clientdescribe_reserved_elasticsearch_instance_offerings)
        - [Client().describe_reserved_elasticsearch_instances](#clientdescribe_reserved_elasticsearch_instances)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_compatible_elasticsearch_versions](#clientget_compatible_elasticsearch_versions)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_upgrade_history](#clientget_upgrade_history)
        - [Client().get_upgrade_status](#clientget_upgrade_status)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_domain_names](#clientlist_domain_names)
        - [Client().list_elasticsearch_instance_types](#clientlist_elasticsearch_instance_types)
        - [Client().list_elasticsearch_versions](#clientlist_elasticsearch_versions)
        - [Client().list_tags](#clientlist_tags)
        - [Client().purchase_reserved_elasticsearch_instance_offering](#clientpurchase_reserved_elasticsearch_instance_offering)
        - [Client().remove_tags](#clientremove_tags)
        - [Client().start_elasticsearch_service_software_update](#clientstart_elasticsearch_service_software_update)
        - [Client().update_elasticsearch_domain_config](#clientupdate_elasticsearch_domain_config)
        - [Client().upgrade_elasticsearch_domain](#clientupgrade_elasticsearch_domain)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L15)

```python
def add_tags(ARN: str, TagList: List[Any]) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_elasticsearch_service_software_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L23)

```python
def cancel_elasticsearch_service_software_update(
    DomainName: str,
) -> Dict[str, Any]:
```

### Client().create_elasticsearch_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L29)

```python
def create_elasticsearch_domain(
    DomainName: str,
    ElasticsearchVersion: str = None,
    ElasticsearchClusterConfig: Dict[str, Any] = None,
    EBSOptions: Dict[str, Any] = None,
    AccessPolicies: str = None,
    SnapshotOptions: Dict[str, Any] = None,
    VPCOptions: Dict[str, Any] = None,
    CognitoOptions: Dict[str, Any] = None,
    EncryptionAtRestOptions: Dict[str, Any] = None,
    NodeToNodeEncryptionOptions: Dict[str, Any] = None,
    AdvancedOptions: Dict[str, Any] = None,
    LogPublishingOptions: Dict[str, Any] = None,
    DomainEndpointOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_elasticsearch_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L48)

```python
def delete_elasticsearch_domain(DomainName: str) -> Dict[str, Any]:
```

### Client().delete_elasticsearch_service_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L52)

```python
def delete_elasticsearch_service_role() -> None:
```

### Client().describe_elasticsearch_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L56)

```python
def describe_elasticsearch_domain(DomainName: str) -> Dict[str, Any]:
```

### Client().describe_elasticsearch_domain_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L60)

```python
def describe_elasticsearch_domain_config(DomainName: str) -> Dict[str, Any]:
```

### Client().describe_elasticsearch_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L64)

```python
def describe_elasticsearch_domains(DomainNames: List[Any]) -> Dict[str, Any]:
```

### Client().describe_elasticsearch_instance_type_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L68)

```python
def describe_elasticsearch_instance_type_limits(
    InstanceType: str,
    ElasticsearchVersion: str,
    DomainName: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_elasticsearch_instance_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L74)

```python
def describe_reserved_elasticsearch_instance_offerings(
    ReservedElasticsearchInstanceOfferingId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_elasticsearch_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L83)

```python
def describe_reserved_elasticsearch_instances(
    ReservedElasticsearchInstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L92)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_compatible_elasticsearch_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L102)

```python
def get_compatible_elasticsearch_versions(
    DomainName: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L108)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_upgrade_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L112)

```python
def get_upgrade_history(
    DomainName: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_upgrade_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L118)

```python
def get_upgrade_status(DomainName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L122)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_domain_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L126)

```python
def list_domain_names() -> Dict[str, Any]:
```

### Client().list_elasticsearch_instance_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L130)

```python
def list_elasticsearch_instance_types(
    ElasticsearchVersion: str,
    DomainName: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_elasticsearch_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L140)

```python
def list_elasticsearch_versions(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L146)

```python
def list_tags(ARN: str) -> Dict[str, Any]:
```

### Client().purchase_reserved_elasticsearch_instance_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L150)

```python
def purchase_reserved_elasticsearch_instance_offering(
    ReservedElasticsearchInstanceOfferingId: str,
    ReservationName: str,
    InstanceCount: int = None,
) -> Dict[str, Any]:
```

### Client().remove_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L159)

```python
def remove_tags(ARN: str, TagKeys: List[Any]) -> None:
```

### Client().start_elasticsearch_service_software_update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L163)

```python
def start_elasticsearch_service_software_update(
    DomainName: str,
) -> Dict[str, Any]:
```

### Client().update_elasticsearch_domain_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L169)

```python
def update_elasticsearch_domain_config(
    DomainName: str,
    ElasticsearchClusterConfig: Dict[str, Any] = None,
    EBSOptions: Dict[str, Any] = None,
    SnapshotOptions: Dict[str, Any] = None,
    VPCOptions: Dict[str, Any] = None,
    CognitoOptions: Dict[str, Any] = None,
    AdvancedOptions: Dict[str, Any] = None,
    AccessPolicies: str = None,
    LogPublishingOptions: Dict[str, Any] = None,
    DomainEndpointOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().upgrade_elasticsearch_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/es/client.py#L185)

```python
def upgrade_elasticsearch_domain(
    DomainName: str,
    TargetVersion: str,
    PerformCheckOnly: bool = None,
) -> Dict[str, Any]:
```
