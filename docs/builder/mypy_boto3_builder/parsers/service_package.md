# Service Package

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.service_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_package.py) module.

Parser that produces `structures.ServiceModule`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Service Package
    - [get_helper_body](#get_helper_body)
    - [parse_service_package](#parse_service_package)

## get_helper_body

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_package.py#L235)

```python
def get_helper_body(
    arguments: Iterable[Argument],
    function_name: Literal['resource', 'client'],
    service_name: ServiceName,
) -> str:
```

## parse_service_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/service_package.py#L34)

```python
def parse_service_package(
    session: Session,
    service_name: ServiceName,
) -> ServicePackage:
```

Extract all data from boto3 service package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceModule structure.
