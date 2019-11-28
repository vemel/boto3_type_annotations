import unittest

from mypy_boto3_builder.type_maps.named_type_map import NAMED_TYPE_MAP


class IndentTrimmerTestCase(unittest.TestCase):
    def test_main(self) -> None:
        self.assertTrue(NAMED_TYPE_MAP["DryRun: bool"])
