# Boto3 Module

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.boto3_module](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_module.py) module.

Parser that produces `structures.Boto3Module`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Boto3 Module
    - [parse_boto3_module](#parse_boto3_module)

## parse_boto3_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_module.py#L12)

```python
def parse_boto3_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> Boto3Module:
```

Parse data for boto3-stubs module.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

MasterModule structure.
