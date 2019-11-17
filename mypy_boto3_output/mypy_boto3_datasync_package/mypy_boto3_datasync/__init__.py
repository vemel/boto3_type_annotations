"Main interface for datasync service"

from mypy_boto3_datasync.client import Client
from mypy_boto3_datasync.helpers import boto3_client


__all__ = ("Client", "boto3_client")
