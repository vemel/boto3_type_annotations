# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
        - [Argument().render](#argumentrender)
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
        - [Function().first_arg](#functionfirst_arg)
        - [Function().get_types](#functionget_types)
    - [MasterModule](#mastermodule)
    - [Method](#method)
        - [Method().first_arg](#methodfirst_arg)
    - [Paginator](#paginator)
    - [Resource](#resource)
        - [Resource().get_types](#resourceget_types)
    - [ServiceModule](#servicemodule)
        - [ServiceModule().get_import_records](#servicemoduleget_import_records)
        - [ServiceModule().get_paginator_required_import_records](#servicemoduleget_paginator_required_import_records)
        - [ServiceModule().get_waiter_required_import_records](#servicemoduleget_waiter_required_import_records)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_import_records](#serviceresourceget_import_records)
        - [ServiceResource().get_types](#serviceresourceget_types)
    - [Waiter](#waiter)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L32)

```python
dataclass
class Argument():
```

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L39)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Argument().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L46)

```python
def render() -> str:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L19)

```python
dataclass
class Attribute():
```

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L25)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Attribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L28)

```python
def render() -> str:
```

## Boto3Module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L283)

```python
dataclass
class Boto3Module():
```

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L87)

```python
dataclass
class ClassRecord():
```

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L105)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L95)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L232)

```python
dataclass
class Client(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L246)

```python
def get_import_records() -> Set[ImportRecord]:
```

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L116)

```python
dataclass
class Collection(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L127)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L53)

```python
dataclass
class Function():
```

### Function().first_arg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L69)

```python
@property
def first_arg() -> Optional[str]:
```

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L62)

```python
def get_types() -> Set[FakeAnnotation]:
```

## MasterModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L291)

```python
dataclass
class MasterModule():
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L74)

```python
dataclass
class Method(Function):
```

#### See also

- [Function](#function)

### Method().first_arg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L76)

```python
@property
def first_arg() -> Optional[str]:
```

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L165)

```python
dataclass
class Paginator(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L133)

```python
dataclass
class Resource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L146)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceModule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L251)

```python
dataclass
class ServiceModule():
```

### ServiceModule().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L259)

```python
def get_import_records() -> List[ImportRecord]:
```

### ServiceModule().get_paginator_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L268)

```python
def get_paginator_required_import_records() -> Set[ImportRecord]:
```

### ServiceModule().get_waiter_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L275)

```python
def get_waiter_required_import_records() -> Set[ImportRecord]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L177)

```python
dataclass
class ServiceResource(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L219)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L206)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L197)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L153)

```python
dataclass
class Waiter(ClassRecord):
```

#### See also

- [ClassRecord](#classrecord)
