"Main interface for emr service"

from mypy_boto3_emr.client import Client
from mypy_boto3_emr.helpers import boto3_client


__all__ = ("Client", "boto3_client")
