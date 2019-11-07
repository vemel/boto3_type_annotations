from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_configuration_items_to_application(
        self,
        applicationConfigurationId: str,
        configurationIds: List,
    ) -> Dict:
        pass


    def batch_delete_import_data(
        self,
        importTaskIds: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_application(
        self,
        name: str,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        configurationIds: List,
        tags: List,
    ) -> Dict:
        pass


    def delete_applications(
        self,
        configurationIds: List,
    ) -> Dict:
        pass


    def delete_tags(
        self,
        configurationIds: List,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_agents(
        self,
        agentIds: Optional[List] = None,
        filters: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_configurations(
        self,
        configurationIds: List,
    ) -> Dict:
        pass


    def describe_continuous_exports(
        self,
        exportIds: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_export_configurations(
        self,
        exportIds: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_export_tasks(
        self,
        exportIds: Optional[List] = None,
        filters: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_import_tasks(
        self,
        filters: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        filters: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_configuration_items_from_application(
        self,
        applicationConfigurationId: str,
        configurationIds: List,
    ) -> Dict:
        pass


    def export_configurations(
        self,
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


    def get_discovery_summary(
        self,
    ) -> Dict:
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


    def list_configurations(
        self,
        configurationType: str,
        filters: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        orderBy: Optional[List] = None,
    ) -> Dict:
        pass


    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: Optional[bool] = None,
        neighborConfigurationIds: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_continuous_export(
        self,
    ) -> Dict:
        pass


    def start_data_collection_by_agent_ids(
        self,
        agentIds: List,
    ) -> Dict:
        pass


    def start_export_task(
        self,
        exportDataFormat: Optional[List] = None,
        filters: Optional[List] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def start_import_task(
        self,
        name: str,
        importUrl: str,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_continuous_export(
        self,
        exportId: str,
    ) -> Dict:
        pass


    def stop_data_collection_by_agent_ids(
        self,
        agentIds: List,
    ) -> Dict:
        pass


    def update_application(
        self,
        configurationId: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict:
        pass

