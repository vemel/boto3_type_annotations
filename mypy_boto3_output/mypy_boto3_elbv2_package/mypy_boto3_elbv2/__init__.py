"Main interface for elbv2 service"

from mypy_boto3_elbv2.client import Client
from mypy_boto3_elbv2.helpers import boto3_client


__all__ = ("Client", "boto3_client")
