"Main interface for cloudtrail service"

from mypy_boto3_cloudtrail.client import Client
from mypy_boto3_cloudtrail.helpers import boto3_client


__all__ = ("Client", "boto3_client")
