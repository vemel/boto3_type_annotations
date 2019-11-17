"Main interface for translate service"

from mypy_boto3_translate.client import Client
from mypy_boto3_translate.helpers import boto3_client


__all__ = ("Client", "boto3_client")
