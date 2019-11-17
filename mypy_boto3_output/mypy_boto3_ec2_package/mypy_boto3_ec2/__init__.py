"Main interface for ec2 service"

from mypy_boto3_ec2.client import Client
from mypy_boto3_ec2.helpers import boto3_client, boto3_resource
from mypy_boto3_ec2.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource", "boto3_client", "boto3_resource")
