"Main interface for sns service"

from mypy_boto3.sns.client import Client
from mypy_boto3.sns.service_resource import PlatformApplication
from mypy_boto3.sns.service_resource import PlatformEndpoint
from mypy_boto3.sns.service_resource import ServiceResource
from mypy_boto3.sns.service_resource import Subscription
from mypy_boto3.sns.service_resource import Topic
from mypy_boto3.sns.service_resource import endpoints
from mypy_boto3.sns.service_resource import platform_applications
from mypy_boto3.sns.service_resource import subscriptions
from mypy_boto3.sns.service_resource import topics

__all__ = (
    "Client",
    "PlatformApplication",
    "PlatformEndpoint",
    "ServiceResource",
    "Subscription",
    "Topic",
    "endpoints",
    "platform_applications",
    "subscriptions",
    "topics",
)
