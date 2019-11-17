"Main interface for appmesh service"

from mypy_boto3_appmesh.client import Client
from mypy_boto3_appmesh.helpers import boto3_client


__all__ = ("Client", "boto3_client")
