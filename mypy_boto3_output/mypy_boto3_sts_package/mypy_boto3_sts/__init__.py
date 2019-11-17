"Main interface for sts service"

from mypy_boto3_sts.client import Client
from mypy_boto3_sts.helpers import boto3_client


__all__ = ("Client", "boto3_client")
