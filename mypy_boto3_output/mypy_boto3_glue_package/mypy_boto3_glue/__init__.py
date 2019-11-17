"Main interface for glue service"

from mypy_boto3_glue.client import Client
from mypy_boto3_glue.helpers import boto3_client


__all__ = ("Client", "boto3_client")
