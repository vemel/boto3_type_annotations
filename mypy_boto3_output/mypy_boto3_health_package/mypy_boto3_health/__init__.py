"Main interface for health service"

from mypy_boto3_health.client import Client
from mypy_boto3_health.helpers import boto3_client


__all__ = ("Client", "boto3_client")
