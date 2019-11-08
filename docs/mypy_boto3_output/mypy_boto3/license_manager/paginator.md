# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.license_manager.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [License Manager](index.md#license-manager) / Paginator
    - [ListAssociationsForLicenseConfiguration](#listassociationsforlicenseconfiguration)
        - [ListAssociationsForLicenseConfiguration().paginate](#listassociationsforlicenseconfigurationpaginate)
    - [ListLicenseConfigurations](#listlicenseconfigurations)
        - [ListLicenseConfigurations().paginate](#listlicenseconfigurationspaginate)
    - [ListLicenseSpecificationsForResource](#listlicensespecificationsforresource)
        - [ListLicenseSpecificationsForResource().paginate](#listlicensespecificationsforresourcepaginate)
    - [ListResourceInventory](#listresourceinventory)
        - [ListResourceInventory().paginate](#listresourceinventorypaginate)
    - [ListUsageForLicenseConfiguration](#listusageforlicenseconfiguration)
        - [ListUsageForLicenseConfiguration().paginate](#listusageforlicenseconfigurationpaginate)

## ListAssociationsForLicenseConfiguration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L10)

```python
class ListAssociationsForLicenseConfiguration(Paginator):
```

### ListAssociationsForLicenseConfiguration().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L13)

```python
def paginate(
    LicenseConfigurationArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListLicenseConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L19)

```python
class ListLicenseConfigurations(Paginator):
```

### ListLicenseConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L22)

```python
def paginate(
    LicenseConfigurationArns: List[Any] = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListLicenseSpecificationsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L31)

```python
class ListLicenseSpecificationsForResource(Paginator):
```

### ListLicenseSpecificationsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L34)

```python
def paginate(
    ResourceArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResourceInventory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L40)

```python
class ListResourceInventory(Paginator):
```

### ListResourceInventory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L43)

```python
def paginate(
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsageForLicenseConfiguration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L49)

```python
class ListUsageForLicenseConfiguration(Paginator):
```

### ListUsageForLicenseConfiguration().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/license_manager/paginator.py#L52)

```python
def paginate(
    LicenseConfigurationArn: str,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
