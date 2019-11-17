# ClassRecord

> Auto-generated documentation for [builder.mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/class_record.py#L13)

```python
dataclass
class ClassRecord():
```

Base class for all structures that can be rendered to a class.

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/class_record.py#L35)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/structures/class_record.py#L25)

```python
def get_types() -> Set[FakeAnnotation]:
```
