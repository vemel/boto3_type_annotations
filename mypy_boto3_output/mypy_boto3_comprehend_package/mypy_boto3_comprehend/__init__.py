"Main interface for comprehend service"

from mypy_boto3_comprehend.client import Client
from mypy_boto3_comprehend.helpers import boto3_client


__all__ = ("Client", "boto3_client")
