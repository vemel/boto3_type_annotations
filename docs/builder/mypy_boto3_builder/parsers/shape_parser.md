# ShapeParser

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.shape_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / ShapeParser
    - [ShapeParser](#shapeparser)
        - [ShapeParser().get_client_method_map](#shapeparserget_client_method_map)
        - [ShapeParser().get_paginate_method](#shapeparserget_paginate_method)
        - [ShapeParser().get_paginator_names](#shapeparserget_paginator_names)
        - [ShapeParser().get_resource_method_map](#shapeparserget_resource_method_map)
        - [ShapeParser().get_service_resource_method_map](#shapeparserget_service_resource_method_map)
        - [ShapeParser().get_wait_method](#shapeparserget_wait_method)
    - [ShapeParserError](#shapeparsererror)

## ShapeParser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L40)

```python
class ShapeParser():
    def __init__(session: Session, service_name: ServiceName):
```

### ShapeParser().get_client_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L199)

```python
def get_client_method_map() -> Dict[str, Method]:
```

### ShapeParser().get_paginate_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L295)

```python
def get_paginate_method(paginator_name: str) -> Method:
```

### ShapeParser().get_paginator_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L170)

```python
def get_paginator_names() -> List[str]:
```

### ShapeParser().get_resource_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L348)

```python
def get_resource_method_map(resource_name: str) -> Dict[str, Method]:
```

### ShapeParser().get_service_resource_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L337)

```python
def get_service_resource_method_map() -> Dict[str, Method]:
```

### ShapeParser().get_wait_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L324)

```python
def get_wait_method(waiter_name: str) -> Method:
```

## ShapeParserError

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/shape_parser.py#L36)

```python
class ShapeParserError(Exception):
```
