"Main interface for appsync service"

from mypy_boto3_appsync.client import Client
from mypy_boto3_appsync.helpers import boto3_client


__all__ = ("Client", "boto3_client")
