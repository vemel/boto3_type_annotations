from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_role_to_group(
        self,
        GroupId: str,
        RoleArn: str,
    ) -> Dict:
        pass


    def associate_service_role_to_account(
        self,
        RoleArn: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_connector_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Connectors: Optional[List] = None,
    ) -> Dict:
        pass


    def create_core_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_core_definition_version(
        self,
        CoreDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Cores: Optional[List] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        DeploymentType: str,
        GroupId: str,
        AmznClientToken: Optional[str] = None,
        DeploymentId: Optional[str] = None,
        GroupVersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_device_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Devices: Optional[List] = None,
    ) -> Dict:
        pass


    def create_function_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        DefaultConfig: Optional[Dict] = None,
        Functions: Optional[List] = None,
    ) -> Dict:
        pass


    def create_group(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_group_certificate_authority(
        self,
        GroupId: str,
        AmznClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: Optional[str] = None,
        ConnectorDefinitionVersionArn: Optional[str] = None,
        CoreDefinitionVersionArn: Optional[str] = None,
        DeviceDefinitionVersionArn: Optional[str] = None,
        FunctionDefinitionVersionArn: Optional[str] = None,
        LoggerDefinitionVersionArn: Optional[str] = None,
        ResourceDefinitionVersionArn: Optional[str] = None,
        SubscriptionDefinitionVersionArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_logger_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Loggers: Optional[List] = None,
    ) -> Dict:
        pass


    def create_resource_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Resources: Optional[List] = None,
    ) -> Dict:
        pass


    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: str,
        UpdateTargets: List,
        UpdateTargetsArchitecture: str,
        UpdateTargetsOperatingSystem: str,
        AmznClientToken: Optional[str] = None,
        UpdateAgentLogLevel: Optional[str] = None,
    ) -> Dict:
        pass


    def create_subscription_definition(
        self,
        AmznClientToken: Optional[str] = None,
        InitialVersion: Optional[Dict] = None,
        Name: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: Optional[str] = None,
        Subscriptions: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_connector_definition(
        self,
        ConnectorDefinitionId: str,
    ) -> Dict:
        pass


    def delete_core_definition(
        self,
        CoreDefinitionId: str,
    ) -> Dict:
        pass


    def delete_device_definition(
        self,
        DeviceDefinitionId: str,
    ) -> Dict:
        pass


    def delete_function_definition(
        self,
        FunctionDefinitionId: str,
    ) -> Dict:
        pass


    def delete_group(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def delete_logger_definition(
        self,
        LoggerDefinitionId: str,
    ) -> Dict:
        pass


    def delete_resource_definition(
        self,
        ResourceDefinitionId: str,
    ) -> Dict:
        pass


    def delete_subscription_definition(
        self,
        SubscriptionDefinitionId: str,
    ) -> Dict:
        pass


    def disassociate_role_from_group(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def disassociate_service_role_from_account(
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


    def get_associated_role(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def get_bulk_deployment_status(
        self,
        BulkDeploymentId: str,
    ) -> Dict:
        pass


    def get_connectivity_info(
        self,
        ThingName: str,
    ) -> Dict:
        pass


    def get_connector_definition(
        self,
        ConnectorDefinitionId: str,
    ) -> Dict:
        pass


    def get_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        ConnectorDefinitionVersionId: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_core_definition(
        self,
        CoreDefinitionId: str,
    ) -> Dict:
        pass


    def get_core_definition_version(
        self,
        CoreDefinitionId: str,
        CoreDefinitionVersionId: str,
    ) -> Dict:
        pass


    def get_deployment_status(
        self,
        DeploymentId: str,
        GroupId: str,
    ) -> Dict:
        pass


    def get_device_definition(
        self,
        DeviceDefinitionId: str,
    ) -> Dict:
        pass


    def get_device_definition_version(
        self,
        DeviceDefinitionId: str,
        DeviceDefinitionVersionId: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_function_definition(
        self,
        FunctionDefinitionId: str,
    ) -> Dict:
        pass


    def get_function_definition_version(
        self,
        FunctionDefinitionId: str,
        FunctionDefinitionVersionId: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_group(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def get_group_certificate_authority(
        self,
        CertificateAuthorityId: str,
        GroupId: str,
    ) -> Dict:
        pass


    def get_group_certificate_configuration(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def get_group_version(
        self,
        GroupId: str,
        GroupVersionId: str,
    ) -> Dict:
        pass


    def get_logger_definition(
        self,
        LoggerDefinitionId: str,
    ) -> Dict:
        pass


    def get_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        LoggerDefinitionVersionId: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_resource_definition(
        self,
        ResourceDefinitionId: str,
    ) -> Dict:
        pass


    def get_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        ResourceDefinitionVersionId: str,
    ) -> Dict:
        pass


    def get_service_role_for_account(
        self,
    ) -> Dict:
        pass


    def get_subscription_definition(
        self,
        SubscriptionDefinitionId: str,
    ) -> Dict:
        pass


    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_bulk_deployment_detailed_reports(
        self,
        BulkDeploymentId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_bulk_deployments(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_connector_definition_versions(
        self,
        ConnectorDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_connector_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_core_definition_versions(
        self,
        CoreDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_core_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_deployments(
        self,
        GroupId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_device_definition_versions(
        self,
        DeviceDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_device_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_function_definition_versions(
        self,
        FunctionDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_function_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_group_certificate_authorities(
        self,
        GroupId: str,
    ) -> Dict:
        pass


    def list_group_versions(
        self,
        GroupId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_groups(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_logger_definition_versions(
        self,
        LoggerDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_logger_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_definition_versions(
        self,
        ResourceDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resource_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_subscription_definition_versions(
        self,
        SubscriptionDefinitionId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_subscription_definitions(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def reset_deployments(
        self,
        GroupId: str,
        AmznClientToken: Optional[str] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def stop_bulk_deployment(
        self,
        BulkDeploymentId: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        tags: Optional[Dict] = None,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_connectivity_info(
        self,
        ThingName: str,
        ConnectivityInfo: Optional[List] = None,
    ) -> Dict:
        pass


    def update_connector_definition(
        self,
        ConnectorDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_core_definition(
        self,
        CoreDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_device_definition(
        self,
        DeviceDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_function_definition(
        self,
        FunctionDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_group(
        self,
        GroupId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_group_certificate_configuration(
        self,
        GroupId: str,
        CertificateExpiryInMilliseconds: Optional[str] = None,
    ) -> Dict:
        pass


    def update_logger_definition(
        self,
        LoggerDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_resource_definition(
        self,
        ResourceDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def update_subscription_definition(
        self,
        SubscriptionDefinitionId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass

