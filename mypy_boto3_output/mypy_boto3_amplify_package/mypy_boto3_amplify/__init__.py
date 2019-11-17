"Main interface for amplify service"

from mypy_boto3_amplify.client import Client
from mypy_boto3_amplify.helpers import boto3_client


__all__ = ("Client", "boto3_client")
