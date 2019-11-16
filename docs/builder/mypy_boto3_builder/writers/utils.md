# Utils

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.utils](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Utils
    - [blackify_str](#blackify_str)
    - [render_jinja2_template](#render_jinja2_template)

## blackify_str

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py#L23)

```python
def blackify_str(
    content: str,
    fast: bool = True,
    is_pyi: bool = False,
) -> str:
```

## render_jinja2_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py#L34)

```python
def render_jinja2_template(template_path: Path, **kwargs: Any) -> str:
```

Render Jinja2 template to a string.

#### Returns

A rendered template.
