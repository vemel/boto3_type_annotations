"Main interface for logs service"

from mypy_boto3_logs.client import Client
from mypy_boto3_logs.helpers import boto3_client


__all__ = ("Client", "boto3_client")
