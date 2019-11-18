# Utils

> Auto-generated documentation for [builder.mypy_boto3_builder.writers.utils](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py) module.

Jinja2 renderer and black formatter.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Utils
    - [blackify](#blackify)
    - [render_jinja2_template](#render_jinja2_template)

## blackify

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py#L26)

```python
def blackify(content: str, file_path: Path, fast: bool = True) -> str:
```

Format `content` with `black` if `file_path` is `*.py` or `*.pyi`.

On error writes invalid `content` to `file_path` to check for errors.

#### Arguments

- `content` - Python code to format.
- `file_path` - Target file path.
- `fast` - Whether to skip AST post-check.

#### Returns

Formatted python code.

#### Raises

- `ValueError` - If `content` is not a valid Python code.

## render_jinja2_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/writers/utils.py#L58)

```python
def render_jinja2_template(template_path: Path, **kwargs: Any) -> str:
```

Render Jinja2 template to a string.

#### Arguments

- `template_path` - Relative path to template in `TEMPLATES_PATH`
- `kwargs` - Format arguments.

#### Returns

A rendered template.
