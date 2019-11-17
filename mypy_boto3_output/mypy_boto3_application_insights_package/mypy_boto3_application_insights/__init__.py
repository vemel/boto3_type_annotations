"Main interface for application-insights service"

from mypy_boto3_application_insights.client import Client
from mypy_boto3_application_insights.helpers import boto3_client


__all__ = ("Client", "boto3_client")
