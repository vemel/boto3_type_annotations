"Main interface for elasticbeanstalk service"

from mypy_boto3_elasticbeanstalk.client import Client
from mypy_boto3_elasticbeanstalk.helpers import boto3_client


__all__ = ("Client", "boto3_client")
