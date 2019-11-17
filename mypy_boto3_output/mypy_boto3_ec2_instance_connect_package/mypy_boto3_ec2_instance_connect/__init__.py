"Main interface for ec2-instance-connect service"

from mypy_boto3_ec2_instance_connect.client import Client
from mypy_boto3_ec2_instance_connect.helpers import boto3_client


__all__ = ("Client", "boto3_client")
