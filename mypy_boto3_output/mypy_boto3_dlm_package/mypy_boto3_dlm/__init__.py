"Main interface for dlm service"

from mypy_boto3_dlm.client import Client
from mypy_boto3_dlm.helpers import boto3_client


__all__ = ("Client", "boto3_client")
