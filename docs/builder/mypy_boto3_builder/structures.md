# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
        - [Attribute().render](#attributerender)
    - [Boto3Module](#boto3module)
    - [ClassRecord](#classrecord)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)
    - [Client](#client)
        - [Client().get_import_records](#clientget_import_records)
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)
    - [Function](#function)
        - [Function().get_types](#functionget_types)
    - [MasterModule](#mastermodule)
    - [Method](#method)
    - [Paginator](#paginator)
    - [Resource](#resource)
        - [Resource().get_types](#resourceget_types)
    - [ServiceModule](#servicemodule)
        - [ServiceModule().extract_typed_dicts](#servicemoduleextract_typed_dicts)
        - [ServiceModule().get_client_required_import_record_groups](#servicemoduleget_client_required_import_record_groups)
        - [ServiceModule().get_import_records](#servicemoduleget_import_records)
        - [ServiceModule().get_paginator_required_import_record_groups](#servicemoduleget_paginator_required_import_record_groups)
        - [ServiceModule().get_service_resource_required_import_record_groups](#servicemoduleget_service_resource_required_import_record_groups)
        - [ServiceModule().get_type_defs_required_import_record_groups](#servicemoduleget_type_defs_required_import_record_groups)
        - [ServiceModule().get_types](#servicemoduleget_types)
        - [ServiceModule().get_waiter_required_import_record_groups](#servicemoduleget_waiter_required_import_record_groups)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_import_records](#serviceresourceget_import_records)
        - [ServiceResource().get_types](#serviceresourceget_types)
    - [Waiter](#waiter)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L34)

```python
dataclass
class Argument():
```

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L41)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L21)

```python
dataclass
class Attribute():
```

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L27)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Attribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L30)

```python
def render() -> str:
```

## Boto3Module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L347)

```python
dataclass
class Boto3Module():
```

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L73)

```python
dataclass
class ClassRecord():
```

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L91)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L81)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L218)

```python
dataclass
class Client(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L232)

```python
def get_import_records() -> Set[ImportRecord]:
```

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L102)

```python
dataclass
class Collection(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L113)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L51)

```python
dataclass
class Function():
```

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L60)

```python
def get_types() -> Set[FakeAnnotation]:
```

## MasterModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L355)

```python
dataclass
class MasterModule():
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L68)

```python
dataclass
class Method(Function):
```

#### See also

- [Function](#function)

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L151)

```python
dataclass
class Paginator(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L119)

```python
dataclass
class Resource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L132)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L237)

```python
dataclass
class ServiceModule():
```

### ServiceModule().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L246)

```python
def extract_typed_dicts(
    type_annotations: Iterable[FakeAnnotation],
    added: Dict[str, TypeTypedDict],
) -> List[TypeTypedDict]:
```

### ServiceModule().get_client_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L291)

```python
def get_client_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L282)

```python
def get_import_records() -> List[ImportRecord]:
```

### ServiceModule().get_paginator_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L314)

```python
def get_paginator_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_service_resource_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L300)

```python
def get_service_resource_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_type_defs_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L334)

```python
def get_type_defs_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L271)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServiceModule().get_waiter_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L324)

```python
def get_waiter_required_import_record_groups() -> List[ImportRecordGroup]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L163)

```python
dataclass
class ServiceResource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L205)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L192)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L183)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L139)

```python
dataclass
class Waiter(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)
