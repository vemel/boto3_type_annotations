"Main interface for textract service"

from mypy_boto3_textract.client import Client
from mypy_boto3_textract.helpers import boto3_client


__all__ = ("Client", "boto3_client")
