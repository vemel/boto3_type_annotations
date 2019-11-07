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


    def create_api(
        self,
        Name: str,
        ProtocolType: str,
        RouteSelectionExpression: str,
        ApiKeySelectionExpression: Optional[str] = None,
        Description: Optional[str] = None,
        DisableSchemaValidation: Optional[bool] = None,
        Version: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_api_mapping(
        self,
        ApiId: str,
        DomainName: str,
        Stage: str,
        ApiMappingKey: Optional[str] = None,
    ) -> Dict:
        pass


    def create_authorizer(
        self,
        ApiId: str,
        AuthorizerType: str,
        AuthorizerUri: str,
        IdentitySource: List,
        Name: str,
        AuthorizerCredentialsArn: Optional[str] = None,
        AuthorizerResultTtlInSeconds: Optional[int] = None,
        IdentityValidationExpression: Optional[str] = None,
        ProviderArns: Optional[List] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        ApiId: str,
        Description: Optional[str] = None,
        StageName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: Optional[List] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_integration(
        self,
        ApiId: str,
        IntegrationType: str,
        ConnectionId: Optional[str] = None,
        ConnectionType: Optional[str] = None,
        ContentHandlingStrategy: Optional[str] = None,
        CredentialsArn: Optional[str] = None,
        Description: Optional[str] = None,
        IntegrationMethod: Optional[str] = None,
        IntegrationUri: Optional[str] = None,
        PassthroughBehavior: Optional[str] = None,
        RequestParameters: Optional[Dict] = None,
        RequestTemplates: Optional[Dict] = None,
        TemplateSelectionExpression: Optional[str] = None,
        TimeoutInMillis: Optional[int] = None,
    ) -> Dict:
        pass


    def create_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: Optional[str] = None,
        ResponseParameters: Optional[Dict] = None,
        ResponseTemplates: Optional[Dict] = None,
        TemplateSelectionExpression: Optional[str] = None,
    ) -> Dict:
        pass


    def create_model(
        self,
        ApiId: str,
        Name: str,
        Schema: str,
        ContentType: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_route(
        self,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: Optional[bool] = None,
        AuthorizationScopes: Optional[List] = None,
        AuthorizationType: Optional[str] = None,
        AuthorizerId: Optional[str] = None,
        ModelSelectionExpression: Optional[str] = None,
        OperationName: Optional[str] = None,
        RequestModels: Optional[Dict] = None,
        RequestParameters: Optional[Dict] = None,
        RouteResponseSelectionExpression: Optional[str] = None,
        Target: Optional[str] = None,
    ) -> Dict:
        pass


    def create_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        ModelSelectionExpression: Optional[str] = None,
        ResponseModels: Optional[Dict] = None,
        ResponseParameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: Optional[Dict] = None,
        ClientCertificateId: Optional[str] = None,
        DefaultRouteSettings: Optional[Dict] = None,
        DeploymentId: Optional[str] = None,
        Description: Optional[str] = None,
        RouteSettings: Optional[Dict] = None,
        StageVariables: Optional[Dict] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_api(
        self,
        ApiId: str,
    ):
        pass


    def delete_api_mapping(
        self,
        ApiMappingId: str,
        DomainName: str,
    ):
        pass


    def delete_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
    ):
        pass


    def delete_deployment(
        self,
        ApiId: str,
        DeploymentId: str,
    ):
        pass


    def delete_domain_name(
        self,
        DomainName: str,
    ):
        pass


    def delete_integration(
        self,
        ApiId: str,
        IntegrationId: str,
    ):
        pass


    def delete_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
    ):
        pass


    def delete_model(
        self,
        ApiId: str,
        ModelId: str,
    ):
        pass


    def delete_route(
        self,
        ApiId: str,
        RouteId: str,
    ):
        pass


    def delete_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
    ):
        pass


    def delete_stage(
        self,
        ApiId: str,
        StageName: str,
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


    def get_api(
        self,
        ApiId: str,
    ) -> Dict:
        pass


    def get_api_mapping(
        self,
        ApiMappingId: str,
        DomainName: str,
    ) -> Dict:
        pass


    def get_api_mappings(
        self,
        DomainName: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_apis(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
    ) -> Dict:
        pass


    def get_authorizers(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_deployment(
        self,
        ApiId: str,
        DeploymentId: str,
    ) -> Dict:
        pass


    def get_deployments(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_domain_name(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def get_domain_names(
        self,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_integration(
        self,
        ApiId: str,
        IntegrationId: str,
    ) -> Dict:
        pass


    def get_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
    ) -> Dict:
        pass


    def get_integration_responses(
        self,
        ApiId: str,
        IntegrationId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_integrations(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_model(
        self,
        ApiId: str,
        ModelId: str,
    ) -> Dict:
        pass


    def get_model_template(
        self,
        ApiId: str,
        ModelId: str,
    ) -> Dict:
        pass


    def get_models(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_route(
        self,
        ApiId: str,
        RouteId: str,
    ) -> Dict:
        pass


    def get_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
    ) -> Dict:
        pass


    def get_route_responses(
        self,
        ApiId: str,
        RouteId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_routes(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_stage(
        self,
        ApiId: str,
        StageName: str,
    ) -> Dict:
        pass


    def get_stages(
        self,
        ApiId: str,
        MaxResults: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_tags(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_api(
        self,
        ApiId: str,
        ApiKeySelectionExpression: Optional[str] = None,
        Description: Optional[str] = None,
        DisableSchemaValidation: Optional[bool] = None,
        Name: Optional[str] = None,
        RouteSelectionExpression: Optional[str] = None,
        Version: Optional[str] = None,
    ) -> Dict:
        pass


    def update_api_mapping(
        self,
        ApiId: str,
        ApiMappingId: str,
        DomainName: str,
        ApiMappingKey: Optional[str] = None,
        Stage: Optional[str] = None,
    ) -> Dict:
        pass


    def update_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
        AuthorizerCredentialsArn: Optional[str] = None,
        AuthorizerResultTtlInSeconds: Optional[int] = None,
        AuthorizerType: Optional[str] = None,
        AuthorizerUri: Optional[str] = None,
        IdentitySource: Optional[List] = None,
        IdentityValidationExpression: Optional[str] = None,
        Name: Optional[str] = None,
        ProviderArns: Optional[List] = None,
    ) -> Dict:
        pass


    def update_deployment(
        self,
        ApiId: str,
        DeploymentId: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_integration(
        self,
        ApiId: str,
        IntegrationId: str,
        ConnectionId: Optional[str] = None,
        ConnectionType: Optional[str] = None,
        ContentHandlingStrategy: Optional[str] = None,
        CredentialsArn: Optional[str] = None,
        Description: Optional[str] = None,
        IntegrationMethod: Optional[str] = None,
        IntegrationType: Optional[str] = None,
        IntegrationUri: Optional[str] = None,
        PassthroughBehavior: Optional[str] = None,
        RequestParameters: Optional[Dict] = None,
        RequestTemplates: Optional[Dict] = None,
        TemplateSelectionExpression: Optional[str] = None,
        TimeoutInMillis: Optional[int] = None,
    ) -> Dict:
        pass


    def update_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
        ContentHandlingStrategy: Optional[str] = None,
        IntegrationResponseKey: Optional[str] = None,
        ResponseParameters: Optional[Dict] = None,
        ResponseTemplates: Optional[Dict] = None,
        TemplateSelectionExpression: Optional[str] = None,
    ) -> Dict:
        pass


    def update_model(
        self,
        ApiId: str,
        ModelId: str,
        ContentType: Optional[str] = None,
        Description: Optional[str] = None,
        Name: Optional[str] = None,
        Schema: Optional[str] = None,
    ) -> Dict:
        pass


    def update_route(
        self,
        ApiId: str,
        RouteId: str,
        ApiKeyRequired: Optional[bool] = None,
        AuthorizationScopes: Optional[List] = None,
        AuthorizationType: Optional[str] = None,
        AuthorizerId: Optional[str] = None,
        ModelSelectionExpression: Optional[str] = None,
        OperationName: Optional[str] = None,
        RequestModels: Optional[Dict] = None,
        RequestParameters: Optional[Dict] = None,
        RouteKey: Optional[str] = None,
        RouteResponseSelectionExpression: Optional[str] = None,
        Target: Optional[str] = None,
    ) -> Dict:
        pass


    def update_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
        ModelSelectionExpression: Optional[str] = None,
        ResponseModels: Optional[Dict] = None,
        ResponseParameters: Optional[Dict] = None,
        RouteResponseKey: Optional[str] = None,
    ) -> Dict:
        pass


    def update_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: Optional[Dict] = None,
        ClientCertificateId: Optional[str] = None,
        DefaultRouteSettings: Optional[Dict] = None,
        DeploymentId: Optional[str] = None,
        Description: Optional[str] = None,
        RouteSettings: Optional[Dict] = None,
        StageVariables: Optional[Dict] = None,
    ) -> Dict:
        pass

