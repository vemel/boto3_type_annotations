from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.constants import MODULE_NAME


class TypeDef(ExternalImport):
    def __init__(self, name: str) -> None:
        super().__init__(
            source=f"{MODULE_NAME}.type_defs", name=name, alias=f"TypeDef{name}",
        )
