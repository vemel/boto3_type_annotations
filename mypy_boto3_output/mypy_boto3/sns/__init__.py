"Main interface for sns service"

from mypy_boto3.sns.client import Client
from mypy_boto3.sns.service_resource import Topic
from mypy_boto3.sns.service_resource import PlatformApplication
from mypy_boto3.sns.service_resource import endpoints
from mypy_boto3.sns.service_resource import ServiceResource
from mypy_boto3.sns.service_resource import Subscription
from mypy_boto3.sns.service_resource import topics
from mypy_boto3.sns.service_resource import PlatformEndpoint
from mypy_boto3.sns.service_resource import subscriptions
from mypy_boto3.sns.service_resource import platform_applications

__all__ = (
    "Client",
    "Topic",
    "PlatformApplication",
    "endpoints",
    "ServiceResource",
    "Subscription",
    "topics",
    "PlatformEndpoint",
    "subscriptions",
    "platform_applications",
)
