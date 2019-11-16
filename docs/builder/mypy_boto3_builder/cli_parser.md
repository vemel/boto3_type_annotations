# Cli Parser

> Auto-generated documentation for [builder.mypy_boto3_builder.cli_parser](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/cli_parser.py) module.

CLI parser.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Cli Parser
    - [get_absolute_path](#get_absolute_path)
    - [get_cli_parser](#get_cli_parser)
    - [get_service_name](#get_service_name)

## get_absolute_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/cli_parser.py#L10)

```python
def get_absolute_path(path: str) -> Path:
```

Get absolute path from a string.

#### Arguments

- `path` - String containing path.

#### Returns

Absolute path.

## get_cli_parser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/cli_parser.py#L39)

```python
def get_cli_parser() -> argparse.ArgumentParser:
```

Main CLI parser for builder.

#### Returns

Argument parser.

## get_service_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/cli_parser.py#L23)

```python
def get_service_name(name: str) -> ServiceName:
```

Convert boto3 service name to ServiceName.

#### Arguments

- `name` - Service name.

#### Raises

- `argparse.ArgumentTypeError` - If service not found.
