"Main interface for pinpoint service"

from mypy_boto3_pinpoint.client import Client
from mypy_boto3_pinpoint.helpers import boto3_client


__all__ = ("Client", "boto3_client")
