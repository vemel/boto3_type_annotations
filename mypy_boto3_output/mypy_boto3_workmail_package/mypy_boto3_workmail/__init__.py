"Main interface for workmail service"

from mypy_boto3_workmail.client import Client
from mypy_boto3_workmail.helpers import boto3_client


__all__ = ("Client", "boto3_client")
