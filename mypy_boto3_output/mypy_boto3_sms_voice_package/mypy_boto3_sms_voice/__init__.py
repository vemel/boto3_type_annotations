"Main interface for sms-voice service"

from mypy_boto3_sms_voice.client import Client
from mypy_boto3_sms_voice.helpers import boto3_client


__all__ = ("Client", "boto3_client")
