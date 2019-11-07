"Main interface for opsworks service"

from mypy_boto3.opsworks.client import Client
from mypy_boto3.opsworks.service_resource import ServiceResource
from mypy_boto3.opsworks.service_resource import Layer
from mypy_boto3.opsworks.service_resource import stacks
from mypy_boto3.opsworks.service_resource import Stack
from mypy_boto3.opsworks.service_resource import StackSummary
from mypy_boto3.opsworks.service_resource import layers

__all__ = (
    "Client",
    "ServiceResource",
    "Layer",
    "stacks",
    "Stack",
    "StackSummary",
    "layers",
)
