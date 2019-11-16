"Main interface for apigateway type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateApiKeyResponseTypeDef",
    "ClientCreateApiKeystageKeysTypeDef",
    "ClientCreateBasePathMappingResponseTypeDef",
    "ClientCreateDeploymentResponseapiSummaryTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeploymentcanarySettingsTypeDef",
    "ClientCreateDocumentationPartResponselocationTypeDef",
    "ClientCreateDocumentationPartResponseTypeDef",
    "ClientCreateDocumentationPartlocationTypeDef",
    "ClientCreateDocumentationVersionResponseTypeDef",
    "ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateDomainNameendpointConfigurationTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRestApiResponseendpointConfigurationTypeDef",
    "ClientCreateRestApiResponseTypeDef",
    "ClientCreateRestApiendpointConfigurationTypeDef",
    "ClientCreateStageResponseaccessLogSettingsTypeDef",
    "ClientCreateStageResponsecanarySettingsTypeDef",
    "ClientCreateStageResponsemethodSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateStagecanarySettingsTypeDef",
    "ClientCreateUsagePlanapiStagesthrottleTypeDef",
    "ClientCreateUsagePlanapiStagesTypeDef",
    "ClientCreateUsagePlanquotaTypeDef",
    "ClientCreateUsagePlanthrottleTypeDef",
    "ClientCreateVpcLinkResponseTypeDef",
    "ClientGetAccountResponsethrottleSettingsTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetApiKeyResponseTypeDef",
    "ClientGetApiKeysResponseitemsTypeDef",
    "ClientGetApiKeysResponseTypeDef",
    "ClientGetBasePathMappingResponseTypeDef",
    "ClientGetDeploymentResponseapiSummaryTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    "ClientGetDeploymentsResponseitemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDocumentationPartResponselocationTypeDef",
    "ClientGetDocumentationPartResponseTypeDef",
    "ClientGetDocumentationPartsResponseitemslocationTypeDef",
    "ClientGetDocumentationPartsResponseitemsTypeDef",
    "ClientGetDocumentationPartsResponseTypeDef",
    "ClientGetDocumentationVersionResponseTypeDef",
    "ClientGetDocumentationVersionsResponseitemsTypeDef",
    "ClientGetDocumentationVersionsResponseTypeDef",
    "ClientGetDomainNameResponseendpointConfigurationTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseintegrationResponsesTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetMethodResponseResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelsResponseitemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRestApiResponseendpointConfigurationTypeDef",
    "ClientGetRestApiResponseTypeDef",
    "ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    "ClientGetRestApisResponseitemsTypeDef",
    "ClientGetRestApisResponseTypeDef",
    "ClientGetSdkResponseTypeDef",
    "ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    "ClientGetSdkTypeResponseTypeDef",
    "ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    "ClientGetSdkTypesResponseitemsTypeDef",
    "ClientGetSdkTypesResponseTypeDef",
    "ClientGetStageResponseaccessLogSettingsTypeDef",
    "ClientGetStageResponsecanarySettingsTypeDef",
    "ClientGetStageResponsemethodSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    "ClientGetStagesResponseitemcanarySettingsTypeDef",
    "ClientGetStagesResponseitemmethodSettingsTypeDef",
    "ClientGetStagesResponseitemTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetVpcLinkResponseTypeDef",
    "ClientImportApiKeysResponseTypeDef",
    "ClientImportDocumentationPartsResponseTypeDef",
    "ClientImportRestApiResponseendpointConfigurationTypeDef",
    "ClientImportRestApiResponseTypeDef",
    "ClientPutIntegrationResponseResponseTypeDef",
    "ClientPutIntegrationResponseintegrationResponsesTypeDef",
    "ClientPutIntegrationResponseTypeDef",
    "ClientPutMethodResponseResponseTypeDef",
    "ClientPutRestApiResponseendpointConfigurationTypeDef",
    "ClientPutRestApiResponseTypeDef",
    "ClientTestInvokeAuthorizerResponseTypeDef",
    "ClientUpdateAccountResponsethrottleSettingsTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateApiKeyResponseTypeDef",
    "ClientUpdateBasePathMappingResponseTypeDef",
    "ClientUpdateDeploymentResponseapiSummaryTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDocumentationPartResponselocationTypeDef",
    "ClientUpdateDocumentationPartResponseTypeDef",
    "ClientUpdateDocumentationVersionResponseTypeDef",
    "ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateMethodResponseResponseTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    "ClientUpdateRestApiResponseTypeDef",
    "ClientUpdateStageResponseaccessLogSettingsTypeDef",
    "ClientUpdateStageResponsecanarySettingsTypeDef",
    "ClientUpdateStageResponsemethodSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateVpcLinkResponseTypeDef",
    "GetApiKeysPaginatePaginationConfigTypeDef",
    "GetApiKeysPaginateResponseitemsTypeDef",
    "GetApiKeysPaginateResponseTypeDef",
    "GetAuthorizersPaginatePaginationConfigTypeDef",
    "GetBasePathMappingsPaginatePaginationConfigTypeDef",
    "GetClientCertificatesPaginatePaginationConfigTypeDef",
    "GetDeploymentsPaginatePaginationConfigTypeDef",
    "GetDeploymentsPaginateResponseitemsapiSummaryTypeDef",
    "GetDeploymentsPaginateResponseitemsTypeDef",
    "GetDeploymentsPaginateResponseTypeDef",
    "GetDocumentationPartsPaginatePaginationConfigTypeDef",
    "GetDocumentationPartsPaginateResponseitemslocationTypeDef",
    "GetDocumentationPartsPaginateResponseitemsTypeDef",
    "GetDocumentationPartsPaginateResponseTypeDef",
    "GetDocumentationVersionsPaginatePaginationConfigTypeDef",
    "GetDocumentationVersionsPaginateResponseitemsTypeDef",
    "GetDocumentationVersionsPaginateResponseTypeDef",
    "GetDomainNamesPaginatePaginationConfigTypeDef",
    "GetGatewayResponsesPaginatePaginationConfigTypeDef",
    "GetModelsPaginatePaginationConfigTypeDef",
    "GetModelsPaginateResponseitemsTypeDef",
    "GetModelsPaginateResponseTypeDef",
    "GetRequestValidatorsPaginatePaginationConfigTypeDef",
    "GetResourcesPaginatePaginationConfigTypeDef",
    "GetRestApisPaginatePaginationConfigTypeDef",
    "GetRestApisPaginateResponseitemsendpointConfigurationTypeDef",
    "GetRestApisPaginateResponseitemsTypeDef",
    "GetRestApisPaginateResponseTypeDef",
    "GetSdkTypesPaginatePaginationConfigTypeDef",
    "GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef",
    "GetSdkTypesPaginateResponseitemsTypeDef",
    "GetSdkTypesPaginateResponseTypeDef",
    "GetUsagePaginatePaginationConfigTypeDef",
    "GetUsagePlanKeysPaginatePaginationConfigTypeDef",
    "GetUsagePlansPaginatePaginationConfigTypeDef",
    "GetVpcLinksPaginatePaginationConfigTypeDef",
)


_ClientCreateApiKeyResponseTypeDef = TypedDict(
    "_ClientCreateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateApiKeyResponseTypeDef(_ClientCreateApiKeyResponseTypeDef):
    """
    Type definition for `ClientCreateApiKey` `Response`

    A resource that can be distributed to callers for executing  Method resources that require an
    API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
    callers with the API key can make requests to that stage.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **id** *(string) --*

      The identifier of the API Key.

    - **value** *(string) --*

      The value of the API Key.

    - **name** *(string) --*

      The name of the API Key.

    - **customerId** *(string) --*

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    - **description** *(string) --*

      The description of the API Key.

    - **enabled** *(boolean) --*

      Specifies whether the API Key can be used by callers.

    - **createdDate** *(datetime) --*

      The timestamp when the API Key was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the API Key was last updated.

    - **stageKeys** *(list) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

      - *(string) --*

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateApiKeystageKeysTypeDef = TypedDict(
    "_ClientCreateApiKeystageKeysTypeDef",
    {"restApiId": str, "stageName": str},
    total=False,
)


class ClientCreateApiKeystageKeysTypeDef(_ClientCreateApiKeystageKeysTypeDef):
    """
    Type definition for `ClientCreateApiKey` `stageKeys`

    A reference to a unique stage identified in the format ``{restApiId}/{stage}`` .

    - **restApiId** *(string) --*

      The string identifier of the associated  RestApi .

    - **stageName** *(string) --*

      The stage name associated with the stage key.
    """


_ClientCreateBasePathMappingResponseTypeDef = TypedDict(
    "_ClientCreateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientCreateBasePathMappingResponseTypeDef(
    _ClientCreateBasePathMappingResponseTypeDef
):
    """
    Type definition for `ClientCreateBasePathMapping` `Response`

    Represents the base path that callers of the API must provide as part of the URL after the
    domain name.

     A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
     in a given stage of the owner  Account .  `Use Custom Domain Names
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **basePath** *(string) --*

      The base path name that callers of the API must provide as part of the URL after the domain
      name.

    - **restApiId** *(string) --*

      The string identifier of the associated  RestApi .

    - **stage** *(string) --*

      The name of the associated stage.
    """


_ClientCreateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientCreateDeploymentResponseapiSummaryTypeDef(
    _ClientCreateDeploymentResponseapiSummaryTypeDef
):
    """
    Type definition for `ClientCreateDeploymentResponse` `apiSummary`

    Represents a summary of a  Method resource, given a particular date and time.

    - **authorizationType** *(string) --*

      The method's authorization type. Valid values are ``NONE`` for open access,
      ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
      authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

    - **apiKeyRequired** *(boolean) --*

      Specifies whether the method requires a valid  ApiKey .
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[
            str, Dict[str, ClientCreateDeploymentResponseapiSummaryTypeDef]
        ],
    },
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

    An immutable representation of a  RestApi resource that can be called by users using  Stages .
    A deployment must be associated with a  Stage for it to be callable over the Internet.

     To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
     update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
     deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
     Deployments ,  Stage , `AWS CLI
     <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
     SDKs <https://aws.amazon.com/tools/>`__

    - **id** *(string) --*

      The identifier for the deployment resource.

    - **description** *(string) --*

      The description for the deployment resource.

    - **createdDate** *(datetime) --*

      The date and time that the deployment resource was created.

    - **apiSummary** *(dict) --*

      A summary of the  RestApi at the date and time that the deployment resource was created.

      - *(string) --*

        - *(dict) --*

          - *(string) --*

            - *(dict) --*

              Represents a summary of a  Method resource, given a particular date and time.

              - **authorizationType** *(string) --*

                The method's authorization type. Valid values are ``NONE`` for open access,
                ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

              - **apiKeyRequired** *(boolean) --*

                Specifies whether the method requires a valid  ApiKey .
    """


_ClientCreateDeploymentcanarySettingsTypeDef = TypedDict(
    "_ClientCreateDeploymentcanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientCreateDeploymentcanarySettingsTypeDef(
    _ClientCreateDeploymentcanarySettingsTypeDef
):
    """
    Type definition for `ClientCreateDeployment` `canarySettings`

    The input configuration for the canary deployment when the deployment is a canary release
    deployment.

    - **percentTraffic** *(float) --*

      The percentage (0.0-100.0) of traffic routed to the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      A stage variable overrides used for the canary release deployment. They can override existing
      stage variables or add new stage variables for the canary release deployment. These stage
      variables are represented as a string-to-string map between stage variable names and their
      values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.
    """


_ClientCreateDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientCreateDocumentationPartResponselocationTypeDef",
    {"type": str, "path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientCreateDocumentationPartResponselocationTypeDef(
    _ClientCreateDocumentationPartResponselocationTypeDef
):
    """
    Type definition for `ClientCreateDocumentationPartResponse` `location`

    The location of the API entity to which the documentation applies. Valid fields depend on the
    targeted API entity type. All the valid location fields are not required. If not explicitly
    specified, a valid location field is treated as a wildcard and associated documentation
    content may be inherited by matching entities, unless overridden.

    - **type** *(string) --*

      [Required] The type of API entity to which the documentation content applies. Valid values
      are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
      ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
      ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
      entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
      ``RESOURCE`` type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
      ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
      ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
      value is ``/`` for the root resource. When an applicable child entity inherits the content
      of another entity of the same type with more general specifications of the other
      ``location`` attributes, the child entity's ``path`` attribute must match that of the
      parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any method. When an applicable child entity inherits the content of an entity of the same
      type with more general specifications of the other ``location`` attributes, the child
      entity's ``method`` attribute must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any status code. When an applicable child entity inherits the content of an entity of the
      same type with more general specifications of the other ``location`` attributes, the child
      entity's ``statusCode`` attribute must match that of the parent entity exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API entity
      types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
      any other entity type.
    """


_ClientCreateDocumentationPartResponseTypeDef = TypedDict(
    "_ClientCreateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientCreateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientCreateDocumentationPartResponseTypeDef(
    _ClientCreateDocumentationPartResponseTypeDef
):
    """
    Type definition for `ClientCreateDocumentationPart` `Response`

    A documentation part for a targeted API entity.

    A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
    The target specifies an API entity to which the documentation content applies. The supported
    API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
    ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE``
    , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API
    entity type. All valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an API can use any
    shape for the content map, only the OpenAPI-compliant documentation fields will be injected
    into the associated API entity definition in the exported OpenAPI definition file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationParts

    - **id** *(string) --*

      The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is
      created.

    - **location** *(dict) --*

      The location of the API entity to which the documentation applies. Valid fields depend on the
      targeted API entity type. All the valid location fields are not required. If not explicitly
      specified, a valid location field is treated as a wildcard and associated documentation
      content may be inherited by matching entities, unless overridden.

      - **type** *(string) --*

        [Required] The type of API entity to which the documentation content applies. Valid values
        are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
        ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
        ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
        entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
        ``RESOURCE`` type.

      - **path** *(string) --*

        The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
        ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
        ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
        value is ``/`` for the root resource. When an applicable child entity inherits the content
        of another entity of the same type with more general specifications of the other
        ``location`` attributes, the child entity's ``path`` attribute must match that of the
        parent entity as a prefix.

      - **method** *(string) --*

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any method. When an applicable child entity inherits the content of an entity of the same
        type with more general specifications of the other ``location`` attributes, the child
        entity's ``method`` attribute must match that of the parent entity exactly.

      - **statusCode** *(string) --*

        The HTTP status code of a response. It is a valid field for the API entity types of
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any status code. When an applicable child entity inherits the content of an entity of the
        same type with more general specifications of the other ``location`` attributes, the child
        entity's ``statusCode`` attribute must match that of the parent entity exactly.

      - **name** *(string) --*

        The name of the targeted API entity. It is a valid and required field for the API entity
        types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
        any other entity type.

    - **properties** *(string) --*

      A content map of API-specific key-value pairs describing the targeted API entity. The map
      must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\" }"`` .
      Only OpenAPI-compliant documentation-related fields from the propertiesmap are exported and,
      hence, published as part of the API entity definitions, while the original documentation
      parts are exported in a OpenAPI extension of ``x-amazon-apigateway-documentation`` .
    """


_RequiredClientCreateDocumentationPartlocationTypeDef = TypedDict(
    "_RequiredClientCreateDocumentationPartlocationTypeDef", {"type": str}
)
_OptionalClientCreateDocumentationPartlocationTypeDef = TypedDict(
    "_OptionalClientCreateDocumentationPartlocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientCreateDocumentationPartlocationTypeDef(
    _RequiredClientCreateDocumentationPartlocationTypeDef,
    _OptionalClientCreateDocumentationPartlocationTypeDef,
):
    """
    Type definition for `ClientCreateDocumentationPart` `location`

    [Required] The location of the targeted API entity of the to-be-created documentation part.

    - **type** *(string) --* **[REQUIRED]**

      [Required] The type of API entity to which the documentation content applies. Valid values are
      ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
      ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
      ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity
      of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE``
      type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
      ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``/`` for the
      root resource. When an applicable child entity inherits the content of another entity of the
      same type with more general specifications of the other ``location`` attributes, the child
      entity's ``path`` attribute must match that of the parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE``
      , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any method. When
      an applicable child entity inherits the content of an entity of the same type with more general
      specifications of the other ``location`` attributes, the child entity's ``method`` attribute
      must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for any
      status code. When an applicable child entity inherits the content of an entity of the same type
      with more general specifications of the other ``location`` attributes, the child entity's
      ``statusCode`` attribute must match that of the parent entity exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API entity types
      of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
      ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.
    """


_ClientCreateDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientCreateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientCreateDocumentationVersionResponseTypeDef(
    _ClientCreateDocumentationVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateDocumentationVersion` `Response`

    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version associated with an API
    stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersions

    - **version** *(string) --*

      The version identifier of the API documentation snapshot.

    - **createdDate** *(datetime) --*

      The date when the API documentation snapshot is created.

    - **description** *(string) --*

      The description of the API documentation snapshot.
    """


_ClientCreateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateDomainNameResponseendpointConfigurationTypeDef(
    _ClientCreateDomainNameResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDomainNameResponse` `endpointConfiguration`

    The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientCreateDomainNameResponseTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientCreateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": str,
        "domainNameStatusMessage": str,
        "securityPolicy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateDomainNameResponseTypeDef(_ClientCreateDomainNameResponseTypeDef):
    """
    Type definition for `ClientCreateDomainName` `Response`

    Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

    When you deploy an API, API Gateway creates a default host name for the API. This default API
    host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
    default host name, you can access the API's root resource with the URL of
    ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom
    domain name of ``apis.example.com`` for this API, you can then access the same resource using
    the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping (
    BasePathMapping ) of your API under the custom domain name.

       `Set a Custom Host Name for an API
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **domainName** *(string) --*

      The custom domain name as an API host name, for example, ``my-api.example.com`` .

    - **certificateName** *(string) --*

      The name of the certificate that will be used by edge-optimized endpoint for this domain name.

    - **certificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for
      this domain name. AWS Certificate Manager is the only supported source.

    - **certificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this domain
      name was uploaded.

    - **regionalDomainName** *(string) --*

      The domain name associated with the regional endpoint for this custom domain name. You set up
      this association by adding a DNS record that points the custom domain name to this regional
      domain name. The regional domain name is returned by API Gateway when you create a regional
      endpoint.

    - **regionalHostedZoneId** *(string) --*

      The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more
      information, see `Set up a Regional Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **regionalCertificateName** *(string) --*

      The name of the certificate that will be used for validating the regional domain name.

    - **regionalCertificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used for validating the regional
      domain name. AWS Certificate Manager is the only supported source.

    - **distributionDomainName** *(string) --*

      The domain name of the Amazon CloudFront distribution associated with this custom domain name
      for an edge-optimized endpoint. You set up this association when adding a DNS record pointing
      the custom domain name to this distribution name. For more information about CloudFront
      distributions, see the `Amazon CloudFront documentation
      <https://aws.amazon.com/documentation/cloudfront/>`__ .

    - **distributionHostedZoneId** *(string) --*

      The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid
      value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional
      Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **domainNameStatus** *(string) --*

      The status of the  DomainName migration. The valid values are ``AVAILABLE`` and ``UPDATING``
      . If the status is ``UPDATING`` , the domain cannot be modified further until the existing
      operation is complete. If it is ``AVAILABLE`` , the domain can be updated.

    - **domainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the  DomainName
      migration.

    - **securityPolicy** *(string) --*

      The Transport Layer Security (TLS) version + cipher suite for this  DomainName . The valid
      values are ``TLS_1_0`` and ``TLS_1_2`` .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateDomainNameendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateDomainNameendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateDomainNameendpointConfigurationTypeDef(
    _ClientCreateDomainNameendpointConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDomainName` `endpointConfiguration`

    The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an
      edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional
      API and its custom domain name, the endpoint type is ``REGIONAL`` . For a private API, the
      endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most suitable
        for mobile applications; ``REGIONAL`` for regional API endpoint setup, most suitable for
        calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It is
      only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientCreateModelResponseTypeDef = TypedDict(
    "_ClientCreateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientCreateModelResponseTypeDef(_ClientCreateModelResponseTypeDef):
    """
    Type definition for `ClientCreateModel` `Response`

    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request payload. A response
    model defines the data structure of the response payload returned by the back end. Although not
    required, models are useful for mapping payloads between the front end and back end.

    A model is used for generating an API's SDK, validating the input request body, and creating a
    skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **id** *(string) --*

      The identifier for the model resource.

    - **name** *(string) --*

      The name of the model. Must be an alphanumeric string.

    - **description** *(string) --*

      The description of the model.

    - **schema** *(string) --*

      The schema for the model. For ``application/json`` models, this should be `JSON schema draft
      4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include "\\*/"
      characters in the description of any properties because such "\\*/" characters may be
      interpreted as the closing marker for comments in some languages, such as Java or JavaScript,
      causing the installation of your API's SDK generated by API Gateway to fail.

    - **contentType** *(string) --*

      The content-type for the model.
    """


_ClientCreateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateRestApiResponseendpointConfigurationTypeDef(
    _ClientCreateRestApiResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientCreateRestApiResponse` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientCreateRestApiResponseTypeDef = TypedDict(
    "_ClientCreateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientCreateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRestApiResponseTypeDef(_ClientCreateRestApiResponseTypeDef):
    """
    Type definition for `ClientCreateRestApi` `Response`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports
      only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When
      compression is enabled, compression or decompression is not applied on the payload if the
      payload size is smaller than this value. Setting it to zero allows compression for any
      payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateRestApiendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateRestApiendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateRestApiendpointConfigurationTypeDef(
    _ClientCreateRestApiendpointConfigurationTypeDef
):
    """
    Type definition for `ClientCreateRestApi` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an
      edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a regional
      API and its custom domain name, the endpoint type is ``REGIONAL`` . For a private API, the
      endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most suitable
        for mobile applications; ``REGIONAL`` for regional API endpoint setup, most suitable for
        calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It is
      only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientCreateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientCreateStageResponseaccessLogSettingsTypeDef(
    _ClientCreateStageResponseaccessLogSettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `accessLogSettings`

    Settings for logging access in this stage.

    - **format** *(string) --*

      A single line format of the access logs of data, as specified by selected `$context
      variables
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
      . The format must include at least ``$context.requestId`` .

    - **destinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientCreateStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientCreateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientCreateStageResponsecanarySettingsTypeDef(
    _ClientCreateStageResponsecanarySettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `canarySettings`

    Settings for the canary deployment in this stage.

    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.

    - **deploymentId** *(string) --*

      The ID of the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      Stage variables overridden for a canary release deployment, including new stage variables
      introduced in the canary. These stage variables are represented as a string-to-string map
      between stage variable names and their values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
    """


_ClientCreateStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": str,
    },
    total=False,
)


class ClientCreateStageResponsemethodSettingsTypeDef(
    _ClientCreateStageResponsemethodSettingsTypeDef
):
    """
    Type definition for `ClientCreateStageResponse` `methodSettings`

    Specifies the method setting properties.

    - **metricsEnabled** *(boolean) --*

      Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
      for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
      Boolean.

    - **loggingLevel** *(string) --*

      Specifies the logging level for this method, which affects the log entries pushed to
      Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
      ``ERROR`` , and ``INFO`` .

    - **dataTraceEnabled** *(boolean) --*

      Specifies whether data trace logging is enabled for this method, which affects the log
      entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

    - **throttlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

    - **throttlingRateLimit** *(float) --*

      Specifies the throttling rate limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

    - **cachingEnabled** *(boolean) --*

      Specifies whether responses should be cached and returned for requests. A cache cluster
      must be enabled on the stage for responses to be cached. The PATCH path for this
      setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

    - **cacheTtlInSeconds** *(integer) --*

      Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
      the longer the response will be cached. The PATCH path for this setting is
      ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

    - **cacheDataEncrypted** *(boolean) --*

      Specifies whether the cached responses are encrypted. The PATCH path for this setting
      is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

    - **requireAuthorizationForCacheControl** *(boolean) --*

      Specifies whether authorization is required for a cache invalidation request. The PATCH
      path for this setting is
      ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
      is a Boolean.

    - **unauthorizedCacheControlHeaderStrategy** *(string) --*

      Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
      for this setting is
      ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
      available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
      ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .
    """


_ClientCreateStageResponseTypeDef = TypedDict(
    "_ClientCreateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": str,
        "cacheClusterStatus": str,
        "methodSettings": Dict[str, ClientCreateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientCreateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientCreateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientCreateStageResponseTypeDef(_ClientCreateStageResponseTypeDef):
    """
    Type definition for `ClientCreateStage` `Response`

    Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

      `Deploy an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__

    - **deploymentId** *(string) --*

      The identifier of the  Deployment that the stage points to.

    - **clientCertificateId** *(string) --*

      The identifier of a client certificate for an API stage.

    - **stageName** *(string) --*

      The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a
      call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and
      underscores. Maximum length is 128 characters.

    - **description** *(string) --*

      The stage's description.

    - **cacheClusterEnabled** *(boolean) --*

      Specifies whether a cache cluster is enabled for the stage.

    - **cacheClusterSize** *(string) --*

      The size of the cache cluster for the stage, if enabled.

    - **cacheClusterStatus** *(string) --*

      The status of the cache cluster for the stage, if enabled.

    - **methodSettings** *(dict) --*

      A map that defines the method settings for a  Stage resource. Keys (designated as
      ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}``
      for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.

      - *(string) --*

        - *(dict) --*

          Specifies the method setting properties.

          - **metricsEnabled** *(boolean) --*

            Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
            for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
            Boolean.

          - **loggingLevel** *(string) --*

            Specifies the logging level for this method, which affects the log entries pushed to
            Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
            ``ERROR`` , and ``INFO`` .

          - **dataTraceEnabled** *(boolean) --*

            Specifies whether data trace logging is enabled for this method, which affects the log
            entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

          - **throttlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

          - **throttlingRateLimit** *(float) --*

            Specifies the throttling rate limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

          - **cachingEnabled** *(boolean) --*

            Specifies whether responses should be cached and returned for requests. A cache cluster
            must be enabled on the stage for responses to be cached. The PATCH path for this
            setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

          - **cacheTtlInSeconds** *(integer) --*

            Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
            the longer the response will be cached. The PATCH path for this setting is
            ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

          - **cacheDataEncrypted** *(boolean) --*

            Specifies whether the cached responses are encrypted. The PATCH path for this setting
            is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

          - **requireAuthorizationForCacheControl** *(boolean) --*

            Specifies whether authorization is required for a cache invalidation request. The PATCH
            path for this setting is
            ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
            is a Boolean.

          - **unauthorizedCacheControlHeaderStrategy** *(string) --*

            Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
            for this setting is
            ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
            available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
            ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

    - **variables** *(dict) --*

      A map that defines the stage variables for a  Stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+``
      .

      - *(string) --*

        - *(string) --*

    - **documentationVersion** *(string) --*

      The version of the associated API documentation.

    - **accessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **format** *(string) --*

        A single line format of the access logs of data, as specified by selected `$context
        variables
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
        . The format must include at least ``$context.requestId`` .

      - **destinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

    - **canarySettings** *(dict) --*

      Settings for the canary deployment in this stage.

      - **percentTraffic** *(float) --*

        The percent (0-100) of traffic diverted to a canary deployment.

      - **deploymentId** *(string) --*

        The ID of the canary deployment.

      - **stageVariableOverrides** *(dict) --*

        Stage variables overridden for a canary release deployment, including new stage variables
        introduced in the canary. These stage variables are represented as a string-to-string map
        between stage variable names and their values.

        - *(string) --*

          - *(string) --*

      - **useStageCache** *(boolean) --*

        A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

    - **tracingEnabled** *(boolean) --*

      Specifies whether active tracing with X-ray is enabled for the  Stage .

    - **webAclArn** *(string) --*

      The ARN of the WebAcl associated with the  Stage .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*

    - **createdDate** *(datetime) --*

      The timestamp when the stage was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the stage last updated.
    """


_ClientCreateStagecanarySettingsTypeDef = TypedDict(
    "_ClientCreateStagecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientCreateStagecanarySettingsTypeDef(_ClientCreateStagecanarySettingsTypeDef):
    """
    Type definition for `ClientCreateStage` `canarySettings`

    The canary deployment settings of this stage.

    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.

    - **deploymentId** *(string) --*

      The ID of the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      Stage variables overridden for a canary release deployment, including new stage variables
      introduced in the canary. These stage variables are represented as a string-to-string map
      between stage variable names and their values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
    """


_ClientCreateUsagePlanapiStagesthrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientCreateUsagePlanapiStagesthrottleTypeDef(
    _ClientCreateUsagePlanapiStagesthrottleTypeDef
):
    """
    Type definition for `ClientCreateUsagePlanapiStages` `throttle`

    The API request rate limits.

    - **burstLimit** *(integer) --*

      The API request burst limit, the maximum rate limit over a time ranging from one to a
      few seconds, depending upon whether the underlying token bucket is at its full capacity.

    - **rateLimit** *(float) --*

      The API request steady-state rate limit.
    """


_ClientCreateUsagePlanapiStagesTypeDef = TypedDict(
    "_ClientCreateUsagePlanapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientCreateUsagePlanapiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientCreateUsagePlanapiStagesTypeDef(_ClientCreateUsagePlanapiStagesTypeDef):
    """
    Type definition for `ClientCreateUsagePlan` `apiStages`

    API stage name of the associated API stage in a usage plan.

    - **apiId** *(string) --*

      API Id of the associated API stage in a usage plan.

    - **stage** *(string) --*

      API stage name of the associated API stage in a usage plan.

    - **throttle** *(dict) --*

      Map containing method level throttling information for API stage in a usage plan.

      - *(string) --*

        - *(dict) --*

          The API request rate limits.

          - **burstLimit** *(integer) --*

            The API request burst limit, the maximum rate limit over a time ranging from one to a
            few seconds, depending upon whether the underlying token bucket is at its full capacity.

          - **rateLimit** *(float) --*

            The API request steady-state rate limit.
    """


_ClientCreateUsagePlanquotaTypeDef = TypedDict(
    "_ClientCreateUsagePlanquotaTypeDef",
    {"limit": int, "offset": int, "period": str},
    total=False,
)


class ClientCreateUsagePlanquotaTypeDef(_ClientCreateUsagePlanquotaTypeDef):
    """
    Type definition for `ClientCreateUsagePlan` `quota`

    The quota of the usage plan.

    - **limit** *(integer) --*

      The maximum number of requests that can be made in a given time period.

    - **offset** *(integer) --*

      The number of requests subtracted from the given limit in the initial time period.

    - **period** *(string) --*

      The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
    """


_ClientCreateUsagePlanthrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientCreateUsagePlanthrottleTypeDef(_ClientCreateUsagePlanthrottleTypeDef):
    """
    Type definition for `ClientCreateUsagePlan` `throttle`

    The throttling limits of the usage plan.

    - **burstLimit** *(integer) --*

      The API request burst limit, the maximum rate limit over a time ranging from one to a few
      seconds, depending upon whether the underlying token bucket is at its full capacity.

    - **rateLimit** *(float) --*

      The API request steady-state rate limit.
    """


_ClientCreateVpcLinkResponseTypeDef = TypedDict(
    "_ClientCreateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": str,
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateVpcLinkResponseTypeDef(_ClientCreateVpcLinkResponseTypeDef):
    """
    Type definition for `ClientCreateVpcLink` `Response`

    A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
    (VPC).

    To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
    you, as an API developer, create a  VpcLink resource targeted for one or more network load
    balancers of the VPC and then integrate an API method with a private integration that uses the
    VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has
    a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
    identify the  VpcLink used.

    - **id** *(string) --*

      The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

    - **name** *(string) --*

      The name used to label and identify the VPC link.

    - **description** *(string) --*

      The description of the VPC link.

    - **targetArns** *(list) --*

      The ARNs of network load balancers of the VPC targeted by the VPC link. The network load
      balancers must be owned by the same AWS account of the API owner.

      - *(string) --*

    - **status** *(string) --*

      The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` ,
      or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the
      status is ``DELETING`` .

    - **statusMessage** *(string) --*

      A description about the VPC link status.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetAccountResponsethrottleSettingsTypeDef = TypedDict(
    "_ClientGetAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetAccountResponsethrottleSettingsTypeDef(
    _ClientGetAccountResponsethrottleSettingsTypeDef
):
    """
    Type definition for `ClientGetAccountResponse` `throttleSettings`

    Specifies the API request limits configured for the current  Account .

    - **burstLimit** *(integer) --*

      The API request burst limit, the maximum rate limit over a time ranging from one to a few
      seconds, depending upon whether the underlying token bucket is at its full capacity.

    - **rateLimit** *(float) --*

      The API request steady-state rate limit.
    """


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientGetAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    Type definition for `ClientGetAccount` `Response`

    Represents an AWS account that is associated with API Gateway.

    To view the account info, call ``GET`` on this resource.

     Error Codes

    The following exception may be thrown when the request fails.

    * UnauthorizedException

    * NotFoundException

    * TooManyRequestsException

    For detailed error code information, including the corresponding HTTP Status Codes, see `API
    Gateway Error Codes
    <https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/#api-error-codes>`__

     Example: Get the information about an account. Request ``GET /account HTTP/1.1 Content-Type:
     application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z
     Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request,
     SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

    The successful response returns a ``200 OK`` status code and a payload similar to the following:

     ``{ "_links": { "curies": { "href":
     "https://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html",
     "name": "account", "templated": true }, "self": { "href": "/account" }, "account:update": {
     "href": "/account" } }, "cloudwatchRoleArn":
     "arn:aws:iam::123456789012:role/apigAwsProxyRole", "throttleSettings": { "rateLimit": 500,
     "burstLimit": 1000 } }``

    In addition to making the REST API call directly, you can use the AWS CLI and an AWS SDK to
    access this resource.

       `API Gateway Limits
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-limits.html>`__
       `Developer Guide
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__ , `AWS CLI
       <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-account.html>`__

    - **cloudwatchRoleArn** *(string) --*

      The ARN of an Amazon CloudWatch role for the current  Account .

    - **throttleSettings** *(dict) --*

      Specifies the API request limits configured for the current  Account .

      - **burstLimit** *(integer) --*

        The API request burst limit, the maximum rate limit over a time ranging from one to a few
        seconds, depending upon whether the underlying token bucket is at its full capacity.

      - **rateLimit** *(float) --*

        The API request steady-state rate limit.

    - **features** *(list) --*

      A list of features supported for the account. When usage plans are enabled, the features list
      will include an entry of ``"UsagePlans"`` .

      - *(string) --*

    - **apiKeyVersion** *(string) --*

      The version of the API keys used for the account.
    """


_ClientGetApiKeyResponseTypeDef = TypedDict(
    "_ClientGetApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiKeyResponseTypeDef(_ClientGetApiKeyResponseTypeDef):
    """
    Type definition for `ClientGetApiKey` `Response`

    A resource that can be distributed to callers for executing  Method resources that require an
    API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
    callers with the API key can make requests to that stage.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **id** *(string) --*

      The identifier of the API Key.

    - **value** *(string) --*

      The value of the API Key.

    - **name** *(string) --*

      The name of the API Key.

    - **customerId** *(string) --*

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    - **description** *(string) --*

      The description of the API Key.

    - **enabled** *(boolean) --*

      Specifies whether the API Key can be used by callers.

    - **createdDate** *(datetime) --*

      The timestamp when the API Key was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the API Key was last updated.

    - **stageKeys** *(list) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

      - *(string) --*

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetApiKeysResponseitemsTypeDef = TypedDict(
    "_ClientGetApiKeysResponseitemsTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiKeysResponseitemsTypeDef(_ClientGetApiKeysResponseitemsTypeDef):
    """
    Type definition for `ClientGetApiKeysResponse` `items`

    A resource that can be distributed to callers for executing  Method resources that require
    an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
    callers with the API key can make requests to that stage.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **id** *(string) --*

      The identifier of the API Key.

    - **value** *(string) --*

      The value of the API Key.

    - **name** *(string) --*

      The name of the API Key.

    - **customerId** *(string) --*

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    - **description** *(string) --*

      The description of the API Key.

    - **enabled** *(boolean) --*

      Specifies whether the API Key can be used by callers.

    - **createdDate** *(datetime) --*

      The timestamp when the API Key was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the API Key was last updated.

    - **stageKeys** *(list) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

      - *(string) --*

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetApiKeysResponseTypeDef = TypedDict(
    "_ClientGetApiKeysResponseTypeDef",
    {
        "warnings": List[str],
        "position": str,
        "items": List[ClientGetApiKeysResponseitemsTypeDef],
    },
    total=False,
)


class ClientGetApiKeysResponseTypeDef(_ClientGetApiKeysResponseTypeDef):
    """
    Type definition for `ClientGetApiKeys` `Response`

    Represents a collection of API keys as represented by an  ApiKeys resource.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **warnings** *(list) --*

      A list of warning messages logged during the import of API keys when the ``failOnWarnings``
      option is set to true.

      - *(string) --*

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A resource that can be distributed to callers for executing  Method resources that require
        an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
        callers with the API key can make requests to that stage.

          `Use API Keys
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

        - **id** *(string) --*

          The identifier of the API Key.

        - **value** *(string) --*

          The value of the API Key.

        - **name** *(string) --*

          The name of the API Key.

        - **customerId** *(string) --*

          An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

        - **description** *(string) --*

          The description of the API Key.

        - **enabled** *(boolean) --*

          Specifies whether the API Key can be used by callers.

        - **createdDate** *(datetime) --*

          The timestamp when the API Key was created.

        - **lastUpdatedDate** *(datetime) --*

          The timestamp when the API Key was last updated.

        - **stageKeys** *(list) --*

          A list of  Stage resources that are associated with the  ApiKey resource.

          - *(string) --*

        - **tags** *(dict) --*

          The collection of tags. Each tag element is associated with a given resource.

          - *(string) --*

            - *(string) --*
    """


_ClientGetBasePathMappingResponseTypeDef = TypedDict(
    "_ClientGetBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientGetBasePathMappingResponseTypeDef(_ClientGetBasePathMappingResponseTypeDef):
    """
    Type definition for `ClientGetBasePathMapping` `Response`

    Represents the base path that callers of the API must provide as part of the URL after the
    domain name.

     A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
     in a given stage of the owner  Account .  `Use Custom Domain Names
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **basePath** *(string) --*

      The base path name that callers of the API must provide as part of the URL after the domain
      name.

    - **restApiId** *(string) --*

      The string identifier of the associated  RestApi .

    - **stage** *(string) --*

      The name of the associated stage.
    """


_ClientGetDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientGetDeploymentResponseapiSummaryTypeDef(
    _ClientGetDeploymentResponseapiSummaryTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponse` `apiSummary`

    Represents a summary of a  Method resource, given a particular date and time.

    - **authorizationType** *(string) --*

      The method's authorization type. Valid values are ``NONE`` for open access,
      ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
      authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

    - **apiKeyRequired** *(boolean) --*

      Specifies whether the method requires a valid  ApiKey .
    """


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[
            str, Dict[str, ClientGetDeploymentResponseapiSummaryTypeDef]
        ],
    },
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    Type definition for `ClientGetDeployment` `Response`

    An immutable representation of a  RestApi resource that can be called by users using  Stages .
    A deployment must be associated with a  Stage for it to be callable over the Internet.

     To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
     update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
     deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
     Deployments ,  Stage , `AWS CLI
     <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
     SDKs <https://aws.amazon.com/tools/>`__

    - **id** *(string) --*

      The identifier for the deployment resource.

    - **description** *(string) --*

      The description for the deployment resource.

    - **createdDate** *(datetime) --*

      The date and time that the deployment resource was created.

    - **apiSummary** *(dict) --*

      A summary of the  RestApi at the date and time that the deployment resource was created.

      - *(string) --*

        - *(dict) --*

          - *(string) --*

            - *(dict) --*

              Represents a summary of a  Method resource, given a particular date and time.

              - **authorizationType** *(string) --*

                The method's authorization type. Valid values are ``NONE`` for open access,
                ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

              - **apiKeyRequired** *(boolean) --*

                Specifies whether the method requires a valid  ApiKey .
    """


_ClientGetDeploymentsResponseitemsapiSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientGetDeploymentsResponseitemsapiSummaryTypeDef(
    _ClientGetDeploymentsResponseitemsapiSummaryTypeDef
):
    """
    Type definition for `ClientGetDeploymentsResponseitems` `apiSummary`

    Represents a summary of a  Method resource, given a particular date and time.

    - **authorizationType** *(string) --*

      The method's authorization type. Valid values are ``NONE`` for open access,
      ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
      authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

    - **apiKeyRequired** *(boolean) --*

      Specifies whether the method requires a valid  ApiKey .
    """


_ClientGetDeploymentsResponseitemsTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseitemsTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[
            str, Dict[str, ClientGetDeploymentsResponseitemsapiSummaryTypeDef]
        ],
    },
    total=False,
)


class ClientGetDeploymentsResponseitemsTypeDef(
    _ClientGetDeploymentsResponseitemsTypeDef
):
    """
    Type definition for `ClientGetDeploymentsResponse` `items`

    An immutable representation of a  RestApi resource that can be called by users using
    Stages . A deployment must be associated with a  Stage for it to be callable over the
    Internet.

     To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To
     view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the
     specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).
     RestApi ,  Deployments ,  Stage , `AWS CLI
     <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ ,
     `AWS SDKs <https://aws.amazon.com/tools/>`__

    - **id** *(string) --*

      The identifier for the deployment resource.

    - **description** *(string) --*

      The description for the deployment resource.

    - **createdDate** *(datetime) --*

      The date and time that the deployment resource was created.

    - **apiSummary** *(dict) --*

      A summary of the  RestApi at the date and time that the deployment resource was created.

      - *(string) --*

        - *(dict) --*

          - *(string) --*

            - *(dict) --*

              Represents a summary of a  Method resource, given a particular date and time.

              - **authorizationType** *(string) --*

                The method's authorization type. Valid values are ``NONE`` for open access,
                ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

              - **apiKeyRequired** *(boolean) --*

                Specifies whether the method requires a valid  ApiKey .
    """


_ClientGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseTypeDef",
    {"position": str, "items": List[ClientGetDeploymentsResponseitemsTypeDef]},
    total=False,
)


class ClientGetDeploymentsResponseTypeDef(_ClientGetDeploymentsResponseTypeDef):
    """
    Type definition for `ClientGetDeployments` `Response`

    Represents a collection resource that contains zero or more references to your existing
    deployments, and links that guide you on how to interact with your collection. The collection
    offers a paginated view of the contained deployments.

     To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To
     view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE``
     request, respectively, on a specified  Deployment resource.  `Deploying an API
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ ,
     `AWS CLI <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__
     , `AWS SDKs <https://aws.amazon.com/tools/>`__

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        An immutable representation of a  RestApi resource that can be called by users using
        Stages . A deployment must be associated with a  Stage for it to be callable over the
        Internet.

         To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To
         view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the
         specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).
         RestApi ,  Deployments ,  Stage , `AWS CLI
         <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ ,
         `AWS SDKs <https://aws.amazon.com/tools/>`__

        - **id** *(string) --*

          The identifier for the deployment resource.

        - **description** *(string) --*

          The description for the deployment resource.

        - **createdDate** *(datetime) --*

          The date and time that the deployment resource was created.

        - **apiSummary** *(dict) --*

          A summary of the  RestApi at the date and time that the deployment resource was created.

          - *(string) --*

            - *(dict) --*

              - *(string) --*

                - *(dict) --*

                  Represents a summary of a  Method resource, given a particular date and time.

                  - **authorizationType** *(string) --*

                    The method's authorization type. Valid values are ``NONE`` for open access,
                    ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                    authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                  - **apiKeyRequired** *(boolean) --*

                    Specifies whether the method requires a valid  ApiKey .
    """


_ClientGetDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientGetDocumentationPartResponselocationTypeDef",
    {"type": str, "path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientGetDocumentationPartResponselocationTypeDef(
    _ClientGetDocumentationPartResponselocationTypeDef
):
    """
    Type definition for `ClientGetDocumentationPartResponse` `location`

    The location of the API entity to which the documentation applies. Valid fields depend on the
    targeted API entity type. All the valid location fields are not required. If not explicitly
    specified, a valid location field is treated as a wildcard and associated documentation
    content may be inherited by matching entities, unless overridden.

    - **type** *(string) --*

      [Required] The type of API entity to which the documentation content applies. Valid values
      are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
      ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
      ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
      entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
      ``RESOURCE`` type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
      ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
      ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
      value is ``/`` for the root resource. When an applicable child entity inherits the content
      of another entity of the same type with more general specifications of the other
      ``location`` attributes, the child entity's ``path`` attribute must match that of the
      parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any method. When an applicable child entity inherits the content of an entity of the same
      type with more general specifications of the other ``location`` attributes, the child
      entity's ``method`` attribute must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any status code. When an applicable child entity inherits the content of an entity of the
      same type with more general specifications of the other ``location`` attributes, the child
      entity's ``statusCode`` attribute must match that of the parent entity exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API entity
      types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
      any other entity type.
    """


_ClientGetDocumentationPartResponseTypeDef = TypedDict(
    "_ClientGetDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientGetDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientGetDocumentationPartResponseTypeDef(
    _ClientGetDocumentationPartResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentationPart` `Response`

    A documentation part for a targeted API entity.

    A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
    The target specifies an API entity to which the documentation content applies. The supported
    API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
    ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE``
    , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API
    entity type. All valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an API can use any
    shape for the content map, only the OpenAPI-compliant documentation fields will be injected
    into the associated API entity definition in the exported OpenAPI definition file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationParts

    - **id** *(string) --*

      The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is
      created.

    - **location** *(dict) --*

      The location of the API entity to which the documentation applies. Valid fields depend on the
      targeted API entity type. All the valid location fields are not required. If not explicitly
      specified, a valid location field is treated as a wildcard and associated documentation
      content may be inherited by matching entities, unless overridden.

      - **type** *(string) --*

        [Required] The type of API entity to which the documentation content applies. Valid values
        are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
        ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
        ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
        entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
        ``RESOURCE`` type.

      - **path** *(string) --*

        The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
        ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
        ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
        value is ``/`` for the root resource. When an applicable child entity inherits the content
        of another entity of the same type with more general specifications of the other
        ``location`` attributes, the child entity's ``path`` attribute must match that of the
        parent entity as a prefix.

      - **method** *(string) --*

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any method. When an applicable child entity inherits the content of an entity of the same
        type with more general specifications of the other ``location`` attributes, the child
        entity's ``method`` attribute must match that of the parent entity exactly.

      - **statusCode** *(string) --*

        The HTTP status code of a response. It is a valid field for the API entity types of
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any status code. When an applicable child entity inherits the content of an entity of the
        same type with more general specifications of the other ``location`` attributes, the child
        entity's ``statusCode`` attribute must match that of the parent entity exactly.

      - **name** *(string) --*

        The name of the targeted API entity. It is a valid and required field for the API entity
        types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
        any other entity type.

    - **properties** *(string) --*

      A content map of API-specific key-value pairs describing the targeted API entity. The map
      must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\" }"`` .
      Only OpenAPI-compliant documentation-related fields from the propertiesmap are exported and,
      hence, published as part of the API entity definitions, while the original documentation
      parts are exported in a OpenAPI extension of ``x-amazon-apigateway-documentation`` .
    """


_ClientGetDocumentationPartsResponseitemslocationTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseitemslocationTypeDef",
    {"type": str, "path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientGetDocumentationPartsResponseitemslocationTypeDef(
    _ClientGetDocumentationPartsResponseitemslocationTypeDef
):
    """
    Type definition for `ClientGetDocumentationPartsResponseitems` `location`

    The location of the API entity to which the documentation applies. Valid fields depend on
    the targeted API entity type. All the valid location fields are not required. If not
    explicitly specified, a valid location field is treated as a wildcard and associated
    documentation content may be inherited by matching entities, unless overridden.

    - **type** *(string) --*

      [Required] The type of API entity to which the documentation content applies. Valid
      values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
      not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
      ``REQUEST_BODY`` , or ``RESOURCE`` type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of
      ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
      ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
      applicable child entity inherits the content of another entity of the same type with
      more general specifications of the other ``location`` attributes, the child entity's
      ``path`` attribute must match that of the parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
      for any method. When an applicable child entity inherits the content of an entity of
      the same type with more general specifications of the other ``location`` attributes,
      the child entity's ``method`` attribute must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
      for any status code. When an applicable child entity inherits the content of an entity
      of the same type with more general specifications of the other ``location`` attributes,
      the child entity's ``statusCode`` attribute must match that of the parent entity
      exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API
      entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
      for any other entity type.
    """


_ClientGetDocumentationPartsResponseitemsTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseitemsTypeDef",
    {
        "id": str,
        "location": ClientGetDocumentationPartsResponseitemslocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientGetDocumentationPartsResponseitemsTypeDef(
    _ClientGetDocumentationPartsResponseitemsTypeDef
):
    """
    Type definition for `ClientGetDocumentationPartsResponse` `items`

    A documentation part for a targeted API entity.

    A documentation part consists of a content map (``properties`` ) and a target (``location``
    ). The target specifies an API entity to which the documentation content applies. The
    supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` ,
    ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
    ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid
    ``location`` fields depend on the API entity type. All valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an API can use
    any shape for the content map, only the OpenAPI-compliant documentation fields will be
    injected into the associated API entity definition in the exported OpenAPI definition file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationParts

    - **id** *(string) --*

      The  DocumentationPart identifier, generated by API Gateway when the
      ``DocumentationPart`` is created.

    - **location** *(dict) --*

      The location of the API entity to which the documentation applies. Valid fields depend on
      the targeted API entity type. All the valid location fields are not required. If not
      explicitly specified, a valid location field is treated as a wildcard and associated
      documentation content may be inherited by matching entities, unless overridden.

      - **type** *(string) --*

        [Required] The type of API entity to which the documentation content applies. Valid
        values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
        not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
        ``REQUEST_BODY`` , or ``RESOURCE`` type.

      - **path** *(string) --*

        The URL path of the target. It is a valid field for the API entity types of
        ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
        ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
        applicable child entity inherits the content of another entity of the same type with
        more general specifications of the other ``location`` attributes, the child entity's
        ``path`` attribute must match that of the parent entity as a prefix.

      - **method** *(string) --*

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
        for any method. When an applicable child entity inherits the content of an entity of
        the same type with more general specifications of the other ``location`` attributes,
        the child entity's ``method`` attribute must match that of the parent entity exactly.

      - **statusCode** *(string) --*

        The HTTP status code of a response. It is a valid field for the API entity types of
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
        for any status code. When an applicable child entity inherits the content of an entity
        of the same type with more general specifications of the other ``location`` attributes,
        the child entity's ``statusCode`` attribute must match that of the parent entity
        exactly.

      - **name** *(string) --*

        The name of the targeted API entity. It is a valid and required field for the API
        entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
        for any other entity type.

    - **properties** *(string) --*

      A content map of API-specific key-value pairs describing the targeted API entity. The map
      must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\"
      }"`` . Only OpenAPI-compliant documentation-related fields from the propertiesmap are
      exported and, hence, published as part of the API entity definitions, while the original
      documentation parts are exported in a OpenAPI extension of
      ``x-amazon-apigateway-documentation`` .
    """


_ClientGetDocumentationPartsResponseTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseTypeDef",
    {"position": str, "items": List[ClientGetDocumentationPartsResponseitemsTypeDef]},
    total=False,
)


class ClientGetDocumentationPartsResponseTypeDef(
    _ClientGetDocumentationPartsResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentationParts` `Response`

    The collection of documentation parts of an API.

       `Documenting an API
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
       ,  DocumentationPart

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A documentation part for a targeted API entity.

        A documentation part consists of a content map (``properties`` ) and a target (``location``
        ). The target specifies an API entity to which the documentation content applies. The
        supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` ,
        ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
        ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid
        ``location`` fields depend on the API entity type. All valid fields are not required.

        The content map is a JSON string of API-specific key-value pairs. Although an API can use
        any shape for the content map, only the OpenAPI-compliant documentation fields will be
        injected into the associated API entity definition in the exported OpenAPI definition file.

          `Documenting an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
          ,  DocumentationParts

        - **id** *(string) --*

          The  DocumentationPart identifier, generated by API Gateway when the
          ``DocumentationPart`` is created.

        - **location** *(dict) --*

          The location of the API entity to which the documentation applies. Valid fields depend on
          the targeted API entity type. All the valid location fields are not required. If not
          explicitly specified, a valid location field is treated as a wildcard and associated
          documentation content may be inherited by matching entities, unless overridden.

          - **type** *(string) --*

            [Required] The type of API entity to which the documentation content applies. Valid
            values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
            ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
            not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
            ``REQUEST_BODY`` , or ``RESOURCE`` type.

          - **path** *(string) --*

            The URL path of the target. It is a valid field for the API entity types of
            ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
            ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
            ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
            applicable child entity inherits the content of another entity of the same type with
            more general specifications of the other ``location`` attributes, the child entity's
            ``path`` attribute must match that of the parent entity as a prefix.

          - **method** *(string) --*

            The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
            ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
            for any method. When an applicable child entity inherits the content of an entity of
            the same type with more general specifications of the other ``location`` attributes,
            the child entity's ``method`` attribute must match that of the parent entity exactly.

          - **statusCode** *(string) --*

            The HTTP status code of a response. It is a valid field for the API entity types of
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
            for any status code. When an applicable child entity inherits the content of an entity
            of the same type with more general specifications of the other ``location`` attributes,
            the child entity's ``statusCode`` attribute must match that of the parent entity
            exactly.

          - **name** *(string) --*

            The name of the targeted API entity. It is a valid and required field for the API
            entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
            ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
            for any other entity type.

        - **properties** *(string) --*

          A content map of API-specific key-value pairs describing the targeted API entity. The map
          must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\"
          }"`` . Only OpenAPI-compliant documentation-related fields from the propertiesmap are
          exported and, hence, published as part of the API entity definitions, while the original
          documentation parts are exported in a OpenAPI extension of
          ``x-amazon-apigateway-documentation`` .
    """


_ClientGetDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientGetDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientGetDocumentationVersionResponseTypeDef(
    _ClientGetDocumentationVersionResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentationVersion` `Response`

    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version associated with an API
    stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersions

    - **version** *(string) --*

      The version identifier of the API documentation snapshot.

    - **createdDate** *(datetime) --*

      The date when the API documentation snapshot is created.

    - **description** *(string) --*

      The description of the API documentation snapshot.
    """


_ClientGetDocumentationVersionsResponseitemsTypeDef = TypedDict(
    "_ClientGetDocumentationVersionsResponseitemsTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientGetDocumentationVersionsResponseitemsTypeDef(
    _ClientGetDocumentationVersionsResponseitemsTypeDef
):
    """
    Type definition for `ClientGetDocumentationVersionsResponse` `items`

    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version associated with an
    API stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersions

    - **version** *(string) --*

      The version identifier of the API documentation snapshot.

    - **createdDate** *(datetime) --*

      The date when the API documentation snapshot is created.

    - **description** *(string) --*

      The description of the API documentation snapshot.
    """


_ClientGetDocumentationVersionsResponseTypeDef = TypedDict(
    "_ClientGetDocumentationVersionsResponseTypeDef",
    {
        "position": str,
        "items": List[ClientGetDocumentationVersionsResponseitemsTypeDef],
    },
    total=False,
)


class ClientGetDocumentationVersionsResponseTypeDef(
    _ClientGetDocumentationVersionsResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentationVersions` `Response`

    The collection of documentation snapshots of an API.

    Use the  DocumentationVersions to manage documentation snapshots associated with various API
    stages.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersion

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A snapshot of the documentation of an API.

        Publishing API documentation involves creating a documentation version associated with an
        API stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

          `Documenting an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
          ,  DocumentationPart ,  DocumentationVersions

        - **version** *(string) --*

          The version identifier of the API documentation snapshot.

        - **createdDate** *(datetime) --*

          The date when the API documentation snapshot is created.

        - **description** *(string) --*

          The description of the API documentation snapshot.
    """


_ClientGetDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientGetDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetDomainNameResponseendpointConfigurationTypeDef(
    _ClientGetDomainNameResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientGetDomainNameResponse` `endpointConfiguration`

    The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientGetDomainNameResponseTypeDef = TypedDict(
    "_ClientGetDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientGetDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": str,
        "domainNameStatusMessage": str,
        "securityPolicy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainNameResponseTypeDef(_ClientGetDomainNameResponseTypeDef):
    """
    Type definition for `ClientGetDomainName` `Response`

    Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

    When you deploy an API, API Gateway creates a default host name for the API. This default API
    host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
    default host name, you can access the API's root resource with the URL of
    ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom
    domain name of ``apis.example.com`` for this API, you can then access the same resource using
    the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping (
    BasePathMapping ) of your API under the custom domain name.

       `Set a Custom Host Name for an API
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **domainName** *(string) --*

      The custom domain name as an API host name, for example, ``my-api.example.com`` .

    - **certificateName** *(string) --*

      The name of the certificate that will be used by edge-optimized endpoint for this domain name.

    - **certificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for
      this domain name. AWS Certificate Manager is the only supported source.

    - **certificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this domain
      name was uploaded.

    - **regionalDomainName** *(string) --*

      The domain name associated with the regional endpoint for this custom domain name. You set up
      this association by adding a DNS record that points the custom domain name to this regional
      domain name. The regional domain name is returned by API Gateway when you create a regional
      endpoint.

    - **regionalHostedZoneId** *(string) --*

      The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more
      information, see `Set up a Regional Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **regionalCertificateName** *(string) --*

      The name of the certificate that will be used for validating the regional domain name.

    - **regionalCertificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used for validating the regional
      domain name. AWS Certificate Manager is the only supported source.

    - **distributionDomainName** *(string) --*

      The domain name of the Amazon CloudFront distribution associated with this custom domain name
      for an edge-optimized endpoint. You set up this association when adding a DNS record pointing
      the custom domain name to this distribution name. For more information about CloudFront
      distributions, see the `Amazon CloudFront documentation
      <https://aws.amazon.com/documentation/cloudfront/>`__ .

    - **distributionHostedZoneId** *(string) --*

      The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid
      value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional
      Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **domainNameStatus** *(string) --*

      The status of the  DomainName migration. The valid values are ``AVAILABLE`` and ``UPDATING``
      . If the status is ``UPDATING`` , the domain cannot be modified further until the existing
      operation is complete. If it is ``AVAILABLE`` , the domain can be updated.

    - **domainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the  DomainName
      migration.

    - **securityPolicy** *(string) --*

      The Transport Layer Security (TLS) version + cipher suite for this  DomainName . The valid
      values are ``TLS_1_0`` and ``TLS_1_2`` .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetExportResponseTypeDef = TypedDict(
    "_ClientGetExportResponseTypeDef",
    {"contentType": str, "contentDisposition": str},
    total=False,
)


class ClientGetExportResponseTypeDef(_ClientGetExportResponseTypeDef):
    """
    Type definition for `ClientGetExport` `Response`

    The binary blob response to  GetExport , which contains the generated SDK.

    - **contentType** *(string) --*

      The content-type header value in the HTTP response. This will correspond to a valid 'accept'
      type in the request.

    - **contentDisposition** *(string) --*

      The content-disposition header value in the HTTP response.

    - **body** (:class:`.StreamingBody`) --

      The binary blob response to  GetExport , which contains the export.
    """


_ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientGetIntegrationResponseResponseTypeDef(
    _ClientGetIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientGetIntegrationResponse` `Response`

    Represents an integration response. The status code must map to an existing  MethodResponse ,
    and parameters and templates can be used to transform the back-end response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response based
      on the response from the back end. For example, if the success response returns nothing and
      the error response returns some string, you could use the ``.+`` regex to match error
      response. However, make sure that the error response does not contain any newline (``\\n`` )
      character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function
      error header is matched. For all other HTTP and AWS back ends, the HTTP status code is
      matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the back end. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The
      mapped non-static value must match the pattern of ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the ``$``
      prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response templates
      are represented as a key/value map, with a content-type as the key and a template as the
      value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientGetIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientGetIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientGetIntegrationResponseintegrationResponsesTypeDef(
    _ClientGetIntegrationResponseintegrationResponsesTypeDef
):
    """
    Type definition for `ClientGetIntegrationResponse` `integrationResponses`

    Represents an integration response. The status code must map to an existing
    MethodResponse , and parameters and templates can be used to transform the back-end
    response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response
      based on the response from the back end. For example, if the success response returns
      nothing and the error response returns some string, you could use the ``.+`` regex to
      match error response. However, make sure that the error response does not contain any
      newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
      the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
      the HTTP status code is matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response
      from the back end. The key is a method response header parameter name and the mapped
      value is an integration response header value, a static value enclosed within a pair of
      single quotes, or a JSON expression from the integration response body. The mapping key
      must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
      and unique header name. The mapped non-static value must match the pattern of
      ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the
      ``$`` prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response
      templates are represented as a key/value map, with a content-type as the key and a
      template as the value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
      the corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
      Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientGetIntegrationResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseTypeDef",
    {
        "type": str,
        "httpMethod": str,
        "uri": str,
        "connectionType": str,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": str,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientGetIntegrationResponseintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientGetIntegrationResponseTypeDef(_ClientGetIntegrationResponseTypeDef):
    """
    Type definition for `ClientGetIntegration` `Response`

    Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

     In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating
     an API <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **type** *(string) --*

      Specifies an API method integration type. The valid value is one of the following:

      * ``AWS`` : for integrating the API method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      the Lambda proxy integration.

      * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom
      integration.

      * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC, with the client request passed through as-is. This is
      also referred to as the HTTP proxy integration.

      * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back"
      endpoint without invoking any backend.

      For the HTTP and HTTP proxy integrations, each integration can specify a protocol
      (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom
      ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK``
      is referred to as a private integration and uses a  VpcLink to connect API Gateway to a
      network load balancer of a VPC.

    - **httpMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **uri** *(string) --*

      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded
      HTTP(S) URL according to the `RFC-3986 specification
      <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard
      integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where
      ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for
      routing.

      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form
      ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here,
      ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of
      the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain
      supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS
      service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The
      ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input
      parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The
      ensuing ``service_api`` refers to the path to an AWS service resource, including the region
      of the integrated AWS service, if applicable. For example, for integration with the S3 API of
      ```GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the
      ``uri`` can be either
      ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or
      ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``

    - **connectionType** *(string) --*

      The type of the network connection to the integration endpoint. The valid value is
      ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private
      connections between API Gateway and a network load balancer in a VPC. The default value is
      ``INTERNET`` .

    - **connectionId** *(string) --*

      The (```id`` <https://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__
      ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined,
      otherwise.

    - **credentials** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string ``arn:aws:iam::\\*:user/\\*`` . To use resource-based permissions
      on supported AWS services, specify null.

    - **requestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      back end. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the back end. The method request parameter value must match the
      pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` ,
      ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter
      name.

      - *(string) --*

        - *(string) --*

    - **requestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

    - **passthroughBehavior** *(string) --*

      Specifies how the method request body of an unmapped content type will be passed through the
      integration request to the back end without transformation. A content type is unmapped if no
      mapping template is defined in the integration or the content type does not match any of the
      mapped content types, as specified in ``requestTemplates`` . The valid value is one of the
      following:

      * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the
      back end without transformation when the method request content type does not match any
      content type associated with the mapping templates defined in the integration request.

      * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to
      the back end without transformation when no mapping template is defined in the integration
      request. If a template is defined when this option is selected, the method request of an
      unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response.

      * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response
      when either the method request content type does not match any content type associated with
      the mapping templates defined in the integration request or no mapping template is defined in
      the integration request.

    - **contentHandling** *(string) --*

      Specifies how to handle request payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the request payload will be passed through from the method
      request to integration request without modification, provided that the
      ``passthroughBehavior`` is configured to support payload pass-through.

    - **timeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.

    - **cacheNamespace** *(string) --*

      An API-specific tag group of related cached parameters. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

    - **cacheKeyParameters** *(list) --*

      A list of request parameters whose values API Gateway caches. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

      - *(string) --*

    - **integrationResponses** *(dict) --*

      Specifies the integration's responses.

       Example: Get integration responses of a method Request

       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200
       HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
       20160607T191449Z Authorization: AWS4-HMAC-SHA256
       Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request,
       SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

      The successful response returns ``200 OK`` status and a payload as follows:

       ``{ "_links": { "curies": { "href":
       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
       "name": "integrationresponse", "templated": true }, "self": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title":
       "200" }, "integrationresponse:delete": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" },
       "integrationresponse:update": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } },
       "responseParameters": { "method.response.header.Content-Type": "'application/xml'" },
       "responseTemplates": { "application/json":
       "$util.urlDecode(\\"%3CkinesisStreams%3E#foreach($stream in
       $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\\")\\n"
       }, "statusCode": "200" }``

         `Creating an API
         <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

      - *(string) --*

        - *(dict) --*

          Represents an integration response. The status code must map to an existing
          MethodResponse , and parameters and templates can be used to transform the back-end
          response.

            `Creating an API
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

          - **statusCode** *(string) --*

            Specifies the status code that is used to map the integration response to an existing
            MethodResponse .

          - **selectionPattern** *(string) --*

            Specifies the regular expression (regex) pattern used to choose an integration response
            based on the response from the back end. For example, if the success response returns
            nothing and the error response returns some string, you could use the ``.+`` regex to
            match error response. However, make sure that the error response does not contain any
            newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
            the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
            the HTTP status code is matched.

          - **responseParameters** *(dict) --*

            A key-value map specifying response parameters that are passed to the method response
            from the back end. The key is a method response header parameter name and the mapped
            value is an integration response header value, a static value enclosed within a pair of
            single quotes, or a JSON expression from the integration response body. The mapping key
            must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
            and unique header name. The mapped non-static value must match the pattern of
            ``integration.response.header.{name}`` or
            ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
            response header name and ``JSON-expression`` is a valid JSON expression without the
            ``$`` prefix.

            - *(string) --*

              - *(string) --*

          - **responseTemplates** *(dict) --*

            Specifies the templates used to transform the integration response body. Response
            templates are represented as a key/value map, with a content-type as the key and a
            template as the value.

            - *(string) --*

              - *(string) --*

          - **contentHandling** *(string) --*

            Specifies how to handle response payload content type conversions. Supported values are
            ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

            * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
            the corresponding binary blob.

            * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
            Base64-encoded string.

            If this property is not defined, the response payload will be passed through from the
            integration response to the method response without modification.
    """


_ClientGetMethodResponseResponseTypeDef = TypedDict(
    "_ClientGetMethodResponseResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)


class ClientGetMethodResponseResponseTypeDef(_ClientGetMethodResponseResponseTypeDef):
    """
    Type definition for `ClientGetMethodResponse` `Response`

    Represents a method response of a given HTTP status code returned to the client. The method
    response is passed from the back end through the associated integration response that can be
    transformed using a mapping template.

     Example: A **MethodResponse** instance of an API Request

    The example request retrieves a **MethodResponse** of the 200 status code.

     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1
     Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
     20160603T222952Z Authorization: AWS4-HMAC-SHA256
     Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request,
     SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

    The successful response returns ``200 OK`` status and a payload as follows:

     ``{ "_links": { "curies": { "href":
     "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
     "name": "methodresponse", "templated": true }, "self": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" },
     "methodresponse:delete": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" },
     "methodresponse:update": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": {
     "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type":
     false }, "statusCode": "200" }``

        Method ,  IntegrationResponse ,  Integration  `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      The method response's status code.

    - **responseParameters** *(dict) --*

      A key-value map specifying required or optional response parameters that API Gateway can send
      back to the caller. A key defines a method response header and the value specifies whether
      the associated method response header is required or not. The expression of the key must
      match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique
      header name. API Gateway passes certain integration response data to the method response
      headers specified here according to the mapping you prescribe in the API's
      IntegrationResponse . The integration response data that can be mapped include an integration
      response header expressed in ``integration.response.header.{name}`` , a static value enclosed
      within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the
      back-end response payload in the form of ``integration.response.body.{JSON-expression}`` ,
      where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

      - *(string) --*

        - *(boolean) --*

    - **responseModels** *(dict) --*

      Specifies the  Model resources used for the response's content-type. Response models are
      represented as a key/value map, with a content-type as the key and a  Model name as the value.

      - *(string) --*

        - *(string) --*
    """


_ClientGetModelResponseTypeDef = TypedDict(
    "_ClientGetModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientGetModelResponseTypeDef(_ClientGetModelResponseTypeDef):
    """
    Type definition for `ClientGetModel` `Response`

    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request payload. A response
    model defines the data structure of the response payload returned by the back end. Although not
    required, models are useful for mapping payloads between the front end and back end.

    A model is used for generating an API's SDK, validating the input request body, and creating a
    skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **id** *(string) --*

      The identifier for the model resource.

    - **name** *(string) --*

      The name of the model. Must be an alphanumeric string.

    - **description** *(string) --*

      The description of the model.

    - **schema** *(string) --*

      The schema for the model. For ``application/json`` models, this should be `JSON schema draft
      4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include "\\*/"
      characters in the description of any properties because such "\\*/" characters may be
      interpreted as the closing marker for comments in some languages, such as Java or JavaScript,
      causing the installation of your API's SDK generated by API Gateway to fail.

    - **contentType** *(string) --*

      The content-type for the model.
    """


_ClientGetModelsResponseitemsTypeDef = TypedDict(
    "_ClientGetModelsResponseitemsTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientGetModelsResponseitemsTypeDef(_ClientGetModelsResponseitemsTypeDef):
    """
    Type definition for `ClientGetModelsResponse` `items`

    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request payload. A
    response model defines the data structure of the response payload returned by the back end.
    Although not required, models are useful for mapping payloads between the front end and
    back end.

    A model is used for generating an API's SDK, validating the input request body, and
    creating a skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **id** *(string) --*

      The identifier for the model resource.

    - **name** *(string) --*

      The name of the model. Must be an alphanumeric string.

    - **description** *(string) --*

      The description of the model.

    - **schema** *(string) --*

      The schema for the model. For ``application/json`` models, this should be `JSON schema
      draft 4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include
      "\\*/" characters in the description of any properties because such "\\*/" characters may
      be interpreted as the closing marker for comments in some languages, such as Java or
      JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

    - **contentType** *(string) --*

      The content-type for the model.
    """


_ClientGetModelsResponseTypeDef = TypedDict(
    "_ClientGetModelsResponseTypeDef",
    {"position": str, "items": List[ClientGetModelsResponseitemsTypeDef]},
    total=False,
)


class ClientGetModelsResponseTypeDef(_ClientGetModelsResponseTypeDef):
    """
    Type definition for `ClientGetModels` `Response`

    Represents a collection of  Model resources.

       Method ,  MethodResponse , `Models and Mappings
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        Represents the data structure of a method's request or response payload.

        A request model defines the data structure of the client-supplied request payload. A
        response model defines the data structure of the response payload returned by the back end.
        Although not required, models are useful for mapping payloads between the front end and
        back end.

        A model is used for generating an API's SDK, validating the input request body, and
        creating a skeletal mapping template.

            Method ,  MethodResponse , `Models and Mappings
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

        - **id** *(string) --*

          The identifier for the model resource.

        - **name** *(string) --*

          The name of the model. Must be an alphanumeric string.

        - **description** *(string) --*

          The description of the model.

        - **schema** *(string) --*

          The schema for the model. For ``application/json`` models, this should be `JSON schema
          draft 4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include
          "\\*/" characters in the description of any properties because such "\\*/" characters may
          be interpreted as the closing marker for comments in some languages, such as Java or
          JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

        - **contentType** *(string) --*

          The content-type for the model.
    """


_ClientGetRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientGetRestApiResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetRestApiResponseendpointConfigurationTypeDef(
    _ClientGetRestApiResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientGetRestApiResponse` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientGetRestApiResponseTypeDef = TypedDict(
    "_ClientGetRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientGetRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetRestApiResponseTypeDef(_ClientGetRestApiResponseTypeDef):
    """
    Type definition for `ClientGetRestApi` `Response`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports
      only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When
      compression is enabled, compression or decompression is not applied on the payload if the
      payload size is smaller than this value. Setting it to zero allows compression for any
      payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetRestApisResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetRestApisResponseitemsendpointConfigurationTypeDef(
    _ClientGetRestApisResponseitemsendpointConfigurationTypeDef
):
    """
    Type definition for `ClientGetRestApisResponseitems` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
      ). For an edge-optimized API and its custom domain name, the endpoint type is
      ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
      ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
      It is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientGetRestApisResponseitemsTypeDef = TypedDict(
    "_ClientGetRestApisResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientGetRestApisResponseitemsendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetRestApisResponseitemsTypeDef(_ClientGetRestApisResponseitemsTypeDef):
    """
    Type definition for `ClientGetRestApisResponse` `items`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi
      supports only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API.
      When compression is enabled, compression or decompression is not applied on the payload
      if the payload size is smaller than this value. Setting it to zero allows compression for
      any payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values
      are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom
      authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
        ). For an edge-optimized API and its custom domain name, the endpoint type is
        ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
        ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
        It is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetRestApisResponseTypeDef = TypedDict(
    "_ClientGetRestApisResponseTypeDef",
    {"position": str, "items": List[ClientGetRestApisResponseitemsTypeDef]},
    total=False,
)


class ClientGetRestApisResponseTypeDef(_ClientGetRestApisResponseTypeDef):
    """
    Type definition for `ClientGetRestApis` `Response`

    Contains references to your APIs and links that guide you in how to interact with your
    collection. A collection offers a paginated view of your APIs.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        Represents a REST API.

          `Create an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

        - **id** *(string) --*

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

        - **name** *(string) --*

          The API's name.

        - **description** *(string) --*

          The API's description.

        - **createdDate** *(datetime) --*

          The timestamp when the API was created.

        - **version** *(string) --*

          A version identifier for the API.

        - **warnings** *(list) --*

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          - *(string) --*

        - **binaryMediaTypes** *(list) --*

          The list of binary media types supported by the  RestApi . By default, the  RestApi
          supports only UTF-8-encoded text payloads.

          - *(string) --*

        - **minimumCompressionSize** *(integer) --*

          A nullable integer that is used to enable compression (with non-negative between 0 and
          10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API.
          When compression is enabled, compression or decompression is not applied on the payload
          if the payload size is smaller than this value. Setting it to zero allows compression for
          any payload size.

        - **apiKeySource** *(string) --*

          The source of the API key for metering requests according to a usage plan. Valid values
          are:

          * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

          * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom
          authorizer.

        - **endpointConfiguration** *(dict) --*

          The endpoint configuration of this  RestApi showing the endpoint types of the API.

          - **types** *(list) --*

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
            ). For an edge-optimized API and its custom domain name, the endpoint type is
            ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
            ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

            - *(string) --*

              The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
              suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
              suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

          - **vpcEndpointIds** *(list) --*

            A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
            It is only supported for ``PRIVATE`` endpoint type.

            - *(string) --*

        - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
        regardless of the caller and  Method configuration.

        - **tags** *(dict) --*

          The collection of tags. Each tag element is associated with a given resource.

          - *(string) --*

            - *(string) --*
    """


_ClientGetSdkResponseTypeDef = TypedDict(
    "_ClientGetSdkResponseTypeDef",
    {"contentType": str, "contentDisposition": str},
    total=False,
)


class ClientGetSdkResponseTypeDef(_ClientGetSdkResponseTypeDef):
    """
    Type definition for `ClientGetSdk` `Response`

    The binary blob response to  GetSdk , which contains the generated SDK.

    - **contentType** *(string) --*

      The content-type header value in the HTTP response.

    - **contentDisposition** *(string) --*

      The content-disposition header value in the HTTP response.

    - **body** (:class:`.StreamingBody`) --

      The binary blob response to  GetSdk , which contains the generated SDK.
    """


_ClientGetSdkTypeResponseconfigurationPropertiesTypeDef = TypedDict(
    "_ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    {
        "name": str,
        "friendlyName": str,
        "description": str,
        "required": bool,
        "defaultValue": str,
    },
    total=False,
)


class ClientGetSdkTypeResponseconfigurationPropertiesTypeDef(
    _ClientGetSdkTypeResponseconfigurationPropertiesTypeDef
):
    """
    Type definition for `ClientGetSdkTypeResponse` `configurationProperties`

    A configuration property of an SDK type.

    - **name** *(string) --*

      The name of a an  SdkType configuration property.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType configuration property.

    - **description** *(string) --*

      The description of an  SdkType configuration property.

    - **required** *(boolean) --*

      A boolean flag of an  SdkType configuration property to indicate if the associated SDK
      configuration property is required (``true`` ) or not (``false`` ).

    - **defaultValue** *(string) --*

      The default value of an  SdkType configuration property.
    """


_ClientGetSdkTypeResponseTypeDef = TypedDict(
    "_ClientGetSdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            ClientGetSdkTypeResponseconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)


class ClientGetSdkTypeResponseTypeDef(_ClientGetSdkTypeResponseTypeDef):
    """
    Type definition for `ClientGetSdkType` `Response`

    A type of SDK that API Gateway can generate.

    - **id** *(string) --*

      The identifier of an  SdkType instance.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType instance.

    - **description** *(string) --*

      The description of an  SdkType .

    - **configurationProperties** *(list) --*

      A list of configuration properties of an  SdkType .

      - *(dict) --*

        A configuration property of an SDK type.

        - **name** *(string) --*

          The name of a an  SdkType configuration property.

        - **friendlyName** *(string) --*

          The user-friendly name of an  SdkType configuration property.

        - **description** *(string) --*

          The description of an  SdkType configuration property.

        - **required** *(boolean) --*

          A boolean flag of an  SdkType configuration property to indicate if the associated SDK
          configuration property is required (``true`` ) or not (``false`` ).

        - **defaultValue** *(string) --*

          The default value of an  SdkType configuration property.
    """


_ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    {
        "name": str,
        "friendlyName": str,
        "description": str,
        "required": bool,
        "defaultValue": str,
    },
    total=False,
)


class ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef(
    _ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef
):
    """
    Type definition for `ClientGetSdkTypesResponseitems` `configurationProperties`

    A configuration property of an SDK type.

    - **name** *(string) --*

      The name of a an  SdkType configuration property.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType configuration property.

    - **description** *(string) --*

      The description of an  SdkType configuration property.

    - **required** *(boolean) --*

      A boolean flag of an  SdkType configuration property to indicate if the associated
      SDK configuration property is required (``true`` ) or not (``false`` ).

    - **defaultValue** *(string) --*

      The default value of an  SdkType configuration property.
    """


_ClientGetSdkTypesResponseitemsTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseitemsTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)


class ClientGetSdkTypesResponseitemsTypeDef(_ClientGetSdkTypesResponseitemsTypeDef):
    """
    Type definition for `ClientGetSdkTypesResponse` `items`

    A type of SDK that API Gateway can generate.

    - **id** *(string) --*

      The identifier of an  SdkType instance.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType instance.

    - **description** *(string) --*

      The description of an  SdkType .

    - **configurationProperties** *(list) --*

      A list of configuration properties of an  SdkType .

      - *(dict) --*

        A configuration property of an SDK type.

        - **name** *(string) --*

          The name of a an  SdkType configuration property.

        - **friendlyName** *(string) --*

          The user-friendly name of an  SdkType configuration property.

        - **description** *(string) --*

          The description of an  SdkType configuration property.

        - **required** *(boolean) --*

          A boolean flag of an  SdkType configuration property to indicate if the associated
          SDK configuration property is required (``true`` ) or not (``false`` ).

        - **defaultValue** *(string) --*

          The default value of an  SdkType configuration property.
    """


_ClientGetSdkTypesResponseTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseTypeDef",
    {"position": str, "items": List[ClientGetSdkTypesResponseitemsTypeDef]},
    total=False,
)


class ClientGetSdkTypesResponseTypeDef(_ClientGetSdkTypesResponseTypeDef):
    """
    Type definition for `ClientGetSdkTypes` `Response`

    The collection of  SdkType instances.

    - **position** *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A type of SDK that API Gateway can generate.

        - **id** *(string) --*

          The identifier of an  SdkType instance.

        - **friendlyName** *(string) --*

          The user-friendly name of an  SdkType instance.

        - **description** *(string) --*

          The description of an  SdkType .

        - **configurationProperties** *(list) --*

          A list of configuration properties of an  SdkType .

          - *(dict) --*

            A configuration property of an SDK type.

            - **name** *(string) --*

              The name of a an  SdkType configuration property.

            - **friendlyName** *(string) --*

              The user-friendly name of an  SdkType configuration property.

            - **description** *(string) --*

              The description of an  SdkType configuration property.

            - **required** *(boolean) --*

              A boolean flag of an  SdkType configuration property to indicate if the associated
              SDK configuration property is required (``true`` ) or not (``false`` ).

            - **defaultValue** *(string) --*

              The default value of an  SdkType configuration property.
    """


_ClientGetStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientGetStageResponseaccessLogSettingsTypeDef(
    _ClientGetStageResponseaccessLogSettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `accessLogSettings`

    Settings for logging access in this stage.

    - **format** *(string) --*

      A single line format of the access logs of data, as specified by selected `$context
      variables
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
      . The format must include at least ``$context.requestId`` .

    - **destinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientGetStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientGetStageResponsecanarySettingsTypeDef(
    _ClientGetStageResponsecanarySettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `canarySettings`

    Settings for the canary deployment in this stage.

    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.

    - **deploymentId** *(string) --*

      The ID of the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      Stage variables overridden for a canary release deployment, including new stage variables
      introduced in the canary. These stage variables are represented as a string-to-string map
      between stage variable names and their values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
    """


_ClientGetStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientGetStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": str,
    },
    total=False,
)


class ClientGetStageResponsemethodSettingsTypeDef(
    _ClientGetStageResponsemethodSettingsTypeDef
):
    """
    Type definition for `ClientGetStageResponse` `methodSettings`

    Specifies the method setting properties.

    - **metricsEnabled** *(boolean) --*

      Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
      for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
      Boolean.

    - **loggingLevel** *(string) --*

      Specifies the logging level for this method, which affects the log entries pushed to
      Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
      ``ERROR`` , and ``INFO`` .

    - **dataTraceEnabled** *(boolean) --*

      Specifies whether data trace logging is enabled for this method, which affects the log
      entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

    - **throttlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

    - **throttlingRateLimit** *(float) --*

      Specifies the throttling rate limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

    - **cachingEnabled** *(boolean) --*

      Specifies whether responses should be cached and returned for requests. A cache cluster
      must be enabled on the stage for responses to be cached. The PATCH path for this
      setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

    - **cacheTtlInSeconds** *(integer) --*

      Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
      the longer the response will be cached. The PATCH path for this setting is
      ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

    - **cacheDataEncrypted** *(boolean) --*

      Specifies whether the cached responses are encrypted. The PATCH path for this setting
      is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

    - **requireAuthorizationForCacheControl** *(boolean) --*

      Specifies whether authorization is required for a cache invalidation request. The PATCH
      path for this setting is
      ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
      is a Boolean.

    - **unauthorizedCacheControlHeaderStrategy** *(string) --*

      Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
      for this setting is
      ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
      available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
      ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .
    """


_ClientGetStageResponseTypeDef = TypedDict(
    "_ClientGetStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": str,
        "cacheClusterStatus": str,
        "methodSettings": Dict[str, ClientGetStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientGetStageResponseTypeDef(_ClientGetStageResponseTypeDef):
    """
    Type definition for `ClientGetStage` `Response`

    Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

      `Deploy an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__

    - **deploymentId** *(string) --*

      The identifier of the  Deployment that the stage points to.

    - **clientCertificateId** *(string) --*

      The identifier of a client certificate for an API stage.

    - **stageName** *(string) --*

      The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a
      call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and
      underscores. Maximum length is 128 characters.

    - **description** *(string) --*

      The stage's description.

    - **cacheClusterEnabled** *(boolean) --*

      Specifies whether a cache cluster is enabled for the stage.

    - **cacheClusterSize** *(string) --*

      The size of the cache cluster for the stage, if enabled.

    - **cacheClusterStatus** *(string) --*

      The status of the cache cluster for the stage, if enabled.

    - **methodSettings** *(dict) --*

      A map that defines the method settings for a  Stage resource. Keys (designated as
      ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}``
      for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.

      - *(string) --*

        - *(dict) --*

          Specifies the method setting properties.

          - **metricsEnabled** *(boolean) --*

            Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
            for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
            Boolean.

          - **loggingLevel** *(string) --*

            Specifies the logging level for this method, which affects the log entries pushed to
            Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
            ``ERROR`` , and ``INFO`` .

          - **dataTraceEnabled** *(boolean) --*

            Specifies whether data trace logging is enabled for this method, which affects the log
            entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

          - **throttlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

          - **throttlingRateLimit** *(float) --*

            Specifies the throttling rate limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

          - **cachingEnabled** *(boolean) --*

            Specifies whether responses should be cached and returned for requests. A cache cluster
            must be enabled on the stage for responses to be cached. The PATCH path for this
            setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

          - **cacheTtlInSeconds** *(integer) --*

            Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
            the longer the response will be cached. The PATCH path for this setting is
            ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

          - **cacheDataEncrypted** *(boolean) --*

            Specifies whether the cached responses are encrypted. The PATCH path for this setting
            is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

          - **requireAuthorizationForCacheControl** *(boolean) --*

            Specifies whether authorization is required for a cache invalidation request. The PATCH
            path for this setting is
            ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
            is a Boolean.

          - **unauthorizedCacheControlHeaderStrategy** *(string) --*

            Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
            for this setting is
            ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
            available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
            ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

    - **variables** *(dict) --*

      A map that defines the stage variables for a  Stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+``
      .

      - *(string) --*

        - *(string) --*

    - **documentationVersion** *(string) --*

      The version of the associated API documentation.

    - **accessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **format** *(string) --*

        A single line format of the access logs of data, as specified by selected `$context
        variables
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
        . The format must include at least ``$context.requestId`` .

      - **destinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

    - **canarySettings** *(dict) --*

      Settings for the canary deployment in this stage.

      - **percentTraffic** *(float) --*

        The percent (0-100) of traffic diverted to a canary deployment.

      - **deploymentId** *(string) --*

        The ID of the canary deployment.

      - **stageVariableOverrides** *(dict) --*

        Stage variables overridden for a canary release deployment, including new stage variables
        introduced in the canary. These stage variables are represented as a string-to-string map
        between stage variable names and their values.

        - *(string) --*

          - *(string) --*

      - **useStageCache** *(boolean) --*

        A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

    - **tracingEnabled** *(boolean) --*

      Specifies whether active tracing with X-ray is enabled for the  Stage .

    - **webAclArn** *(string) --*

      The ARN of the WebAcl associated with the  Stage .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*

    - **createdDate** *(datetime) --*

      The timestamp when the stage was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the stage last updated.
    """


_ClientGetStagesResponseitemaccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientGetStagesResponseitemaccessLogSettingsTypeDef(
    _ClientGetStagesResponseitemaccessLogSettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseitem` `accessLogSettings`

    Settings for logging access in this stage.

    - **format** *(string) --*

      A single line format of the access logs of data, as specified by selected `$context
      variables
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
      . The format must include at least ``$context.requestId`` .

    - **destinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStagesResponseitemcanarySettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemcanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientGetStagesResponseitemcanarySettingsTypeDef(
    _ClientGetStagesResponseitemcanarySettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseitem` `canarySettings`

    Settings for the canary deployment in this stage.

    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.

    - **deploymentId** *(string) --*

      The ID of the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      Stage variables overridden for a canary release deployment, including new stage
      variables introduced in the canary. These stage variables are represented as a
      string-to-string map between stage variable names and their values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
    """


_ClientGetStagesResponseitemmethodSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemmethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": str,
    },
    total=False,
)


class ClientGetStagesResponseitemmethodSettingsTypeDef(
    _ClientGetStagesResponseitemmethodSettingsTypeDef
):
    """
    Type definition for `ClientGetStagesResponseitem` `methodSettings`

    Specifies the method setting properties.

    - **metricsEnabled** *(boolean) --*

      Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH
      path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value
      is a Boolean.

    - **loggingLevel** *(string) --*

      Specifies the logging level for this method, which affects the log entries pushed
      to Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
      ``ERROR`` , and ``INFO`` .

    - **dataTraceEnabled** *(boolean) --*

      Specifies whether data trace logging is enabled for this method, which affects the
      log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

    - **throttlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

    - **throttlingRateLimit** *(float) --*

      Specifies the throttling rate limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

    - **cachingEnabled** *(boolean) --*

      Specifies whether responses should be cached and returned for requests. A cache
      cluster must be enabled on the stage for responses to be cached. The PATCH path for
      this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a
      Boolean.

    - **cacheTtlInSeconds** *(integer) --*

      Specifies the time to live (TTL), in seconds, for cached responses. The higher the
      TTL, the longer the response will be cached. The PATCH path for this setting is
      ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

    - **cacheDataEncrypted** *(boolean) --*

      Specifies whether the cached responses are encrypted. The PATCH path for this
      setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a
      Boolean.

    - **requireAuthorizationForCacheControl** *(boolean) --*

      Specifies whether authorization is required for a cache invalidation request. The
      PATCH path for this setting is
      ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the
      value is a Boolean.

    - **unauthorizedCacheControlHeaderStrategy** *(string) --*

      Specifies how to handle unauthorized requests for cache invalidation. The PATCH
      path for this setting is
      ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
      available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
      ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .
    """


_ClientGetStagesResponseitemTypeDef = TypedDict(
    "_ClientGetStagesResponseitemTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": str,
        "cacheClusterStatus": str,
        "methodSettings": Dict[str, ClientGetStagesResponseitemmethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStagesResponseitemaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStagesResponseitemcanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientGetStagesResponseitemTypeDef(_ClientGetStagesResponseitemTypeDef):
    """
    Type definition for `ClientGetStagesResponse` `item`

    Represents a unique identifier for a version of a deployed  RestApi that is callable by
    users.

      `Deploy an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__

    - **deploymentId** *(string) --*

      The identifier of the  Deployment that the stage points to.

    - **clientCertificateId** *(string) --*

      The identifier of a client certificate for an API stage.

    - **stageName** *(string) --*

      The name of the stage is the first path segment in the Uniform Resource Identifier (URI)
      of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens,
      and underscores. Maximum length is 128 characters.

    - **description** *(string) --*

      The stage's description.

    - **cacheClusterEnabled** *(boolean) --*

      Specifies whether a cache cluster is enabled for the stage.

    - **cacheClusterSize** *(string) --*

      The size of the cache cluster for the stage, if enabled.

    - **cacheClusterStatus** *(string) --*

      The status of the cache cluster for the stage, if enabled.

    - **methodSettings** *(dict) --*

      A map that defines the method settings for a  Stage resource. Keys (designated as
      ``/{method_setting_key`` below) are method paths defined as
      ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for
      overriding all methods in the stage.

      - *(string) --*

        - *(dict) --*

          Specifies the method setting properties.

          - **metricsEnabled** *(boolean) --*

            Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH
            path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value
            is a Boolean.

          - **loggingLevel** *(string) --*

            Specifies the logging level for this method, which affects the log entries pushed
            to Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
            ``ERROR`` , and ``INFO`` .

          - **dataTraceEnabled** *(boolean) --*

            Specifies whether data trace logging is enabled for this method, which affects the
            log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

          - **throttlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

          - **throttlingRateLimit** *(float) --*

            Specifies the throttling rate limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

          - **cachingEnabled** *(boolean) --*

            Specifies whether responses should be cached and returned for requests. A cache
            cluster must be enabled on the stage for responses to be cached. The PATCH path for
            this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a
            Boolean.

          - **cacheTtlInSeconds** *(integer) --*

            Specifies the time to live (TTL), in seconds, for cached responses. The higher the
            TTL, the longer the response will be cached. The PATCH path for this setting is
            ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

          - **cacheDataEncrypted** *(boolean) --*

            Specifies whether the cached responses are encrypted. The PATCH path for this
            setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a
            Boolean.

          - **requireAuthorizationForCacheControl** *(boolean) --*

            Specifies whether authorization is required for a cache invalidation request. The
            PATCH path for this setting is
            ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the
            value is a Boolean.

          - **unauthorizedCacheControlHeaderStrategy** *(string) --*

            Specifies how to handle unauthorized requests for cache invalidation. The PATCH
            path for this setting is
            ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
            available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
            ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

    - **variables** *(dict) --*

      A map that defines the stage variables for a  Stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match
      ``[A-Za-z0-9-._~:/?#&=,]+`` .

      - *(string) --*

        - *(string) --*

    - **documentationVersion** *(string) --*

      The version of the associated API documentation.

    - **accessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **format** *(string) --*

        A single line format of the access logs of data, as specified by selected `$context
        variables
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
        . The format must include at least ``$context.requestId`` .

      - **destinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

    - **canarySettings** *(dict) --*

      Settings for the canary deployment in this stage.

      - **percentTraffic** *(float) --*

        The percent (0-100) of traffic diverted to a canary deployment.

      - **deploymentId** *(string) --*

        The ID of the canary deployment.

      - **stageVariableOverrides** *(dict) --*

        Stage variables overridden for a canary release deployment, including new stage
        variables introduced in the canary. These stage variables are represented as a
        string-to-string map between stage variable names and their values.

        - *(string) --*

          - *(string) --*

      - **useStageCache** *(boolean) --*

        A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

    - **tracingEnabled** *(boolean) --*

      Specifies whether active tracing with X-ray is enabled for the  Stage .

    - **webAclArn** *(string) --*

      The ARN of the WebAcl associated with the  Stage .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*

    - **createdDate** *(datetime) --*

      The timestamp when the stage was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the stage last updated.
    """


_ClientGetStagesResponseTypeDef = TypedDict(
    "_ClientGetStagesResponseTypeDef",
    {"item": List[ClientGetStagesResponseitemTypeDef]},
    total=False,
)


class ClientGetStagesResponseTypeDef(_ClientGetStagesResponseTypeDef):
    """
    Type definition for `ClientGetStages` `Response`

    A list of  Stage resources that are associated with the  ApiKey resource.

     `Deploying API in Stages
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/stages.html>`__

    - **item** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        Represents a unique identifier for a version of a deployed  RestApi that is callable by
        users.

          `Deploy an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__

        - **deploymentId** *(string) --*

          The identifier of the  Deployment that the stage points to.

        - **clientCertificateId** *(string) --*

          The identifier of a client certificate for an API stage.

        - **stageName** *(string) --*

          The name of the stage is the first path segment in the Uniform Resource Identifier (URI)
          of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens,
          and underscores. Maximum length is 128 characters.

        - **description** *(string) --*

          The stage's description.

        - **cacheClusterEnabled** *(boolean) --*

          Specifies whether a cache cluster is enabled for the stage.

        - **cacheClusterSize** *(string) --*

          The size of the cache cluster for the stage, if enabled.

        - **cacheClusterStatus** *(string) --*

          The status of the cache cluster for the stage, if enabled.

        - **methodSettings** *(dict) --*

          A map that defines the method settings for a  Stage resource. Keys (designated as
          ``/{method_setting_key`` below) are method paths defined as
          ``{resource_path}/{http_method}`` for an individual method override, or ``/\\*/\\*`` for
          overriding all methods in the stage.

          - *(string) --*

            - *(dict) --*

              Specifies the method setting properties.

              - **metricsEnabled** *(boolean) --*

                Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH
                path for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value
                is a Boolean.

              - **loggingLevel** *(string) --*

                Specifies the logging level for this method, which affects the log entries pushed
                to Amazon CloudWatch Logs. The PATCH path for this setting is
                ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
                ``ERROR`` , and ``INFO`` .

              - **dataTraceEnabled** *(boolean) --*

                Specifies whether data trace logging is enabled for this method, which affects the
                log entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
                ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

              - **throttlingBurstLimit** *(integer) --*

                Specifies the throttling burst limit. The PATCH path for this setting is
                ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

              - **throttlingRateLimit** *(float) --*

                Specifies the throttling rate limit. The PATCH path for this setting is
                ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

              - **cachingEnabled** *(boolean) --*

                Specifies whether responses should be cached and returned for requests. A cache
                cluster must be enabled on the stage for responses to be cached. The PATCH path for
                this setting is ``/{method_setting_key}/caching/enabled`` , and the value is a
                Boolean.

              - **cacheTtlInSeconds** *(integer) --*

                Specifies the time to live (TTL), in seconds, for cached responses. The higher the
                TTL, the longer the response will be cached. The PATCH path for this setting is
                ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

              - **cacheDataEncrypted** *(boolean) --*

                Specifies whether the cached responses are encrypted. The PATCH path for this
                setting is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a
                Boolean.

              - **requireAuthorizationForCacheControl** *(boolean) --*

                Specifies whether authorization is required for a cache invalidation request. The
                PATCH path for this setting is
                ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the
                value is a Boolean.

              - **unauthorizedCacheControlHeaderStrategy** *(string) --*

                Specifies how to handle unauthorized requests for cache invalidation. The PATCH
                path for this setting is
                ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
                available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
                ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

        - **variables** *(dict) --*

          A map that defines the stage variables for a  Stage resource. Variable names can have
          alphanumeric and underscore characters, and the values must match
          ``[A-Za-z0-9-._~:/?#&=,]+`` .

          - *(string) --*

            - *(string) --*

        - **documentationVersion** *(string) --*

          The version of the associated API documentation.

        - **accessLogSettings** *(dict) --*

          Settings for logging access in this stage.

          - **format** *(string) --*

            A single line format of the access logs of data, as specified by selected `$context
            variables
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
            . The format must include at least ``$context.requestId`` .

          - **destinationArn** *(string) --*

            The ARN of the CloudWatch Logs log group to receive access logs.

        - **canarySettings** *(dict) --*

          Settings for the canary deployment in this stage.

          - **percentTraffic** *(float) --*

            The percent (0-100) of traffic diverted to a canary deployment.

          - **deploymentId** *(string) --*

            The ID of the canary deployment.

          - **stageVariableOverrides** *(dict) --*

            Stage variables overridden for a canary release deployment, including new stage
            variables introduced in the canary. These stage variables are represented as a
            string-to-string map between stage variable names and their values.

            - *(string) --*

              - *(string) --*

          - **useStageCache** *(boolean) --*

            A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

        - **tracingEnabled** *(boolean) --*

          Specifies whether active tracing with X-ray is enabled for the  Stage .

        - **webAclArn** *(string) --*

          The ARN of the WebAcl associated with the  Stage .

        - **tags** *(dict) --*

          The collection of tags. Each tag element is associated with a given resource.

          - *(string) --*

            - *(string) --*

        - **createdDate** *(datetime) --*

          The timestamp when the stage was created.

        - **lastUpdatedDate** *(datetime) --*

          The timestamp when the stage last updated.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    Type definition for `ClientGetTags` `Response`

    The collection of tags. Each tag element is associated with a given resource.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientGetVpcLinkResponseTypeDef = TypedDict(
    "_ClientGetVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": str,
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetVpcLinkResponseTypeDef(_ClientGetVpcLinkResponseTypeDef):
    """
    Type definition for `ClientGetVpcLink` `Response`

    A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
    (VPC).

    To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
    you, as an API developer, create a  VpcLink resource targeted for one or more network load
    balancers of the VPC and then integrate an API method with a private integration that uses the
    VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has
    a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
    identify the  VpcLink used.

    - **id** *(string) --*

      The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

    - **name** *(string) --*

      The name used to label and identify the VPC link.

    - **description** *(string) --*

      The description of the VPC link.

    - **targetArns** *(list) --*

      The ARNs of network load balancers of the VPC targeted by the VPC link. The network load
      balancers must be owned by the same AWS account of the API owner.

      - *(string) --*

    - **status** *(string) --*

      The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` ,
      or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the
      status is ``DELETING`` .

    - **statusMessage** *(string) --*

      A description about the VPC link status.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientImportApiKeysResponseTypeDef = TypedDict(
    "_ClientImportApiKeysResponseTypeDef",
    {"ids": List[str], "warnings": List[str]},
    total=False,
)


class ClientImportApiKeysResponseTypeDef(_ClientImportApiKeysResponseTypeDef):
    """
    Type definition for `ClientImportApiKeys` `Response`

    The identifier of an  ApiKey used in a  UsagePlan .

    - **ids** *(list) --*

      A list of all the  ApiKey identifiers.

      - *(string) --*

    - **warnings** *(list) --*

      A list of warning messages.

      - *(string) --*
    """


_ClientImportDocumentationPartsResponseTypeDef = TypedDict(
    "_ClientImportDocumentationPartsResponseTypeDef",
    {"ids": List[str], "warnings": List[str]},
    total=False,
)


class ClientImportDocumentationPartsResponseTypeDef(
    _ClientImportDocumentationPartsResponseTypeDef
):
    """
    Type definition for `ClientImportDocumentationParts` `Response`

    A collection of the imported  DocumentationPart identifiers.

     This is used to return the result when documentation parts in an external (e.g., OpenAPI) file
     are imported into API Gateway  `Documenting an API
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
     , `documentationpart\\:import
     <https://docs.aws.amazon.com/apigateway/api-reference/link-relation/documentationpart-import/>`__
     ,  DocumentationPart

    - **ids** *(list) --*

      A list of the returned documentation part identifiers.

      - *(string) --*

    - **warnings** *(list) --*

      A list of warning messages reported during import of documentation parts.

      - *(string) --*
    """


_ClientImportRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientImportRestApiResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientImportRestApiResponseendpointConfigurationTypeDef(
    _ClientImportRestApiResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientImportRestApiResponse` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientImportRestApiResponseTypeDef = TypedDict(
    "_ClientImportRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientImportRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientImportRestApiResponseTypeDef(_ClientImportRestApiResponseTypeDef):
    """
    Type definition for `ClientImportRestApi` `Response`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports
      only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When
      compression is enabled, compression or decompression is not applied on the payload if the
      payload size is smaller than this value. Setting it to zero allows compression for any
      payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientPutIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientPutIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientPutIntegrationResponseResponseTypeDef(
    _ClientPutIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientPutIntegrationResponse` `Response`

    Represents an integration response. The status code must map to an existing  MethodResponse ,
    and parameters and templates can be used to transform the back-end response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response based
      on the response from the back end. For example, if the success response returns nothing and
      the error response returns some string, you could use the ``.+`` regex to match error
      response. However, make sure that the error response does not contain any newline (``\\n`` )
      character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function
      error header is matched. For all other HTTP and AWS back ends, the HTTP status code is
      matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the back end. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The
      mapped non-static value must match the pattern of ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the ``$``
      prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response templates
      are represented as a key/value map, with a content-type as the key and a template as the
      value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientPutIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientPutIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientPutIntegrationResponseintegrationResponsesTypeDef(
    _ClientPutIntegrationResponseintegrationResponsesTypeDef
):
    """
    Type definition for `ClientPutIntegrationResponse` `integrationResponses`

    Represents an integration response. The status code must map to an existing
    MethodResponse , and parameters and templates can be used to transform the back-end
    response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response
      based on the response from the back end. For example, if the success response returns
      nothing and the error response returns some string, you could use the ``.+`` regex to
      match error response. However, make sure that the error response does not contain any
      newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
      the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
      the HTTP status code is matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response
      from the back end. The key is a method response header parameter name and the mapped
      value is an integration response header value, a static value enclosed within a pair of
      single quotes, or a JSON expression from the integration response body. The mapping key
      must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
      and unique header name. The mapped non-static value must match the pattern of
      ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the
      ``$`` prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response
      templates are represented as a key/value map, with a content-type as the key and a
      template as the value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
      the corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
      Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientPutIntegrationResponseTypeDef = TypedDict(
    "_ClientPutIntegrationResponseTypeDef",
    {
        "type": str,
        "httpMethod": str,
        "uri": str,
        "connectionType": str,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": str,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientPutIntegrationResponseintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientPutIntegrationResponseTypeDef(_ClientPutIntegrationResponseTypeDef):
    """
    Type definition for `ClientPutIntegration` `Response`

    Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

     In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating
     an API <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **type** *(string) --*

      Specifies an API method integration type. The valid value is one of the following:

      * ``AWS`` : for integrating the API method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      the Lambda proxy integration.

      * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom
      integration.

      * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC, with the client request passed through as-is. This is
      also referred to as the HTTP proxy integration.

      * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back"
      endpoint without invoking any backend.

      For the HTTP and HTTP proxy integrations, each integration can specify a protocol
      (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom
      ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK``
      is referred to as a private integration and uses a  VpcLink to connect API Gateway to a
      network load balancer of a VPC.

    - **httpMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **uri** *(string) --*

      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded
      HTTP(S) URL according to the `RFC-3986 specification
      <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard
      integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where
      ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for
      routing.

      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form
      ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here,
      ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of
      the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain
      supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS
      service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The
      ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input
      parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The
      ensuing ``service_api`` refers to the path to an AWS service resource, including the region
      of the integrated AWS service, if applicable. For example, for integration with the S3 API of
      ```GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the
      ``uri`` can be either
      ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or
      ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``

    - **connectionType** *(string) --*

      The type of the network connection to the integration endpoint. The valid value is
      ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private
      connections between API Gateway and a network load balancer in a VPC. The default value is
      ``INTERNET`` .

    - **connectionId** *(string) --*

      The (```id`` <https://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__
      ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined,
      otherwise.

    - **credentials** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string ``arn:aws:iam::\\*:user/\\*`` . To use resource-based permissions
      on supported AWS services, specify null.

    - **requestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      back end. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the back end. The method request parameter value must match the
      pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` ,
      ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter
      name.

      - *(string) --*

        - *(string) --*

    - **requestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

    - **passthroughBehavior** *(string) --*

      Specifies how the method request body of an unmapped content type will be passed through the
      integration request to the back end without transformation. A content type is unmapped if no
      mapping template is defined in the integration or the content type does not match any of the
      mapped content types, as specified in ``requestTemplates`` . The valid value is one of the
      following:

      * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the
      back end without transformation when the method request content type does not match any
      content type associated with the mapping templates defined in the integration request.

      * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to
      the back end without transformation when no mapping template is defined in the integration
      request. If a template is defined when this option is selected, the method request of an
      unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response.

      * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response
      when either the method request content type does not match any content type associated with
      the mapping templates defined in the integration request or no mapping template is defined in
      the integration request.

    - **contentHandling** *(string) --*

      Specifies how to handle request payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the request payload will be passed through from the method
      request to integration request without modification, provided that the
      ``passthroughBehavior`` is configured to support payload pass-through.

    - **timeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.

    - **cacheNamespace** *(string) --*

      An API-specific tag group of related cached parameters. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

    - **cacheKeyParameters** *(list) --*

      A list of request parameters whose values API Gateway caches. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

      - *(string) --*

    - **integrationResponses** *(dict) --*

      Specifies the integration's responses.

       Example: Get integration responses of a method Request

       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200
       HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
       20160607T191449Z Authorization: AWS4-HMAC-SHA256
       Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request,
       SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

      The successful response returns ``200 OK`` status and a payload as follows:

       ``{ "_links": { "curies": { "href":
       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
       "name": "integrationresponse", "templated": true }, "self": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title":
       "200" }, "integrationresponse:delete": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" },
       "integrationresponse:update": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } },
       "responseParameters": { "method.response.header.Content-Type": "'application/xml'" },
       "responseTemplates": { "application/json":
       "$util.urlDecode(\\"%3CkinesisStreams%3E#foreach($stream in
       $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\\")\\n"
       }, "statusCode": "200" }``

         `Creating an API
         <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

      - *(string) --*

        - *(dict) --*

          Represents an integration response. The status code must map to an existing
          MethodResponse , and parameters and templates can be used to transform the back-end
          response.

            `Creating an API
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

          - **statusCode** *(string) --*

            Specifies the status code that is used to map the integration response to an existing
            MethodResponse .

          - **selectionPattern** *(string) --*

            Specifies the regular expression (regex) pattern used to choose an integration response
            based on the response from the back end. For example, if the success response returns
            nothing and the error response returns some string, you could use the ``.+`` regex to
            match error response. However, make sure that the error response does not contain any
            newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
            the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
            the HTTP status code is matched.

          - **responseParameters** *(dict) --*

            A key-value map specifying response parameters that are passed to the method response
            from the back end. The key is a method response header parameter name and the mapped
            value is an integration response header value, a static value enclosed within a pair of
            single quotes, or a JSON expression from the integration response body. The mapping key
            must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
            and unique header name. The mapped non-static value must match the pattern of
            ``integration.response.header.{name}`` or
            ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
            response header name and ``JSON-expression`` is a valid JSON expression without the
            ``$`` prefix.

            - *(string) --*

              - *(string) --*

          - **responseTemplates** *(dict) --*

            Specifies the templates used to transform the integration response body. Response
            templates are represented as a key/value map, with a content-type as the key and a
            template as the value.

            - *(string) --*

              - *(string) --*

          - **contentHandling** *(string) --*

            Specifies how to handle response payload content type conversions. Supported values are
            ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

            * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
            the corresponding binary blob.

            * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
            Base64-encoded string.

            If this property is not defined, the response payload will be passed through from the
            integration response to the method response without modification.
    """


_ClientPutMethodResponseResponseTypeDef = TypedDict(
    "_ClientPutMethodResponseResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)


class ClientPutMethodResponseResponseTypeDef(_ClientPutMethodResponseResponseTypeDef):
    """
    Type definition for `ClientPutMethodResponse` `Response`

    Represents a method response of a given HTTP status code returned to the client. The method
    response is passed from the back end through the associated integration response that can be
    transformed using a mapping template.

     Example: A **MethodResponse** instance of an API Request

    The example request retrieves a **MethodResponse** of the 200 status code.

     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1
     Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
     20160603T222952Z Authorization: AWS4-HMAC-SHA256
     Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request,
     SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

    The successful response returns ``200 OK`` status and a payload as follows:

     ``{ "_links": { "curies": { "href":
     "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
     "name": "methodresponse", "templated": true }, "self": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" },
     "methodresponse:delete": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" },
     "methodresponse:update": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": {
     "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type":
     false }, "statusCode": "200" }``

        Method ,  IntegrationResponse ,  Integration  `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      The method response's status code.

    - **responseParameters** *(dict) --*

      A key-value map specifying required or optional response parameters that API Gateway can send
      back to the caller. A key defines a method response header and the value specifies whether
      the associated method response header is required or not. The expression of the key must
      match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique
      header name. API Gateway passes certain integration response data to the method response
      headers specified here according to the mapping you prescribe in the API's
      IntegrationResponse . The integration response data that can be mapped include an integration
      response header expressed in ``integration.response.header.{name}`` , a static value enclosed
      within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the
      back-end response payload in the form of ``integration.response.body.{JSON-expression}`` ,
      where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

      - *(string) --*

        - *(boolean) --*

    - **responseModels** *(dict) --*

      Specifies the  Model resources used for the response's content-type. Response models are
      represented as a key/value map, with a content-type as the key and a  Model name as the value.

      - *(string) --*

        - *(string) --*
    """


_ClientPutRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientPutRestApiResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientPutRestApiResponseendpointConfigurationTypeDef(
    _ClientPutRestApiResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientPutRestApiResponse` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientPutRestApiResponseTypeDef = TypedDict(
    "_ClientPutRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientPutRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientPutRestApiResponseTypeDef(_ClientPutRestApiResponseTypeDef):
    """
    Type definition for `ClientPutRestApi` `Response`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports
      only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When
      compression is enabled, compression or decompression is not applied on the payload if the
      payload size is smaller than this value. Setting it to zero allows compression for any
      payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
    },
    total=False,
)


class ClientTestInvokeAuthorizerResponseTypeDef(
    _ClientTestInvokeAuthorizerResponseTypeDef
):
    """
    Type definition for `ClientTestInvokeAuthorizer` `Response`

    Represents the response of the test invoke request for a custom  Authorizer

    - **clientStatus** *(integer) --*

      The HTTP status code that the client would have received. Value is 0 if the authorizer
      succeeded.

    - **log** *(string) --*

      The API Gateway execution log for the test authorizer request.

    - **latency** *(integer) --*

      The execution latency of the test authorizer request.

    - **principalId** *(string) --*

      The principal identity returned by the  Authorizer

    - **policy** *(string) --*

      The JSON policy document returned by the  Authorizer

    - **authorization** *(dict) --*

      - *(string) --*

        - *(list) --*

          - *(string) --*

    - **claims** *(dict) --*

      The `open identity claims
      <https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims>`__ , with any
      supported custom attributes, returned from the Cognito Your User Pool configured for the API.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateAccountResponsethrottleSettingsTypeDef = TypedDict(
    "_ClientUpdateAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientUpdateAccountResponsethrottleSettingsTypeDef(
    _ClientUpdateAccountResponsethrottleSettingsTypeDef
):
    """
    Type definition for `ClientUpdateAccountResponse` `throttleSettings`

    Specifies the API request limits configured for the current  Account .

    - **burstLimit** *(integer) --*

      The API request burst limit, the maximum rate limit over a time ranging from one to a few
      seconds, depending upon whether the underlying token bucket is at its full capacity.

    - **rateLimit** *(float) --*

      The API request steady-state rate limit.
    """


_ClientUpdateAccountResponseTypeDef = TypedDict(
    "_ClientUpdateAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientUpdateAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)


class ClientUpdateAccountResponseTypeDef(_ClientUpdateAccountResponseTypeDef):
    """
    Type definition for `ClientUpdateAccount` `Response`

    Represents an AWS account that is associated with API Gateway.

    To view the account info, call ``GET`` on this resource.

     Error Codes

    The following exception may be thrown when the request fails.

    * UnauthorizedException

    * NotFoundException

    * TooManyRequestsException

    For detailed error code information, including the corresponding HTTP Status Codes, see `API
    Gateway Error Codes
    <https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/#api-error-codes>`__

     Example: Get the information about an account. Request ``GET /account HTTP/1.1 Content-Type:
     application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z
     Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request,
     SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

    The successful response returns a ``200 OK`` status code and a payload similar to the following:

     ``{ "_links": { "curies": { "href":
     "https://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html",
     "name": "account", "templated": true }, "self": { "href": "/account" }, "account:update": {
     "href": "/account" } }, "cloudwatchRoleArn":
     "arn:aws:iam::123456789012:role/apigAwsProxyRole", "throttleSettings": { "rateLimit": 500,
     "burstLimit": 1000 } }``

    In addition to making the REST API call directly, you can use the AWS CLI and an AWS SDK to
    access this resource.

       `API Gateway Limits
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-limits.html>`__
       `Developer Guide
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>`__ , `AWS CLI
       <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-account.html>`__

    - **cloudwatchRoleArn** *(string) --*

      The ARN of an Amazon CloudWatch role for the current  Account .

    - **throttleSettings** *(dict) --*

      Specifies the API request limits configured for the current  Account .

      - **burstLimit** *(integer) --*

        The API request burst limit, the maximum rate limit over a time ranging from one to a few
        seconds, depending upon whether the underlying token bucket is at its full capacity.

      - **rateLimit** *(float) --*

        The API request steady-state rate limit.

    - **features** *(list) --*

      A list of features supported for the account. When usage plans are enabled, the features list
      will include an entry of ``"UsagePlans"`` .

      - *(string) --*

    - **apiKeyVersion** *(string) --*

      The version of the API keys used for the account.
    """


_ClientUpdateApiKeyResponseTypeDef = TypedDict(
    "_ClientUpdateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateApiKeyResponseTypeDef(_ClientUpdateApiKeyResponseTypeDef):
    """
    Type definition for `ClientUpdateApiKey` `Response`

    A resource that can be distributed to callers for executing  Method resources that require an
    API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
    callers with the API key can make requests to that stage.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **id** *(string) --*

      The identifier of the API Key.

    - **value** *(string) --*

      The value of the API Key.

    - **name** *(string) --*

      The name of the API Key.

    - **customerId** *(string) --*

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    - **description** *(string) --*

      The description of the API Key.

    - **enabled** *(boolean) --*

      Specifies whether the API Key can be used by callers.

    - **createdDate** *(datetime) --*

      The timestamp when the API Key was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the API Key was last updated.

    - **stageKeys** *(list) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

      - *(string) --*

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateBasePathMappingResponseTypeDef = TypedDict(
    "_ClientUpdateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientUpdateBasePathMappingResponseTypeDef(
    _ClientUpdateBasePathMappingResponseTypeDef
):
    """
    Type definition for `ClientUpdateBasePathMapping` `Response`

    Represents the base path that callers of the API must provide as part of the URL after the
    domain name.

     A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
     in a given stage of the owner  Account .  `Use Custom Domain Names
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **basePath** *(string) --*

      The base path name that callers of the API must provide as part of the URL after the domain
      name.

    - **restApiId** *(string) --*

      The string identifier of the associated  RestApi .

    - **stage** *(string) --*

      The name of the associated stage.
    """


_ClientUpdateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientUpdateDeploymentResponseapiSummaryTypeDef(
    _ClientUpdateDeploymentResponseapiSummaryTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentResponse` `apiSummary`

    Represents a summary of a  Method resource, given a particular date and time.

    - **authorizationType** *(string) --*

      The method's authorization type. Valid values are ``NONE`` for open access,
      ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
      authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

    - **apiKeyRequired** *(boolean) --*

      Specifies whether the method requires a valid  ApiKey .
    """


_ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[
            str, Dict[str, ClientUpdateDeploymentResponseapiSummaryTypeDef]
        ],
    },
    total=False,
)


class ClientUpdateDeploymentResponseTypeDef(_ClientUpdateDeploymentResponseTypeDef):
    """
    Type definition for `ClientUpdateDeployment` `Response`

    An immutable representation of a  RestApi resource that can be called by users using  Stages .
    A deployment must be associated with a  Stage for it to be callable over the Internet.

     To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
     update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
     deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
     Deployments ,  Stage , `AWS CLI
     <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
     SDKs <https://aws.amazon.com/tools/>`__

    - **id** *(string) --*

      The identifier for the deployment resource.

    - **description** *(string) --*

      The description for the deployment resource.

    - **createdDate** *(datetime) --*

      The date and time that the deployment resource was created.

    - **apiSummary** *(dict) --*

      A summary of the  RestApi at the date and time that the deployment resource was created.

      - *(string) --*

        - *(dict) --*

          - *(string) --*

            - *(dict) --*

              Represents a summary of a  Method resource, given a particular date and time.

              - **authorizationType** *(string) --*

                The method's authorization type. Valid values are ``NONE`` for open access,
                ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

              - **apiKeyRequired** *(boolean) --*

                Specifies whether the method requires a valid  ApiKey .
    """


_ClientUpdateDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientUpdateDocumentationPartResponselocationTypeDef",
    {"type": str, "path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientUpdateDocumentationPartResponselocationTypeDef(
    _ClientUpdateDocumentationPartResponselocationTypeDef
):
    """
    Type definition for `ClientUpdateDocumentationPartResponse` `location`

    The location of the API entity to which the documentation applies. Valid fields depend on the
    targeted API entity type. All the valid location fields are not required. If not explicitly
    specified, a valid location field is treated as a wildcard and associated documentation
    content may be inherited by matching entities, unless overridden.

    - **type** *(string) --*

      [Required] The type of API entity to which the documentation content applies. Valid values
      are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
      ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
      ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
      entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
      ``RESOURCE`` type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
      ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
      ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
      value is ``/`` for the root resource. When an applicable child entity inherits the content
      of another entity of the same type with more general specifications of the other
      ``location`` attributes, the child entity's ``path`` attribute must match that of the
      parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any method. When an applicable child entity inherits the content of an entity of the same
      type with more general specifications of the other ``location`` attributes, the child
      entity's ``method`` attribute must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
      any status code. When an applicable child entity inherits the content of an entity of the
      same type with more general specifications of the other ``location`` attributes, the child
      entity's ``statusCode`` attribute must match that of the parent entity exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API entity
      types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
      any other entity type.
    """


_ClientUpdateDocumentationPartResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientUpdateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientUpdateDocumentationPartResponseTypeDef(
    _ClientUpdateDocumentationPartResponseTypeDef
):
    """
    Type definition for `ClientUpdateDocumentationPart` `Response`

    A documentation part for a targeted API entity.

    A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
    The target specifies an API entity to which the documentation content applies. The supported
    API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
    ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE``
    , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API
    entity type. All valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an API can use any
    shape for the content map, only the OpenAPI-compliant documentation fields will be injected
    into the associated API entity definition in the exported OpenAPI definition file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationParts

    - **id** *(string) --*

      The  DocumentationPart identifier, generated by API Gateway when the ``DocumentationPart`` is
      created.

    - **location** *(dict) --*

      The location of the API entity to which the documentation applies. Valid fields depend on the
      targeted API entity type. All the valid location fields are not required. If not explicitly
      specified, a valid location field is treated as a wildcard and associated documentation
      content may be inherited by matching entities, unless overridden.

      - **type** *(string) --*

        [Required] The type of API entity to which the documentation content applies. Valid values
        are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
        ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
        ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any
        entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or
        ``RESOURCE`` type.

      - **path** *(string) --*

        The URL path of the target. It is a valid field for the API entity types of ``RESOURCE`` ,
        ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
        ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
        value is ``/`` for the root resource. When an applicable child entity inherits the content
        of another entity of the same type with more general specifications of the other
        ``location`` attributes, the child entity's ``path`` attribute must match that of the
        parent entity as a prefix.

      - **method** *(string) --*

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any method. When an applicable child entity inherits the content of an entity of the same
        type with more general specifications of the other ``location`` attributes, the child
        entity's ``method`` attribute must match that of the parent entity exactly.

      - **statusCode** *(string) --*

        The HTTP status code of a response. It is a valid field for the API entity types of
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*`` for
        any status code. When an applicable child entity inherits the content of an entity of the
        same type with more general specifications of the other ``location`` attributes, the child
        entity's ``statusCode`` attribute must match that of the parent entity exactly.

      - **name** *(string) --*

        The name of the targeted API entity. It is a valid and required field for the API entity
        types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field for
        any other entity type.

    - **properties** *(string) --*

      A content map of API-specific key-value pairs describing the targeted API entity. The map
      must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\" }"`` .
      Only OpenAPI-compliant documentation-related fields from the propertiesmap are exported and,
      hence, published as part of the API entity definitions, while the original documentation
      parts are exported in a OpenAPI extension of ``x-amazon-apigateway-documentation`` .
    """


_ClientUpdateDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientUpdateDocumentationVersionResponseTypeDef(
    _ClientUpdateDocumentationVersionResponseTypeDef
):
    """
    Type definition for `ClientUpdateDocumentationVersion` `Response`

    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version associated with an API
    stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersions

    - **version** *(string) --*

      The version identifier of the API documentation snapshot.

    - **createdDate** *(datetime) --*

      The date when the API documentation snapshot is created.

    - **description** *(string) --*

      The description of the API documentation snapshot.
    """


_ClientUpdateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientUpdateDomainNameResponseendpointConfigurationTypeDef(
    _ClientUpdateDomainNameResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDomainNameResponse` `endpointConfiguration`

    The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientUpdateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": str,
        "domainNameStatusMessage": str,
        "securityPolicy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateDomainNameResponseTypeDef(_ClientUpdateDomainNameResponseTypeDef):
    """
    Type definition for `ClientUpdateDomainName` `Response`

    Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

    When you deploy an API, API Gateway creates a default host name for the API. This default API
    host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
    default host name, you can access the API's root resource with the URL of
    ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a custom
    domain name of ``apis.example.com`` for this API, you can then access the same resource using
    the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path mapping (
    BasePathMapping ) of your API under the custom domain name.

       `Set a Custom Host Name for an API
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

    - **domainName** *(string) --*

      The custom domain name as an API host name, for example, ``my-api.example.com`` .

    - **certificateName** *(string) --*

      The name of the certificate that will be used by edge-optimized endpoint for this domain name.

    - **certificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for
      this domain name. AWS Certificate Manager is the only supported source.

    - **certificateUploadDate** *(datetime) --*

      The timestamp when the certificate that was used by edge-optimized endpoint for this domain
      name was uploaded.

    - **regionalDomainName** *(string) --*

      The domain name associated with the regional endpoint for this custom domain name. You set up
      this association by adding a DNS record that points the custom domain name to this regional
      domain name. The regional domain name is returned by API Gateway when you create a regional
      endpoint.

    - **regionalHostedZoneId** *(string) --*

      The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more
      information, see `Set up a Regional Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **regionalCertificateName** *(string) --*

      The name of the certificate that will be used for validating the regional domain name.

    - **regionalCertificateArn** *(string) --*

      The reference to an AWS-managed certificate that will be used for validating the regional
      domain name. AWS Certificate Manager is the only supported source.

    - **distributionDomainName** *(string) --*

      The domain name of the Amazon CloudFront distribution associated with this custom domain name
      for an edge-optimized endpoint. You set up this association when adding a DNS record pointing
      the custom domain name to this distribution name. For more information about CloudFront
      distributions, see the `Amazon CloudFront documentation
      <https://aws.amazon.com/documentation/cloudfront/>`__ .

    - **distributionHostedZoneId** *(string) --*

      The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid
      value is ``Z2FDTNDATAQYW2`` for all the regions. For more information, see `Set up a Regional
      Custom Domain Name
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
      and `AWS Regions and Endpoints for API Gateway
      <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  DomainName showing the endpoint types of the domain name.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **domainNameStatus** *(string) --*

      The status of the  DomainName migration. The valid values are ``AVAILABLE`` and ``UPDATING``
      . If the status is ``UPDATING`` , the domain cannot be modified further until the existing
      operation is complete. If it is ``AVAILABLE`` , the domain can be updated.

    - **domainNameStatusMessage** *(string) --*

      An optional text message containing detailed information about status of the  DomainName
      migration.

    - **securityPolicy** *(string) --*

      The Transport Layer Security (TLS) version + cipher suite for this  DomainName . The valid
      values are ``TLS_1_0`` and ``TLS_1_2`` .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientUpdateIntegrationResponseResponseTypeDef(
    _ClientUpdateIntegrationResponseResponseTypeDef
):
    """
    Type definition for `ClientUpdateIntegrationResponse` `Response`

    Represents an integration response. The status code must map to an existing  MethodResponse ,
    and parameters and templates can be used to transform the back-end response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response based
      on the response from the back end. For example, if the success response returns nothing and
      the error response returns some string, you could use the ``.+`` regex to match error
      response. However, make sure that the error response does not contain any newline (``\\n`` )
      character in such cases. If the back end is an AWS Lambda function, the AWS Lambda function
      error header is matched. For all other HTTP and AWS back ends, the HTTP status code is
      matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response from
      the back end. The key is a method response header parameter name and the mapped value is an
      integration response header value, a static value enclosed within a pair of single quotes, or
      a JSON expression from the integration response body. The mapping key must match the pattern
      of ``method.response.header.{name}`` , where ``name`` is a valid and unique header name. The
      mapped non-static value must match the pattern of ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the ``$``
      prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response templates
      are represented as a key/value map, with a content-type as the key and a template as the
      value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientUpdateIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": str,
    },
    total=False,
)


class ClientUpdateIntegrationResponseintegrationResponsesTypeDef(
    _ClientUpdateIntegrationResponseintegrationResponsesTypeDef
):
    """
    Type definition for `ClientUpdateIntegrationResponse` `integrationResponses`

    Represents an integration response. The status code must map to an existing
    MethodResponse , and parameters and templates can be used to transform the back-end
    response.

      `Creating an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      Specifies the status code that is used to map the integration response to an existing
      MethodResponse .

    - **selectionPattern** *(string) --*

      Specifies the regular expression (regex) pattern used to choose an integration response
      based on the response from the back end. For example, if the success response returns
      nothing and the error response returns some string, you could use the ``.+`` regex to
      match error response. However, make sure that the error response does not contain any
      newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
      the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
      the HTTP status code is matched.

    - **responseParameters** *(dict) --*

      A key-value map specifying response parameters that are passed to the method response
      from the back end. The key is a method response header parameter name and the mapped
      value is an integration response header value, a static value enclosed within a pair of
      single quotes, or a JSON expression from the integration response body. The mapping key
      must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
      and unique header name. The mapped non-static value must match the pattern of
      ``integration.response.header.{name}`` or
      ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
      response header name and ``JSON-expression`` is a valid JSON expression without the
      ``$`` prefix.

      - *(string) --*

        - *(string) --*

    - **responseTemplates** *(dict) --*

      Specifies the templates used to transform the integration response body. Response
      templates are represented as a key/value map, with a content-type as the key and a
      template as the value.

      - *(string) --*

        - *(string) --*

    - **contentHandling** *(string) --*

      Specifies how to handle response payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
      the corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
      Base64-encoded string.

      If this property is not defined, the response payload will be passed through from the
      integration response to the method response without modification.
    """


_ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseTypeDef",
    {
        "type": str,
        "httpMethod": str,
        "uri": str,
        "connectionType": str,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": str,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientUpdateIntegrationResponseintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIntegrationResponseTypeDef(_ClientUpdateIntegrationResponseTypeDef):
    """
    Type definition for `ClientUpdateIntegration` `Response`

    Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

     In the API Gateway console, the built-in Lambda integration is an AWS integration.  `Creating
     an API <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **type** *(string) --*

      Specifies an API method integration type. The valid value is one of the following:

      * ``AWS`` : for integrating the API method request with an AWS service action, including the
      Lambda function-invoking action. With the Lambda function-invoking action, this is referred
      to as the Lambda custom integration. With any other AWS service action, this is known as AWS
      integration.

      * ``AWS_PROXY`` : for integrating the API method request with the Lambda function-invoking
      action with the client request passed through as-is. This integration is also referred to as
      the Lambda proxy integration.

      * ``HTTP`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom
      integration.

      * ``HTTP_PROXY`` : for integrating the API method request with an HTTP endpoint, including a
      private HTTP endpoint within a VPC, with the client request passed through as-is. This is
      also referred to as the HTTP proxy integration.

      * ``MOCK`` : for integrating the API method request with API Gateway as a "loop-back"
      endpoint without invoking any backend.

      For the HTTP and HTTP proxy integrations, each integration can specify a protocol
      (``http/https`` ), port and path. Standard 80 and 443 ports are supported as well as custom
      ports above 1024. An HTTP or HTTP proxy integration with a ``connectionType`` of ``VPC_LINK``
      is referred to as a private integration and uses a  VpcLink to connect API Gateway to a
      network load balancer of a VPC.

    - **httpMethod** *(string) --*

      Specifies the integration's HTTP method type.

    - **uri** *(string) --*

      Specifies Uniform Resource Identifier (URI) of the integration endpoint.

      * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully formed, encoded
      HTTP(S) URL according to the `RFC-3986 specification
      <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard
      integration, where ``connectionType`` is not ``VPC_LINK`` , or private integration, where
      ``connectionType`` is ``VPC_LINK`` . For a private HTTP integration, the URI is not used for
      routing.

      * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form
      ``arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`` . Here,
      ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` ); ``{service}`` is the name of
      the integrated AWS service (e.g., ``s3`` ); and ``{subdomain}`` is a designated subdomain
      supported by certain AWS service for fast host-name lookup. ``action`` can be used for an AWS
      service action-based API, using an ``Action={name}&{p1}={v1}&p2={v2}...`` query string. The
      ensuing ``{service_api}`` refers to a supported action ``{name}`` plus any required input
      parameters. Alternatively, ``path`` can be used for an AWS service path-based API. The
      ensuing ``service_api`` refers to the path to an AWS service resource, including the region
      of the integrated AWS service, if applicable. For example, for integration with the S3 API of
      ```GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__`` , the
      ``uri`` can be either
      ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}`` or
      ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``

    - **connectionType** *(string) --*

      The type of the network connection to the integration endpoint. The valid value is
      ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private
      connections between API Gateway and a network load balancer in a VPC. The default value is
      ``INTERNET`` .

    - **connectionId** *(string) --*

      The (```id`` <https://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__
      ) of the  VpcLink used for the integration when ``connectionType=VPC_LINK`` and undefined,
      otherwise.

    - **credentials** *(string) --*

      Specifies the credentials required for the integration, if any. For AWS integrations, three
      options are available. To specify an IAM Role for API Gateway to assume, use the role's
      Amazon Resource Name (ARN). To require that the caller's identity be passed through from the
      request, specify the string ``arn:aws:iam::\\*:user/\\*`` . To use resource-based permissions
      on supported AWS services, specify null.

    - **requestParameters** *(dict) --*

      A key-value map specifying request parameters that are passed from the method request to the
      back end. The key is an integration request parameter name and the associated value is a
      method request parameter value or static value that must be enclosed within single quotes and
      pre-encoded as required by the back end. The method request parameter value must match the
      pattern of ``method.request.{location}.{name}`` , where ``location`` is ``querystring`` ,
      ``path`` , or ``header`` and ``name`` must be a valid and unique method request parameter
      name.

      - *(string) --*

        - *(string) --*

    - **requestTemplates** *(dict) --*

      Represents a map of Velocity templates that are applied on the request payload based on the
      value of the Content-Type header sent by the client. The content type value is the key in
      this map, and the template (as a String) is the value.

      - *(string) --*

        - *(string) --*

    - **passthroughBehavior** *(string) --*

      Specifies how the method request body of an unmapped content type will be passed through the
      integration request to the back end without transformation. A content type is unmapped if no
      mapping template is defined in the integration or the content type does not match any of the
      mapped content types, as specified in ``requestTemplates`` . The valid value is one of the
      following:

      * ``WHEN_NO_MATCH`` : passes the method request body through the integration request to the
      back end without transformation when the method request content type does not match any
      content type associated with the mapping templates defined in the integration request.

      * ``WHEN_NO_TEMPLATES`` : passes the method request body through the integration request to
      the back end without transformation when no mapping template is defined in the integration
      request. If a template is defined when this option is selected, the method request of an
      unmapped content-type will be rejected with an HTTP ``415 Unsupported Media Type`` response.

      * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported Media Type`` response
      when either the method request content type does not match any content type associated with
      the mapping templates defined in the integration request or no mapping template is defined in
      the integration request.

    - **contentHandling** *(string) --*

      Specifies how to handle request payload content type conversions. Supported values are
      ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

      * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded string to the
      corresponding binary blob.

      * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a Base64-encoded
      string.

      If this property is not defined, the request payload will be passed through from the method
      request to integration request without modification, provided that the
      ``passthroughBehavior`` is configured to support payload pass-through.

    - **timeoutInMillis** *(integer) --*

      Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds
      or 29 seconds.

    - **cacheNamespace** *(string) --*

      An API-specific tag group of related cached parameters. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

    - **cacheKeyParameters** *(list) --*

      A list of request parameters whose values API Gateway caches. To be valid values for
      ``cacheKeyParameters`` , these parameters must also be specified for  Method
      ``requestParameters`` .

      - *(string) --*

    - **integrationResponses** *(dict) --*

      Specifies the integration's responses.

       Example: Get integration responses of a method Request

       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200
       HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
       20160607T191449Z Authorization: AWS4-HMAC-SHA256
       Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request,
       SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

      The successful response returns ``200 OK`` status and a payload as follows:

       ``{ "_links": { "curies": { "href":
       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
       "name": "integrationresponse", "templated": true }, "self": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200", "title":
       "200" }, "integrationresponse:delete": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" },
       "integrationresponse:update": { "href":
       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200" } },
       "responseParameters": { "method.response.header.Content-Type": "'application/xml'" },
       "responseTemplates": { "application/json":
       "$util.urlDecode(\\"%3CkinesisStreams%3E#foreach($stream in
       $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\\")\\n"
       }, "statusCode": "200" }``

         `Creating an API
         <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

      - *(string) --*

        - *(dict) --*

          Represents an integration response. The status code must map to an existing
          MethodResponse , and parameters and templates can be used to transform the back-end
          response.

            `Creating an API
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

          - **statusCode** *(string) --*

            Specifies the status code that is used to map the integration response to an existing
            MethodResponse .

          - **selectionPattern** *(string) --*

            Specifies the regular expression (regex) pattern used to choose an integration response
            based on the response from the back end. For example, if the success response returns
            nothing and the error response returns some string, you could use the ``.+`` regex to
            match error response. However, make sure that the error response does not contain any
            newline (``\\n`` ) character in such cases. If the back end is an AWS Lambda function,
            the AWS Lambda function error header is matched. For all other HTTP and AWS back ends,
            the HTTP status code is matched.

          - **responseParameters** *(dict) --*

            A key-value map specifying response parameters that are passed to the method response
            from the back end. The key is a method response header parameter name and the mapped
            value is an integration response header value, a static value enclosed within a pair of
            single quotes, or a JSON expression from the integration response body. The mapping key
            must match the pattern of ``method.response.header.{name}`` , where ``name`` is a valid
            and unique header name. The mapped non-static value must match the pattern of
            ``integration.response.header.{name}`` or
            ``integration.response.body.{JSON-expression}`` , where ``name`` is a valid and unique
            response header name and ``JSON-expression`` is a valid JSON expression without the
            ``$`` prefix.

            - *(string) --*

              - *(string) --*

          - **responseTemplates** *(dict) --*

            Specifies the templates used to transform the integration response body. Response
            templates are represented as a key/value map, with a content-type as the key and a
            template as the value.

            - *(string) --*

              - *(string) --*

          - **contentHandling** *(string) --*

            Specifies how to handle response payload content type conversions. Supported values are
            ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

            * ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to
            the corresponding binary blob.

            * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a
            Base64-encoded string.

            If this property is not defined, the response payload will be passed through from the
            integration response to the method response without modification.
    """


_ClientUpdateMethodResponseResponseTypeDef = TypedDict(
    "_ClientUpdateMethodResponseResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)


class ClientUpdateMethodResponseResponseTypeDef(
    _ClientUpdateMethodResponseResponseTypeDef
):
    """
    Type definition for `ClientUpdateMethodResponse` `Response`

    Represents a method response of a given HTTP status code returned to the client. The method
    response is passed from the back end through the associated integration response that can be
    transformed using a mapping template.

     Example: A **MethodResponse** instance of an API Request

    The example request retrieves a **MethodResponse** of the 200 status code.

     ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200 HTTP/1.1
     Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
     20160603T222952Z Authorization: AWS4-HMAC-SHA256
     Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request,
     SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}``  Response

    The successful response returns ``200 OK`` status and a payload as follows:

     ``{ "_links": { "curies": { "href":
     "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
     "name": "methodresponse", "templated": true }, "self": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "title": "200" },
     "methodresponse:delete": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" },
     "methodresponse:update": { "href":
     "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } }, "responseModels": {
     "application/json": "Empty" }, "responseParameters": { "method.response.header.Content-Type":
     false }, "statusCode": "200" }``

        Method ,  IntegrationResponse ,  Integration  `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **statusCode** *(string) --*

      The method response's status code.

    - **responseParameters** *(dict) --*

      A key-value map specifying required or optional response parameters that API Gateway can send
      back to the caller. A key defines a method response header and the value specifies whether
      the associated method response header is required or not. The expression of the key must
      match the pattern ``method.response.header.{name}`` , where ``name`` is a valid and unique
      header name. API Gateway passes certain integration response data to the method response
      headers specified here according to the mapping you prescribe in the API's
      IntegrationResponse . The integration response data that can be mapped include an integration
      response header expressed in ``integration.response.header.{name}`` , a static value enclosed
      within a pair of single quotes (e.g., ``'application/json'`` ), or a JSON expression from the
      back-end response payload in the form of ``integration.response.body.{JSON-expression}`` ,
      where ``JSON-expression`` is a valid JSON expression without the ``$`` prefix.)

      - *(string) --*

        - *(boolean) --*

    - **responseModels** *(dict) --*

      Specifies the  Model resources used for the response's content-type. Response models are
      represented as a key/value map, with a content-type as the key and a  Model name as the value.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateModelResponseTypeDef = TypedDict(
    "_ClientUpdateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientUpdateModelResponseTypeDef(_ClientUpdateModelResponseTypeDef):
    """
    Type definition for `ClientUpdateModel` `Response`

    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request payload. A response
    model defines the data structure of the response payload returned by the back end. Although not
    required, models are useful for mapping payloads between the front end and back end.

    A model is used for generating an API's SDK, validating the input request body, and creating a
    skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **id** *(string) --*

      The identifier for the model resource.

    - **name** *(string) --*

      The name of the model. Must be an alphanumeric string.

    - **description** *(string) --*

      The description of the model.

    - **schema** *(string) --*

      The schema for the model. For ``application/json`` models, this should be `JSON schema draft
      4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include "\\*/"
      characters in the description of any properties because such "\\*/" characters may be
      interpreted as the closing marker for comments in some languages, such as Java or JavaScript,
      causing the installation of your API's SDK generated by API Gateway to fail.

    - **contentType** *(string) --*

      The content-type for the model.
    """


_ClientUpdateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientUpdateRestApiResponseendpointConfigurationTypeDef(
    _ClientUpdateRestApiResponseendpointConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateRestApiResponse` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
      For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
      a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
      private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
      is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_ClientUpdateRestApiResponseTypeDef = TypedDict(
    "_ClientUpdateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": ClientUpdateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateRestApiResponseTypeDef(_ClientUpdateRestApiResponseTypeDef):
    """
    Type definition for `ClientUpdateRestApi` `Response`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi supports
      only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When
      compression is enabled, compression or decompression is not applied on the payload if the
      payload size is smaller than this value. Setting it to zero allows compression for any
      payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ).
        For an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For
        a regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a
        private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes. It
        is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientUpdateStageResponseaccessLogSettingsTypeDef(
    _ClientUpdateStageResponseaccessLogSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `accessLogSettings`

    Settings for logging access in this stage.

    - **format** *(string) --*

      A single line format of the access logs of data, as specified by selected `$context
      variables
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
      . The format must include at least ``$context.requestId`` .

    - **destinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientUpdateStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientUpdateStageResponsecanarySettingsTypeDef(
    _ClientUpdateStageResponsecanarySettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `canarySettings`

    Settings for the canary deployment in this stage.

    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.

    - **deploymentId** *(string) --*

      The ID of the canary deployment.

    - **stageVariableOverrides** *(dict) --*

      Stage variables overridden for a canary release deployment, including new stage variables
      introduced in the canary. These stage variables are represented as a string-to-string map
      between stage variable names and their values.

      - *(string) --*

        - *(string) --*

    - **useStageCache** *(boolean) --*

      A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
    """


_ClientUpdateStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": str,
    },
    total=False,
)


class ClientUpdateStageResponsemethodSettingsTypeDef(
    _ClientUpdateStageResponsemethodSettingsTypeDef
):
    """
    Type definition for `ClientUpdateStageResponse` `methodSettings`

    Specifies the method setting properties.

    - **metricsEnabled** *(boolean) --*

      Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
      for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
      Boolean.

    - **loggingLevel** *(string) --*

      Specifies the logging level for this method, which affects the log entries pushed to
      Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
      ``ERROR`` , and ``INFO`` .

    - **dataTraceEnabled** *(boolean) --*

      Specifies whether data trace logging is enabled for this method, which affects the log
      entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
      ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

    - **throttlingBurstLimit** *(integer) --*

      Specifies the throttling burst limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

    - **throttlingRateLimit** *(float) --*

      Specifies the throttling rate limit. The PATCH path for this setting is
      ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

    - **cachingEnabled** *(boolean) --*

      Specifies whether responses should be cached and returned for requests. A cache cluster
      must be enabled on the stage for responses to be cached. The PATCH path for this
      setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

    - **cacheTtlInSeconds** *(integer) --*

      Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
      the longer the response will be cached. The PATCH path for this setting is
      ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

    - **cacheDataEncrypted** *(boolean) --*

      Specifies whether the cached responses are encrypted. The PATCH path for this setting
      is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

    - **requireAuthorizationForCacheControl** *(boolean) --*

      Specifies whether authorization is required for a cache invalidation request. The PATCH
      path for this setting is
      ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
      is a Boolean.

    - **unauthorizedCacheControlHeaderStrategy** *(string) --*

      Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
      for this setting is
      ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
      available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
      ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .
    """


_ClientUpdateStageResponseTypeDef = TypedDict(
    "_ClientUpdateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": str,
        "cacheClusterStatus": str,
        "methodSettings": Dict[str, ClientUpdateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientUpdateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientUpdateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientUpdateStageResponseTypeDef(_ClientUpdateStageResponseTypeDef):
    """
    Type definition for `ClientUpdateStage` `Response`

    Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

      `Deploy an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__

    - **deploymentId** *(string) --*

      The identifier of the  Deployment that the stage points to.

    - **clientCertificateId** *(string) --*

      The identifier of a client certificate for an API stage.

    - **stageName** *(string) --*

      The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a
      call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and
      underscores. Maximum length is 128 characters.

    - **description** *(string) --*

      The stage's description.

    - **cacheClusterEnabled** *(boolean) --*

      Specifies whether a cache cluster is enabled for the stage.

    - **cacheClusterSize** *(string) --*

      The size of the cache cluster for the stage, if enabled.

    - **cacheClusterStatus** *(string) --*

      The status of the cache cluster for the stage, if enabled.

    - **methodSettings** *(dict) --*

      A map that defines the method settings for a  Stage resource. Keys (designated as
      ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}``
      for an individual method override, or ``/\\*/\\*`` for overriding all methods in the stage.

      - *(string) --*

        - *(dict) --*

          Specifies the method setting properties.

          - **metricsEnabled** *(boolean) --*

            Specifies whether Amazon CloudWatch metrics are enabled for this method. The PATCH path
            for this setting is ``/{method_setting_key}/metrics/enabled`` , and the value is a
            Boolean.

          - **loggingLevel** *(string) --*

            Specifies the logging level for this method, which affects the log entries pushed to
            Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/loglevel`` , and the available levels are ``OFF`` ,
            ``ERROR`` , and ``INFO`` .

          - **dataTraceEnabled** *(boolean) --*

            Specifies whether data trace logging is enabled for this method, which affects the log
            entries pushed to Amazon CloudWatch Logs. The PATCH path for this setting is
            ``/{method_setting_key}/logging/dataTrace`` , and the value is a Boolean.

          - **throttlingBurstLimit** *(integer) --*

            Specifies the throttling burst limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/burstLimit`` , and the value is an integer.

          - **throttlingRateLimit** *(float) --*

            Specifies the throttling rate limit. The PATCH path for this setting is
            ``/{method_setting_key}/throttling/rateLimit`` , and the value is a double.

          - **cachingEnabled** *(boolean) --*

            Specifies whether responses should be cached and returned for requests. A cache cluster
            must be enabled on the stage for responses to be cached. The PATCH path for this
            setting is ``/{method_setting_key}/caching/enabled`` , and the value is a Boolean.

          - **cacheTtlInSeconds** *(integer) --*

            Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL,
            the longer the response will be cached. The PATCH path for this setting is
            ``/{method_setting_key}/caching/ttlInSeconds`` , and the value is an integer.

          - **cacheDataEncrypted** *(boolean) --*

            Specifies whether the cached responses are encrypted. The PATCH path for this setting
            is ``/{method_setting_key}/caching/dataEncrypted`` , and the value is a Boolean.

          - **requireAuthorizationForCacheControl** *(boolean) --*

            Specifies whether authorization is required for a cache invalidation request. The PATCH
            path for this setting is
            ``/{method_setting_key}/caching/requireAuthorizationForCacheControl`` , and the value
            is a Boolean.

          - **unauthorizedCacheControlHeaderStrategy** *(string) --*

            Specifies how to handle unauthorized requests for cache invalidation. The PATCH path
            for this setting is
            ``/{method_setting_key}/caching/unauthorizedCacheControlHeaderStrategy`` , and the
            available values are ``FAIL_WITH_403`` , ``SUCCEED_WITH_RESPONSE_HEADER`` ,
            ``SUCCEED_WITHOUT_RESPONSE_HEADER`` .

    - **variables** *(dict) --*

      A map that defines the stage variables for a  Stage resource. Variable names can have
      alphanumeric and underscore characters, and the values must match ``[A-Za-z0-9-._~:/?#&=,]+``
      .

      - *(string) --*

        - *(string) --*

    - **documentationVersion** *(string) --*

      The version of the associated API documentation.

    - **accessLogSettings** *(dict) --*

      Settings for logging access in this stage.

      - **format** *(string) --*

        A single line format of the access logs of data, as specified by selected `$context
        variables
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#context-variable-reference>`__
        . The format must include at least ``$context.requestId`` .

      - **destinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.

    - **canarySettings** *(dict) --*

      Settings for the canary deployment in this stage.

      - **percentTraffic** *(float) --*

        The percent (0-100) of traffic diverted to a canary deployment.

      - **deploymentId** *(string) --*

        The ID of the canary deployment.

      - **stageVariableOverrides** *(dict) --*

        Stage variables overridden for a canary release deployment, including new stage variables
        introduced in the canary. These stage variables are represented as a string-to-string map
        between stage variable names and their values.

        - *(string) --*

          - *(string) --*

      - **useStageCache** *(boolean) --*

        A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

    - **tracingEnabled** *(boolean) --*

      Specifies whether active tracing with X-ray is enabled for the  Stage .

    - **webAclArn** *(string) --*

      The ARN of the WebAcl associated with the  Stage .

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*

    - **createdDate** *(datetime) --*

      The timestamp when the stage was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the stage last updated.
    """


_ClientUpdateVpcLinkResponseTypeDef = TypedDict(
    "_ClientUpdateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": str,
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateVpcLinkResponseTypeDef(_ClientUpdateVpcLinkResponseTypeDef):
    """
    Type definition for `ClientUpdateVpcLink` `Response`

    A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
    (VPC).

    To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
    you, as an API developer, create a  VpcLink resource targeted for one or more network load
    balancers of the VPC and then integrate an API method with a private integration that uses the
    VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and has
    a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
    identify the  VpcLink used.

    - **id** *(string) --*

      The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .

    - **name** *(string) --*

      The name used to label and identify the VPC link.

    - **description** *(string) --*

      The description of the VPC link.

    - **targetArns** *(list) --*

      The ARNs of network load balancers of the VPC targeted by the VPC link. The network load
      balancers must be owned by the same AWS account of the API owner.

      - *(string) --*

    - **status** *(string) --*

      The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` , ``DELETING`` ,
      or ``FAILED`` . Deploying an API will wait if the status is ``PENDING`` and will fail if the
      status is ``DELETING`` .

    - **statusMessage** *(string) --*

      A description about the VPC link status.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_GetApiKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetApiKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetApiKeysPaginatePaginationConfigTypeDef(
    _GetApiKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetApiKeysPaginate` `PaginationConfig`

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


_GetApiKeysPaginateResponseitemsTypeDef = TypedDict(
    "_GetApiKeysPaginateResponseitemsTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class GetApiKeysPaginateResponseitemsTypeDef(_GetApiKeysPaginateResponseitemsTypeDef):
    """
    Type definition for `GetApiKeysPaginateResponse` `items`

    A resource that can be distributed to callers for executing  Method resources that require
    an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
    callers with the API key can make requests to that stage.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **id** *(string) --*

      The identifier of the API Key.

    - **value** *(string) --*

      The value of the API Key.

    - **name** *(string) --*

      The name of the API Key.

    - **customerId** *(string) --*

      An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    - **description** *(string) --*

      The description of the API Key.

    - **enabled** *(boolean) --*

      Specifies whether the API Key can be used by callers.

    - **createdDate** *(datetime) --*

      The timestamp when the API Key was created.

    - **lastUpdatedDate** *(datetime) --*

      The timestamp when the API Key was last updated.

    - **stageKeys** *(list) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

      - *(string) --*

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_GetApiKeysPaginateResponseTypeDef = TypedDict(
    "_GetApiKeysPaginateResponseTypeDef",
    {
        "warnings": List[str],
        "items": List[GetApiKeysPaginateResponseitemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetApiKeysPaginateResponseTypeDef(_GetApiKeysPaginateResponseTypeDef):
    """
    Type definition for `GetApiKeysPaginate` `Response`

    Represents a collection of API keys as represented by an  ApiKeys resource.

      `Use API Keys
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

    - **warnings** *(list) --*

      A list of warning messages logged during the import of API keys when the ``failOnWarnings``
      option is set to true.

      - *(string) --*

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A resource that can be distributed to callers for executing  Method resources that require
        an API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
        callers with the API key can make requests to that stage.

          `Use API Keys
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

        - **id** *(string) --*

          The identifier of the API Key.

        - **value** *(string) --*

          The value of the API Key.

        - **name** *(string) --*

          The name of the API Key.

        - **customerId** *(string) --*

          An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

        - **description** *(string) --*

          The description of the API Key.

        - **enabled** *(boolean) --*

          Specifies whether the API Key can be used by callers.

        - **createdDate** *(datetime) --*

          The timestamp when the API Key was created.

        - **lastUpdatedDate** *(datetime) --*

          The timestamp when the API Key was last updated.

        - **stageKeys** *(list) --*

          A list of  Stage resources that are associated with the  ApiKey resource.

          - *(string) --*

        - **tags** *(dict) --*

          The collection of tags. Each tag element is associated with a given resource.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_GetBasePathMappingsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBasePathMappingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBasePathMappingsPaginatePaginationConfigTypeDef(
    _GetBasePathMappingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBasePathMappingsPaginate` `PaginationConfig`

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


_GetClientCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetClientCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetClientCertificatesPaginatePaginationConfigTypeDef(
    _GetClientCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetClientCertificatesPaginate` `PaginationConfig`

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


_GetDeploymentsPaginateResponseitemsapiSummaryTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseitemsapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class GetDeploymentsPaginateResponseitemsapiSummaryTypeDef(
    _GetDeploymentsPaginateResponseitemsapiSummaryTypeDef
):
    """
    Type definition for `GetDeploymentsPaginateResponseitems` `apiSummary`

    Represents a summary of a  Method resource, given a particular date and time.

    - **authorizationType** *(string) --*

      The method's authorization type. Valid values are ``NONE`` for open access,
      ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
      authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

    - **apiKeyRequired** *(boolean) --*

      Specifies whether the method requires a valid  ApiKey .
    """


_GetDeploymentsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseitemsTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[
            str, Dict[str, GetDeploymentsPaginateResponseitemsapiSummaryTypeDef]
        ],
    },
    total=False,
)


class GetDeploymentsPaginateResponseitemsTypeDef(
    _GetDeploymentsPaginateResponseitemsTypeDef
):
    """
    Type definition for `GetDeploymentsPaginateResponse` `items`

    An immutable representation of a  RestApi resource that can be called by users using
    Stages . A deployment must be associated with a  Stage for it to be callable over the
    Internet.

     To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To
     view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the
     specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).
     RestApi ,  Deployments ,  Stage , `AWS CLI
     <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ ,
     `AWS SDKs <https://aws.amazon.com/tools/>`__

    - **id** *(string) --*

      The identifier for the deployment resource.

    - **description** *(string) --*

      The description for the deployment resource.

    - **createdDate** *(datetime) --*

      The date and time that the deployment resource was created.

    - **apiSummary** *(dict) --*

      A summary of the  RestApi at the date and time that the deployment resource was created.

      - *(string) --*

        - *(dict) --*

          - *(string) --*

            - *(dict) --*

              Represents a summary of a  Method resource, given a particular date and time.

              - **authorizationType** *(string) --*

                The method's authorization type. Valid values are ``NONE`` for open access,
                ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

              - **apiKeyRequired** *(boolean) --*

                Specifies whether the method requires a valid  ApiKey .
    """


_GetDeploymentsPaginateResponseTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseTypeDef",
    {"items": List[GetDeploymentsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetDeploymentsPaginateResponseTypeDef(_GetDeploymentsPaginateResponseTypeDef):
    """
    Type definition for `GetDeploymentsPaginate` `Response`

    Represents a collection resource that contains zero or more references to your existing
    deployments, and links that guide you on how to interact with your collection. The collection
    offers a paginated view of the contained deployments.

     To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To
     view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE``
     request, respectively, on a specified  Deployment resource.  `Deploying an API
     <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ ,
     `AWS CLI <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__
     , `AWS SDKs <https://aws.amazon.com/tools/>`__

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        An immutable representation of a  RestApi resource that can be called by users using
        Stages . A deployment must be associated with a  Stage for it to be callable over the
        Internet.

         To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To
         view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the
         specified deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).
         RestApi ,  Deployments ,  Stage , `AWS CLI
         <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ ,
         `AWS SDKs <https://aws.amazon.com/tools/>`__

        - **id** *(string) --*

          The identifier for the deployment resource.

        - **description** *(string) --*

          The description for the deployment resource.

        - **createdDate** *(datetime) --*

          The date and time that the deployment resource was created.

        - **apiSummary** *(dict) --*

          A summary of the  RestApi at the date and time that the deployment resource was created.

          - *(string) --*

            - *(dict) --*

              - *(string) --*

                - *(dict) --*

                  Represents a summary of a  Method resource, given a particular date and time.

                  - **authorizationType** *(string) --*

                    The method's authorization type. Valid values are ``NONE`` for open access,
                    ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                    authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                  - **apiKeyRequired** *(boolean) --*

                    Specifies whether the method requires a valid  ApiKey .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetDocumentationPartsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDocumentationPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDocumentationPartsPaginatePaginationConfigTypeDef(
    _GetDocumentationPartsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDocumentationPartsPaginate` `PaginationConfig`

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


_GetDocumentationPartsPaginateResponseitemslocationTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseitemslocationTypeDef",
    {"type": str, "path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class GetDocumentationPartsPaginateResponseitemslocationTypeDef(
    _GetDocumentationPartsPaginateResponseitemslocationTypeDef
):
    """
    Type definition for `GetDocumentationPartsPaginateResponseitems` `location`

    The location of the API entity to which the documentation applies. Valid fields depend on
    the targeted API entity type. All the valid location fields are not required. If not
    explicitly specified, a valid location field is treated as a wildcard and associated
    documentation content may be inherited by matching entities, unless overridden.

    - **type** *(string) --*

      [Required] The type of API entity to which the documentation content applies. Valid
      values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
      not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
      ``REQUEST_BODY`` , or ``RESOURCE`` type.

    - **path** *(string) --*

      The URL path of the target. It is a valid field for the API entity types of
      ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
      ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
      applicable child entity inherits the content of another entity of the same type with
      more general specifications of the other ``location`` attributes, the child entity's
      ``path`` attribute must match that of the parent entity as a prefix.

    - **method** *(string) --*

      The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
      for any method. When an applicable child entity inherits the content of an entity of
      the same type with more general specifications of the other ``location`` attributes,
      the child entity's ``method`` attribute must match that of the parent entity exactly.

    - **statusCode** *(string) --*

      The HTTP status code of a response. It is a valid field for the API entity types of
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
      for any status code. When an applicable child entity inherits the content of an entity
      of the same type with more general specifications of the other ``location`` attributes,
      the child entity's ``statusCode`` attribute must match that of the parent entity
      exactly.

    - **name** *(string) --*

      The name of the targeted API entity. It is a valid and required field for the API
      entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
      ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
      for any other entity type.
    """


_GetDocumentationPartsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseitemsTypeDef",
    {
        "id": str,
        "location": GetDocumentationPartsPaginateResponseitemslocationTypeDef,
        "properties": str,
    },
    total=False,
)


class GetDocumentationPartsPaginateResponseitemsTypeDef(
    _GetDocumentationPartsPaginateResponseitemsTypeDef
):
    """
    Type definition for `GetDocumentationPartsPaginateResponse` `items`

    A documentation part for a targeted API entity.

    A documentation part consists of a content map (``properties`` ) and a target (``location``
    ). The target specifies an API entity to which the documentation content applies. The
    supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` ,
    ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
    ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid
    ``location`` fields depend on the API entity type. All valid fields are not required.

    The content map is a JSON string of API-specific key-value pairs. Although an API can use
    any shape for the content map, only the OpenAPI-compliant documentation fields will be
    injected into the associated API entity definition in the exported OpenAPI definition file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationParts

    - **id** *(string) --*

      The  DocumentationPart identifier, generated by API Gateway when the
      ``DocumentationPart`` is created.

    - **location** *(dict) --*

      The location of the API entity to which the documentation applies. Valid fields depend on
      the targeted API entity type. All the valid location fields are not required. If not
      explicitly specified, a valid location field is treated as a wildcard and associated
      documentation content may be inherited by matching entities, unless overridden.

      - **type** *(string) --*

        [Required] The type of API entity to which the documentation content applies. Valid
        values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
        not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
        ``REQUEST_BODY`` , or ``RESOURCE`` type.

      - **path** *(string) --*

        The URL path of the target. It is a valid field for the API entity types of
        ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
        ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
        applicable child entity inherits the content of another entity of the same type with
        more general specifications of the other ``location`` attributes, the child entity's
        ``path`` attribute must match that of the parent entity as a prefix.

      - **method** *(string) --*

        The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
        ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
        for any method. When an applicable child entity inherits the content of an entity of
        the same type with more general specifications of the other ``location`` attributes,
        the child entity's ``method`` attribute must match that of the parent entity exactly.

      - **statusCode** *(string) --*

        The HTTP status code of a response. It is a valid field for the API entity types of
        ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
        for any status code. When an applicable child entity inherits the content of an entity
        of the same type with more general specifications of the other ``location`` attributes,
        the child entity's ``statusCode`` attribute must match that of the parent entity
        exactly.

      - **name** *(string) --*

        The name of the targeted API entity. It is a valid and required field for the API
        entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
        ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
        for any other entity type.

    - **properties** *(string) --*

      A content map of API-specific key-value pairs describing the targeted API entity. The map
      must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\"
      }"`` . Only OpenAPI-compliant documentation-related fields from the propertiesmap are
      exported and, hence, published as part of the API entity definitions, while the original
      documentation parts are exported in a OpenAPI extension of
      ``x-amazon-apigateway-documentation`` .
    """


_GetDocumentationPartsPaginateResponseTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseTypeDef",
    {
        "items": List[GetDocumentationPartsPaginateResponseitemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetDocumentationPartsPaginateResponseTypeDef(
    _GetDocumentationPartsPaginateResponseTypeDef
):
    """
    Type definition for `GetDocumentationPartsPaginate` `Response`

    The collection of documentation parts of an API.

       `Documenting an API
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
       ,  DocumentationPart

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A documentation part for a targeted API entity.

        A documentation part consists of a content map (``properties`` ) and a target (``location``
        ). The target specifies an API entity to which the documentation content applies. The
        supported API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` ,
        ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
        ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid
        ``location`` fields depend on the API entity type. All valid fields are not required.

        The content map is a JSON string of API-specific key-value pairs. Although an API can use
        any shape for the content map, only the OpenAPI-compliant documentation fields will be
        injected into the associated API entity definition in the exported OpenAPI definition file.

          `Documenting an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
          ,  DocumentationParts

        - **id** *(string) --*

          The  DocumentationPart identifier, generated by API Gateway when the
          ``DocumentationPart`` is created.

        - **location** *(dict) --*

          The location of the API entity to which the documentation applies. Valid fields depend on
          the targeted API entity type. All the valid location fields are not required. If not
          explicitly specified, a valid location field is treated as a wildcard and associated
          documentation content may be inherited by matching entities, unless overridden.

          - **type** *(string) --*

            [Required] The type of API entity to which the documentation content applies. Valid
            values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
            ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does
            not apply to any entity of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` ,
            ``REQUEST_BODY`` , or ``RESOURCE`` type.

          - **path** *(string) --*

            The URL path of the target. It is a valid field for the API entity types of
            ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
            ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
            ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
            applicable child entity inherits the content of another entity of the same type with
            more general specifications of the other ``location`` attributes, the child entity's
            ``path`` attribute must match that of the parent entity as a prefix.

          - **method** *(string) --*

            The HTTP verb of a method. It is a valid field for the API entity types of ``METHOD`` ,
            ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
            for any method. When an applicable child entity inherits the content of an entity of
            the same type with more general specifications of the other ``location`` attributes,
            the child entity's ``method`` attribute must match that of the parent entity exactly.

          - **statusCode** *(string) --*

            The HTTP status code of a response. It is a valid field for the API entity types of
            ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default value is ``*``
            for any status code. When an applicable child entity inherits the content of an entity
            of the same type with more general specifications of the other ``location`` attributes,
            the child entity's ``statusCode`` attribute must match that of the parent entity
            exactly.

          - **name** *(string) --*

            The name of the targeted API entity. It is a valid and required field for the API
            entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
            ``REQUEST_HEADER`` , ``REQUEST_BODY`` and ``RESPONSE_HEADER`` . It is an invalid field
            for any other entity type.

        - **properties** *(string) --*

          A content map of API-specific key-value pairs describing the targeted API entity. The map
          must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API does ...\\"
          }"`` . Only OpenAPI-compliant documentation-related fields from the propertiesmap are
          exported and, hence, published as part of the API entity definitions, while the original
          documentation parts are exported in a OpenAPI extension of
          ``x-amazon-apigateway-documentation`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetDocumentationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDocumentationVersionsPaginatePaginationConfigTypeDef(
    _GetDocumentationVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetDocumentationVersionsPaginate` `PaginationConfig`

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


_GetDocumentationVersionsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginateResponseitemsTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class GetDocumentationVersionsPaginateResponseitemsTypeDef(
    _GetDocumentationVersionsPaginateResponseitemsTypeDef
):
    """
    Type definition for `GetDocumentationVersionsPaginateResponse` `items`

    A snapshot of the documentation of an API.

    Publishing API documentation involves creating a documentation version associated with an
    API stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersions

    - **version** *(string) --*

      The version identifier of the API documentation snapshot.

    - **createdDate** *(datetime) --*

      The date when the API documentation snapshot is created.

    - **description** *(string) --*

      The description of the API documentation snapshot.
    """


_GetDocumentationVersionsPaginateResponseTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginateResponseTypeDef",
    {
        "items": List[GetDocumentationVersionsPaginateResponseitemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetDocumentationVersionsPaginateResponseTypeDef(
    _GetDocumentationVersionsPaginateResponseTypeDef
):
    """
    Type definition for `GetDocumentationVersionsPaginate` `Response`

    The collection of documentation snapshots of an API.

    Use the  DocumentationVersions to manage documentation snapshots associated with various API
    stages.

      `Documenting an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
      ,  DocumentationPart ,  DocumentationVersion

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A snapshot of the documentation of an API.

        Publishing API documentation involves creating a documentation version associated with an
        API stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

          `Documenting an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
          ,  DocumentationPart ,  DocumentationVersions

        - **version** *(string) --*

          The version identifier of the API documentation snapshot.

        - **createdDate** *(datetime) --*

          The date when the API documentation snapshot is created.

        - **description** *(string) --*

          The description of the API documentation snapshot.

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_GetGatewayResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGatewayResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetGatewayResponsesPaginatePaginationConfigTypeDef(
    _GetGatewayResponsesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetGatewayResponsesPaginate` `PaginationConfig`

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


_GetModelsPaginateResponseitemsTypeDef = TypedDict(
    "_GetModelsPaginateResponseitemsTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class GetModelsPaginateResponseitemsTypeDef(_GetModelsPaginateResponseitemsTypeDef):
    """
    Type definition for `GetModelsPaginateResponse` `items`

    Represents the data structure of a method's request or response payload.

    A request model defines the data structure of the client-supplied request payload. A
    response model defines the data structure of the response payload returned by the back end.
    Although not required, models are useful for mapping payloads between the front end and
    back end.

    A model is used for generating an API's SDK, validating the input request body, and
    creating a skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **id** *(string) --*

      The identifier for the model resource.

    - **name** *(string) --*

      The name of the model. Must be an alphanumeric string.

    - **description** *(string) --*

      The description of the model.

    - **schema** *(string) --*

      The schema for the model. For ``application/json`` models, this should be `JSON schema
      draft 4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include
      "\\*/" characters in the description of any properties because such "\\*/" characters may
      be interpreted as the closing marker for comments in some languages, such as Java or
      JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

    - **contentType** *(string) --*

      The content-type for the model.
    """


_GetModelsPaginateResponseTypeDef = TypedDict(
    "_GetModelsPaginateResponseTypeDef",
    {"items": List[GetModelsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetModelsPaginateResponseTypeDef(_GetModelsPaginateResponseTypeDef):
    """
    Type definition for `GetModelsPaginate` `Response`

    Represents a collection of  Model resources.

       Method ,  MethodResponse , `Models and Mappings
       <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        Represents the data structure of a method's request or response payload.

        A request model defines the data structure of the client-supplied request payload. A
        response model defines the data structure of the response payload returned by the back end.
        Although not required, models are useful for mapping payloads between the front end and
        back end.

        A model is used for generating an API's SDK, validating the input request body, and
        creating a skeletal mapping template.

            Method ,  MethodResponse , `Models and Mappings
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

        - **id** *(string) --*

          The identifier for the model resource.

        - **name** *(string) --*

          The name of the model. Must be an alphanumeric string.

        - **description** *(string) --*

          The description of the model.

        - **schema** *(string) --*

          The schema for the model. For ``application/json`` models, this should be `JSON schema
          draft 4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do not include
          "\\*/" characters in the description of any properties because such "\\*/" characters may
          be interpreted as the closing marker for comments in some languages, such as Java or
          JavaScript, causing the installation of your API's SDK generated by API Gateway to fail.

        - **contentType** *(string) --*

          The content-type for the model.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetRequestValidatorsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRequestValidatorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRequestValidatorsPaginatePaginationConfigTypeDef(
    _GetRequestValidatorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetRequestValidatorsPaginate` `PaginationConfig`

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


_GetResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcesPaginatePaginationConfigTypeDef(
    _GetResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourcesPaginate` `PaginationConfig`

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


_GetRestApisPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRestApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRestApisPaginatePaginationConfigTypeDef(
    _GetRestApisPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetRestApisPaginate` `PaginationConfig`

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


_GetRestApisPaginateResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_GetRestApisPaginateResponseitemsendpointConfigurationTypeDef",
    {"types": List[str], "vpcEndpointIds": List[str]},
    total=False,
)


class GetRestApisPaginateResponseitemsendpointConfigurationTypeDef(
    _GetRestApisPaginateResponseitemsendpointConfigurationTypeDef
):
    """
    Type definition for `GetRestApisPaginateResponseitems` `endpointConfiguration`

    The endpoint configuration of this  RestApi showing the endpoint types of the API.

    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
      ). For an edge-optimized API and its custom domain name, the endpoint type is
      ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
      ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
        suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
        suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

    - **vpcEndpointIds** *(list) --*

      A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
      It is only supported for ``PRIVATE`` endpoint type.

      - *(string) --*
    """


_GetRestApisPaginateResponseitemsTypeDef = TypedDict(
    "_GetRestApisPaginateResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": str,
        "endpointConfiguration": GetRestApisPaginateResponseitemsendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetRestApisPaginateResponseitemsTypeDef(_GetRestApisPaginateResponseitemsTypeDef):
    """
    Type definition for `GetRestApisPaginateResponse` `items`

    Represents a REST API.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **id** *(string) --*

      The API's identifier. This identifier is unique across all of your APIs in API Gateway.

    - **name** *(string) --*

      The API's name.

    - **description** *(string) --*

      The API's description.

    - **createdDate** *(datetime) --*

      The timestamp when the API was created.

    - **version** *(string) --*

      A version identifier for the API.

    - **warnings** *(list) --*

      The warning messages reported when ``failonwarnings`` is turned on during API import.

      - *(string) --*

    - **binaryMediaTypes** *(list) --*

      The list of binary media types supported by the  RestApi . By default, the  RestApi
      supports only UTF-8-encoded text payloads.

      - *(string) --*

    - **minimumCompressionSize** *(integer) --*

      A nullable integer that is used to enable compression (with non-negative between 0 and
      10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API.
      When compression is enabled, compression or decompression is not applied on the payload
      if the payload size is smaller than this value. Setting it to zero allows compression for
      any payload size.

    - **apiKeySource** *(string) --*

      The source of the API key for metering requests according to a usage plan. Valid values
      are:

      * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

      * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom
      authorizer.

    - **endpointConfiguration** *(dict) --*

      The endpoint configuration of this  RestApi showing the endpoint types of the API.

      - **types** *(list) --*

        A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
        ). For an edge-optimized API and its custom domain name, the endpoint type is
        ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
        ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

        - *(string) --*

          The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
          suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
          suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

      - **vpcEndpointIds** *(list) --*

        A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
        It is only supported for ``PRIVATE`` endpoint type.

        - *(string) --*

    - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
    regardless of the caller and  Method configuration.

    - **tags** *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.

      - *(string) --*

        - *(string) --*
    """


_GetRestApisPaginateResponseTypeDef = TypedDict(
    "_GetRestApisPaginateResponseTypeDef",
    {"items": List[GetRestApisPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetRestApisPaginateResponseTypeDef(_GetRestApisPaginateResponseTypeDef):
    """
    Type definition for `GetRestApisPaginate` `Response`

    Contains references to your APIs and links that guide you in how to interact with your
    collection. A collection offers a paginated view of your APIs.

      `Create an API
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        Represents a REST API.

          `Create an API
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

        - **id** *(string) --*

          The API's identifier. This identifier is unique across all of your APIs in API Gateway.

        - **name** *(string) --*

          The API's name.

        - **description** *(string) --*

          The API's description.

        - **createdDate** *(datetime) --*

          The timestamp when the API was created.

        - **version** *(string) --*

          A version identifier for the API.

        - **warnings** *(list) --*

          The warning messages reported when ``failonwarnings`` is turned on during API import.

          - *(string) --*

        - **binaryMediaTypes** *(list) --*

          The list of binary media types supported by the  RestApi . By default, the  RestApi
          supports only UTF-8-encoded text payloads.

          - *(string) --*

        - **minimumCompressionSize** *(integer) --*

          A nullable integer that is used to enable compression (with non-negative between 0 and
          10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API.
          When compression is enabled, compression or decompression is not applied on the payload
          if the payload size is smaller than this value. Setting it to zero allows compression for
          any payload size.

        - **apiKeySource** *(string) --*

          The source of the API key for metering requests according to a usage plan. Valid values
          are:

          * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

          * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom
          authorizer.

        - **endpointConfiguration** *(dict) --*

          The endpoint configuration of this  RestApi showing the endpoint types of the API.

          - **types** *(list) --*

            A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName
            ). For an edge-optimized API and its custom domain name, the endpoint type is
            ``"EDGE"`` . For a regional API and its custom domain name, the endpoint type is
            ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

            - *(string) --*

              The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most
              suitable for mobile applications; ``REGIONAL`` for regional API endpoint setup, most
              suitable for calling from AWS Region; and ``PRIVATE`` for private APIs.

          - **vpcEndpointIds** *(list) --*

            A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53 ALIASes.
            It is only supported for ``PRIVATE`` endpoint type.

            - *(string) --*

        - **policy** *(string) --* A stringified JSON policy document that applies to this RestApi
        regardless of the caller and  Method configuration.

        - **tags** *(dict) --*

          The collection of tags. Each tag element is associated with a given resource.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetSdkTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSdkTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSdkTypesPaginatePaginationConfigTypeDef(
    _GetSdkTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSdkTypesPaginate` `PaginationConfig`

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


_GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef",
    {
        "name": str,
        "friendlyName": str,
        "description": str,
        "required": bool,
        "defaultValue": str,
    },
    total=False,
)


class GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef(
    _GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef
):
    """
    Type definition for `GetSdkTypesPaginateResponseitems` `configurationProperties`

    A configuration property of an SDK type.

    - **name** *(string) --*

      The name of a an  SdkType configuration property.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType configuration property.

    - **description** *(string) --*

      The description of an  SdkType configuration property.

    - **required** *(boolean) --*

      A boolean flag of an  SdkType configuration property to indicate if the associated
      SDK configuration property is required (``true`` ) or not (``false`` ).

    - **defaultValue** *(string) --*

      The default value of an  SdkType configuration property.
    """


_GetSdkTypesPaginateResponseitemsTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseitemsTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)


class GetSdkTypesPaginateResponseitemsTypeDef(_GetSdkTypesPaginateResponseitemsTypeDef):
    """
    Type definition for `GetSdkTypesPaginateResponse` `items`

    A type of SDK that API Gateway can generate.

    - **id** *(string) --*

      The identifier of an  SdkType instance.

    - **friendlyName** *(string) --*

      The user-friendly name of an  SdkType instance.

    - **description** *(string) --*

      The description of an  SdkType .

    - **configurationProperties** *(list) --*

      A list of configuration properties of an  SdkType .

      - *(dict) --*

        A configuration property of an SDK type.

        - **name** *(string) --*

          The name of a an  SdkType configuration property.

        - **friendlyName** *(string) --*

          The user-friendly name of an  SdkType configuration property.

        - **description** *(string) --*

          The description of an  SdkType configuration property.

        - **required** *(boolean) --*

          A boolean flag of an  SdkType configuration property to indicate if the associated
          SDK configuration property is required (``true`` ) or not (``false`` ).

        - **defaultValue** *(string) --*

          The default value of an  SdkType configuration property.
    """


_GetSdkTypesPaginateResponseTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseTypeDef",
    {"items": List[GetSdkTypesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetSdkTypesPaginateResponseTypeDef(_GetSdkTypesPaginateResponseTypeDef):
    """
    Type definition for `GetSdkTypesPaginate` `Response`

    The collection of  SdkType instances.

    - **items** *(list) --*

      The current page of elements from this collection.

      - *(dict) --*

        A type of SDK that API Gateway can generate.

        - **id** *(string) --*

          The identifier of an  SdkType instance.

        - **friendlyName** *(string) --*

          The user-friendly name of an  SdkType instance.

        - **description** *(string) --*

          The description of an  SdkType .

        - **configurationProperties** *(list) --*

          A list of configuration properties of an  SdkType .

          - *(dict) --*

            A configuration property of an SDK type.

            - **name** *(string) --*

              The name of a an  SdkType configuration property.

            - **friendlyName** *(string) --*

              The user-friendly name of an  SdkType configuration property.

            - **description** *(string) --*

              The description of an  SdkType configuration property.

            - **required** *(boolean) --*

              A boolean flag of an  SdkType configuration property to indicate if the associated
              SDK configuration property is required (``true`` ) or not (``false`` ).

            - **defaultValue** *(string) --*

              The default value of an  SdkType configuration property.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetUsagePaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePaginatePaginationConfigTypeDef(_GetUsagePaginatePaginationConfigTypeDef):
    """
    Type definition for `GetUsagePaginate` `PaginationConfig`

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


_GetUsagePlanKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePlanKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePlanKeysPaginatePaginationConfigTypeDef(
    _GetUsagePlanKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetUsagePlanKeysPaginate` `PaginationConfig`

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


_GetUsagePlansPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePlansPaginatePaginationConfigTypeDef(
    _GetUsagePlansPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetUsagePlansPaginate` `PaginationConfig`

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


_GetVpcLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_GetVpcLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetVpcLinksPaginatePaginationConfigTypeDef(
    _GetVpcLinksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetVpcLinksPaginate` `PaginationConfig`

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
