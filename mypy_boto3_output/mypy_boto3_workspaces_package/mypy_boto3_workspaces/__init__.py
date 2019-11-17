"Main interface for workspaces service"

from mypy_boto3_workspaces.client import Client
from mypy_boto3_workspaces.helpers import boto3_client


__all__ = ("Client", "boto3_client")
