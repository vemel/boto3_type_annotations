# Service Module

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.service_module](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_module.py) module.

Parser that produces `structures.ServiceModule`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Service Module
    - [get_helper_body](#get_helper_body)
    - [parse_service_module](#parse_service_module)

## get_helper_body

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_module.py#L215)

```python
def get_helper_body(
    arguments: Iterable[Argument],
    function_name: Literal['resource', 'client'],
    service_name: ServiceName,
) -> str:
```

## parse_service_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_module.py#L33)

```python
def parse_service_module(
    session: Session,
    service_name: ServiceName,
) -> ServiceModule:
```

Extract all data from boto3 service meodule.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceModule structure.
