import unittest
from unittest.mock import MagicMock

from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


class MethodTypeMapTestCase(unittest.TestCase):
    def test_get_method_type_stub(self) -> None:
        service_name_mock = MagicMock()
        service_name_mock.boto3_name = "s3"
        self.assertTrue(
            get_method_type_stub(
                service_name_mock, "Client", "copy_object", "CopySource"
            )
        )
        service_name_mock.boto3_name = "ec2"
        self.assertTrue(
            get_method_type_stub(service_name_mock, "Any", "create_tags", "Resources")
        )
        service_name_mock.boto3_name = "s3"
        self.assertIsNone(
            get_method_type_stub(service_name_mock, "Client", "copy_object", "Unknown")
        )
