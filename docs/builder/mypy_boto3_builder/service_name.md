# ServiceName

> Auto-generated documentation for [builder.mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py) module.

Description for boto3 service.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().doc_link](#servicenamedoc_link)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_name](#servicenamepypi_name)
    - [ServiceNameCatalog](#servicenamecatalog)
        - [ServiceNameCatalog.find](#servicenamecatalogfind)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L14)

```python
class ServiceName():
    def __init__(name: str, class_name: str) -> None:
```

Description for boto3 service.

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L38)

```python
@property
def boto3_name() -> str:
```

### ServiceName().doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L66)

```python
@property
def doc_link() -> str:
```

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L56)

```python
@property
def extras_name() -> str:
```

Extras name for subpackage installation.

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L63)

```python
def is_essential() -> bool:
```

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L42)

```python
@property
def module_name() -> str:
```

Package name for given service.

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L49)

```python
@property
def pypi_name() -> str:
```

Name of package on PyPI.

## ServiceNameCatalog

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L74)

```python
class ServiceNameCatalog():
```

Finder for boto3 services by name.

### ServiceNameCatalog.find

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L311)

```python
@classmethod
def find(name: str) -> ServiceName:
```

#### See also

- [ServiceName](#servicename)
