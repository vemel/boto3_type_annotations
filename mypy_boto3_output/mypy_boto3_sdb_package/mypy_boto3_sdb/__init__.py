"Main interface for sdb service"

from mypy_boto3_sdb.client import Client
from mypy_boto3_sdb.helpers import boto3_client


__all__ = ("Client", "boto3_client")
