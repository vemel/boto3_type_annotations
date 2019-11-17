"Main interface for codestar service"

from mypy_boto3_codestar.client import Client
from mypy_boto3_codestar.helpers import boto3_client


__all__ = ("Client", "boto3_client")
