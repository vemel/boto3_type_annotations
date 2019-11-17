"Main interface for kinesis service"

from mypy_boto3_kinesis.client import Client
from mypy_boto3_kinesis.helpers import boto3_client


__all__ = ("Client", "boto3_client")
