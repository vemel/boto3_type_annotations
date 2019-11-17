"Main interface for route53 service"

from mypy_boto3_route53.client import Client
from mypy_boto3_route53.helpers import boto3_client


__all__ = ("Client", "boto3_client")
