"Main interface for efs service"

from mypy_boto3_efs.client import Client
from mypy_boto3_efs.helpers import boto3_client


__all__ = ("Client", "boto3_client")
