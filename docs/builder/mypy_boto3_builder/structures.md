# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [AnnotationWrapper](#annotationwrapper)
        - [AnnotationWrapper().get_import_record](#annotationwrapperget_import_record)
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
    - [Client](#client)
        - [Client().get_import_records](#clientget_import_records)
        - [Client().get_types](#clientget_types)
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)
    - [FakeAnnotation](#fakeannotation)
        - [FakeAnnotation().get_import_record](#fakeannotationget_import_record)
    - [InternalImport](#internalimport)
        - [InternalImport().get_import_record](#internalimportget_import_record)
        - [InternalImport().scope](#internalimportscope)
    - [Method](#method)
        - [Method().get_types](#methodget_types)
    - [Paginator](#paginator)
        - [Paginator().get_types](#paginatorget_types)
    - [Resource](#resource)
        - [Resource().get_types](#resourceget_types)
    - [ServicePaginator](#servicepaginator)
        - [ServicePaginator().get_import_records](#servicepaginatorget_import_records)
        - [ServicePaginator().get_types](#servicepaginatorget_types)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_import_records](#serviceresourceget_import_records)
        - [ServiceResource().get_types](#serviceresourceget_types)
    - [ServiceWaiter](#servicewaiter)
        - [ServiceWaiter().get_import_records](#servicewaiterget_import_records)
        - [ServiceWaiter().get_types](#servicewaiterget_types)
    - [TypeCollector](#typecollector)
        - [TypeCollector().get_import_records](#typecollectorget_import_records)
        - [TypeCollector().get_types](#typecollectorget_types)
    - [Waiter](#waiter)
        - [Waiter().get_types](#waiterget_types)

## AnnotationWrapper

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L55)

```python
class AnnotationWrapper(FakeAnnotation):
    def __init__(
        parent: type,
        children: Tuple[TypeAnnotation, ...] = (),
    ) -> None:
```

#### See also

- [FakeAnnotation](#fakeannotation)

### AnnotationWrapper().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L80)

```python
def get_import_record() -> ImportRecord:
```

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L98)

```python
dataclass
class Argument():
```

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L104)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L84)

```python
dataclass
class Attribute():
```

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L89)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L237)

```python
dataclass
class Client(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L249)

```python
def get_import_records() -> Set[ImportRecord]:
```

### Client().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L243)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L139)

```python
dataclass
class Collection(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L146)

```python
def get_types() -> Set[TypeAnnotation]:
```

## FakeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L11)

```python
class FakeAnnotation():
```

### FakeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L18)

```python
@abstractmethod
def get_import_record() -> ImportRecord:
```

## InternalImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L26)

```python
class InternalImport(FakeAnnotation):
    def __init__(
        name: str,
        service_name: ServiceName,
        module_name: str = 'service_resource',
    ) -> None:
```

#### See also

- [FakeAnnotation](#fakeannotation)

### InternalImport().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L49)

```python
def get_import_record() -> ImportRecord:
```

### InternalImport().scope

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L45)

```python
@property
def scope() -> str:
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L113)

```python
dataclass
class Method():
```

### Method().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L120)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L186)

```python
dataclass
class Paginator(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### Paginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L192)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L154)

```python
dataclass
class Resource(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L162)

```python
def get_types() -> Set[TypeAnnotation]:
```

## ServicePaginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L275)

```python
dataclass
class ServicePaginator(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### ServicePaginator().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L286)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServicePaginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L280)

```python
def get_types() -> Set[TypeAnnotation]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L199)

```python
dataclass
class ServiceResource(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L220)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L208)

```python
def get_types() -> Set[TypeAnnotation]:
```

## ServiceWaiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L254)

```python
dataclass
class ServiceWaiter(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### ServiceWaiter().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L265)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceWaiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L259)

```python
def get_types() -> Set[TypeAnnotation]:
```

## TypeCollector

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L129)

```python
class TypeCollector():
```

### TypeCollector().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L135)

```python
def get_import_records() -> Set[ImportRecord]:
```

### TypeCollector().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L131)

```python
def get_types() -> Set[TypeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L173)

```python
dataclass
class Waiter(TypeCollector):
```

#### See also

- [TypeCollector](#typecollector)

### Waiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L179)

```python
def get_types() -> Set[TypeAnnotation]:
```
