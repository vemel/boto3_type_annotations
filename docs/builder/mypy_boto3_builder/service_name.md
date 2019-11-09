# ServiceName

> Auto-generated documentation for [builder.mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().class_prefix](#servicenameclass_prefix)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().fallback](#servicenamefallback)
        - [ServiceName().import_name](#servicenameimport_name)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName().is_with_docs](#servicenameis_with_docs)
        - [ServiceName.items](#servicenameitems)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_name](#servicenamepypi_name)
        - [ServiceName.values](#servicenamevalues)
    - [main](#main)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L9)

```python
class ServiceName(enum.Enum):
```

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L441)

```python
@property
def boto3_name() -> str:
```

### ServiceName().class_prefix

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L445)

```python
@property
def class_prefix() -> str:
```

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L409)

```python
@property
def extras_name() -> str:
```

### ServiceName().fallback

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L413)

```python
@property
def fallback() -> ServiceName:
```

### ServiceName().import_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L420)

```python
@property
def import_name() -> str:
```

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L428)

```python
def is_essential() -> bool:
```

### ServiceName().is_with_docs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L438)

```python
def is_with_docs() -> bool:
```

### ServiceName.items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L397)

```python
@classmethod
def items() -> List[ServiceName]:
```

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L405)

```python
@property
def module_name() -> str:
```

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L424)

```python
@property
def pypi_name() -> str:
```

### ServiceName.values

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L401)

```python
@classmethod
def values() -> List[str]:
```

## main

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/service_name.py#L455)

```python
def main() -> None:
```
