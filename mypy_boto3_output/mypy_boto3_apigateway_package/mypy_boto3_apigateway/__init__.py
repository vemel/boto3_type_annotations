"Main interface for apigateway service"

from mypy_boto3_apigateway.client import Client
from mypy_boto3_apigateway.helpers import boto3_client


__all__ = ("Client", "boto3_client")
