from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_api(
        self,
        Name: str,
        ProtocolType: str,
        RouteSelectionExpression: str,
        ApiKeySelectionExpression: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        Version: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_api_mapping(
        self, ApiId: str, DomainName: str, Stage: str, ApiMappingKey: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_authorizer(
        self,
        ApiId: str,
        AuthorizerType: str,
        AuthorizerUri: str,
        IdentitySource: List[Any],
        Name: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        IdentityValidationExpression: str = None,
        ProviderArns: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_deployment(
        self, ApiId: str, Description: str = None, StageName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: List[Any] = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_integration(
        self,
        ApiId: str,
        IntegrationType: str,
        ConnectionId: str = None,
        ConnectionType: str = None,
        ContentHandlingStrategy: str = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationUri: str = None,
        PassthroughBehavior: str = None,
        RequestParameters: Dict[str, Any] = None,
        RequestTemplates: Dict[str, Any] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: str = None,
        ResponseParameters: Dict[str, Any] = None,
        ResponseTemplates: Dict[str, Any] = None,
        TemplateSelectionExpression: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_model(
        self,
        ApiId: str,
        Name: str,
        Schema: str,
        ContentType: str = None,
        Description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_route(
        self,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[Any] = None,
        AuthorizationType: str = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, Any] = None,
        RequestParameters: Dict[str, Any] = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, Any] = None,
        ResponseParameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: Dict[str, Any] = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: Dict[str, Any] = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, Any] = None,
        StageVariables: Dict[str, Any] = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_api(self, ApiId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_api_mapping(self, ApiMappingId: str, DomainName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_authorizer(self, ApiId: str, AuthorizerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_deployment(self, ApiId: str, DeploymentId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_domain_name(self, DomainName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_integration(self, ApiId: str, IntegrationId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_model(self, ApiId: str, ModelId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_route(self, ApiId: str, RouteId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_route_response(
        self, ApiId: str, RouteId: str, RouteResponseId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_stage(self, ApiId: str, StageName: str) -> None:
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
    def get_api(self, ApiId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_api_mapping(self, ApiMappingId: str, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_api_mappings(
        self, DomainName: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_apis(self, MaxResults: str = None, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_authorizer(self, ApiId: str, AuthorizerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_authorizers(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_deployment(self, ApiId: str, DeploymentId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_deployments(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_name(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_names(
        self, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integration(self, ApiId: str, IntegrationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integration_responses(
        self,
        ApiId: str,
        IntegrationId: str,
        MaxResults: str = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integrations(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_model(self, ApiId: str, ModelId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_model_template(self, ApiId: str, ModelId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_models(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_route(self, ApiId: str, RouteId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_route_response(
        self, ApiId: str, RouteId: str, RouteResponseId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_route_responses(
        self, ApiId: str, RouteId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_routes(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_stage(self, ApiId: str, StageName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_stages(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tags(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(
        self, ResourceArn: str, Tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_api(
        self,
        ApiId: str,
        ApiKeySelectionExpression: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        Name: str = None,
        RouteSelectionExpression: str = None,
        Version: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_api_mapping(
        self,
        ApiId: str,
        ApiMappingId: str,
        DomainName: str,
        ApiMappingKey: str = None,
        Stage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        AuthorizerType: str = None,
        AuthorizerUri: str = None,
        IdentitySource: List[Any] = None,
        IdentityValidationExpression: str = None,
        Name: str = None,
        ProviderArns: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_deployment(
        self, ApiId: str, DeploymentId: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_name(
        self, DomainName: str, DomainNameConfigurations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_integration(
        self,
        ApiId: str,
        IntegrationId: str,
        ConnectionId: str = None,
        ConnectionType: str = None,
        ContentHandlingStrategy: str = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationType: str = None,
        IntegrationUri: str = None,
        PassthroughBehavior: str = None,
        RequestParameters: Dict[str, Any] = None,
        RequestTemplates: Dict[str, Any] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
        ContentHandlingStrategy: str = None,
        IntegrationResponseKey: str = None,
        ResponseParameters: Dict[str, Any] = None,
        ResponseTemplates: Dict[str, Any] = None,
        TemplateSelectionExpression: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_model(
        self,
        ApiId: str,
        ModelId: str,
        ContentType: str = None,
        Description: str = None,
        Name: str = None,
        Schema: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_route(
        self,
        ApiId: str,
        RouteId: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[Any] = None,
        AuthorizationType: str = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, Any] = None,
        RequestParameters: Dict[str, Any] = None,
        RouteKey: str = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, Any] = None,
        ResponseParameters: Dict[str, Any] = None,
        RouteResponseKey: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: Dict[str, Any] = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: Dict[str, Any] = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, Any] = None,
        StageVariables: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
