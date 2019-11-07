from datetime import datetime
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


    def create_app(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        roleName: Optional[str] = None,
        clientToken: Optional[str] = None,
        serverGroups: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_replication_job(
        self,
        serverId: str,
        seedReplicationTime: datetime,
        frequency: Optional[int] = None,
        runOnce: Optional[bool] = None,
        licenseType: Optional[str] = None,
        roleName: Optional[str] = None,
        description: Optional[str] = None,
        numberOfRecentAmisToKeep: Optional[int] = None,
        encrypted: Optional[bool] = None,
        kmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_app(
        self,
        appId: Optional[str] = None,
        forceStopAppReplication: Optional[bool] = None,
        forceTerminateApp: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_app_launch_configuration(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_app_replication_configuration(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_replication_job(
        self,
        replicationJobId: str,
    ) -> Dict:
        pass


    def delete_server_catalog(
        self,
    ) -> Dict:
        pass


    def disassociate_connector(
        self,
        connectorId: str,
    ) -> Dict:
        pass


    def generate_change_set(
        self,
        appId: Optional[str] = None,
        changesetFormat: Optional[str] = None,
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


    def generate_template(
        self,
        appId: Optional[str] = None,
        templateFormat: Optional[str] = None,
    ) -> Dict:
        pass


    def get_app(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_app_launch_configuration(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_app_replication_configuration(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_connectors(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_replication_jobs(
        self,
        replicationJobId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_replication_runs(
        self,
        replicationJobId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_servers(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        vmServerAddressList: Optional[List] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_server_catalog(
        self,
    ) -> Dict:
        pass


    def launch_app(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_apps(
        self,
        appIds: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_app_launch_configuration(
        self,
        appId: Optional[str] = None,
        roleName: Optional[str] = None,
        serverGroupLaunchConfigurations: Optional[List] = None,
    ) -> Dict:
        pass


    def put_app_replication_configuration(
        self,
        appId: Optional[str] = None,
        serverGroupReplicationConfigurations: Optional[List] = None,
    ) -> Dict:
        pass


    def start_app_replication(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def start_on_demand_replication_run(
        self,
        replicationJobId: str,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_app_replication(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def terminate_app(
        self,
        appId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_app(
        self,
        appId: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        roleName: Optional[str] = None,
        serverGroups: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def update_replication_job(
        self,
        replicationJobId: str,
        frequency: Optional[int] = None,
        nextReplicationRunStartTime: Optional[datetime] = None,
        licenseType: Optional[str] = None,
        roleName: Optional[str] = None,
        description: Optional[str] = None,
        numberOfRecentAmisToKeep: Optional[int] = None,
        encrypted: Optional[bool] = None,
        kmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass

