"Main interface for connect service"

from mypy_boto3_connect.client import Client
from mypy_boto3_connect.helpers import boto3_client


__all__ = ("Client", "boto3_client")
