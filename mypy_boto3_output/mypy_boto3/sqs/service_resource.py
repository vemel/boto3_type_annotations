from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.sqs.service_resource as sqs_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    queues: sqs_service_resource_scope.queues

    # pylint: disable=arguments-differ
    def Message(
        self, queue_url: str = None, receipt_handle: str = None
    ) -> sqs_service_resource_scope.Message:
        pass

    # pylint: disable=arguments-differ
    def Queue(self, url: str = None) -> sqs_service_resource_scope.Queue:
        pass

    # pylint: disable=arguments-differ
    def create_queue(
        self,
        QueueName: str,
        Attributes: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> sqs_service_resource_scope.Queue:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def get_queue_by_name(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> sqs_service_resource_scope.Queue:
        pass


class Message(Boto3ServiceResource):
    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict
    md5_of_message_attributes: str
    message_attributes: Dict
    queue_url: str
    receipt_handle: str

    # pylint: disable=arguments-differ
    def change_visibility(self, VisibilityTimeout: int) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Queue(Boto3ServiceResource):
    attributes: Dict
    url: str
    dead_letter_source_queues: sqs_service_resource_scope.dead_letter_source_queues

    # pylint: disable=arguments-differ
    def add_permission(
        self, Label: str, AWSAccountIds: List[Any], Actions: List[Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def change_message_visibility_batch(self, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_messages(self, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def purge(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def receive_messages(
        self,
        AttributeNames: List[Any] = None,
        MessageAttributeNames: List[Any] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> List[sqs_service_resource_scope.Message]:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_permission(self, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def send_message(
        self,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, Any] = None,
        MessageSystemAttributes: Dict[str, Any] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_messages(self, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_attributes(self, Attributes: Dict[str, Any]) -> None:
        pass


class queues(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, QueueNamePrefix: str = None
    ) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class dead_letter_source_queues(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(cls) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[sqs_service_resource_scope.Queue]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
