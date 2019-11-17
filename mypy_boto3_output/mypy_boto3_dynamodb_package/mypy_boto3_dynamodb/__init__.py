"Main interface for dynamodb service"

from mypy_boto3_dynamodb.client import Client
from mypy_boto3_dynamodb.helpers import boto3_client, boto3_resource
from mypy_boto3_dynamodb.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
