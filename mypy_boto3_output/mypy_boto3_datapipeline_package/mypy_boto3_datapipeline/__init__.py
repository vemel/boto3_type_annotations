"Main interface for datapipeline service"

from mypy_boto3_datapipeline.client import Client
from mypy_boto3_datapipeline.helpers import boto3_client


__all__ = ("Client", "boto3_client")
