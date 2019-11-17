"Main interface for kafka service"

from mypy_boto3_kafka.client import Client
from mypy_boto3_kafka.helpers import boto3_client


__all__ = ("Client", "boto3_client")
