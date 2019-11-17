"Main interface for sns service"

from mypy_boto3_sns.client import Client
from mypy_boto3_sns.helpers import boto3_client, boto3_resource
from mypy_boto3_sns.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
