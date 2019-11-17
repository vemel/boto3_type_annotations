"Main interface for inspector service"

from mypy_boto3_inspector.client import Client
from mypy_boto3_inspector.helpers import boto3_client


__all__ = ("Client", "boto3_client")
