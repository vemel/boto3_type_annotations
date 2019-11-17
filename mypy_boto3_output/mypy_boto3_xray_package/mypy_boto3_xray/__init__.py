"Main interface for xray service"

from mypy_boto3_xray.client import Client
from mypy_boto3_xray.helpers import boto3_client


__all__ = ("Client", "boto3_client")
