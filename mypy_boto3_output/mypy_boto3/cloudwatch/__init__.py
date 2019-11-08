"Main interface for cloudwatch service"

from mypy_boto3.cloudwatch.client import Client
from mypy_boto3.cloudwatch.service_resource import Alarm
from mypy_boto3.cloudwatch.service_resource import Metric
from mypy_boto3.cloudwatch.service_resource import ServiceResource
from mypy_boto3.cloudwatch.service_resource import alarms
from mypy_boto3.cloudwatch.service_resource import metrics

__all__ = (
    "Client",
    "Alarm",
    "Metric",
    "ServiceResource",
    "alarms",
    "metrics",
)
