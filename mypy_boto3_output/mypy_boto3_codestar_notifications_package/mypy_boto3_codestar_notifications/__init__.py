"Main interface for codestar-notifications service"

from mypy_boto3_codestar_notifications.client import Client
from mypy_boto3_codestar_notifications.helpers import boto3_client


__all__ = ("Client", "boto3_client")
