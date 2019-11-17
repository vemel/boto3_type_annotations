"Main interface for dms service"

from mypy_boto3_dms.client import Client
from mypy_boto3_dms.helpers import boto3_client


__all__ = ("Client", "boto3_client")
