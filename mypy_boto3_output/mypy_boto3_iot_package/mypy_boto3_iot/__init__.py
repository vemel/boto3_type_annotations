"Main interface for iot service"

from mypy_boto3_iot.client import Client
from mypy_boto3_iot.helpers import boto3_client


__all__ = ("Client", "boto3_client")
