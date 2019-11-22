import unittest

from mypy_boto3_builder.enums.service_name import ServiceName


class ServiceNameTestCase(unittest.TestCase):
    def test_init(self) -> None:
        self.assertTrue(ServiceName.items())
        self.assertIsInstance(ServiceName.items()[0], ServiceName)

        self.assertTrue(ServiceName.values())
        self.assertIsInstance(ServiceName.values()[0], str)

    def test_properties(self) -> None:
        self.assertEqual(ServiceName.ec2.module_name, "mypy_boto3_ec2")
        self.assertEqual(ServiceName.ec2.extras_name, "ec2")
        self.assertEqual(ServiceName.ec2.import_name, "ec2")
        self.assertEqual(ServiceName.ec2.pypi_name, "mypy-boto3-ec2")
        self.assertEqual(ServiceName.ec2.boto3_name, "ec2")
        self.assertEqual(ServiceName.ec2.class_prefix, "EC2")

        self.assertEqual(ServiceName.lambda_.module_name, "mypy_boto3_lambda")
        self.assertEqual(ServiceName.lambda_.extras_name, "lambda")
        self.assertEqual(ServiceName.lambda_.import_name, "lambda_")
        self.assertEqual(ServiceName.lambda_.pypi_name, "mypy-boto3-lambda")
        self.assertEqual(ServiceName.lambda_.boto3_name, "lambda")
        self.assertEqual(ServiceName.lambda_.class_prefix, "Lambda")

    def test_is_essential(self) -> None:
        self.assertTrue(ServiceName.ec2.is_essential())
        self.assertFalse(ServiceName.acm.is_essential())
