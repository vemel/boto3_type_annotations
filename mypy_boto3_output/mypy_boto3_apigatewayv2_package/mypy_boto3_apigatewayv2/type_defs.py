"Main interface for apigatewayv2 type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateApiMappingResponseTypeDef",
    "ClientCreateApiResponseTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateIntegrationResponseResponseTypeDef",
    "ClientCreateIntegrationResponseTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRouteRequestParametersTypeDef",
    "ClientCreateRouteResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseTypeDef",
    "ClientCreateRouteResponseRequestParametersTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateStageAccessLogSettingsTypeDef",
    "ClientCreateStageDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseAccessLogSettingsTypeDef",
    "ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseRouteSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateStageRouteSettingsTypeDef",
    "ClientGetApiMappingResponseTypeDef",
    "ClientGetApiMappingsResponseItemsTypeDef",
    "ClientGetApiMappingsResponseTypeDef",
    "ClientGetApiResponseTypeDef",
    "ClientGetApisResponseItemsTypeDef",
    "ClientGetApisResponseTypeDef",
    "ClientGetAuthorizerResponseTypeDef",
    "ClientGetAuthorizersResponseItemsTypeDef",
    "ClientGetAuthorizersResponseTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseItemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    "ClientGetDomainNamesResponseItemsTypeDef",
    "ClientGetDomainNamesResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetIntegrationResponsesResponseItemsTypeDef",
    "ClientGetIntegrationResponsesResponseTypeDef",
    "ClientGetIntegrationsResponseItemsTypeDef",
    "ClientGetIntegrationsResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelTemplateResponseTypeDef",
    "ClientGetModelsResponseItemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRouteResponseResponseResponseParametersTypeDef",
    "ClientGetRouteResponseResponseTypeDef",
    "ClientGetRouteResponseRequestParametersTypeDef",
    "ClientGetRouteResponseTypeDef",
    "ClientGetRouteResponsesResponseItemsResponseParametersTypeDef",
    "ClientGetRouteResponsesResponseItemsTypeDef",
    "ClientGetRouteResponsesResponseTypeDef",
    "ClientGetRoutesResponseItemsRequestParametersTypeDef",
    "ClientGetRoutesResponseItemsTypeDef",
    "ClientGetRoutesResponseTypeDef",
    "ClientGetStageResponseAccessLogSettingsTypeDef",
    "ClientGetStageResponseDefaultRouteSettingsTypeDef",
    "ClientGetStageResponseRouteSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    "ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientUpdateApiMappingResponseTypeDef",
    "ClientUpdateApiResponseTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRouteRequestParametersTypeDef",
    "ClientUpdateRouteResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseTypeDef",
    "ClientUpdateRouteResponseRequestParametersTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateStageAccessLogSettingsTypeDef",
    "ClientUpdateStageDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseAccessLogSettingsTypeDef",
    "ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseRouteSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateStageRouteSettingsTypeDef",
    "GetApisPaginatePaginationConfigTypeDef",
    "GetApisPaginateResponseItemsTypeDef",
    "GetApisPaginateResponseTypeDef",
    "GetAuthorizersPaginatePaginationConfigTypeDef",
    "GetAuthorizersPaginateResponseItemsTypeDef",
    "GetAuthorizersPaginateResponseTypeDef",
    "GetDeploymentsPaginatePaginationConfigTypeDef",
    "GetDeploymentsPaginateResponseItemsTypeDef",
    "GetDeploymentsPaginateResponseTypeDef",
    "GetDomainNamesPaginatePaginationConfigTypeDef",
    "GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef",
    "GetDomainNamesPaginateResponseItemsTypeDef",
    "GetDomainNamesPaginateResponseTypeDef",
    "GetIntegrationResponsesPaginatePaginationConfigTypeDef",
    "GetIntegrationResponsesPaginateResponseItemsTypeDef",
    "GetIntegrationResponsesPaginateResponseTypeDef",
    "GetIntegrationsPaginatePaginationConfigTypeDef",
    "GetIntegrationsPaginateResponseItemsTypeDef",
    "GetIntegrationsPaginateResponseTypeDef",
    "GetModelsPaginatePaginationConfigTypeDef",
    "GetModelsPaginateResponseItemsTypeDef",
    "GetModelsPaginateResponseTypeDef",
    "GetRouteResponsesPaginatePaginationConfigTypeDef",
    "GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef",
    "GetRouteResponsesPaginateResponseItemsTypeDef",
    "GetRouteResponsesPaginateResponseTypeDef",
    "GetRoutesPaginatePaginationConfigTypeDef",
    "GetRoutesPaginateResponseItemsRequestParametersTypeDef",
    "GetRoutesPaginateResponseItemsTypeDef",
    "GetRoutesPaginateResponseTypeDef",
    "GetStagesPaginatePaginationConfigTypeDef",
    "GetStagesPaginateResponseItemsAccessLogSettingsTypeDef",
    "GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef",
    "GetStagesPaginateResponseItemsRouteSettingsTypeDef",
    "GetStagesPaginateResponseItemsTypeDef",
    "GetStagesPaginateResponseTypeDef",
)


_ClientCreateApiMappingResponseTypeDef = TypedDict(
    "_ClientCreateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientCreateApiMappingResponseTypeDef(_ClientCreateApiMappingResponseTypeDef):
    """
    Type definition for `ClientCreateApiMapping` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ApiId** *(string) --*

      The API identifier.

    - **ApiMappingId** *(string) --*

      The API mapping identifier.

    - **ApiMappingKey** *(string) --*

      The API mapping key.

    - **Stage** *(string) --*

      The API stage.
    """


_ClientCreateApiResponseTypeDef = TypedDict(
    "_ClientCreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateApiResponseTypeDef(_ClientCreateApiResponseTypeDef):
    """
    Type definition for `ClientCreateApi` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ApiEndpoint** *(string) --*

      The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
      is typically appended to this URI to form a complete path to a deployed API stage.

    - **ApiId** *(string) --*

      The API ID.

    - **ApiKeySelectionExpression** *(string) --*

      An API key selection expression. See `API Key Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
      .

    - **CreatedDate** *(datetime) --*

      The timestamp when the API was created.

    - **Description** *(string) --*

      The description of the API.

    - **DisableSchemaValidation** *(boolean) --*

      Avoid validating models when creating a deployment.

    - **Name** *(string) --*

      The name of the API.

    - **ProtocolType** *(string) --*

      The API protocol: Currently only WEBSOCKET is supported.

    - **RouteSelectionExpression** *(string) --*

      The route selection expression for the API.

    - **Version** *(string) --*

      A version identifier for the API.

    - **Warnings** *(list) --*

      The warning messages reported when failonwarnings is turned on during API import.

      - *(string) --*

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "_ClientCreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientCreateAuthorizerResponseTypeDef(_ClientCreateAuthorizerResponseTypeDef):
    """
    Type definition for `ClientCreateAuthorizer` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **AuthorizerCredentialsArn** *(string) --*

      Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
      To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
      To use resource-based permissions on the Lambda function, specify null.

    - **AuthorizerId** *(string) --*

      The authorizer identifier.

    - **AuthorizerResultTtlInSeconds** *(integer) --*

      The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
      authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer
      responses. If this field is not set, the default value is 300. The maximum value is 3600, or
      1 hour.

    - **AuthorizerType** *(string) --*

      The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using
      incoming request parameters.

    - **AuthorizerUri** *(string) --*

      The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a
      well-formed Lambda function URI, for example,
      arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
      In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} ,
      where {region} is the same as the region hosting the Lambda function, path indicates that the
      remaining substring in the URI should be treated as the path to the resource, including the
      initial /. For Lambda functions, this is usually of the form
      /2015-03-31/functions/[FunctionARN]/invocations.

    - **IdentitySource** *(list) --*

      The identity source for which authorization is requested.

      For the REQUEST authorizer, this is required when authorization caching is enabled. The value
      is a comma-separated string of one or more mapping expressions of the specified request
      parameters. For example, if an Auth header and a Name query string parameters are defined as
      identity sources, this value is method.request.header.Auth, method.request.querystring.Name.
      These parameters will be used to derive the authorization caching key and to perform runtime
      validation of the REQUEST authorizer by verifying all of the identity-related request
      parameters are present, not null, and non-empty. Only when this is true does the authorizer
      invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response
      without calling the Lambda function. The valid value is a string of comma-separated mapping
      expressions of the specified request parameters. When the authorization caching is not
      enabled, this property is optional.

      - *(string) --*

    - **IdentityValidationExpression** *(string) --*

      The validation expression does not apply to the REQUEST authorizer.

    - **Name** *(string) --*

      The name of the authorizer.

    - **ProviderArns** *(list) --*

      For REQUEST authorizer, this is not defined.

      - *(string) --*

        Represents an Amazon Resource Name (ARN).
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **CreatedDate** *(datetime) --*

      The date and time when the Deployment resource was created.

    - **DeploymentId** *(string) --*

      The identifier for the deployment.

    - **DeploymentStatus** *(string) --*

      The status of the deployment: PENDING, FAILED, or SUCCEEDED.

    - **DeploymentStatusMessage** *(string) --*

      May contain additional feedback on the status of an API deployment.

    - **Description** *(string) --*

      The description for the deployment.
    """


_ClientCreateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientCreateDomainNameDomainNameConfigurationsTypeDef(
    _ClientCreateDomainNameDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientCreateDomainName` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain
      name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized endpoint
      for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this domain
      name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain name. The
      valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the
      status is UPDATING, the domain cannot be modified further until the existing operation is
      complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain name
      migration.
    """


_ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientCreateDomainNameResponse` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this
      domain name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized
      endpoint for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this
      domain name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain name.
      The valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
      the status is UPDATING, the domain cannot be modified further until the existing
      operation is complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain name
      migration.
    """


_ClientCreateDomainNameResponseTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateDomainNameResponseTypeDef(_ClientCreateDomainNameResponseTypeDef):
    """
    Type definition for `ClientCreateDomainName` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ApiMappingSelectionExpression** *(string) --*

      The API mapping selection expression.

    - **DomainName** *(string) --*

      The name of the DomainName resource.

    - **DomainNameConfigurations** *(list) --*

      The domain name configurations.

      - *(dict) --*

        The domain name configuration.

        - **ApiGatewayDomainName** *(string) --*

          A domain name for the WebSocket API.

        - **CertificateArn** *(string) --*

          An AWS-managed certificate that will be used by the edge-optimized endpoint for this
          domain name. AWS Certificate Manager is the only supported source.

        - **CertificateName** *(string) --*

          The user-friendly name of the certificate that will be used by the edge-optimized
          endpoint for this domain name.

        - **CertificateUploadDate** *(datetime) --*

          The timestamp when the certificate that was used by edge-optimized endpoint for this
          domain name was uploaded.

        - **EndpointType** *(string) --*

          The endpoint type.

        - **HostedZoneId** *(string) --*

          The Amazon Route 53 Hosted Zone ID of the endpoint.

        - **SecurityPolicy** *(string) --*

          The Transport Layer Security (TLS) version of the security policy for this domain name.
          The valid values are TLS_1_0 and TLS_1_2.

        - **DomainNameStatus** *(string) --*

          The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
          the status is UPDATING, the domain cannot be modified further until the existing
          operation is complete. If it is AVAILABLE, the domain can be updated.

        - **DomainNameStatusMessage** *(string) --*

          An optional text message containing detailed information about status of the domain name
          migration.

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientCreateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientCreateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": str,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class ClientCreateIntegrationResponseResponseTypeDef(
    _ClientCreateIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientCreateIntegrationResponse` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **IntegrationResponseId** *(string) --*

      The integration response ID.

    - **IntegrationResponseKey** *(string) --*

      The integration response key.

    - **ResponseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the backend. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of method.response.header.{name}, where name is a valid and unique header name. The mapped
      non-static value must match the pattern of integration.response.header.{name} or
      integration.response.body.{JSON-expression}, where name is a valid and unique response header
      name and JSON-expression is a valid JSON expression without the $ prefix.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **ResponseTemplates** *(dict) --*

      The collection of response templates for the integration response as a string-to-string map
      of key-value pairs. Response templates are represented as a key/value map, with a
      content-type as the key and a template as the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expressions for the integration response.
    """


_ClientCreateIntegrationResponseTypeDef = TypedDict(
    "_ClientCreateIntegrationResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": str,
        "ContentHandlingStrategy": str,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": str,
        "IntegrationUri": str,
        "PassthroughBehavior": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientCreateIntegrationResponseTypeDef(_ClientCreateIntegrationResponseTypeDef):
    """
    Type definition for `ClientCreateIntegration` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ConnectionId** *(string) --*

      The connection ID.

    - **ConnectionType** *(string) --*

      The type of the network connection to the integration endpoint. Currently the only valid
      value is INTERNET, for connections through the public routable internet.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **CredentialsArn** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on
      supported AWS services, specify null.

    - **Description** *(string) --*

      Represents the description of an integration.

    - **IntegrationId** *(string) --*

      Represents the identifier of an integration.

    - **IntegrationMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **IntegrationResponseSelectionExpression** *(string) --*

      The integration response selection expression for the integration. See `Integration Response
      Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
      .

    - **IntegrationType** *(string) --*

      The integration type of an integration. One of the following:

      AWS: for integrating the route or method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      Lambda proxy integration.

      HTTP: for integrating the route or method request with an HTTP endpoint. This integration is
      also referred to as the HTTP custom integration.

      HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the client
      request passed through as-is. This is also referred to as HTTP proxy integration.

      MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint
      without invoking any backend.

    - **IntegrationUri** *(string) --*

      For a Lambda proxy integration, this is the URI of the Lambda function.

    - **PassthroughBehavior** *(string) --*

      Specifies the pass-through behavior for incoming requests based on the Content-Type header in
      the request, and the available mapping templates specified as the requestTemplates property
      on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES,
      and NEVER.

      WHEN_NO_MATCH passes the request body for unmapped content types through to the integration
      backend without transformation.

      NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

      WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
      templates. However, if there is at least one content type defined, unmapped content types
      will be rejected with the same HTTP 415 Unsupported Media Type response.

    - **RequestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      backend. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the backend. The method request parameter value must match the
      pattern of method.request.{location}.{name} , where {location} is querystring, path, or
      header; and {name} must be a valid and unique method request parameter name.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **RequestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expression for the integration.

    - **TimeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.
    """


_ClientCreateModelResponseTypeDef = TypedDict(
    "_ClientCreateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class ClientCreateModelResponseTypeDef(_ClientCreateModelResponseTypeDef):
    """
    Type definition for `ClientCreateModel` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ContentType** *(string) --*

      The content-type for the model, for example, "application/json".

    - **Description** *(string) --*

      The description of the model.

    - **ModelId** *(string) --*

      The model identifier.

    - **Name** *(string) --*

      The name of the model. Must be alphanumeric.

    - **Schema** *(string) --*

      The schema for the model. For application/json models, this should be JSON schema draft 4
      model.
    """


_ClientCreateRouteRequestParametersTypeDef = TypedDict(
    "_ClientCreateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientCreateRouteRequestParametersTypeDef(
    _ClientCreateRouteRequestParametersTypeDef
):
    """
    Type definition for `ClientCreateRoute` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientCreateRouteResponseResponseParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientCreateRouteResponseResponseParametersTypeDef(
    _ClientCreateRouteResponseResponseParametersTypeDef
):
    """
    Type definition for `ClientCreateRouteResponse` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientCreateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientCreateRouteResponseResponseResponseParametersTypeDef(
    _ClientCreateRouteResponseResponseResponseParametersTypeDef
):
    """
    Type definition for `ClientCreateRouteResponseResponse` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientCreateRouteResponseResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientCreateRouteResponseResponseResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientCreateRouteResponseResponseTypeDef(
    _ClientCreateRouteResponseResponseTypeDef
):
    """
    Type definition for `ClientCreateRouteResponse` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ModelSelectionExpression** *(string) --*

      Represents the model selection expression of a route response.

    - **ResponseModels** *(dict) --*

      Represents the response models of a route response.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **ResponseParameters** *(dict) --*

      Represents the response parameters of a route response.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteResponseId** *(string) --*

      Represents the identifier of a route response.

    - **RouteResponseKey** *(string) --*

      Represents the route response key of a route response.
    """


_ClientCreateRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseRequestParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientCreateRouteResponseRequestParametersTypeDef(
    _ClientCreateRouteResponseRequestParametersTypeDef
):
    """
    Type definition for `ClientCreateRouteResponse` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientCreateRouteResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": str,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[
            str, ClientCreateRouteResponseRequestParametersTypeDef
        ],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class ClientCreateRouteResponseTypeDef(_ClientCreateRouteResponseTypeDef):
    """
    Type definition for `ClientCreateRoute` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **ApiKeyRequired** *(boolean) --*

      Specifies whether an API key is required for this route.

    - **AuthorizationScopes** *(list) --*

      A list of authorization scopes configured on a route. The scopes are used with a
      COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by
      matching the route scopes against the scopes parsed from the access token in the incoming
      request. The method invocation is authorized if any route scope matches a claimed scope in
      the access token. Otherwise, the invocation is not authorized. When the route scope is
      configured, the client must provide an access token instead of an identity token for
      authorization purposes.

      - *(string) --*

        A string with a length between [1-64].

    - **AuthorizationType** *(string) --*

      The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
      using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

    - **AuthorizerId** *(string) --*

      The identifier of the Authorizer resource to be associated with this route, if the
      authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when you
      created the authorizer.

    - **ModelSelectionExpression** *(string) --*

      The model selection expression for the route.

    - **OperationName** *(string) --*

      The operation name for the route.

    - **RequestModels** *(dict) --*

      The request models for the route.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **RequestParameters** *(dict) --*

      The request parameters for the route.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteId** *(string) --*

      The route ID.

    - **RouteKey** *(string) --*

      The route key for the route.

    - **RouteResponseSelectionExpression** *(string) --*

      The route response selection expression for the route.

    - **Target** *(string) --*

      The target for the route.
    """


_ClientCreateStageAccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientCreateStageAccessLogSettingsTypeDef(
    _ClientCreateStageAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientCreateStage` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context variables.
      The format must include at least $context.requestId.
    """


_ClientCreateStageDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageDefaultRouteSettingsTypeDef(
    _ClientCreateStageDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientCreateStage` `DefaultRouteSettings`

    The default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log
      entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientCreateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientCreateStageResponseAccessLogSettingsTypeDef(
    _ClientCreateStageResponseAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context
      variables. The format must include at least $context.requestId.
    """


_ClientCreateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageResponseDefaultRouteSettingsTypeDef(
    _ClientCreateStageResponseDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `DefaultRouteSettings`

    Default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
      log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientCreateStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageResponseRouteSettingsTypeDef(
    _ClientCreateStageResponseRouteSettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route.
      This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
      the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientCreateStageResponseTypeDef = TypedDict(
    "_ClientCreateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientCreateStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientCreateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientCreateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateStageResponseTypeDef(_ClientCreateStageResponseTypeDef):
    """
    Type definition for `ClientCreateStage` `Response`

    The request has succeeded and has resulted in the creation of a resource.

    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

      - **Format** *(string) --*

        A single line format of the access logs of data, as specified by selected $context
        variables. The format must include at least $context.requestId.

    - **ClientCertificateId** *(string) --*

      The identifier of a client certificate for a Stage.

    - **CreatedDate** *(datetime) --*

      The timestamp when the stage was created.

    - **DefaultRouteSettings** *(dict) --*

      Default route settings for the stage.

      - **DataTraceEnabled** *(boolean) --*

        Specifies whether (true) or not (false) data trace logging is enabled for this route. This
        property affects the log entries pushed to Amazon CloudWatch Logs.

      - **DetailedMetricsEnabled** *(boolean) --*

        Specifies whether detailed metrics are enabled.

      - **LoggingLevel** *(string) --*

        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
        log entries pushed to Amazon CloudWatch Logs.

      - **ThrottlingBurstLimit** *(integer) --*

        Specifies the throttling burst limit.

      - **ThrottlingRateLimit** *(float) --*

        Specifies the throttling rate limit.

    - **DeploymentId** *(string) --*

      The identifier of the Deployment that the Stage is associated with.

    - **Description** *(string) --*

      The description of the stage.

    - **LastUpdatedDate** *(datetime) --*

      The timestamp when the stage was last updated.

    - **RouteSettings** *(dict) --*

      Route settings for the stage.

      - *(string) --*

        - *(dict) --*

          Represents a collection of route settings.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this route.
            This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
            the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

    - **StageName** *(string) --*

      The name of the stage.

    - **StageVariables** *(dict) --*

      A map that defines the stage variables for a stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-2048].

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientCreateStageRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageRouteSettingsTypeDef(_ClientCreateStageRouteSettingsTypeDef):
    """
    Type definition for `ClientCreateStage` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
      log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientGetApiMappingResponseTypeDef = TypedDict(
    "_ClientGetApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientGetApiMappingResponseTypeDef(_ClientGetApiMappingResponseTypeDef):
    """
    Type definition for `ClientGetApiMapping` `Response`

    Success

    - **ApiId** *(string) --*

      The API identifier.

    - **ApiMappingId** *(string) --*

      The API mapping identifier.

    - **ApiMappingKey** *(string) --*

      The API mapping key.

    - **Stage** *(string) --*

      The API stage.
    """


_ClientGetApiMappingsResponseItemsTypeDef = TypedDict(
    "_ClientGetApiMappingsResponseItemsTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientGetApiMappingsResponseItemsTypeDef(
    _ClientGetApiMappingsResponseItemsTypeDef
):
    """
    Type definition for `ClientGetApiMappingsResponse` `Items`

    Represents an API mapping.

    - **ApiId** *(string) --*

      The API identifier.

    - **ApiMappingId** *(string) --*

      The API mapping identifier.

    - **ApiMappingKey** *(string) --*

      The API mapping key.

    - **Stage** *(string) --*

      The API stage.
    """


_ClientGetApiMappingsResponseTypeDef = TypedDict(
    "_ClientGetApiMappingsResponseTypeDef",
    {"Items": List[ClientGetApiMappingsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetApiMappingsResponseTypeDef(_ClientGetApiMappingsResponseTypeDef):
    """
    Type definition for `ClientGetApiMappings` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an API mapping.

        - **ApiId** *(string) --*

          The API identifier.

        - **ApiMappingId** *(string) --*

          The API mapping identifier.

        - **ApiMappingKey** *(string) --*

          The API mapping key.

        - **Stage** *(string) --*

          The API stage.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetApiResponseTypeDef = TypedDict(
    "_ClientGetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiResponseTypeDef(_ClientGetApiResponseTypeDef):
    """
    Type definition for `ClientGetApi` `Response`

    Success

    - **ApiEndpoint** *(string) --*

      The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
      is typically appended to this URI to form a complete path to a deployed API stage.

    - **ApiId** *(string) --*

      The API ID.

    - **ApiKeySelectionExpression** *(string) --*

      An API key selection expression. See `API Key Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
      .

    - **CreatedDate** *(datetime) --*

      The timestamp when the API was created.

    - **Description** *(string) --*

      The description of the API.

    - **DisableSchemaValidation** *(boolean) --*

      Avoid validating models when creating a deployment.

    - **Name** *(string) --*

      The name of the API.

    - **ProtocolType** *(string) --*

      The API protocol: Currently only WEBSOCKET is supported.

    - **RouteSelectionExpression** *(string) --*

      The route selection expression for the API.

    - **Version** *(string) --*

      A version identifier for the API.

    - **Warnings** *(list) --*

      The warning messages reported when failonwarnings is turned on during API import.

      - *(string) --*

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetApisResponseItemsTypeDef = TypedDict(
    "_ClientGetApisResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApisResponseItemsTypeDef(_ClientGetApisResponseItemsTypeDef):
    """
    Type definition for `ClientGetApisResponse` `Items`

    Represents an API.

    - **ApiEndpoint** *(string) --*

      The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
      name is typically appended to this URI to form a complete path to a deployed API stage.

    - **ApiId** *(string) --*

      The API ID.

    - **ApiKeySelectionExpression** *(string) --*

      An API key selection expression. See `API Key Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
      .

    - **CreatedDate** *(datetime) --*

      The timestamp when the API was created.

    - **Description** *(string) --*

      The description of the API.

    - **DisableSchemaValidation** *(boolean) --*

      Avoid validating models when creating a deployment.

    - **Name** *(string) --*

      The name of the API.

    - **ProtocolType** *(string) --*

      The API protocol: Currently only WEBSOCKET is supported.

    - **RouteSelectionExpression** *(string) --*

      The route selection expression for the API.

    - **Version** *(string) --*

      A version identifier for the API.

    - **Warnings** *(list) --*

      The warning messages reported when failonwarnings is turned on during API import.

      - *(string) --*

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetApisResponseTypeDef = TypedDict(
    "_ClientGetApisResponseTypeDef",
    {"Items": List[ClientGetApisResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetApisResponseTypeDef(_ClientGetApisResponseTypeDef):
    """
    Type definition for `ClientGetApis` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an API.

        - **ApiEndpoint** *(string) --*

          The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
          name is typically appended to this URI to form a complete path to a deployed API stage.

        - **ApiId** *(string) --*

          The API ID.

        - **ApiKeySelectionExpression** *(string) --*

          An API key selection expression. See `API Key Selection Expressions
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
          .

        - **CreatedDate** *(datetime) --*

          The timestamp when the API was created.

        - **Description** *(string) --*

          The description of the API.

        - **DisableSchemaValidation** *(boolean) --*

          Avoid validating models when creating a deployment.

        - **Name** *(string) --*

          The name of the API.

        - **ProtocolType** *(string) --*

          The API protocol: Currently only WEBSOCKET is supported.

        - **RouteSelectionExpression** *(string) --*

          The route selection expression for the API.

        - **Version** *(string) --*

          A version identifier for the API.

        - **Warnings** *(list) --*

          The warning messages reported when failonwarnings is turned on during API import.

          - *(string) --*

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetAuthorizerResponseTypeDef = TypedDict(
    "_ClientGetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientGetAuthorizerResponseTypeDef(_ClientGetAuthorizerResponseTypeDef):
    """
    Type definition for `ClientGetAuthorizer` `Response`

    Success

    - **AuthorizerCredentialsArn** *(string) --*

      Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
      To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
      To use resource-based permissions on the Lambda function, specify null.

    - **AuthorizerId** *(string) --*

      The authorizer identifier.

    - **AuthorizerResultTtlInSeconds** *(integer) --*

      The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
      authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer
      responses. If this field is not set, the default value is 300. The maximum value is 3600, or
      1 hour.

    - **AuthorizerType** *(string) --*

      The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using
      incoming request parameters.

    - **AuthorizerUri** *(string) --*

      The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a
      well-formed Lambda function URI, for example,
      arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
      In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} ,
      where {region} is the same as the region hosting the Lambda function, path indicates that the
      remaining substring in the URI should be treated as the path to the resource, including the
      initial /. For Lambda functions, this is usually of the form
      /2015-03-31/functions/[FunctionARN]/invocations.

    - **IdentitySource** *(list) --*

      The identity source for which authorization is requested.

      For the REQUEST authorizer, this is required when authorization caching is enabled. The value
      is a comma-separated string of one or more mapping expressions of the specified request
      parameters. For example, if an Auth header and a Name query string parameters are defined as
      identity sources, this value is method.request.header.Auth, method.request.querystring.Name.
      These parameters will be used to derive the authorization caching key and to perform runtime
      validation of the REQUEST authorizer by verifying all of the identity-related request
      parameters are present, not null, and non-empty. Only when this is true does the authorizer
      invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response
      without calling the Lambda function. The valid value is a string of comma-separated mapping
      expressions of the specified request parameters. When the authorization caching is not
      enabled, this property is optional.

      - *(string) --*

    - **IdentityValidationExpression** *(string) --*

      The validation expression does not apply to the REQUEST authorizer.

    - **Name** *(string) --*

      The name of the authorizer.

    - **ProviderArns** *(list) --*

      For REQUEST authorizer, this is not defined.

      - *(string) --*

        Represents an Amazon Resource Name (ARN).
    """


_ClientGetAuthorizersResponseItemsTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientGetAuthorizersResponseItemsTypeDef(
    _ClientGetAuthorizersResponseItemsTypeDef
):
    """
    Type definition for `ClientGetAuthorizersResponse` `Items`

    Represents an authorizer.

    - **AuthorizerCredentialsArn** *(string) --*

      Specifies the required credentials as an IAM role for API Gateway to invoke the
      authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
      Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
      null.

    - **AuthorizerId** *(string) --*

      The authorizer identifier.

    - **AuthorizerResultTtlInSeconds** *(integer) --*

      The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
      authorization caching is disabled. If it is greater than 0, API Gateway will cache
      authorizer responses. If this field is not set, the default value is 300. The maximum
      value is 3600, or 1 hour.

    - **AuthorizerType** *(string) --*

      The authorizer type. Currently the only valid value is REQUEST, for a Lambda function
      using incoming request parameters.

    - **AuthorizerUri** *(string) --*

      The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be
      a well-formed Lambda function URI, for example,
      arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
      In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}
      , where {region} is the same as the region hosting the Lambda function, path indicates
      that the remaining substring in the URI should be treated as the path to the resource,
      including the initial /. For Lambda functions, this is usually of the form
      /2015-03-31/functions/[FunctionARN]/invocations.

    - **IdentitySource** *(list) --*

      The identity source for which authorization is requested.

      For the REQUEST authorizer, this is required when authorization caching is enabled. The
      value is a comma-separated string of one or more mapping expressions of the specified
      request parameters. For example, if an Auth header and a Name query string parameters are
      defined as identity sources, this value is method.request.header.Auth,
      method.request.querystring.Name. These parameters will be used to derive the
      authorization caching key and to perform runtime validation of the REQUEST authorizer by
      verifying all of the identity-related request parameters are present, not null, and
      non-empty. Only when this is true does the authorizer invoke the authorizer Lambda
      function, otherwise, it returns a 401 Unauthorized response without calling the Lambda
      function. The valid value is a string of comma-separated mapping expressions of the
      specified request parameters. When the authorization caching is not enabled, this
      property is optional.

      - *(string) --*

    - **IdentityValidationExpression** *(string) --*

      The validation expression does not apply to the REQUEST authorizer.

    - **Name** *(string) --*

      The name of the authorizer.

    - **ProviderArns** *(list) --*

      For REQUEST authorizer, this is not defined.

      - *(string) --*

        Represents an Amazon Resource Name (ARN).
    """


_ClientGetAuthorizersResponseTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseTypeDef",
    {"Items": List[ClientGetAuthorizersResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetAuthorizersResponseTypeDef(_ClientGetAuthorizersResponseTypeDef):
    """
    Type definition for `ClientGetAuthorizers` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an authorizer.

        - **AuthorizerCredentialsArn** *(string) --*

          Specifies the required credentials as an IAM role for API Gateway to invoke the
          authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
          Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
          null.

        - **AuthorizerId** *(string) --*

          The authorizer identifier.

        - **AuthorizerResultTtlInSeconds** *(integer) --*

          The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
          authorization caching is disabled. If it is greater than 0, API Gateway will cache
          authorizer responses. If this field is not set, the default value is 300. The maximum
          value is 3600, or 1 hour.

        - **AuthorizerType** *(string) --*

          The authorizer type. Currently the only valid value is REQUEST, for a Lambda function
          using incoming request parameters.

        - **AuthorizerUri** *(string) --*

          The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be
          a well-formed Lambda function URI, for example,
          arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
          In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}
          , where {region} is the same as the region hosting the Lambda function, path indicates
          that the remaining substring in the URI should be treated as the path to the resource,
          including the initial /. For Lambda functions, this is usually of the form
          /2015-03-31/functions/[FunctionARN]/invocations.

        - **IdentitySource** *(list) --*

          The identity source for which authorization is requested.

          For the REQUEST authorizer, this is required when authorization caching is enabled. The
          value is a comma-separated string of one or more mapping expressions of the specified
          request parameters. For example, if an Auth header and a Name query string parameters are
          defined as identity sources, this value is method.request.header.Auth,
          method.request.querystring.Name. These parameters will be used to derive the
          authorization caching key and to perform runtime validation of the REQUEST authorizer by
          verifying all of the identity-related request parameters are present, not null, and
          non-empty. Only when this is true does the authorizer invoke the authorizer Lambda
          function, otherwise, it returns a 401 Unauthorized response without calling the Lambda
          function. The valid value is a string of comma-separated mapping expressions of the
          specified request parameters. When the authorization caching is not enabled, this
          property is optional.

          - *(string) --*

        - **IdentityValidationExpression** *(string) --*

          The validation expression does not apply to the REQUEST authorizer.

        - **Name** *(string) --*

          The name of the authorizer.

        - **ProviderArns** *(list) --*

          For REQUEST authorizer, this is not defined.

          - *(string) --*

            Represents an Amazon Resource Name (ARN).

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    Type definition for `ClientGetDeployment` `Response`

    Success

    - **CreatedDate** *(datetime) --*

      The date and time when the Deployment resource was created.

    - **DeploymentId** *(string) --*

      The identifier for the deployment.

    - **DeploymentStatus** *(string) --*

      The status of the deployment: PENDING, FAILED, or SUCCEEDED.

    - **DeploymentStatusMessage** *(string) --*

      May contain additional feedback on the status of an API deployment.

    - **Description** *(string) --*

      The description for the deployment.
    """


_ClientGetDeploymentsResponseItemsTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseItemsTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientGetDeploymentsResponseItemsTypeDef(
    _ClientGetDeploymentsResponseItemsTypeDef
):
    """
    Type definition for `ClientGetDeploymentsResponse` `Items`

    An immutable representation of an API that can be called by users. A Deployment must be
    associated with a Stage for it to be callable over the internet.

    - **CreatedDate** *(datetime) --*

      The date and time when the Deployment resource was created.

    - **DeploymentId** *(string) --*

      The identifier for the deployment.

    - **DeploymentStatus** *(string) --*

      The status of the deployment: PENDING, FAILED, or SUCCEEDED.

    - **DeploymentStatusMessage** *(string) --*

      May contain additional feedback on the status of an API deployment.

    - **Description** *(string) --*

      The description for the deployment.
    """


_ClientGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseTypeDef",
    {"Items": List[ClientGetDeploymentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDeploymentsResponseTypeDef(_ClientGetDeploymentsResponseTypeDef):
    """
    Type definition for `ClientGetDeployments` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        An immutable representation of an API that can be called by users. A Deployment must be
        associated with a Stage for it to be callable over the internet.

        - **CreatedDate** *(datetime) --*

          The date and time when the Deployment resource was created.

        - **DeploymentId** *(string) --*

          The identifier for the deployment.

        - **DeploymentStatus** *(string) --*

          The status of the deployment: PENDING, FAILED, or SUCCEEDED.

        - **DeploymentStatusMessage** *(string) --*

          May contain additional feedback on the status of an API deployment.

        - **Description** *(string) --*

          The description for the deployment.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientGetDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientGetDomainNameResponseDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientGetDomainNameResponse` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this
      domain name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized
      endpoint for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this
      domain name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain name.
      The valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
      the status is UPDATING, the domain cannot be modified further until the existing
      operation is complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain name
      migration.
    """


_ClientGetDomainNameResponseTypeDef = TypedDict(
    "_ClientGetDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainNameResponseTypeDef(_ClientGetDomainNameResponseTypeDef):
    """
    Type definition for `ClientGetDomainName` `Response`

    Success

    - **ApiMappingSelectionExpression** *(string) --*

      The API mapping selection expression.

    - **DomainName** *(string) --*

      The name of the DomainName resource.

    - **DomainNameConfigurations** *(list) --*

      The domain name configurations.

      - *(dict) --*

        The domain name configuration.

        - **ApiGatewayDomainName** *(string) --*

          A domain name for the WebSocket API.

        - **CertificateArn** *(string) --*

          An AWS-managed certificate that will be used by the edge-optimized endpoint for this
          domain name. AWS Certificate Manager is the only supported source.

        - **CertificateName** *(string) --*

          The user-friendly name of the certificate that will be used by the edge-optimized
          endpoint for this domain name.

        - **CertificateUploadDate** *(datetime) --*

          The timestamp when the certificate that was used by edge-optimized endpoint for this
          domain name was uploaded.

        - **EndpointType** *(string) --*

          The endpoint type.

        - **HostedZoneId** *(string) --*

          The Amazon Route 53 Hosted Zone ID of the endpoint.

        - **SecurityPolicy** *(string) --*

          The Transport Layer Security (TLS) version of the security policy for this domain name.
          The valid values are TLS_1_0 and TLS_1_2.

        - **DomainNameStatus** *(string) --*

          The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
          the status is UPDATING, the domain cannot be modified further until the existing
          operation is complete. If it is AVAILABLE, the domain can be updated.

        - **DomainNameStatusMessage** *(string) --*

          An optional text message containing detailed information about status of the domain name
          migration.

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef(
    _ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientGetDomainNamesResponseItems` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this
      domain name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized
      endpoint for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this
      domain name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain
      name. The valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
      If the status is UPDATING, the domain cannot be modified further until the existing
      operation is complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain
      name migration.
    """


_ClientGetDomainNamesResponseItemsTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseItemsTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainNamesResponseItemsTypeDef(
    _ClientGetDomainNamesResponseItemsTypeDef
):
    """
    Type definition for `ClientGetDomainNamesResponse` `Items`

    Represents a domain name.

    - **ApiMappingSelectionExpression** *(string) --*

      The API mapping selection expression.

    - **DomainName** *(string) --*

      The name of the DomainName resource.

    - **DomainNameConfigurations** *(list) --*

      The domain name configurations.

      - *(dict) --*

        The domain name configuration.

        - **ApiGatewayDomainName** *(string) --*

          A domain name for the WebSocket API.

        - **CertificateArn** *(string) --*

          An AWS-managed certificate that will be used by the edge-optimized endpoint for this
          domain name. AWS Certificate Manager is the only supported source.

        - **CertificateName** *(string) --*

          The user-friendly name of the certificate that will be used by the edge-optimized
          endpoint for this domain name.

        - **CertificateUploadDate** *(datetime) --*

          The timestamp when the certificate that was used by edge-optimized endpoint for this
          domain name was uploaded.

        - **EndpointType** *(string) --*

          The endpoint type.

        - **HostedZoneId** *(string) --*

          The Amazon Route 53 Hosted Zone ID of the endpoint.

        - **SecurityPolicy** *(string) --*

          The Transport Layer Security (TLS) version of the security policy for this domain
          name. The valid values are TLS_1_0 and TLS_1_2.

        - **DomainNameStatus** *(string) --*

          The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
          If the status is UPDATING, the domain cannot be modified further until the existing
          operation is complete. If it is AVAILABLE, the domain can be updated.

        - **DomainNameStatusMessage** *(string) --*

          An optional text message containing detailed information about status of the domain
          name migration.

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetDomainNamesResponseTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseTypeDef",
    {"Items": List[ClientGetDomainNamesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDomainNamesResponseTypeDef(_ClientGetDomainNamesResponseTypeDef):
    """
    Type definition for `ClientGetDomainNames` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a domain name.

        - **ApiMappingSelectionExpression** *(string) --*

          The API mapping selection expression.

        - **DomainName** *(string) --*

          The name of the DomainName resource.

        - **DomainNameConfigurations** *(list) --*

          The domain name configurations.

          - *(dict) --*

            The domain name configuration.

            - **ApiGatewayDomainName** *(string) --*

              A domain name for the WebSocket API.

            - **CertificateArn** *(string) --*

              An AWS-managed certificate that will be used by the edge-optimized endpoint for this
              domain name. AWS Certificate Manager is the only supported source.

            - **CertificateName** *(string) --*

              The user-friendly name of the certificate that will be used by the edge-optimized
              endpoint for this domain name.

            - **CertificateUploadDate** *(datetime) --*

              The timestamp when the certificate that was used by edge-optimized endpoint for this
              domain name was uploaded.

            - **EndpointType** *(string) --*

              The endpoint type.

            - **HostedZoneId** *(string) --*

              The Amazon Route 53 Hosted Zone ID of the endpoint.

            - **SecurityPolicy** *(string) --*

              The Transport Layer Security (TLS) version of the security policy for this domain
              name. The valid values are TLS_1_0 and TLS_1_2.

            - **DomainNameStatus** *(string) --*

              The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
              If the status is UPDATING, the domain cannot be modified further until the existing
              operation is complete. If it is AVAILABLE, the domain can be updated.

            - **DomainNameStatusMessage** *(string) --*

              An optional text message containing detailed information about status of the domain
              name migration.

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": str,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class ClientGetIntegrationResponseResponseTypeDef(
    _ClientGetIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientGetIntegrationResponse` `Response`

    Success

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **IntegrationResponseId** *(string) --*

      The integration response ID.

    - **IntegrationResponseKey** *(string) --*

      The integration response key.

    - **ResponseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the backend. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of method.response.header.{name}, where name is a valid and unique header name. The mapped
      non-static value must match the pattern of integration.response.header.{name} or
      integration.response.body.{JSON-expression}, where name is a valid and unique response header
      name and JSON-expression is a valid JSON expression without the $ prefix.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **ResponseTemplates** *(dict) --*

      The collection of response templates for the integration response as a string-to-string map
      of key-value pairs. Response templates are represented as a key/value map, with a
      content-type as the key and a template as the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expressions for the integration response.
    """


_ClientGetIntegrationResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": str,
        "ContentHandlingStrategy": str,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": str,
        "IntegrationUri": str,
        "PassthroughBehavior": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientGetIntegrationResponseTypeDef(_ClientGetIntegrationResponseTypeDef):
    """
    Type definition for `ClientGetIntegration` `Response`

    Success

    - **ConnectionId** *(string) --*

      The connection ID.

    - **ConnectionType** *(string) --*

      The type of the network connection to the integration endpoint. Currently the only valid
      value is INTERNET, for connections through the public routable internet.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **CredentialsArn** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on
      supported AWS services, specify null.

    - **Description** *(string) --*

      Represents the description of an integration.

    - **IntegrationId** *(string) --*

      Represents the identifier of an integration.

    - **IntegrationMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **IntegrationResponseSelectionExpression** *(string) --*

      The integration response selection expression for the integration. See `Integration Response
      Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
      .

    - **IntegrationType** *(string) --*

      The integration type of an integration. One of the following:

      AWS: for integrating the route or method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      Lambda proxy integration.

      HTTP: for integrating the route or method request with an HTTP endpoint. This integration is
      also referred to as the HTTP custom integration.

      HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the client
      request passed through as-is. This is also referred to as HTTP proxy integration.

      MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint
      without invoking any backend.

    - **IntegrationUri** *(string) --*

      For a Lambda proxy integration, this is the URI of the Lambda function.

    - **PassthroughBehavior** *(string) --*

      Specifies the pass-through behavior for incoming requests based on the Content-Type header in
      the request, and the available mapping templates specified as the requestTemplates property
      on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES,
      and NEVER.

      WHEN_NO_MATCH passes the request body for unmapped content types through to the integration
      backend without transformation.

      NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

      WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
      templates. However, if there is at least one content type defined, unmapped content types
      will be rejected with the same HTTP 415 Unsupported Media Type response.

    - **RequestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      backend. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the backend. The method request parameter value must match the
      pattern of method.request.{location}.{name} , where {location} is querystring, path, or
      header; and {name} must be a valid and unique method request parameter name.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **RequestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expression for the integration.

    - **TimeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.
    """


_ClientGetIntegrationResponsesResponseItemsTypeDef = TypedDict(
    "_ClientGetIntegrationResponsesResponseItemsTypeDef",
    {
        "ContentHandlingStrategy": str,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class ClientGetIntegrationResponsesResponseItemsTypeDef(
    _ClientGetIntegrationResponsesResponseItemsTypeDef
):
    """
    Type definition for `ClientGetIntegrationResponsesResponse` `Items`

    Represents an integration response.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **IntegrationResponseId** *(string) --*

      The integration response ID.

    - **IntegrationResponseKey** *(string) --*

      The integration response key.

    - **ResponseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response
      from the backend. The key is a method response header parameter name and the mapped value
      is an integration response header value, a static value enclosed within a pair of single
      quotes, or a JSON expression from the integration response body. The mapping key must
      match the pattern of method.response.header.{name}, where name is a valid and unique
      header name. The mapped non-static value must match the pattern of
      integration.response.header.{name} or integration.response.body.{JSON-expression}, where
      name is a valid and unique response header name and JSON-expression is a valid JSON
      expression without the $ prefix.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **ResponseTemplates** *(dict) --*

      The collection of response templates for the integration response as a string-to-string
      map of key-value pairs. Response templates are represented as a key/value map, with a
      content-type as the key and a template as the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expressions for the integration response.
    """


_ClientGetIntegrationResponsesResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponsesResponseTypeDef",
    {
        "Items": List[ClientGetIntegrationResponsesResponseItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetIntegrationResponsesResponseTypeDef(
    _ClientGetIntegrationResponsesResponseTypeDef
):
    """
    Type definition for `ClientGetIntegrationResponses` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an integration response.

        - **ContentHandlingStrategy** *(string) --*

          Specifies how to handle response payload content type conversions. Supported values are
          CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
          corresponding binary blob.

          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
          string.

          If this property is not defined, the response payload will be passed through from the
          integration response to the route response or method response without modification.

        - **IntegrationResponseId** *(string) --*

          The integration response ID.

        - **IntegrationResponseKey** *(string) --*

          The integration response key.

        - **ResponseParameters** *(dict) --*

          A key-value map specifying response parameters that are passed to the method response
          from the backend. The key is a method response header parameter name and the mapped value
          is an integration response header value, a static value enclosed within a pair of single
          quotes, or a JSON expression from the integration response body. The mapping key must
          match the pattern of method.response.header.{name}, where name is a valid and unique
          header name. The mapped non-static value must match the pattern of
          integration.response.header.{name} or integration.response.body.{JSON-expression}, where
          name is a valid and unique response header name and JSON-expression is a valid JSON
          expression without the $ prefix.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-512].

        - **ResponseTemplates** *(dict) --*

          The collection of response templates for the integration response as a string-to-string
          map of key-value pairs. Response templates are represented as a key/value map, with a
          content-type as the key and a template as the value.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-32768].

        - **TemplateSelectionExpression** *(string) --*

          The template selection expressions for the integration response.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetIntegrationsResponseItemsTypeDef = TypedDict(
    "_ClientGetIntegrationsResponseItemsTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": str,
        "ContentHandlingStrategy": str,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": str,
        "IntegrationUri": str,
        "PassthroughBehavior": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientGetIntegrationsResponseItemsTypeDef(
    _ClientGetIntegrationsResponseItemsTypeDef
):
    """
    Type definition for `ClientGetIntegrationsResponse` `Items`

    Represents an integration.

    - **ConnectionId** *(string) --*

      The connection ID.

    - **ConnectionType** *(string) --*

      The type of the network connection to the integration endpoint. Currently the only valid
      value is INTERNET, for connections through the public routable internet.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **CredentialsArn** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations,
      three options are available. To specify an IAM Role for API Gateway to assume, use the
      role's Amazon Resource Name (ARN). To require that the caller's identity be passed
      through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based
      permissions on supported AWS services, specify null.

    - **Description** *(string) --*

      Represents the description of an integration.

    - **IntegrationId** *(string) --*

      Represents the identifier of an integration.

    - **IntegrationMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **IntegrationResponseSelectionExpression** *(string) --*

      The integration response selection expression for the integration. See `Integration
      Response Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
      .

    - **IntegrationType** *(string) --*

      The integration type of an integration. One of the following:

      AWS: for integrating the route or method request with an AWS service action, including
      the Lambda function-invoking action. With the Lambda function-invoking action, this is
      referred to as the Lambda custom integration. With any other AWS service action, this is
      known as AWS integration.

      AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to
      as Lambda proxy integration.

      HTTP: for integrating the route or method request with an HTTP endpoint. This integration
      is also referred to as the HTTP custom integration.

      HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the
      client request passed through as-is. This is also referred to as HTTP proxy integration.

      MOCK: for integrating the route or method request with API Gateway as a "loopback"
      endpoint without invoking any backend.

    - **IntegrationUri** *(string) --*

      For a Lambda proxy integration, this is the URI of the Lambda function.

    - **PassthroughBehavior** *(string) --*

      Specifies the pass-through behavior for incoming requests based on the Content-Type
      header in the request, and the available mapping templates specified as the
      requestTemplates property on the Integration resource. There are three valid values:
      WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.

      WHEN_NO_MATCH passes the request body for unmapped content types through to the
      integration backend without transformation.

      NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

      WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
      templates. However, if there is at least one content type defined, unmapped content types
      will be rejected with the same HTTP 415 Unsupported Media Type response.

    - **RequestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to
      the backend. The key is an integration request parameter name and the associated value is
      a method request parameter value or static value that must be enclosed within single
      quotes and pre-encoded as required by the backend. The method request parameter value
      must match the pattern of method.request.{location}.{name} , where {location} is
      querystring, path, or header; and {name} must be a valid and unique method request
      parameter name.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **RequestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on
      the value of the Content-Type header sent by the client. The content type value is the
      key in this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expression for the integration.

    - **TimeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000
      milliseconds or 29 seconds.
    """


_ClientGetIntegrationsResponseTypeDef = TypedDict(
    "_ClientGetIntegrationsResponseTypeDef",
    {"Items": List[ClientGetIntegrationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetIntegrationsResponseTypeDef(_ClientGetIntegrationsResponseTypeDef):
    """
    Type definition for `ClientGetIntegrations` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an integration.

        - **ConnectionId** *(string) --*

          The connection ID.

        - **ConnectionType** *(string) --*

          The type of the network connection to the integration endpoint. Currently the only valid
          value is INTERNET, for connections through the public routable internet.

        - **ContentHandlingStrategy** *(string) --*

          Specifies how to handle response payload content type conversions. Supported values are
          CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
          corresponding binary blob.

          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
          string.

          If this property is not defined, the response payload will be passed through from the
          integration response to the route response or method response without modification.

        - **CredentialsArn** *(string) --*

          Specifies the credentials required for the integration, if any. For AWS integrations,
          three options are available. To specify an IAM Role for API Gateway to assume, use the
          role's Amazon Resource Name (ARN). To require that the caller's identity be passed
          through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based
          permissions on supported AWS services, specify null.

        - **Description** *(string) --*

          Represents the description of an integration.

        - **IntegrationId** *(string) --*

          Represents the identifier of an integration.

        - **IntegrationMethod** *(string) --*

          Specifies the integration's HTTP method type.

        - **IntegrationResponseSelectionExpression** *(string) --*

          The integration response selection expression for the integration. See `Integration
          Response Selection Expressions
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
          .

        - **IntegrationType** *(string) --*

          The integration type of an integration. One of the following:

          AWS: for integrating the route or method request with an AWS service action, including
          the Lambda function-invoking action. With the Lambda function-invoking action, this is
          referred to as the Lambda custom integration. With any other AWS service action, this is
          known as AWS integration.

          AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
          action with the client request passed through as-is. This integration is also referred to
          as Lambda proxy integration.

          HTTP: for integrating the route or method request with an HTTP endpoint. This integration
          is also referred to as the HTTP custom integration.

          HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the
          client request passed through as-is. This is also referred to as HTTP proxy integration.

          MOCK: for integrating the route or method request with API Gateway as a "loopback"
          endpoint without invoking any backend.

        - **IntegrationUri** *(string) --*

          For a Lambda proxy integration, this is the URI of the Lambda function.

        - **PassthroughBehavior** *(string) --*

          Specifies the pass-through behavior for incoming requests based on the Content-Type
          header in the request, and the available mapping templates specified as the
          requestTemplates property on the Integration resource. There are three valid values:
          WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.

          WHEN_NO_MATCH passes the request body for unmapped content types through to the
          integration backend without transformation.

          NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

          WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
          templates. However, if there is at least one content type defined, unmapped content types
          will be rejected with the same HTTP 415 Unsupported Media Type response.

        - **RequestParameters** *(dict) --*

          A key-value map specifying request parameters that are passed from the method request to
          the backend. The key is an integration request parameter name and the associated value is
          a method request parameter value or static value that must be enclosed within single
          quotes and pre-encoded as required by the backend. The method request parameter value
          must match the pattern of method.request.{location}.{name} , where {location} is
          querystring, path, or header; and {name} must be a valid and unique method request
          parameter name.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-512].

        - **RequestTemplates** *(dict) --*

          Represents a map of Velocity templates that are applied on the request payload based on
          the value of the Content-Type header sent by the client. The content type value is the
          key in this map, and the template (as a String) is the value.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-32768].

        - **TemplateSelectionExpression** *(string) --*

          The template selection expression for the integration.

        - **TimeoutInMillis** *(integer) --*

          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000
          milliseconds or 29 seconds.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetModelResponseTypeDef = TypedDict(
    "_ClientGetModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class ClientGetModelResponseTypeDef(_ClientGetModelResponseTypeDef):
    """
    Type definition for `ClientGetModel` `Response`

    Success

    - **ContentType** *(string) --*

      The content-type for the model, for example, "application/json".

    - **Description** *(string) --*

      The description of the model.

    - **ModelId** *(string) --*

      The model identifier.

    - **Name** *(string) --*

      The name of the model. Must be alphanumeric.

    - **Schema** *(string) --*

      The schema for the model. For application/json models, this should be JSON schema draft 4
      model.
    """


_ClientGetModelTemplateResponseTypeDef = TypedDict(
    "_ClientGetModelTemplateResponseTypeDef", {"Value": str}, total=False
)


class ClientGetModelTemplateResponseTypeDef(_ClientGetModelTemplateResponseTypeDef):
    """
    Type definition for `ClientGetModelTemplate` `Response`

    Success

    - **Value** *(string) --*

      The template value.
    """


_ClientGetModelsResponseItemsTypeDef = TypedDict(
    "_ClientGetModelsResponseItemsTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class ClientGetModelsResponseItemsTypeDef(_ClientGetModelsResponseItemsTypeDef):
    """
    Type definition for `ClientGetModelsResponse` `Items`

    Represents a data model for an API. See `Create Models and Mapping Templates for Request
    and Response Mappings
    <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .

    - **ContentType** *(string) --*

      The content-type for the model, for example, "application/json".

    - **Description** *(string) --*

      The description of the model.

    - **ModelId** *(string) --*

      The model identifier.

    - **Name** *(string) --*

      The name of the model. Must be alphanumeric.

    - **Schema** *(string) --*

      The schema for the model. For application/json models, this should be JSON schema draft 4
      model.
    """


_ClientGetModelsResponseTypeDef = TypedDict(
    "_ClientGetModelsResponseTypeDef",
    {"Items": List[ClientGetModelsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetModelsResponseTypeDef(_ClientGetModelsResponseTypeDef):
    """
    Type definition for `ClientGetModels` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a data model for an API. See `Create Models and Mapping Templates for Request
        and Response Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .

        - **ContentType** *(string) --*

          The content-type for the model, for example, "application/json".

        - **Description** *(string) --*

          The description of the model.

        - **ModelId** *(string) --*

          The model identifier.

        - **Name** *(string) --*

          The name of the model. Must be alphanumeric.

        - **Schema** *(string) --*

          The schema for the model. For application/json models, this should be JSON schema draft 4
          model.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientGetRouteResponseResponseResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientGetRouteResponseResponseResponseParametersTypeDef(
    _ClientGetRouteResponseResponseResponseParametersTypeDef
):
    """
    Type definition for `ClientGetRouteResponseResponse` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientGetRouteResponseResponseTypeDef = TypedDict(
    "_ClientGetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientGetRouteResponseResponseResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientGetRouteResponseResponseTypeDef(_ClientGetRouteResponseResponseTypeDef):
    """
    Type definition for `ClientGetRouteResponse` `Response`

    Success

    - **ModelSelectionExpression** *(string) --*

      Represents the model selection expression of a route response.

    - **ResponseModels** *(dict) --*

      Represents the response models of a route response.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **ResponseParameters** *(dict) --*

      Represents the response parameters of a route response.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteResponseId** *(string) --*

      Represents the identifier of a route response.

    - **RouteResponseKey** *(string) --*

      Represents the route response key of a route response.
    """


_ClientGetRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientGetRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientGetRouteResponseRequestParametersTypeDef(
    _ClientGetRouteResponseRequestParametersTypeDef
):
    """
    Type definition for `ClientGetRouteResponse` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientGetRouteResponseTypeDef = TypedDict(
    "_ClientGetRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": str,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientGetRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class ClientGetRouteResponseTypeDef(_ClientGetRouteResponseTypeDef):
    """
    Type definition for `ClientGetRoute` `Response`

    Success

    - **ApiKeyRequired** *(boolean) --*

      Specifies whether an API key is required for this route.

    - **AuthorizationScopes** *(list) --*

      A list of authorization scopes configured on a route. The scopes are used with a
      COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by
      matching the route scopes against the scopes parsed from the access token in the incoming
      request. The method invocation is authorized if any route scope matches a claimed scope in
      the access token. Otherwise, the invocation is not authorized. When the route scope is
      configured, the client must provide an access token instead of an identity token for
      authorization purposes.

      - *(string) --*

        A string with a length between [1-64].

    - **AuthorizationType** *(string) --*

      The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
      using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

    - **AuthorizerId** *(string) --*

      The identifier of the Authorizer resource to be associated with this route, if the
      authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when you
      created the authorizer.

    - **ModelSelectionExpression** *(string) --*

      The model selection expression for the route.

    - **OperationName** *(string) --*

      The operation name for the route.

    - **RequestModels** *(dict) --*

      The request models for the route.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **RequestParameters** *(dict) --*

      The request parameters for the route.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteId** *(string) --*

      The route ID.

    - **RouteKey** *(string) --*

      The route key for the route.

    - **RouteResponseSelectionExpression** *(string) --*

      The route response selection expression for the route.

    - **Target** *(string) --*

      The target for the route.
    """


_ClientGetRouteResponsesResponseItemsResponseParametersTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseItemsResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientGetRouteResponsesResponseItemsResponseParametersTypeDef(
    _ClientGetRouteResponsesResponseItemsResponseParametersTypeDef
):
    """
    Type definition for `ClientGetRouteResponsesResponseItems` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string,
    headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientGetRouteResponsesResponseItemsTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseItemsTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientGetRouteResponsesResponseItemsResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientGetRouteResponsesResponseItemsTypeDef(
    _ClientGetRouteResponsesResponseItemsTypeDef
):
    """
    Type definition for `ClientGetRouteResponsesResponse` `Items`

    Represents a route response.

    - **ModelSelectionExpression** *(string) --*

      Represents the model selection expression of a route response.

    - **ResponseModels** *(dict) --*

      Represents the response models of a route response.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **ResponseParameters** *(dict) --*

      Represents the response parameters of a route response.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string,
          headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteResponseId** *(string) --*

      Represents the identifier of a route response.

    - **RouteResponseKey** *(string) --*

      Represents the route response key of a route response.
    """


_ClientGetRouteResponsesResponseTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseTypeDef",
    {"Items": List[ClientGetRouteResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetRouteResponsesResponseTypeDef(_ClientGetRouteResponsesResponseTypeDef):
    """
    Type definition for `ClientGetRouteResponses` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a route response.

        - **ModelSelectionExpression** *(string) --*

          Represents the model selection expression of a route response.

        - **ResponseModels** *(dict) --*

          Represents the response models of a route response.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-128].

        - **ResponseParameters** *(dict) --*

          Represents the response parameters of a route response.

          - *(string) --*

            - *(dict) --*

              Validation constraints imposed on parameters of a request (path, query string,
              headers).

              - **Required** *(boolean) --*

                Whether or not the parameter is required.

        - **RouteResponseId** *(string) --*

          Represents the identifier of a route response.

        - **RouteResponseKey** *(string) --*

          Represents the route response key of a route response.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetRoutesResponseItemsRequestParametersTypeDef = TypedDict(
    "_ClientGetRoutesResponseItemsRequestParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientGetRoutesResponseItemsRequestParametersTypeDef(
    _ClientGetRoutesResponseItemsRequestParametersTypeDef
):
    """
    Type definition for `ClientGetRoutesResponseItems` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string,
    headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientGetRoutesResponseItemsTypeDef = TypedDict(
    "_ClientGetRoutesResponseItemsTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": str,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[
            str, ClientGetRoutesResponseItemsRequestParametersTypeDef
        ],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class ClientGetRoutesResponseItemsTypeDef(_ClientGetRoutesResponseItemsTypeDef):
    """
    Type definition for `ClientGetRoutesResponse` `Items`

    Represents a route.

    - **ApiKeyRequired** *(boolean) --*

      Specifies whether an API key is required for this route.

    - **AuthorizationScopes** *(list) --*

      A list of authorization scopes configured on a route. The scopes are used with a
      COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works
      by matching the route scopes against the scopes parsed from the access token in the
      incoming request. The method invocation is authorized if any route scope matches a
      claimed scope in the access token. Otherwise, the invocation is not authorized. When the
      route scope is configured, the client must provide an access token instead of an identity
      token for authorization purposes.

      - *(string) --*

        A string with a length between [1-64].

    - **AuthorizationType** *(string) --*

      The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
      using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

    - **AuthorizerId** *(string) --*

      The identifier of the Authorizer resource to be associated with this route, if the
      authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when
      you created the authorizer.

    - **ModelSelectionExpression** *(string) --*

      The model selection expression for the route.

    - **OperationName** *(string) --*

      The operation name for the route.

    - **RequestModels** *(dict) --*

      The request models for the route.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **RequestParameters** *(dict) --*

      The request parameters for the route.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string,
          headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteId** *(string) --*

      The route ID.

    - **RouteKey** *(string) --*

      The route key for the route.

    - **RouteResponseSelectionExpression** *(string) --*

      The route response selection expression for the route.

    - **Target** *(string) --*

      The target for the route.
    """


_ClientGetRoutesResponseTypeDef = TypedDict(
    "_ClientGetRoutesResponseTypeDef",
    {"Items": List[ClientGetRoutesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetRoutesResponseTypeDef(_ClientGetRoutesResponseTypeDef):
    """
    Type definition for `ClientGetRoutes` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a route.

        - **ApiKeyRequired** *(boolean) --*

          Specifies whether an API key is required for this route.

        - **AuthorizationScopes** *(list) --*

          A list of authorization scopes configured on a route. The scopes are used with a
          COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works
          by matching the route scopes against the scopes parsed from the access token in the
          incoming request. The method invocation is authorized if any route scope matches a
          claimed scope in the access token. Otherwise, the invocation is not authorized. When the
          route scope is configured, the client must provide an access token instead of an identity
          token for authorization purposes.

          - *(string) --*

            A string with a length between [1-64].

        - **AuthorizationType** *(string) --*

          The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
          using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

        - **AuthorizerId** *(string) --*

          The identifier of the Authorizer resource to be associated with this route, if the
          authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when
          you created the authorizer.

        - **ModelSelectionExpression** *(string) --*

          The model selection expression for the route.

        - **OperationName** *(string) --*

          The operation name for the route.

        - **RequestModels** *(dict) --*

          The request models for the route.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-128].

        - **RequestParameters** *(dict) --*

          The request parameters for the route.

          - *(string) --*

            - *(dict) --*

              Validation constraints imposed on parameters of a request (path, query string,
              headers).

              - **Required** *(boolean) --*

                Whether or not the parameter is required.

        - **RouteId** *(string) --*

          The route ID.

        - **RouteKey** *(string) --*

          The route key for the route.

        - **RouteResponseSelectionExpression** *(string) --*

          The route response selection expression for the route.

        - **Target** *(string) --*

          The target for the route.

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientGetStageResponseAccessLogSettingsTypeDef(
    _ClientGetStageResponseAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context
      variables. The format must include at least $context.requestId.
    """


_ClientGetStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStageResponseDefaultRouteSettingsTypeDef(
    _ClientGetStageResponseDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `DefaultRouteSettings`

    Default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
      log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientGetStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStageResponseRouteSettingsTypeDef(
    _ClientGetStageResponseRouteSettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route.
      This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
      the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientGetStageResponseTypeDef = TypedDict(
    "_ClientGetStageResponseTypeDef",
    {
        "AccessLogSettings": ClientGetStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetStageResponseTypeDef(_ClientGetStageResponseTypeDef):
    """
    Type definition for `ClientGetStage` `Response`

    Success

    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

      - **Format** *(string) --*

        A single line format of the access logs of data, as specified by selected $context
        variables. The format must include at least $context.requestId.

    - **ClientCertificateId** *(string) --*

      The identifier of a client certificate for a Stage.

    - **CreatedDate** *(datetime) --*

      The timestamp when the stage was created.

    - **DefaultRouteSettings** *(dict) --*

      Default route settings for the stage.

      - **DataTraceEnabled** *(boolean) --*

        Specifies whether (true) or not (false) data trace logging is enabled for this route. This
        property affects the log entries pushed to Amazon CloudWatch Logs.

      - **DetailedMetricsEnabled** *(boolean) --*

        Specifies whether detailed metrics are enabled.

      - **LoggingLevel** *(string) --*

        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
        log entries pushed to Amazon CloudWatch Logs.

      - **ThrottlingBurstLimit** *(integer) --*

        Specifies the throttling burst limit.

      - **ThrottlingRateLimit** *(float) --*

        Specifies the throttling rate limit.

    - **DeploymentId** *(string) --*

      The identifier of the Deployment that the Stage is associated with.

    - **Description** *(string) --*

      The description of the stage.

    - **LastUpdatedDate** *(datetime) --*

      The timestamp when the stage was last updated.

    - **RouteSettings** *(dict) --*

      Route settings for the stage.

      - *(string) --*

        - *(dict) --*

          Represents a collection of route settings.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this route.
            This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
            the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

    - **StageName** *(string) --*

      The name of the stage.

    - **StageVariables** *(dict) --*

      A map that defines the stage variables for a stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-2048].

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetStagesResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientGetStagesResponseItemsAccessLogSettingsTypeDef(
    _ClientGetStagesResponseItemsAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseItems` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context
      variables. The format must include at least $context.requestId.
    """


_ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef(
    _ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseItems` `DefaultRouteSettings`

    Default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route.
      This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
      the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientGetStagesResponseItemsRouteSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStagesResponseItemsRouteSettingsTypeDef(
    _ClientGetStagesResponseItemsRouteSettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseItems` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this
      route. This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
      affects the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientGetStagesResponseItemsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsTypeDef",
    {
        "AccessLogSettings": ClientGetStagesResponseItemsAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStagesResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetStagesResponseItemsTypeDef(_ClientGetStagesResponseItemsTypeDef):
    """
    Type definition for `ClientGetStagesResponse` `Items`

    Represents an API stage.

    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

      - **Format** *(string) --*

        A single line format of the access logs of data, as specified by selected $context
        variables. The format must include at least $context.requestId.

    - **ClientCertificateId** *(string) --*

      The identifier of a client certificate for a Stage.

    - **CreatedDate** *(datetime) --*

      The timestamp when the stage was created.

    - **DefaultRouteSettings** *(dict) --*

      Default route settings for the stage.

      - **DataTraceEnabled** *(boolean) --*

        Specifies whether (true) or not (false) data trace logging is enabled for this route.
        This property affects the log entries pushed to Amazon CloudWatch Logs.

      - **DetailedMetricsEnabled** *(boolean) --*

        Specifies whether detailed metrics are enabled.

      - **LoggingLevel** *(string) --*

        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
        the log entries pushed to Amazon CloudWatch Logs.

      - **ThrottlingBurstLimit** *(integer) --*

        Specifies the throttling burst limit.

      - **ThrottlingRateLimit** *(float) --*

        Specifies the throttling rate limit.

    - **DeploymentId** *(string) --*

      The identifier of the Deployment that the Stage is associated with.

    - **Description** *(string) --*

      The description of the stage.

    - **LastUpdatedDate** *(datetime) --*

      The timestamp when the stage was last updated.

    - **RouteSettings** *(dict) --*

      Route settings for the stage.

      - *(string) --*

        - *(dict) --*

          Represents a collection of route settings.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this
            route. This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
            affects the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

    - **StageName** *(string) --*

      The name of the stage.

    - **StageVariables** *(dict) --*

      A map that defines the stage variables for a stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-2048].

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientGetStagesResponseTypeDef = TypedDict(
    "_ClientGetStagesResponseTypeDef",
    {"Items": List[ClientGetStagesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetStagesResponseTypeDef(_ClientGetStagesResponseTypeDef):
    """
    Type definition for `ClientGetStages` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an API stage.

        - **AccessLogSettings** *(dict) --*

          Settings for logging access in this stage.

          - **DestinationArn** *(string) --*

            The ARN of the CloudWatch Logs log group to receive access logs.

          - **Format** *(string) --*

            A single line format of the access logs of data, as specified by selected $context
            variables. The format must include at least $context.requestId.

        - **ClientCertificateId** *(string) --*

          The identifier of a client certificate for a Stage.

        - **CreatedDate** *(datetime) --*

          The timestamp when the stage was created.

        - **DefaultRouteSettings** *(dict) --*

          Default route settings for the stage.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this route.
            This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
            the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

        - **DeploymentId** *(string) --*

          The identifier of the Deployment that the Stage is associated with.

        - **Description** *(string) --*

          The description of the stage.

        - **LastUpdatedDate** *(datetime) --*

          The timestamp when the stage was last updated.

        - **RouteSettings** *(dict) --*

          Route settings for the stage.

          - *(string) --*

            - *(dict) --*

              Represents a collection of route settings.

              - **DataTraceEnabled** *(boolean) --*

                Specifies whether (true) or not (false) data trace logging is enabled for this
                route. This property affects the log entries pushed to Amazon CloudWatch Logs.

              - **DetailedMetricsEnabled** *(boolean) --*

                Specifies whether detailed metrics are enabled.

              - **LoggingLevel** *(string) --*

                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
                affects the log entries pushed to Amazon CloudWatch Logs.

              - **ThrottlingBurstLimit** *(integer) --*

                Specifies the throttling burst limit.

              - **ThrottlingRateLimit** *(float) --*

                Specifies the throttling rate limit.

        - **StageName** *(string) --*

          The name of the stage.

        - **StageVariables** *(dict) --*

          A map that defines the stage variables for a stage resource. Variable names can have
          alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-2048].

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].

    - **NextToken** *(string) --*

      The next page of elements from this collection. Not valid for the last element of the
      collection.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    Type definition for `ClientGetTags` `Response`

    - **Tags** *(dict) --*

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateApiMappingResponseTypeDef = TypedDict(
    "_ClientUpdateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientUpdateApiMappingResponseTypeDef(_ClientUpdateApiMappingResponseTypeDef):
    """
    Type definition for `ClientUpdateApiMapping` `Response`

    Success

    - **ApiId** *(string) --*

      The API identifier.

    - **ApiMappingId** *(string) --*

      The API mapping identifier.

    - **ApiMappingKey** *(string) --*

      The API mapping key.

    - **Stage** *(string) --*

      The API stage.
    """


_ClientUpdateApiResponseTypeDef = TypedDict(
    "_ClientUpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateApiResponseTypeDef(_ClientUpdateApiResponseTypeDef):
    """
    Type definition for `ClientUpdateApi` `Response`

    Success

    - **ApiEndpoint** *(string) --*

      The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
      is typically appended to this URI to form a complete path to a deployed API stage.

    - **ApiId** *(string) --*

      The API ID.

    - **ApiKeySelectionExpression** *(string) --*

      An API key selection expression. See `API Key Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
      .

    - **CreatedDate** *(datetime) --*

      The timestamp when the API was created.

    - **Description** *(string) --*

      The description of the API.

    - **DisableSchemaValidation** *(boolean) --*

      Avoid validating models when creating a deployment.

    - **Name** *(string) --*

      The name of the API.

    - **ProtocolType** *(string) --*

      The API protocol: Currently only WEBSOCKET is supported.

    - **RouteSelectionExpression** *(string) --*

      The route selection expression for the API.

    - **Version** *(string) --*

      A version identifier for the API.

    - **Warnings** *(list) --*

      The warning messages reported when failonwarnings is turned on during API import.

      - *(string) --*

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "_ClientUpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientUpdateAuthorizerResponseTypeDef(_ClientUpdateAuthorizerResponseTypeDef):
    """
    Type definition for `ClientUpdateAuthorizer` `Response`

    Success

    - **AuthorizerCredentialsArn** *(string) --*

      Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
      To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
      To use resource-based permissions on the Lambda function, specify null.

    - **AuthorizerId** *(string) --*

      The authorizer identifier.

    - **AuthorizerResultTtlInSeconds** *(integer) --*

      The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
      authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer
      responses. If this field is not set, the default value is 300. The maximum value is 3600, or
      1 hour.

    - **AuthorizerType** *(string) --*

      The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using
      incoming request parameters.

    - **AuthorizerUri** *(string) --*

      The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a
      well-formed Lambda function URI, for example,
      arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
      In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} ,
      where {region} is the same as the region hosting the Lambda function, path indicates that the
      remaining substring in the URI should be treated as the path to the resource, including the
      initial /. For Lambda functions, this is usually of the form
      /2015-03-31/functions/[FunctionARN]/invocations.

    - **IdentitySource** *(list) --*

      The identity source for which authorization is requested.

      For the REQUEST authorizer, this is required when authorization caching is enabled. The value
      is a comma-separated string of one or more mapping expressions of the specified request
      parameters. For example, if an Auth header and a Name query string parameters are defined as
      identity sources, this value is method.request.header.Auth, method.request.querystring.Name.
      These parameters will be used to derive the authorization caching key and to perform runtime
      validation of the REQUEST authorizer by verifying all of the identity-related request
      parameters are present, not null, and non-empty. Only when this is true does the authorizer
      invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response
      without calling the Lambda function. The valid value is a string of comma-separated mapping
      expressions of the specified request parameters. When the authorization caching is not
      enabled, this property is optional.

      - *(string) --*

    - **IdentityValidationExpression** *(string) --*

      The validation expression does not apply to the REQUEST authorizer.

    - **Name** *(string) --*

      The name of the authorizer.

    - **ProviderArns** *(list) --*

      For REQUEST authorizer, this is not defined.

      - *(string) --*

        Represents an Amazon Resource Name (ARN).
    """


_ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientUpdateDeploymentResponseTypeDef(_ClientUpdateDeploymentResponseTypeDef):
    """
    Type definition for `ClientUpdateDeployment` `Response`

    Success

    - **CreatedDate** *(datetime) --*

      The date and time when the Deployment resource was created.

    - **DeploymentId** *(string) --*

      The identifier for the deployment.

    - **DeploymentStatus** *(string) --*

      The status of the deployment: PENDING, FAILED, or SUCCEEDED.

    - **DeploymentStatusMessage** *(string) --*

      May contain additional feedback on the status of an API deployment.

    - **Description** *(string) --*

      The description for the deployment.
    """


_ClientUpdateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientUpdateDomainNameDomainNameConfigurationsTypeDef(
    _ClientUpdateDomainNameDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateDomainName` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain
      name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized endpoint
      for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this domain
      name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain name. The
      valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the
      status is UPDATING, the domain cannot be modified further until the existing operation is
      complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain name
      migration.
    """


_ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateDomainNameResponse` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this
      domain name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized
      endpoint for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this
      domain name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain name.
      The valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
      the status is UPDATING, the domain cannot be modified further until the existing
      operation is complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain name
      migration.
    """


_ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateDomainNameResponseTypeDef(_ClientUpdateDomainNameResponseTypeDef):
    """
    Type definition for `ClientUpdateDomainName` `Response`

    Success

    - **ApiMappingSelectionExpression** *(string) --*

      The API mapping selection expression.

    - **DomainName** *(string) --*

      The name of the DomainName resource.

    - **DomainNameConfigurations** *(list) --*

      The domain name configurations.

      - *(dict) --*

        The domain name configuration.

        - **ApiGatewayDomainName** *(string) --*

          A domain name for the WebSocket API.

        - **CertificateArn** *(string) --*

          An AWS-managed certificate that will be used by the edge-optimized endpoint for this
          domain name. AWS Certificate Manager is the only supported source.

        - **CertificateName** *(string) --*

          The user-friendly name of the certificate that will be used by the edge-optimized
          endpoint for this domain name.

        - **CertificateUploadDate** *(datetime) --*

          The timestamp when the certificate that was used by edge-optimized endpoint for this
          domain name was uploaded.

        - **EndpointType** *(string) --*

          The endpoint type.

        - **HostedZoneId** *(string) --*

          The Amazon Route 53 Hosted Zone ID of the endpoint.

        - **SecurityPolicy** *(string) --*

          The Transport Layer Security (TLS) version of the security policy for this domain name.
          The valid values are TLS_1_0 and TLS_1_2.

        - **DomainNameStatus** *(string) --*

          The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If
          the status is UPDATING, the domain cannot be modified further until the existing
          operation is complete. If it is AVAILABLE, the domain can be updated.

        - **DomainNameStatusMessage** *(string) --*

          An optional text message containing detailed information about status of the domain name
          migration.

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": str,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class ClientUpdateIntegrationResponseResponseTypeDef(
    _ClientUpdateIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientUpdateIntegrationResponse` `Response`

    Success

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **IntegrationResponseId** *(string) --*

      The integration response ID.

    - **IntegrationResponseKey** *(string) --*

      The integration response key.

    - **ResponseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the backend. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of method.response.header.{name}, where name is a valid and unique header name. The mapped
      non-static value must match the pattern of integration.response.header.{name} or
      integration.response.body.{JSON-expression}, where name is a valid and unique response header
      name and JSON-expression is a valid JSON expression without the $ prefix.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **ResponseTemplates** *(dict) --*

      The collection of response templates for the integration response as a string-to-string map
      of key-value pairs. Response templates are represented as a key/value map, with a
      content-type as the key and a template as the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expressions for the integration response.
    """


_ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": str,
        "ContentHandlingStrategy": str,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": str,
        "IntegrationUri": str,
        "PassthroughBehavior": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientUpdateIntegrationResponseTypeDef(_ClientUpdateIntegrationResponseTypeDef):
    """
    Type definition for `ClientUpdateIntegration` `Response`

    Success

    - **ConnectionId** *(string) --*

      The connection ID.

    - **ConnectionType** *(string) --*

      The type of the network connection to the integration endpoint. Currently the only valid
      value is INTERNET, for connections through the public routable internet.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **CredentialsArn** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on
      supported AWS services, specify null.

    - **Description** *(string) --*

      Represents the description of an integration.

    - **IntegrationId** *(string) --*

      Represents the identifier of an integration.

    - **IntegrationMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **IntegrationResponseSelectionExpression** *(string) --*

      The integration response selection expression for the integration. See `Integration Response
      Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
      .

    - **IntegrationType** *(string) --*

      The integration type of an integration. One of the following:

      AWS: for integrating the route or method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      Lambda proxy integration.

      HTTP: for integrating the route or method request with an HTTP endpoint. This integration is
      also referred to as the HTTP custom integration.

      HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the client
      request passed through as-is. This is also referred to as HTTP proxy integration.

      MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint
      without invoking any backend.

    - **IntegrationUri** *(string) --*

      For a Lambda proxy integration, this is the URI of the Lambda function.

    - **PassthroughBehavior** *(string) --*

      Specifies the pass-through behavior for incoming requests based on the Content-Type header in
      the request, and the available mapping templates specified as the requestTemplates property
      on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES,
      and NEVER.

      WHEN_NO_MATCH passes the request body for unmapped content types through to the integration
      backend without transformation.

      NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

      WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
      templates. However, if there is at least one content type defined, unmapped content types
      will be rejected with the same HTTP 415 Unsupported Media Type response.

    - **RequestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      backend. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the backend. The method request parameter value must match the
      pattern of method.request.{location}.{name} , where {location} is querystring, path, or
      header; and {name} must be a valid and unique method request parameter name.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **RequestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expression for the integration.

    - **TimeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.
    """


_ClientUpdateModelResponseTypeDef = TypedDict(
    "_ClientUpdateModelResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class ClientUpdateModelResponseTypeDef(_ClientUpdateModelResponseTypeDef):
    """
    Type definition for `ClientUpdateModel` `Response`

    Success

    - **ContentType** *(string) --*

      The content-type for the model, for example, "application/json".

    - **Description** *(string) --*

      The description of the model.

    - **ModelId** *(string) --*

      The model identifier.

    - **Name** *(string) --*

      The name of the model. Must be alphanumeric.

    - **Schema** *(string) --*

      The schema for the model. For application/json models, this should be JSON schema draft 4
      model.
    """


_ClientUpdateRouteRequestParametersTypeDef = TypedDict(
    "_ClientUpdateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientUpdateRouteRequestParametersTypeDef(
    _ClientUpdateRouteRequestParametersTypeDef
):
    """
    Type definition for `ClientUpdateRoute` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientUpdateRouteResponseResponseParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientUpdateRouteResponseResponseParametersTypeDef(
    _ClientUpdateRouteResponseResponseParametersTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponse` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientUpdateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientUpdateRouteResponseResponseResponseParametersTypeDef(
    _ClientUpdateRouteResponseResponseResponseParametersTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponseResponse` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientUpdateRouteResponseResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientUpdateRouteResponseResponseResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientUpdateRouteResponseResponseTypeDef(
    _ClientUpdateRouteResponseResponseTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponse` `Response`

    Success

    - **ModelSelectionExpression** *(string) --*

      Represents the model selection expression of a route response.

    - **ResponseModels** *(dict) --*

      Represents the response models of a route response.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **ResponseParameters** *(dict) --*

      Represents the response parameters of a route response.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteResponseId** *(string) --*

      Represents the identifier of a route response.

    - **RouteResponseKey** *(string) --*

      Represents the route response key of a route response.
    """


_ClientUpdateRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseRequestParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientUpdateRouteResponseRequestParametersTypeDef(
    _ClientUpdateRouteResponseRequestParametersTypeDef
):
    """
    Type definition for `ClientUpdateRouteResponse` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string, headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_ClientUpdateRouteResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": str,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[
            str, ClientUpdateRouteResponseRequestParametersTypeDef
        ],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class ClientUpdateRouteResponseTypeDef(_ClientUpdateRouteResponseTypeDef):
    """
    Type definition for `ClientUpdateRoute` `Response`

    Success

    - **ApiKeyRequired** *(boolean) --*

      Specifies whether an API key is required for this route.

    - **AuthorizationScopes** *(list) --*

      A list of authorization scopes configured on a route. The scopes are used with a
      COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by
      matching the route scopes against the scopes parsed from the access token in the incoming
      request. The method invocation is authorized if any route scope matches a claimed scope in
      the access token. Otherwise, the invocation is not authorized. When the route scope is
      configured, the client must provide an access token instead of an identity token for
      authorization purposes.

      - *(string) --*

        A string with a length between [1-64].

    - **AuthorizationType** *(string) --*

      The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
      using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

    - **AuthorizerId** *(string) --*

      The identifier of the Authorizer resource to be associated with this route, if the
      authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when you
      created the authorizer.

    - **ModelSelectionExpression** *(string) --*

      The model selection expression for the route.

    - **OperationName** *(string) --*

      The operation name for the route.

    - **RequestModels** *(dict) --*

      The request models for the route.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **RequestParameters** *(dict) --*

      The request parameters for the route.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string, headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteId** *(string) --*

      The route ID.

    - **RouteKey** *(string) --*

      The route key for the route.

    - **RouteResponseSelectionExpression** *(string) --*

      The route response selection expression for the route.

    - **Target** *(string) --*

      The target for the route.
    """


_ClientUpdateStageAccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientUpdateStageAccessLogSettingsTypeDef(
    _ClientUpdateStageAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStage` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context variables.
      The format must include at least $context.requestId.
    """


_ClientUpdateStageDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageDefaultRouteSettingsTypeDef(
    _ClientUpdateStageDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStage` `DefaultRouteSettings`

    The default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log
      entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientUpdateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientUpdateStageResponseAccessLogSettingsTypeDef(
    _ClientUpdateStageResponseAccessLogSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context
      variables. The format must include at least $context.requestId.
    """


_ClientUpdateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageResponseDefaultRouteSettingsTypeDef(
    _ClientUpdateStageResponseDefaultRouteSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `DefaultRouteSettings`

    Default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
      log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientUpdateStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageResponseRouteSettingsTypeDef(
    _ClientUpdateStageResponseRouteSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route.
      This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
      the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_ClientUpdateStageResponseTypeDef = TypedDict(
    "_ClientUpdateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientUpdateStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientUpdateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientUpdateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateStageResponseTypeDef(_ClientUpdateStageResponseTypeDef):
    """
    Type definition for `ClientUpdateStage` `Response`

    Success

    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

      - **Format** *(string) --*

        A single line format of the access logs of data, as specified by selected $context
        variables. The format must include at least $context.requestId.

    - **ClientCertificateId** *(string) --*

      The identifier of a client certificate for a Stage.

    - **CreatedDate** *(datetime) --*

      The timestamp when the stage was created.

    - **DefaultRouteSettings** *(dict) --*

      Default route settings for the stage.

      - **DataTraceEnabled** *(boolean) --*

        Specifies whether (true) or not (false) data trace logging is enabled for this route. This
        property affects the log entries pushed to Amazon CloudWatch Logs.

      - **DetailedMetricsEnabled** *(boolean) --*

        Specifies whether detailed metrics are enabled.

      - **LoggingLevel** *(string) --*

        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
        log entries pushed to Amazon CloudWatch Logs.

      - **ThrottlingBurstLimit** *(integer) --*

        Specifies the throttling burst limit.

      - **ThrottlingRateLimit** *(float) --*

        Specifies the throttling rate limit.

    - **DeploymentId** *(string) --*

      The identifier of the Deployment that the Stage is associated with.

    - **Description** *(string) --*

      The description of the stage.

    - **LastUpdatedDate** *(datetime) --*

      The timestamp when the stage was last updated.

    - **RouteSettings** *(dict) --*

      Route settings for the stage.

      - *(string) --*

        - *(dict) --*

          Represents a collection of route settings.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this route.
            This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
            the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

    - **StageName** *(string) --*

      The name of the stage.

    - **StageVariables** *(dict) --*

      A map that defines the stage variables for a stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-2048].

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be
      up to 128 characters and must not start with aws:. The tag value can be up to 256 characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_ClientUpdateStageRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageRouteSettingsTypeDef(_ClientUpdateStageRouteSettingsTypeDef):
    """
    Type definition for `ClientUpdateStage` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the
      log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_GetApisPaginatePaginationConfigTypeDef = TypedDict(
    "_GetApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetApisPaginatePaginationConfigTypeDef(_GetApisPaginatePaginationConfigTypeDef):
    """
    Type definition for `GetApisPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetApisPaginateResponseItemsTypeDef = TypedDict(
    "_GetApisPaginateResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetApisPaginateResponseItemsTypeDef(_GetApisPaginateResponseItemsTypeDef):
    """
    Type definition for `GetApisPaginateResponse` `Items`

    Represents an API.

    - **ApiEndpoint** *(string) --*

      The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
      name is typically appended to this URI to form a complete path to a deployed API stage.

    - **ApiId** *(string) --*

      The API ID.

    - **ApiKeySelectionExpression** *(string) --*

      An API key selection expression. See `API Key Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
      .

    - **CreatedDate** *(datetime) --*

      The timestamp when the API was created.

    - **Description** *(string) --*

      The description of the API.

    - **DisableSchemaValidation** *(boolean) --*

      Avoid validating models when creating a deployment.

    - **Name** *(string) --*

      The name of the API.

    - **ProtocolType** *(string) --*

      The API protocol: Currently only WEBSOCKET is supported.

    - **RouteSelectionExpression** *(string) --*

      The route selection expression for the API.

    - **Version** *(string) --*

      A version identifier for the API.

    - **Warnings** *(list) --*

      The warning messages reported when failonwarnings is turned on during API import.

      - *(string) --*

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_GetApisPaginateResponseTypeDef = TypedDict(
    "_GetApisPaginateResponseTypeDef",
    {"Items": List[GetApisPaginateResponseItemsTypeDef]},
    total=False,
)


class GetApisPaginateResponseTypeDef(_GetApisPaginateResponseTypeDef):
    """
    Type definition for `GetApisPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an API.

        - **ApiEndpoint** *(string) --*

          The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
          name is typically appended to this URI to form a complete path to a deployed API stage.

        - **ApiId** *(string) --*

          The API ID.

        - **ApiKeySelectionExpression** *(string) --*

          An API key selection expression. See `API Key Selection Expressions
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
          .

        - **CreatedDate** *(datetime) --*

          The timestamp when the API was created.

        - **Description** *(string) --*

          The description of the API.

        - **DisableSchemaValidation** *(boolean) --*

          Avoid validating models when creating a deployment.

        - **Name** *(string) --*

          The name of the API.

        - **ProtocolType** *(string) --*

          The API protocol: Currently only WEBSOCKET is supported.

        - **RouteSelectionExpression** *(string) --*

          The route selection expression for the API.

        - **Version** *(string) --*

          A version identifier for the API.

        - **Warnings** *(list) --*

          The warning messages reported when failonwarnings is turned on during API import.

          - *(string) --*

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].
    """


_GetAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAuthorizersPaginatePaginationConfigTypeDef(
    _GetAuthorizersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetAuthorizersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetAuthorizersPaginateResponseItemsTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class GetAuthorizersPaginateResponseItemsTypeDef(
    _GetAuthorizersPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetAuthorizersPaginateResponse` `Items`

    Represents an authorizer.

    - **AuthorizerCredentialsArn** *(string) --*

      Specifies the required credentials as an IAM role for API Gateway to invoke the
      authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
      Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
      null.

    - **AuthorizerId** *(string) --*

      The authorizer identifier.

    - **AuthorizerResultTtlInSeconds** *(integer) --*

      The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
      authorization caching is disabled. If it is greater than 0, API Gateway will cache
      authorizer responses. If this field is not set, the default value is 300. The maximum
      value is 3600, or 1 hour.

    - **AuthorizerType** *(string) --*

      The authorizer type. Currently the only valid value is REQUEST, for a Lambda function
      using incoming request parameters.

    - **AuthorizerUri** *(string) --*

      The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be
      a well-formed Lambda function URI, for example,
      arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
      In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}
      , where {region} is the same as the region hosting the Lambda function, path indicates
      that the remaining substring in the URI should be treated as the path to the resource,
      including the initial /. For Lambda functions, this is usually of the form
      /2015-03-31/functions/[FunctionARN]/invocations.

    - **IdentitySource** *(list) --*

      The identity source for which authorization is requested.

      For the REQUEST authorizer, this is required when authorization caching is enabled. The
      value is a comma-separated string of one or more mapping expressions of the specified
      request parameters. For example, if an Auth header and a Name query string parameters are
      defined as identity sources, this value is method.request.header.Auth,
      method.request.querystring.Name. These parameters will be used to derive the
      authorization caching key and to perform runtime validation of the REQUEST authorizer by
      verifying all of the identity-related request parameters are present, not null, and
      non-empty. Only when this is true does the authorizer invoke the authorizer Lambda
      function, otherwise, it returns a 401 Unauthorized response without calling the Lambda
      function. The valid value is a string of comma-separated mapping expressions of the
      specified request parameters. When the authorization caching is not enabled, this
      property is optional.

      - *(string) --*

    - **IdentityValidationExpression** *(string) --*

      The validation expression does not apply to the REQUEST authorizer.

    - **Name** *(string) --*

      The name of the authorizer.

    - **ProviderArns** *(list) --*

      For REQUEST authorizer, this is not defined.

      - *(string) --*

        Represents an Amazon Resource Name (ARN).
    """


_GetAuthorizersPaginateResponseTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseTypeDef",
    {"Items": List[GetAuthorizersPaginateResponseItemsTypeDef]},
    total=False,
)


class GetAuthorizersPaginateResponseTypeDef(_GetAuthorizersPaginateResponseTypeDef):
    """
    Type definition for `GetAuthorizersPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an authorizer.

        - **AuthorizerCredentialsArn** *(string) --*

          Specifies the required credentials as an IAM role for API Gateway to invoke the
          authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
          Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
          null.

        - **AuthorizerId** *(string) --*

          The authorizer identifier.

        - **AuthorizerResultTtlInSeconds** *(integer) --*

          The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
          authorization caching is disabled. If it is greater than 0, API Gateway will cache
          authorizer responses. If this field is not set, the default value is 300. The maximum
          value is 3600, or 1 hour.

        - **AuthorizerType** *(string) --*

          The authorizer type. Currently the only valid value is REQUEST, for a Lambda function
          using incoming request parameters.

        - **AuthorizerUri** *(string) --*

          The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be
          a well-formed Lambda function URI, for example,
          arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
          In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}
          , where {region} is the same as the region hosting the Lambda function, path indicates
          that the remaining substring in the URI should be treated as the path to the resource,
          including the initial /. For Lambda functions, this is usually of the form
          /2015-03-31/functions/[FunctionARN]/invocations.

        - **IdentitySource** *(list) --*

          The identity source for which authorization is requested.

          For the REQUEST authorizer, this is required when authorization caching is enabled. The
          value is a comma-separated string of one or more mapping expressions of the specified
          request parameters. For example, if an Auth header and a Name query string parameters are
          defined as identity sources, this value is method.request.header.Auth,
          method.request.querystring.Name. These parameters will be used to derive the
          authorization caching key and to perform runtime validation of the REQUEST authorizer by
          verifying all of the identity-related request parameters are present, not null, and
          non-empty. Only when this is true does the authorizer invoke the authorizer Lambda
          function, otherwise, it returns a 401 Unauthorized response without calling the Lambda
          function. The valid value is a string of comma-separated mapping expressions of the
          specified request parameters. When the authorization caching is not enabled, this
          property is optional.

          - *(string) --*

        - **IdentityValidationExpression** *(string) --*

          The validation expression does not apply to the REQUEST authorizer.

        - **Name** *(string) --*

          The name of the authorizer.

        - **ProviderArns** *(list) --*

          For REQUEST authorizer, this is not defined.

          - *(string) --*

            Represents an Amazon Resource Name (ARN).
    """


_GetDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDeploymentsPaginatePaginationConfigTypeDef(
    _GetDeploymentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDeploymentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetDeploymentsPaginateResponseItemsTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseItemsTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class GetDeploymentsPaginateResponseItemsTypeDef(
    _GetDeploymentsPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetDeploymentsPaginateResponse` `Items`

    An immutable representation of an API that can be called by users. A Deployment must be
    associated with a Stage for it to be callable over the internet.

    - **CreatedDate** *(datetime) --*

      The date and time when the Deployment resource was created.

    - **DeploymentId** *(string) --*

      The identifier for the deployment.

    - **DeploymentStatus** *(string) --*

      The status of the deployment: PENDING, FAILED, or SUCCEEDED.

    - **DeploymentStatusMessage** *(string) --*

      May contain additional feedback on the status of an API deployment.

    - **Description** *(string) --*

      The description for the deployment.
    """


_GetDeploymentsPaginateResponseTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseTypeDef",
    {"Items": List[GetDeploymentsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetDeploymentsPaginateResponseTypeDef(_GetDeploymentsPaginateResponseTypeDef):
    """
    Type definition for `GetDeploymentsPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        An immutable representation of an API that can be called by users. A Deployment must be
        associated with a Stage for it to be callable over the internet.

        - **CreatedDate** *(datetime) --*

          The date and time when the Deployment resource was created.

        - **DeploymentId** *(string) --*

          The identifier for the deployment.

        - **DeploymentStatus** *(string) --*

          The status of the deployment: PENDING, FAILED, or SUCCEEDED.

        - **DeploymentStatusMessage** *(string) --*

          May contain additional feedback on the status of an API deployment.

        - **Description** *(string) --*

          The description for the deployment.
    """


_GetDomainNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDomainNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDomainNamesPaginatePaginationConfigTypeDef(
    _GetDomainNamesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDomainNamesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": str,
        "HostedZoneId": str,
        "SecurityPolicy": str,
        "DomainNameStatus": str,
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef(
    _GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef
):
    """
    Type definition for `GetDomainNamesPaginateResponseItems` `DomainNameConfigurations`

    The domain name configuration.

    - **ApiGatewayDomainName** *(string) --*

      A domain name for the WebSocket API.

    - **CertificateArn** *(string) --*

      An AWS-managed certificate that will be used by the edge-optimized endpoint for this
      domain name. AWS Certificate Manager is the only supported source.

    - **CertificateName** *(string) --*

      The user-friendly name of the certificate that will be used by the edge-optimized
      endpoint for this domain name.

    - **CertificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this
      domain name was uploaded.

    - **EndpointType** *(string) --*

      The endpoint type.

    - **HostedZoneId** *(string) --*

      The Amazon Route 53 Hosted Zone ID of the endpoint.

    - **SecurityPolicy** *(string) --*

      The Transport Layer Security (TLS) version of the security policy for this domain
      name. The valid values are TLS_1_0 and TLS_1_2.

    - **DomainNameStatus** *(string) --*

      The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
      If the status is UPDATING, the domain cannot be modified further until the existing
      operation is complete. If it is AVAILABLE, the domain can be updated.

    - **DomainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the domain
      name migration.
    """


_GetDomainNamesPaginateResponseItemsTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseItemsTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetDomainNamesPaginateResponseItemsTypeDef(
    _GetDomainNamesPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetDomainNamesPaginateResponse` `Items`

    Represents a domain name.

    - **ApiMappingSelectionExpression** *(string) --*

      The API mapping selection expression.

    - **DomainName** *(string) --*

      The name of the DomainName resource.

    - **DomainNameConfigurations** *(list) --*

      The domain name configurations.

      - *(dict) --*

        The domain name configuration.

        - **ApiGatewayDomainName** *(string) --*

          A domain name for the WebSocket API.

        - **CertificateArn** *(string) --*

          An AWS-managed certificate that will be used by the edge-optimized endpoint for this
          domain name. AWS Certificate Manager is the only supported source.

        - **CertificateName** *(string) --*

          The user-friendly name of the certificate that will be used by the edge-optimized
          endpoint for this domain name.

        - **CertificateUploadDate** *(datetime) --*

          The timestamp when the certificate that was used by edge-optimized endpoint for this
          domain name was uploaded.

        - **EndpointType** *(string) --*

          The endpoint type.

        - **HostedZoneId** *(string) --*

          The Amazon Route 53 Hosted Zone ID of the endpoint.

        - **SecurityPolicy** *(string) --*

          The Transport Layer Security (TLS) version of the security policy for this domain
          name. The valid values are TLS_1_0 and TLS_1_2.

        - **DomainNameStatus** *(string) --*

          The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
          If the status is UPDATING, the domain cannot be modified further until the existing
          operation is complete. If it is AVAILABLE, the domain can be updated.

        - **DomainNameStatusMessage** *(string) --*

          An optional text message containing detailed information about status of the domain
          name migration.

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_GetDomainNamesPaginateResponseTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseTypeDef",
    {"Items": List[GetDomainNamesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetDomainNamesPaginateResponseTypeDef(_GetDomainNamesPaginateResponseTypeDef):
    """
    Type definition for `GetDomainNamesPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a domain name.

        - **ApiMappingSelectionExpression** *(string) --*

          The API mapping selection expression.

        - **DomainName** *(string) --*

          The name of the DomainName resource.

        - **DomainNameConfigurations** *(list) --*

          The domain name configurations.

          - *(dict) --*

            The domain name configuration.

            - **ApiGatewayDomainName** *(string) --*

              A domain name for the WebSocket API.

            - **CertificateArn** *(string) --*

              An AWS-managed certificate that will be used by the edge-optimized endpoint for this
              domain name. AWS Certificate Manager is the only supported source.

            - **CertificateName** *(string) --*

              The user-friendly name of the certificate that will be used by the edge-optimized
              endpoint for this domain name.

            - **CertificateUploadDate** *(datetime) --*

              The timestamp when the certificate that was used by edge-optimized endpoint for this
              domain name was uploaded.

            - **EndpointType** *(string) --*

              The endpoint type.

            - **HostedZoneId** *(string) --*

              The Amazon Route 53 Hosted Zone ID of the endpoint.

            - **SecurityPolicy** *(string) --*

              The Transport Layer Security (TLS) version of the security policy for this domain
              name. The valid values are TLS_1_0 and TLS_1_2.

            - **DomainNameStatus** *(string) --*

              The status of the domain name migration. The valid values are AVAILABLE and UPDATING.
              If the status is UPDATING, the domain cannot be modified further until the existing
              operation is complete. If it is AVAILABLE, the domain can be updated.

            - **DomainNameStatusMessage** *(string) --*

              An optional text message containing detailed information about status of the domain
              name migration.

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].
    """


_GetIntegrationResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntegrationResponsesPaginatePaginationConfigTypeDef(
    _GetIntegrationResponsesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetIntegrationResponsesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetIntegrationResponsesPaginateResponseItemsTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginateResponseItemsTypeDef",
    {
        "ContentHandlingStrategy": str,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class GetIntegrationResponsesPaginateResponseItemsTypeDef(
    _GetIntegrationResponsesPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetIntegrationResponsesPaginateResponse` `Items`

    Represents an integration response.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **IntegrationResponseId** *(string) --*

      The integration response ID.

    - **IntegrationResponseKey** *(string) --*

      The integration response key.

    - **ResponseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response
      from the backend. The key is a method response header parameter name and the mapped value
      is an integration response header value, a static value enclosed within a pair of single
      quotes, or a JSON expression from the integration response body. The mapping key must
      match the pattern of method.response.header.{name}, where name is a valid and unique
      header name. The mapped non-static value must match the pattern of
      integration.response.header.{name} or integration.response.body.{JSON-expression}, where
      name is a valid and unique response header name and JSON-expression is a valid JSON
      expression without the $ prefix.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **ResponseTemplates** *(dict) --*

      The collection of response templates for the integration response as a string-to-string
      map of key-value pairs. Response templates are represented as a key/value map, with a
      content-type as the key and a template as the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expressions for the integration response.
    """


_GetIntegrationResponsesPaginateResponseTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginateResponseTypeDef",
    {"Items": List[GetIntegrationResponsesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetIntegrationResponsesPaginateResponseTypeDef(
    _GetIntegrationResponsesPaginateResponseTypeDef
):
    """
    Type definition for `GetIntegrationResponsesPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an integration response.

        - **ContentHandlingStrategy** *(string) --*

          Specifies how to handle response payload content type conversions. Supported values are
          CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
          corresponding binary blob.

          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
          string.

          If this property is not defined, the response payload will be passed through from the
          integration response to the route response or method response without modification.

        - **IntegrationResponseId** *(string) --*

          The integration response ID.

        - **IntegrationResponseKey** *(string) --*

          The integration response key.

        - **ResponseParameters** *(dict) --*

          A key-value map specifying response parameters that are passed to the method response
          from the backend. The key is a method response header parameter name and the mapped value
          is an integration response header value, a static value enclosed within a pair of single
          quotes, or a JSON expression from the integration response body. The mapping key must
          match the pattern of method.response.header.{name}, where name is a valid and unique
          header name. The mapped non-static value must match the pattern of
          integration.response.header.{name} or integration.response.body.{JSON-expression}, where
          name is a valid and unique response header name and JSON-expression is a valid JSON
          expression without the $ prefix.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-512].

        - **ResponseTemplates** *(dict) --*

          The collection of response templates for the integration response as a string-to-string
          map of key-value pairs. Response templates are represented as a key/value map, with a
          content-type as the key and a template as the value.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-32768].

        - **TemplateSelectionExpression** *(string) --*

          The template selection expressions for the integration response.
    """


_GetIntegrationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntegrationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntegrationsPaginatePaginationConfigTypeDef(
    _GetIntegrationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetIntegrationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetIntegrationsPaginateResponseItemsTypeDef = TypedDict(
    "_GetIntegrationsPaginateResponseItemsTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": str,
        "ContentHandlingStrategy": str,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": str,
        "IntegrationUri": str,
        "PassthroughBehavior": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class GetIntegrationsPaginateResponseItemsTypeDef(
    _GetIntegrationsPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetIntegrationsPaginateResponse` `Items`

    Represents an integration.

    - **ConnectionId** *(string) --*

      The connection ID.

    - **ConnectionType** *(string) --*

      The type of the network connection to the integration endpoint. Currently the only valid
      value is INTERNET, for connections through the public routable internet.

    - **ContentHandlingStrategy** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

      CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the route response or method response without modification.

    - **CredentialsArn** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations,
      three options are available. To specify an IAM Role for API Gateway to assume, use the
      role's Amazon Resource Name (ARN). To require that the caller's identity be passed
      through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based
      permissions on supported AWS services, specify null.

    - **Description** *(string) --*

      Represents the description of an integration.

    - **IntegrationId** *(string) --*

      Represents the identifier of an integration.

    - **IntegrationMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **IntegrationResponseSelectionExpression** *(string) --*

      The integration response selection expression for the integration. See `Integration
      Response Selection Expressions
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
      .

    - **IntegrationType** *(string) --*

      The integration type of an integration. One of the following:

      AWS: for integrating the route or method request with an AWS service action, including
      the Lambda function-invoking action. With the Lambda function-invoking action, this is
      referred to as the Lambda custom integration. With any other AWS service action, this is
      known as AWS integration.

      AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to
      as Lambda proxy integration.

      HTTP: for integrating the route or method request with an HTTP endpoint. This integration
      is also referred to as the HTTP custom integration.

      HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the
      client request passed through as-is. This is also referred to as HTTP proxy integration.

      MOCK: for integrating the route or method request with API Gateway as a "loopback"
      endpoint without invoking any backend.

    - **IntegrationUri** *(string) --*

      For a Lambda proxy integration, this is the URI of the Lambda function.

    - **PassthroughBehavior** *(string) --*

      Specifies the pass-through behavior for incoming requests based on the Content-Type
      header in the request, and the available mapping templates specified as the
      requestTemplates property on the Integration resource. There are three valid values:
      WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.

      WHEN_NO_MATCH passes the request body for unmapped content types through to the
      integration backend without transformation.

      NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

      WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
      templates. However, if there is at least one content type defined, unmapped content types
      will be rejected with the same HTTP 415 Unsupported Media Type response.

    - **RequestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to
      the backend. The key is an integration request parameter name and the associated value is
      a method request parameter value or static value that must be enclosed within single
      quotes and pre-encoded as required by the backend. The method request parameter value
      must match the pattern of method.request.{location}.{name} , where {location} is
      querystring, path, or header; and {name} must be a valid and unique method request
      parameter name.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-512].

    - **RequestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on
      the value of the Content-Type header sent by the client. The content type value is the
      key in this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-32768].

    - **TemplateSelectionExpression** *(string) --*

      The template selection expression for the integration.

    - **TimeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000
      milliseconds or 29 seconds.
    """


_GetIntegrationsPaginateResponseTypeDef = TypedDict(
    "_GetIntegrationsPaginateResponseTypeDef",
    {"Items": List[GetIntegrationsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetIntegrationsPaginateResponseTypeDef(_GetIntegrationsPaginateResponseTypeDef):
    """
    Type definition for `GetIntegrationsPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an integration.

        - **ConnectionId** *(string) --*

          The connection ID.

        - **ConnectionType** *(string) --*

          The type of the network connection to the integration endpoint. Currently the only valid
          value is INTERNET, for connections through the public routable internet.

        - **ContentHandlingStrategy** *(string) --*

          Specifies how to handle response payload content type conversions. Supported values are
          CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
          corresponding binary blob.

          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
          string.

          If this property is not defined, the response payload will be passed through from the
          integration response to the route response or method response without modification.

        - **CredentialsArn** *(string) --*

          Specifies the credentials required for the integration, if any. For AWS integrations,
          three options are available. To specify an IAM Role for API Gateway to assume, use the
          role's Amazon Resource Name (ARN). To require that the caller's identity be passed
          through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based
          permissions on supported AWS services, specify null.

        - **Description** *(string) --*

          Represents the description of an integration.

        - **IntegrationId** *(string) --*

          Represents the identifier of an integration.

        - **IntegrationMethod** *(string) --*

          Specifies the integration's HTTP method type.

        - **IntegrationResponseSelectionExpression** *(string) --*

          The integration response selection expression for the integration. See `Integration
          Response Selection Expressions
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
          .

        - **IntegrationType** *(string) --*

          The integration type of an integration. One of the following:

          AWS: for integrating the route or method request with an AWS service action, including
          the Lambda function-invoking action. With the Lambda function-invoking action, this is
          referred to as the Lambda custom integration. With any other AWS service action, this is
          known as AWS integration.

          AWS_PROXY: for integrating the route or method request with the Lambda function-invoking
          action with the client request passed through as-is. This integration is also referred to
          as Lambda proxy integration.

          HTTP: for integrating the route or method request with an HTTP endpoint. This integration
          is also referred to as the HTTP custom integration.

          HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with the
          client request passed through as-is. This is also referred to as HTTP proxy integration.

          MOCK: for integrating the route or method request with API Gateway as a "loopback"
          endpoint without invoking any backend.

        - **IntegrationUri** *(string) --*

          For a Lambda proxy integration, this is the URI of the Lambda function.

        - **PassthroughBehavior** *(string) --*

          Specifies the pass-through behavior for incoming requests based on the Content-Type
          header in the request, and the available mapping templates specified as the
          requestTemplates property on the Integration resource. There are three valid values:
          WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.

          WHEN_NO_MATCH passes the request body for unmapped content types through to the
          integration backend without transformation.

          NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.

          WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to
          templates. However, if there is at least one content type defined, unmapped content types
          will be rejected with the same HTTP 415 Unsupported Media Type response.

        - **RequestParameters** *(dict) --*

          A key-value map specifying request parameters that are passed from the method request to
          the backend. The key is an integration request parameter name and the associated value is
          a method request parameter value or static value that must be enclosed within single
          quotes and pre-encoded as required by the backend. The method request parameter value
          must match the pattern of method.request.{location}.{name} , where {location} is
          querystring, path, or header; and {name} must be a valid and unique method request
          parameter name.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-512].

        - **RequestTemplates** *(dict) --*

          Represents a map of Velocity templates that are applied on the request payload based on
          the value of the Content-Type header sent by the client. The content type value is the
          key in this map, and the template (as a String) is the value.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-32768].

        - **TemplateSelectionExpression** *(string) --*

          The template selection expression for the integration.

        - **TimeoutInMillis** *(integer) --*

          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000
          milliseconds or 29 seconds.
    """


_GetModelsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetModelsPaginatePaginationConfigTypeDef(
    _GetModelsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetModelsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetModelsPaginateResponseItemsTypeDef = TypedDict(
    "_GetModelsPaginateResponseItemsTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class GetModelsPaginateResponseItemsTypeDef(_GetModelsPaginateResponseItemsTypeDef):
    """
    Type definition for `GetModelsPaginateResponse` `Items`

    Represents a data model for an API. See `Create Models and Mapping Templates for Request
    and Response Mappings
    <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .

    - **ContentType** *(string) --*

      The content-type for the model, for example, "application/json".

    - **Description** *(string) --*

      The description of the model.

    - **ModelId** *(string) --*

      The model identifier.

    - **Name** *(string) --*

      The name of the model. Must be alphanumeric.

    - **Schema** *(string) --*

      The schema for the model. For application/json models, this should be JSON schema draft 4
      model.
    """


_GetModelsPaginateResponseTypeDef = TypedDict(
    "_GetModelsPaginateResponseTypeDef",
    {"Items": List[GetModelsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetModelsPaginateResponseTypeDef(_GetModelsPaginateResponseTypeDef):
    """
    Type definition for `GetModelsPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a data model for an API. See `Create Models and Mapping Templates for Request
        and Response Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .

        - **ContentType** *(string) --*

          The content-type for the model, for example, "application/json".

        - **Description** *(string) --*

          The description of the model.

        - **ModelId** *(string) --*

          The model identifier.

        - **Name** *(string) --*

          The name of the model. Must be alphanumeric.

        - **Schema** *(string) --*

          The schema for the model. For application/json models, this should be JSON schema draft 4
          model.
    """


_GetRouteResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRouteResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRouteResponsesPaginatePaginationConfigTypeDef(
    _GetRouteResponsesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetRouteResponsesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef(
    _GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef
):
    """
    Type definition for `GetRouteResponsesPaginateResponseItems` `ResponseParameters`

    Validation constraints imposed on parameters of a request (path, query string,
    headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_GetRouteResponsesPaginateResponseItemsTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseItemsTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class GetRouteResponsesPaginateResponseItemsTypeDef(
    _GetRouteResponsesPaginateResponseItemsTypeDef
):
    """
    Type definition for `GetRouteResponsesPaginateResponse` `Items`

    Represents a route response.

    - **ModelSelectionExpression** *(string) --*

      Represents the model selection expression of a route response.

    - **ResponseModels** *(dict) --*

      Represents the response models of a route response.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **ResponseParameters** *(dict) --*

      Represents the response parameters of a route response.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string,
          headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteResponseId** *(string) --*

      Represents the identifier of a route response.

    - **RouteResponseKey** *(string) --*

      Represents the route response key of a route response.
    """


_GetRouteResponsesPaginateResponseTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseTypeDef",
    {"Items": List[GetRouteResponsesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetRouteResponsesPaginateResponseTypeDef(
    _GetRouteResponsesPaginateResponseTypeDef
):
    """
    Type definition for `GetRouteResponsesPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a route response.

        - **ModelSelectionExpression** *(string) --*

          Represents the model selection expression of a route response.

        - **ResponseModels** *(dict) --*

          Represents the response models of a route response.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-128].

        - **ResponseParameters** *(dict) --*

          Represents the response parameters of a route response.

          - *(string) --*

            - *(dict) --*

              Validation constraints imposed on parameters of a request (path, query string,
              headers).

              - **Required** *(boolean) --*

                Whether or not the parameter is required.

        - **RouteResponseId** *(string) --*

          Represents the identifier of a route response.

        - **RouteResponseKey** *(string) --*

          Represents the route response key of a route response.
    """


_GetRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRoutesPaginatePaginationConfigTypeDef(
    _GetRoutesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetRoutesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetRoutesPaginateResponseItemsRequestParametersTypeDef = TypedDict(
    "_GetRoutesPaginateResponseItemsRequestParametersTypeDef",
    {"Required": bool},
    total=False,
)


class GetRoutesPaginateResponseItemsRequestParametersTypeDef(
    _GetRoutesPaginateResponseItemsRequestParametersTypeDef
):
    """
    Type definition for `GetRoutesPaginateResponseItems` `RequestParameters`

    Validation constraints imposed on parameters of a request (path, query string,
    headers).

    - **Required** *(boolean) --*

      Whether or not the parameter is required.
    """


_GetRoutesPaginateResponseItemsTypeDef = TypedDict(
    "_GetRoutesPaginateResponseItemsTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": str,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[
            str, GetRoutesPaginateResponseItemsRequestParametersTypeDef
        ],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class GetRoutesPaginateResponseItemsTypeDef(_GetRoutesPaginateResponseItemsTypeDef):
    """
    Type definition for `GetRoutesPaginateResponse` `Items`

    Represents a route.

    - **ApiKeyRequired** *(boolean) --*

      Specifies whether an API key is required for this route.

    - **AuthorizationScopes** *(list) --*

      A list of authorization scopes configured on a route. The scopes are used with a
      COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works
      by matching the route scopes against the scopes parsed from the access token in the
      incoming request. The method invocation is authorized if any route scope matches a
      claimed scope in the access token. Otherwise, the invocation is not authorized. When the
      route scope is configured, the client must provide an access token instead of an identity
      token for authorization purposes.

      - *(string) --*

        A string with a length between [1-64].

    - **AuthorizationType** *(string) --*

      The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
      using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

    - **AuthorizerId** *(string) --*

      The identifier of the Authorizer resource to be associated with this route, if the
      authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when
      you created the authorizer.

    - **ModelSelectionExpression** *(string) --*

      The model selection expression for the route.

    - **OperationName** *(string) --*

      The operation name for the route.

    - **RequestModels** *(dict) --*

      The request models for the route.

      - *(string) --*

        - *(string) --*

          A string with a length between [1-128].

    - **RequestParameters** *(dict) --*

      The request parameters for the route.

      - *(string) --*

        - *(dict) --*

          Validation constraints imposed on parameters of a request (path, query string,
          headers).

          - **Required** *(boolean) --*

            Whether or not the parameter is required.

    - **RouteId** *(string) --*

      The route ID.

    - **RouteKey** *(string) --*

      The route key for the route.

    - **RouteResponseSelectionExpression** *(string) --*

      The route response selection expression for the route.

    - **Target** *(string) --*

      The target for the route.
    """


_GetRoutesPaginateResponseTypeDef = TypedDict(
    "_GetRoutesPaginateResponseTypeDef",
    {"Items": List[GetRoutesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetRoutesPaginateResponseTypeDef(_GetRoutesPaginateResponseTypeDef):
    """
    Type definition for `GetRoutesPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents a route.

        - **ApiKeyRequired** *(boolean) --*

          Specifies whether an API key is required for this route.

        - **AuthorizationScopes** *(list) --*

          A list of authorization scopes configured on a route. The scopes are used with a
          COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works
          by matching the route scopes against the scopes parsed from the access token in the
          incoming request. The method invocation is authorized if any route scope matches a
          claimed scope in the access token. Otherwise, the invocation is not authorized. When the
          route scope is configured, the client must provide an access token instead of an identity
          token for authorization purposes.

          - *(string) --*

            A string with a length between [1-64].

        - **AuthorizationType** *(string) --*

          The authorization type for the route. Valid values are NONE for open access, AWS_IAM for
          using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

        - **AuthorizerId** *(string) --*

          The identifier of the Authorizer resource to be associated with this route, if the
          authorizationType is CUSTOM . The authorizer identifier is generated by API Gateway when
          you created the authorizer.

        - **ModelSelectionExpression** *(string) --*

          The model selection expression for the route.

        - **OperationName** *(string) --*

          The operation name for the route.

        - **RequestModels** *(dict) --*

          The request models for the route.

          - *(string) --*

            - *(string) --*

              A string with a length between [1-128].

        - **RequestParameters** *(dict) --*

          The request parameters for the route.

          - *(string) --*

            - *(dict) --*

              Validation constraints imposed on parameters of a request (path, query string,
              headers).

              - **Required** *(boolean) --*

                Whether or not the parameter is required.

        - **RouteId** *(string) --*

          The route ID.

        - **RouteKey** *(string) --*

          The route key for the route.

        - **RouteResponseSelectionExpression** *(string) --*

          The route response selection expression for the route.

        - **Target** *(string) --*

          The target for the route.
    """


_GetStagesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetStagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetStagesPaginatePaginationConfigTypeDef(
    _GetStagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetStagesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetStagesPaginateResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class GetStagesPaginateResponseItemsAccessLogSettingsTypeDef(
    _GetStagesPaginateResponseItemsAccessLogSettingsTypeDef
):
    """
    Type definition for `GetStagesPaginateResponseItems` `AccessLogSettings`

    Settings for logging access in this stage.

    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.

    - **Format** *(string) --*

      A single line format of the access logs of data, as specified by selected $context
      variables. The format must include at least $context.requestId.
    """


_GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef(
    _GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef
):
    """
    Type definition for `GetStagesPaginateResponseItems` `DefaultRouteSettings`

    Default route settings for the stage.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route.
      This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
      the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_GetStagesPaginateResponseItemsRouteSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class GetStagesPaginateResponseItemsRouteSettingsTypeDef(
    _GetStagesPaginateResponseItemsRouteSettingsTypeDef
):
    """
    Type definition for `GetStagesPaginateResponseItems` `RouteSettings`

    Represents a collection of route settings.

    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this
      route. This property affects the log entries pushed to Amazon CloudWatch Logs.

    - **DetailedMetricsEnabled** *(boolean) --*

      Specifies whether detailed metrics are enabled.

    - **LoggingLevel** *(string) --*

      Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
      affects the log entries pushed to Amazon CloudWatch Logs.

    - **ThrottlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit.

    - **ThrottlingRateLimit** *(float) --*

      Specifies the throttling rate limit.
    """


_GetStagesPaginateResponseItemsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsTypeDef",
    {
        "AccessLogSettings": GetStagesPaginateResponseItemsAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, GetStagesPaginateResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetStagesPaginateResponseItemsTypeDef(_GetStagesPaginateResponseItemsTypeDef):
    """
    Type definition for `GetStagesPaginateResponse` `Items`

    Represents an API stage.

    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

      - **Format** *(string) --*

        A single line format of the access logs of data, as specified by selected $context
        variables. The format must include at least $context.requestId.

    - **ClientCertificateId** *(string) --*

      The identifier of a client certificate for a Stage.

    - **CreatedDate** *(datetime) --*

      The timestamp when the stage was created.

    - **DefaultRouteSettings** *(dict) --*

      Default route settings for the stage.

      - **DataTraceEnabled** *(boolean) --*

        Specifies whether (true) or not (false) data trace logging is enabled for this route.
        This property affects the log entries pushed to Amazon CloudWatch Logs.

      - **DetailedMetricsEnabled** *(boolean) --*

        Specifies whether detailed metrics are enabled.

      - **LoggingLevel** *(string) --*

        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
        the log entries pushed to Amazon CloudWatch Logs.

      - **ThrottlingBurstLimit** *(integer) --*

        Specifies the throttling burst limit.

      - **ThrottlingRateLimit** *(float) --*

        Specifies the throttling rate limit.

    - **DeploymentId** *(string) --*

      The identifier of the Deployment that the Stage is associated with.

    - **Description** *(string) --*

      The description of the stage.

    - **LastUpdatedDate** *(datetime) --*

      The timestamp when the stage was last updated.

    - **RouteSettings** *(dict) --*

      Route settings for the stage.

      - *(string) --*

        - *(dict) --*

          Represents a collection of route settings.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this
            route. This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
            affects the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

    - **StageName** *(string) --*

      The name of the stage.

    - **StageVariables** *(dict) --*

      A map that defines the stage variables for a stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

      - *(string) --*

        - *(string) --*

          A string with a length between [0-2048].

    - **Tags** *(dict) --*

      The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
      be up to 128 characters and must not start with aws:. The tag value can be up to 256
      characters..

      - *(string) --*

        - *(string) --*

          A string with a length between [1-1600].
    """


_GetStagesPaginateResponseTypeDef = TypedDict(
    "_GetStagesPaginateResponseTypeDef",
    {"Items": List[GetStagesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetStagesPaginateResponseTypeDef(_GetStagesPaginateResponseTypeDef):
    """
    Type definition for `GetStagesPaginate` `Response`

    Success

    - **Items** *(list) --*

      The elements from this collection.

      - *(dict) --*

        Represents an API stage.

        - **AccessLogSettings** *(dict) --*

          Settings for logging access in this stage.

          - **DestinationArn** *(string) --*

            The ARN of the CloudWatch Logs log group to receive access logs.

          - **Format** *(string) --*

            A single line format of the access logs of data, as specified by selected $context
            variables. The format must include at least $context.requestId.

        - **ClientCertificateId** *(string) --*

          The identifier of a client certificate for a Stage.

        - **CreatedDate** *(datetime) --*

          The timestamp when the stage was created.

        - **DefaultRouteSettings** *(dict) --*

          Default route settings for the stage.

          - **DataTraceEnabled** *(boolean) --*

            Specifies whether (true) or not (false) data trace logging is enabled for this route.
            This property affects the log entries pushed to Amazon CloudWatch Logs.

          - **DetailedMetricsEnabled** *(boolean) --*

            Specifies whether detailed metrics are enabled.

          - **LoggingLevel** *(string) --*

            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects
            the log entries pushed to Amazon CloudWatch Logs.

          - **ThrottlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit.

          - **ThrottlingRateLimit** *(float) --*

            Specifies the throttling rate limit.

        - **DeploymentId** *(string) --*

          The identifier of the Deployment that the Stage is associated with.

        - **Description** *(string) --*

          The description of the stage.

        - **LastUpdatedDate** *(datetime) --*

          The timestamp when the stage was last updated.

        - **RouteSettings** *(dict) --*

          Route settings for the stage.

          - *(string) --*

            - *(dict) --*

              Represents a collection of route settings.

              - **DataTraceEnabled** *(boolean) --*

                Specifies whether (true) or not (false) data trace logging is enabled for this
                route. This property affects the log entries pushed to Amazon CloudWatch Logs.

              - **DetailedMetricsEnabled** *(boolean) --*

                Specifies whether detailed metrics are enabled.

              - **LoggingLevel** *(string) --*

                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
                affects the log entries pushed to Amazon CloudWatch Logs.

              - **ThrottlingBurstLimit** *(integer) --*

                Specifies the throttling burst limit.

              - **ThrottlingRateLimit** *(float) --*

                Specifies the throttling rate limit.

        - **StageName** *(string) --*

          The name of the stage.

        - **StageVariables** *(dict) --*

          A map that defines the stage variables for a stage resource. Variable names can have
          alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

          - *(string) --*

            - *(string) --*

              A string with a length between [0-2048].

        - **Tags** *(dict) --*

          The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can
          be up to 128 characters and must not start with aws:. The tag value can be up to 256
          characters..

          - *(string) --*

            - *(string) --*

              A string with a length between [1-1600].
    """
