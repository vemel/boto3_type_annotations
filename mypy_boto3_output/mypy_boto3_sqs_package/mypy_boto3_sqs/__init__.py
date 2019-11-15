"Main interface for sqs service"

from mypy_boto3_sqs.client import Client
from mypy_boto3_sqs.service_resource import Message
from mypy_boto3_sqs.service_resource import Queue
from mypy_boto3_sqs.service_resource import ServiceResource
from mypy_boto3_sqs.service_resource import dead_letter_source_queues
from mypy_boto3_sqs.service_resource import queues

__all__ = (
    "Client",
    "Message",
    "Queue",
    "ServiceResource",
    "dead_letter_source_queues",
    "queues",
)
