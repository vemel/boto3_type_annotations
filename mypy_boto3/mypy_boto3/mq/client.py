from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_broker(
        self,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        BrokerName: Optional[str] = None,
        Configuration: Optional[Dict] = None,
        CreatorRequestId: Optional[str] = None,
        DeploymentMode: Optional[str] = None,
        EncryptionOptions: Optional[Dict] = None,
        EngineType: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        HostInstanceType: Optional[str] = None,
        Logs: Optional[Dict] = None,
        MaintenanceWindowStartTime: Optional[Dict] = None,
        PubliclyAccessible: Optional[bool] = None,
        SecurityGroups: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        Tags: Optional[Dict] = None,
        Users: Optional[List] = None,
    ) -> Dict:
        pass


    def create_configuration(
        self,
        EngineType: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        Name: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        ResourceArn: str,
        Tags: Optional[Dict] = None,
    ):
        pass


    def create_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: Optional[bool] = None,
        Groups: Optional[List] = None,
        Password: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_broker(
        self,
        BrokerId: str,
    ) -> Dict:
        pass


    def delete_tags(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def delete_user(
        self,
        BrokerId: str,
        Username: str,
    ) -> Dict:
        pass


    def describe_broker(
        self,
        BrokerId: str,
    ) -> Dict:
        pass


    def describe_broker_engine_types(
        self,
        EngineType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_broker_instance_options(
        self,
        EngineType: Optional[str] = None,
        HostInstanceType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_configuration(
        self,
        ConfigurationId: str,
    ) -> Dict:
        pass


    def describe_configuration_revision(
        self,
        ConfigurationId: str,
        ConfigurationRevision: str,
    ) -> Dict:
        pass


    def describe_user(
        self,
        BrokerId: str,
        Username: str,
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


    def list_brokers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_configuration_revisions(
        self,
        ConfigurationId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_configurations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_users(
        self,
        BrokerId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def reboot_broker(
        self,
        BrokerId: str,
    ) -> Dict:
        pass


    def update_broker(
        self,
        BrokerId: str,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        Configuration: Optional[Dict] = None,
        EngineVersion: Optional[str] = None,
        HostInstanceType: Optional[str] = None,
        Logs: Optional[Dict] = None,
        SecurityGroups: Optional[List] = None,
    ) -> Dict:
        pass


    def update_configuration(
        self,
        ConfigurationId: str,
        Data: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: Optional[bool] = None,
        Groups: Optional[List] = None,
        Password: Optional[str] = None,
    ) -> Dict:
        pass

