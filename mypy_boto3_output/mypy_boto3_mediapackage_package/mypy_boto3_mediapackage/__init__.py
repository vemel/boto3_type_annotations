"Main interface for mediapackage service"

from mypy_boto3_mediapackage.client import Client
from mypy_boto3_mediapackage.helpers import boto3_client


__all__ = ("Client", "boto3_client")
