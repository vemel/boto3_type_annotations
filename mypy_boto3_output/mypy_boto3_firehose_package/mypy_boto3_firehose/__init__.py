"Main interface for firehose service"

from mypy_boto3_firehose.client import Client
from mypy_boto3_firehose.helpers import boto3_client


__all__ = ("Client", "boto3_client")
