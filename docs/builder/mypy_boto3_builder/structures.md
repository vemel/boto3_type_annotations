# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

Structures produced by parsers.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
        - [Attribute().render](#attributerender)
    - [Boto3Module](#boto3module)
        - [Boto3Module().essential_service_names](#boto3moduleessential_service_names)
    - [ClassRecord](#classrecord)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)
    - [Client](#client)
        - [Client().get_all_names](#clientget_all_names)
        - [Client().get_import_records](#clientget_import_records)
        - [Client.get_paginator_method](#clientget_paginator_method)
        - [Client.get_waiter_method](#clientget_waiter_method)
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)
    - [Function](#function)
        - [Function().get_types](#functionget_types)
    - [MasterModule](#mastermodule)
        - [MasterModule().essential_service_names](#mastermoduleessential_service_names)
    - [Method](#method)
    - [Paginator](#paginator)
        - [Paginator().get_client_method](#paginatorget_client_method)
        - [Paginator().get_import_record](#paginatorget_import_record)
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
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_import_records](#serviceresourceget_import_records)
        - [ServiceResource().get_types](#serviceresourceget_types)
    - [Waiter](#waiter)
        - [Waiter().get_client_method](#waiterget_client_method)
        - [Waiter().get_import_record](#waiterget_import_record)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L67)

```python
dataclass
class Argument():
```

Method or function argument.

#### Attributes

- `name` - Argument name.
- `type` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L84)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L31)

```python
dataclass
class Attribute():
```

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L46)

```python
def get_types() -> Set[FakeAnnotation]:
```

Return all type annotations used.

#### Returns

A set of type annotations.

### Attribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L55)

```python
def render() -> str:
```

Render arguemnt to a string.

Probably not used.

#### Returns

A string with rendered attribute.

## Boto3Module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L464)

```python
dataclass
class Boto3Module():
```

### Boto3Module().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L471)

```python
@property
def essential_service_names() -> List[ServiceName]:
```

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L118)

```python
dataclass
class ClassRecord():
```

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L136)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L126)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L310)

```python
dataclass
class Client(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Client().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L328)

```python
def get_all_names() -> List[str]:
```

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L324)

```python
def get_import_records() -> Set[ImportRecord]:
```

### Client.get_paginator_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L331)

```python
@staticmethod
def get_paginator_method() -> Method:
```

#### See also

- [Method](#method)

### Client.get_waiter_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L343)

```python
@staticmethod
def get_waiter_method() -> Method:
```

#### See also

- [Method](#method)

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L149)

```python
dataclass
class Collection(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L161)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L94)

```python
dataclass
class Function():
```

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L103)

```python
def get_types() -> Set[FakeAnnotation]:
```

## MasterModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L480)

```python
dataclass
class MasterModule():
```

### MasterModule().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L487)

```python
@property
def essential_service_names() -> List[ServiceName]:
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L113)

```python
dataclass
class Method(Function):
```

#### See also

- [Function](#function)

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L217)

```python
dataclass
class Paginator(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Paginator().get_client_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L234)

```python
def get_client_method() -> Method:
```

#### See also

- [Method](#method)

### Paginator().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L229)

```python
def get_import_record() -> InternalImportRecord:
```

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L167)

```python
dataclass
class Resource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L180)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L353)

```python
dataclass
class ServiceModule():
```

### ServiceModule().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L362)

```python
def extract_typed_dicts(
    type_annotations: Iterable[FakeAnnotation],
    added: Dict[str, TypeTypedDict],
) -> List[TypeTypedDict]:
```

### ServiceModule().get_client_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L407)

```python
def get_client_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L398)

```python
def get_import_records() -> List[ImportRecord]:
```

### ServiceModule().get_paginator_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L431)

```python
def get_paginator_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_service_resource_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L417)

```python
def get_service_resource_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_type_defs_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L451)

```python
def get_type_defs_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServiceModule().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L387)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServiceModule().get_waiter_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L441)

```python
def get_waiter_required_import_record_groups() -> List[ImportRecordGroup]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L249)

```python
dataclass
class ServiceResource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L288)

```python
def get_all_names() -> List[str]:
```

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L296)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L278)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L269)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L187)

```python
dataclass
class Waiter(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Waiter().get_client_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L204)

```python
def get_client_method() -> Method:
```

#### See also

- [Method](#method)

### Waiter().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L199)

```python
def get_import_record() -> InternalImportRecord:
```
