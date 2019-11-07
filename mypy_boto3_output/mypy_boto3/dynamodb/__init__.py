"Main interface for dynamodb service"

from mypy_boto3.dynamodb.client import Client
from mypy_boto3.dynamodb.service_resource import tables
from mypy_boto3.dynamodb.service_resource import Table
from mypy_boto3.dynamodb.service_resource import ServiceResource

__all__ = (
    "Client",
    "tables",
    "Table",
    "ServiceResource",
)
