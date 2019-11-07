from typing import Dict
from typing import IO
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


    def create_api_key(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        generateDistinctId: Optional[bool] = None,
        value: Optional[str] = None,
        stageKeys: Optional[List] = None,
        customerId: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_authorizer(
        self,
        restApiId: str,
        name: str,
        type: str,
        providerARNs: Optional[List] = None,
        authType: Optional[str] = None,
        authorizerUri: Optional[str] = None,
        authorizerCredentials: Optional[str] = None,
        identitySource: Optional[str] = None,
        identityValidationExpression: Optional[str] = None,
        authorizerResultTtlInSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def create_base_path_mapping(
        self,
        domainName: str,
        restApiId: str,
        basePath: Optional[str] = None,
        stage: Optional[str] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        restApiId: str,
        stageName: Optional[str] = None,
        stageDescription: Optional[str] = None,
        description: Optional[str] = None,
        cacheClusterEnabled: Optional[bool] = None,
        cacheClusterSize: Optional[str] = None,
        variables: Optional[Dict] = None,
        canarySettings: Optional[Dict] = None,
        tracingEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_documentation_part(
        self,
        restApiId: str,
        location: Dict,
        properties: str,
    ) -> Dict:
        pass


    def create_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        stageName: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_domain_name(
        self,
        domainName: str,
        certificateName: Optional[str] = None,
        certificateBody: Optional[str] = None,
        certificatePrivateKey: Optional[str] = None,
        certificateChain: Optional[str] = None,
        certificateArn: Optional[str] = None,
        regionalCertificateName: Optional[str] = None,
        regionalCertificateArn: Optional[str] = None,
        endpointConfiguration: Optional[Dict] = None,
        tags: Optional[Dict] = None,
        securityPolicy: Optional[str] = None,
    ) -> Dict:
        pass


    def create_model(
        self,
        restApiId: str,
        name: str,
        contentType: str,
        description: Optional[str] = None,
        schema: Optional[str] = None,
    ) -> Dict:
        pass


    def create_request_validator(
        self,
        restApiId: str,
        name: Optional[str] = None,
        validateRequestBody: Optional[bool] = None,
        validateRequestParameters: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_resource(
        self,
        restApiId: str,
        parentId: str,
        pathPart: str,
    ) -> Dict:
        pass


    def create_rest_api(
        self,
        name: str,
        description: Optional[str] = None,
        version: Optional[str] = None,
        cloneFrom: Optional[str] = None,
        binaryMediaTypes: Optional[List] = None,
        minimumCompressionSize: Optional[int] = None,
        apiKeySource: Optional[str] = None,
        endpointConfiguration: Optional[Dict] = None,
        policy: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_stage(
        self,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: Optional[str] = None,
        cacheClusterEnabled: Optional[bool] = None,
        cacheClusterSize: Optional[str] = None,
        variables: Optional[Dict] = None,
        documentationVersion: Optional[str] = None,
        canarySettings: Optional[Dict] = None,
        tracingEnabled: Optional[bool] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_usage_plan(
        self,
        name: str,
        description: Optional[str] = None,
        apiStages: Optional[List] = None,
        throttle: Optional[Dict] = None,
        quota: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_usage_plan_key(
        self,
        usagePlanId: str,
        keyId: str,
        keyType: str,
    ) -> Dict:
        pass


    def create_vpc_link(
        self,
        name: str,
        targetArns: List,
        description: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_api_key(
        self,
        apiKey: str,
    ):
        pass


    def delete_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
    ):
        pass


    def delete_base_path_mapping(
        self,
        domainName: str,
        basePath: str,
    ):
        pass


    def delete_client_certificate(
        self,
        clientCertificateId: str,
    ):
        pass


    def delete_deployment(
        self,
        restApiId: str,
        deploymentId: str,
    ):
        pass


    def delete_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
    ):
        pass


    def delete_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
    ):
        pass


    def delete_domain_name(
        self,
        domainName: str,
    ):
        pass


    def delete_gateway_response(
        self,
        restApiId: str,
        responseType: str,
    ):
        pass


    def delete_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ):
        pass


    def delete_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ):
        pass


    def delete_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ):
        pass


    def delete_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ):
        pass


    def delete_model(
        self,
        restApiId: str,
        modelName: str,
    ):
        pass


    def delete_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
    ):
        pass


    def delete_resource(
        self,
        restApiId: str,
        resourceId: str,
    ):
        pass


    def delete_rest_api(
        self,
        restApiId: str,
    ):
        pass


    def delete_stage(
        self,
        restApiId: str,
        stageName: str,
    ):
        pass


    def delete_usage_plan(
        self,
        usagePlanId: str,
    ):
        pass


    def delete_usage_plan_key(
        self,
        usagePlanId: str,
        keyId: str,
    ):
        pass


    def delete_vpc_link(
        self,
        vpcLinkId: str,
    ):
        pass


    def flush_stage_authorizers_cache(
        self,
        restApiId: str,
        stageName: str,
    ):
        pass


    def flush_stage_cache(
        self,
        restApiId: str,
        stageName: str,
    ):
        pass


    def generate_client_certificate(
        self,
        description: Optional[str] = None,
        tags: Optional[Dict] = None,
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


    def get_account(
        self,
    ) -> Dict:
        pass


    def get_api_key(
        self,
        apiKey: str,
        includeValue: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_api_keys(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
        nameQuery: Optional[str] = None,
        customerId: Optional[str] = None,
        includeValues: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
    ) -> Dict:
        pass


    def get_authorizers(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_base_path_mapping(
        self,
        domainName: str,
        basePath: str,
    ) -> Dict:
        pass


    def get_base_path_mappings(
        self,
        domainName: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_client_certificate(
        self,
        clientCertificateId: str,
    ) -> Dict:
        pass


    def get_client_certificates(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_deployment(
        self,
        restApiId: str,
        deploymentId: str,
        embed: Optional[List] = None,
    ) -> Dict:
        pass


    def get_deployments(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
    ) -> Dict:
        pass


    def get_documentation_parts(
        self,
        restApiId: str,
        type: Optional[str] = None,
        nameQuery: Optional[str] = None,
        path: Optional[str] = None,
        position: Optional[str] = None,
        limit: Optional[int] = None,
        locationStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def get_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
    ) -> Dict:
        pass


    def get_documentation_versions(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_domain_name(
        self,
        domainName: str,
    ) -> Dict:
        pass


    def get_domain_names(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_export(
        self,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Optional[Dict] = None,
        accepts: Optional[str] = None,
    ) -> Dict:
        pass


    def get_gateway_response(
        self,
        restApiId: str,
        responseType: str,
    ) -> Dict:
        pass


    def get_gateway_responses(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> Dict:
        pass


    def get_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> Dict:
        pass


    def get_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
    ) -> Dict:
        pass


    def get_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
    ) -> Dict:
        pass


    def get_model(
        self,
        restApiId: str,
        modelName: str,
        flatten: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_model_template(
        self,
        restApiId: str,
        modelName: str,
    ) -> Dict:
        pass


    def get_models(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
    ) -> Dict:
        pass


    def get_request_validators(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_resource(
        self,
        restApiId: str,
        resourceId: str,
        embed: Optional[List] = None,
    ) -> Dict:
        pass


    def get_resources(
        self,
        restApiId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
        embed: Optional[List] = None,
    ) -> Dict:
        pass


    def get_rest_api(
        self,
        restApiId: str,
    ) -> Dict:
        pass


    def get_rest_apis(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_sdk(
        self,
        restApiId: str,
        stageName: str,
        sdkType: str,
        parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_sdk_type(
        self,
        id: str,
    ) -> Dict:
        pass


    def get_sdk_types(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_stage(
        self,
        restApiId: str,
        stageName: str,
    ) -> Dict:
        pass


    def get_stages(
        self,
        restApiId: str,
        deploymentId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_tags(
        self,
        resourceArn: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_usage(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: Optional[str] = None,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_usage_plan(
        self,
        usagePlanId: str,
    ) -> Dict:
        pass


    def get_usage_plan_key(
        self,
        usagePlanId: str,
        keyId: str,
    ) -> Dict:
        pass


    def get_usage_plan_keys(
        self,
        usagePlanId: str,
        position: Optional[str] = None,
        limit: Optional[int] = None,
        nameQuery: Optional[str] = None,
    ) -> Dict:
        pass


    def get_usage_plans(
        self,
        position: Optional[str] = None,
        keyId: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_vpc_link(
        self,
        vpcLinkId: str,
    ) -> Dict:
        pass


    def get_vpc_links(
        self,
        position: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_api_keys(
        self,
        body: Union[bytes, IO],
        format: str,
        failOnWarnings: Optional[bool] = None,
    ) -> Dict:
        pass


    def import_documentation_parts(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: Optional[str] = None,
        failOnWarnings: Optional[bool] = None,
    ) -> Dict:
        pass


    def import_rest_api(
        self,
        body: Union[bytes, IO],
        failOnWarnings: Optional[bool] = None,
        parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_gateway_response(
        self,
        restApiId: str,
        responseType: str,
        statusCode: Optional[str] = None,
        responseParameters: Optional[Dict] = None,
        responseTemplates: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: str,
        integrationHttpMethod: Optional[str] = None,
        uri: Optional[str] = None,
        connectionType: Optional[str] = None,
        connectionId: Optional[str] = None,
        credentials: Optional[str] = None,
        requestParameters: Optional[Dict] = None,
        requestTemplates: Optional[Dict] = None,
        passthroughBehavior: Optional[str] = None,
        cacheNamespace: Optional[str] = None,
        cacheKeyParameters: Optional[List] = None,
        contentHandling: Optional[str] = None,
        timeoutInMillis: Optional[int] = None,
    ) -> Dict:
        pass


    def put_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: Optional[str] = None,
        responseParameters: Optional[Dict] = None,
        responseTemplates: Optional[Dict] = None,
        contentHandling: Optional[str] = None,
    ) -> Dict:
        pass


    def put_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: Optional[str] = None,
        apiKeyRequired: Optional[bool] = None,
        operationName: Optional[str] = None,
        requestParameters: Optional[Dict] = None,
        requestModels: Optional[Dict] = None,
        requestValidatorId: Optional[str] = None,
        authorizationScopes: Optional[List] = None,
    ) -> Dict:
        pass


    def put_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Optional[Dict] = None,
        responseModels: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_rest_api(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: Optional[str] = None,
        failOnWarnings: Optional[bool] = None,
        parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ):
        pass


    def test_invoke_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        headers: Optional[Dict] = None,
        multiValueHeaders: Optional[Dict] = None,
        pathWithQueryString: Optional[str] = None,
        body: Optional[str] = None,
        stageVariables: Optional[Dict] = None,
        additionalContext: Optional[Dict] = None,
    ) -> Dict:
        pass


    def test_invoke_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: Optional[str] = None,
        body: Optional[str] = None,
        headers: Optional[Dict] = None,
        multiValueHeaders: Optional[Dict] = None,
        clientCertificateId: Optional[str] = None,
        stageVariables: Optional[Dict] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ):
        pass


    def update_account(
        self,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_api_key(
        self,
        apiKey: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_base_path_mapping(
        self,
        domainName: str,
        basePath: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_client_certificate(
        self,
        clientCertificateId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_deployment(
        self,
        restApiId: str,
        deploymentId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_domain_name(
        self,
        domainName: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_gateway_response(
        self,
        restApiId: str,
        responseType: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_model(
        self,
        restApiId: str,
        modelName: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_resource(
        self,
        restApiId: str,
        resourceId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_rest_api(
        self,
        restApiId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_stage(
        self,
        restApiId: str,
        stageName: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_usage(
        self,
        usagePlanId: str,
        keyId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_usage_plan(
        self,
        usagePlanId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_vpc_link(
        self,
        vpcLinkId: str,
        patchOperations: Optional[List] = None,
    ) -> Dict:
        pass

