# Client

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.client](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/client.py) module.

Boto3 client parser, produces `structures.Client`.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Client
    - [parse_client](#parse_client)

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/client.py#L18)

```python
def parse_client(session: Session, service_name: ServiceName) -> Client:
```

Parse boto3 client to a structure.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

Client structure.
