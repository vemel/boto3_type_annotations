"Main interface for dax service"

from mypy_boto3_dax.client import Client
from mypy_boto3_dax.helpers import boto3_client


__all__ = ("Client", "boto3_client")
