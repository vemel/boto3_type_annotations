"Main interface for forecast service"

from mypy_boto3_forecast.client import Client
from mypy_boto3_forecast.helpers import boto3_client


__all__ = ("Client", "boto3_client")
