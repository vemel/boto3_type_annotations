"Main interface for mediaconvert service"

from mypy_boto3_mediaconvert.client import Client
from mypy_boto3_mediaconvert.helpers import boto3_client


__all__ = ("Client", "boto3_client")
