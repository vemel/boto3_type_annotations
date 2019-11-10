# Enums

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.enums](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Enums
    - [ServiceSubmodule](#servicesubmodule)
        - [ServiceSubmodule().boto3_function_name](#servicesubmoduleboto3_function_name)
        - [ServiceSubmodule().class_name](#servicesubmoduleclass_name)
        - [ServiceSubmodule().file_name](#servicesubmodulefile_name)
        - [ServiceSubmodule.get_imported](#servicesubmoduleget_imported)
        - [ServiceSubmodule().import_name](#servicesubmoduleimport_name)

## ServiceSubmodule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L7)

```python
class ServiceSubmodule(enum.Enum):
```

### ServiceSubmodule().boto3_function_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L30)

```python
@property
def boto3_function_name() -> str:
```

### ServiceSubmodule().class_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L21)

```python
@property
def class_name() -> str:
```

### ServiceSubmodule().file_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L17)

```python
@property
def file_name() -> str:
```

### ServiceSubmodule.get_imported

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L43)

```python
@classmethod
def get_imported() -> List[ServiceSubmodule]:
```

### ServiceSubmodule().import_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/enums.py#L13)

```python
@property
def import_name() -> str:
```
