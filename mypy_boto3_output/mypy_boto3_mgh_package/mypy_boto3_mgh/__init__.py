"Main interface for mgh service"

from mypy_boto3_mgh.client import Client
from mypy_boto3_mgh.helpers import boto3_client


__all__ = ("Client", "boto3_client")
