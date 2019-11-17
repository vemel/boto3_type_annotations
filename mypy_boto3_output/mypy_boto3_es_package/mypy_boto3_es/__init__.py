"Main interface for es service"

from mypy_boto3_es.client import Client
from mypy_boto3_es.helpers import boto3_client


__all__ = ("Client", "boto3_client")
