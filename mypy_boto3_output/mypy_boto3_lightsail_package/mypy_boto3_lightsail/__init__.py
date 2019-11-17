"Main interface for lightsail service"

from mypy_boto3_lightsail.client import Client
from mypy_boto3_lightsail.helpers import boto3_client


__all__ = ("Client", "boto3_client")
