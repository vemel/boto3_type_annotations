# JinjaManager

> Auto-generated documentation for [builder.mypy_boto3_builder.jinja_manager](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/jinja_manager.py) module.

Jinja2 `Environment` manager.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / JinjaManager
    - [JinjaManager](#jinjamanager)
        - [JinjaManager.get_environment](#jinjamanagerget_environment)
        - [JinjaManager.update_globals](#jinjamanagerupdate_globals)

## JinjaManager

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/jinja_manager.py#L15)

```python
class JinjaManager():
```

Jinja2 `Environment` manager.

### JinjaManager.get_environment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/jinja_manager.py#L35)

```python
@classmethod
def get_environment() -> jinja2.Environment:
```

Get `jinja2.Environment`.

### JinjaManager.update_globals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/jinja_manager.py#L25)

```python
@classmethod
def update_globals(**kwargs: Any) -> None:
```

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.
