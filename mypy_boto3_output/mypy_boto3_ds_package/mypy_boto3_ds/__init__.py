"Main interface for ds service"

from mypy_boto3_ds.client import Client
from mypy_boto3_ds.helpers import boto3_client


__all__ = ("Client", "boto3_client")
