"Main interface for cloudwatch service"

from mypy_boto3_cloudwatch.client import Client
from mypy_boto3_cloudwatch.helpers import boto3_client, boto3_resource
from mypy_boto3_cloudwatch.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
