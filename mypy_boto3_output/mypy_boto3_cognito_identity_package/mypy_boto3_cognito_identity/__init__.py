"Main interface for cognito-identity service"

from mypy_boto3_cognito_identity.client import Client
from mypy_boto3_cognito_identity.helpers import boto3_client


__all__ = ("Client", "boto3_client")
