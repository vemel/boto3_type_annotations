"Main interface for fms service"

from mypy_boto3_fms.client import Client
from mypy_boto3_fms.helpers import boto3_client


__all__ = ("Client", "boto3_client")
