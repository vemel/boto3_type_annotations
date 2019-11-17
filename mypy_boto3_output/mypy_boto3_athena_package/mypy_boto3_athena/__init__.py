"Main interface for athena service"

from mypy_boto3_athena.client import Client
from mypy_boto3_athena.helpers import boto3_client


__all__ = ("Client", "boto3_client")
