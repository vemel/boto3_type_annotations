"Main interface for iam service"

from mypy_boto3_iam.client import Client
from mypy_boto3_iam.helpers import boto3_client, boto3_resource
from mypy_boto3_iam.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
