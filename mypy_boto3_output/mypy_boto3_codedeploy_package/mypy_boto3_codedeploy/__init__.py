"Main interface for codedeploy service"

from mypy_boto3_codedeploy.client import Client
from mypy_boto3_codedeploy.helpers import boto3_client


__all__ = ("Client", "boto3_client")
