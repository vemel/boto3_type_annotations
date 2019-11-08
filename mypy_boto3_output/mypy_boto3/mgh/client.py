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
    def associate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifact: Dict[str, Any],
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        DiscoveredResource: Dict[str, Any],
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_progress_update_stream(
        self, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_application_state(self, ApplicationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_created_artifact(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifactName: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_discovered_resource(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ConfigurationId: str,
        DryRun: bool = None,
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
    def import_migration_task(
        self, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_created_artifacts(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_discovered_resources(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_migration_tasks(
        self, NextToken: str = None, MaxResults: int = None, ResourceName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_progress_update_streams(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def notify_application_state(
        self, ApplicationId: str, Status: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def notify_migration_task_state(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        Task: Dict[str, Any],
        UpdateDateTime: datetime,
        NextUpdateSeconds: int,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_resource_attributes(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ResourceAttributeList: List[Any],
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass
