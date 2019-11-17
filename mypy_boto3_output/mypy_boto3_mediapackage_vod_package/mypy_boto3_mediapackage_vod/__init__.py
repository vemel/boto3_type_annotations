"Main interface for mediapackage-vod service"

from mypy_boto3_mediapackage_vod.client import Client
from mypy_boto3_mediapackage_vod.helpers import boto3_client


__all__ = ("Client", "boto3_client")
