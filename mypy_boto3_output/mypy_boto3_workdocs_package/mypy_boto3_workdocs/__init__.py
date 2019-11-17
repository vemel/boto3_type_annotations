"Main interface for workdocs service"

from mypy_boto3_workdocs.client import Client
from mypy_boto3_workdocs.helpers import boto3_client


__all__ = ("Client", "boto3_client")
