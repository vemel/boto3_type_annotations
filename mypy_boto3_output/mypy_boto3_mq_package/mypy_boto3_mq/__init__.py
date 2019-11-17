"Main interface for mq service"

from mypy_boto3_mq.client import Client
from mypy_boto3_mq.helpers import boto3_client


__all__ = ("Client", "boto3_client")
