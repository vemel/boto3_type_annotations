# Fake Service Package

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.fake_service_package](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/fake_service_package.py) module.

Fake parser that produces `structures.ServiceModule` for master module and stubs.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Fake Service Package
    - [parse_fake_service_package](#parse_fake_service_package)

## parse_fake_service_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/fake_service_package.py#L18)

```python
def parse_fake_service_package(
    session: Session,
    service_name: ServiceName,
) -> ServicePackage:
```

Create fake boto3 service module structure.

Used by stubs and master package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceModule structure.
