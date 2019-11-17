"Main interface for shield service"

from mypy_boto3_shield.client import Client
from mypy_boto3_shield.helpers import boto3_client


__all__ = ("Client", "boto3_client")
