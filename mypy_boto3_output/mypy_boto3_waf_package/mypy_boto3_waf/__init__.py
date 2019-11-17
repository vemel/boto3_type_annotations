"Main interface for waf service"

from mypy_boto3_waf.client import Client
from mypy_boto3_waf.helpers import boto3_client


__all__ = ("Client", "boto3_client")
