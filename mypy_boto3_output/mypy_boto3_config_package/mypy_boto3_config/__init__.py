"Main interface for config service"

from mypy_boto3_config.client import Client
from mypy_boto3_config.helpers import boto3_client


__all__ = ("Client", "boto3_client")
