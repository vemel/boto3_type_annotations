"Main interface for organizations service"

from mypy_boto3_organizations.client import Client
from mypy_boto3_organizations.helpers import boto3_client


__all__ = ("Client", "boto3_client")
