from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_permission(
        self, QueueUrl: str, Label: str, AWSAccountIds: List[Any], Actions: List[Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def change_message_visibility(
        self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def change_message_visibility_batch(
        self, QueueUrl: str, Entries: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_queue(
        self,
        QueueName: str,
        Attributes: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_message(self, QueueUrl: str, ReceiptHandle: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_message_batch(self, QueueUrl: str, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_queue(self, QueueUrl: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_queue_attributes(
        self, QueueUrl: str, AttributeNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_queue_url(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_dead_letter_source_queues(self, QueueUrl: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_queue_tags(self, QueueUrl: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_queues(self, QueueNamePrefix: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purge_queue(self, QueueUrl: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def receive_message(
        self,
        QueueUrl: str,
        AttributeNames: List[Any] = None,
        MessageAttributeNames: List[Any] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_permission(self, QueueUrl: str, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def send_message(
        self,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, Any] = None,
        MessageSystemAttributes: Dict[str, Any] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_message_batch(self, QueueUrl: str, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_queue_attributes(self, QueueUrl: str, Attributes: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_queue(self, QueueUrl: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_queue(self, QueueUrl: str, TagKeys: List[Any]) -> None:
        pass
