from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.sns.service_resource as sns_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    platform_applications: sns_service_resource_scope.platform_applications
    subscriptions: sns_service_resource_scope.subscriptions
    topics: sns_service_resource_scope.topics

    # pylint: disable=arguments-differ
    def PlatformApplication(
        self, arn: str = None
    ) -> sns_service_resource_scope.PlatformApplication:
        pass

    # pylint: disable=arguments-differ
    def PlatformEndpoint(
        self, arn: str = None
    ) -> sns_service_resource_scope.PlatformEndpoint:
        pass

    # pylint: disable=arguments-differ
    def Subscription(self, arn: str = None) -> sns_service_resource_scope.Subscription:
        pass

    # pylint: disable=arguments-differ
    def Topic(self, arn: str = None) -> sns_service_resource_scope.Topic:
        pass

    # pylint: disable=arguments-differ
    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, Any]
    ) -> sns_service_resource_scope.PlatformApplication:
        pass

    # pylint: disable=arguments-differ
    def create_topic(
        self, Name: str, Attributes: Dict[str, Any] = None, Tags: List[Any] = None
    ) -> sns_service_resource_scope.Topic:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class PlatformApplication(Boto3ServiceResource):
    attributes: Dict
    arn: str
    endpoints: sns_service_resource_scope.endpoints

    # pylint: disable=arguments-differ
    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, Any] = None
    ) -> sns_service_resource_scope.PlatformEndpoint:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_attributes(self, Attributes: Dict[str, Any]) -> None:
        pass


class PlatformEndpoint(Boto3ServiceResource):
    attributes: Dict
    arn: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_attributes(self, Attributes: Dict[str, Any]) -> None:
        pass


class Subscription(Boto3ServiceResource):
    attributes: Dict
    arn: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass


class Topic(Boto3ServiceResource):
    attributes: Dict
    arn: str
    subscriptions: sns_service_resource_scope.subscriptions

    # pylint: disable=arguments-differ
    def add_permission(
        self, Label: str, AWSAccountId: List[Any], ActionName: List[Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> sns_service_resource_scope.Subscription:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_permission(self, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, Any] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> sns_service_resource_scope.Subscription:
        pass


class platform_applications(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sns_service_resource_scope.PlatformApplication]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, NextToken: str = None
    ) -> List[sns_service_resource_scope.PlatformApplication]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[sns_service_resource_scope.PlatformApplication]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[sns_service_resource_scope.PlatformApplication]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class subscriptions(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sns_service_resource_scope.Subscription]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, NextToken: str = None
    ) -> List[sns_service_resource_scope.Subscription]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[sns_service_resource_scope.Subscription]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[sns_service_resource_scope.Subscription]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class topics(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sns_service_resource_scope.Topic]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(cls, NextToken: str = None) -> List[sns_service_resource_scope.Topic]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[sns_service_resource_scope.Topic]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[sns_service_resource_scope.Topic]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class endpoints(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[sns_service_resource_scope.PlatformEndpoint]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, NextToken: str = None
    ) -> List[sns_service_resource_scope.PlatformEndpoint]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[sns_service_resource_scope.PlatformEndpoint]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[sns_service_resource_scope.PlatformEndpoint]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
