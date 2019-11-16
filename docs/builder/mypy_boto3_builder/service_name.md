# ServiceName

> Auto-generated documentation for [builder.mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py) module.

Enum with all AWS services.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().class_prefix](#servicenameclass_prefix)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().import_name](#servicenameimport_name)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName.items](#servicenameitems)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_name](#servicenamepypi_name)
        - [ServiceName.values](#servicenamevalues)
    - [main](#main)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L12)

```python
class ServiceName(enum.Enum):
```

Enum with all AWS services.

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L267)

```python
@property
def boto3_name() -> str:
```

Boto3 service name.

### ServiceName().class_prefix

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L274)

```python
@property
def class_prefix() -> str:
```

Class prefix for internal classes.

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L232)

```python
@property
def extras_name() -> str:
```

Extras name for subpackage installation.

### ServiceName().import_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L239)

```python
@property
def import_name() -> str:
```

Submodule name in main module.

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L253)

```python
def is_essential() -> bool:
```

Whether service is essential and installed with main package by default.

### ServiceName.items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L211)

```python
@classmethod
def items() -> List[ServiceName]:
```

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L225)

```python
@property
def module_name() -> str:
```

Package name for given service.

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L246)

```python
@property
def pypi_name() -> str:
```

Name of package on PyPI.

### ServiceName.values

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L215)

```python
@classmethod
def values() -> List[str]:
```

Get all values - valid boto3 service names.

#### Returns

A list of supported boto3 service names.

## main

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L287)

```python
def main() -> None:
```
