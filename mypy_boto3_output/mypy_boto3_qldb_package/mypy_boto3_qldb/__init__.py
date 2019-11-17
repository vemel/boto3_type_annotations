"Main interface for qldb service"

from mypy_boto3_qldb.client import Client
from mypy_boto3_qldb.helpers import boto3_client


__all__ = ("Client", "boto3_client")
