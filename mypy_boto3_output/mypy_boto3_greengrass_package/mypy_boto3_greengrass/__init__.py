"Main interface for greengrass service"

from mypy_boto3_greengrass.client import Client
from mypy_boto3_greengrass.helpers import boto3_client


__all__ = ("Client", "boto3_client")
