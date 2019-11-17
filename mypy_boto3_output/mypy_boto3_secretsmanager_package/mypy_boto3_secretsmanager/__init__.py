"Main interface for secretsmanager service"

from mypy_boto3_secretsmanager.client import Client
from mypy_boto3_secretsmanager.helpers import boto3_client


__all__ = ("Client", "boto3_client")
