"Main interface for sms service"

from mypy_boto3_sms.client import Client
from mypy_boto3_sms.helpers import boto3_client


__all__ = ("Client", "boto3_client")
