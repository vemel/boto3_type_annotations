# Boto3 Utils

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.boto3_utils](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_utils.py) module.

Getters for boto3 client and resource from session.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Boto3 Utils
    - [get_boto3_client](#get_boto3_client)
    - [get_boto3_resource](#get_boto3_resource)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_utils.py#L14)

```python
def get_boto3_client(
    session: Session,
    service_name: ServiceName,
) -> BaseClient:
```

Get boto3 client from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 client.

## get_boto3_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/boto3_utils.py#L28)

```python
def get_boto3_resource(
    session: Session,
    service_name: ServiceName,
) -> Optional[Boto3ServiceResource]:
```

Get boto3 resource from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 resource or None.
