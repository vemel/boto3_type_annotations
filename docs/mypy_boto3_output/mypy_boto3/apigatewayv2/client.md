# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.apigatewayv2.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Apigatewayv2](index.md#apigatewayv2) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_api](#clientcreate_api)
        - [Client().create_api_mapping](#clientcreate_api_mapping)
        - [Client().create_authorizer](#clientcreate_authorizer)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_domain_name](#clientcreate_domain_name)
        - [Client().create_integration](#clientcreate_integration)
        - [Client().create_integration_response](#clientcreate_integration_response)
        - [Client().create_model](#clientcreate_model)
        - [Client().create_route](#clientcreate_route)
        - [Client().create_route_response](#clientcreate_route_response)
        - [Client().create_stage](#clientcreate_stage)
        - [Client().delete_api](#clientdelete_api)
        - [Client().delete_api_mapping](#clientdelete_api_mapping)
        - [Client().delete_authorizer](#clientdelete_authorizer)
        - [Client().delete_deployment](#clientdelete_deployment)
        - [Client().delete_domain_name](#clientdelete_domain_name)
        - [Client().delete_integration](#clientdelete_integration)
        - [Client().delete_integration_response](#clientdelete_integration_response)
        - [Client().delete_model](#clientdelete_model)
        - [Client().delete_route](#clientdelete_route)
        - [Client().delete_route_response](#clientdelete_route_response)
        - [Client().delete_stage](#clientdelete_stage)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_api](#clientget_api)
        - [Client().get_api_mapping](#clientget_api_mapping)
        - [Client().get_api_mappings](#clientget_api_mappings)
        - [Client().get_apis](#clientget_apis)
        - [Client().get_authorizer](#clientget_authorizer)
        - [Client().get_authorizers](#clientget_authorizers)
        - [Client().get_deployment](#clientget_deployment)
        - [Client().get_deployments](#clientget_deployments)
        - [Client().get_domain_name](#clientget_domain_name)
        - [Client().get_domain_names](#clientget_domain_names)
        - [Client().get_integration](#clientget_integration)
        - [Client().get_integration_response](#clientget_integration_response)
        - [Client().get_integration_responses](#clientget_integration_responses)
        - [Client().get_integrations](#clientget_integrations)
        - [Client().get_model](#clientget_model)
        - [Client().get_model_template](#clientget_model_template)
        - [Client().get_models](#clientget_models)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_route](#clientget_route)
        - [Client().get_route_response](#clientget_route_response)
        - [Client().get_route_responses](#clientget_route_responses)
        - [Client().get_routes](#clientget_routes)
        - [Client().get_stage](#clientget_stage)
        - [Client().get_stages](#clientget_stages)
        - [Client().get_tags](#clientget_tags)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_api](#clientupdate_api)
        - [Client().update_api_mapping](#clientupdate_api_mapping)
        - [Client().update_authorizer](#clientupdate_authorizer)
        - [Client().update_deployment](#clientupdate_deployment)
        - [Client().update_domain_name](#clientupdate_domain_name)
        - [Client().update_integration](#clientupdate_integration)
        - [Client().update_integration_response](#clientupdate_integration_response)
        - [Client().update_model](#clientupdate_model)
        - [Client().update_route](#clientupdate_route)
        - [Client().update_route_response](#clientupdate_route_response)
        - [Client().update_stage](#clientupdate_stage)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L19)

```python
def create_api(
    Name: str,
    ProtocolType: str,
    RouteSelectionExpression: str,
    ApiKeySelectionExpression: str = None,
    Description: str = None,
    DisableSchemaValidation: bool = None,
    Version: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_api_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L33)

```python
def create_api_mapping(
    ApiId: str,
    DomainName: str,
    Stage: str,
    ApiMappingKey: str = None,
) -> Dict[str, Any]:
```

### Client().create_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L39)

```python
def create_authorizer(
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
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L54)

```python
def create_deployment(
    ApiId: str,
    Description: str = None,
    StageName: str = None,
) -> Dict[str, Any]:
```

### Client().create_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L60)

```python
def create_domain_name(
    DomainName: str,
    DomainNameConfigurations: List[Any] = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L69)

```python
def create_integration(
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
```

### Client().create_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L89)

```python
def create_integration_response(
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseKey: str,
    ContentHandlingStrategy: str = None,
    ResponseParameters: Dict[str, Any] = None,
    ResponseTemplates: Dict[str, Any] = None,
    TemplateSelectionExpression: str = None,
) -> Dict[str, Any]:
```

### Client().create_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L102)

```python
def create_model(
    ApiId: str,
    Name: str,
    Schema: str,
    ContentType: str = None,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L113)

```python
def create_route(
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
```

### Client().create_route_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L131)

```python
def create_route_response(
    ApiId: str,
    RouteId: str,
    RouteResponseKey: str,
    ModelSelectionExpression: str = None,
    ResponseModels: Dict[str, Any] = None,
    ResponseParameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L143)

```python
def create_stage(
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
```

### Client().delete_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L159)

```python
def delete_api(ApiId: str) -> None:
```

### Client().delete_api_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L163)

```python
def delete_api_mapping(ApiMappingId: str, DomainName: str) -> None:
```

### Client().delete_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L167)

```python
def delete_authorizer(ApiId: str, AuthorizerId: str) -> None:
```

### Client().delete_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L171)

```python
def delete_deployment(ApiId: str, DeploymentId: str) -> None:
```

### Client().delete_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L175)

```python
def delete_domain_name(DomainName: str) -> None:
```

### Client().delete_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L179)

```python
def delete_integration(ApiId: str, IntegrationId: str) -> None:
```

### Client().delete_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L183)

```python
def delete_integration_response(
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str,
) -> None:
```

### Client().delete_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L189)

```python
def delete_model(ApiId: str, ModelId: str) -> None:
```

### Client().delete_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L193)

```python
def delete_route(ApiId: str, RouteId: str) -> None:
```

### Client().delete_route_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L197)

```python
def delete_route_response(
    ApiId: str,
    RouteId: str,
    RouteResponseId: str,
) -> None:
```

### Client().delete_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L203)

```python
def delete_stage(ApiId: str, StageName: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L207)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L217)

```python
def get_api(ApiId: str) -> Dict[str, Any]:
```

### Client().get_api_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L221)

```python
def get_api_mapping(ApiMappingId: str, DomainName: str) -> Dict[str, Any]:
```

### Client().get_api_mappings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L225)

```python
def get_api_mappings(
    DomainName: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_apis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L231)

```python
def get_apis(MaxResults: str = None, NextToken: str = None) -> Dict[str, Any]:
```

### Client().get_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L235)

```python
def get_authorizer(ApiId: str, AuthorizerId: str) -> Dict[str, Any]:
```

### Client().get_authorizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L239)

```python
def get_authorizers(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L245)

```python
def get_deployment(ApiId: str, DeploymentId: str) -> Dict[str, Any]:
```

### Client().get_deployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L249)

```python
def get_deployments(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L255)

```python
def get_domain_name(DomainName: str) -> Dict[str, Any]:
```

### Client().get_domain_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L259)

```python
def get_domain_names(
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L265)

```python
def get_integration(ApiId: str, IntegrationId: str) -> Dict[str, Any]:
```

### Client().get_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L269)

```python
def get_integration_response(
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str,
) -> Dict[str, Any]:
```

### Client().get_integration_responses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L275)

```python
def get_integration_responses(
    ApiId: str,
    IntegrationId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_integrations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L285)

```python
def get_integrations(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L291)

```python
def get_model(ApiId: str, ModelId: str) -> Dict[str, Any]:
```

### Client().get_model_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L295)

```python
def get_model_template(ApiId: str, ModelId: str) -> Dict[str, Any]:
```

### Client().get_models

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L299)

```python
def get_models(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L305)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L309)

```python
def get_route(ApiId: str, RouteId: str) -> Dict[str, Any]:
```

### Client().get_route_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L313)

```python
def get_route_response(
    ApiId: str,
    RouteId: str,
    RouteResponseId: str,
) -> Dict[str, Any]:
```

### Client().get_route_responses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L319)

```python
def get_route_responses(
    ApiId: str,
    RouteId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_routes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L325)

```python
def get_routes(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L331)

```python
def get_stage(ApiId: str, StageName: str) -> Dict[str, Any]:
```

### Client().get_stages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L335)

```python
def get_stages(
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L341)

```python
def get_tags(ResourceArn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L345)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L349)

```python
def tag_resource(
    ResourceArn: str,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L355)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L359)

```python
def update_api(
    ApiId: str,
    ApiKeySelectionExpression: str = None,
    Description: str = None,
    DisableSchemaValidation: bool = None,
    Name: str = None,
    RouteSelectionExpression: str = None,
    Version: str = None,
) -> Dict[str, Any]:
```

### Client().update_api_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L372)

```python
def update_api_mapping(
    ApiId: str,
    ApiMappingId: str,
    DomainName: str,
    ApiMappingKey: str = None,
    Stage: str = None,
) -> Dict[str, Any]:
```

### Client().update_authorizer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L383)

```python
def update_authorizer(
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
```

### Client().update_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L399)

```python
def update_deployment(
    ApiId: str,
    DeploymentId: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_domain_name

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L405)

```python
def update_domain_name(
    DomainName: str,
    DomainNameConfigurations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_integration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L411)

```python
def update_integration(
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
```

### Client().update_integration_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L432)

```python
def update_integration_response(
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str,
    ContentHandlingStrategy: str = None,
    IntegrationResponseKey: str = None,
    ResponseParameters: Dict[str, Any] = None,
    ResponseTemplates: Dict[str, Any] = None,
    TemplateSelectionExpression: str = None,
) -> Dict[str, Any]:
```

### Client().update_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L446)

```python
def update_model(
    ApiId: str,
    ModelId: str,
    ContentType: str = None,
    Description: str = None,
    Name: str = None,
    Schema: str = None,
) -> Dict[str, Any]:
```

### Client().update_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L458)

```python
def update_route(
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
```

### Client().update_route_response

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L477)

```python
def update_route_response(
    ApiId: str,
    RouteId: str,
    RouteResponseId: str,
    ModelSelectionExpression: str = None,
    ResponseModels: Dict[str, Any] = None,
    ResponseParameters: Dict[str, Any] = None,
    RouteResponseKey: str = None,
) -> Dict[str, Any]:
```

### Client().update_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/client.py#L490)

```python
def update_stage(
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
```
