# Master Module

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.master_module](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/master_module.py) module.

Parser that produces `structures.MasterModule`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Master Module
    - [parse_master_module](#parse_master_module)

## parse_master_module

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/master_module.py#L12)

```python
def parse_master_module(
    session: Session,
    service_names: Iterable[ServiceName],
) -> MasterModule:
```

Parse data for master module.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

MasterModule structure.
