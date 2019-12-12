import unittest

from mypy_boto3_builder.type_maps.type_map import TYPE_MAP


class TypeMapTestCase(unittest.TestCase):
    def test_main(self) -> None:
        self.assertTrue(TYPE_MAP["bytes"])
