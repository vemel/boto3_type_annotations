"Main interface for s3control service"

from mypy_boto3_s3control.client import Client
from mypy_boto3_s3control.helpers import boto3_client


__all__ = ("Client", "boto3_client")
