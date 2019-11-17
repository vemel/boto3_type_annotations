"Main interface for cognito-idp service"

from mypy_boto3_cognito_idp.client import Client
from mypy_boto3_cognito_idp.helpers import boto3_client


__all__ = ("Client", "boto3_client")
