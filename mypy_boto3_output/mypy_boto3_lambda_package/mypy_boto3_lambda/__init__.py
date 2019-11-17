"Main interface for lambda service"

from mypy_boto3_lambda.client import Client
from mypy_boto3_lambda.helpers import boto3_client


__all__ = ("Client", "boto3_client")
