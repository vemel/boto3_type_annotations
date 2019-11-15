"Main interface for dynamodb service"

from mypy_boto3_dynamodb.client import Client
from mypy_boto3_dynamodb.service_resource import ServiceResource
from mypy_boto3_dynamodb.service_resource import Table
from mypy_boto3_dynamodb.service_resource import tables

__all__ = (
    "Client",
    "ServiceResource",
    "Table",
    "tables",
)
