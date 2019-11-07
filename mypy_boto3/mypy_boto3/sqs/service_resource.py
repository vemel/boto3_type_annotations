from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    queues: 'queues'

    def Message(
        self,
        queue_url: Optional[str] = None,
        receipt_handle: Optional[str] = None,
    ) -> 'Message':
        pass


    def Queue(
        self,
        url: Optional[str] = None,
    ) -> 'Queue':
        pass


    def create_queue(
        self,
        QueueName: str,
        Attributes: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> 'Queue':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def get_queue_by_name(
        self,
        QueueName: str,
        QueueOwnerAWSAccountId: Optional[str] = None,
    ) -> 'Queue':
        pass



class Message(base.ServiceResource):
    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict
    md5_of_message_attributes: str
    message_attributes: Dict
    queue_url: str
    receipt_handle: str

    def change_visibility(
        self,
        VisibilityTimeout: int,
    ):
        pass


    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Queue(base.ServiceResource):
    attributes: Dict
    url: str
    dead_letter_source_queues: 'dead_letter_source_queues'

    def add_permission(
        self,
        Label: str,
        AWSAccountIds: List,
        Actions: List,
    ):
        pass


    def change_message_visibility_batch(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def delete(
        self,
    ):
        pass


    def delete_messages(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def purge(
        self,
    ):
        pass


    def receive_messages(
        self,
        AttributeNames: Optional[List] = None,
        MessageAttributeNames: Optional[List] = None,
        MaxNumberOfMessages: Optional[int] = None,
        VisibilityTimeout: Optional[int] = None,
        WaitTimeSeconds: Optional[int] = None,
        ReceiveRequestAttemptId: Optional[str] = None,
    ) -> List['Message']:
        pass


    def reload(
        self,
    ):
        pass


    def remove_permission(
        self,
        Label: str,
    ):
        pass


    def send_message(
        self,
        MessageBody: str,
        DelaySeconds: Optional[int] = None,
        MessageAttributes: Optional[Dict] = None,
        MessageSystemAttributes: Optional[Dict] = None,
        MessageDeduplicationId: Optional[str] = None,
        MessageGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def send_messages(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def set_attributes(
        self,
        Attributes: Dict,
    ):
        pass



class queues(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Queue']:
        pass


    @classmethod
    def filter(
        cls,
        QueueNamePrefix: Optional[str] = None,
    ) -> List['Queue']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Queue']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Queue']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

