"Main interface for ram service"

from mypy_boto3_ram.client import Client
from mypy_boto3_ram.helpers import boto3_client


__all__ = ("Client", "boto3_client")
