"Main interface for machinelearning service"

from mypy_boto3_machinelearning.client import Client
from mypy_boto3_machinelearning.helpers import boto3_client


__all__ = ("Client", "boto3_client")
