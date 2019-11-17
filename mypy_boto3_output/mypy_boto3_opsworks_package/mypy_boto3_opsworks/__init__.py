"Main interface for opsworks service"

from mypy_boto3_opsworks.client import Client
from mypy_boto3_opsworks.helpers import boto3_client, boto3_resource
from mypy_boto3_opsworks.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
