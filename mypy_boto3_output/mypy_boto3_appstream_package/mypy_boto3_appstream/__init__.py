"Main interface for appstream service"

from mypy_boto3_appstream.client import Client
from mypy_boto3_appstream.helpers import boto3_client


__all__ = ("Client", "boto3_client")
