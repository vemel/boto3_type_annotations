"Main interface for elastictranscoder service"

from mypy_boto3_elastictranscoder.client import Client
from mypy_boto3_elastictranscoder.helpers import boto3_client


__all__ = ("Client", "boto3_client")
