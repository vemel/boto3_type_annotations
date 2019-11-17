"Main interface for ses service"

from mypy_boto3_ses.client import Client
from mypy_boto3_ses.helpers import boto3_client


__all__ = ("Client", "boto3_client")
