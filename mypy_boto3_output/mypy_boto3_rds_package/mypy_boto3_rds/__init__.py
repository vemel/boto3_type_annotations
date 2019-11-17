"Main interface for rds service"

from mypy_boto3_rds.client import Client
from mypy_boto3_rds.helpers import boto3_client


__all__ = ("Client", "boto3_client")
