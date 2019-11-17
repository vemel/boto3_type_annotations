"Main interface for s3 service"

from mypy_boto3_s3.client import Client
from mypy_boto3_s3.helpers import boto3_client, boto3_resource
from mypy_boto3_s3.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
