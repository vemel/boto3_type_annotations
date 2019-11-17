"Main interface for codepipeline service"

from mypy_boto3_codepipeline.client import Client
from mypy_boto3_codepipeline.helpers import boto3_client


__all__ = ("Client", "boto3_client")
