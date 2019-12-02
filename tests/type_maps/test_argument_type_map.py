import unittest

from mypy_boto3_builder.type_maps.argument_type_map import ARGUMENT_TYPE_MAP


class IndentTrimmerTestCase(unittest.TestCase):
    def test_main(self) -> None:
        self.assertTrue(ARGUMENT_TYPE_MAP["DryRun: bool"])
