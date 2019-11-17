"Main interface for groundstation service"

from mypy_boto3_groundstation.client import Client
from mypy_boto3_groundstation.helpers import boto3_client


__all__ = ("Client", "boto3_client")
