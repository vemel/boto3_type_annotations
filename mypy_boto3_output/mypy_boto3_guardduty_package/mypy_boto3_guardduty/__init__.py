"Main interface for guardduty service"

from mypy_boto3_guardduty.client import Client
from mypy_boto3_guardduty.helpers import boto3_client


__all__ = ("Client", "boto3_client")
