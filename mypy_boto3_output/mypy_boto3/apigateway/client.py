from __future__ import annotations

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
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_api_key(
        self,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        generateDistinctId: bool = None,
        value: str = None,
        stageKeys: List[Any] = None,
        customerId: str = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_authorizer(
        self,
        restApiId: str,
        name: str,
        type: str,
        providerARNs: List[Any] = None,
        authType: str = None,
        authorizerUri: str = None,
        authorizerCredentials: str = None,
        identitySource: str = None,
        identityValidationExpression: str = None,
        authorizerResultTtlInSeconds: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_base_path_mapping(
        self, domainName: str, restApiId: str, basePath: str = None, stage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_deployment(
        self,
        restApiId: str,
        stageName: str = None,
        stageDescription: str = None,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: str = None,
        variables: Dict[str, Any] = None,
        canarySettings: Dict[str, Any] = None,
        tracingEnabled: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_documentation_part(
        self, restApiId: str, location: Dict[str, Any], properties: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        stageName: str = None,
        description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_domain_name(
        self,
        domainName: str,
        certificateName: str = None,
        certificateBody: str = None,
        certificatePrivateKey: str = None,
        certificateChain: str = None,
        certificateArn: str = None,
        regionalCertificateName: str = None,
        regionalCertificateArn: str = None,
        endpointConfiguration: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
        securityPolicy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_model(
        self,
        restApiId: str,
        name: str,
        contentType: str,
        description: str = None,
        schema: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_request_validator(
        self,
        restApiId: str,
        name: str = None,
        validateRequestBody: bool = None,
        validateRequestParameters: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_resource(
        self, restApiId: str, parentId: str, pathPart: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_rest_api(
        self,
        name: str,
        description: str = None,
        version: str = None,
        cloneFrom: str = None,
        binaryMediaTypes: List[Any] = None,
        minimumCompressionSize: int = None,
        apiKeySource: str = None,
        endpointConfiguration: Dict[str, Any] = None,
        policy: str = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stage(
        self,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: str = None,
        variables: Dict[str, Any] = None,
        documentationVersion: str = None,
        canarySettings: Dict[str, Any] = None,
        tracingEnabled: bool = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_usage_plan(
        self,
        name: str,
        description: str = None,
        apiStages: List[Any] = None,
        throttle: Dict[str, Any] = None,
        quota: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_usage_plan_key(
        self, usagePlanId: str, keyId: str, keyType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_vpc_link(
        self,
        name: str,
        targetArns: List[Any],
        description: str = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_api_key(self, apiKey: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_authorizer(self, restApiId: str, authorizerId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_base_path_mapping(self, domainName: str, basePath: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_client_certificate(self, clientCertificateId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_deployment(self, restApiId: str, deploymentId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_documentation_part(
        self, restApiId: str, documentationPartId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_documentation_version(
        self, restApiId: str, documentationVersion: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_domain_name(self, domainName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_gateway_response(self, restApiId: str, responseType: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_integration(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_method(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_model(self, restApiId: str, modelName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_request_validator(self, restApiId: str, requestValidatorId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_resource(self, restApiId: str, resourceId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_rest_api(self, restApiId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_stage(self, restApiId: str, stageName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_usage_plan(self, usagePlanId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_usage_plan_key(self, usagePlanId: str, keyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vpc_link(self, vpcLinkId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def flush_stage_authorizers_cache(self, restApiId: str, stageName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def flush_stage_cache(self, restApiId: str, stageName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def generate_client_certificate(
        self, description: str = None, tags: Dict[str, Any] = None
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
    def get_account(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_api_key(self, apiKey: str, includeValue: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_api_keys(
        self,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_authorizer(self, restApiId: str, authorizerId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_authorizers(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_base_path_mapping(self, domainName: str, basePath: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_base_path_mappings(
        self, domainName: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_client_certificate(self, clientCertificateId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_client_certificates(
        self, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_deployment(
        self, restApiId: str, deploymentId: str, embed: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_deployments(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_documentation_part(
        self, restApiId: str, documentationPartId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_documentation_parts(
        self,
        restApiId: str,
        type: str = None,
        nameQuery: str = None,
        path: str = None,
        position: str = None,
        limit: int = None,
        locationStatus: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_documentation_version(
        self, restApiId: str, documentationVersion: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_documentation_versions(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_name(self, domainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_names(
        self, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_export(
        self,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Dict[str, Any] = None,
        accepts: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_gateway_response(self, restApiId: str, responseType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_gateway_responses(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integration(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_method(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_model(
        self, restApiId: str, modelName: str, flatten: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_model_template(self, restApiId: str, modelName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_models(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_request_validator(
        self, restApiId: str, requestValidatorId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_request_validators(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resource(
        self, restApiId: str, resourceId: str, embed: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resources(
        self,
        restApiId: str,
        position: str = None,
        limit: int = None,
        embed: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rest_api(self, restApiId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rest_apis(self, position: str = None, limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sdk(
        self,
        restApiId: str,
        stageName: str,
        sdkType: str,
        parameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sdk_type(self, id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_sdk_types(self, position: str = None, limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_stage(self, restApiId: str, stageName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_stages(self, restApiId: str, deploymentId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tags(
        self, resourceArn: str, position: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        position: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage_plan(self, usagePlanId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage_plan_key(self, usagePlanId: str, keyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage_plan_keys(
        self,
        usagePlanId: str,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage_plans(
        self, position: str = None, keyId: str = None, limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_vpc_link(self, vpcLinkId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_vpc_links(self, position: str = None, limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def import_api_keys(
        self, body: Union[bytes, IO], format: str, failOnWarnings: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def import_documentation_parts(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: str = None,
        failOnWarnings: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def import_rest_api(
        self,
        body: Union[bytes, IO],
        failOnWarnings: bool = None,
        parameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_gateway_response(
        self,
        restApiId: str,
        responseType: str,
        statusCode: str = None,
        responseParameters: Dict[str, Any] = None,
        responseTemplates: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: str,
        integrationHttpMethod: str = None,
        uri: str = None,
        connectionType: str = None,
        connectionId: str = None,
        credentials: str = None,
        requestParameters: Dict[str, Any] = None,
        requestTemplates: Dict[str, Any] = None,
        passthroughBehavior: str = None,
        cacheNamespace: str = None,
        cacheKeyParameters: List[Any] = None,
        contentHandling: str = None,
        timeoutInMillis: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str = None,
        responseParameters: Dict[str, Any] = None,
        responseTemplates: Dict[str, Any] = None,
        contentHandling: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: str = None,
        apiKeyRequired: bool = None,
        operationName: str = None,
        requestParameters: Dict[str, Any] = None,
        requestModels: Dict[str, Any] = None,
        requestValidatorId: str = None,
        authorizationScopes: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Dict[str, Any] = None,
        responseModels: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_rest_api(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: str = None,
        failOnWarnings: bool = None,
        parameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def test_invoke_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        headers: Dict[str, Any] = None,
        multiValueHeaders: Dict[str, Any] = None,
        pathWithQueryString: str = None,
        body: str = None,
        stageVariables: Dict[str, Any] = None,
        additionalContext: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_invoke_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str = None,
        body: str = None,
        headers: Dict[str, Any] = None,
        multiValueHeaders: Dict[str, Any] = None,
        clientCertificateId: str = None,
        stageVariables: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_account(self, patchOperations: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_api_key(
        self, apiKey: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_authorizer(
        self, restApiId: str, authorizerId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_base_path_mapping(
        self, domainName: str, basePath: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_client_certificate(
        self, clientCertificateId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_deployment(
        self, restApiId: str, deploymentId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_name(
        self, domainName: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_gateway_response(
        self, restApiId: str, responseType: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_model(
        self, restApiId: str, modelName: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_request_validator(
        self, restApiId: str, requestValidatorId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resource(
        self, restApiId: str, resourceId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_rest_api(
        self, restApiId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stage(
        self, restApiId: str, stageName: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_usage(
        self, usagePlanId: str, keyId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_usage_plan(
        self, usagePlanId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_vpc_link(
        self, vpcLinkId: str, patchOperations: List[Any] = None
    ) -> Dict[str, Any]:
        pass
