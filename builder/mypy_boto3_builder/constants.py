from pathlib import Path

# Master module name
MODULE_NAME = "mypy_boto3"

# PyPI module name
PYPI_NAME = "mypy-boto3"

# Postfix for package name generated with docs
WITH_DOCS_POSTFIX = "_with_docs"

# Postfix for PyPI module name generated with docs
WITH_DOCS_PYPI_POSTFIX = "-with-docs"

# Random region to initialize services
DUMMY_REGION = "us-west-2"

# Static file assets, format-ready
ASSETS_PATH = Path(__file__).parent / "assets"

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH = Path(__file__).parent / "templates"
