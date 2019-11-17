"Main interface for neptune service"

from mypy_boto3_neptune.client import Client
from mypy_boto3_neptune.helpers import boto3_client


__all__ = ("Client", "boto3_client")
