"Main interface for sns service"

from mypy_boto3_sns.client import Client
from mypy_boto3_sns.service_resource import PlatformApplication
from mypy_boto3_sns.service_resource import PlatformEndpoint
from mypy_boto3_sns.service_resource import ServiceResource
from mypy_boto3_sns.service_resource import Subscription
from mypy_boto3_sns.service_resource import Topic


__all__ = (
    "Client",
    "PlatformApplication",
    "PlatformEndpoint",
    "ServiceResource",
    "Subscription",
    "Topic",
)
