"Main interface for ecs service"

from mypy_boto3_ecs.client import Client
from mypy_boto3_ecs.helpers import boto3_client


__all__ = ("Client", "boto3_client")
