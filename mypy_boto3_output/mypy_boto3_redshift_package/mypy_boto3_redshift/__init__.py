"Main interface for redshift service"

from mypy_boto3_redshift.client import Client
from mypy_boto3_redshift.helpers import boto3_client


__all__ = ("Client", "boto3_client")
