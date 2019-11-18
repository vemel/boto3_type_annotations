"""
Wrapper for type annotations defined in `mypy_boto3.type_defs` module.
"""
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.constants import MODULE_NAME


class TypeDef(ExternalImport):
    """
    Wrapper for type annotations defined in `mypy_boto3.type_defs` module.

    Arguments:
        name -- Type definition class name.
    """

    def __init__(self, name: str) -> None:
        super().__init__(
            source=ImportString(MODULE_NAME, ServiceModuleName.type_defs.name),
            name=name,
        )
