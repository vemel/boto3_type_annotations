"Main interface for cognito-sync service"

from mypy_boto3_cognito_sync.client import Client
from mypy_boto3_cognito_sync.helpers import boto3_client


__all__ = ("Client", "boto3_client")
