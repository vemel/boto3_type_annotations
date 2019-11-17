"Main interface for support service"

from mypy_boto3_support.client import Client
from mypy_boto3_support.helpers import boto3_client


__all__ = ("Client", "boto3_client")
