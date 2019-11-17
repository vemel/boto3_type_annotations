"Main interface for transcribe service"

from mypy_boto3_transcribe.client import Client
from mypy_boto3_transcribe.helpers import boto3_client


__all__ = ("Client", "boto3_client")
