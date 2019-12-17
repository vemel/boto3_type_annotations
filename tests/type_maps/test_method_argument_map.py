import unittest
from unittest.mock import MagicMock

from mypy_boto3_builder.type_maps.method_argument_map import get_method_arguments_stub


class MethodArgumentMapTestCase(unittest.TestCase):
    def test_get_method_arguments_stub(self) -> None:
        service_name_mock = MagicMock()
        service_name_mock.boto3_name = "ec2"
        self.assertTrue(
            get_method_arguments_stub(service_name_mock, "Instance", "delete_tags")[0]
        )
        self.assertIsNone(
            get_method_arguments_stub(service_name_mock, "Instance", "unknown")
        )
        self.assertIsNone(
            get_method_arguments_stub(service_name_mock, "unknown", "delete_tags")
        )
