from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_configuration_items_to_application(
        self, applicationConfigurationId: str, configurationIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_import_data(self, importTaskIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_application(self, name: str, description: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, configurationIds: List[Any], tags: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_applications(self, configurationIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(
        self, configurationIds: List[Any], tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_agents(
        self,
        agentIds: List[Any] = None,
        filters: List[Any] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_configurations(self, configurationIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_continuous_exports(
        self, exportIds: List[Any] = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_export_configurations(
        self, exportIds: List[Any] = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_export_tasks(
        self,
        exportIds: List[Any] = None,
        filters: List[Any] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_import_tasks(
        self, filters: List[Any] = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(
        self, filters: List[Any] = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_configuration_items_from_application(
        self, applicationConfigurationId: str, configurationIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_configurations(self) -> Dict[str, Any]:
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
    def get_discovery_summary(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_configurations(
        self,
        configurationType: str,
        filters: List[Any] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[Any] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_continuous_export(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_data_collection_by_agent_ids(self, agentIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_export_task(
        self,
        exportDataFormat: List[Any] = None,
        filters: List[Any] = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_import_task(
        self, name: str, importUrl: str, clientRequestToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_continuous_export(self, exportId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_data_collection_by_agent_ids(self, agentIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application(
        self, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        pass
