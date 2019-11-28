import unittest

from mypy_boto3_builder.type_maps.method_type_map import METHOD_TYPE_MAP


class IndentTrimmerTestCase(unittest.TestCase):
    def test_main(self) -> None:
        self.assertTrue(METHOD_TYPE_MAP["page_size: count"])
