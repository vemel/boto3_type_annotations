"Main interface for sqs service"

from mypy_boto3.sqs.client import Client
from mypy_boto3.sqs.service_resource import Queue
from mypy_boto3.sqs.service_resource import ServiceResource
from mypy_boto3.sqs.service_resource import dead_letter_source_queues
from mypy_boto3.sqs.service_resource import queues
from mypy_boto3.sqs.service_resource import Message

__all__ = (
    "Client",
    "Queue",
    "ServiceResource",
    "dead_letter_source_queues",
    "queues",
    "Message",
)
