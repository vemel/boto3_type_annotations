"Main interface for docdb service"

from mypy_boto3_docdb.client import Client
from mypy_boto3_docdb.helpers import boto3_client


__all__ = ("Client", "boto3_client")
