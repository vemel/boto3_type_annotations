"Main interface for opsworks service"

from mypy_boto3_opsworks.client import Client
from mypy_boto3_opsworks.service_resource import Layer
from mypy_boto3_opsworks.service_resource import ServiceResource
from mypy_boto3_opsworks.service_resource import Stack
from mypy_boto3_opsworks.service_resource import StackSummary


__all__ = ("Client", "Layer", "ServiceResource", "Stack", "StackSummary")
