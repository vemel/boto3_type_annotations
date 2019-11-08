from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_broker(
        self,
        AutoMinorVersionUpgrade: bool = None,
        BrokerName: str = None,
        Configuration: Dict[str, Any] = None,
        CreatorRequestId: str = None,
        DeploymentMode: str = None,
        EncryptionOptions: Dict[str, Any] = None,
        EngineType: str = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: Dict[str, Any] = None,
        MaintenanceWindowStartTime: Dict[str, Any] = None,
        PubliclyAccessible: bool = None,
        SecurityGroups: List[Any] = None,
        SubnetIds: List[Any] = None,
        Tags: Dict[str, Any] = None,
        Users: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_configuration(
        self,
        EngineType: str = None,
        EngineVersion: str = None,
        Name: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(self, ResourceArn: str, Tags: Dict[str, Any] = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[Any] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_broker(self, BrokerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_user(self, BrokerId: str, Username: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_broker(self, BrokerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_broker_engine_types(
        self, EngineType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_broker_instance_options(
        self,
        EngineType: str = None,
        HostInstanceType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configuration(self, ConfigurationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configuration_revision(
        self, ConfigurationId: str, ConfigurationRevision: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user(self, BrokerId: str, Username: str) -> Dict[str, Any]:
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
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_brokers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_configuration_revisions(
        self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_users(
        self, BrokerId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_broker(self, BrokerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_broker(
        self,
        BrokerId: str,
        AutoMinorVersionUpgrade: bool = None,
        Configuration: Dict[str, Any] = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: Dict[str, Any] = None,
        SecurityGroups: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_configuration(
        self, ConfigurationId: str, Data: str = None, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[Any] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        pass
