from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Union

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str = None,
        RevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str = None,
        SourceAccount: str = None,
        EventSourceToken: str = None,
        Qualifier: str = None,
        RevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str = None,
        RoutingConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_event_source_mapping(
        self,
        EventSourceArn: str,
        FunctionName: str,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        StartingPosition: str = None,
        StartingPositionTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_function(
        self,
        FunctionName: str,
        Runtime: str,
        Role: str,
        Handler: str,
        Code: Dict[str, Any],
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        Publish: bool = None,
        VpcConfig: Dict[str, Any] = None,
        DeadLetterConfig: Dict[str, Any] = None,
        Environment: Dict[str, Any] = None,
        KMSKeyArn: str = None,
        TracingConfig: Dict[str, Any] = None,
        Tags: Dict[str, Any] = None,
        Layers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_alias(self, FunctionName: str, Name: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_event_source_mapping(self, UUID: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_function(self, FunctionName: str, Qualifier: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_function_concurrency(self, FunctionName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_layer_version(self, LayerName: str, VersionNumber: int) -> None:
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
    def get_account_settings(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_alias(self, FunctionName: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_event_source_mapping(self, UUID: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_function(self, FunctionName: str, Qualifier: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_function_configuration(
        self, FunctionName: str, Qualifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_layer_version(self, LayerName: str, VersionNumber: int) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_layer_version_by_arn(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_layer_version_policy(
        self, LayerName: str, VersionNumber: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_policy(self, FunctionName: str, Qualifier: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def invoke(
        self,
        FunctionName: str,
        InvocationType: str = None,
        LogType: str = None,
        ClientContext: str = None,
        Payload: Union[bytes, IO] = None,
        Qualifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def invoke_async(
        self, FunctionName: str, InvokeArgs: Union[bytes, IO]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_aliases(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_event_source_mappings(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_functions(
        self,
        MasterRegion: str = None,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_layer_versions(
        self,
        LayerName: str,
        CompatibleRuntime: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_layers(
        self, CompatibleRuntime: str = None, Marker: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(self, Resource: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_versions_by_function(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def publish_layer_version(
        self,
        LayerName: str,
        Content: Dict[str, Any],
        Description: str = None,
        CompatibleRuntimes: List[Any] = None,
        LicenseInfo: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def publish_version(
        self,
        FunctionName: str,
        CodeSha256: str = None,
        Description: str = None,
        RevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_function_concurrency(
        self, FunctionName: str, ReservedConcurrentExecutions: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        RevisionId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Qualifier: str = None,
        RevisionId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Resource: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Resource: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str = None,
        Description: str = None,
        RoutingConfig: Dict[str, Any] = None,
        RevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_event_source_mapping(
        self,
        UUID: str,
        FunctionName: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_function_code(
        self,
        FunctionName: str,
        ZipFile: bytes = None,
        S3Bucket: str = None,
        S3Key: str = None,
        S3ObjectVersion: str = None,
        Publish: bool = None,
        DryRun: bool = None,
        RevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_function_configuration(
        self,
        FunctionName: str,
        Role: str = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        VpcConfig: Dict[str, Any] = None,
        Environment: Dict[str, Any] = None,
        Runtime: str = None,
        DeadLetterConfig: Dict[str, Any] = None,
        KMSKeyArn: str = None,
        TracingConfig: Dict[str, Any] = None,
        RevisionId: str = None,
        Layers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
