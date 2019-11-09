# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
    - [Client](#client)
        - [Client().get_import_records](#clientget_import_records)
        - [Client().get_types](#clientget_types)
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)
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
    - [Waiter](#waiter)
        - [Waiter().get_types](#waiterget_types)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L29)

```python
dataclass
class Argument():
```

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L35)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L20)

```python
dataclass
class Attribute():
```

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L25)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L164)

```python
dataclass
class Client():
```

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L182)

```python
def get_import_records() -> Set[ImportRecord]:
```

### Client().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L170)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L54)

```python
dataclass
class Collection():
```

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L61)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L39)

```python
dataclass
class Method():
```

### Method().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L46)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L100)

```python
dataclass
class Paginator():
```

### Paginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L106)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L68)

```python
dataclass
class Resource():
```

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L76)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServicePaginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L214)

```python
dataclass
class ServicePaginator():
```

### ServicePaginator().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L231)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServicePaginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L219)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L113)

```python
dataclass
class ServiceResource():
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L147)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L122)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceWaiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L187)

```python
dataclass
class ServiceWaiter():
```

### ServiceWaiter().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L204)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceWaiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L192)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L87)

```python
dataclass
class Waiter():
```

### Waiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L93)

```python
def get_types() -> Set[FakeAnnotation]:
```
