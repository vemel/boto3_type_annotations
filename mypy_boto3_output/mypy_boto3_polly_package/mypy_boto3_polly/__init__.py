"Main interface for polly service"

from mypy_boto3_polly.client import Client
from mypy_boto3_polly.helpers import boto3_client


__all__ = ("Client", "boto3_client")
