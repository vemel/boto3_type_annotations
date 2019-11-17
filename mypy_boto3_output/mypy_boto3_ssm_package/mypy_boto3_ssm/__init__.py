"Main interface for ssm service"

from mypy_boto3_ssm.client import Client
from mypy_boto3_ssm.helpers import boto3_client


__all__ = ("Client", "boto3_client")
