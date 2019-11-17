"Main interface for license-manager service"

from mypy_boto3_license_manager.client import Client
from mypy_boto3_license_manager.helpers import boto3_client


__all__ = ("Client", "boto3_client")
