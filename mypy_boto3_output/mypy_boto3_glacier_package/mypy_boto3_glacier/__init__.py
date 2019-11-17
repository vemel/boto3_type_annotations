"Main interface for glacier service"

from mypy_boto3_glacier.client import Client
from mypy_boto3_glacier.helpers import boto3_client, boto3_resource
from mypy_boto3_glacier.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
