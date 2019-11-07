from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_backup(
        self,
        ServerName: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_server(
        self,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: Optional[bool] = None,
        CustomDomain: Optional[str] = None,
        CustomCertificate: Optional[str] = None,
        CustomPrivateKey: Optional[str] = None,
        DisableAutomatedBackup: Optional[bool] = None,
        Engine: Optional[str] = None,
        EngineModel: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        EngineAttributes: Optional[List] = None,
        BackupRetentionCount: Optional[int] = None,
        KeyPair: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        BackupId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_backup(
        self,
        BackupId: str,
    ) -> Dict:
        pass


    def delete_server(
        self,
        ServerName: str,
    ) -> Dict:
        pass


    def describe_account_attributes(
        self,
    ) -> Dict:
        pass


    def describe_backups(
        self,
        BackupId: Optional[str] = None,
        ServerName: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        ServerName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_node_association_status(
        self,
        NodeAssociationStatusToken: str,
        ServerName: str,
    ) -> Dict:
        pass


    def describe_servers(
        self,
        ServerName: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def disassociate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: Optional[List] = None,
    ) -> Dict:
        pass


    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: Optional[List] = None,
    ) -> Dict:
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def restore_server(
        self,
        BackupId: str,
        ServerName: str,
        InstanceType: Optional[str] = None,
        KeyPair: Optional[str] = None,
    ) -> Dict:
        pass


    def start_maintenance(
        self,
        ServerName: str,
        EngineAttributes: Optional[List] = None,
    ) -> Dict:
        pass


    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: Optional[bool] = None,
        BackupRetentionCount: Optional[int] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
    ) -> Dict:
        pass


    def update_server_engine_attributes(
        self,
        ServerName: str,
        AttributeName: str,
        AttributeValue: Optional[str] = None,
    ) -> Dict:
        pass

