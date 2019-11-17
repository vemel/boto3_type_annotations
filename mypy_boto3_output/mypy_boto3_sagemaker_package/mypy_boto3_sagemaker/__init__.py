"Main interface for sagemaker service"

from mypy_boto3_sagemaker.client import Client
from mypy_boto3_sagemaker.helpers import boto3_client


__all__ = ("Client", "boto3_client")
