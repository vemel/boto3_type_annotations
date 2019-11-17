"Main interface for dynamodbstreams service"

from mypy_boto3_dynamodbstreams.client import Client
from mypy_boto3_dynamodbstreams.helpers import boto3_client


__all__ = ("Client", "boto3_client")
