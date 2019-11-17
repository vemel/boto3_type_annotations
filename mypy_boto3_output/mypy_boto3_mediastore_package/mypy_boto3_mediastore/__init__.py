"Main interface for mediastore service"

from mypy_boto3_mediastore.client import Client
from mypy_boto3_mediastore.helpers import boto3_client


__all__ = ("Client", "boto3_client")
