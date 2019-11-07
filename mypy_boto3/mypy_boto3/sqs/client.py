from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_permission(
        self,
        QueueUrl: str,
        Label: str,
        AWSAccountIds: List,
        Actions: List,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def change_message_visibility(
        self,
        QueueUrl: str,
        ReceiptHandle: str,
        VisibilityTimeout: int,
    ):
        pass


    def change_message_visibility_batch(
        self,
        QueueUrl: str,
        Entries: List,
    ) -> Dict:
        pass


    def create_queue(
        self,
        QueueName: str,
        Attributes: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_message(
        self,
        QueueUrl: str,
        ReceiptHandle: str,
    ):
        pass


    def delete_message_batch(
        self,
        QueueUrl: str,
        Entries: List,
    ) -> Dict:
        pass


    def delete_queue(
        self,
        QueueUrl: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_queue_attributes(
        self,
        QueueUrl: str,
        AttributeNames: Optional[List] = None,
    ) -> Dict:
        pass


    def get_queue_url(
        self,
        QueueName: str,
        QueueOwnerAWSAccountId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_dead_letter_source_queues(
        self,
        QueueUrl: str,
    ) -> Dict:
        pass


    def list_queue_tags(
        self,
        QueueUrl: str,
    ) -> Dict:
        pass


    def list_queues(
        self,
        QueueNamePrefix: Optional[str] = None,
    ) -> Dict:
        pass


    def purge_queue(
        self,
        QueueUrl: str,
    ):
        pass


    def receive_message(
        self,
        QueueUrl: str,
        AttributeNames: Optional[List] = None,
        MessageAttributeNames: Optional[List] = None,
        MaxNumberOfMessages: Optional[int] = None,
        VisibilityTimeout: Optional[int] = None,
        WaitTimeSeconds: Optional[int] = None,
        ReceiveRequestAttemptId: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_permission(
        self,
        QueueUrl: str,
        Label: str,
    ):
        pass


    def send_message(
        self,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: Optional[int] = None,
        MessageAttributes: Optional[Dict] = None,
        MessageSystemAttributes: Optional[Dict] = None,
        MessageDeduplicationId: Optional[str] = None,
        MessageGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def send_message_batch(
        self,
        QueueUrl: str,
        Entries: List,
    ) -> Dict:
        pass


    def set_queue_attributes(
        self,
        QueueUrl: str,
        Attributes: Dict,
    ):
        pass


    def tag_queue(
        self,
        QueueUrl: str,
        Tags: Dict,
    ):
        pass


    def untag_queue(
        self,
        QueueUrl: str,
        TagKeys: List,
    ):
        pass

