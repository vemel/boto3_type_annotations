from typing import Iterable, Set, Generator, Dict, Optional

from mypy_boto3_builder.structures import FakeAnnotation
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.enums import ImportRecordType


class ImportRecordRenderer:
    boto_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

    def __init__(
        self,
        local_modules: Iterable[str],
        common_import_records: Iterable[ImportRecord] = (),
    ) -> None:
        self.common_import_records = common_import_records
        self.local_import_strings = [ImportString(i) for i in local_modules]

    def _get_import_record_type(self, import_record: ImportRecord) -> ImportRecordType:
        if import_record.source.parts[0] == "builtins":
            return ImportRecordType.builtins

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
        self, type_annotation: FakeAnnotation
    ) -> Optional[ImportRecord]:
        import_record = type_annotation.get_import_record()
        return import_record

    def generate_lines(
        self, type_annotations: Iterable[FakeAnnotation] = (),
    ) -> Generator[str, None, None]:
        all_import_records: Set[ImportRecord] = set()
        all_import_records.update(
            self.common_import_records, self._get_import_records(type_annotations),
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
        self, type_annotations: Iterable[FakeAnnotation]
    ) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        for type_annotation in type_annotations:
            import_records.add(type_annotation.get_import_record())

        return import_records
