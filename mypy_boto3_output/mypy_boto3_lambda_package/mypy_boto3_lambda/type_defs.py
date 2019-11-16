"Main interface for lambda type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddLayerVersionPermissionResponseTypeDef",
    "ClientAddPermissionResponseTypeDef",
    "ClientCreateAliasResponseRoutingConfigTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateAliasRoutingConfigTypeDef",
    "ClientCreateEventSourceMappingResponseTypeDef",
    "ClientCreateFunctionCodeTypeDef",
    "ClientCreateFunctionDeadLetterConfigTypeDef",
    "ClientCreateFunctionEnvironmentTypeDef",
    "ClientCreateFunctionResponseDeadLetterConfigTypeDef",
    "ClientCreateFunctionResponseEnvironmentErrorTypeDef",
    "ClientCreateFunctionResponseEnvironmentTypeDef",
    "ClientCreateFunctionResponseLayersTypeDef",
    "ClientCreateFunctionResponseTracingConfigTypeDef",
    "ClientCreateFunctionResponseVpcConfigTypeDef",
    "ClientCreateFunctionResponseTypeDef",
    "ClientCreateFunctionTracingConfigTypeDef",
    "ClientCreateFunctionVpcConfigTypeDef",
    "ClientDeleteEventSourceMappingResponseTypeDef",
    "ClientGetAccountSettingsResponseAccountLimitTypeDef",
    "ClientGetAccountSettingsResponseAccountUsageTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetAliasResponseRoutingConfigTypeDef",
    "ClientGetAliasResponseTypeDef",
    "ClientGetEventSourceMappingResponseTypeDef",
    "ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef",
    "ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef",
    "ClientGetFunctionConfigurationResponseEnvironmentTypeDef",
    "ClientGetFunctionConfigurationResponseLayersTypeDef",
    "ClientGetFunctionConfigurationResponseTracingConfigTypeDef",
    "ClientGetFunctionConfigurationResponseVpcConfigTypeDef",
    "ClientGetFunctionConfigurationResponseTypeDef",
    "ClientGetFunctionResponseCodeTypeDef",
    "ClientGetFunctionResponseConcurrencyTypeDef",
    "ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef",
    "ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef",
    "ClientGetFunctionResponseConfigurationEnvironmentTypeDef",
    "ClientGetFunctionResponseConfigurationLayersTypeDef",
    "ClientGetFunctionResponseConfigurationTracingConfigTypeDef",
    "ClientGetFunctionResponseConfigurationVpcConfigTypeDef",
    "ClientGetFunctionResponseConfigurationTypeDef",
    "ClientGetFunctionResponseTypeDef",
    "ClientGetLayerVersionByArnResponseContentTypeDef",
    "ClientGetLayerVersionByArnResponseTypeDef",
    "ClientGetLayerVersionPolicyResponseTypeDef",
    "ClientGetLayerVersionResponseContentTypeDef",
    "ClientGetLayerVersionResponseTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientInvokeAsyncResponseTypeDef",
    "ClientInvokeResponseTypeDef",
    "ClientListAliasesResponseAliasesRoutingConfigTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef",
    "ClientListEventSourceMappingsResponseTypeDef",
    "ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef",
    "ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef",
    "ClientListFunctionsResponseFunctionsEnvironmentTypeDef",
    "ClientListFunctionsResponseFunctionsLayersTypeDef",
    "ClientListFunctionsResponseFunctionsTracingConfigTypeDef",
    "ClientListFunctionsResponseFunctionsVpcConfigTypeDef",
    "ClientListFunctionsResponseFunctionsTypeDef",
    "ClientListFunctionsResponseTypeDef",
    "ClientListLayerVersionsResponseLayerVersionsTypeDef",
    "ClientListLayerVersionsResponseTypeDef",
    "ClientListLayersResponseLayersLatestMatchingVersionTypeDef",
    "ClientListLayersResponseLayersTypeDef",
    "ClientListLayersResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef",
    "ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef",
    "ClientListVersionsByFunctionResponseVersionsLayersTypeDef",
    "ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsTypeDef",
    "ClientListVersionsByFunctionResponseTypeDef",
    "ClientPublishLayerVersionContentTypeDef",
    "ClientPublishLayerVersionResponseContentTypeDef",
    "ClientPublishLayerVersionResponseTypeDef",
    "ClientPublishVersionResponseDeadLetterConfigTypeDef",
    "ClientPublishVersionResponseEnvironmentErrorTypeDef",
    "ClientPublishVersionResponseEnvironmentTypeDef",
    "ClientPublishVersionResponseLayersTypeDef",
    "ClientPublishVersionResponseTracingConfigTypeDef",
    "ClientPublishVersionResponseVpcConfigTypeDef",
    "ClientPublishVersionResponseTypeDef",
    "ClientPutFunctionConcurrencyResponseTypeDef",
    "ClientUpdateAliasResponseRoutingConfigTypeDef",
    "ClientUpdateAliasResponseTypeDef",
    "ClientUpdateAliasRoutingConfigTypeDef",
    "ClientUpdateEventSourceMappingResponseTypeDef",
    "ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef",
    "ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef",
    "ClientUpdateFunctionCodeResponseEnvironmentTypeDef",
    "ClientUpdateFunctionCodeResponseLayersTypeDef",
    "ClientUpdateFunctionCodeResponseTracingConfigTypeDef",
    "ClientUpdateFunctionCodeResponseVpcConfigTypeDef",
    "ClientUpdateFunctionCodeResponseTypeDef",
    "ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef",
    "ClientUpdateFunctionConfigurationEnvironmentTypeDef",
    "ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef",
    "ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef",
    "ClientUpdateFunctionConfigurationResponseLayersTypeDef",
    "ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseTypeDef",
    "ClientUpdateFunctionConfigurationTracingConfigTypeDef",
    "ClientUpdateFunctionConfigurationVpcConfigTypeDef",
    "FunctionExistsWaitWaiterConfigTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesRoutingConfigTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListEventSourceMappingsPaginatePaginationConfigTypeDef",
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef",
    "ListEventSourceMappingsPaginateResponseTypeDef",
    "ListFunctionsPaginatePaginationConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef",
    "ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef",
    "ListFunctionsPaginateResponseFunctionsLayersTypeDef",
    "ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsTypeDef",
    "ListFunctionsPaginateResponseTypeDef",
    "ListLayerVersionsPaginatePaginationConfigTypeDef",
    "ListLayerVersionsPaginateResponseLayerVersionsTypeDef",
    "ListLayerVersionsPaginateResponseTypeDef",
    "ListLayersPaginatePaginationConfigTypeDef",
    "ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef",
    "ListLayersPaginateResponseLayersTypeDef",
    "ListLayersPaginateResponseTypeDef",
    "ListVersionsByFunctionPaginatePaginationConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsTypeDef",
    "ListVersionsByFunctionPaginateResponseTypeDef",
)


_ClientAddLayerVersionPermissionResponseTypeDef = TypedDict(
    "_ClientAddLayerVersionPermissionResponseTypeDef",
    {"Statement": str, "RevisionId": str},
    total=False,
)


class ClientAddLayerVersionPermissionResponseTypeDef(
    _ClientAddLayerVersionPermissionResponseTypeDef
):
    """
    Type definition for `ClientAddLayerVersionPermission` `Response`

    - **Statement** *(string) --*

      The permission statement.

    - **RevisionId** *(string) --*

      A unique identifier for the current revision of the policy.
    """


_ClientAddPermissionResponseTypeDef = TypedDict(
    "_ClientAddPermissionResponseTypeDef", {"Statement": str}, total=False
)


class ClientAddPermissionResponseTypeDef(_ClientAddPermissionResponseTypeDef):
    """
    Type definition for `ClientAddPermission` `Response`

    - **Statement** *(string) --*

      The permission statement that's added to the function policy.
    """


_ClientCreateAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientCreateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientCreateAliasResponseRoutingConfigTypeDef(
    _ClientCreateAliasResponseRoutingConfigTypeDef
):
    """
    Type definition for `ClientCreateAliasResponse` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
    of the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientCreateAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    Type definition for `ClientCreateAlias` `Response`

    Provides configuration information about a Lambda function `alias
    <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

    - **AliasArn** *(string) --*

      The Amazon Resource Name (ARN) of the alias.

    - **Name** *(string) --*

      The name of the alias.

    - **FunctionVersion** *(string) --*

      The function version that the alias invokes.

    - **Description** *(string) --*

      A description of the alias.

    - **RoutingConfig** *(dict) --*

      The `routing configuration
      <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
      of the alias.

      - **AdditionalVersionWeights** *(dict) --*

        The name of the second alias, and the percentage of traffic that's routed to it.

        - *(string) --*

          - *(float) --*

    - **RevisionId** *(string) --*

      A unique identifier that changes when you update the alias.
    """


_ClientCreateAliasRoutingConfigTypeDef = TypedDict(
    "_ClientCreateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientCreateAliasRoutingConfigTypeDef(_ClientCreateAliasRoutingConfigTypeDef):
    """
    Type definition for `ClientCreateAlias` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ of
    the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientCreateEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ClientCreateEventSourceMappingResponseTypeDef(
    _ClientCreateEventSourceMappingResponseTypeDef
):
    """
    Type definition for `ClientCreateEventSourceMapping` `Response`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for
    details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientCreateFunctionCodeTypeDef = TypedDict(
    "_ClientCreateFunctionCodeTypeDef",
    {"ZipFile": bytes, "S3Bucket": str, "S3Key": str, "S3ObjectVersion": str},
    total=False,
)


class ClientCreateFunctionCodeTypeDef(_ClientCreateFunctionCodeTypeDef):
    """
    Type definition for `ClientCreateFunction` `Code`

    The code for the function.

    - **ZipFile** *(bytes) --*

      The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the
      encoding for you.

    - **S3Bucket** *(string) --*

      An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different
      AWS account.

    - **S3Key** *(string) --*

      The Amazon S3 key of the deployment package.

    - **S3ObjectVersion** *(string) --*

      For versioned objects, the version of the deployment package object to use.
    """


_ClientCreateFunctionDeadLetterConfigTypeDef = TypedDict(
    "_ClientCreateFunctionDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientCreateFunctionDeadLetterConfigTypeDef(
    _ClientCreateFunctionDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientCreateFunction` `DeadLetterConfig`

    A dead letter queue configuration that specifies the queue or topic where Lambda sends
    asynchronous events when they fail processing. For more information, see `Dead Letter Queues
    <https://docs.aws.amazon.com/lambda/latest/dg/dlq.html>`__ .

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientCreateFunctionEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionEnvironmentTypeDef",
    {"Variables": Dict[str, str]},
    total=False,
)


class ClientCreateFunctionEnvironmentTypeDef(_ClientCreateFunctionEnvironmentTypeDef):
    """
    Type definition for `ClientCreateFunction` `Environment`

    Environment variables that are accessible from function code during execution.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateFunctionResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientCreateFunctionResponseDeadLetterConfigTypeDef(
    _ClientCreateFunctionResponseDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponse` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientCreateFunctionResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientCreateFunctionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientCreateFunctionResponseEnvironmentErrorTypeDef(
    _ClientCreateFunctionResponseEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponseEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientCreateFunctionResponseEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientCreateFunctionResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientCreateFunctionResponseEnvironmentTypeDef(
    _ClientCreateFunctionResponseEnvironmentTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponse` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientCreateFunctionResponseLayersTypeDef = TypedDict(
    "_ClientCreateFunctionResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientCreateFunctionResponseLayersTypeDef(
    _ClientCreateFunctionResponseLayersTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponse` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientCreateFunctionResponseTracingConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseTracingConfigTypeDef", {"Mode": str}, total=False
)


class ClientCreateFunctionResponseTracingConfigTypeDef(
    _ClientCreateFunctionResponseTracingConfigTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponse` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientCreateFunctionResponseVpcConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientCreateFunctionResponseVpcConfigTypeDef(
    _ClientCreateFunctionResponseVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateFunctionResponse` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientCreateFunctionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientCreateFunctionResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientCreateFunctionResponseDeadLetterConfigTypeDef,
        "Environment": ClientCreateFunctionResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientCreateFunctionResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientCreateFunctionResponseLayersTypeDef],
    },
    total=False,
)


class ClientCreateFunctionResponseTypeDef(_ClientCreateFunctionResponseTypeDef):
    """
    Type definition for `ClientCreateFunction` `Response`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientCreateFunctionTracingConfigTypeDef = TypedDict(
    "_ClientCreateFunctionTracingConfigTypeDef", {"Mode": str}, total=False
)


class ClientCreateFunctionTracingConfigTypeDef(
    _ClientCreateFunctionTracingConfigTypeDef
):
    """
    Type definition for `ClientCreateFunction` `TracingConfig`

    Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientCreateFunctionVpcConfigTypeDef = TypedDict(
    "_ClientCreateFunctionVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFunctionVpcConfigTypeDef(_ClientCreateFunctionVpcConfigTypeDef):
    """
    Type definition for `ClientCreateFunction` `VpcConfig`

    For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets
    in the VPC. When you connect a function to a VPC, it can only access resources and the internet
    through that VPC. For more information, see `VPC Settings
    <https://docs.aws.amazon.com/lambda/latest/dg/vpc.html>`__ .

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*
    """


_ClientDeleteEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientDeleteEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ClientDeleteEventSourceMappingResponseTypeDef(
    _ClientDeleteEventSourceMappingResponseTypeDef
):
    """
    Type definition for `ClientDeleteEventSourceMapping` `Response`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for
    details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientGetAccountSettingsResponseAccountLimitTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)


class ClientGetAccountSettingsResponseAccountLimitTypeDef(
    _ClientGetAccountSettingsResponseAccountLimitTypeDef
):
    """
    Type definition for `ClientGetAccountSettingsResponse` `AccountLimit`

    Limits that are related to concurrency and code storage.

    - **TotalCodeSize** *(integer) --*

      The amount of storage space that you can use for all deployment packages and layer archives.

    - **CodeSizeUnzipped** *(integer) --*

      The maximum size of your function's code and layers when they're extracted.

    - **CodeSizeZipped** *(integer) --*

      The maximum size of a deployment package when it's uploaded directly to AWS Lambda. Use
      Amazon S3 for larger files.

    - **ConcurrentExecutions** *(integer) --*

      The maximum number of simultaneous function executions.

    - **UnreservedConcurrentExecutions** *(integer) --*

      The maximum number of simultaneous function executions, minus the capacity that's reserved
      for individual functions with  PutFunctionConcurrency .
    """


_ClientGetAccountSettingsResponseAccountUsageTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountUsageTypeDef",
    {"TotalCodeSize": int, "FunctionCount": int},
    total=False,
)


class ClientGetAccountSettingsResponseAccountUsageTypeDef(
    _ClientGetAccountSettingsResponseAccountUsageTypeDef
):
    """
    Type definition for `ClientGetAccountSettingsResponse` `AccountUsage`

    The number of functions and amount of storage in use.

    - **TotalCodeSize** *(integer) --*

      The amount of storage space, in bytes, that's being used by deployment packages and layer
      archives.

    - **FunctionCount** *(integer) --*

      The number of Lambda functions.
    """


_ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseTypeDef",
    {
        "AccountLimit": ClientGetAccountSettingsResponseAccountLimitTypeDef,
        "AccountUsage": ClientGetAccountSettingsResponseAccountUsageTypeDef,
    },
    total=False,
)


class ClientGetAccountSettingsResponseTypeDef(_ClientGetAccountSettingsResponseTypeDef):
    """
    Type definition for `ClientGetAccountSettings` `Response`

    - **AccountLimit** *(dict) --*

      Limits that are related to concurrency and code storage.

      - **TotalCodeSize** *(integer) --*

        The amount of storage space that you can use for all deployment packages and layer archives.

      - **CodeSizeUnzipped** *(integer) --*

        The maximum size of your function's code and layers when they're extracted.

      - **CodeSizeZipped** *(integer) --*

        The maximum size of a deployment package when it's uploaded directly to AWS Lambda. Use
        Amazon S3 for larger files.

      - **ConcurrentExecutions** *(integer) --*

        The maximum number of simultaneous function executions.

      - **UnreservedConcurrentExecutions** *(integer) --*

        The maximum number of simultaneous function executions, minus the capacity that's reserved
        for individual functions with  PutFunctionConcurrency .

    - **AccountUsage** *(dict) --*

      The number of functions and amount of storage in use.

      - **TotalCodeSize** *(integer) --*

        The amount of storage space, in bytes, that's being used by deployment packages and layer
        archives.

      - **FunctionCount** *(integer) --*

        The number of Lambda functions.
    """


_ClientGetAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientGetAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientGetAliasResponseRoutingConfigTypeDef(
    _ClientGetAliasResponseRoutingConfigTypeDef
):
    """
    Type definition for `ClientGetAliasResponse` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
    of the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientGetAliasResponseTypeDef = TypedDict(
    "_ClientGetAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientGetAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)


class ClientGetAliasResponseTypeDef(_ClientGetAliasResponseTypeDef):
    """
    Type definition for `ClientGetAlias` `Response`

    Provides configuration information about a Lambda function `alias
    <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

    - **AliasArn** *(string) --*

      The Amazon Resource Name (ARN) of the alias.

    - **Name** *(string) --*

      The name of the alias.

    - **FunctionVersion** *(string) --*

      The function version that the alias invokes.

    - **Description** *(string) --*

      A description of the alias.

    - **RoutingConfig** *(dict) --*

      The `routing configuration
      <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
      of the alias.

      - **AdditionalVersionWeights** *(dict) --*

        The name of the second alias, and the percentage of traffic that's routed to it.

        - *(string) --*

          - *(float) --*

    - **RevisionId** *(string) --*

      A unique identifier that changes when you update the alias.
    """


_ClientGetEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientGetEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ClientGetEventSourceMappingResponseTypeDef(
    _ClientGetEventSourceMappingResponseTypeDef
):
    """
    Type definition for `ClientGetEventSourceMapping` `Response`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for
    details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef(
    _ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponse` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef(
    _ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponseEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientGetFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientGetFunctionConfigurationResponseEnvironmentTypeDef(
    _ClientGetFunctionConfigurationResponseEnvironmentTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponse` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientGetFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientGetFunctionConfigurationResponseLayersTypeDef(
    _ClientGetFunctionConfigurationResponseLayersTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponse` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientGetFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseTracingConfigTypeDef(
    _ClientGetFunctionConfigurationResponseTracingConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponse` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientGetFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseVpcConfigTypeDef(
    _ClientGetFunctionConfigurationResponseVpcConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionConfigurationResponse` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientGetFunctionConfigurationResponseTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientGetFunctionConfigurationResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef,
        "Environment": ClientGetFunctionConfigurationResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientGetFunctionConfigurationResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientGetFunctionConfigurationResponseLayersTypeDef],
    },
    total=False,
)


class ClientGetFunctionConfigurationResponseTypeDef(
    _ClientGetFunctionConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetFunctionConfiguration` `Response`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientGetFunctionResponseCodeTypeDef = TypedDict(
    "_ClientGetFunctionResponseCodeTypeDef",
    {"RepositoryType": str, "Location": str},
    total=False,
)


class ClientGetFunctionResponseCodeTypeDef(_ClientGetFunctionResponseCodeTypeDef):
    """
    Type definition for `ClientGetFunctionResponse` `Code`

    The deployment package of the function or version.

    - **RepositoryType** *(string) --*

      The service that's hosting the file.

    - **Location** *(string) --*

      A presigned URL that you can use to download the deployment package.
    """


_ClientGetFunctionResponseConcurrencyTypeDef = TypedDict(
    "_ClientGetFunctionResponseConcurrencyTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)


class ClientGetFunctionResponseConcurrencyTypeDef(
    _ClientGetFunctionResponseConcurrencyTypeDef
):
    """
    Type definition for `ClientGetFunctionResponse` `Concurrency`

    The function's `reserved concurrency
    <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .

    - **ReservedConcurrentExecutions** *(integer) --*

      The number of concurrent executions that are reserved for this function. For more
      information, see `Managing Concurrency
      <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
    """


_ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef(
    _ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfiguration` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef(
    _ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfigurationEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientGetFunctionResponseConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientGetFunctionResponseConfigurationEnvironmentTypeDef(
    _ClientGetFunctionResponseConfigurationEnvironmentTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfiguration` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientGetFunctionResponseConfigurationLayersTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientGetFunctionResponseConfigurationLayersTypeDef(
    _ClientGetFunctionResponseConfigurationLayersTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfiguration` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientGetFunctionResponseConfigurationTracingConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationTracingConfigTypeDef(
    _ClientGetFunctionResponseConfigurationTracingConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfiguration` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientGetFunctionResponseConfigurationVpcConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationVpcConfigTypeDef(
    _ClientGetFunctionResponseConfigurationVpcConfigTypeDef
):
    """
    Type definition for `ClientGetFunctionResponseConfiguration` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientGetFunctionResponseConfigurationTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientGetFunctionResponseConfigurationVpcConfigTypeDef,
        "DeadLetterConfig": ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef,
        "Environment": ClientGetFunctionResponseConfigurationEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientGetFunctionResponseConfigurationTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientGetFunctionResponseConfigurationLayersTypeDef],
    },
    total=False,
)


class ClientGetFunctionResponseConfigurationTypeDef(
    _ClientGetFunctionResponseConfigurationTypeDef
):
    """
    Type definition for `ClientGetFunctionResponse` `Configuration`

    The configuration of the function or version.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientGetFunctionResponseTypeDef = TypedDict(
    "_ClientGetFunctionResponseTypeDef",
    {
        "Configuration": ClientGetFunctionResponseConfigurationTypeDef,
        "Code": ClientGetFunctionResponseCodeTypeDef,
        "Tags": Dict[str, str],
        "Concurrency": ClientGetFunctionResponseConcurrencyTypeDef,
    },
    total=False,
)


class ClientGetFunctionResponseTypeDef(_ClientGetFunctionResponseTypeDef):
    """
    Type definition for `ClientGetFunction` `Response`

    - **Configuration** *(dict) --*

      The configuration of the function or version.

      - **FunctionName** *(string) --*

        The name of the function.

      - **FunctionArn** *(string) --*

        The function's Amazon Resource Name (ARN).

      - **Runtime** *(string) --*

        The runtime environment for the Lambda function.

      - **Role** *(string) --*

        The function's execution role.

      - **Handler** *(string) --*

        The function that Lambda calls to begin executing your function.

      - **CodeSize** *(integer) --*

        The size of the function's deployment package, in bytes.

      - **Description** *(string) --*

        The function's description.

      - **Timeout** *(integer) --*

        The amount of time that Lambda allows a function to run before stopping it.

      - **MemorySize** *(integer) --*

        The memory that's allocated to the function.

      - **LastModified** *(string) --*

        The date and time that the function was last updated, in `ISO-8601 format
        <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

      - **CodeSha256** *(string) --*

        The SHA256 hash of the function's deployment package.

      - **Version** *(string) --*

        The version of the Lambda function.

      - **VpcConfig** *(dict) --*

        The function's networking configuration.

        - **SubnetIds** *(list) --*

          A list of VPC subnet IDs.

          - *(string) --*

        - **SecurityGroupIds** *(list) --*

          A list of VPC security groups IDs.

          - *(string) --*

        - **VpcId** *(string) --*

          The ID of the VPC.

      - **DeadLetterConfig** *(dict) --*

        The function's dead letter queue.

        - **TargetArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

      - **Environment** *(dict) --*

        The function's environment variables.

        - **Variables** *(dict) --*

          Environment variable key-value pairs.

          - *(string) --*

            - *(string) --*

        - **Error** *(dict) --*

          Error messages for environment variables that couldn't be applied.

          - **ErrorCode** *(string) --*

            The error code.

          - **Message** *(string) --*

            The error message.

      - **KMSKeyArn** *(string) --*

        The KMS key that's used to encrypt the function's environment variables. This key is only
        returned if you've configured a customer-managed CMK.

      - **TracingConfig** *(dict) --*

        The function's AWS X-Ray tracing configuration.

        - **Mode** *(string) --*

          The tracing mode.

      - **MasterArn** *(string) --*

        For Lambda@Edge functions, the ARN of the master function.

      - **RevisionId** *(string) --*

        The latest updated revision of the function or alias.

      - **Layers** *(list) --*

        The function's `layers
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - *(dict) --*

          An `AWS Lambda layer
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the function layer.

          - **CodeSize** *(integer) --*

            The size of the layer archive in bytes.

    - **Code** *(dict) --*

      The deployment package of the function or version.

      - **RepositoryType** *(string) --*

        The service that's hosting the file.

      - **Location** *(string) --*

        A presigned URL that you can use to download the deployment package.

    - **Tags** *(dict) --*

      The function's `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ .

      - *(string) --*

        - *(string) --*

    - **Concurrency** *(dict) --*

      The function's `reserved concurrency
      <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .

      - **ReservedConcurrentExecutions** *(integer) --*

        The number of concurrent executions that are reserved for this function. For more
        information, see `Managing Concurrency
        <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
    """


_ClientGetLayerVersionByArnResponseContentTypeDef = TypedDict(
    "_ClientGetLayerVersionByArnResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientGetLayerVersionByArnResponseContentTypeDef(
    _ClientGetLayerVersionByArnResponseContentTypeDef
):
    """
    Type definition for `ClientGetLayerVersionByArnResponse` `Content`

    Details about the layer version.

    - **Location** *(string) --*

      A link to the layer archive in Amazon S3 that is valid for 10 minutes.

    - **CodeSha256** *(string) --*

      The SHA-256 hash of the layer archive.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientGetLayerVersionByArnResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionByArnResponseTypeDef",
    {
        "Content": ClientGetLayerVersionByArnResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ClientGetLayerVersionByArnResponseTypeDef(
    _ClientGetLayerVersionByArnResponseTypeDef
):
    """
    Type definition for `ClientGetLayerVersionByArn` `Response`

    - **Content** *(dict) --*

      Details about the layer version.

      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.

      - **CodeSha256** *(string) --*

        The SHA-256 hash of the layer archive.

      - **CodeSize** *(integer) --*

        The size of the layer archive in bytes.

    - **LayerArn** *(string) --*

      The ARN of the layer.

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the layer version was created, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **Version** *(integer) --*

      The version number.

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's software license.
    """


_ClientGetLayerVersionPolicyResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionPolicyResponseTypeDef",
    {"Policy": str, "RevisionId": str},
    total=False,
)


class ClientGetLayerVersionPolicyResponseTypeDef(
    _ClientGetLayerVersionPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetLayerVersionPolicy` `Response`

    - **Policy** *(string) --*

      The policy document.

    - **RevisionId** *(string) --*

      A unique identifier for the current revision of the policy.
    """


_ClientGetLayerVersionResponseContentTypeDef = TypedDict(
    "_ClientGetLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientGetLayerVersionResponseContentTypeDef(
    _ClientGetLayerVersionResponseContentTypeDef
):
    """
    Type definition for `ClientGetLayerVersionResponse` `Content`

    Details about the layer version.

    - **Location** *(string) --*

      A link to the layer archive in Amazon S3 that is valid for 10 minutes.

    - **CodeSha256** *(string) --*

      The SHA-256 hash of the layer archive.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientGetLayerVersionResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionResponseTypeDef",
    {
        "Content": ClientGetLayerVersionResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ClientGetLayerVersionResponseTypeDef(_ClientGetLayerVersionResponseTypeDef):
    """
    Type definition for `ClientGetLayerVersion` `Response`

    - **Content** *(dict) --*

      Details about the layer version.

      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.

      - **CodeSha256** *(string) --*

        The SHA-256 hash of the layer archive.

      - **CodeSize** *(integer) --*

        The size of the layer archive in bytes.

    - **LayerArn** *(string) --*

      The ARN of the layer.

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the layer version was created, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **Version** *(integer) --*

      The version number.

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's software license.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    Type definition for `ClientGetPolicy` `Response`

    - **Policy** *(string) --*

      The resource-based policy.

    - **RevisionId** *(string) --*

      A unique identifier for the current revision of the policy.
    """


_ClientInvokeAsyncResponseTypeDef = TypedDict(
    "_ClientInvokeAsyncResponseTypeDef", {"Status": int}, total=False
)


class ClientInvokeAsyncResponseTypeDef(_ClientInvokeAsyncResponseTypeDef):
    """
    Type definition for `ClientInvokeAsync` `Response`

    A success response (``202 Accepted`` ) indicates that the request is queued for invocation.

    - **Status** *(integer) --*

      The status code.
    """


_ClientInvokeResponseTypeDef = TypedDict(
    "_ClientInvokeResponseTypeDef",
    {"StatusCode": int, "FunctionError": str, "LogResult": str, "ExecutedVersion": str},
    total=False,
)


class ClientInvokeResponseTypeDef(_ClientInvokeResponseTypeDef):
    """
    Type definition for `ClientInvoke` `Response`

    - **StatusCode** *(integer) --*

      The HTTP status code is in the 200 range for a successful request. For the
      ``RequestResponse`` invocation type, this status code is 200. For the ``Event`` invocation
      type, this status code is 202. For the ``DryRun`` invocation type, the status code is 204.

    - **FunctionError** *(string) --*

      If present, indicates that an error occurred during function execution. Details about the
      error are included in the response payload.

      * ``Handled`` - The runtime caught an error thrown by the function and formatted it into a
      JSON document.

      * ``Unhandled`` - The runtime didn't handle the error. For example, the function ran out of
      memory or timed out.

    - **LogResult** *(string) --*

      The last 4 KB of the execution log, which is base64 encoded.

    - **Payload** (:class:`.StreamingBody`) --

      The response from the function, or an error object.

    - **ExecutedVersion** *(string) --*

      The version of the function that executed. When you invoke a function with an alias, this
      indicates which version the alias resolved to.
    """


_ClientListAliasesResponseAliasesRoutingConfigTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientListAliasesResponseAliasesRoutingConfigTypeDef(
    _ClientListAliasesResponseAliasesRoutingConfigTypeDef
):
    """
    Type definition for `ClientListAliasesResponseAliases` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
    of the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientListAliasesResponseAliasesRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    """
    Type definition for `ClientListAliasesResponse` `Aliases`

    Provides configuration information about a Lambda function `alias
    <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

    - **AliasArn** *(string) --*

      The Amazon Resource Name (ARN) of the alias.

    - **Name** *(string) --*

      The name of the alias.

    - **FunctionVersion** *(string) --*

      The function version that the alias invokes.

    - **Description** *(string) --*

      A description of the alias.

    - **RoutingConfig** *(dict) --*

      The `routing configuration
      <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
      of the alias.

      - **AdditionalVersionWeights** *(dict) --*

        The name of the second alias, and the percentage of traffic that's routed to it.

        - *(string) --*

          - *(float) --*

    - **RevisionId** *(string) --*

      A unique identifier that changes when you update the alias.
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {"NextMarker": str, "Aliases": List[ClientListAliasesResponseAliasesTypeDef]},
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    Type definition for `ClientListAliases` `Response`

    - **NextMarker** *(string) --*

      The pagination token that's included if more results are available.

    - **Aliases** *(list) --*

      A list of aliases.

      - *(dict) --*

        Provides configuration information about a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

        - **AliasArn** *(string) --*

          The Amazon Resource Name (ARN) of the alias.

        - **Name** *(string) --*

          The name of the alias.

        - **FunctionVersion** *(string) --*

          The function version that the alias invokes.

        - **Description** *(string) --*

          A description of the alias.

        - **RoutingConfig** *(dict) --*

          The `routing configuration
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
          of the alias.

          - **AdditionalVersionWeights** *(dict) --*

            The name of the second alias, and the percentage of traffic that's routed to it.

            - *(string) --*

              - *(float) --*

        - **RevisionId** *(string) --*

          A unique identifier that changes when you update the alias.
    """


_ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef(
    _ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef
):
    """
    Type definition for `ClientListEventSourceMappingsResponse` `EventSourceMappings`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
    for details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
      ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientListEventSourceMappingsResponseTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List[
            ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef
        ],
    },
    total=False,
)


class ClientListEventSourceMappingsResponseTypeDef(
    _ClientListEventSourceMappingsResponseTypeDef
):
    """
    Type definition for `ClientListEventSourceMappings` `Response`

    - **NextMarker** *(string) --*

      A pagination token that's returned when the response doesn't contain all event source
      mappings.

    - **EventSourceMappings** *(list) --*

      A list of event source mappings.

      - *(dict) --*

        A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
        for details.

        - **UUID** *(string) --*

          The identifier of the event source mapping.

        - **BatchSize** *(integer) --*

          The maximum number of items to retrieve in a single batch.

        - **MaximumBatchingWindowInSeconds** *(integer) --*

        - **EventSourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the event source.

        - **FunctionArn** *(string) --*

          The ARN of the Lambda function.

        - **LastModified** *(datetime) --*

          The date that the event source mapping was last updated.

        - **LastProcessingResult** *(string) --*

          The result of the last AWS Lambda invocation of your Lambda function.

        - **State** *(string) --*

          The state of the event source mapping. It can be one of the following: ``Creating`` ,
          ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
          ``Deleting`` .

        - **StateTransitionReason** *(string) --*

          The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef(
    _ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctions` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef(
    _ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctionsEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientListFunctionsResponseFunctionsEnvironmentTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientListFunctionsResponseFunctionsEnvironmentTypeDef(
    _ClientListFunctionsResponseFunctionsEnvironmentTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctions` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientListFunctionsResponseFunctionsLayersTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientListFunctionsResponseFunctionsLayersTypeDef(
    _ClientListFunctionsResponseFunctionsLayersTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctions` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientListFunctionsResponseFunctionsTracingConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsTracingConfigTypeDef(
    _ClientListFunctionsResponseFunctionsTracingConfigTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctions` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientListFunctionsResponseFunctionsVpcConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsVpcConfigTypeDef(
    _ClientListFunctionsResponseFunctionsVpcConfigTypeDef
):
    """
    Type definition for `ClientListFunctionsResponseFunctions` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientListFunctionsResponseFunctionsTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientListFunctionsResponseFunctionsVpcConfigTypeDef,
        "DeadLetterConfig": ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef,
        "Environment": ClientListFunctionsResponseFunctionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientListFunctionsResponseFunctionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientListFunctionsResponseFunctionsLayersTypeDef],
    },
    total=False,
)


class ClientListFunctionsResponseFunctionsTypeDef(
    _ClientListFunctionsResponseFunctionsTypeDef
):
    """
    Type definition for `ClientListFunctionsResponse` `Functions`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientListFunctionsResponseTypeDef = TypedDict(
    "_ClientListFunctionsResponseTypeDef",
    {"NextMarker": str, "Functions": List[ClientListFunctionsResponseFunctionsTypeDef]},
    total=False,
)


class ClientListFunctionsResponseTypeDef(_ClientListFunctionsResponseTypeDef):
    """
    Type definition for `ClientListFunctions` `Response`

    A list of Lambda functions.

    - **NextMarker** *(string) --*

      The pagination token that's included if more results are available.

    - **Functions** *(list) --*

      A list of Lambda functions.

      - *(dict) --*

        Details about a function's configuration.

        - **FunctionName** *(string) --*

          The name of the function.

        - **FunctionArn** *(string) --*

          The function's Amazon Resource Name (ARN).

        - **Runtime** *(string) --*

          The runtime environment for the Lambda function.

        - **Role** *(string) --*

          The function's execution role.

        - **Handler** *(string) --*

          The function that Lambda calls to begin executing your function.

        - **CodeSize** *(integer) --*

          The size of the function's deployment package, in bytes.

        - **Description** *(string) --*

          The function's description.

        - **Timeout** *(integer) --*

          The amount of time that Lambda allows a function to run before stopping it.

        - **MemorySize** *(integer) --*

          The memory that's allocated to the function.

        - **LastModified** *(string) --*

          The date and time that the function was last updated, in `ISO-8601 format
          <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

        - **CodeSha256** *(string) --*

          The SHA256 hash of the function's deployment package.

        - **Version** *(string) --*

          The version of the Lambda function.

        - **VpcConfig** *(dict) --*

          The function's networking configuration.

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

          - **VpcId** *(string) --*

            The ID of the VPC.

        - **DeadLetterConfig** *(dict) --*

          The function's dead letter queue.

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        - **Environment** *(dict) --*

          The function's environment variables.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

          - **Error** *(dict) --*

            Error messages for environment variables that couldn't be applied.

            - **ErrorCode** *(string) --*

              The error code.

            - **Message** *(string) --*

              The error message.

        - **KMSKeyArn** *(string) --*

          The KMS key that's used to encrypt the function's environment variables. This key is only
          returned if you've configured a customer-managed CMK.

        - **TracingConfig** *(dict) --*

          The function's AWS X-Ray tracing configuration.

          - **Mode** *(string) --*

            The tracing mode.

        - **MasterArn** *(string) --*

          For Lambda@Edge functions, the ARN of the master function.

        - **RevisionId** *(string) --*

          The latest updated revision of the function or alias.

        - **Layers** *(list) --*

          The function's `layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

          - *(dict) --*

            An `AWS Lambda layer
            <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the function layer.

            - **CodeSize** *(integer) --*

              The size of the layer archive in bytes.
    """


_ClientListLayerVersionsResponseLayerVersionsTypeDef = TypedDict(
    "_ClientListLayerVersionsResponseLayerVersionsTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ClientListLayerVersionsResponseLayerVersionsTypeDef(
    _ClientListLayerVersionsResponseLayerVersionsTypeDef
):
    """
    Type definition for `ClientListLayerVersionsResponse` `LayerVersions`

    Details about a version of an `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Version** *(integer) --*

      The version number.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the version was created, in ISO 8601 format. For example,
      ``2018-11-27T15:10:45.123+0000`` .

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's open-source license.
    """


_ClientListLayerVersionsResponseTypeDef = TypedDict(
    "_ClientListLayerVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "LayerVersions": List[ClientListLayerVersionsResponseLayerVersionsTypeDef],
    },
    total=False,
)


class ClientListLayerVersionsResponseTypeDef(_ClientListLayerVersionsResponseTypeDef):
    """
    Type definition for `ClientListLayerVersions` `Response`

    - **NextMarker** *(string) --*

      A pagination token returned when the response doesn't contain all versions.

    - **LayerVersions** *(list) --*

      A list of versions.

      - *(dict) --*

        Details about a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **LayerVersionArn** *(string) --*

          The ARN of the layer version.

        - **Version** *(integer) --*

          The version number.

        - **Description** *(string) --*

          The description of the version.

        - **CreatedDate** *(string) --*

          The date that the version was created, in ISO 8601 format. For example,
          ``2018-11-27T15:10:45.123+0000`` .

        - **CompatibleRuntimes** *(list) --*

          The layer's compatible runtimes.

          - *(string) --*

        - **LicenseInfo** *(string) --*

          The layer's open-source license.
    """


_ClientListLayersResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "_ClientListLayersResponseLayersLatestMatchingVersionTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ClientListLayersResponseLayersLatestMatchingVersionTypeDef(
    _ClientListLayersResponseLayersLatestMatchingVersionTypeDef
):
    """
    Type definition for `ClientListLayersResponseLayers` `LatestMatchingVersion`

    The newest version of the layer.

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Version** *(integer) --*

      The version number.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the version was created, in ISO 8601 format. For example,
      ``2018-11-27T15:10:45.123+0000`` .

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's open-source license.
    """


_ClientListLayersResponseLayersTypeDef = TypedDict(
    "_ClientListLayersResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ClientListLayersResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)


class ClientListLayersResponseLayersTypeDef(_ClientListLayersResponseLayersTypeDef):
    """
    Type definition for `ClientListLayersResponse` `Layers`

    Details about an `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **LayerName** *(string) --*

      The name of the layer.

    - **LayerArn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **LatestMatchingVersion** *(dict) --*

      The newest version of the layer.

      - **LayerVersionArn** *(string) --*

        The ARN of the layer version.

      - **Version** *(integer) --*

        The version number.

      - **Description** *(string) --*

        The description of the version.

      - **CreatedDate** *(string) --*

        The date that the version was created, in ISO 8601 format. For example,
        ``2018-11-27T15:10:45.123+0000`` .

      - **CompatibleRuntimes** *(list) --*

        The layer's compatible runtimes.

        - *(string) --*

      - **LicenseInfo** *(string) --*

        The layer's open-source license.
    """


_ClientListLayersResponseTypeDef = TypedDict(
    "_ClientListLayersResponseTypeDef",
    {"NextMarker": str, "Layers": List[ClientListLayersResponseLayersTypeDef]},
    total=False,
)


class ClientListLayersResponseTypeDef(_ClientListLayersResponseTypeDef):
    """
    Type definition for `ClientListLayers` `Response`

    - **NextMarker** *(string) --*

      A pagination token returned when the response doesn't contain all layers.

    - **Layers** *(list) --*

      A list of function layers.

      - *(dict) --*

        Details about an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **LayerName** *(string) --*

          The name of the layer.

        - **LayerArn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **LatestMatchingVersion** *(dict) --*

          The newest version of the layer.

          - **LayerVersionArn** *(string) --*

            The ARN of the layer version.

          - **Version** *(integer) --*

            The version number.

          - **Description** *(string) --*

            The description of the version.

          - **CreatedDate** *(string) --*

            The date that the version was created, in ISO 8601 format. For example,
            ``2018-11-27T15:10:45.123+0000`` .

          - **CompatibleRuntimes** *(list) --*

            The layer's compatible runtimes.

            - *(string) --*

          - **LicenseInfo** *(string) --*

            The layer's open-source license.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **Tags** *(dict) --*

      The function's tags.

      - *(string) --*

        - *(string) --*
    """


_ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersions` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef(
    _ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersionsEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef(
    _ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersions` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientListVersionsByFunctionResponseVersionsLayersTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsLayersTypeDef(
    _ClientListVersionsByFunctionResponseVersionsLayersTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersions` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersions` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponseVersions` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientListVersionsByFunctionResponseVersionsTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef,
        "DeadLetterConfig": ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef,
        "Environment": ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientListVersionsByFunctionResponseVersionsLayersTypeDef],
    },
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsTypeDef(
    _ClientListVersionsByFunctionResponseVersionsTypeDef
):
    """
    Type definition for `ClientListVersionsByFunctionResponse` `Versions`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientListVersionsByFunctionResponseTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List[ClientListVersionsByFunctionResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListVersionsByFunctionResponseTypeDef(
    _ClientListVersionsByFunctionResponseTypeDef
):
    """
    Type definition for `ClientListVersionsByFunction` `Response`

    - **NextMarker** *(string) --*

      The pagination token that's included if more results are available.

    - **Versions** *(list) --*

      A list of Lambda function versions.

      - *(dict) --*

        Details about a function's configuration.

        - **FunctionName** *(string) --*

          The name of the function.

        - **FunctionArn** *(string) --*

          The function's Amazon Resource Name (ARN).

        - **Runtime** *(string) --*

          The runtime environment for the Lambda function.

        - **Role** *(string) --*

          The function's execution role.

        - **Handler** *(string) --*

          The function that Lambda calls to begin executing your function.

        - **CodeSize** *(integer) --*

          The size of the function's deployment package, in bytes.

        - **Description** *(string) --*

          The function's description.

        - **Timeout** *(integer) --*

          The amount of time that Lambda allows a function to run before stopping it.

        - **MemorySize** *(integer) --*

          The memory that's allocated to the function.

        - **LastModified** *(string) --*

          The date and time that the function was last updated, in `ISO-8601 format
          <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

        - **CodeSha256** *(string) --*

          The SHA256 hash of the function's deployment package.

        - **Version** *(string) --*

          The version of the Lambda function.

        - **VpcConfig** *(dict) --*

          The function's networking configuration.

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

          - **VpcId** *(string) --*

            The ID of the VPC.

        - **DeadLetterConfig** *(dict) --*

          The function's dead letter queue.

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        - **Environment** *(dict) --*

          The function's environment variables.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

          - **Error** *(dict) --*

            Error messages for environment variables that couldn't be applied.

            - **ErrorCode** *(string) --*

              The error code.

            - **Message** *(string) --*

              The error message.

        - **KMSKeyArn** *(string) --*

          The KMS key that's used to encrypt the function's environment variables. This key is only
          returned if you've configured a customer-managed CMK.

        - **TracingConfig** *(dict) --*

          The function's AWS X-Ray tracing configuration.

          - **Mode** *(string) --*

            The tracing mode.

        - **MasterArn** *(string) --*

          For Lambda@Edge functions, the ARN of the master function.

        - **RevisionId** *(string) --*

          The latest updated revision of the function or alias.

        - **Layers** *(list) --*

          The function's `layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

          - *(dict) --*

            An `AWS Lambda layer
            <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the function layer.

            - **CodeSize** *(integer) --*

              The size of the layer archive in bytes.
    """


_ClientPublishLayerVersionContentTypeDef = TypedDict(
    "_ClientPublishLayerVersionContentTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": bytes},
    total=False,
)


class ClientPublishLayerVersionContentTypeDef(_ClientPublishLayerVersionContentTypeDef):
    """
    Type definition for `ClientPublishLayerVersion` `Content`

    The function layer archive.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket of the layer archive.

    - **S3Key** *(string) --*

      The Amazon S3 key of the layer archive.

    - **S3ObjectVersion** *(string) --*

      For versioned objects, the version of the layer archive object to use.

    - **ZipFile** *(bytes) --*

      The base64-encoded contents of the layer archive. AWS SDK and AWS CLI clients handle the
      encoding for you.
    """


_ClientPublishLayerVersionResponseContentTypeDef = TypedDict(
    "_ClientPublishLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientPublishLayerVersionResponseContentTypeDef(
    _ClientPublishLayerVersionResponseContentTypeDef
):
    """
    Type definition for `ClientPublishLayerVersionResponse` `Content`

    Details about the layer version.

    - **Location** *(string) --*

      A link to the layer archive in Amazon S3 that is valid for 10 minutes.

    - **CodeSha256** *(string) --*

      The SHA-256 hash of the layer archive.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientPublishLayerVersionResponseTypeDef = TypedDict(
    "_ClientPublishLayerVersionResponseTypeDef",
    {
        "Content": ClientPublishLayerVersionResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ClientPublishLayerVersionResponseTypeDef(
    _ClientPublishLayerVersionResponseTypeDef
):
    """
    Type definition for `ClientPublishLayerVersion` `Response`

    - **Content** *(dict) --*

      Details about the layer version.

      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.

      - **CodeSha256** *(string) --*

        The SHA-256 hash of the layer archive.

      - **CodeSize** *(integer) --*

        The size of the layer archive in bytes.

    - **LayerArn** *(string) --*

      The ARN of the layer.

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the layer version was created, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **Version** *(integer) --*

      The version number.

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's software license.
    """


_ClientPublishVersionResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientPublishVersionResponseDeadLetterConfigTypeDef(
    _ClientPublishVersionResponseDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientPublishVersionResponse` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientPublishVersionResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientPublishVersionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientPublishVersionResponseEnvironmentErrorTypeDef(
    _ClientPublishVersionResponseEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientPublishVersionResponseEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientPublishVersionResponseEnvironmentTypeDef = TypedDict(
    "_ClientPublishVersionResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientPublishVersionResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientPublishVersionResponseEnvironmentTypeDef(
    _ClientPublishVersionResponseEnvironmentTypeDef
):
    """
    Type definition for `ClientPublishVersionResponse` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientPublishVersionResponseLayersTypeDef = TypedDict(
    "_ClientPublishVersionResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientPublishVersionResponseLayersTypeDef(
    _ClientPublishVersionResponseLayersTypeDef
):
    """
    Type definition for `ClientPublishVersionResponse` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientPublishVersionResponseTracingConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseTracingConfigTypeDef", {"Mode": str}, total=False
)


class ClientPublishVersionResponseTracingConfigTypeDef(
    _ClientPublishVersionResponseTracingConfigTypeDef
):
    """
    Type definition for `ClientPublishVersionResponse` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientPublishVersionResponseVpcConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientPublishVersionResponseVpcConfigTypeDef(
    _ClientPublishVersionResponseVpcConfigTypeDef
):
    """
    Type definition for `ClientPublishVersionResponse` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientPublishVersionResponseTypeDef = TypedDict(
    "_ClientPublishVersionResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientPublishVersionResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientPublishVersionResponseDeadLetterConfigTypeDef,
        "Environment": ClientPublishVersionResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientPublishVersionResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientPublishVersionResponseLayersTypeDef],
    },
    total=False,
)


class ClientPublishVersionResponseTypeDef(_ClientPublishVersionResponseTypeDef):
    """
    Type definition for `ClientPublishVersion` `Response`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientPutFunctionConcurrencyResponseTypeDef = TypedDict(
    "_ClientPutFunctionConcurrencyResponseTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)


class ClientPutFunctionConcurrencyResponseTypeDef(
    _ClientPutFunctionConcurrencyResponseTypeDef
):
    """
    Type definition for `ClientPutFunctionConcurrency` `Response`

    - **ReservedConcurrentExecutions** *(integer) --*

      The number of concurrent executions that are reserved for this function. For more
      information, see `Managing Concurrency
      <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
    """


_ClientUpdateAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientUpdateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientUpdateAliasResponseRoutingConfigTypeDef(
    _ClientUpdateAliasResponseRoutingConfigTypeDef
):
    """
    Type definition for `ClientUpdateAliasResponse` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
    of the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientUpdateAliasResponseTypeDef = TypedDict(
    "_ClientUpdateAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientUpdateAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)


class ClientUpdateAliasResponseTypeDef(_ClientUpdateAliasResponseTypeDef):
    """
    Type definition for `ClientUpdateAlias` `Response`

    Provides configuration information about a Lambda function `alias
    <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

    - **AliasArn** *(string) --*

      The Amazon Resource Name (ARN) of the alias.

    - **Name** *(string) --*

      The name of the alias.

    - **FunctionVersion** *(string) --*

      The function version that the alias invokes.

    - **Description** *(string) --*

      A description of the alias.

    - **RoutingConfig** *(dict) --*

      The `routing configuration
      <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
      of the alias.

      - **AdditionalVersionWeights** *(dict) --*

        The name of the second alias, and the percentage of traffic that's routed to it.

        - *(string) --*

          - *(float) --*

    - **RevisionId** *(string) --*

      A unique identifier that changes when you update the alias.
    """


_ClientUpdateAliasRoutingConfigTypeDef = TypedDict(
    "_ClientUpdateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientUpdateAliasRoutingConfigTypeDef(_ClientUpdateAliasRoutingConfigTypeDef):
    """
    Type definition for `ClientUpdateAlias` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ of
    the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ClientUpdateEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ClientUpdateEventSourceMappingResponseTypeDef(
    _ClientUpdateEventSourceMappingResponseTypeDef
):
    """
    Type definition for `ClientUpdateEventSourceMapping` `Response`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for
    details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef(
    _ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponse` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef(
    _ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponseEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientUpdateFunctionCodeResponseEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionCodeResponseEnvironmentTypeDef(
    _ClientUpdateFunctionCodeResponseEnvironmentTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponse` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientUpdateFunctionCodeResponseLayersTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientUpdateFunctionCodeResponseLayersTypeDef(
    _ClientUpdateFunctionCodeResponseLayersTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponse` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientUpdateFunctionCodeResponseTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseTracingConfigTypeDef", {"Mode": str}, total=False
)


class ClientUpdateFunctionCodeResponseTracingConfigTypeDef(
    _ClientUpdateFunctionCodeResponseTracingConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponse` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientUpdateFunctionCodeResponseVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientUpdateFunctionCodeResponseVpcConfigTypeDef(
    _ClientUpdateFunctionCodeResponseVpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionCodeResponse` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientUpdateFunctionCodeResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientUpdateFunctionCodeResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef,
        "Environment": ClientUpdateFunctionCodeResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientUpdateFunctionCodeResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientUpdateFunctionCodeResponseLayersTypeDef],
    },
    total=False,
)


class ClientUpdateFunctionCodeResponseTypeDef(_ClientUpdateFunctionCodeResponseTypeDef):
    """
    Type definition for `ClientUpdateFunctionCode` `Response`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef(
    _ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfiguration` `DeadLetterConfig`

    A dead letter queue configuration that specifies the queue or topic where Lambda sends
    asynchronous events when they fail processing. For more information, see `Dead Letter Queues
    <https://docs.aws.amazon.com/lambda/latest/dg/dlq.html>`__ .

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientUpdateFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationEnvironmentTypeDef",
    {"Variables": Dict[str, str]},
    total=False,
)


class ClientUpdateFunctionConfigurationEnvironmentTypeDef(
    _ClientUpdateFunctionConfigurationEnvironmentTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfiguration` `Environment`

    Environment variables that are accessible from function code during execution.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponse` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef(
    _ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponseEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef(
    _ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponse` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ClientUpdateFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseLayersTypeDef(
    _ClientUpdateFunctionConfigurationResponseLayersTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponse` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponse` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfigurationResponse` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ClientUpdateFunctionConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef,
        "Environment": ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientUpdateFunctionConfigurationResponseLayersTypeDef],
    },
    total=False,
)


class ClientUpdateFunctionConfigurationResponseTypeDef(
    _ClientUpdateFunctionConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfiguration` `Response`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ClientUpdateFunctionConfigurationTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationTracingConfigTypeDef", {"Mode": str}, total=False
)


class ClientUpdateFunctionConfigurationTracingConfigTypeDef(
    _ClientUpdateFunctionConfigurationTracingConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfiguration` `TracingConfig`

    Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientUpdateFunctionConfigurationVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFunctionConfigurationVpcConfigTypeDef(
    _ClientUpdateFunctionConfigurationVpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateFunctionConfiguration` `VpcConfig`

    For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets
    in the VPC. When you connect a function to a VPC, it can only access resources and the internet
    through that VPC. For more information, see `VPC Settings
    <https://docs.aws.amazon.com/lambda/latest/dg/vpc.html>`__ .

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*
    """


_FunctionExistsWaitWaiterConfigTypeDef = TypedDict(
    "_FunctionExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class FunctionExistsWaitWaiterConfigTypeDef(_FunctionExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `FunctionExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(
    _ListAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAliasesPaginate` `PaginationConfig`

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


_ListAliasesPaginateResponseAliasesRoutingConfigTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ListAliasesPaginateResponseAliasesRoutingConfigTypeDef(
    _ListAliasesPaginateResponseAliasesRoutingConfigTypeDef
):
    """
    Type definition for `ListAliasesPaginateResponseAliases` `RoutingConfig`

    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
    of the alias.

    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.

      - *(string) --*

        - *(float) --*
    """


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ListAliasesPaginateResponseAliasesRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)


class ListAliasesPaginateResponseAliasesTypeDef(
    _ListAliasesPaginateResponseAliasesTypeDef
):
    """
    Type definition for `ListAliasesPaginateResponse` `Aliases`

    Provides configuration information about a Lambda function `alias
    <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

    - **AliasArn** *(string) --*

      The Amazon Resource Name (ARN) of the alias.

    - **Name** *(string) --*

      The name of the alias.

    - **FunctionVersion** *(string) --*

      The function version that the alias invokes.

    - **Description** *(string) --*

      A description of the alias.

    - **RoutingConfig** *(dict) --*

      The `routing configuration
      <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
      of the alias.

      - **AdditionalVersionWeights** *(dict) --*

        The name of the second alias, and the percentage of traffic that's routed to it.

        - *(string) --*

          - *(float) --*

    - **RevisionId** *(string) --*

      A unique identifier that changes when you update the alias.
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef], "NextToken": str},
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    Type definition for `ListAliasesPaginate` `Response`

    - **Aliases** *(list) --*

      A list of aliases.

      - *(dict) --*

        Provides configuration information about a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

        - **AliasArn** *(string) --*

          The Amazon Resource Name (ARN) of the alias.

        - **Name** *(string) --*

          The name of the alias.

        - **FunctionVersion** *(string) --*

          The function version that the alias invokes.

        - **Description** *(string) --*

          A description of the alias.

        - **RoutingConfig** *(dict) --*

          The `routing configuration
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
          of the alias.

          - **AdditionalVersionWeights** *(dict) --*

            The name of the second alias, and the percentage of traffic that's routed to it.

            - *(string) --*

              - *(float) --*

        - **RevisionId** *(string) --*

          A unique identifier that changes when you update the alias.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListEventSourceMappingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventSourceMappingsPaginatePaginationConfigTypeDef(
    _ListEventSourceMappingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEventSourceMappingsPaginate` `PaginationConfig`

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


_ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
    },
    total=False,
)


class ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef(
    _ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef
):
    """
    Type definition for `ListEventSourceMappingsPaginateResponse` `EventSourceMappings`

    A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
    for details.

    - **UUID** *(string) --*

      The identifier of the event source mapping.

    - **BatchSize** *(integer) --*

      The maximum number of items to retrieve in a single batch.

    - **MaximumBatchingWindowInSeconds** *(integer) --*

    - **EventSourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the event source.

    - **FunctionArn** *(string) --*

      The ARN of the Lambda function.

    - **LastModified** *(datetime) --*

      The date that the event source mapping was last updated.

    - **LastProcessingResult** *(string) --*

      The result of the last AWS Lambda invocation of your Lambda function.

    - **State** *(string) --*

      The state of the event source mapping. It can be one of the following: ``Creating`` ,
      ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
      ``Deleting`` .

    - **StateTransitionReason** *(string) --*

      The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
    """


_ListEventSourceMappingsPaginateResponseTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseTypeDef",
    {
        "EventSourceMappings": List[
            ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListEventSourceMappingsPaginateResponseTypeDef(
    _ListEventSourceMappingsPaginateResponseTypeDef
):
    """
    Type definition for `ListEventSourceMappingsPaginate` `Response`

    - **EventSourceMappings** *(list) --*

      A list of event source mappings.

      - *(dict) --*

        A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
        for details.

        - **UUID** *(string) --*

          The identifier of the event source mapping.

        - **BatchSize** *(integer) --*

          The maximum number of items to retrieve in a single batch.

        - **MaximumBatchingWindowInSeconds** *(integer) --*

        - **EventSourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the event source.

        - **FunctionArn** *(string) --*

          The ARN of the Lambda function.

        - **LastModified** *(datetime) --*

          The date that the event source mapping was last updated.

        - **LastProcessingResult** *(string) --*

          The result of the last AWS Lambda invocation of your Lambda function.

        - **State** *(string) --*

          The state of the event source mapping. It can be one of the following: ``Creating`` ,
          ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
          ``Deleting`` .

        - **StateTransitionReason** *(string) --*

          The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionsPaginatePaginationConfigTypeDef(
    _ListFunctionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFunctionsPaginate` `PaginationConfig`

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


_ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctions` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef(
    _ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctionsEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef(
    _ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctions` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ListFunctionsPaginateResponseFunctionsLayersTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsLayersTypeDef(
    _ListFunctionsPaginateResponseFunctionsLayersTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctions` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctions` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponseFunctions` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ListFunctionsPaginateResponseFunctionsTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef,
        "DeadLetterConfig": ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef,
        "Environment": ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ListFunctionsPaginateResponseFunctionsLayersTypeDef],
    },
    total=False,
)


class ListFunctionsPaginateResponseFunctionsTypeDef(
    _ListFunctionsPaginateResponseFunctionsTypeDef
):
    """
    Type definition for `ListFunctionsPaginateResponse` `Functions`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ListFunctionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseTypeDef",
    {
        "Functions": List[ListFunctionsPaginateResponseFunctionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListFunctionsPaginateResponseTypeDef(_ListFunctionsPaginateResponseTypeDef):
    """
    Type definition for `ListFunctionsPaginate` `Response`

    A list of Lambda functions.

    - **Functions** *(list) --*

      A list of Lambda functions.

      - *(dict) --*

        Details about a function's configuration.

        - **FunctionName** *(string) --*

          The name of the function.

        - **FunctionArn** *(string) --*

          The function's Amazon Resource Name (ARN).

        - **Runtime** *(string) --*

          The runtime environment for the Lambda function.

        - **Role** *(string) --*

          The function's execution role.

        - **Handler** *(string) --*

          The function that Lambda calls to begin executing your function.

        - **CodeSize** *(integer) --*

          The size of the function's deployment package, in bytes.

        - **Description** *(string) --*

          The function's description.

        - **Timeout** *(integer) --*

          The amount of time that Lambda allows a function to run before stopping it.

        - **MemorySize** *(integer) --*

          The memory that's allocated to the function.

        - **LastModified** *(string) --*

          The date and time that the function was last updated, in `ISO-8601 format
          <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

        - **CodeSha256** *(string) --*

          The SHA256 hash of the function's deployment package.

        - **Version** *(string) --*

          The version of the Lambda function.

        - **VpcConfig** *(dict) --*

          The function's networking configuration.

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

          - **VpcId** *(string) --*

            The ID of the VPC.

        - **DeadLetterConfig** *(dict) --*

          The function's dead letter queue.

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        - **Environment** *(dict) --*

          The function's environment variables.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

          - **Error** *(dict) --*

            Error messages for environment variables that couldn't be applied.

            - **ErrorCode** *(string) --*

              The error code.

            - **Message** *(string) --*

              The error message.

        - **KMSKeyArn** *(string) --*

          The KMS key that's used to encrypt the function's environment variables. This key is only
          returned if you've configured a customer-managed CMK.

        - **TracingConfig** *(dict) --*

          The function's AWS X-Ray tracing configuration.

          - **Mode** *(string) --*

            The tracing mode.

        - **MasterArn** *(string) --*

          For Lambda@Edge functions, the ARN of the master function.

        - **RevisionId** *(string) --*

          The latest updated revision of the function or alias.

        - **Layers** *(list) --*

          The function's `layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

          - *(dict) --*

            An `AWS Lambda layer
            <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the function layer.

            - **CodeSize** *(integer) --*

              The size of the layer archive in bytes.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListLayerVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLayerVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLayerVersionsPaginatePaginationConfigTypeDef(
    _ListLayerVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLayerVersionsPaginate` `PaginationConfig`

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


_ListLayerVersionsPaginateResponseLayerVersionsTypeDef = TypedDict(
    "_ListLayerVersionsPaginateResponseLayerVersionsTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ListLayerVersionsPaginateResponseLayerVersionsTypeDef(
    _ListLayerVersionsPaginateResponseLayerVersionsTypeDef
):
    """
    Type definition for `ListLayerVersionsPaginateResponse` `LayerVersions`

    Details about a version of an `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Version** *(integer) --*

      The version number.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the version was created, in ISO 8601 format. For example,
      ``2018-11-27T15:10:45.123+0000`` .

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's open-source license.
    """


_ListLayerVersionsPaginateResponseTypeDef = TypedDict(
    "_ListLayerVersionsPaginateResponseTypeDef",
    {
        "LayerVersions": List[ListLayerVersionsPaginateResponseLayerVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListLayerVersionsPaginateResponseTypeDef(
    _ListLayerVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListLayerVersionsPaginate` `Response`

    - **LayerVersions** *(list) --*

      A list of versions.

      - *(dict) --*

        Details about a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **LayerVersionArn** *(string) --*

          The ARN of the layer version.

        - **Version** *(integer) --*

          The version number.

        - **Description** *(string) --*

          The description of the version.

        - **CreatedDate** *(string) --*

          The date that the version was created, in ISO 8601 format. For example,
          ``2018-11-27T15:10:45.123+0000`` .

        - **CompatibleRuntimes** *(list) --*

          The layer's compatible runtimes.

          - *(string) --*

        - **LicenseInfo** *(string) --*

          The layer's open-source license.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListLayersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLayersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLayersPaginatePaginationConfigTypeDef(
    _ListLayersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLayersPaginate` `PaginationConfig`

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


_ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "_ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[str],
        "LicenseInfo": str,
    },
    total=False,
)


class ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef(
    _ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef
):
    """
    Type definition for `ListLayersPaginateResponseLayers` `LatestMatchingVersion`

    The newest version of the layer.

    - **LayerVersionArn** *(string) --*

      The ARN of the layer version.

    - **Version** *(integer) --*

      The version number.

    - **Description** *(string) --*

      The description of the version.

    - **CreatedDate** *(string) --*

      The date that the version was created, in ISO 8601 format. For example,
      ``2018-11-27T15:10:45.123+0000`` .

    - **CompatibleRuntimes** *(list) --*

      The layer's compatible runtimes.

      - *(string) --*

    - **LicenseInfo** *(string) --*

      The layer's open-source license.
    """


_ListLayersPaginateResponseLayersTypeDef = TypedDict(
    "_ListLayersPaginateResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)


class ListLayersPaginateResponseLayersTypeDef(_ListLayersPaginateResponseLayersTypeDef):
    """
    Type definition for `ListLayersPaginateResponse` `Layers`

    Details about an `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **LayerName** *(string) --*

      The name of the layer.

    - **LayerArn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **LatestMatchingVersion** *(dict) --*

      The newest version of the layer.

      - **LayerVersionArn** *(string) --*

        The ARN of the layer version.

      - **Version** *(integer) --*

        The version number.

      - **Description** *(string) --*

        The description of the version.

      - **CreatedDate** *(string) --*

        The date that the version was created, in ISO 8601 format. For example,
        ``2018-11-27T15:10:45.123+0000`` .

      - **CompatibleRuntimes** *(list) --*

        The layer's compatible runtimes.

        - *(string) --*

      - **LicenseInfo** *(string) --*

        The layer's open-source license.
    """


_ListLayersPaginateResponseTypeDef = TypedDict(
    "_ListLayersPaginateResponseTypeDef",
    {"Layers": List[ListLayersPaginateResponseLayersTypeDef], "NextToken": str},
    total=False,
)


class ListLayersPaginateResponseTypeDef(_ListLayersPaginateResponseTypeDef):
    """
    Type definition for `ListLayersPaginate` `Response`

    - **Layers** *(list) --*

      A list of function layers.

      - *(dict) --*

        Details about an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **LayerName** *(string) --*

          The name of the layer.

        - **LayerArn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **LatestMatchingVersion** *(dict) --*

          The newest version of the layer.

          - **LayerVersionArn** *(string) --*

            The ARN of the layer version.

          - **Version** *(integer) --*

            The version number.

          - **Description** *(string) --*

            The description of the version.

          - **CreatedDate** *(string) --*

            The date that the version was created, in ISO 8601 format. For example,
            ``2018-11-27T15:10:45.123+0000`` .

          - **CompatibleRuntimes** *(list) --*

            The layer's compatible runtimes.

            - *(string) --*

          - **LicenseInfo** *(string) --*

            The layer's open-source license.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVersionsByFunctionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVersionsByFunctionPaginatePaginationConfigTypeDef(
    _ListVersionsByFunctionPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginate` `PaginationConfig`

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


_ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersions` `DeadLetterConfig`

    The function's dead letter queue.

    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersionsEnvironment` `Error`

    Error messages for environment variables that couldn't be applied.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersions` `Environment`

    The function's environment variables.

    - **Variables** *(dict) --*

      Environment variable key-value pairs.

      - *(string) --*

        - *(string) --*

    - **Error** *(dict) --*

      Error messages for environment variables that couldn't be applied.

      - **ErrorCode** *(string) --*

        The error code.

      - **Message** *(string) --*

        The error message.
    """


_ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersions` `Layers`

    An `AWS Lambda layer
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the function layer.

    - **CodeSize** *(integer) --*

      The size of the layer archive in bytes.
    """


_ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef",
    {"Mode": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersions` `TracingConfig`

    The function's AWS X-Ray tracing configuration.

    - **Mode** *(string) --*

      The tracing mode.
    """


_ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponseVersions` `VpcConfig`

    The function's networking configuration.

    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.

      - *(string) --*

    - **SecurityGroupIds** *(list) --*

      A list of VPC security groups IDs.

      - *(string) --*

    - **VpcId** *(string) --*

      The ID of the VPC.
    """


_ListVersionsByFunctionPaginateResponseVersionsTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": str,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef,
        "DeadLetterConfig": ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef,
        "Environment": ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef],
    },
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginateResponse` `Versions`

    Details about a function's configuration.

    - **FunctionName** *(string) --*

      The name of the function.

    - **FunctionArn** *(string) --*

      The function's Amazon Resource Name (ARN).

    - **Runtime** *(string) --*

      The runtime environment for the Lambda function.

    - **Role** *(string) --*

      The function's execution role.

    - **Handler** *(string) --*

      The function that Lambda calls to begin executing your function.

    - **CodeSize** *(integer) --*

      The size of the function's deployment package, in bytes.

    - **Description** *(string) --*

      The function's description.

    - **Timeout** *(integer) --*

      The amount of time that Lambda allows a function to run before stopping it.

    - **MemorySize** *(integer) --*

      The memory that's allocated to the function.

    - **LastModified** *(string) --*

      The date and time that the function was last updated, in `ISO-8601 format
      <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

    - **CodeSha256** *(string) --*

      The SHA256 hash of the function's deployment package.

    - **Version** *(string) --*

      The version of the Lambda function.

    - **VpcConfig** *(dict) --*

      The function's networking configuration.

      - **SubnetIds** *(list) --*

        A list of VPC subnet IDs.

        - *(string) --*

      - **SecurityGroupIds** *(list) --*

        A list of VPC security groups IDs.

        - *(string) --*

      - **VpcId** *(string) --*

        The ID of the VPC.

    - **DeadLetterConfig** *(dict) --*

      The function's dead letter queue.

      - **TargetArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

    - **Environment** *(dict) --*

      The function's environment variables.

      - **Variables** *(dict) --*

        Environment variable key-value pairs.

        - *(string) --*

          - *(string) --*

      - **Error** *(dict) --*

        Error messages for environment variables that couldn't be applied.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.

    - **KMSKeyArn** *(string) --*

      The KMS key that's used to encrypt the function's environment variables. This key is only
      returned if you've configured a customer-managed CMK.

    - **TracingConfig** *(dict) --*

      The function's AWS X-Ray tracing configuration.

      - **Mode** *(string) --*

        The tracing mode.

    - **MasterArn** *(string) --*

      For Lambda@Edge functions, the ARN of the master function.

    - **RevisionId** *(string) --*

      The latest updated revision of the function or alias.

    - **Layers** *(list) --*

      The function's `layers
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

      - *(dict) --*

        An `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the function layer.

        - **CodeSize** *(integer) --*

          The size of the layer archive in bytes.
    """


_ListVersionsByFunctionPaginateResponseTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseTypeDef",
    {
        "Versions": List[ListVersionsByFunctionPaginateResponseVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVersionsByFunctionPaginateResponseTypeDef(
    _ListVersionsByFunctionPaginateResponseTypeDef
):
    """
    Type definition for `ListVersionsByFunctionPaginate` `Response`

    - **Versions** *(list) --*

      A list of Lambda function versions.

      - *(dict) --*

        Details about a function's configuration.

        - **FunctionName** *(string) --*

          The name of the function.

        - **FunctionArn** *(string) --*

          The function's Amazon Resource Name (ARN).

        - **Runtime** *(string) --*

          The runtime environment for the Lambda function.

        - **Role** *(string) --*

          The function's execution role.

        - **Handler** *(string) --*

          The function that Lambda calls to begin executing your function.

        - **CodeSize** *(integer) --*

          The size of the function's deployment package, in bytes.

        - **Description** *(string) --*

          The function's description.

        - **Timeout** *(integer) --*

          The amount of time that Lambda allows a function to run before stopping it.

        - **MemorySize** *(integer) --*

          The memory that's allocated to the function.

        - **LastModified** *(string) --*

          The date and time that the function was last updated, in `ISO-8601 format
          <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

        - **CodeSha256** *(string) --*

          The SHA256 hash of the function's deployment package.

        - **Version** *(string) --*

          The version of the Lambda function.

        - **VpcConfig** *(dict) --*

          The function's networking configuration.

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

          - **VpcId** *(string) --*

            The ID of the VPC.

        - **DeadLetterConfig** *(dict) --*

          The function's dead letter queue.

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        - **Environment** *(dict) --*

          The function's environment variables.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

          - **Error** *(dict) --*

            Error messages for environment variables that couldn't be applied.

            - **ErrorCode** *(string) --*

              The error code.

            - **Message** *(string) --*

              The error message.

        - **KMSKeyArn** *(string) --*

          The KMS key that's used to encrypt the function's environment variables. This key is only
          returned if you've configured a customer-managed CMK.

        - **TracingConfig** *(dict) --*

          The function's AWS X-Ray tracing configuration.

          - **Mode** *(string) --*

            The tracing mode.

        - **MasterArn** *(string) --*

          For Lambda@Edge functions, the ARN of the master function.

        - **RevisionId** *(string) --*

          The latest updated revision of the function or alias.

        - **Layers** *(list) --*

          The function's `layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

          - *(dict) --*

            An `AWS Lambda layer
            <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the function layer.

            - **CodeSize** *(integer) --*

              The size of the layer archive in bytes.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
