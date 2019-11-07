from datetime import datetime
from typing import Dict
from typing import IO
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: Optional[str] = None,
        RevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def add_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: Optional[str] = None,
        SourceAccount: Optional[str] = None,
        EventSourceToken: Optional[str] = None,
        Qualifier: Optional[str] = None,
        RevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: Optional[str] = None,
        RoutingConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_event_source_mapping(
        self,
        EventSourceArn: str,
        FunctionName: str,
        Enabled: Optional[bool] = None,
        BatchSize: Optional[int] = None,
        MaximumBatchingWindowInSeconds: Optional[int] = None,
        StartingPosition: Optional[str] = None,
        StartingPositionTimestamp: Optional[datetime] = None,
    ) -> Dict:
        pass


    def create_function(
        self,
        FunctionName: str,
        Runtime: str,
        Role: str,
        Handler: str,
        Code: Dict,
        Description: Optional[str] = None,
        Timeout: Optional[int] = None,
        MemorySize: Optional[int] = None,
        Publish: Optional[bool] = None,
        VpcConfig: Optional[Dict] = None,
        DeadLetterConfig: Optional[Dict] = None,
        Environment: Optional[Dict] = None,
        KMSKeyArn: Optional[str] = None,
        TracingConfig: Optional[Dict] = None,
        Tags: Optional[Dict] = None,
        Layers: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_alias(
        self,
        FunctionName: str,
        Name: str,
    ):
        pass


    def delete_event_source_mapping(
        self,
        UUID: str,
    ) -> Dict:
        pass


    def delete_function(
        self,
        FunctionName: str,
        Qualifier: Optional[str] = None,
    ):
        pass


    def delete_function_concurrency(
        self,
        FunctionName: str,
    ):
        pass


    def delete_layer_version(
        self,
        LayerName: str,
        VersionNumber: int,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_account_settings(
        self,
    ) -> Dict:
        pass


    def get_alias(
        self,
        FunctionName: str,
        Name: str,
    ) -> Dict:
        pass


    def get_event_source_mapping(
        self,
        UUID: str,
    ) -> Dict:
        pass


    def get_function(
        self,
        FunctionName: str,
        Qualifier: Optional[str] = None,
    ) -> Dict:
        pass


    def get_function_configuration(
        self,
        FunctionName: str,
        Qualifier: Optional[str] = None,
    ) -> Dict:
        pass


    def get_layer_version(
        self,
        LayerName: str,
        VersionNumber: int,
    ) -> Dict:
        pass


    def get_layer_version_by_arn(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def get_layer_version_policy(
        self,
        LayerName: str,
        VersionNumber: int,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_policy(
        self,
        FunctionName: str,
        Qualifier: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def invoke(
        self,
        FunctionName: str,
        InvocationType: Optional[str] = None,
        LogType: Optional[str] = None,
        ClientContext: Optional[str] = None,
        Payload: Optional[Union[bytes, IO]] = None,
        Qualifier: Optional[str] = None,
    ) -> Dict:
        pass


    def invoke_async(
        self,
        FunctionName: str,
        InvokeArgs: Union[bytes, IO],
    ) -> Dict:
        pass


    def list_aliases(
        self,
        FunctionName: str,
        FunctionVersion: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_event_source_mappings(
        self,
        EventSourceArn: Optional[str] = None,
        FunctionName: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_functions(
        self,
        MasterRegion: Optional[str] = None,
        FunctionVersion: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_layer_versions(
        self,
        LayerName: str,
        CompatibleRuntime: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_layers(
        self,
        CompatibleRuntime: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        Resource: str,
    ) -> Dict:
        pass


    def list_versions_by_function(
        self,
        FunctionName: str,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def publish_layer_version(
        self,
        LayerName: str,
        Content: Dict,
        Description: Optional[str] = None,
        CompatibleRuntimes: Optional[List] = None,
        LicenseInfo: Optional[str] = None,
    ) -> Dict:
        pass


    def publish_version(
        self,
        FunctionName: str,
        CodeSha256: Optional[str] = None,
        Description: Optional[str] = None,
        RevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def put_function_concurrency(
        self,
        FunctionName: str,
        ReservedConcurrentExecutions: int,
    ) -> Dict:
        pass


    def remove_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        RevisionId: Optional[str] = None,
    ):
        pass


    def remove_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Qualifier: Optional[str] = None,
        RevisionId: Optional[str] = None,
    ):
        pass


    def tag_resource(
        self,
        Resource: str,
        Tags: Dict,
    ):
        pass


    def untag_resource(
        self,
        Resource: str,
        TagKeys: List,
    ):
        pass


    def update_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: Optional[str] = None,
        Description: Optional[str] = None,
        RoutingConfig: Optional[Dict] = None,
        RevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_event_source_mapping(
        self,
        UUID: str,
        FunctionName: Optional[str] = None,
        Enabled: Optional[bool] = None,
        BatchSize: Optional[int] = None,
        MaximumBatchingWindowInSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def update_function_code(
        self,
        FunctionName: str,
        ZipFile: Optional[bytes] = None,
        S3Bucket: Optional[str] = None,
        S3Key: Optional[str] = None,
        S3ObjectVersion: Optional[str] = None,
        Publish: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        RevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_function_configuration(
        self,
        FunctionName: str,
        Role: Optional[str] = None,
        Handler: Optional[str] = None,
        Description: Optional[str] = None,
        Timeout: Optional[int] = None,
        MemorySize: Optional[int] = None,
        VpcConfig: Optional[Dict] = None,
        Environment: Optional[Dict] = None,
        Runtime: Optional[str] = None,
        DeadLetterConfig: Optional[Dict] = None,
        KMSKeyArn: Optional[str] = None,
        TracingConfig: Optional[Dict] = None,
        RevisionId: Optional[str] = None,
        Layers: Optional[List] = None,
    ) -> Dict:
        pass

