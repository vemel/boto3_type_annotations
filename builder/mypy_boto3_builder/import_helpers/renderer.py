import inspect
import builtins
from typing import Iterable, Set, Generator, Dict, Optional

from mypy_boto3_builder.structures import TypeAnnotation, FakeAnnotation
from mypy_boto3_builder.utils import render_type_annotation
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.enums import ImportRecordType
from mypy_boto3_builder.service_name import ServiceName


class ImportRecordRenderer:
    boto_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

    def __init__(
        self, module_name: str, default_import_records: Iterable[ImportRecord] = ()
    ) -> None:
        self.module_import_string = ImportString(module_name)
        self.default_import_records = default_import_records
        self.local_import_strings: Set[ImportString] = set()

    def _get_import_record_type(self, import_record: ImportRecord) -> ImportRecordType:
        if import_record.source.parts[0].startswith("__"):
            return ImportRecordType.magic

        for local_import_string in self.local_import_strings:
            if import_record.source.startswith(local_import_string):
                return ImportRecordType.local

        for boto_import_string in self.boto_import_strings:
            if import_record.source.startswith(boto_import_string):
                return ImportRecordType.boto

        return ImportRecordType.python

    def _get_import_record(
        self, type_annotation: TypeAnnotation
    ) -> Optional[ImportRecord]:
        if isinstance(type_annotation, FakeAnnotation):
            import_record = type_annotation.get_import_record()
            if type_annotation.is_internal:
                localized_import_record = self.get_localized(import_record)
                self.local_import_strings.add(localized_import_record.source)
                return localized_import_record

            return import_record

        parent_module = inspect.getmodule(type_annotation)
        if parent_module is None or parent_module == builtins:
            return None

        parent_module_name = parent_module.__name__
        return ImportRecord(
            source=parent_module_name, name=render_type_annotation(type_annotation),
        )

    def get_localized(self, import_record: ImportRecord) -> ImportRecord:
        import_service_name = import_record.source.parts[0]
        service_name = ServiceName.get(import_service_name)
        source = ImportString(f"{self.module_import_string}_{service_name.name}")
        source.parts.extend(import_record.source.parts[1:])

        return ImportRecord(
            source=source.render(), name=import_record.name, alias=import_record.alias,
        )

    def generate_lines(
        self,
        *,
        import_records: Iterable[ImportRecord] = (),
        type_annotations: Iterable[TypeAnnotation] = (),
    ) -> Generator[str, None, None]:
        all_import_records: Set[ImportRecord] = set()
        all_import_records.update(
            self.default_import_records,
            import_records,
            self._get_import_records(type_annotations),
        )

        typed_import_records: Dict[ImportRecordType, Set[ImportRecord]] = {
            k: set() for k in ImportRecordType
        }

        for import_record in all_import_records:
            import_record_type = self._get_import_record_type(import_record)
            typed_import_records[import_record_type].add(import_record)

        for import_record_type in ImportRecordType.items():
            if not typed_import_records[import_record_type]:
                continue

            for import_string in sorted(typed_import_records[import_record_type]):
                comment = import_record_type.get_comment()
                if comment:
                    yield f"# {comment}"
                yield import_string.render()
            yield ""

    def _get_import_records(
        self, type_annotations: Iterable[TypeAnnotation]
    ) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        for type_annotation in type_annotations:
            import_record = self._get_import_record(type_annotation)
            if import_record:
                import_records.add(import_record)

        return import_records
