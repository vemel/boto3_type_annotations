"Main interface for ecr service"

from mypy_boto3_ecr.client import Client
from mypy_boto3_ecr.helpers import boto3_client


__all__ = ("Client", "boto3_client")
