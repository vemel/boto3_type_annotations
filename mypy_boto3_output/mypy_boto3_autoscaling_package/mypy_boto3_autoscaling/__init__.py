"Main interface for autoscaling service"

from mypy_boto3_autoscaling.client import Client
from mypy_boto3_autoscaling.helpers import boto3_client


__all__ = ("Client", "boto3_client")
