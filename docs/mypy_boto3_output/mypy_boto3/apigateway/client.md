# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.apigateway.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Apigateway](index.md#apigateway) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_api_key](#clientcreate_api_key)
        - [Client().create_authorizer](#clientcreate_authorizer)
        - [Client().create_base_path_mapping](#clientcreate_base_path_mapping)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_documentation_part](#clientcreate_documentation_part)
        - [Client().create_documentation_version](#clientcreate_documentation_version)
        - [Client().create_domain_name](#clientcreate_domain_name)
        - [Client().create_model](#clientcreate_model)
        - [Client().create_request_validator](#clientcreate_request_validator)
        - [Client().create_resource](#clientcreate_resource)
        - [Client().create_rest_api](#clientcreate_rest_api)
        - [Client().create_stage](#clientcreate_stage)
        - [Client().create_usage_plan](#clientcreate_usage_plan)
        - [Client().create_usage_plan_key](#clientcreate_usage_plan_key)
        - [Client().create_vpc_link](#clientcreate_vpc_link)
        - [Client().delete_api_key](#clientdelete_api_key)
        - [Client().delete_authorizer](#clientdelete_authorizer)
        - [Client().delete_base_path_mapping](#clientdelete_base_path_mapping)
        - [Client().delete_client_certificate](#clientdelete_client_certificate)
        - [Client().delete_deployment](#clientdelete_deployment)
        - [Client().delete_documentation_part](#clientdelete_documentation_part)
        - [Client().delete_documentation_version](#clientdelete_documentation_version)
        - [Client().delete_domain_name](#clientdelete_domain_name)
        - [Client().delete_gateway_response](#clientdelete_gateway_response)
        - [Client().delete_integration](#clientdelete_integration)
        - [Client().delete_integration_response](#clientdelete_integration_response)
        - [Client().delete_method](#clientdelete_method)
        - [Client().delete_method_response](#clientdelete_method_response)
        - [Client().delete_model](#clientdelete_model)
        - [Client().delete_request_validator](#clientdelete_request_validator)
        - [Client().delete_resource](#clientdelete_resource)
        - [Client().delete_rest_api](#clientdelete_rest_api)
        - [Client().delete_stage](#clientdelete_stage)
        - [Client().delete_usage_plan](#clientdelete_usage_plan)
        - [Client().delete_usage_plan_key](#clientdelete_usage_plan_key)
        - [Client().delete_vpc_link](#clientdelete_vpc_link)
        - [Client().flush_stage_authorizers_cache](#clientflush_stage_authorizers_cache)
        - [Client().flush_stage_cache](#clientflush_stage_cache)
        - [Client().generate_client_certificate](#clientgenerate_client_certificate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_account](#clientget_account)
        - [Client().get_api_key](#clientget_api_key)
        - [Client().get_api_keys](#clientget_api_keys)
        - [Client().get_authorizer](#clientget_authorizer)
        - [Client().get_authorizers](#clientget_authorizers)
        - [Client().get_base_path_mapping](#clientget_base_path_mapping)
        - [Client().get_base_path_mappings](#clientget_base_path_mappings)
        - [Client().get_client_certificate](#clientget_client_certificate)
        - [Client().get_client_certificates](#clientget_client_certificates)
        - [Client().get_deployment](#clientget_deployment)
        - [Client().get_deployments](#clientget_deployments)
        - [Client().get_documentation_part](#clientget_documentation_part)
        - [Client().get_documentation_parts](#clientget_documentation_parts)
        - [Client().get_documentation_version](#clientget_documentation_version)
        - [Client().get_documentation_versions](#clientget_documentation_versions)
        - [Client().get_domain_name](#clientget_domain_name)
        - [Client().get_domain_names](#clientget_domain_names)
        - [Client().get_export](#clientget_export)
        - [Client().get_gateway_response](#clientget_gateway_response)
        - [Client().get_gateway_responses](#clientget_gateway_responses)
        - [Client().get_integration](#clientget_integration)
        - [Client().get_integration_response](#clientget_integration_response)
        - [Client().get_method](#clientget_method)
        - [Client().get_method_response](#clientget_method_response)
        - [Client().get_model](#clientget_model)
        - [Client().get_model_template](#clientget_model_template)
        - [Client().get_models](#clientget_models)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_request_validator](#clientget_request_validator)
        - [Client().get_request_validators](#clientget_request_validators)
        - [Client().get_resource](#clientget_resource)
        - [Client().get_resources](#clientget_resources)
        - [Client().get_rest_api](#clientget_rest_api)
        - [Client().get_rest_apis](#clientget_rest_apis)
        - [Client().get_sdk](#clientget_sdk)
        - [Client().get_sdk_type](#clientget_sdk_type)
        - [Client().get_sdk_types](#clientget_sdk_types)
        - [Client().get_stage](#clientget_stage)
        - [Client().get_stages](#clientget_stages)
        - [Client().get_tags](#clientget_tags)
        - [Client().get_usage](#clientget_usage)
        - [Client().get_usage_plan](#clientget_usage_plan)
        - [Client().get_usage_plan_key](#clientget_usage_plan_key)
        - [Client().get_usage_plan_keys](#clientget_usage_plan_keys)
        - [Client().get_usage_plans](#clientget_usage_plans)
        - [Client().get_vpc_link](#clientget_vpc_link)
        - [Client().get_vpc_links](#clientget_vpc_links)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_api_keys](#clientimport_api_keys)
        - [Client().import_documentation_parts](#clientimport_documentation_parts)
        - [Client().import_rest_api](#clientimport_rest_api)
        - [Client().put_gateway_response](#clientput_gateway_response)
        - [Client().put_integration](#clientput_integration)
        - [Client().put_integration_response](#clientput_integration_response)
        - [Client().put_method](#clientput_method)
        - [Client().put_method_response](#clientput_method_response)
        - [Client().put_rest_api](#clientput_rest_api)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().test_invoke_authorizer](#clienttest_invoke_authorizer)
        - [Client().test_invoke_method](#clienttest_invoke_method)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_account](#clientupdate_account)
        - [Client().update_api_key](#clientupdate_api_key)
        - [Client().update_authorizer](#clientupdate_authorizer)
        - [Client().update_base_path_mapping](#clientupdate_base_path_mapping)
        - [Client().update_client_certificate](#clientupdate_client_certificate)
        - [Client().update_deployment](#clientupdate_deployment)
        - [Client().update_documentation_part](#clientupdate_documentation_part)
        - [Client().update_documentation_version](#clientupdate_documentation_version)
        - [Client().update_domain_name](#clientupdate_domain_name)
        - [Client().update_gateway_response](#clientupdate_gateway_response)
        - [Client().update_integration](#clientupdate_integration)
        - [Client().update_integration_response](#clientupdate_integration_response)
        - [Client().update_method](#clientupdate_method)
        - [Client().update_method_response](#clientupdate_method_response)
        - [Client().update_model](#clientupdate_model)
        - [Client().update_request_validator](#clientupdate_request_validator)
        - [Client().update_resource](#clientupdate_resource)
        - [Client().update_rest_api](#clientupdate_rest_api)
        - [Client().update_stage](#clientupdate_stage)
        - [Client().update_usage](#clientupdate_usage)
        - [Client().update_usage_plan](#clientupdate_usage_plan)
        - [Client().update_vpc_link](#clientupdate_vpc_link)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L14)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L17)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L21)

```python
def create_api_key(
    name: str = None,
    description: str = None,
    enabled: bool = None,
    generateDistinctId: bool = None,
    value: str = None,
    stageKeys: List[Any] = None,
    customerId: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L35)

```python
def create_authorizer(
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
```

### Client().create_base_path_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L51)

```python
def create_base_path_mapping(
    domainName: str,
    restApiId: str,
    basePath: str = None,
    stage: str = None,
) -> Dict[str, Any]:
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L57)

```python
def create_deployment(
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
```

### Client().create_documentation_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L72)

```python
def create_documentation_part(
    restApiId: str,
    location: Dict[str, Any],
    properties: str,
) -> Dict[str, Any]:
```

### Client().create_documentation_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L78)

```python
def create_documentation_version(
    restApiId: str,
    documentationVersion: str,
    stageName: str = None,
    description: str = None,
) -> Dict[str, Any]:
```

### Client().create_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L88)

```python
def create_domain_name(
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
```

### Client().create_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L105)

```python
def create_model(
    restApiId: str,
    name: str,
    contentType: str,
    description: str = None,
    schema: str = None,
) -> Dict[str, Any]:
```

### Client().create_request_validator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L116)

```python
def create_request_validator(
    restApiId: str,
    name: str = None,
    validateRequestBody: bool = None,
    validateRequestParameters: bool = None,
) -> Dict[str, Any]:
```

### Client().create_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L126)

```python
def create_resource(
    restApiId: str,
    parentId: str,
    pathPart: str,
) -> Dict[str, Any]:
```

### Client().create_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L132)

```python
def create_rest_api(
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
```

### Client().create_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L148)

```python
def create_stage(
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
```

### Client().create_usage_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L165)

```python
def create_usage_plan(
    name: str,
    description: str = None,
    apiStages: List[Any] = None,
    throttle: Dict[str, Any] = None,
    quota: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_usage_plan_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L177)

```python
def create_usage_plan_key(
    usagePlanId: str,
    keyId: str,
    keyType: str,
) -> Dict[str, Any]:
```

### Client().create_vpc_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L183)

```python
def create_vpc_link(
    name: str,
    targetArns: List[Any],
    description: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L193)

```python
def delete_api_key(apiKey: str) -> None:
```

### Client().delete_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L197)

```python
def delete_authorizer(restApiId: str, authorizerId: str) -> None:
```

### Client().delete_base_path_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L201)

```python
def delete_base_path_mapping(domainName: str, basePath: str) -> None:
```

### Client().delete_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L205)

```python
def delete_client_certificate(clientCertificateId: str) -> None:
```

### Client().delete_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L209)

```python
def delete_deployment(restApiId: str, deploymentId: str) -> None:
```

### Client().delete_documentation_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L213)

```python
def delete_documentation_part(
    restApiId: str,
    documentationPartId: str,
) -> None:
```

### Client().delete_documentation_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L219)

```python
def delete_documentation_version(
    restApiId: str,
    documentationVersion: str,
) -> None:
```

### Client().delete_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L225)

```python
def delete_domain_name(domainName: str) -> None:
```

### Client().delete_gateway_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L229)

```python
def delete_gateway_response(restApiId: str, responseType: str) -> None:
```

### Client().delete_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L233)

```python
def delete_integration(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
) -> None:
```

### Client().delete_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L239)

```python
def delete_integration_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
) -> None:
```

### Client().delete_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L245)

```python
def delete_method(restApiId: str, resourceId: str, httpMethod: str) -> None:
```

### Client().delete_method_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L249)

```python
def delete_method_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
) -> None:
```

### Client().delete_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L255)

```python
def delete_model(restApiId: str, modelName: str) -> None:
```

### Client().delete_request_validator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L259)

```python
def delete_request_validator(restApiId: str, requestValidatorId: str) -> None:
```

### Client().delete_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L263)

```python
def delete_resource(restApiId: str, resourceId: str) -> None:
```

### Client().delete_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L267)

```python
def delete_rest_api(restApiId: str) -> None:
```

### Client().delete_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L271)

```python
def delete_stage(restApiId: str, stageName: str) -> None:
```

### Client().delete_usage_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L275)

```python
def delete_usage_plan(usagePlanId: str) -> None:
```

### Client().delete_usage_plan_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L279)

```python
def delete_usage_plan_key(usagePlanId: str, keyId: str) -> None:
```

### Client().delete_vpc_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L283)

```python
def delete_vpc_link(vpcLinkId: str) -> None:
```

### Client().flush_stage_authorizers_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L287)

```python
def flush_stage_authorizers_cache(restApiId: str, stageName: str) -> None:
```

### Client().flush_stage_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L291)

```python
def flush_stage_cache(restApiId: str, stageName: str) -> None:
```

### Client().generate_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L295)

```python
def generate_client_certificate(
    description: str = None,
    tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L301)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L311)

```python
def get_account() -> Dict[str, Any]:
```

### Client().get_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L315)

```python
def get_api_key(apiKey: str, includeValue: bool = None) -> Dict[str, Any]:
```

### Client().get_api_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L319)

```python
def get_api_keys(
    position: str = None,
    limit: int = None,
    nameQuery: str = None,
    customerId: str = None,
    includeValues: bool = None,
) -> Dict[str, Any]:
```

### Client().get_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L330)

```python
def get_authorizer(restApiId: str, authorizerId: str) -> Dict[str, Any]:
```

### Client().get_authorizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L334)

```python
def get_authorizers(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_base_path_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L340)

```python
def get_base_path_mapping(domainName: str, basePath: str) -> Dict[str, Any]:
```

### Client().get_base_path_mappings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L344)

```python
def get_base_path_mappings(
    domainName: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L350)

```python
def get_client_certificate(clientCertificateId: str) -> Dict[str, Any]:
```

### Client().get_client_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L354)

```python
def get_client_certificates(
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L360)

```python
def get_deployment(
    restApiId: str,
    deploymentId: str,
    embed: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L366)

```python
def get_deployments(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_documentation_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L372)

```python
def get_documentation_part(
    restApiId: str,
    documentationPartId: str,
) -> Dict[str, Any]:
```

### Client().get_documentation_parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L378)

```python
def get_documentation_parts(
    restApiId: str,
    type: str = None,
    nameQuery: str = None,
    path: str = None,
    position: str = None,
    limit: int = None,
    locationStatus: str = None,
) -> Dict[str, Any]:
```

### Client().get_documentation_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L391)

```python
def get_documentation_version(
    restApiId: str,
    documentationVersion: str,
) -> Dict[str, Any]:
```

### Client().get_documentation_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L397)

```python
def get_documentation_versions(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L403)

```python
def get_domain_name(domainName: str) -> Dict[str, Any]:
```

### Client().get_domain_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L407)

```python
def get_domain_names(
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L413)

```python
def get_export(
    restApiId: str,
    stageName: str,
    exportType: str,
    parameters: Dict[str, Any] = None,
    accepts: str = None,
) -> Dict[str, Any]:
```

### Client().get_gateway_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L424)

```python
def get_gateway_response(restApiId: str, responseType: str) -> Dict[str, Any]:
```

### Client().get_gateway_responses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L428)

```python
def get_gateway_responses(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L434)

```python
def get_integration(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
) -> Dict[str, Any]:
```

### Client().get_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L440)

```python
def get_integration_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
) -> Dict[str, Any]:
```

### Client().get_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L446)

```python
def get_method(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
) -> Dict[str, Any]:
```

### Client().get_method_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L452)

```python
def get_method_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
) -> Dict[str, Any]:
```

### Client().get_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L458)

```python
def get_model(
    restApiId: str,
    modelName: str,
    flatten: bool = None,
) -> Dict[str, Any]:
```

### Client().get_model_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L464)

```python
def get_model_template(restApiId: str, modelName: str) -> Dict[str, Any]:
```

### Client().get_models

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L468)

```python
def get_models(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L474)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_request_validator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L478)

```python
def get_request_validator(
    restApiId: str,
    requestValidatorId: str,
) -> Dict[str, Any]:
```

### Client().get_request_validators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L484)

```python
def get_request_validators(
    restApiId: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L490)

```python
def get_resource(
    restApiId: str,
    resourceId: str,
    embed: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L496)

```python
def get_resources(
    restApiId: str,
    position: str = None,
    limit: int = None,
    embed: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L506)

```python
def get_rest_api(restApiId: str) -> Dict[str, Any]:
```

### Client().get_rest_apis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L510)

```python
def get_rest_apis(position: str = None, limit: int = None) -> Dict[str, Any]:
```

### Client().get_sdk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L514)

```python
def get_sdk(
    restApiId: str,
    stageName: str,
    sdkType: str,
    parameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_sdk_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L524)

```python
def get_sdk_type(id: str) -> Dict[str, Any]:
```

### Client().get_sdk_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L528)

```python
def get_sdk_types(position: str = None, limit: int = None) -> Dict[str, Any]:
```

### Client().get_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L532)

```python
def get_stage(restApiId: str, stageName: str) -> Dict[str, Any]:
```

### Client().get_stages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L536)

```python
def get_stages(restApiId: str, deploymentId: str = None) -> Dict[str, Any]:
```

### Client().get_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L540)

```python
def get_tags(
    resourceArn: str,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L546)

```python
def get_usage(
    usagePlanId: str,
    startDate: str,
    endDate: str,
    keyId: str = None,
    position: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_usage_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L558)

```python
def get_usage_plan(usagePlanId: str) -> Dict[str, Any]:
```

### Client().get_usage_plan_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L562)

```python
def get_usage_plan_key(usagePlanId: str, keyId: str) -> Dict[str, Any]:
```

### Client().get_usage_plan_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L566)

```python
def get_usage_plan_keys(
    usagePlanId: str,
    position: str = None,
    limit: int = None,
    nameQuery: str = None,
) -> Dict[str, Any]:
```

### Client().get_usage_plans

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L576)

```python
def get_usage_plans(
    position: str = None,
    keyId: str = None,
    limit: int = None,
) -> Dict[str, Any]:
```

### Client().get_vpc_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L582)

```python
def get_vpc_link(vpcLinkId: str) -> Dict[str, Any]:
```

### Client().get_vpc_links

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L586)

```python
def get_vpc_links(position: str = None, limit: int = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L590)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_api_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L594)

```python
def import_api_keys(
    body: Union[bytes, IO],
    format: str,
    failOnWarnings: bool = None,
) -> Dict[str, Any]:
```

### Client().import_documentation_parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L600)

```python
def import_documentation_parts(
    restApiId: str,
    body: Union[bytes, IO],
    mode: str = None,
    failOnWarnings: bool = None,
) -> Dict[str, Any]:
```

### Client().import_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L610)

```python
def import_rest_api(
    body: Union[bytes, IO],
    failOnWarnings: bool = None,
    parameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_gateway_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L619)

```python
def put_gateway_response(
    restApiId: str,
    responseType: str,
    statusCode: str = None,
    responseParameters: Dict[str, Any] = None,
    responseTemplates: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L630)

```python
def put_integration(
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
```

### Client().put_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L652)

```python
def put_integration_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    selectionPattern: str = None,
    responseParameters: Dict[str, Any] = None,
    responseTemplates: Dict[str, Any] = None,
    contentHandling: str = None,
) -> Dict[str, Any]:
```

### Client().put_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L666)

```python
def put_method(
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
```

### Client().put_method_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L683)

```python
def put_method_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    responseParameters: Dict[str, Any] = None,
    responseModels: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L695)

```python
def put_rest_api(
    restApiId: str,
    body: Union[bytes, IO],
    mode: str = None,
    failOnWarnings: bool = None,
    parameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L706)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> None:
```

### Client().test_invoke_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L710)

```python
def test_invoke_authorizer(
    restApiId: str,
    authorizerId: str,
    headers: Dict[str, Any] = None,
    multiValueHeaders: Dict[str, Any] = None,
    pathWithQueryString: str = None,
    body: str = None,
    stageVariables: Dict[str, Any] = None,
    additionalContext: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().test_invoke_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L724)

```python
def test_invoke_method(
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
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L739)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> None:
```

### Client().update_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L743)

```python
def update_account(patchOperations: List[Any] = None) -> Dict[str, Any]:
```

### Client().update_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L747)

```python
def update_api_key(
    apiKey: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L753)

```python
def update_authorizer(
    restApiId: str,
    authorizerId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_base_path_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L759)

```python
def update_base_path_mapping(
    domainName: str,
    basePath: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L765)

```python
def update_client_certificate(
    clientCertificateId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L771)

```python
def update_deployment(
    restApiId: str,
    deploymentId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_documentation_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L777)

```python
def update_documentation_part(
    restApiId: str,
    documentationPartId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_documentation_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L786)

```python
def update_documentation_version(
    restApiId: str,
    documentationVersion: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L795)

```python
def update_domain_name(
    domainName: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_gateway_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L801)

```python
def update_gateway_response(
    restApiId: str,
    responseType: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L807)

```python
def update_integration(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L817)

```python
def update_integration_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_method

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L828)

```python
def update_method(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_method_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L838)

```python
def update_method_response(
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L849)

```python
def update_model(
    restApiId: str,
    modelName: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_request_validator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L855)

```python
def update_request_validator(
    restApiId: str,
    requestValidatorId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L861)

```python
def update_resource(
    restApiId: str,
    resourceId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_rest_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L867)

```python
def update_rest_api(
    restApiId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L873)

```python
def update_stage(
    restApiId: str,
    stageName: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L879)

```python
def update_usage(
    usagePlanId: str,
    keyId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_usage_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L885)

```python
def update_usage_plan(
    usagePlanId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_vpc_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigateway/client.py#L891)

```python
def update_vpc_link(
    vpcLinkId: str,
    patchOperations: List[Any] = None,
) -> Dict[str, Any]:
```
