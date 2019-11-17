"Main interface for sagemaker-runtime service"

from mypy_boto3_sagemaker_runtime.client import Client
from mypy_boto3_sagemaker_runtime.helpers import boto3_client


__all__ = ("Client", "boto3_client")
