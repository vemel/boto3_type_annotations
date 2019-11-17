"Main interface for rekognition service"

from mypy_boto3_rekognition.client import Client
from mypy_boto3_rekognition.helpers import boto3_client


__all__ = ("Client", "boto3_client")
