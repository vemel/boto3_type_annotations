# Utils

> Auto-generated documentation for [builder.mypy_boto3_builder.utils](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils.py) module.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Utils
    - [black_reformat](#black_reformat)
    - [clean_doc](#clean_doc)
    - [render_template](#render_template)
    - [render_type_annotation](#render_type_annotation)

## black_reformat

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils.py#L58)

```python
def black_reformat(source_path: Path) -> bool:
```

## clean_doc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils.py#L38)

```python
def clean_doc(doc: Optional[str]) -> str:
```

## render_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils.py#L53)

```python
def render_template(template_name: str, **kwargs: str) -> str:
```

## render_type_annotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/utils.py#L9)

```python
def render_type_annotation(
    type_annotation: TypeAnnotation,
    render_args: bool = False,
) -> str:
```
