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
    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_application_input(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Input: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_application_output(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Output: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_application(
        self,
        ApplicationName: str,
        RuntimeEnvironment: str,
        ServiceExecutionRole: str,
        ApplicationDescription: str = None,
        ApplicationConfiguration: Dict[str, Any] = None,
        CloudWatchLoggingOptions: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application(
        self, ApplicationName: str, CreateTimestamp: datetime
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOptionId: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application_snapshot(
        self,
        ApplicationName: str,
        SnapshotName: str,
        SnapshotCreationTimestamp: datetime,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_application(
        self, ApplicationName: str, IncludeAdditionalDetails: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def discover_input_schema(
        self,
        ServiceExecutionRole: str,
        ResourceARN: str = None,
        InputStartingPositionConfiguration: Dict[str, Any] = None,
        S3Configuration: Dict[str, Any] = None,
        InputProcessingConfiguration: Dict[str, Any] = None,
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
    def list_application_snapshots(
        self, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_applications(
        self, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_application(
        self, ApplicationName: str, RunConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_application(self, ApplicationName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceARN: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationConfigurationUpdate: Dict[str, Any] = None,
        ServiceExecutionRoleUpdate: str = None,
        RunConfigurationUpdate: Dict[str, Any] = None,
        CloudWatchLoggingOptionUpdates: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
