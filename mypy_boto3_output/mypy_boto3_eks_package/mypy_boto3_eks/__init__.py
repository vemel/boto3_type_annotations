"Main interface for eks service"

from mypy_boto3_eks.client import Client
from mypy_boto3_eks.helpers import boto3_client


__all__ = ("Client", "boto3_client")
