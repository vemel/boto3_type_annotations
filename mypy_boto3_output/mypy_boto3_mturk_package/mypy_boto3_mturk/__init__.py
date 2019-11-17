"Main interface for mturk service"

from mypy_boto3_mturk.client import Client
from mypy_boto3_mturk.helpers import boto3_client


__all__ = ("Client", "boto3_client")
