"Main interface for application-autoscaling service"

from mypy_boto3_application_autoscaling.client import Client
from mypy_boto3_application_autoscaling.helpers import boto3_client


__all__ = ("Client", "boto3_client")
