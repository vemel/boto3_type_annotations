"""
Helper for Python import strings with not set master module name.
"""
from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class InternalImportRecord(ImportRecord):
    """
    Helper for Python import strings with not set master module name.

    Used in TypeDef.
    """

    _is_internal = True

    def get_external(self, module_name: str) -> ImportRecord:
        """
        Get full import record with `module_name` set as master module.

        Arguments:
            module_name -- Master module import string.

        Returns:
            A new non-internal ImportRecord.
        """
        source = f"{module_name}.{self.source}"
        return ImportRecord(source=source, name=self.name, alias=self.alias,)
