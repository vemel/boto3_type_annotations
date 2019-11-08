# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.license_manager.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [License Manager](index.md#license-manager) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_license_configuration](#clientcreate_license_configuration)
        - [Client().delete_license_configuration](#clientdelete_license_configuration)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_license_configuration](#clientget_license_configuration)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_service_settings](#clientget_service_settings)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_associations_for_license_configuration](#clientlist_associations_for_license_configuration)
        - [Client().list_license_configurations](#clientlist_license_configurations)
        - [Client().list_license_specifications_for_resource](#clientlist_license_specifications_for_resource)
        - [Client().list_resource_inventory](#clientlist_resource_inventory)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_usage_for_license_configuration](#clientlist_usage_for_license_configuration)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_license_configuration](#clientupdate_license_configuration)
        - [Client().update_license_specifications_for_resource](#clientupdate_license_specifications_for_resource)
        - [Client().update_service_settings](#clientupdate_service_settings)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L19)

```python
def create_license_configuration(
    Name: str,
    LicenseCountingType: str,
    Description: str = None,
    LicenseCount: int = None,
    LicenseCountHardLimit: bool = None,
    LicenseRules: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L32)

```python
def delete_license_configuration(
    LicenseConfigurationArn: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L38)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L48)

```python
def get_license_configuration(LicenseConfigurationArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L52)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_service_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L56)

```python
def get_service_settings() -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L60)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_associations_for_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L64)

```python
def list_associations_for_license_configuration(
    LicenseConfigurationArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_license_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L73)

```python
def list_license_configurations(
    LicenseConfigurationArns: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_license_specifications_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L83)

```python
def list_license_specifications_for_resource(
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_resource_inventory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L89)

```python
def list_resource_inventory(
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L95)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().list_usage_for_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L99)

```python
def list_usage_for_license_configuration(
    LicenseConfigurationArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L109)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L113)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_license_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L117)

```python
def update_license_configuration(
    LicenseConfigurationArn: str,
    LicenseConfigurationStatus: str = None,
    LicenseRules: List[Any] = None,
    LicenseCount: int = None,
    LicenseCountHardLimit: bool = None,
    Name: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_license_specifications_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L130)

```python
def update_license_specifications_for_resource(
    ResourceArn: str,
    AddLicenseSpecifications: List[Any] = None,
    RemoveLicenseSpecifications: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_service_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/client.py#L139)

```python
def update_service_settings(
    S3BucketArn: str = None,
    SnsTopicArn: str = None,
    OrganizationConfiguration: Dict[str, Any] = None,
    EnableCrossAccountsDiscovery: bool = None,
) -> Dict[str, Any]:
```
