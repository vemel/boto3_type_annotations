import jinja2
from boto3 import __version__ as boto3_version

from mypy_boto3_builder.constants import (
    TEMPLATES_PATH,
    MODULE_NAME,
    PYPI_NAME,
    BOTO3_STUBS_NAME,
)
from mypy_boto3_builder.version import __version__ as version


__all__ = ["jinja2_env"]


jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
    undefined=jinja2.StrictUndefined,
)
jinja2_env.globals = dict(
    version=version,
    master_pypi_name=PYPI_NAME,
    master_module_name=MODULE_NAME,
    boto3_stubs_name=BOTO3_STUBS_NAME,
    boto3_version=boto3_version,
    render_docstrings=True,
)
