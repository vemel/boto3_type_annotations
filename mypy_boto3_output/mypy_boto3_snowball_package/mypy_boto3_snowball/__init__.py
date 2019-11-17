"Main interface for snowball service"

from mypy_boto3_snowball.client import Client
from mypy_boto3_snowball.helpers import boto3_client


__all__ = ("Client", "boto3_client")
