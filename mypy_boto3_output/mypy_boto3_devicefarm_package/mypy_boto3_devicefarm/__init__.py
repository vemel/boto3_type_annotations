"Main interface for devicefarm service"

from mypy_boto3_devicefarm.client import Client
from mypy_boto3_devicefarm.helpers import boto3_client


__all__ = ("Client", "boto3_client")
