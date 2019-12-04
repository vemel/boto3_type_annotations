# Boto3 Stubs Package

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.boto3_stubs_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_stubs_package.py) module.

Parser that produces `structures.Boto3Module`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Boto3 Stubs Package
    - [parse_boto3_stubs_package](#parse_boto3_stubs_package)

## parse_boto3_stubs_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_stubs_package.py#L13)

```python
def parse_boto3_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
) -> Boto3StubsPackage:
```

Parse data for boto3-stubs package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

MasterModule structure.
