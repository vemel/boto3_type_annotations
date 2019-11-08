from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_backup(self, ServerName: str, Description: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_server(
        self,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = None,
        CustomDomain: str = None,
        CustomCertificate: str = None,
        CustomPrivateKey: str = None,
        DisableAutomatedBackup: bool = None,
        Engine: str = None,
        EngineModel: str = None,
        EngineVersion: str = None,
        EngineAttributes: List[Any] = None,
        BackupRetentionCount: int = None,
        KeyPair: str = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
        SecurityGroupIds: List[Any] = None,
        SubnetIds: List[Any] = None,
        BackupId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_backup(self, BackupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_server(self, ServerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_attributes(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_backups(
        self,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_events(
        self, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_node_association_status(
        self, NodeAssociationStatusToken: str, ServerName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_servers(
        self, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List[Any] = None,
    ) -> Dict[str, Any]:
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
    def restore_server(
        self,
        BackupId: str,
        ServerName: str,
        InstanceType: str = None,
        KeyPair: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_maintenance(
        self, ServerName: str, EngineAttributes: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_server_engine_attributes(
        self, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> Dict[str, Any]:
        pass
