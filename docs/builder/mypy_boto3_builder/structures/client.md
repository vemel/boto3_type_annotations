# Client

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.client](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/client.py) module.

Boto3 Client.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Client
    - [Client](#client)
        - [Client().get_all_names](#clientget_all_names)
        - [Client().get_import_records](#clientget_import_records)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/client.py#L18)

```python
dataclass
class Client(ClassRecord):
```

Boto3 Client.

### Client().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/client.py#L46)

```python
def get_all_names() -> List[str]:
```

### Client().get_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/client.py#L40)

```python
def get_import_records() -> Set[ImportRecord]:
```
