from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class InternalImportRecord(ImportRecord):
    _is_internal = True

    def get_external(self, module_name: str) -> ImportRecord:
        source = f"{module_name}.{self.source}"
        return ImportRecord(source=source, name=self.name, alias=self.alias,)
