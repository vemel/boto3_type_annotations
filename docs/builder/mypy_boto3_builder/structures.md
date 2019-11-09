# Structures

> Auto-generated documentation for [builder.mypy_boto3_builder.structures](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Structures
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
        - [Argument().render](#argumentrender)
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
        - [Attribute().render](#attributerender)
    - [Client](#client)
        - [Client().get_import_records](#clientget_import_records)
        - [Client().get_types](#clientget_types)
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)
    - [Function](#function)
        - [Function().first_arg](#functionfirst_arg)
        - [Function().get_types](#functionget_types)
        - [Function().render_lines](#functionrender_lines)
    - [Method](#method)
        - [Method().first_arg](#methodfirst_arg)
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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L33)

```python
dataclass
class Argument():
```

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L40)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Argument().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L47)

```python
def render() -> str:
```

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L20)

```python
dataclass
class Attribute():
```

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L26)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Attribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L29)

```python
def render() -> str:
```

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L225)

```python
dataclass
class Client():
```

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L243)

```python
def get_import_records() -> Set[ImportRecord]:
```

### Client().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L231)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L115)

```python
dataclass
class Collection():
```

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L122)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L54)

```python
dataclass
class Function():
```

### Function().first_arg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L71)

```python
@property
def first_arg() -> Optional[str]:
```

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L64)

```python
def get_types() -> Set[FakeAnnotation]:
```

### Function().render_lines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L75)

```python
def render_lines(include_doc: bool = True) -> List[str]:
```

## Method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L103)

```python
dataclass
class Method(Function):
```

#### See also

- [Function](#function)

### Method().first_arg

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L105)

```python
@property
def first_arg() -> Optional[str]:
```

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L161)

```python
dataclass
class Paginator():
```

### Paginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L167)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L129)

```python
dataclass
class Resource():
```

### Resource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L137)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServicePaginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L275)

```python
dataclass
class ServicePaginator():
```

### ServicePaginator().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L292)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServicePaginator().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L280)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L174)

```python
dataclass
class ServiceResource():
```

### ServiceResource().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L208)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L183)

```python
def get_types() -> Set[FakeAnnotation]:
```

## ServiceWaiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L248)

```python
dataclass
class ServiceWaiter():
```

### ServiceWaiter().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L265)

```python
def get_import_records() -> Set[ImportRecord]:
```

### ServiceWaiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L253)

```python
def get_types() -> Set[FakeAnnotation]:
```

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L148)

```python
dataclass
class Waiter():
```

### Waiter().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures.py#L154)

```python
def get_types() -> Set[FakeAnnotation]:
```
