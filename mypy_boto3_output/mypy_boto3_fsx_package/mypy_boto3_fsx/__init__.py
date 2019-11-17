"Main interface for fsx service"

from mypy_boto3_fsx.client import Client
from mypy_boto3_fsx.helpers import boto3_client


__all__ = ("Client", "boto3_client")
