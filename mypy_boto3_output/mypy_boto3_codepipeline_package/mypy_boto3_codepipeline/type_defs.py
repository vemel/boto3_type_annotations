"Main interface for codepipeline type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAcknowledgeJobResponseTypeDef",
    "ClientAcknowledgeThirdPartyJobResponseTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeidTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeTypeDef",
    "ClientCreateCustomActionTypeResponsetagsTypeDef",
    "ClientCreateCustomActionTypeResponseTypeDef",
    "ClientCreateCustomActionTypeconfigurationPropertiesTypeDef",
    "ClientCreateCustomActionTypeinputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeoutputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypesettingsTypeDef",
    "ClientCreateCustomActionTypetagsTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoreTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoresTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesblockersTypeDef",
    "ClientCreatePipelineResponsepipelinestagesTypeDef",
    "ClientCreatePipelineResponsepipelineTypeDef",
    "ClientCreatePipelineResponsetagsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef",
    "ClientCreatePipelinepipelineartifactStoreTypeDef",
    "ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef",
    "ClientCreatePipelinepipelineartifactStoresTypeDef",
    "ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef",
    "ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef",
    "ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientCreatePipelinepipelinestagesactionsTypeDef",
    "ClientCreatePipelinepipelinestagesblockersTypeDef",
    "ClientCreatePipelinepipelinestagesTypeDef",
    "ClientCreatePipelinepipelineTypeDef",
    "ClientCreatePipelinetagsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataTypeDef",
    "ClientGetJobDetailsResponsejobDetailsTypeDef",
    "ClientGetJobDetailsResponseTypeDef",
    "ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef",
    "ClientGetPipelineExecutionResponsepipelineExecutionTypeDef",
    "ClientGetPipelineExecutionResponseTypeDef",
    "ClientGetPipelineResponsemetadataTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoreTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoresTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsTypeDef",
    "ClientGetPipelineResponsepipelinestagesblockersTypeDef",
    "ClientGetPipelineResponsepipelinestagesTypeDef",
    "ClientGetPipelineResponsepipelineTypeDef",
    "ClientGetPipelineResponseTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStatesTypeDef",
    "ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef",
    "ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef",
    "ClientGetPipelineStateResponsestageStatesTypeDef",
    "ClientGetPipelineStateResponseTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef",
    "ClientGetThirdPartyJobDetailsResponseTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsTypeDef",
    "ClientListActionExecutionsResponseTypeDef",
    "ClientListActionExecutionsfilterTypeDef",
    "ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef",
    "ClientListActionTypesResponseactionTypesidTypeDef",
    "ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef",
    "ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef",
    "ClientListActionTypesResponseactionTypessettingsTypeDef",
    "ClientListActionTypesResponseactionTypesTypeDef",
    "ClientListActionTypesResponseTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef",
    "ClientListPipelineExecutionsResponseTypeDef",
    "ClientListPipelinesResponsepipelinesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionTypeDef",
    "ClientListWebhooksResponsewebhookstagsTypeDef",
    "ClientListWebhooksResponsewebhooksTypeDef",
    "ClientListWebhooksResponseTypeDef",
    "ClientPollForJobsResponsejobsdataactionConfigurationTypeDef",
    "ClientPollForJobsResponsejobsdataactionTypeIdTypeDef",
    "ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef",
    "ClientPollForJobsResponsejobsdataencryptionKeyTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactsTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextTypeDef",
    "ClientPollForJobsResponsejobsdataTypeDef",
    "ClientPollForJobsResponsejobsTypeDef",
    "ClientPollForJobsResponseTypeDef",
    "ClientPollForJobsactionTypeIdTypeDef",
    "ClientPollForThirdPartyJobsResponsejobsTypeDef",
    "ClientPollForThirdPartyJobsResponseTypeDef",
    "ClientPollForThirdPartyJobsactionTypeIdTypeDef",
    "ClientPutActionRevisionResponseTypeDef",
    "ClientPutActionRevisionactionRevisionTypeDef",
    "ClientPutApprovalResultResponseTypeDef",
    "ClientPutApprovalResultresultTypeDef",
    "ClientPutJobFailureResultfailureDetailsTypeDef",
    "ClientPutJobSuccessResultcurrentRevisionTypeDef",
    "ClientPutJobSuccessResultexecutionDetailsTypeDef",
    "ClientPutThirdPartyJobFailureResultfailureDetailsTypeDef",
    "ClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef",
    "ClientPutThirdPartyJobSuccessResultexecutionDetailsTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionTypeDef",
    "ClientPutWebhookResponsewebhooktagsTypeDef",
    "ClientPutWebhookResponsewebhookTypeDef",
    "ClientPutWebhookResponseTypeDef",
    "ClientPutWebhooktagsTypeDef",
    "ClientPutWebhookwebhookauthenticationConfigurationTypeDef",
    "ClientPutWebhookwebhookfiltersTypeDef",
    "ClientPutWebhookwebhookTypeDef",
    "ClientRetryStageExecutionResponseTypeDef",
    "ClientStartPipelineExecutionResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoreTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoresTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesblockersTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesTypeDef",
    "ClientUpdatePipelineResponsepipelineTypeDef",
    "ClientUpdatePipelineResponseTypeDef",
    "ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef",
    "ClientUpdatePipelinepipelineartifactStoreTypeDef",
    "ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef",
    "ClientUpdatePipelinepipelineartifactStoresTypeDef",
    "ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef",
    "ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef",
    "ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientUpdatePipelinepipelinestagesactionsTypeDef",
    "ClientUpdatePipelinepipelinestagesblockersTypeDef",
    "ClientUpdatePipelinepipelinestagesTypeDef",
    "ClientUpdatePipelinepipelineTypeDef",
    "ListActionExecutionsPaginatePaginationConfigTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef",
    "ListActionExecutionsPaginateResponseTypeDef",
    "ListActionExecutionsPaginatefilterTypeDef",
    "ListActionTypesPaginatePaginationConfigTypeDef",
    "ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef",
    "ListActionTypesPaginateResponseactionTypesidTypeDef",
    "ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef",
    "ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef",
    "ListActionTypesPaginateResponseactionTypessettingsTypeDef",
    "ListActionTypesPaginateResponseactionTypesTypeDef",
    "ListActionTypesPaginateResponseTypeDef",
    "ListPipelineExecutionsPaginatePaginationConfigTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef",
    "ListPipelineExecutionsPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelinesTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListWebhooksPaginatePaginationConfigTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionTypeDef",
    "ListWebhooksPaginateResponsewebhookstagsTypeDef",
    "ListWebhooksPaginateResponsewebhooksTypeDef",
    "ListWebhooksPaginateResponseTypeDef",
)


_ClientAcknowledgeJobResponseTypeDef = TypedDict(
    "_ClientAcknowledgeJobResponseTypeDef", {"status": str}, total=False
)


class ClientAcknowledgeJobResponseTypeDef(_ClientAcknowledgeJobResponseTypeDef):
    """
    Type definition for `ClientAcknowledgeJob` `Response`

    Represents the output of an AcknowledgeJob action.

    - **status** *(string) --*

      Whether the job worker has received the specified job.
    """


_ClientAcknowledgeThirdPartyJobResponseTypeDef = TypedDict(
    "_ClientAcknowledgeThirdPartyJobResponseTypeDef", {"status": str}, total=False
)


class ClientAcknowledgeThirdPartyJobResponseTypeDef(
    _ClientAcknowledgeThirdPartyJobResponseTypeDef
):
    """
    Type definition for `ClientAcknowledgeThirdPartyJob` `Response`

    Represents the output of an AcknowledgeThirdPartyJob action.

    - **status** *(string) --*

      The status information for the third party job, if any.
    """


_ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": str,
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponseactionType` `actionConfigurationProperties`

    Represents information about an action configuration property.

    - **name** *(string) --*

      The name of the action configuration property.

    - **required** *(boolean) --*

      Whether the configuration property is a required value.

    - **key** *(boolean) --*

      Whether the configuration property is a key.

    - **secret** *(boolean) --*

      Whether the configuration property is secret. Secrets are hidden from all calls except
      for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
      ``PollForThirdPartyJobs`` .

      When updating a pipeline, passing * * * * * without changing any other values of the
      action preserves the previous value of the secret.

    - **queryable** *(boolean) --*

      Indicates that the property is used with ``PollForJobs`` . When creating a custom
      action, an action can have up to one queryable property. If it has one, that property
      must be both required and not secret.

      If you create a pipeline with a custom action type, and that custom action contains a
      queryable property, the value for that configuration property is subject to other
      restrictions. The value must be less than or equal to twenty (20) characters. The value
      can contain only alphanumeric characters, underscores, and hyphens.

    - **description** *(string) --*

      The description of the action configuration property that is displayed to users.

    - **type** *(string) --*

      The type of the configuration property.
    """


_ClientCreateCustomActionTypeResponseactionTypeidTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeidTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeidTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeidTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponseactionType` `id`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are determined by
      the action category. For example, an action in the Deploy category type might have a
      provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information,
      see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponseactionType` `inputArtifactDetails`

    The details of the input artifact for the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponseactionType` `outputArtifactDetails`

    The details of the output artifact of the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponseactionType` `settings`

    The settings for the action type.

    - **thirdPartyConfigurationUrl** *(string) --*

      The URL of a sign-up page where users can sign up for an external service and perform
      initial configuration of the action provided by that service.

    - **entityUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that provides a deep link to the
      resources of the external system, such as the configuration page for an AWS CodeDeploy
      deployment group. This link is provided as part of the action display in the pipeline.

    - **executionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the top-level
      landing page for the external system, such as the console page for AWS CodeDeploy. This
      link is shown on the pipeline view page in the AWS CodePipeline console and provides a
      link to the execution entity of the external action.

    - **revisionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the page where
      customers can update or change the configuration of the external action.
    """


_ClientCreateCustomActionTypeResponseactionTypeTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeTypeDef",
    {
        "id": ClientCreateCustomActionTypeResponseactionTypeidTypeDef,
        "settings": ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef,
        "actionConfigurationProperties": List[
            ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef,
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponse` `actionType`

    Returns information about the details of an action type.

    - **id** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are determined by
        the action category. For example, an action in the Deploy category type might have a
        provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information,
        see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **settings** *(dict) --*

      The settings for the action type.

      - **thirdPartyConfigurationUrl** *(string) --*

        The URL of a sign-up page where users can sign up for an external service and perform
        initial configuration of the action provided by that service.

      - **entityUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that provides a deep link to the
        resources of the external system, such as the configuration page for an AWS CodeDeploy
        deployment group. This link is provided as part of the action display in the pipeline.

      - **executionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the top-level
        landing page for the external system, such as the console page for AWS CodeDeploy. This
        link is shown on the pipeline view page in the AWS CodePipeline console and provides a
        link to the execution entity of the external action.

      - **revisionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the page where
        customers can update or change the configuration of the external action.

    - **actionConfigurationProperties** *(list) --*

      The configuration properties for the action type.

      - *(dict) --*

        Represents information about an action configuration property.

        - **name** *(string) --*

          The name of the action configuration property.

        - **required** *(boolean) --*

          Whether the configuration property is a required value.

        - **key** *(boolean) --*

          Whether the configuration property is a key.

        - **secret** *(boolean) --*

          Whether the configuration property is secret. Secrets are hidden from all calls except
          for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
          ``PollForThirdPartyJobs`` .

          When updating a pipeline, passing * * * * * without changing any other values of the
          action preserves the previous value of the secret.

        - **queryable** *(boolean) --*

          Indicates that the property is used with ``PollForJobs`` . When creating a custom
          action, an action can have up to one queryable property. If it has one, that property
          must be both required and not secret.

          If you create a pipeline with a custom action type, and that custom action contains a
          queryable property, the value for that configuration property is subject to other
          restrictions. The value must be less than or equal to twenty (20) characters. The value
          can contain only alphanumeric characters, underscores, and hyphens.

        - **description** *(string) --*

          The description of the action configuration property that is displayed to users.

        - **type** *(string) --*

          The type of the configuration property.

    - **inputArtifactDetails** *(dict) --*

      The details of the input artifact for the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.

    - **outputArtifactDetails** *(dict) --*

      The details of the output artifact of the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypeResponsetagsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateCustomActionTypeResponsetagsTypeDef(
    _ClientCreateCustomActionTypeResponsetagsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionTypeResponse` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientCreateCustomActionTypeResponseTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseTypeDef",
    {
        "actionType": ClientCreateCustomActionTypeResponseactionTypeTypeDef,
        "tags": List[ClientCreateCustomActionTypeResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseTypeDef(
    _ClientCreateCustomActionTypeResponseTypeDef
):
    """
    Type definition for `ClientCreateCustomActionType` `Response`

    Represents the output of a ``CreateCustomActionType`` operation.

    - **actionType** *(dict) --*

      Returns information about the details of an action type.

      - **id** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are determined by
          the action category. For example, an action in the Deploy category type might have a
          provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information,
          see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **settings** *(dict) --*

        The settings for the action type.

        - **thirdPartyConfigurationUrl** *(string) --*

          The URL of a sign-up page where users can sign up for an external service and perform
          initial configuration of the action provided by that service.

        - **entityUrlTemplate** *(string) --*

          The URL returned to the AWS CodePipeline console that provides a deep link to the
          resources of the external system, such as the configuration page for an AWS CodeDeploy
          deployment group. This link is provided as part of the action display in the pipeline.

        - **executionUrlTemplate** *(string) --*

          The URL returned to the AWS CodePipeline console that contains a link to the top-level
          landing page for the external system, such as the console page for AWS CodeDeploy. This
          link is shown on the pipeline view page in the AWS CodePipeline console and provides a
          link to the execution entity of the external action.

        - **revisionUrlTemplate** *(string) --*

          The URL returned to the AWS CodePipeline console that contains a link to the page where
          customers can update or change the configuration of the external action.

      - **actionConfigurationProperties** *(list) --*

        The configuration properties for the action type.

        - *(dict) --*

          Represents information about an action configuration property.

          - **name** *(string) --*

            The name of the action configuration property.

          - **required** *(boolean) --*

            Whether the configuration property is a required value.

          - **key** *(boolean) --*

            Whether the configuration property is a key.

          - **secret** *(boolean) --*

            Whether the configuration property is secret. Secrets are hidden from all calls except
            for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
            ``PollForThirdPartyJobs`` .

            When updating a pipeline, passing * * * * * without changing any other values of the
            action preserves the previous value of the secret.

          - **queryable** *(boolean) --*

            Indicates that the property is used with ``PollForJobs`` . When creating a custom
            action, an action can have up to one queryable property. If it has one, that property
            must be both required and not secret.

            If you create a pipeline with a custom action type, and that custom action contains a
            queryable property, the value for that configuration property is subject to other
            restrictions. The value must be less than or equal to twenty (20) characters. The value
            can contain only alphanumeric characters, underscores, and hyphens.

          - **description** *(string) --*

            The description of the action configuration property that is displayed to users.

          - **type** *(string) --*

            The type of the configuration property.

      - **inputArtifactDetails** *(dict) --*

        The details of the input artifact for the action, such as its commit ID.

        - **minimumCount** *(integer) --*

          The minimum number of artifacts allowed for the action type.

        - **maximumCount** *(integer) --*

          The maximum number of artifacts allowed for the action type.

      - **outputArtifactDetails** *(dict) --*

        The details of the output artifact of the action, such as its commit ID.

        - **minimumCount** *(integer) --*

          The minimum number of artifacts allowed for the action type.

        - **maximumCount** *(integer) --*

          The maximum number of artifacts allowed for the action type.

    - **tags** *(list) --*

      Specifies the tags applied to the custom action.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_RequiredClientCreateCustomActionTypeconfigurationPropertiesTypeDef = TypedDict(
    "_RequiredClientCreateCustomActionTypeconfigurationPropertiesTypeDef",
    {"name": str, "required": bool, "key": bool, "secret": bool},
)
_OptionalClientCreateCustomActionTypeconfigurationPropertiesTypeDef = TypedDict(
    "_OptionalClientCreateCustomActionTypeconfigurationPropertiesTypeDef",
    {"queryable": bool, "description": str, "type": str},
    total=False,
)


class ClientCreateCustomActionTypeconfigurationPropertiesTypeDef(
    _RequiredClientCreateCustomActionTypeconfigurationPropertiesTypeDef,
    _OptionalClientCreateCustomActionTypeconfigurationPropertiesTypeDef,
):
    """
    Type definition for `ClientCreateCustomActionType` `configurationProperties`

    Represents information about an action configuration property.

    - **name** *(string) --* **[REQUIRED]**

      The name of the action configuration property.

    - **required** *(boolean) --* **[REQUIRED]**

      Whether the configuration property is a required value.

    - **key** *(boolean) --* **[REQUIRED]**

      Whether the configuration property is a key.

    - **secret** *(boolean) --* **[REQUIRED]**

      Whether the configuration property is secret. Secrets are hidden from all calls except for
      ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
      ``PollForThirdPartyJobs`` .

      When updating a pipeline, passing * * * * * without changing any other values of the action
      preserves the previous value of the secret.

    - **queryable** *(boolean) --*

      Indicates that the property is used with ``PollForJobs`` . When creating a custom action, an
      action can have up to one queryable property. If it has one, that property must be both
      required and not secret.

      If you create a pipeline with a custom action type, and that custom action contains a
      queryable property, the value for that configuration property is subject to other
      restrictions. The value must be less than or equal to twenty (20) characters. The value can
      contain only alphanumeric characters, underscores, and hyphens.

    - **description** *(string) --*

      The description of the action configuration property that is displayed to users.

    - **type** *(string) --*

      The type of the configuration property.
    """


_ClientCreateCustomActionTypeinputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
)


class ClientCreateCustomActionTypeinputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeinputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionType` `inputArtifactDetails`

    The details of the input artifact for the action, such as its commit ID.

    - **minimumCount** *(integer) --* **[REQUIRED]**

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --* **[REQUIRED]**

      The maximum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypeoutputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
)


class ClientCreateCustomActionTypeoutputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeoutputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionType` `outputArtifactDetails`

    The details of the output artifact of the action, such as its commit ID.

    - **minimumCount** *(integer) --* **[REQUIRED]**

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --* **[REQUIRED]**

      The maximum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypesettingsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypesettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientCreateCustomActionTypesettingsTypeDef(
    _ClientCreateCustomActionTypesettingsTypeDef
):
    """
    Type definition for `ClientCreateCustomActionType` `settings`

    URLs that provide users information about this custom action.

    - **thirdPartyConfigurationUrl** *(string) --*

      The URL of a sign-up page where users can sign up for an external service and perform initial
      configuration of the action provided by that service.

    - **entityUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that provides a deep link to the resources of
      the external system, such as the configuration page for an AWS CodeDeploy deployment group.
      This link is provided as part of the action display in the pipeline.

    - **executionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the top-level landing
      page for the external system, such as the console page for AWS CodeDeploy. This link is shown
      on the pipeline view page in the AWS CodePipeline console and provides a link to the execution
      entity of the external action.

    - **revisionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the page where
      customers can update or change the configuration of the external action.
    """


_ClientCreateCustomActionTypetagsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypetagsTypeDef", {"key": str, "value": str}
)


class ClientCreateCustomActionTypetagsTypeDef(_ClientCreateCustomActionTypetagsTypeDef):
    """
    Type definition for `ClientCreateCustomActionType` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelineartifactStore` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
    used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoreTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoreTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipeline` `artifactStore`

    Represents information about the Amazon S3 bucket where artifacts are stored for the
    pipeline.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
      name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
      artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
      bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
      used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelineartifactStores` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
    is used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
      key ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to
        identify the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
      When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoresTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoresTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipeline` `artifactStores`

    The Amazon S3 bucket where artifacts for the pipeline are stored.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
      you cannot use both. If you create a cross-region action in your pipeline, you must
      use ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
      the name of an S3 bucket but not a folder in the bucket. A folder to contain the
      pipeline artifacts is created for you based on the name of the pipeline. You can use
      any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
      artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
      is used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
        key ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to
          identify the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
        When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelinestagesactions` `actionTypeId`

    Specifies the action type and the provider of the action.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains
      the provider type for the action. Valid categories are limited to one of the
      following values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category
      type might have a provider of AWS CodeDeploy, which would be specified as
      CodeDeploy. For more information, see `Valid Action Types and Providers in
      CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelinestagesactions` `inputArtifacts`

    Represents information about an artifact to be worked on, such as a test or build
    artifact.

    - **name** *(string) --*

      The name of the artifact to be worked on (for example, "My App").

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.
    """


_ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelinestagesactions` `outputArtifacts`

    Represents information about the output of an action.

    - **name** *(string) --*

      The name of the output of an artifact, such as "My App".

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.

      Output artifact names must be unique within a pipeline.
    """


_ClientCreatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelinestages` `actions`

    Represents information about an action declaration.

    - **name** *(string) --*

      The action declaration's name.

    - **actionTypeId** *(dict) --*

      Specifies the action type and the provider of the action.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains
        the provider type for the action. Valid categories are limited to one of the
        following values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category
        type might have a provider of AWS CodeDeploy, which would be specified as
        CodeDeploy. For more information, see `Valid Action Types and Providers in
        CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **runOrder** *(integer) --*

      The order in which actions are run.

    - **configuration** *(dict) --*

      The action's configuration. These are key-value pairs that specify input values for
      an action. For more information, see `Action Structure Requirements in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      . For the list of configuration properties for the AWS CloudFormation action type
      in CodePipeline, see `Configuration Properties Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
      in the *AWS CloudFormation User Guide* . For template snippets with examples, see
      `Using Parameter Override Functions with CodePipeline Pipelines
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
      in the *AWS CloudFormation User Guide* .

      The values can be represented in either JSON or YAML format. For example, the JSON
      configuration item format is as follows:

       *JSON:*

       ``"Configuration" : { Key : Value },``

      - *(string) --*

        - *(string) --*

    - **outputArtifacts** *(list) --*

      The name or ID of the result of the action declaration, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about the output of an action.

        - **name** *(string) --*

          The name of the output of an artifact, such as "My App".

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

          Output artifact names must be unique within a pipeline.

    - **inputArtifacts** *(list) --*

      The name or ID of the artifact consumed by the action, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about an artifact to be worked on, such as a test or build
        artifact.

        - **name** *(string) --*

          The name of the artifact to be worked on (for example, "My App").

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The action declaration's AWS Region, such as us-east-1.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output
      by this action fall under this namespace.
    """


_ClientCreatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesblockersTypeDef(
    _ClientCreatePipelineResponsepipelinestagesblockersTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipelinestages` `blockers`

    Reserved for future use.

    - **name** *(string) --*

      Reserved for future use.

    - **type** *(string) --*

      Reserved for future use.
    """


_ClientCreatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientCreatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientCreatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesTypeDef(
    _ClientCreatePipelineResponsepipelinestagesTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponsepipeline` `stages`

    Represents information about a stage and its definition.

    - **name** *(string) --*

      The name of the stage.

    - **blockers** *(list) --*

      Reserved for future use.

      - *(dict) --*

        Reserved for future use.

        - **name** *(string) --*

          Reserved for future use.

        - **type** *(string) --*

          Reserved for future use.

    - **actions** *(list) --*

      The actions included in a stage.

      - *(dict) --*

        Represents information about an action declaration.

        - **name** *(string) --*

          The action declaration's name.

        - **actionTypeId** *(dict) --*

          Specifies the action type and the provider of the action.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains
            the provider type for the action. Valid categories are limited to one of the
            following values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are
            determined by the action category. For example, an action in the Deploy category
            type might have a provider of AWS CodeDeploy, which would be specified as
            CodeDeploy. For more information, see `Valid Action Types and Providers in
            CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **runOrder** *(integer) --*

          The order in which actions are run.

        - **configuration** *(dict) --*

          The action's configuration. These are key-value pairs that specify input values for
          an action. For more information, see `Action Structure Requirements in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          . For the list of configuration properties for the AWS CloudFormation action type
          in CodePipeline, see `Configuration Properties Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
          in the *AWS CloudFormation User Guide* . For template snippets with examples, see
          `Using Parameter Override Functions with CodePipeline Pipelines
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
          in the *AWS CloudFormation User Guide* .

          The values can be represented in either JSON or YAML format. For example, the JSON
          configuration item format is as follows:

           *JSON:*

           ``"Configuration" : { Key : Value },``

          - *(string) --*

            - *(string) --*

        - **outputArtifacts** *(list) --*

          The name or ID of the result of the action declaration, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about the output of an action.

            - **name** *(string) --*

              The name of the output of an artifact, such as "My App".

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

              Output artifact names must be unique within a pipeline.

        - **inputArtifacts** *(list) --*

          The name or ID of the artifact consumed by the action, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about an artifact to be worked on, such as a test or build
            artifact.

            - **name** *(string) --*

              The name of the artifact to be worked on (for example, "My App").

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

        - **roleArn** *(string) --*

          The ARN of the IAM service role that performs the declared action. This is assumed
          through the roleArn for the pipeline.

        - **region** *(string) --*

          The action declaration's AWS Region, such as us-east-1.

        - **namespace** *(string) --*

          The variable namespace associated with the action. All variables produced as output
          by this action fall under this namespace.
    """


_ClientCreatePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientCreatePipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[
            str, ClientCreatePipelineResponsepipelineartifactStoresTypeDef
        ],
        "stages": List[ClientCreatePipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelineTypeDef(
    _ClientCreatePipelineResponsepipelineTypeDef
):
    """
    Type definition for `ClientCreatePipelineResponse` `pipeline`

    Represents the structure of actions and stages to be performed in the pipeline.

    - **name** *(string) --*

      The name of the action to be performed.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
      no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

    - **artifactStore** *(dict) --*

      Represents information about the Amazon S3 bucket where artifacts are stored for the
      pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - **type** *(string) --*

        The type of the artifact store, such as S3.

      - **location** *(string) --*

        The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
        name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
        artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
        bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt the data in the artifact store, such as an AWS Key
        Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
        used.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
            the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **artifactStores** *(dict) --*

      A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
      an artifact store for the pipeline Region and for each cross-region action in the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - *(string) --*

        - *(dict) --*

          The Amazon S3 bucket where artifacts for the pipeline are stored.

          .. note::

            You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
            you cannot use both. If you create a cross-region action in your pipeline, you must
            use ``artifactStores`` .

          - **type** *(string) --*

            The type of the artifact store, such as S3.

          - **location** *(string) --*

            The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
            the name of an S3 bucket but not a folder in the bucket. A folder to contain the
            pipeline artifacts is created for you based on the name of the pipeline. You can use
            any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
            artifacts.

          - **encryptionKey** *(dict) --*

            The encryption key used to encrypt the data in the artifact store, such as an AWS Key
            Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
            is used.

            - **id** *(string) --*

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
              key ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to
                identify the key.

            - **type** *(string) --*

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
              When creating or updating a pipeline, the value must be set to 'KMS'.

    - **stages** *(list) --*

      The stage in which to perform the action.

      - *(dict) --*

        Represents information about a stage and its definition.

        - **name** *(string) --*

          The name of the stage.

        - **blockers** *(list) --*

          Reserved for future use.

          - *(dict) --*

            Reserved for future use.

            - **name** *(string) --*

              Reserved for future use.

            - **type** *(string) --*

              Reserved for future use.

        - **actions** *(list) --*

          The actions included in a stage.

          - *(dict) --*

            Represents information about an action declaration.

            - **name** *(string) --*

              The action declaration's name.

            - **actionTypeId** *(dict) --*

              Specifies the action type and the provider of the action.

              - **category** *(string) --*

                A category defines what kind of action can be taken in the stage, and constrains
                the provider type for the action. Valid categories are limited to one of the
                following values.

              - **owner** *(string) --*

                The creator of the action being called.

              - **provider** *(string) --*

                The provider of the service being called by the action. Valid providers are
                determined by the action category. For example, an action in the Deploy category
                type might have a provider of AWS CodeDeploy, which would be specified as
                CodeDeploy. For more information, see `Valid Action Types and Providers in
                CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                .

              - **version** *(string) --*

                A string that describes the action version.

            - **runOrder** *(integer) --*

              The order in which actions are run.

            - **configuration** *(dict) --*

              The action's configuration. These are key-value pairs that specify input values for
              an action. For more information, see `Action Structure Requirements in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              . For the list of configuration properties for the AWS CloudFormation action type
              in CodePipeline, see `Configuration Properties Reference
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
              in the *AWS CloudFormation User Guide* . For template snippets with examples, see
              `Using Parameter Override Functions with CodePipeline Pipelines
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
              in the *AWS CloudFormation User Guide* .

              The values can be represented in either JSON or YAML format. For example, the JSON
              configuration item format is as follows:

               *JSON:*

               ``"Configuration" : { Key : Value },``

              - *(string) --*

                - *(string) --*

            - **outputArtifacts** *(list) --*

              The name or ID of the result of the action declaration, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about the output of an action.

                - **name** *(string) --*

                  The name of the output of an artifact, such as "My App".

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

                  Output artifact names must be unique within a pipeline.

            - **inputArtifacts** *(list) --*

              The name or ID of the artifact consumed by the action, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about an artifact to be worked on, such as a test or build
                artifact.

                - **name** *(string) --*

                  The name of the artifact to be worked on (for example, "My App").

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

            - **roleArn** *(string) --*

              The ARN of the IAM service role that performs the declared action. This is assumed
              through the roleArn for the pipeline.

            - **region** *(string) --*

              The action declaration's AWS Region, such as us-east-1.

            - **namespace** *(string) --*

              The variable namespace associated with the action. All variables produced as output
              by this action fall under this namespace.

    - **version** *(integer) --*

      The version number of the pipeline. A new pipeline always has a version number of 1. This
      number is incremented when a pipeline is updated.
    """


_ClientCreatePipelineResponsetagsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreatePipelineResponsetagsTypeDef(_ClientCreatePipelineResponsetagsTypeDef):
    """
    Type definition for `ClientCreatePipelineResponse` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef",
    {
        "pipeline": ClientCreatePipelineResponsepipelineTypeDef,
        "tags": List[ClientCreatePipelineResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    Type definition for `ClientCreatePipeline` `Response`

    Represents the output of a ``CreatePipeline`` action.

    - **pipeline** *(dict) --*

      Represents the structure of actions and stages to be performed in the pipeline.

      - **name** *(string) --*

        The name of the action to be performed.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
        no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

      - **artifactStore** *(dict) --*

        Represents information about the Amazon S3 bucket where artifacts are stored for the
        pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - **type** *(string) --*

          The type of the artifact store, such as S3.

        - **location** *(string) --*

          The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
          name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
          artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
          bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

        - **encryptionKey** *(dict) --*

          The encryption key used to encrypt the data in the artifact store, such as an AWS Key
          Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
          used.

          - **id** *(string) --*

            The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
            ARN, or the alias ARN.

            .. note::

              Aliases are recognized only in the account that created the customer master key
              (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
              the key.

          - **type** *(string) --*

            The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
            creating or updating a pipeline, the value must be set to 'KMS'.

      - **artifactStores** *(dict) --*

        A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
        an artifact store for the pipeline Region and for each cross-region action in the pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - *(string) --*

          - *(dict) --*

            The Amazon S3 bucket where artifacts for the pipeline are stored.

            .. note::

              You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
              you cannot use both. If you create a cross-region action in your pipeline, you must
              use ``artifactStores`` .

            - **type** *(string) --*

              The type of the artifact store, such as S3.

            - **location** *(string) --*

              The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
              the name of an S3 bucket but not a folder in the bucket. A folder to contain the
              pipeline artifacts is created for you based on the name of the pipeline. You can use
              any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
              artifacts.

            - **encryptionKey** *(dict) --*

              The encryption key used to encrypt the data in the artifact store, such as an AWS Key
              Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
              is used.

              - **id** *(string) --*

                The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
                key ARN, or the alias ARN.

                .. note::

                  Aliases are recognized only in the account that created the customer master key
                  (CMK). For cross-account actions, you can only use the key ID or key ARN to
                  identify the key.

              - **type** *(string) --*

                The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
                When creating or updating a pipeline, the value must be set to 'KMS'.

      - **stages** *(list) --*

        The stage in which to perform the action.

        - *(dict) --*

          Represents information about a stage and its definition.

          - **name** *(string) --*

            The name of the stage.

          - **blockers** *(list) --*

            Reserved for future use.

            - *(dict) --*

              Reserved for future use.

              - **name** *(string) --*

                Reserved for future use.

              - **type** *(string) --*

                Reserved for future use.

          - **actions** *(list) --*

            The actions included in a stage.

            - *(dict) --*

              Represents information about an action declaration.

              - **name** *(string) --*

                The action declaration's name.

              - **actionTypeId** *(dict) --*

                Specifies the action type and the provider of the action.

                - **category** *(string) --*

                  A category defines what kind of action can be taken in the stage, and constrains
                  the provider type for the action. Valid categories are limited to one of the
                  following values.

                - **owner** *(string) --*

                  The creator of the action being called.

                - **provider** *(string) --*

                  The provider of the service being called by the action. Valid providers are
                  determined by the action category. For example, an action in the Deploy category
                  type might have a provider of AWS CodeDeploy, which would be specified as
                  CodeDeploy. For more information, see `Valid Action Types and Providers in
                  CodePipeline
                  <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                  .

                - **version** *(string) --*

                  A string that describes the action version.

              - **runOrder** *(integer) --*

                The order in which actions are run.

              - **configuration** *(dict) --*

                The action's configuration. These are key-value pairs that specify input values for
                an action. For more information, see `Action Structure Requirements in CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
                . For the list of configuration properties for the AWS CloudFormation action type
                in CodePipeline, see `Configuration Properties Reference
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
                in the *AWS CloudFormation User Guide* . For template snippets with examples, see
                `Using Parameter Override Functions with CodePipeline Pipelines
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
                in the *AWS CloudFormation User Guide* .

                The values can be represented in either JSON or YAML format. For example, the JSON
                configuration item format is as follows:

                 *JSON:*

                 ``"Configuration" : { Key : Value },``

                - *(string) --*

                  - *(string) --*

              - **outputArtifacts** *(list) --*

                The name or ID of the result of the action declaration, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about the output of an action.

                  - **name** *(string) --*

                    The name of the output of an artifact, such as "My App".

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

                    Output artifact names must be unique within a pipeline.

              - **inputArtifacts** *(list) --*

                The name or ID of the artifact consumed by the action, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about an artifact to be worked on, such as a test or build
                  artifact.

                  - **name** *(string) --*

                    The name of the artifact to be worked on (for example, "My App").

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

              - **roleArn** *(string) --*

                The ARN of the IAM service role that performs the declared action. This is assumed
                through the roleArn for the pipeline.

              - **region** *(string) --*

                The action declaration's AWS Region, such as us-east-1.

              - **namespace** *(string) --*

                The variable namespace associated with the action. All variables produced as output
                by this action fall under this namespace.

      - **version** *(integer) --*

        The version number of the pipeline. A new pipeline always has a version number of 1. This
        number is incremented when a pipeline is updated.

    - **tags** *(list) --*

      Specifies the tags applied to the pipeline.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
)


class ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef(
    _ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelineartifactStore` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

    - **id** *(string) --* **[REQUIRED]**

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
      or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key (CMK).
        For cross-account actions, you can only use the key ID or key ARN to identify the key.

    - **type** *(string) --* **[REQUIRED]**

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_RequiredClientCreatePipelinepipelineartifactStoreTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineartifactStoreTypeDef",
    {"type": str, "location": str},
)
_OptionalClientCreatePipelinepipelineartifactStoreTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineartifactStoreTypeDef",
    {"encryptionKey": ClientCreatePipelinepipelineartifactStoreencryptionKeyTypeDef},
    total=False,
)


class ClientCreatePipelinepipelineartifactStoreTypeDef(
    _RequiredClientCreatePipelinepipelineartifactStoreTypeDef,
    _OptionalClientCreatePipelinepipelineartifactStoreTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipeline` `artifactStore`

    Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --* **[REQUIRED]**

      The type of the artifact store, such as S3.

    - **location** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name
      of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is
      created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the
      same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

      - **id** *(string) --* **[REQUIRED]**

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
        or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key (CMK).
          For cross-account actions, you can only use the key ID or key ARN to identify the key.

      - **type** *(string) --* **[REQUIRED]**

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
)


class ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef(
    _ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelineartifactStores` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
    used.

    - **id** *(string) --* **[REQUIRED]**

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --* **[REQUIRED]**

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_RequiredClientCreatePipelinepipelineartifactStoresTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineartifactStoresTypeDef",
    {"type": str, "location": str},
)
_OptionalClientCreatePipelinepipelineartifactStoresTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineartifactStoresTypeDef",
    {"encryptionKey": ClientCreatePipelinepipelineartifactStoresencryptionKeyTypeDef},
    total=False,
)


class ClientCreatePipelinepipelineartifactStoresTypeDef(
    _RequiredClientCreatePipelinepipelineartifactStoresTypeDef,
    _OptionalClientCreatePipelinepipelineartifactStoresTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipeline` `artifactStores`

    The Amazon S3 bucket where artifacts for the pipeline are stored.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --* **[REQUIRED]**

      The type of the artifact store, such as S3.

    - **location** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
      name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
      artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
      bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
      used.

      - **id** *(string) --* **[REQUIRED]**

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --* **[REQUIRED]**

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
)


class ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef(
    _ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelinestagesactions` `actionTypeId`

    Specifies the action type and the provider of the action.

    - **category** *(string) --* **[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --* **[REQUIRED]**

      The creator of the action being called.

    - **provider** *(string) --* **[REQUIRED]**

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category type
      might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
      more information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --* **[REQUIRED]**

      A string that describes the action version.
    """


_ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef", {"name": str}
)


class ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef(
    _ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelinestagesactions` `inputArtifacts`

    Represents information about an artifact to be worked on, such as a test or build
    artifact.

    - **name** *(string) --* **[REQUIRED]**

      The name of the artifact to be worked on (for example, "My App").

      The input artifact of an action must exactly match the output artifact declared in
      a preceding action, but the input artifact does not have to be the next action in
      strict sequence from the action that provided the output artifact. Actions in
      parallel can declare different output artifacts, which are in turn consumed by
      different following actions.
    """


_ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef", {"name": str}
)


class ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelinestagesactions` `outputArtifacts`

    Represents information about the output of an action.

    - **name** *(string) --* **[REQUIRED]**

      The name of the output of an artifact, such as "My App".

      The input artifact of an action must exactly match the output artifact declared in
      a preceding action, but the input artifact does not have to be the next action in
      strict sequence from the action that provided the output artifact. Actions in
      parallel can declare different output artifacts, which are in turn consumed by
      different following actions.

      Output artifact names must be unique within a pipeline.
    """


_RequiredClientCreatePipelinepipelinestagesactionsTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientCreatePipelinepipelinestagesactionsactionTypeIdTypeDef,
    },
)
_OptionalClientCreatePipelinepipelinestagesactionsTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelinestagesactionsTypeDef",
    {
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientCreatePipelinepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientCreatePipelinepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ClientCreatePipelinepipelinestagesactionsTypeDef(
    _RequiredClientCreatePipelinepipelinestagesactionsTypeDef,
    _OptionalClientCreatePipelinepipelinestagesactionsTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipelinestages` `actions`

    Represents information about an action declaration.

    - **name** *(string) --* **[REQUIRED]**

      The action declaration's name.

    - **actionTypeId** *(dict) --* **[REQUIRED]**

      Specifies the action type and the provider of the action.

      - **category** *(string) --* **[REQUIRED]**

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --* **[REQUIRED]**

        The creator of the action being called.

      - **provider** *(string) --* **[REQUIRED]**

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category type
        might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
        more information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --* **[REQUIRED]**

        A string that describes the action version.

    - **runOrder** *(integer) --*

      The order in which actions are run.

    - **configuration** *(dict) --*

      The action's configuration. These are key-value pairs that specify input values for an
      action. For more information, see `Action Structure Requirements in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      . For the list of configuration properties for the AWS CloudFormation action type in
      CodePipeline, see `Configuration Properties Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
      in the *AWS CloudFormation User Guide* . For template snippets with examples, see
      `Using Parameter Override Functions with CodePipeline Pipelines
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
      in the *AWS CloudFormation User Guide* .

      The values can be represented in either JSON or YAML format. For example, the JSON
      configuration item format is as follows:

       *JSON:*

       ``"Configuration" : { Key : Value },``

      - *(string) --*

        - *(string) --*

    - **outputArtifacts** *(list) --*

      The name or ID of the result of the action declaration, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about the output of an action.

        - **name** *(string) --* **[REQUIRED]**

          The name of the output of an artifact, such as "My App".

          The input artifact of an action must exactly match the output artifact declared in
          a preceding action, but the input artifact does not have to be the next action in
          strict sequence from the action that provided the output artifact. Actions in
          parallel can declare different output artifacts, which are in turn consumed by
          different following actions.

          Output artifact names must be unique within a pipeline.

    - **inputArtifacts** *(list) --*

      The name or ID of the artifact consumed by the action, such as a test or build artifact.

      - *(dict) --*

        Represents information about an artifact to be worked on, such as a test or build
        artifact.

        - **name** *(string) --* **[REQUIRED]**

          The name of the artifact to be worked on (for example, "My App").

          The input artifact of an action must exactly match the output artifact declared in
          a preceding action, but the input artifact does not have to be the next action in
          strict sequence from the action that provided the output artifact. Actions in
          parallel can declare different output artifacts, which are in turn consumed by
          different following actions.

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The action declaration's AWS Region, such as us-east-1.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output by
      this action fall under this namespace.
    """


_ClientCreatePipelinepipelinestagesblockersTypeDef = TypedDict(
    "_ClientCreatePipelinepipelinestagesblockersTypeDef", {"name": str, "type": str}
)


class ClientCreatePipelinepipelinestagesblockersTypeDef(
    _ClientCreatePipelinepipelinestagesblockersTypeDef
):
    """
    Type definition for `ClientCreatePipelinepipelinestages` `blockers`

    Reserved for future use.

    - **name** *(string) --* **[REQUIRED]**

      Reserved for future use.

    - **type** *(string) --* **[REQUIRED]**

      Reserved for future use.
    """


_RequiredClientCreatePipelinepipelinestagesTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelinestagesTypeDef",
    {"name": str, "actions": List[ClientCreatePipelinepipelinestagesactionsTypeDef]},
)
_OptionalClientCreatePipelinepipelinestagesTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelinestagesTypeDef",
    {"blockers": List[ClientCreatePipelinepipelinestagesblockersTypeDef]},
    total=False,
)


class ClientCreatePipelinepipelinestagesTypeDef(
    _RequiredClientCreatePipelinepipelinestagesTypeDef,
    _OptionalClientCreatePipelinepipelinestagesTypeDef,
):
    """
    Type definition for `ClientCreatePipelinepipeline` `stages`

    Represents information about a stage and its definition.

    - **name** *(string) --* **[REQUIRED]**

      The name of the stage.

    - **blockers** *(list) --*

      Reserved for future use.

      - *(dict) --*

        Reserved for future use.

        - **name** *(string) --* **[REQUIRED]**

          Reserved for future use.

        - **type** *(string) --* **[REQUIRED]**

          Reserved for future use.

    - **actions** *(list) --* **[REQUIRED]**

      The actions included in a stage.

      - *(dict) --*

        Represents information about an action declaration.

        - **name** *(string) --* **[REQUIRED]**

          The action declaration's name.

        - **actionTypeId** *(dict) --* **[REQUIRED]**

          Specifies the action type and the provider of the action.

          - **category** *(string) --* **[REQUIRED]**

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --* **[REQUIRED]**

            The creator of the action being called.

          - **provider** *(string) --* **[REQUIRED]**

            The provider of the service being called by the action. Valid providers are
            determined by the action category. For example, an action in the Deploy category type
            might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
            more information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --* **[REQUIRED]**

            A string that describes the action version.

        - **runOrder** *(integer) --*

          The order in which actions are run.

        - **configuration** *(dict) --*

          The action's configuration. These are key-value pairs that specify input values for an
          action. For more information, see `Action Structure Requirements in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          . For the list of configuration properties for the AWS CloudFormation action type in
          CodePipeline, see `Configuration Properties Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
          in the *AWS CloudFormation User Guide* . For template snippets with examples, see
          `Using Parameter Override Functions with CodePipeline Pipelines
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
          in the *AWS CloudFormation User Guide* .

          The values can be represented in either JSON or YAML format. For example, the JSON
          configuration item format is as follows:

           *JSON:*

           ``"Configuration" : { Key : Value },``

          - *(string) --*

            - *(string) --*

        - **outputArtifacts** *(list) --*

          The name or ID of the result of the action declaration, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about the output of an action.

            - **name** *(string) --* **[REQUIRED]**

              The name of the output of an artifact, such as "My App".

              The input artifact of an action must exactly match the output artifact declared in
              a preceding action, but the input artifact does not have to be the next action in
              strict sequence from the action that provided the output artifact. Actions in
              parallel can declare different output artifacts, which are in turn consumed by
              different following actions.

              Output artifact names must be unique within a pipeline.

        - **inputArtifacts** *(list) --*

          The name or ID of the artifact consumed by the action, such as a test or build artifact.

          - *(dict) --*

            Represents information about an artifact to be worked on, such as a test or build
            artifact.

            - **name** *(string) --* **[REQUIRED]**

              The name of the artifact to be worked on (for example, "My App").

              The input artifact of an action must exactly match the output artifact declared in
              a preceding action, but the input artifact does not have to be the next action in
              strict sequence from the action that provided the output artifact. Actions in
              parallel can declare different output artifacts, which are in turn consumed by
              different following actions.

        - **roleArn** *(string) --*

          The ARN of the IAM service role that performs the declared action. This is assumed
          through the roleArn for the pipeline.

        - **region** *(string) --*

          The action declaration's AWS Region, such as us-east-1.

        - **namespace** *(string) --*

          The variable namespace associated with the action. All variables produced as output by
          this action fall under this namespace.
    """


_RequiredClientCreatePipelinepipelineTypeDef = TypedDict(
    "_RequiredClientCreatePipelinepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": List[ClientCreatePipelinepipelinestagesTypeDef],
    },
)
_OptionalClientCreatePipelinepipelineTypeDef = TypedDict(
    "_OptionalClientCreatePipelinepipelineTypeDef",
    {
        "artifactStore": ClientCreatePipelinepipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientCreatePipelinepipelineartifactStoresTypeDef],
        "version": int,
    },
    total=False,
)


class ClientCreatePipelinepipelineTypeDef(
    _RequiredClientCreatePipelinepipelineTypeDef,
    _OptionalClientCreatePipelinepipelineTypeDef,
):
    """
    Type definition for `ClientCreatePipeline` `pipeline`

    Represents the structure of actions and stages to be performed in the pipeline.

    - **name** *(string) --* **[REQUIRED]**

      The name of the action to be performed.

    - **roleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no
      ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

    - **artifactStore** *(dict) --*

      Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - **type** *(string) --* **[REQUIRED]**

        The type of the artifact store, such as S3.

      - **location** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name
        of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is
        created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the
        same AWS Region as the pipeline to store your pipeline artifacts.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt the data in the artifact store, such as an AWS Key
        Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

        - **id** *(string) --* **[REQUIRED]**

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
          or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key (CMK).
            For cross-account actions, you can only use the key ID or key ARN to identify the key.

        - **type** *(string) --* **[REQUIRED]**

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **artifactStores** *(dict) --*

      A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be an
      artifact store for the pipeline Region and for each cross-region action in the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - *(string) --*

        - *(dict) --*

          The Amazon S3 bucket where artifacts for the pipeline are stored.

          .. note::

            You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
            cannot use both. If you create a cross-region action in your pipeline, you must use
            ``artifactStores`` .

          - **type** *(string) --* **[REQUIRED]**

            The type of the artifact store, such as S3.

          - **location** *(string) --* **[REQUIRED]**

            The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
            name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
            artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
            bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

          - **encryptionKey** *(dict) --*

            The encryption key used to encrypt the data in the artifact store, such as an AWS Key
            Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
            used.

            - **id** *(string) --* **[REQUIRED]**

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
              ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
                the key.

            - **type** *(string) --* **[REQUIRED]**

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
              creating or updating a pipeline, the value must be set to 'KMS'.

    - **stages** *(list) --* **[REQUIRED]**

      The stage in which to perform the action.

      - *(dict) --*

        Represents information about a stage and its definition.

        - **name** *(string) --* **[REQUIRED]**

          The name of the stage.

        - **blockers** *(list) --*

          Reserved for future use.

          - *(dict) --*

            Reserved for future use.

            - **name** *(string) --* **[REQUIRED]**

              Reserved for future use.

            - **type** *(string) --* **[REQUIRED]**

              Reserved for future use.

        - **actions** *(list) --* **[REQUIRED]**

          The actions included in a stage.

          - *(dict) --*

            Represents information about an action declaration.

            - **name** *(string) --* **[REQUIRED]**

              The action declaration's name.

            - **actionTypeId** *(dict) --* **[REQUIRED]**

              Specifies the action type and the provider of the action.

              - **category** *(string) --* **[REQUIRED]**

                A category defines what kind of action can be taken in the stage, and constrains the
                provider type for the action. Valid categories are limited to one of the following
                values.

              - **owner** *(string) --* **[REQUIRED]**

                The creator of the action being called.

              - **provider** *(string) --* **[REQUIRED]**

                The provider of the service being called by the action. Valid providers are
                determined by the action category. For example, an action in the Deploy category type
                might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
                more information, see `Valid Action Types and Providers in CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                .

              - **version** *(string) --* **[REQUIRED]**

                A string that describes the action version.

            - **runOrder** *(integer) --*

              The order in which actions are run.

            - **configuration** *(dict) --*

              The action's configuration. These are key-value pairs that specify input values for an
              action. For more information, see `Action Structure Requirements in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              . For the list of configuration properties for the AWS CloudFormation action type in
              CodePipeline, see `Configuration Properties Reference
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
              in the *AWS CloudFormation User Guide* . For template snippets with examples, see
              `Using Parameter Override Functions with CodePipeline Pipelines
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
              in the *AWS CloudFormation User Guide* .

              The values can be represented in either JSON or YAML format. For example, the JSON
              configuration item format is as follows:

               *JSON:*

               ``"Configuration" : { Key : Value },``

              - *(string) --*

                - *(string) --*

            - **outputArtifacts** *(list) --*

              The name or ID of the result of the action declaration, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about the output of an action.

                - **name** *(string) --* **[REQUIRED]**

                  The name of the output of an artifact, such as "My App".

                  The input artifact of an action must exactly match the output artifact declared in
                  a preceding action, but the input artifact does not have to be the next action in
                  strict sequence from the action that provided the output artifact. Actions in
                  parallel can declare different output artifacts, which are in turn consumed by
                  different following actions.

                  Output artifact names must be unique within a pipeline.

            - **inputArtifacts** *(list) --*

              The name or ID of the artifact consumed by the action, such as a test or build artifact.

              - *(dict) --*

                Represents information about an artifact to be worked on, such as a test or build
                artifact.

                - **name** *(string) --* **[REQUIRED]**

                  The name of the artifact to be worked on (for example, "My App").

                  The input artifact of an action must exactly match the output artifact declared in
                  a preceding action, but the input artifact does not have to be the next action in
                  strict sequence from the action that provided the output artifact. Actions in
                  parallel can declare different output artifacts, which are in turn consumed by
                  different following actions.

            - **roleArn** *(string) --*

              The ARN of the IAM service role that performs the declared action. This is assumed
              through the roleArn for the pipeline.

            - **region** *(string) --*

              The action declaration's AWS Region, such as us-east-1.

            - **namespace** *(string) --*

              The variable namespace associated with the action. All variables produced as output by
              this action fall under this namespace.

    - **version** *(integer) --*

      The version number of the pipeline. A new pipeline always has a version number of 1. This
      number is incremented when a pipeline is updated.
    """


_ClientCreatePipelinetagsTypeDef = TypedDict(
    "_ClientCreatePipelinetagsTypeDef", {"key": str, "value": str}
)


class ClientCreatePipelinetagsTypeDef(_ClientCreatePipelinetagsTypeDef):
    """
    Type definition for `ClientCreatePipeline` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `actionConfiguration`

    Represents information about an action configuration.

    - **configuration** *(dict) --*

      The configuration data for the action.

      - *(string) --*

        - *(string) --*
    """


_ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are determined
      by the action category. For example, an action in the Deploy category type might have a
      provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
      information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `artifactCredentials`

    Represents an AWS session credentials object. These credentials are temporary credentials
    that are issued by AWS Secure Token Service (STS). They can be used to access input and
    output artifacts in the Amazon S3 bucket used to store artifacts for the pipeline in AWS
    CodePipeline.

    - **accessKeyId** *(string) --*

      The access key for the session.

    - **secretAccessKey** *(string) --*

      The secret access key for the session.

    - **sessionToken** *(string) --*

      The token for the session.
    """


_ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `encryptionKey`

    Represents information about the key used to encrypt data in the artifact store, such as
    an AWS Key Management Service (AWS KMS) key.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdatainputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `inputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdataoutputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `outputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdatapipelineContext` `action`

    The context of an action to a job worker in the stage of a pipeline.

    - **name** *(string) --*

      The name of the action in the context of a job.

    - **actionExecutionId** *(string) --*

      The system-generated unique ID that corresponds to an action's execution.
    """


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdatapipelineContext` `stage`

    The stage of the pipeline.

    - **name** *(string) --*

      The name of the stage.
    """


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetailsdata` `pipelineContext`

    Represents information about a pipeline to a job worker.

    .. note::

      Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

    - **pipelineName** *(string) --*

      The name of the pipeline. This is a user-specified value. Pipeline names must be unique
      across all pipeline names under an Amazon Web Services account.

    - **stage** *(dict) --*

      The stage of the pipeline.

      - **name** *(string) --*

        The name of the stage.

    - **action** *(dict) --*

      The context of an action to a job worker in the stage of a pipeline.

      - **name** *(string) --*

        The name of the action in the context of a job.

      - **actionExecutionId** *(string) --*

        The system-generated unique ID that corresponds to an action's execution.

    - **pipelineArn** *(string) --*

      The Amazon Resource Name (ARN) of the pipeline.

    - **pipelineExecutionId** *(string) --*

      The execution ID of the pipeline.
    """


_ClientGetJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataTypeDef",
    {
        "actionTypeId": ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef,
        "pipelineContext": ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef,
        "inputArtifacts": List[
            ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
        ],
        "outputArtifacts": List[
            ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
        ],
        "artifactCredentials": ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponsejobDetails` `data`

    Represents other information about a job required for a job worker to complete the job.

    - **actionTypeId** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are determined
        by the action category. For example, an action in the Deploy category type might have a
        provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
        information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **actionConfiguration** *(dict) --*

      Represents information about an action configuration.

      - **configuration** *(dict) --*

        The configuration data for the action.

        - *(string) --*

          - *(string) --*

    - **pipelineContext** *(dict) --*

      Represents information about a pipeline to a job worker.

      .. note::

        Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

      - **pipelineName** *(string) --*

        The name of the pipeline. This is a user-specified value. Pipeline names must be unique
        across all pipeline names under an Amazon Web Services account.

      - **stage** *(dict) --*

        The stage of the pipeline.

        - **name** *(string) --*

          The name of the stage.

      - **action** *(dict) --*

        The context of an action to a job worker in the stage of a pipeline.

        - **name** *(string) --*

          The name of the action in the context of a job.

        - **actionExecutionId** *(string) --*

          The system-generated unique ID that corresponds to an action's execution.

      - **pipelineArn** *(string) --*

        The Amazon Resource Name (ARN) of the pipeline.

      - **pipelineExecutionId** *(string) --*

        The execution ID of the pipeline.

    - **inputArtifacts** *(list) --*

      The artifact supplied to the job.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **outputArtifacts** *(list) --*

      The output of the job.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **artifactCredentials** *(dict) --*

      Represents an AWS session credentials object. These credentials are temporary credentials
      that are issued by AWS Secure Token Service (STS). They can be used to access input and
      output artifacts in the Amazon S3 bucket used to store artifacts for the pipeline in AWS
      CodePipeline.

      - **accessKeyId** *(string) --*

        The access key for the session.

      - **secretAccessKey** *(string) --*

        The secret access key for the session.

      - **sessionToken** *(string) --*

        The token for the session.

    - **continuationToken** *(string) --*

      A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
      continue the job asynchronously.

    - **encryptionKey** *(dict) --*

      Represents information about the key used to encrypt data in the artifact store, such as
      an AWS Key Management Service (AWS KMS) key.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsTypeDef",
    {
        "id": str,
        "data": ClientGetJobDetailsResponsejobDetailsdataTypeDef,
        "accountId": str,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsTypeDef
):
    """
    Type definition for `ClientGetJobDetailsResponse` `jobDetails`

    The details of the job.

    .. note::

      If AWSSessionCredentials is used, a long-running job can call ``GetJobDetails`` again to
      obtain new credentials.

    - **id** *(string) --*

      The unique system-generated ID of the job.

    - **data** *(dict) --*

      Represents other information about a job required for a job worker to complete the job.

      - **actionTypeId** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following
          values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are determined
          by the action category. For example, an action in the Deploy category type might have a
          provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
          information, see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **actionConfiguration** *(dict) --*

        Represents information about an action configuration.

        - **configuration** *(dict) --*

          The configuration data for the action.

          - *(string) --*

            - *(string) --*

      - **pipelineContext** *(dict) --*

        Represents information about a pipeline to a job worker.

        .. note::

          Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

        - **pipelineName** *(string) --*

          The name of the pipeline. This is a user-specified value. Pipeline names must be unique
          across all pipeline names under an Amazon Web Services account.

        - **stage** *(dict) --*

          The stage of the pipeline.

          - **name** *(string) --*

            The name of the stage.

        - **action** *(dict) --*

          The context of an action to a job worker in the stage of a pipeline.

          - **name** *(string) --*

            The name of the action in the context of a job.

          - **actionExecutionId** *(string) --*

            The system-generated unique ID that corresponds to an action's execution.

        - **pipelineArn** *(string) --*

          The Amazon Resource Name (ARN) of the pipeline.

        - **pipelineExecutionId** *(string) --*

          The execution ID of the pipeline.

      - **inputArtifacts** *(list) --*

        The artifact supplied to the job.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **outputArtifacts** *(list) --*

        The output of the job.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **artifactCredentials** *(dict) --*

        Represents an AWS session credentials object. These credentials are temporary credentials
        that are issued by AWS Secure Token Service (STS). They can be used to access input and
        output artifacts in the Amazon S3 bucket used to store artifacts for the pipeline in AWS
        CodePipeline.

        - **accessKeyId** *(string) --*

          The access key for the session.

        - **secretAccessKey** *(string) --*

          The secret access key for the session.

        - **sessionToken** *(string) --*

          The token for the session.

      - **continuationToken** *(string) --*

        A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
        continue the job asynchronously.

      - **encryptionKey** *(dict) --*

        Represents information about the key used to encrypt data in the artifact store, such as
        an AWS Key Management Service (AWS KMS) key.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
            the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **accountId** *(string) --*

      The AWS account ID associated with the job.
    """


_ClientGetJobDetailsResponseTypeDef = TypedDict(
    "_ClientGetJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetJobDetailsResponsejobDetailsTypeDef},
    total=False,
)


class ClientGetJobDetailsResponseTypeDef(_ClientGetJobDetailsResponseTypeDef):
    """
    Type definition for `ClientGetJobDetails` `Response`

    Represents the output of a ``GetJobDetails`` action.

    - **jobDetails** *(dict) --*

      The details of the job.

      .. note::

        If AWSSessionCredentials is used, a long-running job can call ``GetJobDetails`` again to
        obtain new credentials.

      - **id** *(string) --*

        The unique system-generated ID of the job.

      - **data** *(dict) --*

        Represents other information about a job required for a job worker to complete the job.

        - **actionTypeId** *(dict) --*

          Represents information about an action type.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are determined
            by the action category. For example, an action in the Deploy category type might have a
            provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
            information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **actionConfiguration** *(dict) --*

          Represents information about an action configuration.

          - **configuration** *(dict) --*

            The configuration data for the action.

            - *(string) --*

              - *(string) --*

        - **pipelineContext** *(dict) --*

          Represents information about a pipeline to a job worker.

          .. note::

            Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

          - **pipelineName** *(string) --*

            The name of the pipeline. This is a user-specified value. Pipeline names must be unique
            across all pipeline names under an Amazon Web Services account.

          - **stage** *(dict) --*

            The stage of the pipeline.

            - **name** *(string) --*

              The name of the stage.

          - **action** *(dict) --*

            The context of an action to a job worker in the stage of a pipeline.

            - **name** *(string) --*

              The name of the action in the context of a job.

            - **actionExecutionId** *(string) --*

              The system-generated unique ID that corresponds to an action's execution.

          - **pipelineArn** *(string) --*

            The Amazon Resource Name (ARN) of the pipeline.

          - **pipelineExecutionId** *(string) --*

            The execution ID of the pipeline.

        - **inputArtifacts** *(list) --*

          The artifact supplied to the job.

          - *(dict) --*

            Represents information about an artifact that is worked on by actions in the pipeline.

            - **name** *(string) --*

              The artifact's name.

            - **revision** *(string) --*

              The artifact's revision ID. Depending on the type of object, this could be a commit
              ID (GitHub) or a revision ID (Amazon S3).

            - **location** *(dict) --*

              The location of an artifact.

              - **type** *(string) --*

                The type of artifact in the location.

              - **s3Location** *(dict) --*

                The Amazon S3 bucket that contains the artifact.

                - **bucketName** *(string) --*

                  The name of the Amazon S3 bucket.

                - **objectKey** *(string) --*

                  The key of the object in the Amazon S3 bucket, which uniquely identifies the
                  object in the bucket.

        - **outputArtifacts** *(list) --*

          The output of the job.

          - *(dict) --*

            Represents information about an artifact that is worked on by actions in the pipeline.

            - **name** *(string) --*

              The artifact's name.

            - **revision** *(string) --*

              The artifact's revision ID. Depending on the type of object, this could be a commit
              ID (GitHub) or a revision ID (Amazon S3).

            - **location** *(dict) --*

              The location of an artifact.

              - **type** *(string) --*

                The type of artifact in the location.

              - **s3Location** *(dict) --*

                The Amazon S3 bucket that contains the artifact.

                - **bucketName** *(string) --*

                  The name of the Amazon S3 bucket.

                - **objectKey** *(string) --*

                  The key of the object in the Amazon S3 bucket, which uniquely identifies the
                  object in the bucket.

        - **artifactCredentials** *(dict) --*

          Represents an AWS session credentials object. These credentials are temporary credentials
          that are issued by AWS Secure Token Service (STS). They can be used to access input and
          output artifacts in the Amazon S3 bucket used to store artifacts for the pipeline in AWS
          CodePipeline.

          - **accessKeyId** *(string) --*

            The access key for the session.

          - **secretAccessKey** *(string) --*

            The secret access key for the session.

          - **sessionToken** *(string) --*

            The token for the session.

        - **continuationToken** *(string) --*

          A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
          continue the job asynchronously.

        - **encryptionKey** *(dict) --*

          Represents information about the key used to encrypt data in the artifact store, such as
          an AWS Key Management Service (AWS KMS) key.

          - **id** *(string) --*

            The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
            ARN, or the alias ARN.

            .. note::

              Aliases are recognized only in the account that created the customer master key
              (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
              the key.

          - **type** *(string) --*

            The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
            creating or updating a pipeline, the value must be set to 'KMS'.

      - **accountId** *(string) --*

        The AWS account ID associated with the job.
    """


_ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef",
    {
        "name": str,
        "revisionId": str,
        "revisionChangeIdentifier": str,
        "revisionSummary": str,
        "created": datetime,
        "revisionUrl": str,
    },
    total=False,
)


class ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef(
    _ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef
):
    """
    Type definition for `ClientGetPipelineExecutionResponsepipelineExecution` `artifactRevisions`

    Represents revision details of an artifact.

    - **name** *(string) --*

      The name of an artifact. This name might be system-generated, such as "MyApp", or
      defined by the user when an action is created.

    - **revisionId** *(string) --*

      The revision ID of the artifact.

    - **revisionChangeIdentifier** *(string) --*

      An additional identifier for a revision, such as a commit date or, for artifacts stored
      in Amazon S3 buckets, the ETag value.

    - **revisionSummary** *(string) --*

      Summary information about the most recent revision of the artifact. For GitHub and AWS
      CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the
      user-provided content of a ``codepipeline-artifact-revision-summary`` key specified in
      the object metadata.

    - **created** *(datetime) --*

      The date and time when the most recent revision of the artifact was created, in
      timestamp format.

    - **revisionUrl** *(string) --*

      The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
      CodeCommit repositories, the commit ID is linked to a commit details page.
    """


_ClientGetPipelineExecutionResponsepipelineExecutionTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponsepipelineExecutionTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "pipelineExecutionId": str,
        "status": str,
        "artifactRevisions": List[
            ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef
        ],
    },
    total=False,
)


class ClientGetPipelineExecutionResponsepipelineExecutionTypeDef(
    _ClientGetPipelineExecutionResponsepipelineExecutionTypeDef
):
    """
    Type definition for `ClientGetPipelineExecutionResponse` `pipelineExecution`

    Represents information about the execution of a pipeline.

    - **pipelineName** *(string) --*

      The name of the pipeline that was executed.

    - **pipelineVersion** *(integer) --*

      The version number of the pipeline that was executed.

    - **pipelineExecutionId** *(string) --*

      The ID of the pipeline execution.

    - **status** *(string) --*

      The status of the pipeline execution.

      * InProgress: The pipeline execution is currently running.

      * Succeeded: The pipeline execution was completed successfully.

      * Superseded: While this pipeline execution was waiting for the next stage to be completed,
      a newer pipeline execution advanced and continued through the pipeline instead.

      * Failed: The pipeline execution was not completed successfully.

    - **artifactRevisions** *(list) --*

      A list of ``ArtifactRevision`` objects included in a pipeline execution.

      - *(dict) --*

        Represents revision details of an artifact.

        - **name** *(string) --*

          The name of an artifact. This name might be system-generated, such as "MyApp", or
          defined by the user when an action is created.

        - **revisionId** *(string) --*

          The revision ID of the artifact.

        - **revisionChangeIdentifier** *(string) --*

          An additional identifier for a revision, such as a commit date or, for artifacts stored
          in Amazon S3 buckets, the ETag value.

        - **revisionSummary** *(string) --*

          Summary information about the most recent revision of the artifact. For GitHub and AWS
          CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the
          user-provided content of a ``codepipeline-artifact-revision-summary`` key specified in
          the object metadata.

        - **created** *(datetime) --*

          The date and time when the most recent revision of the artifact was created, in
          timestamp format.

        - **revisionUrl** *(string) --*

          The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
          CodeCommit repositories, the commit ID is linked to a commit details page.
    """


_ClientGetPipelineExecutionResponseTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponseTypeDef",
    {"pipelineExecution": ClientGetPipelineExecutionResponsepipelineExecutionTypeDef},
    total=False,
)


class ClientGetPipelineExecutionResponseTypeDef(
    _ClientGetPipelineExecutionResponseTypeDef
):
    """
    Type definition for `ClientGetPipelineExecution` `Response`

    Represents the output of a ``GetPipelineExecution`` action.

    - **pipelineExecution** *(dict) --*

      Represents information about the execution of a pipeline.

      - **pipelineName** *(string) --*

        The name of the pipeline that was executed.

      - **pipelineVersion** *(integer) --*

        The version number of the pipeline that was executed.

      - **pipelineExecutionId** *(string) --*

        The ID of the pipeline execution.

      - **status** *(string) --*

        The status of the pipeline execution.

        * InProgress: The pipeline execution is currently running.

        * Succeeded: The pipeline execution was completed successfully.

        * Superseded: While this pipeline execution was waiting for the next stage to be completed,
        a newer pipeline execution advanced and continued through the pipeline instead.

        * Failed: The pipeline execution was not completed successfully.

      - **artifactRevisions** *(list) --*

        A list of ``ArtifactRevision`` objects included in a pipeline execution.

        - *(dict) --*

          Represents revision details of an artifact.

          - **name** *(string) --*

            The name of an artifact. This name might be system-generated, such as "MyApp", or
            defined by the user when an action is created.

          - **revisionId** *(string) --*

            The revision ID of the artifact.

          - **revisionChangeIdentifier** *(string) --*

            An additional identifier for a revision, such as a commit date or, for artifacts stored
            in Amazon S3 buckets, the ETag value.

          - **revisionSummary** *(string) --*

            Summary information about the most recent revision of the artifact. For GitHub and AWS
            CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the
            user-provided content of a ``codepipeline-artifact-revision-summary`` key specified in
            the object metadata.

          - **created** *(datetime) --*

            The date and time when the most recent revision of the artifact was created, in
            timestamp format.

          - **revisionUrl** *(string) --*

            The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
            CodeCommit repositories, the commit ID is linked to a commit details page.
    """


_ClientGetPipelineResponsemetadataTypeDef = TypedDict(
    "_ClientGetPipelineResponsemetadataTypeDef",
    {"pipelineArn": str, "created": datetime, "updated": datetime},
    total=False,
)


class ClientGetPipelineResponsemetadataTypeDef(
    _ClientGetPipelineResponsemetadataTypeDef
):
    """
    Type definition for `ClientGetPipelineResponse` `metadata`

    Represents the pipeline metadata information returned as part of the output of a
    ``GetPipeline`` action.

    - **pipelineArn** *(string) --*

      The Amazon Resource Name (ARN) of the pipeline.

    - **created** *(datetime) --*

      The date and time the pipeline was created, in timestamp format.

    - **updated** *(datetime) --*

      The date and time the pipeline was last updated, in timestamp format.
    """


_ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelineartifactStore` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
    used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetPipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoreTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoreTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipeline` `artifactStore`

    Represents information about the Amazon S3 bucket where artifacts are stored for the
    pipeline.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
      name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
      artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
      bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
      used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelineartifactStores` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
    is used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
      key ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to
        identify the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
      When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetPipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoresTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoresTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipeline` `artifactStores`

    The Amazon S3 bucket where artifacts for the pipeline are stored.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
      you cannot use both. If you create a cross-region action in your pipeline, you must
      use ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
      the name of an S3 bucket but not a folder in the bucket. A folder to contain the
      pipeline artifacts is created for you based on the name of the pipeline. You can use
      any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
      artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
      is used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
        key ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to
          identify the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
        When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelinestagesactions` `actionTypeId`

    Specifies the action type and the provider of the action.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains
      the provider type for the action. Valid categories are limited to one of the
      following values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category
      type might have a provider of AWS CodeDeploy, which would be specified as
      CodeDeploy. For more information, see `Valid Action Types and Providers in
      CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelinestagesactions` `inputArtifacts`

    Represents information about an artifact to be worked on, such as a test or build
    artifact.

    - **name** *(string) --*

      The name of the artifact to be worked on (for example, "My App").

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.
    """


_ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelinestagesactions` `outputArtifacts`

    Represents information about the output of an action.

    - **name** *(string) --*

      The name of the output of an artifact, such as "My App".

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.

      Output artifact names must be unique within a pipeline.
    """


_ClientGetPipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelinestages` `actions`

    Represents information about an action declaration.

    - **name** *(string) --*

      The action declaration's name.

    - **actionTypeId** *(dict) --*

      Specifies the action type and the provider of the action.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains
        the provider type for the action. Valid categories are limited to one of the
        following values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category
        type might have a provider of AWS CodeDeploy, which would be specified as
        CodeDeploy. For more information, see `Valid Action Types and Providers in
        CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **runOrder** *(integer) --*

      The order in which actions are run.

    - **configuration** *(dict) --*

      The action's configuration. These are key-value pairs that specify input values for
      an action. For more information, see `Action Structure Requirements in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      . For the list of configuration properties for the AWS CloudFormation action type
      in CodePipeline, see `Configuration Properties Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
      in the *AWS CloudFormation User Guide* . For template snippets with examples, see
      `Using Parameter Override Functions with CodePipeline Pipelines
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
      in the *AWS CloudFormation User Guide* .

      The values can be represented in either JSON or YAML format. For example, the JSON
      configuration item format is as follows:

       *JSON:*

       ``"Configuration" : { Key : Value },``

      - *(string) --*

        - *(string) --*

    - **outputArtifacts** *(list) --*

      The name or ID of the result of the action declaration, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about the output of an action.

        - **name** *(string) --*

          The name of the output of an artifact, such as "My App".

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

          Output artifact names must be unique within a pipeline.

    - **inputArtifacts** *(list) --*

      The name or ID of the artifact consumed by the action, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about an artifact to be worked on, such as a test or build
        artifact.

        - **name** *(string) --*

          The name of the artifact to be worked on (for example, "My App").

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The action declaration's AWS Region, such as us-east-1.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output
      by this action fall under this namespace.
    """


_ClientGetPipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesblockersTypeDef(
    _ClientGetPipelineResponsepipelinestagesblockersTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipelinestages` `blockers`

    Reserved for future use.

    - **name** *(string) --*

      Reserved for future use.

    - **type** *(string) --*

      Reserved for future use.
    """


_ClientGetPipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientGetPipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientGetPipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientGetPipelineResponsepipelinestagesTypeDef(
    _ClientGetPipelineResponsepipelinestagesTypeDef
):
    """
    Type definition for `ClientGetPipelineResponsepipeline` `stages`

    Represents information about a stage and its definition.

    - **name** *(string) --*

      The name of the stage.

    - **blockers** *(list) --*

      Reserved for future use.

      - *(dict) --*

        Reserved for future use.

        - **name** *(string) --*

          Reserved for future use.

        - **type** *(string) --*

          Reserved for future use.

    - **actions** *(list) --*

      The actions included in a stage.

      - *(dict) --*

        Represents information about an action declaration.

        - **name** *(string) --*

          The action declaration's name.

        - **actionTypeId** *(dict) --*

          Specifies the action type and the provider of the action.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains
            the provider type for the action. Valid categories are limited to one of the
            following values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are
            determined by the action category. For example, an action in the Deploy category
            type might have a provider of AWS CodeDeploy, which would be specified as
            CodeDeploy. For more information, see `Valid Action Types and Providers in
            CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **runOrder** *(integer) --*

          The order in which actions are run.

        - **configuration** *(dict) --*

          The action's configuration. These are key-value pairs that specify input values for
          an action. For more information, see `Action Structure Requirements in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          . For the list of configuration properties for the AWS CloudFormation action type
          in CodePipeline, see `Configuration Properties Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
          in the *AWS CloudFormation User Guide* . For template snippets with examples, see
          `Using Parameter Override Functions with CodePipeline Pipelines
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
          in the *AWS CloudFormation User Guide* .

          The values can be represented in either JSON or YAML format. For example, the JSON
          configuration item format is as follows:

           *JSON:*

           ``"Configuration" : { Key : Value },``

          - *(string) --*

            - *(string) --*

        - **outputArtifacts** *(list) --*

          The name or ID of the result of the action declaration, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about the output of an action.

            - **name** *(string) --*

              The name of the output of an artifact, such as "My App".

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

              Output artifact names must be unique within a pipeline.

        - **inputArtifacts** *(list) --*

          The name or ID of the artifact consumed by the action, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about an artifact to be worked on, such as a test or build
            artifact.

            - **name** *(string) --*

              The name of the artifact to be worked on (for example, "My App").

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

        - **roleArn** *(string) --*

          The ARN of the IAM service role that performs the declared action. This is assumed
          through the roleArn for the pipeline.

        - **region** *(string) --*

          The action declaration's AWS Region, such as us-east-1.

        - **namespace** *(string) --*

          The variable namespace associated with the action. All variables produced as output
          by this action fall under this namespace.
    """


_ClientGetPipelineResponsepipelineTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientGetPipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[
            str, ClientGetPipelineResponsepipelineartifactStoresTypeDef
        ],
        "stages": List[ClientGetPipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)


class ClientGetPipelineResponsepipelineTypeDef(
    _ClientGetPipelineResponsepipelineTypeDef
):
    """
    Type definition for `ClientGetPipelineResponse` `pipeline`

    Represents the structure of actions and stages to be performed in the pipeline.

    - **name** *(string) --*

      The name of the action to be performed.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
      no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

    - **artifactStore** *(dict) --*

      Represents information about the Amazon S3 bucket where artifacts are stored for the
      pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - **type** *(string) --*

        The type of the artifact store, such as S3.

      - **location** *(string) --*

        The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
        name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
        artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
        bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt the data in the artifact store, such as an AWS Key
        Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
        used.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
            the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **artifactStores** *(dict) --*

      A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
      an artifact store for the pipeline Region and for each cross-region action in the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - *(string) --*

        - *(dict) --*

          The Amazon S3 bucket where artifacts for the pipeline are stored.

          .. note::

            You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
            you cannot use both. If you create a cross-region action in your pipeline, you must
            use ``artifactStores`` .

          - **type** *(string) --*

            The type of the artifact store, such as S3.

          - **location** *(string) --*

            The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
            the name of an S3 bucket but not a folder in the bucket. A folder to contain the
            pipeline artifacts is created for you based on the name of the pipeline. You can use
            any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
            artifacts.

          - **encryptionKey** *(dict) --*

            The encryption key used to encrypt the data in the artifact store, such as an AWS Key
            Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
            is used.

            - **id** *(string) --*

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
              key ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to
                identify the key.

            - **type** *(string) --*

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
              When creating or updating a pipeline, the value must be set to 'KMS'.

    - **stages** *(list) --*

      The stage in which to perform the action.

      - *(dict) --*

        Represents information about a stage and its definition.

        - **name** *(string) --*

          The name of the stage.

        - **blockers** *(list) --*

          Reserved for future use.

          - *(dict) --*

            Reserved for future use.

            - **name** *(string) --*

              Reserved for future use.

            - **type** *(string) --*

              Reserved for future use.

        - **actions** *(list) --*

          The actions included in a stage.

          - *(dict) --*

            Represents information about an action declaration.

            - **name** *(string) --*

              The action declaration's name.

            - **actionTypeId** *(dict) --*

              Specifies the action type and the provider of the action.

              - **category** *(string) --*

                A category defines what kind of action can be taken in the stage, and constrains
                the provider type for the action. Valid categories are limited to one of the
                following values.

              - **owner** *(string) --*

                The creator of the action being called.

              - **provider** *(string) --*

                The provider of the service being called by the action. Valid providers are
                determined by the action category. For example, an action in the Deploy category
                type might have a provider of AWS CodeDeploy, which would be specified as
                CodeDeploy. For more information, see `Valid Action Types and Providers in
                CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                .

              - **version** *(string) --*

                A string that describes the action version.

            - **runOrder** *(integer) --*

              The order in which actions are run.

            - **configuration** *(dict) --*

              The action's configuration. These are key-value pairs that specify input values for
              an action. For more information, see `Action Structure Requirements in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              . For the list of configuration properties for the AWS CloudFormation action type
              in CodePipeline, see `Configuration Properties Reference
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
              in the *AWS CloudFormation User Guide* . For template snippets with examples, see
              `Using Parameter Override Functions with CodePipeline Pipelines
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
              in the *AWS CloudFormation User Guide* .

              The values can be represented in either JSON or YAML format. For example, the JSON
              configuration item format is as follows:

               *JSON:*

               ``"Configuration" : { Key : Value },``

              - *(string) --*

                - *(string) --*

            - **outputArtifacts** *(list) --*

              The name or ID of the result of the action declaration, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about the output of an action.

                - **name** *(string) --*

                  The name of the output of an artifact, such as "My App".

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

                  Output artifact names must be unique within a pipeline.

            - **inputArtifacts** *(list) --*

              The name or ID of the artifact consumed by the action, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about an artifact to be worked on, such as a test or build
                artifact.

                - **name** *(string) --*

                  The name of the artifact to be worked on (for example, "My App").

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

            - **roleArn** *(string) --*

              The ARN of the IAM service role that performs the declared action. This is assumed
              through the roleArn for the pipeline.

            - **region** *(string) --*

              The action declaration's AWS Region, such as us-east-1.

            - **namespace** *(string) --*

              The variable namespace associated with the action. All variables produced as output
              by this action fall under this namespace.

    - **version** *(integer) --*

      The version number of the pipeline. A new pipeline always has a version number of 1. This
      number is incremented when a pipeline is updated.
    """


_ClientGetPipelineResponseTypeDef = TypedDict(
    "_ClientGetPipelineResponseTypeDef",
    {
        "pipeline": ClientGetPipelineResponsepipelineTypeDef,
        "metadata": ClientGetPipelineResponsemetadataTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponseTypeDef(_ClientGetPipelineResponseTypeDef):
    """
    Type definition for `ClientGetPipeline` `Response`

    Represents the output of a ``GetPipeline`` action.

    - **pipeline** *(dict) --*

      Represents the structure of actions and stages to be performed in the pipeline.

      - **name** *(string) --*

        The name of the action to be performed.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
        no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

      - **artifactStore** *(dict) --*

        Represents information about the Amazon S3 bucket where artifacts are stored for the
        pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - **type** *(string) --*

          The type of the artifact store, such as S3.

        - **location** *(string) --*

          The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
          name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
          artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
          bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

        - **encryptionKey** *(dict) --*

          The encryption key used to encrypt the data in the artifact store, such as an AWS Key
          Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
          used.

          - **id** *(string) --*

            The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
            ARN, or the alias ARN.

            .. note::

              Aliases are recognized only in the account that created the customer master key
              (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
              the key.

          - **type** *(string) --*

            The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
            creating or updating a pipeline, the value must be set to 'KMS'.

      - **artifactStores** *(dict) --*

        A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
        an artifact store for the pipeline Region and for each cross-region action in the pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - *(string) --*

          - *(dict) --*

            The Amazon S3 bucket where artifacts for the pipeline are stored.

            .. note::

              You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
              you cannot use both. If you create a cross-region action in your pipeline, you must
              use ``artifactStores`` .

            - **type** *(string) --*

              The type of the artifact store, such as S3.

            - **location** *(string) --*

              The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
              the name of an S3 bucket but not a folder in the bucket. A folder to contain the
              pipeline artifacts is created for you based on the name of the pipeline. You can use
              any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
              artifacts.

            - **encryptionKey** *(dict) --*

              The encryption key used to encrypt the data in the artifact store, such as an AWS Key
              Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
              is used.

              - **id** *(string) --*

                The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
                key ARN, or the alias ARN.

                .. note::

                  Aliases are recognized only in the account that created the customer master key
                  (CMK). For cross-account actions, you can only use the key ID or key ARN to
                  identify the key.

              - **type** *(string) --*

                The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
                When creating or updating a pipeline, the value must be set to 'KMS'.

      - **stages** *(list) --*

        The stage in which to perform the action.

        - *(dict) --*

          Represents information about a stage and its definition.

          - **name** *(string) --*

            The name of the stage.

          - **blockers** *(list) --*

            Reserved for future use.

            - *(dict) --*

              Reserved for future use.

              - **name** *(string) --*

                Reserved for future use.

              - **type** *(string) --*

                Reserved for future use.

          - **actions** *(list) --*

            The actions included in a stage.

            - *(dict) --*

              Represents information about an action declaration.

              - **name** *(string) --*

                The action declaration's name.

              - **actionTypeId** *(dict) --*

                Specifies the action type and the provider of the action.

                - **category** *(string) --*

                  A category defines what kind of action can be taken in the stage, and constrains
                  the provider type for the action. Valid categories are limited to one of the
                  following values.

                - **owner** *(string) --*

                  The creator of the action being called.

                - **provider** *(string) --*

                  The provider of the service being called by the action. Valid providers are
                  determined by the action category. For example, an action in the Deploy category
                  type might have a provider of AWS CodeDeploy, which would be specified as
                  CodeDeploy. For more information, see `Valid Action Types and Providers in
                  CodePipeline
                  <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                  .

                - **version** *(string) --*

                  A string that describes the action version.

              - **runOrder** *(integer) --*

                The order in which actions are run.

              - **configuration** *(dict) --*

                The action's configuration. These are key-value pairs that specify input values for
                an action. For more information, see `Action Structure Requirements in CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
                . For the list of configuration properties for the AWS CloudFormation action type
                in CodePipeline, see `Configuration Properties Reference
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
                in the *AWS CloudFormation User Guide* . For template snippets with examples, see
                `Using Parameter Override Functions with CodePipeline Pipelines
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
                in the *AWS CloudFormation User Guide* .

                The values can be represented in either JSON or YAML format. For example, the JSON
                configuration item format is as follows:

                 *JSON:*

                 ``"Configuration" : { Key : Value },``

                - *(string) --*

                  - *(string) --*

              - **outputArtifacts** *(list) --*

                The name or ID of the result of the action declaration, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about the output of an action.

                  - **name** *(string) --*

                    The name of the output of an artifact, such as "My App".

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

                    Output artifact names must be unique within a pipeline.

              - **inputArtifacts** *(list) --*

                The name or ID of the artifact consumed by the action, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about an artifact to be worked on, such as a test or build
                  artifact.

                  - **name** *(string) --*

                    The name of the artifact to be worked on (for example, "My App").

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

              - **roleArn** *(string) --*

                The ARN of the IAM service role that performs the declared action. This is assumed
                through the roleArn for the pipeline.

              - **region** *(string) --*

                The action declaration's AWS Region, such as us-east-1.

              - **namespace** *(string) --*

                The variable namespace associated with the action. All variables produced as output
                by this action fall under this namespace.

      - **version** *(integer) --*

        The version number of the pipeline. A new pipeline always has a version number of 1. This
        number is incremented when a pipeline is updated.

    - **metadata** *(dict) --*

      Represents the pipeline metadata information returned as part of the output of a
      ``GetPipeline`` action.

      - **pipelineArn** *(string) --*

        The Amazon Resource Name (ARN) of the pipeline.

      - **created** *(datetime) --*

        The date and time the pipeline was created, in timestamp format.

      - **updated** *(datetime) --*

        The date and time the pipeline was last updated, in timestamp format.
    """


_ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef",
    {"revisionId": str, "revisionChangeId": str, "created": datetime},
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStatesactionStates` `currentRevision`

    Represents information about the version (or revision) of an action.

    - **revisionId** *(string) --*

      The system-generated unique ID that identifies the revision number of the action.

    - **revisionChangeId** *(string) --*

      The unique identifier of the change that set the state to this revision (for
      example, a deployment ID or timestamp).

    - **created** *(datetime) --*

      The date and time when the most recent version of the action was created, in
      timestamp format.
    """


_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStatesactionStateslatestExecution` `errorDetails`

    The details of an error returned by a URL external to AWS.

    - **code** *(string) --*

      The system ID or number code of the error.

    - **message** *(string) --*

      The text of the error message.
    """


_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef",
    {
        "status": str,
        "summary": str,
        "lastStatusChange": datetime,
        "token": str,
        "lastUpdatedBy": str,
        "externalExecutionId": str,
        "externalExecutionUrl": str,
        "percentComplete": int,
        "errorDetails": ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStatesactionStates` `latestExecution`

    Represents information about the run of an action.

    - **status** *(string) --*

      The status of the action, or for a completed action, the last status of the action.

    - **summary** *(string) --*

      A summary of the run of the action.

    - **lastStatusChange** *(datetime) --*

      The last status change of the action.

    - **token** *(string) --*

      The system-generated token used to identify a unique approval request. The token
      for each open approval request can be obtained using the ``GetPipelineState``
      command. It is used to validate that the approval request corresponding to this
      token is still valid.

    - **lastUpdatedBy** *(string) --*

      The ARN of the user who last changed the pipeline.

    - **externalExecutionId** *(string) --*

      The external ID of the run of the action.

    - **externalExecutionUrl** *(string) --*

      The URL of a resource external to AWS that is used when running the action (for
      example, an external repository URL).

    - **percentComplete** *(integer) --*

      A percentage of completeness of the action as it runs.

    - **errorDetails** *(dict) --*

      The details of an error returned by a URL external to AWS.

      - **code** *(string) --*

        The system ID or number code of the error.

      - **message** *(string) --*

        The text of the error message.
    """


_ClientGetPipelineStateResponsestageStatesactionStatesTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStatesTypeDef",
    {
        "actionName": str,
        "currentRevision": ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef,
        "latestExecution": ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef,
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStatesTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStatesTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStates` `actionStates`

    Represents information about the state of an action.

    - **actionName** *(string) --*

      The name of the action.

    - **currentRevision** *(dict) --*

      Represents information about the version (or revision) of an action.

      - **revisionId** *(string) --*

        The system-generated unique ID that identifies the revision number of the action.

      - **revisionChangeId** *(string) --*

        The unique identifier of the change that set the state to this revision (for
        example, a deployment ID or timestamp).

      - **created** *(datetime) --*

        The date and time when the most recent version of the action was created, in
        timestamp format.

    - **latestExecution** *(dict) --*

      Represents information about the run of an action.

      - **status** *(string) --*

        The status of the action, or for a completed action, the last status of the action.

      - **summary** *(string) --*

        A summary of the run of the action.

      - **lastStatusChange** *(datetime) --*

        The last status change of the action.

      - **token** *(string) --*

        The system-generated token used to identify a unique approval request. The token
        for each open approval request can be obtained using the ``GetPipelineState``
        command. It is used to validate that the approval request corresponding to this
        token is still valid.

      - **lastUpdatedBy** *(string) --*

        The ARN of the user who last changed the pipeline.

      - **externalExecutionId** *(string) --*

        The external ID of the run of the action.

      - **externalExecutionUrl** *(string) --*

        The URL of a resource external to AWS that is used when running the action (for
        example, an external repository URL).

      - **percentComplete** *(integer) --*

        A percentage of completeness of the action as it runs.

      - **errorDetails** *(dict) --*

        The details of an error returned by a URL external to AWS.

        - **code** *(string) --*

          The system ID or number code of the error.

        - **message** *(string) --*

          The text of the error message.

    - **entityUrl** *(string) --*

      A URL link for more information about the state of the action, such as a deployment
      group details page.

    - **revisionUrl** *(string) --*

      A URL link for more information about the revision, such as a commit details page.
    """


_ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef",
    {
        "enabled": bool,
        "lastChangedBy": str,
        "lastChangedAt": datetime,
        "disabledReason": str,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef(
    _ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStates` `inboundTransitionState`

    The state of the inbound transition, which is either enabled or disabled.

    - **enabled** *(boolean) --*

      Whether the transition between stages is enabled (true) or disabled (false).

    - **lastChangedBy** *(string) --*

      The ID of the user who last changed the transition state.

    - **lastChangedAt** *(datetime) --*

      The timestamp when the transition state was last changed.

    - **disabledReason** *(string) --*

      The user-specified reason why the transition between two stages of a pipeline was
      disabled.
    """


_ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef",
    {"pipelineExecutionId": str, "status": str},
    total=False,
)


class ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef(
    _ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponsestageStates` `latestExecution`

    Information about the latest execution in the stage, including its ID and status.

    - **pipelineExecutionId** *(string) --*

      The ID of the pipeline execution associated with the stage.

    - **status** *(string) --*

      The status of the stage, or for a completed stage, the last status of the stage.
    """


_ClientGetPipelineStateResponsestageStatesTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesTypeDef",
    {
        "stageName": str,
        "inboundTransitionState": ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef,
        "actionStates": List[
            ClientGetPipelineStateResponsestageStatesactionStatesTypeDef
        ],
        "latestExecution": ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesTypeDef(
    _ClientGetPipelineStateResponsestageStatesTypeDef
):
    """
    Type definition for `ClientGetPipelineStateResponse` `stageStates`

    Represents information about the state of the stage.

    - **stageName** *(string) --*

      The name of the stage.

    - **inboundTransitionState** *(dict) --*

      The state of the inbound transition, which is either enabled or disabled.

      - **enabled** *(boolean) --*

        Whether the transition between stages is enabled (true) or disabled (false).

      - **lastChangedBy** *(string) --*

        The ID of the user who last changed the transition state.

      - **lastChangedAt** *(datetime) --*

        The timestamp when the transition state was last changed.

      - **disabledReason** *(string) --*

        The user-specified reason why the transition between two stages of a pipeline was
        disabled.

    - **actionStates** *(list) --*

      The state of the stage.

      - *(dict) --*

        Represents information about the state of an action.

        - **actionName** *(string) --*

          The name of the action.

        - **currentRevision** *(dict) --*

          Represents information about the version (or revision) of an action.

          - **revisionId** *(string) --*

            The system-generated unique ID that identifies the revision number of the action.

          - **revisionChangeId** *(string) --*

            The unique identifier of the change that set the state to this revision (for
            example, a deployment ID or timestamp).

          - **created** *(datetime) --*

            The date and time when the most recent version of the action was created, in
            timestamp format.

        - **latestExecution** *(dict) --*

          Represents information about the run of an action.

          - **status** *(string) --*

            The status of the action, or for a completed action, the last status of the action.

          - **summary** *(string) --*

            A summary of the run of the action.

          - **lastStatusChange** *(datetime) --*

            The last status change of the action.

          - **token** *(string) --*

            The system-generated token used to identify a unique approval request. The token
            for each open approval request can be obtained using the ``GetPipelineState``
            command. It is used to validate that the approval request corresponding to this
            token is still valid.

          - **lastUpdatedBy** *(string) --*

            The ARN of the user who last changed the pipeline.

          - **externalExecutionId** *(string) --*

            The external ID of the run of the action.

          - **externalExecutionUrl** *(string) --*

            The URL of a resource external to AWS that is used when running the action (for
            example, an external repository URL).

          - **percentComplete** *(integer) --*

            A percentage of completeness of the action as it runs.

          - **errorDetails** *(dict) --*

            The details of an error returned by a URL external to AWS.

            - **code** *(string) --*

              The system ID or number code of the error.

            - **message** *(string) --*

              The text of the error message.

        - **entityUrl** *(string) --*

          A URL link for more information about the state of the action, such as a deployment
          group details page.

        - **revisionUrl** *(string) --*

          A URL link for more information about the revision, such as a commit details page.

    - **latestExecution** *(dict) --*

      Information about the latest execution in the stage, including its ID and status.

      - **pipelineExecutionId** *(string) --*

        The ID of the pipeline execution associated with the stage.

      - **status** *(string) --*

        The status of the stage, or for a completed stage, the last status of the stage.
    """


_ClientGetPipelineStateResponseTypeDef = TypedDict(
    "_ClientGetPipelineStateResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List[ClientGetPipelineStateResponsestageStatesTypeDef],
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)


class ClientGetPipelineStateResponseTypeDef(_ClientGetPipelineStateResponseTypeDef):
    """
    Type definition for `ClientGetPipelineState` `Response`

    Represents the output of a ``GetPipelineState`` action.

    - **pipelineName** *(string) --*

      The name of the pipeline for which you want to get the state.

    - **pipelineVersion** *(integer) --*

      The version number of the pipeline.

      .. note::

        A newly created pipeline is always assigned a version number of ``1`` .

    - **stageStates** *(list) --*

      A list of the pipeline stage output information, including stage name, state, most recent run
      details, whether the stage is disabled, and other data.

      - *(dict) --*

        Represents information about the state of the stage.

        - **stageName** *(string) --*

          The name of the stage.

        - **inboundTransitionState** *(dict) --*

          The state of the inbound transition, which is either enabled or disabled.

          - **enabled** *(boolean) --*

            Whether the transition between stages is enabled (true) or disabled (false).

          - **lastChangedBy** *(string) --*

            The ID of the user who last changed the transition state.

          - **lastChangedAt** *(datetime) --*

            The timestamp when the transition state was last changed.

          - **disabledReason** *(string) --*

            The user-specified reason why the transition between two stages of a pipeline was
            disabled.

        - **actionStates** *(list) --*

          The state of the stage.

          - *(dict) --*

            Represents information about the state of an action.

            - **actionName** *(string) --*

              The name of the action.

            - **currentRevision** *(dict) --*

              Represents information about the version (or revision) of an action.

              - **revisionId** *(string) --*

                The system-generated unique ID that identifies the revision number of the action.

              - **revisionChangeId** *(string) --*

                The unique identifier of the change that set the state to this revision (for
                example, a deployment ID or timestamp).

              - **created** *(datetime) --*

                The date and time when the most recent version of the action was created, in
                timestamp format.

            - **latestExecution** *(dict) --*

              Represents information about the run of an action.

              - **status** *(string) --*

                The status of the action, or for a completed action, the last status of the action.

              - **summary** *(string) --*

                A summary of the run of the action.

              - **lastStatusChange** *(datetime) --*

                The last status change of the action.

              - **token** *(string) --*

                The system-generated token used to identify a unique approval request. The token
                for each open approval request can be obtained using the ``GetPipelineState``
                command. It is used to validate that the approval request corresponding to this
                token is still valid.

              - **lastUpdatedBy** *(string) --*

                The ARN of the user who last changed the pipeline.

              - **externalExecutionId** *(string) --*

                The external ID of the run of the action.

              - **externalExecutionUrl** *(string) --*

                The URL of a resource external to AWS that is used when running the action (for
                example, an external repository URL).

              - **percentComplete** *(integer) --*

                A percentage of completeness of the action as it runs.

              - **errorDetails** *(dict) --*

                The details of an error returned by a URL external to AWS.

                - **code** *(string) --*

                  The system ID or number code of the error.

                - **message** *(string) --*

                  The text of the error message.

            - **entityUrl** *(string) --*

              A URL link for more information about the state of the action, such as a deployment
              group details page.

            - **revisionUrl** *(string) --*

              A URL link for more information about the revision, such as a commit details page.

        - **latestExecution** *(dict) --*

          Information about the latest execution in the stage, including its ID and status.

          - **pipelineExecutionId** *(string) --*

            The ID of the pipeline execution associated with the stage.

          - **status** *(string) --*

            The status of the stage, or for a completed stage, the last status of the stage.

    - **created** *(datetime) --*

      The date and time the pipeline was created, in timestamp format.

    - **updated** *(datetime) --*

      The date and time the pipeline was last updated, in timestamp format.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `actionConfiguration`

    Represents information about an action configuration.

    - **configuration** *(dict) --*

      The configuration data for the action.

      - *(string) --*

        - *(string) --*
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are determined
      by the action category. For example, an action in the Deploy category type might have a
      provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
      information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `artifactCredentials`

    Represents an AWS session credentials object. These credentials are temporary credentials
    that are issued by AWS Secure Token Service (STS). They can be used to access input and
    output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS
    CodePipeline.

    - **accessKeyId** *(string) --*

      The access key for the session.

    - **secretAccessKey** *(string) --*

      The secret access key for the session.

    - **sessionToken** *(string) --*

      The token for the session.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `encryptionKey`

    The encryption key used to encrypt and decrypt data in the artifact store for the
    pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might
    not be present.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `inputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `outputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContext` `action`

    The context of an action to a job worker in the stage of a pipeline.

    - **name** *(string) --*

      The name of the action in the context of a job.

    - **actionExecutionId** *(string) --*

      The system-generated unique ID that corresponds to an action's execution.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContext` `stage`

    The stage of the pipeline.

    - **name** *(string) --*

      The name of the stage.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetailsdata` `pipelineContext`

    Represents information about a pipeline to a job worker.

    .. note::

      Does not include ``pipelineArn`` and ``pipelineExecutionId`` for ThirdParty jobs.

    - **pipelineName** *(string) --*

      The name of the pipeline. This is a user-specified value. Pipeline names must be unique
      across all pipeline names under an Amazon Web Services account.

    - **stage** *(dict) --*

      The stage of the pipeline.

      - **name** *(string) --*

        The name of the stage.

    - **action** *(dict) --*

      The context of an action to a job worker in the stage of a pipeline.

      - **name** *(string) --*

        The name of the action in the context of a job.

      - **actionExecutionId** *(string) --*

        The system-generated unique ID that corresponds to an action's execution.

    - **pipelineArn** *(string) --*

      The Amazon Resource Name (ARN) of the pipeline.

    - **pipelineExecutionId** *(string) --*

      The execution ID of the pipeline.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef",
    {
        "actionTypeId": ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef,
        "pipelineContext": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef,
        "inputArtifacts": List[
            ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
        ],
        "outputArtifacts": List[
            ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
        ],
        "artifactCredentials": ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponsejobDetails` `data`

    The data to be returned by the third party job worker.

    - **actionTypeId** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are determined
        by the action category. For example, an action in the Deploy category type might have a
        provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
        information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **actionConfiguration** *(dict) --*

      Represents information about an action configuration.

      - **configuration** *(dict) --*

        The configuration data for the action.

        - *(string) --*

          - *(string) --*

    - **pipelineContext** *(dict) --*

      Represents information about a pipeline to a job worker.

      .. note::

        Does not include ``pipelineArn`` and ``pipelineExecutionId`` for ThirdParty jobs.

      - **pipelineName** *(string) --*

        The name of the pipeline. This is a user-specified value. Pipeline names must be unique
        across all pipeline names under an Amazon Web Services account.

      - **stage** *(dict) --*

        The stage of the pipeline.

        - **name** *(string) --*

          The name of the stage.

      - **action** *(dict) --*

        The context of an action to a job worker in the stage of a pipeline.

        - **name** *(string) --*

          The name of the action in the context of a job.

        - **actionExecutionId** *(string) --*

          The system-generated unique ID that corresponds to an action's execution.

      - **pipelineArn** *(string) --*

        The Amazon Resource Name (ARN) of the pipeline.

      - **pipelineExecutionId** *(string) --*

        The execution ID of the pipeline.

    - **inputArtifacts** *(list) --*

      The name of the artifact that is worked on by the action, if any. This name might be
      system-generated, such as "MyApp", or it might be defined by the user when the action is
      created. The input artifact name must match the name of an output artifact generated by
      an action in an earlier action or stage of the pipeline.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **outputArtifacts** *(list) --*

      The name of the artifact that is the result of the action, if any. This name might be
      system-generated, such as "MyBuiltApp", or it might be defined by the user when the
      action is created.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **artifactCredentials** *(dict) --*

      Represents an AWS session credentials object. These credentials are temporary credentials
      that are issued by AWS Secure Token Service (STS). They can be used to access input and
      output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS
      CodePipeline.

      - **accessKeyId** *(string) --*

        The access key for the session.

      - **secretAccessKey** *(string) --*

        The secret access key for the session.

      - **sessionToken** *(string) --*

        The token for the session.

    - **continuationToken** *(string) --*

      A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires to
      continue the job asynchronously.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt and decrypt data in the artifact store for the
      pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might
      not be present.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef",
    {
        "id": str,
        "data": ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef,
        "nonce": str,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetailsResponse` `jobDetails`

    The details of the job, including any protected values defined for the job.

    - **id** *(string) --*

      The identifier used to identify the job details in AWS CodePipeline.

    - **data** *(dict) --*

      The data to be returned by the third party job worker.

      - **actionTypeId** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following
          values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are determined
          by the action category. For example, an action in the Deploy category type might have a
          provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
          information, see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **actionConfiguration** *(dict) --*

        Represents information about an action configuration.

        - **configuration** *(dict) --*

          The configuration data for the action.

          - *(string) --*

            - *(string) --*

      - **pipelineContext** *(dict) --*

        Represents information about a pipeline to a job worker.

        .. note::

          Does not include ``pipelineArn`` and ``pipelineExecutionId`` for ThirdParty jobs.

        - **pipelineName** *(string) --*

          The name of the pipeline. This is a user-specified value. Pipeline names must be unique
          across all pipeline names under an Amazon Web Services account.

        - **stage** *(dict) --*

          The stage of the pipeline.

          - **name** *(string) --*

            The name of the stage.

        - **action** *(dict) --*

          The context of an action to a job worker in the stage of a pipeline.

          - **name** *(string) --*

            The name of the action in the context of a job.

          - **actionExecutionId** *(string) --*

            The system-generated unique ID that corresponds to an action's execution.

        - **pipelineArn** *(string) --*

          The Amazon Resource Name (ARN) of the pipeline.

        - **pipelineExecutionId** *(string) --*

          The execution ID of the pipeline.

      - **inputArtifacts** *(list) --*

        The name of the artifact that is worked on by the action, if any. This name might be
        system-generated, such as "MyApp", or it might be defined by the user when the action is
        created. The input artifact name must match the name of an output artifact generated by
        an action in an earlier action or stage of the pipeline.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **outputArtifacts** *(list) --*

        The name of the artifact that is the result of the action, if any. This name might be
        system-generated, such as "MyBuiltApp", or it might be defined by the user when the
        action is created.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **artifactCredentials** *(dict) --*

        Represents an AWS session credentials object. These credentials are temporary credentials
        that are issued by AWS Secure Token Service (STS). They can be used to access input and
        output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS
        CodePipeline.

        - **accessKeyId** *(string) --*

          The access key for the session.

        - **secretAccessKey** *(string) --*

          The secret access key for the session.

        - **sessionToken** *(string) --*

          The token for the session.

      - **continuationToken** *(string) --*

        A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires to
        continue the job asynchronously.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt and decrypt data in the artifact store for the
        pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might
        not be present.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
            the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **nonce** *(string) --*

      A system-generated random number that AWS CodePipeline uses to ensure that the job is being
      worked on by only one job worker. Use this number in an  AcknowledgeThirdPartyJob request.
    """


_ClientGetThirdPartyJobDetailsResponseTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponseTypeDef(
    _ClientGetThirdPartyJobDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetThirdPartyJobDetails` `Response`

    Represents the output of a ``GetThirdPartyJobDetails`` action.

    - **jobDetails** *(dict) --*

      The details of the job, including any protected values defined for the job.

      - **id** *(string) --*

        The identifier used to identify the job details in AWS CodePipeline.

      - **data** *(dict) --*

        The data to be returned by the third party job worker.

        - **actionTypeId** *(dict) --*

          Represents information about an action type.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are determined
            by the action category. For example, an action in the Deploy category type might have a
            provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
            information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **actionConfiguration** *(dict) --*

          Represents information about an action configuration.

          - **configuration** *(dict) --*

            The configuration data for the action.

            - *(string) --*

              - *(string) --*

        - **pipelineContext** *(dict) --*

          Represents information about a pipeline to a job worker.

          .. note::

            Does not include ``pipelineArn`` and ``pipelineExecutionId`` for ThirdParty jobs.

          - **pipelineName** *(string) --*

            The name of the pipeline. This is a user-specified value. Pipeline names must be unique
            across all pipeline names under an Amazon Web Services account.

          - **stage** *(dict) --*

            The stage of the pipeline.

            - **name** *(string) --*

              The name of the stage.

          - **action** *(dict) --*

            The context of an action to a job worker in the stage of a pipeline.

            - **name** *(string) --*

              The name of the action in the context of a job.

            - **actionExecutionId** *(string) --*

              The system-generated unique ID that corresponds to an action's execution.

          - **pipelineArn** *(string) --*

            The Amazon Resource Name (ARN) of the pipeline.

          - **pipelineExecutionId** *(string) --*

            The execution ID of the pipeline.

        - **inputArtifacts** *(list) --*

          The name of the artifact that is worked on by the action, if any. This name might be
          system-generated, such as "MyApp", or it might be defined by the user when the action is
          created. The input artifact name must match the name of an output artifact generated by
          an action in an earlier action or stage of the pipeline.

          - *(dict) --*

            Represents information about an artifact that is worked on by actions in the pipeline.

            - **name** *(string) --*

              The artifact's name.

            - **revision** *(string) --*

              The artifact's revision ID. Depending on the type of object, this could be a commit
              ID (GitHub) or a revision ID (Amazon S3).

            - **location** *(dict) --*

              The location of an artifact.

              - **type** *(string) --*

                The type of artifact in the location.

              - **s3Location** *(dict) --*

                The Amazon S3 bucket that contains the artifact.

                - **bucketName** *(string) --*

                  The name of the Amazon S3 bucket.

                - **objectKey** *(string) --*

                  The key of the object in the Amazon S3 bucket, which uniquely identifies the
                  object in the bucket.

        - **outputArtifacts** *(list) --*

          The name of the artifact that is the result of the action, if any. This name might be
          system-generated, such as "MyBuiltApp", or it might be defined by the user when the
          action is created.

          - *(dict) --*

            Represents information about an artifact that is worked on by actions in the pipeline.

            - **name** *(string) --*

              The artifact's name.

            - **revision** *(string) --*

              The artifact's revision ID. Depending on the type of object, this could be a commit
              ID (GitHub) or a revision ID (Amazon S3).

            - **location** *(dict) --*

              The location of an artifact.

              - **type** *(string) --*

                The type of artifact in the location.

              - **s3Location** *(dict) --*

                The Amazon S3 bucket that contains the artifact.

                - **bucketName** *(string) --*

                  The name of the Amazon S3 bucket.

                - **objectKey** *(string) --*

                  The key of the object in the Amazon S3 bucket, which uniquely identifies the
                  object in the bucket.

        - **artifactCredentials** *(dict) --*

          Represents an AWS session credentials object. These credentials are temporary credentials
          that are issued by AWS Secure Token Service (STS). They can be used to access input and
          output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS
          CodePipeline.

          - **accessKeyId** *(string) --*

            The access key for the session.

          - **secretAccessKey** *(string) --*

            The secret access key for the session.

          - **sessionToken** *(string) --*

            The token for the session.

        - **continuationToken** *(string) --*

          A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires to
          continue the job asynchronously.

        - **encryptionKey** *(dict) --*

          The encryption key used to encrypt and decrypt data in the artifact store for the
          pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might
          not be present.

          - **id** *(string) --*

            The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
            ARN, or the alias ARN.

            .. note::

              Aliases are recognized only in the account that created the customer master key
              (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
              the key.

          - **type** *(string) --*

            The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
            creating or updating a pipeline, the value must be set to 'KMS'.

      - **nonce** *(string) --*

        A system-generated random number that AWS CodePipeline uses to ensure that the job is being
        worked on by only one job worker. Use this number in an  AcknowledgeThirdPartyJob request.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsinput` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category type
      might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
      more information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifacts` `s3location`

    The Amazon S3 artifact location for the action execution.

    - **bucket** *(string) --*

      The Amazon S3 artifact bucket for an action's artifacts.

    - **key** *(string) --*

      The artifact name.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsinput` `inputArtifacts`

    Artifact details for the action execution, such as the artifact location.

    - **name** *(string) --*

      The artifact object name for the action execution.

    - **s3location** *(dict) --*

      The Amazon S3 artifact location for the action execution.

      - **bucket** *(string) --*

        The Amazon S3 artifact bucket for an action's artifacts.

      - **key** *(string) --*

        The artifact name.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef",
    {
        "actionTypeId": ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef,
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List[
            ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef
        ],
        "namespace": str,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetails` `input`

    Input details for the action execution, such as role ARN, Region, and input artifacts.

    - **actionTypeId** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category type
        might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
        more information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **configuration** *(dict) --*

      Configuration data for an action execution.

      - *(string) --*

        - *(string) --*

    - **resolvedConfiguration** *(dict) --*

      Configuration data for an action execution with all variable references replaced with
      their real values for the execution.

      - *(string) --*

        - *(string) --*

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The AWS Region for the action, such as us-east-1.

    - **inputArtifacts** *(list) --*

      Details of input artifacts of the action that correspond to the action execution.

      - *(dict) --*

        Artifact details for the action execution, such as the artifact location.

        - **name** *(string) --*

          The artifact object name for the action execution.

        - **s3location** *(dict) --*

          The Amazon S3 artifact location for the action execution.

          - **bucket** *(string) --*

            The Amazon S3 artifact bucket for an action's artifacts.

          - **key** *(string) --*

            The artifact name.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output by
      this action fall under this namespace.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {
        "externalExecutionId": str,
        "externalExecutionSummary": str,
        "externalExecutionUrl": str,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsoutput` `executionResult`

    Execution result information listed in the output details for an action execution.

    - **externalExecutionId** *(string) --*

      The action provider's external ID for the action execution.

    - **externalExecutionSummary** *(string) --*

      The action provider's summary for the action execution.

    - **externalExecutionUrl** *(string) --*

      The deepest external link to the external resource (for example, a repository URL or
      deployment endpoint) that is used when running the action.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifacts` `s3location`

    The Amazon S3 artifact location for the action execution.

    - **bucket** *(string) --*

      The Amazon S3 artifact bucket for an action's artifacts.

    - **key** *(string) --*

      The artifact name.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetailsoutput` `outputArtifacts`

    Artifact details for the action execution, such as the artifact location.

    - **name** *(string) --*

      The artifact object name for the action execution.

    - **s3location** *(dict) --*

      The Amazon S3 artifact location for the action execution.

      - **bucket** *(string) --*

        The Amazon S3 artifact bucket for an action's artifacts.

      - **key** *(string) --*

        The artifact name.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponseactionExecutionDetails` `output`

    Output details for the action execution, such as the action execution result.

    - **outputArtifacts** *(list) --*

      Details of output artifacts of the action that correspond to the action execution.

      - *(dict) --*

        Artifact details for the action execution, such as the artifact location.

        - **name** *(string) --*

          The artifact object name for the action execution.

        - **s3location** *(dict) --*

          The Amazon S3 artifact location for the action execution.

          - **bucket** *(string) --*

            The Amazon S3 artifact bucket for an action's artifacts.

          - **key** *(string) --*

            The artifact name.

    - **executionResult** *(dict) --*

      Execution result information listed in the output details for an action execution.

      - **externalExecutionId** *(string) --*

        The action provider's external ID for the action execution.

      - **externalExecutionSummary** *(string) --*

        The action provider's summary for the action execution.

      - **externalExecutionUrl** *(string) --*

        The deepest external link to the external resource (for example, a repository URL or
        deployment endpoint) that is used when running the action.

    - **outputVariables** *(dict) --*

      The outputVariables field shows the key-value pairs that were output as part of that
      execution.

      - *(string) --*

        - *(string) --*
    """


_ClientListActionExecutionsResponseactionExecutionDetailsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "input": ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef,
        "output": ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsTypeDef
):
    """
    Type definition for `ClientListActionExecutionsResponse` `actionExecutionDetails`

    Returns information about an execution of an action, including the action execution ID, and
    the name, version, and timing of the action.

    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID for the action execution.

    - **actionExecutionId** *(string) --*

      The action execution ID.

    - **pipelineVersion** *(integer) --*

      The version of the pipeline where the action was run.

    - **stageName** *(string) --*

      The name of the stage that contains the action.

    - **actionName** *(string) --*

      The name of the action.

    - **startTime** *(datetime) --*

      The start time of the action execution.

    - **lastUpdateTime** *(datetime) --*

      The last update time of the action execution.

    - **status** *(string) --*

      The status of the action execution. Status categories are ``InProgress`` , ``Succeeded``
      , and ``Failed`` .

    - **input** *(dict) --*

      Input details for the action execution, such as role ARN, Region, and input artifacts.

      - **actionTypeId** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following
          values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are
          determined by the action category. For example, an action in the Deploy category type
          might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
          more information, see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **configuration** *(dict) --*

        Configuration data for an action execution.

        - *(string) --*

          - *(string) --*

      - **resolvedConfiguration** *(dict) --*

        Configuration data for an action execution with all variable references replaced with
        their real values for the execution.

        - *(string) --*

          - *(string) --*

      - **roleArn** *(string) --*

        The ARN of the IAM service role that performs the declared action. This is assumed
        through the roleArn for the pipeline.

      - **region** *(string) --*

        The AWS Region for the action, such as us-east-1.

      - **inputArtifacts** *(list) --*

        Details of input artifacts of the action that correspond to the action execution.

        - *(dict) --*

          Artifact details for the action execution, such as the artifact location.

          - **name** *(string) --*

            The artifact object name for the action execution.

          - **s3location** *(dict) --*

            The Amazon S3 artifact location for the action execution.

            - **bucket** *(string) --*

              The Amazon S3 artifact bucket for an action's artifacts.

            - **key** *(string) --*

              The artifact name.

      - **namespace** *(string) --*

        The variable namespace associated with the action. All variables produced as output by
        this action fall under this namespace.

    - **output** *(dict) --*

      Output details for the action execution, such as the action execution result.

      - **outputArtifacts** *(list) --*

        Details of output artifacts of the action that correspond to the action execution.

        - *(dict) --*

          Artifact details for the action execution, such as the artifact location.

          - **name** *(string) --*

            The artifact object name for the action execution.

          - **s3location** *(dict) --*

            The Amazon S3 artifact location for the action execution.

            - **bucket** *(string) --*

              The Amazon S3 artifact bucket for an action's artifacts.

            - **key** *(string) --*

              The artifact name.

      - **executionResult** *(dict) --*

        Execution result information listed in the output details for an action execution.

        - **externalExecutionId** *(string) --*

          The action provider's external ID for the action execution.

        - **externalExecutionSummary** *(string) --*

          The action provider's summary for the action execution.

        - **externalExecutionUrl** *(string) --*

          The deepest external link to the external resource (for example, a repository URL or
          deployment endpoint) that is used when running the action.

      - **outputVariables** *(dict) --*

        The outputVariables field shows the key-value pairs that were output as part of that
        execution.

        - *(string) --*

          - *(string) --*
    """


_ClientListActionExecutionsResponseTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ClientListActionExecutionsResponseactionExecutionDetailsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListActionExecutionsResponseTypeDef(
    _ClientListActionExecutionsResponseTypeDef
):
    """
    Type definition for `ClientListActionExecutions` `Response`

    - **actionExecutionDetails** *(list) --*

      The details for a list of recent executions, such as action execution ID.

      - *(dict) --*

        Returns information about an execution of an action, including the action execution ID, and
        the name, version, and timing of the action.

        - **pipelineExecutionId** *(string) --*

          The pipeline execution ID for the action execution.

        - **actionExecutionId** *(string) --*

          The action execution ID.

        - **pipelineVersion** *(integer) --*

          The version of the pipeline where the action was run.

        - **stageName** *(string) --*

          The name of the stage that contains the action.

        - **actionName** *(string) --*

          The name of the action.

        - **startTime** *(datetime) --*

          The start time of the action execution.

        - **lastUpdateTime** *(datetime) --*

          The last update time of the action execution.

        - **status** *(string) --*

          The status of the action execution. Status categories are ``InProgress`` , ``Succeeded``
          , and ``Failed`` .

        - **input** *(dict) --*

          Input details for the action execution, such as role ARN, Region, and input artifacts.

          - **actionTypeId** *(dict) --*

            Represents information about an action type.

            - **category** *(string) --*

              A category defines what kind of action can be taken in the stage, and constrains the
              provider type for the action. Valid categories are limited to one of the following
              values.

            - **owner** *(string) --*

              The creator of the action being called.

            - **provider** *(string) --*

              The provider of the service being called by the action. Valid providers are
              determined by the action category. For example, an action in the Deploy category type
              might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
              more information, see `Valid Action Types and Providers in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
              .

            - **version** *(string) --*

              A string that describes the action version.

          - **configuration** *(dict) --*

            Configuration data for an action execution.

            - *(string) --*

              - *(string) --*

          - **resolvedConfiguration** *(dict) --*

            Configuration data for an action execution with all variable references replaced with
            their real values for the execution.

            - *(string) --*

              - *(string) --*

          - **roleArn** *(string) --*

            The ARN of the IAM service role that performs the declared action. This is assumed
            through the roleArn for the pipeline.

          - **region** *(string) --*

            The AWS Region for the action, such as us-east-1.

          - **inputArtifacts** *(list) --*

            Details of input artifacts of the action that correspond to the action execution.

            - *(dict) --*

              Artifact details for the action execution, such as the artifact location.

              - **name** *(string) --*

                The artifact object name for the action execution.

              - **s3location** *(dict) --*

                The Amazon S3 artifact location for the action execution.

                - **bucket** *(string) --*

                  The Amazon S3 artifact bucket for an action's artifacts.

                - **key** *(string) --*

                  The artifact name.

          - **namespace** *(string) --*

            The variable namespace associated with the action. All variables produced as output by
            this action fall under this namespace.

        - **output** *(dict) --*

          Output details for the action execution, such as the action execution result.

          - **outputArtifacts** *(list) --*

            Details of output artifacts of the action that correspond to the action execution.

            - *(dict) --*

              Artifact details for the action execution, such as the artifact location.

              - **name** *(string) --*

                The artifact object name for the action execution.

              - **s3location** *(dict) --*

                The Amazon S3 artifact location for the action execution.

                - **bucket** *(string) --*

                  The Amazon S3 artifact bucket for an action's artifacts.

                - **key** *(string) --*

                  The artifact name.

          - **executionResult** *(dict) --*

            Execution result information listed in the output details for an action execution.

            - **externalExecutionId** *(string) --*

              The action provider's external ID for the action execution.

            - **externalExecutionSummary** *(string) --*

              The action provider's summary for the action execution.

            - **externalExecutionUrl** *(string) --*

              The deepest external link to the external resource (for example, a repository URL or
              deployment endpoint) that is used when running the action.

          - **outputVariables** *(dict) --*

            The outputVariables field shows the key-value pairs that were output as part of that
            execution.

            - *(string) --*

              - *(string) --*

    - **nextToken** *(string) --*

      If the amount of returned information is significantly large, an identifier is also returned
      and can be used in a subsequent ``ListActionExecutions`` call to return the next set of
      action executions in the list.
    """


_ClientListActionExecutionsfilterTypeDef = TypedDict(
    "_ClientListActionExecutionsfilterTypeDef",
    {"pipelineExecutionId": str},
    total=False,
)


class ClientListActionExecutionsfilterTypeDef(_ClientListActionExecutionsfilterTypeDef):
    """
    Type definition for `ClientListActionExecutions` `filter`

    Input information used to filter action execution history.

    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID used to filter action execution history.
    """


_ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": str,
    },
    total=False,
)


class ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef(
    _ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef
):
    """
    Type definition for `ClientListActionTypesResponseactionTypes` `actionConfigurationProperties`

    Represents information about an action configuration property.

    - **name** *(string) --*

      The name of the action configuration property.

    - **required** *(boolean) --*

      Whether the configuration property is a required value.

    - **key** *(boolean) --*

      Whether the configuration property is a key.

    - **secret** *(boolean) --*

      Whether the configuration property is secret. Secrets are hidden from all calls
      except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
      ``PollForThirdPartyJobs`` .

      When updating a pipeline, passing * * * * * without changing any other values of the
      action preserves the previous value of the secret.

    - **queryable** *(boolean) --*

      Indicates that the property is used with ``PollForJobs`` . When creating a custom
      action, an action can have up to one queryable property. If it has one, that property
      must be both required and not secret.

      If you create a pipeline with a custom action type, and that custom action contains a
      queryable property, the value for that configuration property is subject to other
      restrictions. The value must be less than or equal to twenty (20) characters. The
      value can contain only alphanumeric characters, underscores, and hyphens.

    - **description** *(string) --*

      The description of the action configuration property that is displayed to users.

    - **type** *(string) --*

      The type of the configuration property.
    """


_ClientListActionTypesResponseactionTypesidTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesidTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientListActionTypesResponseactionTypesidTypeDef(
    _ClientListActionTypesResponseactionTypesidTypeDef
):
    """
    Type definition for `ClientListActionTypesResponseactionTypes` `id`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are determined
      by the action category. For example, an action in the Deploy category type might have a
      provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
      information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef(
    _ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientListActionTypesResponseactionTypes` `inputArtifactDetails`

    The details of the input artifact for the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef(
    _ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef
):
    """
    Type definition for `ClientListActionTypesResponseactionTypes` `outputArtifactDetails`

    The details of the output artifact of the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ClientListActionTypesResponseactionTypessettingsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientListActionTypesResponseactionTypessettingsTypeDef(
    _ClientListActionTypesResponseactionTypessettingsTypeDef
):
    """
    Type definition for `ClientListActionTypesResponseactionTypes` `settings`

    The settings for the action type.

    - **thirdPartyConfigurationUrl** *(string) --*

      The URL of a sign-up page where users can sign up for an external service and perform
      initial configuration of the action provided by that service.

    - **entityUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that provides a deep link to the
      resources of the external system, such as the configuration page for an AWS CodeDeploy
      deployment group. This link is provided as part of the action display in the pipeline.

    - **executionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the top-level
      landing page for the external system, such as the console page for AWS CodeDeploy. This
      link is shown on the pipeline view page in the AWS CodePipeline console and provides a
      link to the execution entity of the external action.

    - **revisionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the page where
      customers can update or change the configuration of the external action.
    """


_ClientListActionTypesResponseactionTypesTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesTypeDef",
    {
        "id": ClientListActionTypesResponseactionTypesidTypeDef,
        "settings": ClientListActionTypesResponseactionTypessettingsTypeDef,
        "actionConfigurationProperties": List[
            ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef,
    },
    total=False,
)


class ClientListActionTypesResponseactionTypesTypeDef(
    _ClientListActionTypesResponseactionTypesTypeDef
):
    """
    Type definition for `ClientListActionTypesResponse` `actionTypes`

    Returns information about the details of an action type.

    - **id** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are determined
        by the action category. For example, an action in the Deploy category type might have a
        provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
        information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **settings** *(dict) --*

      The settings for the action type.

      - **thirdPartyConfigurationUrl** *(string) --*

        The URL of a sign-up page where users can sign up for an external service and perform
        initial configuration of the action provided by that service.

      - **entityUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that provides a deep link to the
        resources of the external system, such as the configuration page for an AWS CodeDeploy
        deployment group. This link is provided as part of the action display in the pipeline.

      - **executionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the top-level
        landing page for the external system, such as the console page for AWS CodeDeploy. This
        link is shown on the pipeline view page in the AWS CodePipeline console and provides a
        link to the execution entity of the external action.

      - **revisionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the page where
        customers can update or change the configuration of the external action.

    - **actionConfigurationProperties** *(list) --*

      The configuration properties for the action type.

      - *(dict) --*

        Represents information about an action configuration property.

        - **name** *(string) --*

          The name of the action configuration property.

        - **required** *(boolean) --*

          Whether the configuration property is a required value.

        - **key** *(boolean) --*

          Whether the configuration property is a key.

        - **secret** *(boolean) --*

          Whether the configuration property is secret. Secrets are hidden from all calls
          except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
          ``PollForThirdPartyJobs`` .

          When updating a pipeline, passing * * * * * without changing any other values of the
          action preserves the previous value of the secret.

        - **queryable** *(boolean) --*

          Indicates that the property is used with ``PollForJobs`` . When creating a custom
          action, an action can have up to one queryable property. If it has one, that property
          must be both required and not secret.

          If you create a pipeline with a custom action type, and that custom action contains a
          queryable property, the value for that configuration property is subject to other
          restrictions. The value must be less than or equal to twenty (20) characters. The
          value can contain only alphanumeric characters, underscores, and hyphens.

        - **description** *(string) --*

          The description of the action configuration property that is displayed to users.

        - **type** *(string) --*

          The type of the configuration property.

    - **inputArtifactDetails** *(dict) --*

      The details of the input artifact for the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.

    - **outputArtifactDetails** *(dict) --*

      The details of the output artifact of the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.
    """


_ClientListActionTypesResponseTypeDef = TypedDict(
    "_ClientListActionTypesResponseTypeDef",
    {
        "actionTypes": List[ClientListActionTypesResponseactionTypesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListActionTypesResponseTypeDef(_ClientListActionTypesResponseTypeDef):
    """
    Type definition for `ClientListActionTypes` `Response`

    Represents the output of a ``ListActionTypes`` action.

    - **actionTypes** *(list) --*

      Provides details of the action types.

      - *(dict) --*

        Returns information about the details of an action type.

        - **id** *(dict) --*

          Represents information about an action type.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are determined
            by the action category. For example, an action in the Deploy category type might have a
            provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
            information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **settings** *(dict) --*

          The settings for the action type.

          - **thirdPartyConfigurationUrl** *(string) --*

            The URL of a sign-up page where users can sign up for an external service and perform
            initial configuration of the action provided by that service.

          - **entityUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that provides a deep link to the
            resources of the external system, such as the configuration page for an AWS CodeDeploy
            deployment group. This link is provided as part of the action display in the pipeline.

          - **executionUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that contains a link to the top-level
            landing page for the external system, such as the console page for AWS CodeDeploy. This
            link is shown on the pipeline view page in the AWS CodePipeline console and provides a
            link to the execution entity of the external action.

          - **revisionUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that contains a link to the page where
            customers can update or change the configuration of the external action.

        - **actionConfigurationProperties** *(list) --*

          The configuration properties for the action type.

          - *(dict) --*

            Represents information about an action configuration property.

            - **name** *(string) --*

              The name of the action configuration property.

            - **required** *(boolean) --*

              Whether the configuration property is a required value.

            - **key** *(boolean) --*

              Whether the configuration property is a key.

            - **secret** *(boolean) --*

              Whether the configuration property is secret. Secrets are hidden from all calls
              except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
              ``PollForThirdPartyJobs`` .

              When updating a pipeline, passing * * * * * without changing any other values of the
              action preserves the previous value of the secret.

            - **queryable** *(boolean) --*

              Indicates that the property is used with ``PollForJobs`` . When creating a custom
              action, an action can have up to one queryable property. If it has one, that property
              must be both required and not secret.

              If you create a pipeline with a custom action type, and that custom action contains a
              queryable property, the value for that configuration property is subject to other
              restrictions. The value must be less than or equal to twenty (20) characters. The
              value can contain only alphanumeric characters, underscores, and hyphens.

            - **description** *(string) --*

              The description of the action configuration property that is displayed to users.

            - **type** *(string) --*

              The type of the configuration property.

        - **inputArtifactDetails** *(dict) --*

          The details of the input artifact for the action, such as its commit ID.

          - **minimumCount** *(integer) --*

            The minimum number of artifacts allowed for the action type.

          - **maximumCount** *(integer) --*

            The maximum number of artifacts allowed for the action type.

        - **outputArtifactDetails** *(dict) --*

          The details of the output artifact of the action, such as its commit ID.

          - **minimumCount** *(integer) --*

            The minimum number of artifacts allowed for the action type.

          - **maximumCount** *(integer) --*

            The maximum number of artifacts allowed for the action type.

    - **nextToken** *(string) --*

      If the amount of returned information is significantly large, an identifier is also returned.
      It can be used in a subsequent list action types call to return the next set of action types
      in the list.
    """


_ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)


class ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef
):
    """
    Type definition for `ClientListPipelineExecutionsResponsepipelineExecutionSummaries` `sourceRevisions`

    Information about the version (or revision) of a source artifact that initiated a
    pipeline execution.

    - **actionName** *(string) --*

      The name of the action that processed the revision to the source artifact.

    - **revisionId** *(string) --*

      The system-generated unique ID that identifies the revision number of the artifact.

    - **revisionSummary** *(string) --*

      Summary information about the most recent revision of the artifact. For GitHub and
      AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
      the user-provided content of a ``codepipeline-artifact-revision-summary`` key
      specified in the object metadata.

    - **revisionUrl** *(string) --*

      The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
      CodeCommit repositories, the commit ID is linked to a commit details page.
    """


_ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef",
    {"triggerType": str, "triggerDetail": str},
    total=False,
)


class ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef
):
    """
    Type definition for `ClientListPipelineExecutionsResponsepipelineExecutionSummaries` `trigger`

    The interaction or event that started a pipeline execution, such as automated change
    detection or a ``StartPipelineExecution`` API call.

    - **triggerType** *(string) --*

      The type of change-detection method, command, or user interaction that started a
      pipeline execution.

    - **triggerDetail** *(string) --*

      Detail related to the event that started a pipeline execution, such as the webhook ARN
      of the webhook that triggered the pipeline execution or the user ARN for a
      user-initiated ``start-pipeline-execution`` CLI command.
    """


_ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef",
    {
        "pipelineExecutionId": str,
        "status": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List[
            ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef
        ],
        "trigger": ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef,
    },
    total=False,
)


class ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef
):
    """
    Type definition for `ClientListPipelineExecutionsResponse` `pipelineExecutionSummaries`

    Summary information about a pipeline execution.

    - **pipelineExecutionId** *(string) --*

      The ID of the pipeline execution.

    - **status** *(string) --*

      The status of the pipeline execution.

      * InProgress: The pipeline execution is currently running.

      * Succeeded: The pipeline execution was completed successfully.

      * Superseded: While this pipeline execution was waiting for the next stage to be
      completed, a newer pipeline execution advanced and continued through the pipeline instead.

      * Failed: The pipeline execution was not completed successfully.

    - **startTime** *(datetime) --*

      The date and time when the pipeline execution began, in timestamp format.

    - **lastUpdateTime** *(datetime) --*

      The date and time of the last change to the pipeline execution, in timestamp format.

    - **sourceRevisions** *(list) --*

      A list of the source artifact revisions that initiated a pipeline execution.

      - *(dict) --*

        Information about the version (or revision) of a source artifact that initiated a
        pipeline execution.

        - **actionName** *(string) --*

          The name of the action that processed the revision to the source artifact.

        - **revisionId** *(string) --*

          The system-generated unique ID that identifies the revision number of the artifact.

        - **revisionSummary** *(string) --*

          Summary information about the most recent revision of the artifact. For GitHub and
          AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
          the user-provided content of a ``codepipeline-artifact-revision-summary`` key
          specified in the object metadata.

        - **revisionUrl** *(string) --*

          The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
          CodeCommit repositories, the commit ID is linked to a commit details page.

    - **trigger** *(dict) --*

      The interaction or event that started a pipeline execution, such as automated change
      detection or a ``StartPipelineExecution`` API call.

      - **triggerType** *(string) --*

        The type of change-detection method, command, or user interaction that started a
        pipeline execution.

      - **triggerDetail** *(string) --*

        Detail related to the event that started a pipeline execution, such as the webhook ARN
        of the webhook that triggered the pipeline execution or the user ARN for a
        user-initiated ``start-pipeline-execution`` CLI command.
    """


_ClientListPipelineExecutionsResponseTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListPipelineExecutionsResponseTypeDef(
    _ClientListPipelineExecutionsResponseTypeDef
):
    """
    Type definition for `ClientListPipelineExecutions` `Response`

    Represents the output of a ``ListPipelineExecutions`` action.

    - **pipelineExecutionSummaries** *(list) --*

      A list of executions in the history of a pipeline.

      - *(dict) --*

        Summary information about a pipeline execution.

        - **pipelineExecutionId** *(string) --*

          The ID of the pipeline execution.

        - **status** *(string) --*

          The status of the pipeline execution.

          * InProgress: The pipeline execution is currently running.

          * Succeeded: The pipeline execution was completed successfully.

          * Superseded: While this pipeline execution was waiting for the next stage to be
          completed, a newer pipeline execution advanced and continued through the pipeline instead.

          * Failed: The pipeline execution was not completed successfully.

        - **startTime** *(datetime) --*

          The date and time when the pipeline execution began, in timestamp format.

        - **lastUpdateTime** *(datetime) --*

          The date and time of the last change to the pipeline execution, in timestamp format.

        - **sourceRevisions** *(list) --*

          A list of the source artifact revisions that initiated a pipeline execution.

          - *(dict) --*

            Information about the version (or revision) of a source artifact that initiated a
            pipeline execution.

            - **actionName** *(string) --*

              The name of the action that processed the revision to the source artifact.

            - **revisionId** *(string) --*

              The system-generated unique ID that identifies the revision number of the artifact.

            - **revisionSummary** *(string) --*

              Summary information about the most recent revision of the artifact. For GitHub and
              AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
              the user-provided content of a ``codepipeline-artifact-revision-summary`` key
              specified in the object metadata.

            - **revisionUrl** *(string) --*

              The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
              CodeCommit repositories, the commit ID is linked to a commit details page.

        - **trigger** *(dict) --*

          The interaction or event that started a pipeline execution, such as automated change
          detection or a ``StartPipelineExecution`` API call.

          - **triggerType** *(string) --*

            The type of change-detection method, command, or user interaction that started a
            pipeline execution.

          - **triggerDetail** *(string) --*

            Detail related to the event that started a pipeline execution, such as the webhook ARN
            of the webhook that triggered the pipeline execution or the user ARN for a
            user-initiated ``start-pipeline-execution`` CLI command.

    - **nextToken** *(string) --*

      A token that can be used in the next ``ListPipelineExecutions`` call. To view all items in
      the list, continue to call this operation with each subsequent token until no more nextToken
      values are returned.
    """


_ClientListPipelinesResponsepipelinesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)


class ClientListPipelinesResponsepipelinesTypeDef(
    _ClientListPipelinesResponsepipelinesTypeDef
):
    """
    Type definition for `ClientListPipelinesResponse` `pipelines`

    Returns a summary of a pipeline.

    - **name** *(string) --*

      The name of the pipeline.

    - **version** *(integer) --*

      The version number of the pipeline.

    - **created** *(datetime) --*

      The date and time the pipeline was created, in timestamp format.

    - **updated** *(datetime) --*

      The date and time of the last update to the pipeline, in timestamp format.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {"pipelines": List[ClientListPipelinesResponsepipelinesTypeDef], "nextToken": str},
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    Type definition for `ClientListPipelines` `Response`

    Represents the output of a ``ListPipelines`` action.

    - **pipelines** *(list) --*

      The list of pipelines.

      - *(dict) --*

        Returns a summary of a pipeline.

        - **name** *(string) --*

          The name of the pipeline.

        - **version** *(integer) --*

          The version number of the pipeline.

        - **created** *(datetime) --*

          The date and time the pipeline was created, in timestamp format.

        - **updated** *(datetime) --*

          The date and time of the last update to the pipeline, in timestamp format.

    - **nextToken** *(string) --*

      If the amount of returned information is significantly large, an identifier is also returned.
      It can be used in a subsequent list pipelines call to return the next set of pipelines in the
      list.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      The tags for the resource.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.

    - **nextToken** *(string) --*

      If the amount of returned information is significantly large, an identifier is also returned
      and can be used in a subsequent API call to return the next page of the list. The
      ListTagsforResource call lists all available tags in one call and does not use pagination.
    """


_ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef
):
    """
    Type definition for `ClientListWebhooksResponsewebhooksdefinition` `authenticationConfiguration`

    Properties that configure the authentication applied to incoming webhook trigger
    requests. The required properties depend on the authentication type. For GITHUB_HMAC,
    only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
    property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
    set.

    - **AllowedIPRange** *(string) --*

      The property used to configure acceptance of webhooks in an IP address range. For IP,
      only the ``AllowedIPRange`` property must be set. This property must be set to a
      valid CIDR range.

    - **SecretToken** *(string) --*

      The property used to configure GitHub authentication. For GITHUB_HMAC, only the
      ``SecretToken`` property must be set.
    """


_ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef
):
    """
    Type definition for `ClientListWebhooksResponsewebhooksdefinition` `filters`

    The event criteria that specify when a webhook notification is sent to your URL.

    - **jsonPath** *(string) --*

      A JsonPath expression that is applied to the body/payload of the webhook. The value
      selected by the JsonPath expression must match the value specified in the
      ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
      `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

    - **matchEquals** *(string) --*

      The value selected by the ``JsonPath`` expression must match what is supplied in
      the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
      target action configuration can be included as placeholders in this value by
      surrounding the action configuration key with curly brackets. For example, if the
      value supplied here is "refs/heads/{Branch}" and the target action has an action
      configuration property called "Branch" with a value of "master", the
      ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
      configuration properties for built-in action types, see `Pipeline Structure
      Reference Action Requirements
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      .
    """


_ClientListWebhooksResponsewebhooksdefinitionTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef],
        "authentication": str,
        "authenticationConfiguration": ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)


class ClientListWebhooksResponsewebhooksdefinitionTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionTypeDef
):
    """
    Type definition for `ClientListWebhooksResponsewebhooks` `definition`

    The detail returned for each webhook, such as the webhook authentication type and filter
    rules.

    - **name** *(string) --*

      The name of the webhook.

    - **targetPipeline** *(string) --*

      The name of the pipeline you want to connect to the webhook.

    - **targetAction** *(string) --*

      The name of the action in a pipeline you want to connect to the webhook. The action
      must be from the source (first) stage of the pipeline.

    - **filters** *(list) --*

      A list of rules applied to the body/payload sent in the POST request to a webhook URL.
      All defined rules must pass for the request to be accepted and the pipeline started.

      - *(dict) --*

        The event criteria that specify when a webhook notification is sent to your URL.

        - **jsonPath** *(string) --*

          A JsonPath expression that is applied to the body/payload of the webhook. The value
          selected by the JsonPath expression must match the value specified in the
          ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
          `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

        - **matchEquals** *(string) --*

          The value selected by the ``JsonPath`` expression must match what is supplied in
          the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
          target action configuration can be included as placeholders in this value by
          surrounding the action configuration key with curly brackets. For example, if the
          value supplied here is "refs/heads/{Branch}" and the target action has an action
          configuration property called "Branch" with a value of "master", the
          ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
          configuration properties for built-in action types, see `Pipeline Structure
          Reference Action Requirements
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          .

    - **authentication** *(string) --*

      Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

      * For information about the authentication scheme implemented by GITHUB_HMAC, see
      `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
      GitHub Developer website.

      * IP rejects webhooks trigger requests unless they originate from an IP address in the
      IP range whitelisted in the authentication configuration.

      * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

    - **authenticationConfiguration** *(dict) --*

      Properties that configure the authentication applied to incoming webhook trigger
      requests. The required properties depend on the authentication type. For GITHUB_HMAC,
      only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
      property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
      set.

      - **AllowedIPRange** *(string) --*

        The property used to configure acceptance of webhooks in an IP address range. For IP,
        only the ``AllowedIPRange`` property must be set. This property must be set to a
        valid CIDR range.

      - **SecretToken** *(string) --*

        The property used to configure GitHub authentication. For GITHUB_HMAC, only the
        ``SecretToken`` property must be set.
    """


_ClientListWebhooksResponsewebhookstagsTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhookstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListWebhooksResponsewebhookstagsTypeDef(
    _ClientListWebhooksResponsewebhookstagsTypeDef
):
    """
    Type definition for `ClientListWebhooksResponsewebhooks` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksTypeDef",
    {
        "definition": ClientListWebhooksResponsewebhooksdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ClientListWebhooksResponsewebhookstagsTypeDef],
    },
    total=False,
)


class ClientListWebhooksResponsewebhooksTypeDef(
    _ClientListWebhooksResponsewebhooksTypeDef
):
    """
    Type definition for `ClientListWebhooksResponse` `webhooks`

    The detail returned for each webhook after listing webhooks, such as the webhook URL, the
    webhook name, and the webhook ARN.

    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.

      - **name** *(string) --*

        The name of the webhook.

      - **targetPipeline** *(string) --*

        The name of the pipeline you want to connect to the webhook.

      - **targetAction** *(string) --*

        The name of the action in a pipeline you want to connect to the webhook. The action
        must be from the source (first) stage of the pipeline.

      - **filters** *(list) --*

        A list of rules applied to the body/payload sent in the POST request to a webhook URL.
        All defined rules must pass for the request to be accepted and the pipeline started.

        - *(dict) --*

          The event criteria that specify when a webhook notification is sent to your URL.

          - **jsonPath** *(string) --*

            A JsonPath expression that is applied to the body/payload of the webhook. The value
            selected by the JsonPath expression must match the value specified in the
            ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
            `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

          - **matchEquals** *(string) --*

            The value selected by the ``JsonPath`` expression must match what is supplied in
            the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
            target action configuration can be included as placeholders in this value by
            surrounding the action configuration key with curly brackets. For example, if the
            value supplied here is "refs/heads/{Branch}" and the target action has an action
            configuration property called "Branch" with a value of "master", the
            ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
            configuration properties for built-in action types, see `Pipeline Structure
            Reference Action Requirements
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
            .

      - **authentication** *(string) --*

        Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

        * For information about the authentication scheme implemented by GITHUB_HMAC, see
        `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
        GitHub Developer website.

        * IP rejects webhooks trigger requests unless they originate from an IP address in the
        IP range whitelisted in the authentication configuration.

        * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

      - **authenticationConfiguration** *(dict) --*

        Properties that configure the authentication applied to incoming webhook trigger
        requests. The required properties depend on the authentication type. For GITHUB_HMAC,
        only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
        property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
        set.

        - **AllowedIPRange** *(string) --*

          The property used to configure acceptance of webhooks in an IP address range. For IP,
          only the ``AllowedIPRange`` property must be set. This property must be set to a
          valid CIDR range.

        - **SecretToken** *(string) --*

          The property used to configure GitHub authentication. For GITHUB_HMAC, only the
          ``SecretToken`` property must be set.

    - **url** *(string) --*

      A unique URL generated by CodePipeline. When a POST request is made to this URL, the
      defined pipeline is started as long as the body of the post request satisfies the defined
      authentication and filtering conditions. Deleting and re-creating a webhook makes the old
      URL invalid and generates a new one.

    - **errorMessage** *(string) --*

      The text of the error message about the webhook.

    - **errorCode** *(string) --*

      The number code of the error.

    - **lastTriggered** *(datetime) --*

      The date and time a webhook was last successfully triggered, in timestamp format.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the webhook.

    - **tags** *(list) --*

      Specifies the tags applied to the webhook.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_ClientListWebhooksResponseTypeDef = TypedDict(
    "_ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "NextToken": str},
    total=False,
)


class ClientListWebhooksResponseTypeDef(_ClientListWebhooksResponseTypeDef):
    """
    Type definition for `ClientListWebhooks` `Response`

    - **webhooks** *(list) --*

      The JSON detail returned for each webhook in the list output for the ListWebhooks call.

      - *(dict) --*

        The detail returned for each webhook after listing webhooks, such as the webhook URL, the
        webhook name, and the webhook ARN.

        - **definition** *(dict) --*

          The detail returned for each webhook, such as the webhook authentication type and filter
          rules.

          - **name** *(string) --*

            The name of the webhook.

          - **targetPipeline** *(string) --*

            The name of the pipeline you want to connect to the webhook.

          - **targetAction** *(string) --*

            The name of the action in a pipeline you want to connect to the webhook. The action
            must be from the source (first) stage of the pipeline.

          - **filters** *(list) --*

            A list of rules applied to the body/payload sent in the POST request to a webhook URL.
            All defined rules must pass for the request to be accepted and the pipeline started.

            - *(dict) --*

              The event criteria that specify when a webhook notification is sent to your URL.

              - **jsonPath** *(string) --*

                A JsonPath expression that is applied to the body/payload of the webhook. The value
                selected by the JsonPath expression must match the value specified in the
                ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
                `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

              - **matchEquals** *(string) --*

                The value selected by the ``JsonPath`` expression must match what is supplied in
                the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
                target action configuration can be included as placeholders in this value by
                surrounding the action configuration key with curly brackets. For example, if the
                value supplied here is "refs/heads/{Branch}" and the target action has an action
                configuration property called "Branch" with a value of "master", the
                ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
                configuration properties for built-in action types, see `Pipeline Structure
                Reference Action Requirements
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
                .

          - **authentication** *(string) --*

            Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

            * For information about the authentication scheme implemented by GITHUB_HMAC, see
            `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
            GitHub Developer website.

            * IP rejects webhooks trigger requests unless they originate from an IP address in the
            IP range whitelisted in the authentication configuration.

            * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

          - **authenticationConfiguration** *(dict) --*

            Properties that configure the authentication applied to incoming webhook trigger
            requests. The required properties depend on the authentication type. For GITHUB_HMAC,
            only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
            property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
            set.

            - **AllowedIPRange** *(string) --*

              The property used to configure acceptance of webhooks in an IP address range. For IP,
              only the ``AllowedIPRange`` property must be set. This property must be set to a
              valid CIDR range.

            - **SecretToken** *(string) --*

              The property used to configure GitHub authentication. For GITHUB_HMAC, only the
              ``SecretToken`` property must be set.

        - **url** *(string) --*

          A unique URL generated by CodePipeline. When a POST request is made to this URL, the
          defined pipeline is started as long as the body of the post request satisfies the defined
          authentication and filtering conditions. Deleting and re-creating a webhook makes the old
          URL invalid and generates a new one.

        - **errorMessage** *(string) --*

          The text of the error message about the webhook.

        - **errorCode** *(string) --*

          The number code of the error.

        - **lastTriggered** *(datetime) --*

          The date and time a webhook was last successfully triggered, in timestamp format.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the webhook.

        - **tags** *(list) --*

          Specifies the tags applied to the webhook.

          - *(dict) --*

            A tag is a key-value pair that is used to manage the resource.

            - **key** *(string) --*

              The tag's key.

            - **value** *(string) --*

              The tag's value.

    - **NextToken** *(string) --*

      If the amount of returned information is significantly large, an identifier is also returned
      and can be used in a subsequent ListWebhooks call to return the next set of webhooks in the
      list.
    """


_ClientPollForJobsResponsejobsdataactionConfigurationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientPollForJobsResponsejobsdataactionConfigurationTypeDef(
    _ClientPollForJobsResponsejobsdataactionConfigurationTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `actionConfiguration`

    Represents information about an action configuration.

    - **configuration** *(dict) --*

      The configuration data for the action.

      - *(string) --*

        - *(string) --*
    """


_ClientPollForJobsResponsejobsdataactionTypeIdTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataactionTypeIdTypeDef(
    _ClientPollForJobsResponsejobsdataactionTypeIdTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category type
      might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
      more information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef(
    _ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `artifactCredentials`

    Represents an AWS session credentials object. These credentials are temporary
    credentials that are issued by AWS Secure Token Service (STS). They can be used to
    access input and output artifacts in the Amazon S3 bucket used to store artifacts for
    the pipeline in AWS CodePipeline.

    - **accessKeyId** *(string) --*

      The access key for the session.

    - **secretAccessKey** *(string) --*

      The secret access key for the session.

    - **sessionToken** *(string) --*

      The token for the session.
    """


_ClientPollForJobsResponsejobsdataencryptionKeyTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataencryptionKeyTypeDef(
    _ClientPollForJobsResponsejobsdataencryptionKeyTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `encryptionKey`

    Represents information about the key used to encrypt data in the artifact store, such
    as an AWS Key Management Service (AWS KMS) key.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to
        identify the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdatainputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdatainputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientPollForJobsResponsejobsdatainputArtifactsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactsTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactsTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `inputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdataoutputArtifactslocation` `s3Location`

    The Amazon S3 bucket that contains the artifact.

    - **bucketName** *(string) --*

      The name of the Amazon S3 bucket.

    - **objectKey** *(string) --*

      The key of the object in the Amazon S3 bucket, which uniquely identifies the
      object in the bucket.
    """


_ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdataoutputArtifacts` `location`

    The location of an artifact.

    - **type** *(string) --*

      The type of artifact in the location.

    - **s3Location** *(dict) --*

      The Amazon S3 bucket that contains the artifact.

      - **bucketName** *(string) --*

        The name of the Amazon S3 bucket.

      - **objectKey** *(string) --*

        The key of the object in the Amazon S3 bucket, which uniquely identifies the
        object in the bucket.
    """


_ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `outputArtifacts`

    Represents information about an artifact that is worked on by actions in the pipeline.

    - **name** *(string) --*

      The artifact's name.

    - **revision** *(string) --*

      The artifact's revision ID. Depending on the type of object, this could be a commit
      ID (GitHub) or a revision ID (Amazon S3).

    - **location** *(dict) --*

      The location of an artifact.

      - **type** *(string) --*

        The type of artifact in the location.

      - **s3Location** *(dict) --*

        The Amazon S3 bucket that contains the artifact.

        - **bucketName** *(string) --*

          The name of the Amazon S3 bucket.

        - **objectKey** *(string) --*

          The key of the object in the Amazon S3 bucket, which uniquely identifies the
          object in the bucket.
    """


_ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdatapipelineContext` `action`

    The context of an action to a job worker in the stage of a pipeline.

    - **name** *(string) --*

      The name of the action in the context of a job.

    - **actionExecutionId** *(string) --*

      The system-generated unique ID that corresponds to an action's execution.
    """


_ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)


class ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdatapipelineContext` `stage`

    The stage of the pipeline.

    - **name** *(string) --*

      The name of the stage.
    """


_ClientPollForJobsResponsejobsdatapipelineContextTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef,
        "action": ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatapipelineContextTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobsdata` `pipelineContext`

    Represents information about a pipeline to a job worker.

    .. note::

      Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

    - **pipelineName** *(string) --*

      The name of the pipeline. This is a user-specified value. Pipeline names must be
      unique across all pipeline names under an Amazon Web Services account.

    - **stage** *(dict) --*

      The stage of the pipeline.

      - **name** *(string) --*

        The name of the stage.

    - **action** *(dict) --*

      The context of an action to a job worker in the stage of a pipeline.

      - **name** *(string) --*

        The name of the action in the context of a job.

      - **actionExecutionId** *(string) --*

        The system-generated unique ID that corresponds to an action's execution.

    - **pipelineArn** *(string) --*

      The Amazon Resource Name (ARN) of the pipeline.

    - **pipelineExecutionId** *(string) --*

      The execution ID of the pipeline.
    """


_ClientPollForJobsResponsejobsdataTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataTypeDef",
    {
        "actionTypeId": ClientPollForJobsResponsejobsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientPollForJobsResponsejobsdataactionConfigurationTypeDef,
        "pipelineContext": ClientPollForJobsResponsejobsdatapipelineContextTypeDef,
        "inputArtifacts": List[ClientPollForJobsResponsejobsdatainputArtifactsTypeDef],
        "outputArtifacts": List[
            ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef
        ],
        "artifactCredentials": ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientPollForJobsResponsejobsdataencryptionKeyTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataTypeDef(
    _ClientPollForJobsResponsejobsdataTypeDef
):
    """
    Type definition for `ClientPollForJobsResponsejobs` `data`

    Other data about a job.

    - **actionTypeId** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category type
        might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
        more information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **actionConfiguration** *(dict) --*

      Represents information about an action configuration.

      - **configuration** *(dict) --*

        The configuration data for the action.

        - *(string) --*

          - *(string) --*

    - **pipelineContext** *(dict) --*

      Represents information about a pipeline to a job worker.

      .. note::

        Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

      - **pipelineName** *(string) --*

        The name of the pipeline. This is a user-specified value. Pipeline names must be
        unique across all pipeline names under an Amazon Web Services account.

      - **stage** *(dict) --*

        The stage of the pipeline.

        - **name** *(string) --*

          The name of the stage.

      - **action** *(dict) --*

        The context of an action to a job worker in the stage of a pipeline.

        - **name** *(string) --*

          The name of the action in the context of a job.

        - **actionExecutionId** *(string) --*

          The system-generated unique ID that corresponds to an action's execution.

      - **pipelineArn** *(string) --*

        The Amazon Resource Name (ARN) of the pipeline.

      - **pipelineExecutionId** *(string) --*

        The execution ID of the pipeline.

    - **inputArtifacts** *(list) --*

      The artifact supplied to the job.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **outputArtifacts** *(list) --*

      The output of the job.

      - *(dict) --*

        Represents information about an artifact that is worked on by actions in the pipeline.

        - **name** *(string) --*

          The artifact's name.

        - **revision** *(string) --*

          The artifact's revision ID. Depending on the type of object, this could be a commit
          ID (GitHub) or a revision ID (Amazon S3).

        - **location** *(dict) --*

          The location of an artifact.

          - **type** *(string) --*

            The type of artifact in the location.

          - **s3Location** *(dict) --*

            The Amazon S3 bucket that contains the artifact.

            - **bucketName** *(string) --*

              The name of the Amazon S3 bucket.

            - **objectKey** *(string) --*

              The key of the object in the Amazon S3 bucket, which uniquely identifies the
              object in the bucket.

    - **artifactCredentials** *(dict) --*

      Represents an AWS session credentials object. These credentials are temporary
      credentials that are issued by AWS Secure Token Service (STS). They can be used to
      access input and output artifacts in the Amazon S3 bucket used to store artifacts for
      the pipeline in AWS CodePipeline.

      - **accessKeyId** *(string) --*

        The access key for the session.

      - **secretAccessKey** *(string) --*

        The secret access key for the session.

      - **sessionToken** *(string) --*

        The token for the session.

    - **continuationToken** *(string) --*

      A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
      continue the job asynchronously.

    - **encryptionKey** *(dict) --*

      Represents information about the key used to encrypt data in the artifact store, such
      as an AWS Key Management Service (AWS KMS) key.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to
          identify the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientPollForJobsResponsejobsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsTypeDef",
    {
        "id": str,
        "data": ClientPollForJobsResponsejobsdataTypeDef,
        "nonce": str,
        "accountId": str,
    },
    total=False,
)


class ClientPollForJobsResponsejobsTypeDef(_ClientPollForJobsResponsejobsTypeDef):
    """
    Type definition for `ClientPollForJobsResponse` `jobs`

    Represents information about a job.

    - **id** *(string) --*

      The unique system-generated ID of the job.

    - **data** *(dict) --*

      Other data about a job.

      - **actionTypeId** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following
          values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are
          determined by the action category. For example, an action in the Deploy category type
          might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
          more information, see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **actionConfiguration** *(dict) --*

        Represents information about an action configuration.

        - **configuration** *(dict) --*

          The configuration data for the action.

          - *(string) --*

            - *(string) --*

      - **pipelineContext** *(dict) --*

        Represents information about a pipeline to a job worker.

        .. note::

          Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

        - **pipelineName** *(string) --*

          The name of the pipeline. This is a user-specified value. Pipeline names must be
          unique across all pipeline names under an Amazon Web Services account.

        - **stage** *(dict) --*

          The stage of the pipeline.

          - **name** *(string) --*

            The name of the stage.

        - **action** *(dict) --*

          The context of an action to a job worker in the stage of a pipeline.

          - **name** *(string) --*

            The name of the action in the context of a job.

          - **actionExecutionId** *(string) --*

            The system-generated unique ID that corresponds to an action's execution.

        - **pipelineArn** *(string) --*

          The Amazon Resource Name (ARN) of the pipeline.

        - **pipelineExecutionId** *(string) --*

          The execution ID of the pipeline.

      - **inputArtifacts** *(list) --*

        The artifact supplied to the job.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **outputArtifacts** *(list) --*

        The output of the job.

        - *(dict) --*

          Represents information about an artifact that is worked on by actions in the pipeline.

          - **name** *(string) --*

            The artifact's name.

          - **revision** *(string) --*

            The artifact's revision ID. Depending on the type of object, this could be a commit
            ID (GitHub) or a revision ID (Amazon S3).

          - **location** *(dict) --*

            The location of an artifact.

            - **type** *(string) --*

              The type of artifact in the location.

            - **s3Location** *(dict) --*

              The Amazon S3 bucket that contains the artifact.

              - **bucketName** *(string) --*

                The name of the Amazon S3 bucket.

              - **objectKey** *(string) --*

                The key of the object in the Amazon S3 bucket, which uniquely identifies the
                object in the bucket.

      - **artifactCredentials** *(dict) --*

        Represents an AWS session credentials object. These credentials are temporary
        credentials that are issued by AWS Secure Token Service (STS). They can be used to
        access input and output artifacts in the Amazon S3 bucket used to store artifacts for
        the pipeline in AWS CodePipeline.

        - **accessKeyId** *(string) --*

          The access key for the session.

        - **secretAccessKey** *(string) --*

          The secret access key for the session.

        - **sessionToken** *(string) --*

          The token for the session.

      - **continuationToken** *(string) --*

        A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
        continue the job asynchronously.

      - **encryptionKey** *(dict) --*

        Represents information about the key used to encrypt data in the artifact store, such
        as an AWS Key Management Service (AWS KMS) key.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to
            identify the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **nonce** *(string) --*

      A system-generated random number that AWS CodePipeline uses to ensure that the job is
      being worked on by only one job worker. Use this number in an  AcknowledgeJob request.

    - **accountId** *(string) --*

      The ID of the AWS account to use when performing the job.
    """


_ClientPollForJobsResponseTypeDef = TypedDict(
    "_ClientPollForJobsResponseTypeDef",
    {"jobs": List[ClientPollForJobsResponsejobsTypeDef]},
    total=False,
)


class ClientPollForJobsResponseTypeDef(_ClientPollForJobsResponseTypeDef):
    """
    Type definition for `ClientPollForJobs` `Response`

    Represents the output of a ``PollForJobs`` action.

    - **jobs** *(list) --*

      Information about the jobs to take action on.

      - *(dict) --*

        Represents information about a job.

        - **id** *(string) --*

          The unique system-generated ID of the job.

        - **data** *(dict) --*

          Other data about a job.

          - **actionTypeId** *(dict) --*

            Represents information about an action type.

            - **category** *(string) --*

              A category defines what kind of action can be taken in the stage, and constrains the
              provider type for the action. Valid categories are limited to one of the following
              values.

            - **owner** *(string) --*

              The creator of the action being called.

            - **provider** *(string) --*

              The provider of the service being called by the action. Valid providers are
              determined by the action category. For example, an action in the Deploy category type
              might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
              more information, see `Valid Action Types and Providers in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
              .

            - **version** *(string) --*

              A string that describes the action version.

          - **actionConfiguration** *(dict) --*

            Represents information about an action configuration.

            - **configuration** *(dict) --*

              The configuration data for the action.

              - *(string) --*

                - *(string) --*

          - **pipelineContext** *(dict) --*

            Represents information about a pipeline to a job worker.

            .. note::

              Includes ``pipelineArn`` and ``pipelineExecutionId`` for custom jobs.

            - **pipelineName** *(string) --*

              The name of the pipeline. This is a user-specified value. Pipeline names must be
              unique across all pipeline names under an Amazon Web Services account.

            - **stage** *(dict) --*

              The stage of the pipeline.

              - **name** *(string) --*

                The name of the stage.

            - **action** *(dict) --*

              The context of an action to a job worker in the stage of a pipeline.

              - **name** *(string) --*

                The name of the action in the context of a job.

              - **actionExecutionId** *(string) --*

                The system-generated unique ID that corresponds to an action's execution.

            - **pipelineArn** *(string) --*

              The Amazon Resource Name (ARN) of the pipeline.

            - **pipelineExecutionId** *(string) --*

              The execution ID of the pipeline.

          - **inputArtifacts** *(list) --*

            The artifact supplied to the job.

            - *(dict) --*

              Represents information about an artifact that is worked on by actions in the pipeline.

              - **name** *(string) --*

                The artifact's name.

              - **revision** *(string) --*

                The artifact's revision ID. Depending on the type of object, this could be a commit
                ID (GitHub) or a revision ID (Amazon S3).

              - **location** *(dict) --*

                The location of an artifact.

                - **type** *(string) --*

                  The type of artifact in the location.

                - **s3Location** *(dict) --*

                  The Amazon S3 bucket that contains the artifact.

                  - **bucketName** *(string) --*

                    The name of the Amazon S3 bucket.

                  - **objectKey** *(string) --*

                    The key of the object in the Amazon S3 bucket, which uniquely identifies the
                    object in the bucket.

          - **outputArtifacts** *(list) --*

            The output of the job.

            - *(dict) --*

              Represents information about an artifact that is worked on by actions in the pipeline.

              - **name** *(string) --*

                The artifact's name.

              - **revision** *(string) --*

                The artifact's revision ID. Depending on the type of object, this could be a commit
                ID (GitHub) or a revision ID (Amazon S3).

              - **location** *(dict) --*

                The location of an artifact.

                - **type** *(string) --*

                  The type of artifact in the location.

                - **s3Location** *(dict) --*

                  The Amazon S3 bucket that contains the artifact.

                  - **bucketName** *(string) --*

                    The name of the Amazon S3 bucket.

                  - **objectKey** *(string) --*

                    The key of the object in the Amazon S3 bucket, which uniquely identifies the
                    object in the bucket.

          - **artifactCredentials** *(dict) --*

            Represents an AWS session credentials object. These credentials are temporary
            credentials that are issued by AWS Secure Token Service (STS). They can be used to
            access input and output artifacts in the Amazon S3 bucket used to store artifacts for
            the pipeline in AWS CodePipeline.

            - **accessKeyId** *(string) --*

              The access key for the session.

            - **secretAccessKey** *(string) --*

              The secret access key for the session.

            - **sessionToken** *(string) --*

              The token for the session.

          - **continuationToken** *(string) --*

            A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to
            continue the job asynchronously.

          - **encryptionKey** *(dict) --*

            Represents information about the key used to encrypt data in the artifact store, such
            as an AWS Key Management Service (AWS KMS) key.

            - **id** *(string) --*

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
              ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to
                identify the key.

            - **type** *(string) --*

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
              creating or updating a pipeline, the value must be set to 'KMS'.

        - **nonce** *(string) --*

          A system-generated random number that AWS CodePipeline uses to ensure that the job is
          being worked on by only one job worker. Use this number in an  AcknowledgeJob request.

        - **accountId** *(string) --*

          The ID of the AWS account to use when performing the job.
    """


_ClientPollForJobsactionTypeIdTypeDef = TypedDict(
    "_ClientPollForJobsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
)


class ClientPollForJobsactionTypeIdTypeDef(_ClientPollForJobsactionTypeIdTypeDef):
    """
    Type definition for `ClientPollForJobs` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --* **[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the provider
      type for the action. Valid categories are limited to one of the following values.

    - **owner** *(string) --* **[REQUIRED]**

      The creator of the action being called.

    - **provider** *(string) --* **[REQUIRED]**

      The provider of the service being called by the action. Valid providers are determined by the
      action category. For example, an action in the Deploy category type might have a provider of
      AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see `Valid Action
      Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --* **[REQUIRED]**

      A string that describes the action version.
    """


_ClientPollForThirdPartyJobsResponsejobsTypeDef = TypedDict(
    "_ClientPollForThirdPartyJobsResponsejobsTypeDef",
    {"clientId": str, "jobId": str},
    total=False,
)


class ClientPollForThirdPartyJobsResponsejobsTypeDef(
    _ClientPollForThirdPartyJobsResponsejobsTypeDef
):
    """
    Type definition for `ClientPollForThirdPartyJobsResponse` `jobs`

    A response to a ``PollForThirdPartyJobs`` request returned by AWS CodePipeline when there
    is a job to be worked on by a partner action.

    - **clientId** *(string) --*

      The ``clientToken`` portion of the ``clientId`` and ``clientToken`` pair used to verify
      that the calling entity is allowed access to the job and its details.

    - **jobId** *(string) --*

      The identifier used to identify the job in AWS CodePipeline.
    """


_ClientPollForThirdPartyJobsResponseTypeDef = TypedDict(
    "_ClientPollForThirdPartyJobsResponseTypeDef",
    {"jobs": List[ClientPollForThirdPartyJobsResponsejobsTypeDef]},
    total=False,
)


class ClientPollForThirdPartyJobsResponseTypeDef(
    _ClientPollForThirdPartyJobsResponseTypeDef
):
    """
    Type definition for `ClientPollForThirdPartyJobs` `Response`

    Represents the output of a ``PollForThirdPartyJobs`` action.

    - **jobs** *(list) --*

      Information about the jobs to take action on.

      - *(dict) --*

        A response to a ``PollForThirdPartyJobs`` request returned by AWS CodePipeline when there
        is a job to be worked on by a partner action.

        - **clientId** *(string) --*

          The ``clientToken`` portion of the ``clientId`` and ``clientToken`` pair used to verify
          that the calling entity is allowed access to the job and its details.

        - **jobId** *(string) --*

          The identifier used to identify the job in AWS CodePipeline.
    """


_ClientPollForThirdPartyJobsactionTypeIdTypeDef = TypedDict(
    "_ClientPollForThirdPartyJobsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
)


class ClientPollForThirdPartyJobsactionTypeIdTypeDef(
    _ClientPollForThirdPartyJobsactionTypeIdTypeDef
):
    """
    Type definition for `ClientPollForThirdPartyJobs` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --* **[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the provider
      type for the action. Valid categories are limited to one of the following values.

    - **owner** *(string) --* **[REQUIRED]**

      The creator of the action being called.

    - **provider** *(string) --* **[REQUIRED]**

      The provider of the service being called by the action. Valid providers are determined by the
      action category. For example, an action in the Deploy category type might have a provider of
      AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see `Valid Action
      Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --* **[REQUIRED]**

      A string that describes the action version.
    """


_ClientPutActionRevisionResponseTypeDef = TypedDict(
    "_ClientPutActionRevisionResponseTypeDef",
    {"newRevision": bool, "pipelineExecutionId": str},
    total=False,
)


class ClientPutActionRevisionResponseTypeDef(_ClientPutActionRevisionResponseTypeDef):
    """
    Type definition for `ClientPutActionRevision` `Response`

    Represents the output of a ``PutActionRevision`` action.

    - **newRevision** *(boolean) --*

      Indicates whether the artifact revision was previously used in an execution of the specified
      pipeline.

    - **pipelineExecutionId** *(string) --*

      The ID of the current workflow state of the pipeline.
    """


_ClientPutActionRevisionactionRevisionTypeDef = TypedDict(
    "_ClientPutActionRevisionactionRevisionTypeDef",
    {"revisionId": str, "revisionChangeId": str, "created": datetime},
)


class ClientPutActionRevisionactionRevisionTypeDef(
    _ClientPutActionRevisionactionRevisionTypeDef
):
    """
    Type definition for `ClientPutActionRevision` `actionRevision`

    Represents information about the version (or revision) of an action.

    - **revisionId** *(string) --* **[REQUIRED]**

      The system-generated unique ID that identifies the revision number of the action.

    - **revisionChangeId** *(string) --* **[REQUIRED]**

      The unique identifier of the change that set the state to this revision (for example, a
      deployment ID or timestamp).

    - **created** *(datetime) --* **[REQUIRED]**

      The date and time when the most recent version of the action was created, in timestamp format.
    """


_ClientPutApprovalResultResponseTypeDef = TypedDict(
    "_ClientPutApprovalResultResponseTypeDef", {"approvedAt": datetime}, total=False
)


class ClientPutApprovalResultResponseTypeDef(_ClientPutApprovalResultResponseTypeDef):
    """
    Type definition for `ClientPutApprovalResult` `Response`

    Represents the output of a ``PutApprovalResult`` action.

    - **approvedAt** *(datetime) --*

      The timestamp showing when the approval or rejection was submitted.
    """


_ClientPutApprovalResultresultTypeDef = TypedDict(
    "_ClientPutApprovalResultresultTypeDef", {"summary": str, "status": str}
)


class ClientPutApprovalResultresultTypeDef(_ClientPutApprovalResultresultTypeDef):
    """
    Type definition for `ClientPutApprovalResult` `result`

    Represents information about the result of the approval request.

    - **summary** *(string) --* **[REQUIRED]**

      The summary of the current status of the approval request.

    - **status** *(string) --* **[REQUIRED]**

      The response submitted by a reviewer assigned to an approval action request.
    """


_RequiredClientPutJobFailureResultfailureDetailsTypeDef = TypedDict(
    "_RequiredClientPutJobFailureResultfailureDetailsTypeDef",
    {"type": str, "message": str},
)
_OptionalClientPutJobFailureResultfailureDetailsTypeDef = TypedDict(
    "_OptionalClientPutJobFailureResultfailureDetailsTypeDef",
    {"externalExecutionId": str},
    total=False,
)


class ClientPutJobFailureResultfailureDetailsTypeDef(
    _RequiredClientPutJobFailureResultfailureDetailsTypeDef,
    _OptionalClientPutJobFailureResultfailureDetailsTypeDef,
):
    """
    Type definition for `ClientPutJobFailureResult` `failureDetails`

    The details about the failure of a job.

    - **type** *(string) --* **[REQUIRED]**

      The type of the failure.

    - **message** *(string) --* **[REQUIRED]**

      The message about the failure.

    - **externalExecutionId** *(string) --*

      The external ID of the run of the action that failed.
    """


_RequiredClientPutJobSuccessResultcurrentRevisionTypeDef = TypedDict(
    "_RequiredClientPutJobSuccessResultcurrentRevisionTypeDef",
    {"revision": str, "changeIdentifier": str},
)
_OptionalClientPutJobSuccessResultcurrentRevisionTypeDef = TypedDict(
    "_OptionalClientPutJobSuccessResultcurrentRevisionTypeDef",
    {"created": datetime, "revisionSummary": str},
    total=False,
)


class ClientPutJobSuccessResultcurrentRevisionTypeDef(
    _RequiredClientPutJobSuccessResultcurrentRevisionTypeDef,
    _OptionalClientPutJobSuccessResultcurrentRevisionTypeDef,
):
    """
    Type definition for `ClientPutJobSuccessResult` `currentRevision`

    The ID of the current revision of the artifact successfully worked on by the job.

    - **revision** *(string) --* **[REQUIRED]**

      The revision ID of the current version of an artifact.

    - **changeIdentifier** *(string) --* **[REQUIRED]**

      The change identifier for the current revision.

    - **created** *(datetime) --*

      The date and time when the most recent revision of the artifact was created, in timestamp
      format.

    - **revisionSummary** *(string) --*

      The summary of the most recent revision of the artifact.
    """


_ClientPutJobSuccessResultexecutionDetailsTypeDef = TypedDict(
    "_ClientPutJobSuccessResultexecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)


class ClientPutJobSuccessResultexecutionDetailsTypeDef(
    _ClientPutJobSuccessResultexecutionDetailsTypeDef
):
    """
    Type definition for `ClientPutJobSuccessResult` `executionDetails`

    The execution details of the successful job, such as the actions taken by the job worker.

    - **summary** *(string) --*

      The summary of the current status of the actions.

    - **externalExecutionId** *(string) --*

      The system-generated unique ID of this action used to identify this job worker in any external
      systems, such as AWS CodeDeploy.

    - **percentComplete** *(integer) --*

      The percentage of work completed on the action, represented on a scale of 0 to 100 percent.
    """


_RequiredClientPutThirdPartyJobFailureResultfailureDetailsTypeDef = TypedDict(
    "_RequiredClientPutThirdPartyJobFailureResultfailureDetailsTypeDef",
    {"type": str, "message": str},
)
_OptionalClientPutThirdPartyJobFailureResultfailureDetailsTypeDef = TypedDict(
    "_OptionalClientPutThirdPartyJobFailureResultfailureDetailsTypeDef",
    {"externalExecutionId": str},
    total=False,
)


class ClientPutThirdPartyJobFailureResultfailureDetailsTypeDef(
    _RequiredClientPutThirdPartyJobFailureResultfailureDetailsTypeDef,
    _OptionalClientPutThirdPartyJobFailureResultfailureDetailsTypeDef,
):
    """
    Type definition for `ClientPutThirdPartyJobFailureResult` `failureDetails`

    Represents information about failure details.

    - **type** *(string) --* **[REQUIRED]**

      The type of the failure.

    - **message** *(string) --* **[REQUIRED]**

      The message about the failure.

    - **externalExecutionId** *(string) --*

      The external ID of the run of the action that failed.
    """


_RequiredClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef = TypedDict(
    "_RequiredClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef",
    {"revision": str, "changeIdentifier": str},
)
_OptionalClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef = TypedDict(
    "_OptionalClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef",
    {"created": datetime, "revisionSummary": str},
    total=False,
)


class ClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef(
    _RequiredClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef,
    _OptionalClientPutThirdPartyJobSuccessResultcurrentRevisionTypeDef,
):
    """
    Type definition for `ClientPutThirdPartyJobSuccessResult` `currentRevision`

    Represents information about a current revision.

    - **revision** *(string) --* **[REQUIRED]**

      The revision ID of the current version of an artifact.

    - **changeIdentifier** *(string) --* **[REQUIRED]**

      The change identifier for the current revision.

    - **created** *(datetime) --*

      The date and time when the most recent revision of the artifact was created, in timestamp
      format.

    - **revisionSummary** *(string) --*

      The summary of the most recent revision of the artifact.
    """


_ClientPutThirdPartyJobSuccessResultexecutionDetailsTypeDef = TypedDict(
    "_ClientPutThirdPartyJobSuccessResultexecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)


class ClientPutThirdPartyJobSuccessResultexecutionDetailsTypeDef(
    _ClientPutThirdPartyJobSuccessResultexecutionDetailsTypeDef
):
    """
    Type definition for `ClientPutThirdPartyJobSuccessResult` `executionDetails`

    The details of the actions taken and results produced on an artifact as it passes through stages
    in the pipeline.

    - **summary** *(string) --*

      The summary of the current status of the actions.

    - **externalExecutionId** *(string) --*

      The system-generated unique ID of this action used to identify this job worker in any external
      systems, such as AWS CodeDeploy.

    - **percentComplete** *(integer) --*

      The percentage of work completed on the action, represented on a scale of 0 to 100 percent.
    """


_ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef
):
    """
    Type definition for `ClientPutWebhookResponsewebhookdefinition` `authenticationConfiguration`

    Properties that configure the authentication applied to incoming webhook trigger
    requests. The required properties depend on the authentication type. For GITHUB_HMAC,
    only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
    property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

    - **AllowedIPRange** *(string) --*

      The property used to configure acceptance of webhooks in an IP address range. For IP,
      only the ``AllowedIPRange`` property must be set. This property must be set to a valid
      CIDR range.

    - **SecretToken** *(string) --*

      The property used to configure GitHub authentication. For GITHUB_HMAC, only the
      ``SecretToken`` property must be set.
    """


_ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef
):
    """
    Type definition for `ClientPutWebhookResponsewebhookdefinition` `filters`

    The event criteria that specify when a webhook notification is sent to your URL.

    - **jsonPath** *(string) --*

      A JsonPath expression that is applied to the body/payload of the webhook. The value
      selected by the JsonPath expression must match the value specified in the
      ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
      `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

    - **matchEquals** *(string) --*

      The value selected by the ``JsonPath`` expression must match what is supplied in the
      ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target
      action configuration can be included as placeholders in this value by surrounding the
      action configuration key with curly brackets. For example, if the value supplied here
      is "refs/heads/{Branch}" and the target action has an action configuration property
      called "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
      "refs/heads/master". For a list of action configuration properties for built-in
      action types, see `Pipeline Structure Reference Action Requirements
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      .
    """


_ClientPutWebhookResponsewebhookdefinitionTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef],
        "authentication": str,
        "authenticationConfiguration": ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)


class ClientPutWebhookResponsewebhookdefinitionTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionTypeDef
):
    """
    Type definition for `ClientPutWebhookResponsewebhook` `definition`

    The detail returned for each webhook, such as the webhook authentication type and filter
    rules.

    - **name** *(string) --*

      The name of the webhook.

    - **targetPipeline** *(string) --*

      The name of the pipeline you want to connect to the webhook.

    - **targetAction** *(string) --*

      The name of the action in a pipeline you want to connect to the webhook. The action must
      be from the source (first) stage of the pipeline.

    - **filters** *(list) --*

      A list of rules applied to the body/payload sent in the POST request to a webhook URL.
      All defined rules must pass for the request to be accepted and the pipeline started.

      - *(dict) --*

        The event criteria that specify when a webhook notification is sent to your URL.

        - **jsonPath** *(string) --*

          A JsonPath expression that is applied to the body/payload of the webhook. The value
          selected by the JsonPath expression must match the value specified in the
          ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
          `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

        - **matchEquals** *(string) --*

          The value selected by the ``JsonPath`` expression must match what is supplied in the
          ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target
          action configuration can be included as placeholders in this value by surrounding the
          action configuration key with curly brackets. For example, if the value supplied here
          is "refs/heads/{Branch}" and the target action has an action configuration property
          called "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
          "refs/heads/master". For a list of action configuration properties for built-in
          action types, see `Pipeline Structure Reference Action Requirements
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          .

    - **authentication** *(string) --*

      Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

      * For information about the authentication scheme implemented by GITHUB_HMAC, see
      `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
      GitHub Developer website.

      * IP rejects webhooks trigger requests unless they originate from an IP address in the IP
      range whitelisted in the authentication configuration.

      * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

    - **authenticationConfiguration** *(dict) --*

      Properties that configure the authentication applied to incoming webhook trigger
      requests. The required properties depend on the authentication type. For GITHUB_HMAC,
      only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
      property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

      - **AllowedIPRange** *(string) --*

        The property used to configure acceptance of webhooks in an IP address range. For IP,
        only the ``AllowedIPRange`` property must be set. This property must be set to a valid
        CIDR range.

      - **SecretToken** *(string) --*

        The property used to configure GitHub authentication. For GITHUB_HMAC, only the
        ``SecretToken`` property must be set.
    """


_ClientPutWebhookResponsewebhooktagsTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhooktagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientPutWebhookResponsewebhooktagsTypeDef(
    _ClientPutWebhookResponsewebhooktagsTypeDef
):
    """
    Type definition for `ClientPutWebhookResponsewebhook` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientPutWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookTypeDef",
    {
        "definition": ClientPutWebhookResponsewebhookdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ClientPutWebhookResponsewebhooktagsTypeDef],
    },
    total=False,
)


class ClientPutWebhookResponsewebhookTypeDef(_ClientPutWebhookResponsewebhookTypeDef):
    """
    Type definition for `ClientPutWebhookResponse` `webhook`

    The detail returned from creating the webhook, such as the webhook name, webhook URL, and
    webhook ARN.

    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.

      - **name** *(string) --*

        The name of the webhook.

      - **targetPipeline** *(string) --*

        The name of the pipeline you want to connect to the webhook.

      - **targetAction** *(string) --*

        The name of the action in a pipeline you want to connect to the webhook. The action must
        be from the source (first) stage of the pipeline.

      - **filters** *(list) --*

        A list of rules applied to the body/payload sent in the POST request to a webhook URL.
        All defined rules must pass for the request to be accepted and the pipeline started.

        - *(dict) --*

          The event criteria that specify when a webhook notification is sent to your URL.

          - **jsonPath** *(string) --*

            A JsonPath expression that is applied to the body/payload of the webhook. The value
            selected by the JsonPath expression must match the value specified in the
            ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
            `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

          - **matchEquals** *(string) --*

            The value selected by the ``JsonPath`` expression must match what is supplied in the
            ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target
            action configuration can be included as placeholders in this value by surrounding the
            action configuration key with curly brackets. For example, if the value supplied here
            is "refs/heads/{Branch}" and the target action has an action configuration property
            called "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
            "refs/heads/master". For a list of action configuration properties for built-in
            action types, see `Pipeline Structure Reference Action Requirements
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
            .

      - **authentication** *(string) --*

        Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

        * For information about the authentication scheme implemented by GITHUB_HMAC, see
        `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
        GitHub Developer website.

        * IP rejects webhooks trigger requests unless they originate from an IP address in the IP
        range whitelisted in the authentication configuration.

        * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

      - **authenticationConfiguration** *(dict) --*

        Properties that configure the authentication applied to incoming webhook trigger
        requests. The required properties depend on the authentication type. For GITHUB_HMAC,
        only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
        property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

        - **AllowedIPRange** *(string) --*

          The property used to configure acceptance of webhooks in an IP address range. For IP,
          only the ``AllowedIPRange`` property must be set. This property must be set to a valid
          CIDR range.

        - **SecretToken** *(string) --*

          The property used to configure GitHub authentication. For GITHUB_HMAC, only the
          ``SecretToken`` property must be set.

    - **url** *(string) --*

      A unique URL generated by CodePipeline. When a POST request is made to this URL, the
      defined pipeline is started as long as the body of the post request satisfies the defined
      authentication and filtering conditions. Deleting and re-creating a webhook makes the old
      URL invalid and generates a new one.

    - **errorMessage** *(string) --*

      The text of the error message about the webhook.

    - **errorCode** *(string) --*

      The number code of the error.

    - **lastTriggered** *(datetime) --*

      The date and time a webhook was last successfully triggered, in timestamp format.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the webhook.

    - **tags** *(list) --*

      Specifies the tags applied to the webhook.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_ClientPutWebhookResponseTypeDef = TypedDict(
    "_ClientPutWebhookResponseTypeDef",
    {"webhook": ClientPutWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientPutWebhookResponseTypeDef(_ClientPutWebhookResponseTypeDef):
    """
    Type definition for `ClientPutWebhook` `Response`

    - **webhook** *(dict) --*

      The detail returned from creating the webhook, such as the webhook name, webhook URL, and
      webhook ARN.

      - **definition** *(dict) --*

        The detail returned for each webhook, such as the webhook authentication type and filter
        rules.

        - **name** *(string) --*

          The name of the webhook.

        - **targetPipeline** *(string) --*

          The name of the pipeline you want to connect to the webhook.

        - **targetAction** *(string) --*

          The name of the action in a pipeline you want to connect to the webhook. The action must
          be from the source (first) stage of the pipeline.

        - **filters** *(list) --*

          A list of rules applied to the body/payload sent in the POST request to a webhook URL.
          All defined rules must pass for the request to be accepted and the pipeline started.

          - *(dict) --*

            The event criteria that specify when a webhook notification is sent to your URL.

            - **jsonPath** *(string) --*

              A JsonPath expression that is applied to the body/payload of the webhook. The value
              selected by the JsonPath expression must match the value specified in the
              ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
              `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

            - **matchEquals** *(string) --*

              The value selected by the ``JsonPath`` expression must match what is supplied in the
              ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target
              action configuration can be included as placeholders in this value by surrounding the
              action configuration key with curly brackets. For example, if the value supplied here
              is "refs/heads/{Branch}" and the target action has an action configuration property
              called "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
              "refs/heads/master". For a list of action configuration properties for built-in
              action types, see `Pipeline Structure Reference Action Requirements
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              .

        - **authentication** *(string) --*

          Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

          * For information about the authentication scheme implemented by GITHUB_HMAC, see
          `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
          GitHub Developer website.

          * IP rejects webhooks trigger requests unless they originate from an IP address in the IP
          range whitelisted in the authentication configuration.

          * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

        - **authenticationConfiguration** *(dict) --*

          Properties that configure the authentication applied to incoming webhook trigger
          requests. The required properties depend on the authentication type. For GITHUB_HMAC,
          only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
          property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

          - **AllowedIPRange** *(string) --*

            The property used to configure acceptance of webhooks in an IP address range. For IP,
            only the ``AllowedIPRange`` property must be set. This property must be set to a valid
            CIDR range.

          - **SecretToken** *(string) --*

            The property used to configure GitHub authentication. For GITHUB_HMAC, only the
            ``SecretToken`` property must be set.

      - **url** *(string) --*

        A unique URL generated by CodePipeline. When a POST request is made to this URL, the
        defined pipeline is started as long as the body of the post request satisfies the defined
        authentication and filtering conditions. Deleting and re-creating a webhook makes the old
        URL invalid and generates a new one.

      - **errorMessage** *(string) --*

        The text of the error message about the webhook.

      - **errorCode** *(string) --*

        The number code of the error.

      - **lastTriggered** *(datetime) --*

        The date and time a webhook was last successfully triggered, in timestamp format.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the webhook.

      - **tags** *(list) --*

        Specifies the tags applied to the webhook.

        - *(dict) --*

          A tag is a key-value pair that is used to manage the resource.

          - **key** *(string) --*

            The tag's key.

          - **value** *(string) --*

            The tag's value.
    """


_ClientPutWebhooktagsTypeDef = TypedDict(
    "_ClientPutWebhooktagsTypeDef", {"key": str, "value": str}
)


class ClientPutWebhooktagsTypeDef(_ClientPutWebhooktagsTypeDef):
    """
    Type definition for `ClientPutWebhook` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientPutWebhookwebhookauthenticationConfigurationTypeDef = TypedDict(
    "_ClientPutWebhookwebhookauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientPutWebhookwebhookauthenticationConfigurationTypeDef(
    _ClientPutWebhookwebhookauthenticationConfigurationTypeDef
):
    """
    Type definition for `ClientPutWebhookwebhook` `authenticationConfiguration`

    Properties that configure the authentication applied to incoming webhook trigger requests. The
    required properties depend on the authentication type. For GITHUB_HMAC, only the
    ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange`` property must be set
    to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

    - **AllowedIPRange** *(string) --*

      The property used to configure acceptance of webhooks in an IP address range. For IP, only
      the ``AllowedIPRange`` property must be set. This property must be set to a valid CIDR range.

    - **SecretToken** *(string) --*

      The property used to configure GitHub authentication. For GITHUB_HMAC, only the
      ``SecretToken`` property must be set.
    """


_RequiredClientPutWebhookwebhookfiltersTypeDef = TypedDict(
    "_RequiredClientPutWebhookwebhookfiltersTypeDef", {"jsonPath": str}
)
_OptionalClientPutWebhookwebhookfiltersTypeDef = TypedDict(
    "_OptionalClientPutWebhookwebhookfiltersTypeDef", {"matchEquals": str}, total=False
)


class ClientPutWebhookwebhookfiltersTypeDef(
    _RequiredClientPutWebhookwebhookfiltersTypeDef,
    _OptionalClientPutWebhookwebhookfiltersTypeDef,
):
    """
    Type definition for `ClientPutWebhookwebhook` `filters`

    The event criteria that specify when a webhook notification is sent to your URL.

    - **jsonPath** *(string) --* **[REQUIRED]**

      A JsonPath expression that is applied to the body/payload of the webhook. The value
      selected by the JsonPath expression must match the value specified in the ``MatchEquals``
      field. Otherwise, the request is ignored. For more information, see `Java JsonPath
      implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

    - **matchEquals** *(string) --*

      The value selected by the ``JsonPath`` expression must match what is supplied in the
      ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target action
      configuration can be included as placeholders in this value by surrounding the action
      configuration key with curly brackets. For example, if the value supplied here is
      "refs/heads/{Branch}" and the target action has an action configuration property called
      "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
      "refs/heads/master". For a list of action configuration properties for built-in action
      types, see `Pipeline Structure Reference Action Requirements
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      .
    """


_ClientPutWebhookwebhookTypeDef = TypedDict(
    "_ClientPutWebhookwebhookTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientPutWebhookwebhookfiltersTypeDef],
        "authentication": str,
        "authenticationConfiguration": ClientPutWebhookwebhookauthenticationConfigurationTypeDef,
    },
)


class ClientPutWebhookwebhookTypeDef(_ClientPutWebhookwebhookTypeDef):
    """
    Type definition for `ClientPutWebhook` `webhook`

    The detail provided in an input file to create the webhook, such as the webhook name, the
    pipeline name, and the action name. Give the webhook a unique name that helps you identify it.
    You might name the webhook after the pipeline and action it targets so that you can easily
    recognize what it's used for later.

    - **name** *(string) --* **[REQUIRED]**

      The name of the webhook.

    - **targetPipeline** *(string) --* **[REQUIRED]**

      The name of the pipeline you want to connect to the webhook.

    - **targetAction** *(string) --* **[REQUIRED]**

      The name of the action in a pipeline you want to connect to the webhook. The action must be
      from the source (first) stage of the pipeline.

    - **filters** *(list) --* **[REQUIRED]**

      A list of rules applied to the body/payload sent in the POST request to a webhook URL. All
      defined rules must pass for the request to be accepted and the pipeline started.

      - *(dict) --*

        The event criteria that specify when a webhook notification is sent to your URL.

        - **jsonPath** *(string) --* **[REQUIRED]**

          A JsonPath expression that is applied to the body/payload of the webhook. The value
          selected by the JsonPath expression must match the value specified in the ``MatchEquals``
          field. Otherwise, the request is ignored. For more information, see `Java JsonPath
          implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

        - **matchEquals** *(string) --*

          The value selected by the ``JsonPath`` expression must match what is supplied in the
          ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the target action
          configuration can be included as placeholders in this value by surrounding the action
          configuration key with curly brackets. For example, if the value supplied here is
          "refs/heads/{Branch}" and the target action has an action configuration property called
          "Branch" with a value of "master", the ``MatchEquals`` value is evaluated as
          "refs/heads/master". For a list of action configuration properties for built-in action
          types, see `Pipeline Structure Reference Action Requirements
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          .

    - **authentication** *(string) --* **[REQUIRED]**

      Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

      * For information about the authentication scheme implemented by GITHUB_HMAC, see `Securing
      your webhooks <https://developer.github.com/webhooks/securing/>`__ on the GitHub Developer
      website.

      * IP rejects webhooks trigger requests unless they originate from an IP address in the IP range
      whitelisted in the authentication configuration.

      * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

    - **authenticationConfiguration** *(dict) --* **[REQUIRED]**

      Properties that configure the authentication applied to incoming webhook trigger requests. The
      required properties depend on the authentication type. For GITHUB_HMAC, only the
      ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange`` property must be set
      to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

      - **AllowedIPRange** *(string) --*

        The property used to configure acceptance of webhooks in an IP address range. For IP, only
        the ``AllowedIPRange`` property must be set. This property must be set to a valid CIDR range.

      - **SecretToken** *(string) --*

        The property used to configure GitHub authentication. For GITHUB_HMAC, only the
        ``SecretToken`` property must be set.
    """


_ClientRetryStageExecutionResponseTypeDef = TypedDict(
    "_ClientRetryStageExecutionResponseTypeDef",
    {"pipelineExecutionId": str},
    total=False,
)


class ClientRetryStageExecutionResponseTypeDef(
    _ClientRetryStageExecutionResponseTypeDef
):
    """
    Type definition for `ClientRetryStageExecution` `Response`

    Represents the output of a ``RetryStageExecution`` action.

    - **pipelineExecutionId** *(string) --*

      The ID of the current workflow execution in the failed stage.
    """


_ClientStartPipelineExecutionResponseTypeDef = TypedDict(
    "_ClientStartPipelineExecutionResponseTypeDef",
    {"pipelineExecutionId": str},
    total=False,
)


class ClientStartPipelineExecutionResponseTypeDef(
    _ClientStartPipelineExecutionResponseTypeDef
):
    """
    Type definition for `ClientStartPipelineExecution` `Response`

    Represents the output of a ``StartPipelineExecution`` action.

    - **pipelineExecutionId** *(string) --*

      The unique system-generated ID of the pipeline execution that was started.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --* **[REQUIRED]**

      The tag's key.

    - **value** *(string) --* **[REQUIRED]**

      The tag's value.
    """


_ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelineartifactStore` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
    used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoreTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoreTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipeline` `artifactStore`

    Represents information about the Amazon S3 bucket where artifacts are stored for the
    pipeline.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
      name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
      artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
      bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
      used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelineartifactStores` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
    is used.

    - **id** *(string) --*

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
      key ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to
        identify the key.

    - **type** *(string) --*

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
      When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoresTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoresTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipeline` `artifactStores`

    The Amazon S3 bucket where artifacts for the pipeline are stored.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
      you cannot use both. If you create a cross-region action in your pipeline, you must
      use ``artifactStores`` .

    - **type** *(string) --*

      The type of the artifact store, such as S3.

    - **location** *(string) --*

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
      the name of an S3 bucket but not a folder in the bucket. A folder to contain the
      pipeline artifacts is created for you based on the name of the pipeline. You can use
      any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
      artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
      is used.

      - **id** *(string) --*

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
        key ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to
          identify the key.

      - **type** *(string) --*

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
        When creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelinestagesactions` `actionTypeId`

    Specifies the action type and the provider of the action.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains
      the provider type for the action. Valid categories are limited to one of the
      following values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category
      type might have a provider of AWS CodeDeploy, which would be specified as
      CodeDeploy. For more information, see `Valid Action Types and Providers in
      CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelinestagesactions` `inputArtifacts`

    Represents information about an artifact to be worked on, such as a test or build
    artifact.

    - **name** *(string) --*

      The name of the artifact to be worked on (for example, "My App").

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.
    """


_ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelinestagesactions` `outputArtifacts`

    Represents information about the output of an action.

    - **name** *(string) --*

      The name of the output of an artifact, such as "My App".

      The input artifact of an action must exactly match the output artifact declared
      in a preceding action, but the input artifact does not have to be the next
      action in strict sequence from the action that provided the output artifact.
      Actions in parallel can declare different output artifacts, which are in turn
      consumed by different following actions.

      Output artifact names must be unique within a pipeline.
    """


_ClientUpdatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelinestages` `actions`

    Represents information about an action declaration.

    - **name** *(string) --*

      The action declaration's name.

    - **actionTypeId** *(dict) --*

      Specifies the action type and the provider of the action.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains
        the provider type for the action. Valid categories are limited to one of the
        following values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category
        type might have a provider of AWS CodeDeploy, which would be specified as
        CodeDeploy. For more information, see `Valid Action Types and Providers in
        CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **runOrder** *(integer) --*

      The order in which actions are run.

    - **configuration** *(dict) --*

      The action's configuration. These are key-value pairs that specify input values for
      an action. For more information, see `Action Structure Requirements in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      . For the list of configuration properties for the AWS CloudFormation action type
      in CodePipeline, see `Configuration Properties Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
      in the *AWS CloudFormation User Guide* . For template snippets with examples, see
      `Using Parameter Override Functions with CodePipeline Pipelines
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
      in the *AWS CloudFormation User Guide* .

      The values can be represented in either JSON or YAML format. For example, the JSON
      configuration item format is as follows:

       *JSON:*

       ``"Configuration" : { Key : Value },``

      - *(string) --*

        - *(string) --*

    - **outputArtifacts** *(list) --*

      The name or ID of the result of the action declaration, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about the output of an action.

        - **name** *(string) --*

          The name of the output of an artifact, such as "My App".

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

          Output artifact names must be unique within a pipeline.

    - **inputArtifacts** *(list) --*

      The name or ID of the artifact consumed by the action, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about an artifact to be worked on, such as a test or build
        artifact.

        - **name** *(string) --*

          The name of the artifact to be worked on (for example, "My App").

          The input artifact of an action must exactly match the output artifact declared
          in a preceding action, but the input artifact does not have to be the next
          action in strict sequence from the action that provided the output artifact.
          Actions in parallel can declare different output artifacts, which are in turn
          consumed by different following actions.

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The action declaration's AWS Region, such as us-east-1.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output
      by this action fall under this namespace.
    """


_ClientUpdatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesblockersTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesblockersTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipelinestages` `blockers`

    Reserved for future use.

    - **name** *(string) --*

      Reserved for future use.

    - **type** *(string) --*

      Reserved for future use.
    """


_ClientUpdatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientUpdatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientUpdatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponsepipeline` `stages`

    Represents information about a stage and its definition.

    - **name** *(string) --*

      The name of the stage.

    - **blockers** *(list) --*

      Reserved for future use.

      - *(dict) --*

        Reserved for future use.

        - **name** *(string) --*

          Reserved for future use.

        - **type** *(string) --*

          Reserved for future use.

    - **actions** *(list) --*

      The actions included in a stage.

      - *(dict) --*

        Represents information about an action declaration.

        - **name** *(string) --*

          The action declaration's name.

        - **actionTypeId** *(dict) --*

          Specifies the action type and the provider of the action.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains
            the provider type for the action. Valid categories are limited to one of the
            following values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are
            determined by the action category. For example, an action in the Deploy category
            type might have a provider of AWS CodeDeploy, which would be specified as
            CodeDeploy. For more information, see `Valid Action Types and Providers in
            CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **runOrder** *(integer) --*

          The order in which actions are run.

        - **configuration** *(dict) --*

          The action's configuration. These are key-value pairs that specify input values for
          an action. For more information, see `Action Structure Requirements in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          . For the list of configuration properties for the AWS CloudFormation action type
          in CodePipeline, see `Configuration Properties Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
          in the *AWS CloudFormation User Guide* . For template snippets with examples, see
          `Using Parameter Override Functions with CodePipeline Pipelines
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
          in the *AWS CloudFormation User Guide* .

          The values can be represented in either JSON or YAML format. For example, the JSON
          configuration item format is as follows:

           *JSON:*

           ``"Configuration" : { Key : Value },``

          - *(string) --*

            - *(string) --*

        - **outputArtifacts** *(list) --*

          The name or ID of the result of the action declaration, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about the output of an action.

            - **name** *(string) --*

              The name of the output of an artifact, such as "My App".

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

              Output artifact names must be unique within a pipeline.

        - **inputArtifacts** *(list) --*

          The name or ID of the artifact consumed by the action, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about an artifact to be worked on, such as a test or build
            artifact.

            - **name** *(string) --*

              The name of the artifact to be worked on (for example, "My App").

              The input artifact of an action must exactly match the output artifact declared
              in a preceding action, but the input artifact does not have to be the next
              action in strict sequence from the action that provided the output artifact.
              Actions in parallel can declare different output artifacts, which are in turn
              consumed by different following actions.

        - **roleArn** *(string) --*

          The ARN of the IAM service role that performs the declared action. This is assumed
          through the roleArn for the pipeline.

        - **region** *(string) --*

          The action declaration's AWS Region, such as us-east-1.

        - **namespace** *(string) --*

          The variable namespace associated with the action. All variables produced as output
          by this action fall under this namespace.
    """


_ClientUpdatePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientUpdatePipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[
            str, ClientUpdatePipelineResponsepipelineartifactStoresTypeDef
        ],
        "stages": List[ClientUpdatePipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelineTypeDef(
    _ClientUpdatePipelineResponsepipelineTypeDef
):
    """
    Type definition for `ClientUpdatePipelineResponse` `pipeline`

    The structure of the updated pipeline.

    - **name** *(string) --*

      The name of the action to be performed.

    - **roleArn** *(string) --*

      The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
      no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

    - **artifactStore** *(dict) --*

      Represents information about the Amazon S3 bucket where artifacts are stored for the
      pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - **type** *(string) --*

        The type of the artifact store, such as S3.

      - **location** *(string) --*

        The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
        name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
        artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
        bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt the data in the artifact store, such as an AWS Key
        Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
        used.

        - **id** *(string) --*

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
          ARN, or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key
            (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
            the key.

        - **type** *(string) --*

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **artifactStores** *(dict) --*

      A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
      an artifact store for the pipeline Region and for each cross-region action in the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - *(string) --*

        - *(dict) --*

          The Amazon S3 bucket where artifacts for the pipeline are stored.

          .. note::

            You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
            you cannot use both. If you create a cross-region action in your pipeline, you must
            use ``artifactStores`` .

          - **type** *(string) --*

            The type of the artifact store, such as S3.

          - **location** *(string) --*

            The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
            the name of an S3 bucket but not a folder in the bucket. A folder to contain the
            pipeline artifacts is created for you based on the name of the pipeline. You can use
            any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
            artifacts.

          - **encryptionKey** *(dict) --*

            The encryption key used to encrypt the data in the artifact store, such as an AWS Key
            Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
            is used.

            - **id** *(string) --*

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
              key ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to
                identify the key.

            - **type** *(string) --*

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
              When creating or updating a pipeline, the value must be set to 'KMS'.

    - **stages** *(list) --*

      The stage in which to perform the action.

      - *(dict) --*

        Represents information about a stage and its definition.

        - **name** *(string) --*

          The name of the stage.

        - **blockers** *(list) --*

          Reserved for future use.

          - *(dict) --*

            Reserved for future use.

            - **name** *(string) --*

              Reserved for future use.

            - **type** *(string) --*

              Reserved for future use.

        - **actions** *(list) --*

          The actions included in a stage.

          - *(dict) --*

            Represents information about an action declaration.

            - **name** *(string) --*

              The action declaration's name.

            - **actionTypeId** *(dict) --*

              Specifies the action type and the provider of the action.

              - **category** *(string) --*

                A category defines what kind of action can be taken in the stage, and constrains
                the provider type for the action. Valid categories are limited to one of the
                following values.

              - **owner** *(string) --*

                The creator of the action being called.

              - **provider** *(string) --*

                The provider of the service being called by the action. Valid providers are
                determined by the action category. For example, an action in the Deploy category
                type might have a provider of AWS CodeDeploy, which would be specified as
                CodeDeploy. For more information, see `Valid Action Types and Providers in
                CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                .

              - **version** *(string) --*

                A string that describes the action version.

            - **runOrder** *(integer) --*

              The order in which actions are run.

            - **configuration** *(dict) --*

              The action's configuration. These are key-value pairs that specify input values for
              an action. For more information, see `Action Structure Requirements in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              . For the list of configuration properties for the AWS CloudFormation action type
              in CodePipeline, see `Configuration Properties Reference
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
              in the *AWS CloudFormation User Guide* . For template snippets with examples, see
              `Using Parameter Override Functions with CodePipeline Pipelines
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
              in the *AWS CloudFormation User Guide* .

              The values can be represented in either JSON or YAML format. For example, the JSON
              configuration item format is as follows:

               *JSON:*

               ``"Configuration" : { Key : Value },``

              - *(string) --*

                - *(string) --*

            - **outputArtifacts** *(list) --*

              The name or ID of the result of the action declaration, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about the output of an action.

                - **name** *(string) --*

                  The name of the output of an artifact, such as "My App".

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

                  Output artifact names must be unique within a pipeline.

            - **inputArtifacts** *(list) --*

              The name or ID of the artifact consumed by the action, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about an artifact to be worked on, such as a test or build
                artifact.

                - **name** *(string) --*

                  The name of the artifact to be worked on (for example, "My App").

                  The input artifact of an action must exactly match the output artifact declared
                  in a preceding action, but the input artifact does not have to be the next
                  action in strict sequence from the action that provided the output artifact.
                  Actions in parallel can declare different output artifacts, which are in turn
                  consumed by different following actions.

            - **roleArn** *(string) --*

              The ARN of the IAM service role that performs the declared action. This is assumed
              through the roleArn for the pipeline.

            - **region** *(string) --*

              The action declaration's AWS Region, such as us-east-1.

            - **namespace** *(string) --*

              The variable namespace associated with the action. All variables produced as output
              by this action fall under this namespace.

    - **version** *(integer) --*

      The version number of the pipeline. A new pipeline always has a version number of 1. This
      number is incremented when a pipeline is updated.
    """


_ClientUpdatePipelineResponseTypeDef = TypedDict(
    "_ClientUpdatePipelineResponseTypeDef",
    {"pipeline": ClientUpdatePipelineResponsepipelineTypeDef},
    total=False,
)


class ClientUpdatePipelineResponseTypeDef(_ClientUpdatePipelineResponseTypeDef):
    """
    Type definition for `ClientUpdatePipeline` `Response`

    Represents the output of an ``UpdatePipeline`` action.

    - **pipeline** *(dict) --*

      The structure of the updated pipeline.

      - **name** *(string) --*

        The name of the action to be performed.

      - **roleArn** *(string) --*

        The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with
        no ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

      - **artifactStore** *(dict) --*

        Represents information about the Amazon S3 bucket where artifacts are stored for the
        pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - **type** *(string) --*

          The type of the artifact store, such as S3.

        - **location** *(string) --*

          The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
          name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
          artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
          bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

        - **encryptionKey** *(dict) --*

          The encryption key used to encrypt the data in the artifact store, such as an AWS Key
          Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
          used.

          - **id** *(string) --*

            The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
            ARN, or the alias ARN.

            .. note::

              Aliases are recognized only in the account that created the customer master key
              (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
              the key.

          - **type** *(string) --*

            The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
            creating or updating a pipeline, the value must be set to 'KMS'.

      - **artifactStores** *(dict) --*

        A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be
        an artifact store for the pipeline Region and for each cross-region action in the pipeline.

        .. note::

          You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
          cannot use both. If you create a cross-region action in your pipeline, you must use
          ``artifactStores`` .

        - *(string) --*

          - *(dict) --*

            The Amazon S3 bucket where artifacts for the pipeline are stored.

            .. note::

              You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but
              you cannot use both. If you create a cross-region action in your pipeline, you must
              use ``artifactStores`` .

            - **type** *(string) --*

              The type of the artifact store, such as S3.

            - **location** *(string) --*

              The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify
              the name of an S3 bucket but not a folder in the bucket. A folder to contain the
              pipeline artifacts is created for you based on the name of the pipeline. You can use
              any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline
              artifacts.

            - **encryptionKey** *(dict) --*

              The encryption key used to encrypt the data in the artifact store, such as an AWS Key
              Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3
              is used.

              - **id** *(string) --*

                The ID used to identify the key. For an AWS KMS key, you can use the key ID, the
                key ARN, or the alias ARN.

                .. note::

                  Aliases are recognized only in the account that created the customer master key
                  (CMK). For cross-account actions, you can only use the key ID or key ARN to
                  identify the key.

              - **type** *(string) --*

                The type of encryption key, such as an AWS Key Management Service (AWS KMS) key.
                When creating or updating a pipeline, the value must be set to 'KMS'.

      - **stages** *(list) --*

        The stage in which to perform the action.

        - *(dict) --*

          Represents information about a stage and its definition.

          - **name** *(string) --*

            The name of the stage.

          - **blockers** *(list) --*

            Reserved for future use.

            - *(dict) --*

              Reserved for future use.

              - **name** *(string) --*

                Reserved for future use.

              - **type** *(string) --*

                Reserved for future use.

          - **actions** *(list) --*

            The actions included in a stage.

            - *(dict) --*

              Represents information about an action declaration.

              - **name** *(string) --*

                The action declaration's name.

              - **actionTypeId** *(dict) --*

                Specifies the action type and the provider of the action.

                - **category** *(string) --*

                  A category defines what kind of action can be taken in the stage, and constrains
                  the provider type for the action. Valid categories are limited to one of the
                  following values.

                - **owner** *(string) --*

                  The creator of the action being called.

                - **provider** *(string) --*

                  The provider of the service being called by the action. Valid providers are
                  determined by the action category. For example, an action in the Deploy category
                  type might have a provider of AWS CodeDeploy, which would be specified as
                  CodeDeploy. For more information, see `Valid Action Types and Providers in
                  CodePipeline
                  <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                  .

                - **version** *(string) --*

                  A string that describes the action version.

              - **runOrder** *(integer) --*

                The order in which actions are run.

              - **configuration** *(dict) --*

                The action's configuration. These are key-value pairs that specify input values for
                an action. For more information, see `Action Structure Requirements in CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
                . For the list of configuration properties for the AWS CloudFormation action type
                in CodePipeline, see `Configuration Properties Reference
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
                in the *AWS CloudFormation User Guide* . For template snippets with examples, see
                `Using Parameter Override Functions with CodePipeline Pipelines
                <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
                in the *AWS CloudFormation User Guide* .

                The values can be represented in either JSON or YAML format. For example, the JSON
                configuration item format is as follows:

                 *JSON:*

                 ``"Configuration" : { Key : Value },``

                - *(string) --*

                  - *(string) --*

              - **outputArtifacts** *(list) --*

                The name or ID of the result of the action declaration, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about the output of an action.

                  - **name** *(string) --*

                    The name of the output of an artifact, such as "My App".

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

                    Output artifact names must be unique within a pipeline.

              - **inputArtifacts** *(list) --*

                The name or ID of the artifact consumed by the action, such as a test or build
                artifact.

                - *(dict) --*

                  Represents information about an artifact to be worked on, such as a test or build
                  artifact.

                  - **name** *(string) --*

                    The name of the artifact to be worked on (for example, "My App").

                    The input artifact of an action must exactly match the output artifact declared
                    in a preceding action, but the input artifact does not have to be the next
                    action in strict sequence from the action that provided the output artifact.
                    Actions in parallel can declare different output artifacts, which are in turn
                    consumed by different following actions.

              - **roleArn** *(string) --*

                The ARN of the IAM service role that performs the declared action. This is assumed
                through the roleArn for the pipeline.

              - **region** *(string) --*

                The action declaration's AWS Region, such as us-east-1.

              - **namespace** *(string) --*

                The variable namespace associated with the action. All variables produced as output
                by this action fall under this namespace.

      - **version** *(integer) --*

        The version number of the pipeline. A new pipeline always has a version number of 1. This
        number is incremented when a pipeline is updated.
    """


_ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
)


class ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef(
    _ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelineartifactStore` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

    - **id** *(string) --* **[REQUIRED]**

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
      or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key (CMK).
        For cross-account actions, you can only use the key ID or key ARN to identify the key.

    - **type** *(string) --* **[REQUIRED]**

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_RequiredClientUpdatePipelinepipelineartifactStoreTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineartifactStoreTypeDef",
    {"type": str, "location": str},
)
_OptionalClientUpdatePipelinepipelineartifactStoreTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineartifactStoreTypeDef",
    {"encryptionKey": ClientUpdatePipelinepipelineartifactStoreencryptionKeyTypeDef},
    total=False,
)


class ClientUpdatePipelinepipelineartifactStoreTypeDef(
    _RequiredClientUpdatePipelinepipelineartifactStoreTypeDef,
    _OptionalClientUpdatePipelinepipelineartifactStoreTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipeline` `artifactStore`

    Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --* **[REQUIRED]**

      The type of the artifact store, such as S3.

    - **location** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name
      of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is
      created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the
      same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

      - **id** *(string) --* **[REQUIRED]**

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
        or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key (CMK).
          For cross-account actions, you can only use the key ID or key ARN to identify the key.

      - **type** *(string) --* **[REQUIRED]**

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
)


class ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef(
    _ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelineartifactStores` `encryptionKey`

    The encryption key used to encrypt the data in the artifact store, such as an AWS Key
    Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
    used.

    - **id** *(string) --* **[REQUIRED]**

      The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
      ARN, or the alias ARN.

      .. note::

        Aliases are recognized only in the account that created the customer master key
        (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
        the key.

    - **type** *(string) --* **[REQUIRED]**

      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
      creating or updating a pipeline, the value must be set to 'KMS'.
    """


_RequiredClientUpdatePipelinepipelineartifactStoresTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineartifactStoresTypeDef",
    {"type": str, "location": str},
)
_OptionalClientUpdatePipelinepipelineartifactStoresTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineartifactStoresTypeDef",
    {"encryptionKey": ClientUpdatePipelinepipelineartifactStoresencryptionKeyTypeDef},
    total=False,
)


class ClientUpdatePipelinepipelineartifactStoresTypeDef(
    _RequiredClientUpdatePipelinepipelineartifactStoresTypeDef,
    _OptionalClientUpdatePipelinepipelineartifactStoresTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipeline` `artifactStores`

    The Amazon S3 bucket where artifacts for the pipeline are stored.

    .. note::

      You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
      cannot use both. If you create a cross-region action in your pipeline, you must use
      ``artifactStores`` .

    - **type** *(string) --* **[REQUIRED]**

      The type of the artifact store, such as S3.

    - **location** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
      name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
      artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
      bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

    - **encryptionKey** *(dict) --*

      The encryption key used to encrypt the data in the artifact store, such as an AWS Key
      Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
      used.

      - **id** *(string) --* **[REQUIRED]**

        The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
        ARN, or the alias ARN.

        .. note::

          Aliases are recognized only in the account that created the customer master key
          (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
          the key.

      - **type** *(string) --* **[REQUIRED]**

        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
        creating or updating a pipeline, the value must be set to 'KMS'.
    """


_ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
)


class ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef(
    _ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelinestagesactions` `actionTypeId`

    Specifies the action type and the provider of the action.

    - **category** *(string) --* **[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --* **[REQUIRED]**

      The creator of the action being called.

    - **provider** *(string) --* **[REQUIRED]**

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category type
      might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
      more information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --* **[REQUIRED]**

      A string that describes the action version.
    """


_ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef", {"name": str}
)


class ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef(
    _ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelinestagesactions` `inputArtifacts`

    Represents information about an artifact to be worked on, such as a test or build
    artifact.

    - **name** *(string) --* **[REQUIRED]**

      The name of the artifact to be worked on (for example, "My App").

      The input artifact of an action must exactly match the output artifact declared in
      a preceding action, but the input artifact does not have to be the next action in
      strict sequence from the action that provided the output artifact. Actions in
      parallel can declare different output artifacts, which are in turn consumed by
      different following actions.
    """


_ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef", {"name": str}
)


class ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelinestagesactions` `outputArtifacts`

    Represents information about the output of an action.

    - **name** *(string) --* **[REQUIRED]**

      The name of the output of an artifact, such as "My App".

      The input artifact of an action must exactly match the output artifact declared in
      a preceding action, but the input artifact does not have to be the next action in
      strict sequence from the action that provided the output artifact. Actions in
      parallel can declare different output artifacts, which are in turn consumed by
      different following actions.

      Output artifact names must be unique within a pipeline.
    """


_RequiredClientUpdatePipelinepipelinestagesactionsTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientUpdatePipelinepipelinestagesactionsactionTypeIdTypeDef,
    },
)
_OptionalClientUpdatePipelinepipelinestagesactionsTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelinestagesactionsTypeDef",
    {
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientUpdatePipelinepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientUpdatePipelinepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ClientUpdatePipelinepipelinestagesactionsTypeDef(
    _RequiredClientUpdatePipelinepipelinestagesactionsTypeDef,
    _OptionalClientUpdatePipelinepipelinestagesactionsTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipelinestages` `actions`

    Represents information about an action declaration.

    - **name** *(string) --* **[REQUIRED]**

      The action declaration's name.

    - **actionTypeId** *(dict) --* **[REQUIRED]**

      Specifies the action type and the provider of the action.

      - **category** *(string) --* **[REQUIRED]**

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --* **[REQUIRED]**

        The creator of the action being called.

      - **provider** *(string) --* **[REQUIRED]**

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category type
        might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
        more information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --* **[REQUIRED]**

        A string that describes the action version.

    - **runOrder** *(integer) --*

      The order in which actions are run.

    - **configuration** *(dict) --*

      The action's configuration. These are key-value pairs that specify input values for an
      action. For more information, see `Action Structure Requirements in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      . For the list of configuration properties for the AWS CloudFormation action type in
      CodePipeline, see `Configuration Properties Reference
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
      in the *AWS CloudFormation User Guide* . For template snippets with examples, see
      `Using Parameter Override Functions with CodePipeline Pipelines
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
      in the *AWS CloudFormation User Guide* .

      The values can be represented in either JSON or YAML format. For example, the JSON
      configuration item format is as follows:

       *JSON:*

       ``"Configuration" : { Key : Value },``

      - *(string) --*

        - *(string) --*

    - **outputArtifacts** *(list) --*

      The name or ID of the result of the action declaration, such as a test or build
      artifact.

      - *(dict) --*

        Represents information about the output of an action.

        - **name** *(string) --* **[REQUIRED]**

          The name of the output of an artifact, such as "My App".

          The input artifact of an action must exactly match the output artifact declared in
          a preceding action, but the input artifact does not have to be the next action in
          strict sequence from the action that provided the output artifact. Actions in
          parallel can declare different output artifacts, which are in turn consumed by
          different following actions.

          Output artifact names must be unique within a pipeline.

    - **inputArtifacts** *(list) --*

      The name or ID of the artifact consumed by the action, such as a test or build artifact.

      - *(dict) --*

        Represents information about an artifact to be worked on, such as a test or build
        artifact.

        - **name** *(string) --* **[REQUIRED]**

          The name of the artifact to be worked on (for example, "My App").

          The input artifact of an action must exactly match the output artifact declared in
          a preceding action, but the input artifact does not have to be the next action in
          strict sequence from the action that provided the output artifact. Actions in
          parallel can declare different output artifacts, which are in turn consumed by
          different following actions.

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The action declaration's AWS Region, such as us-east-1.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output by
      this action fall under this namespace.
    """


_ClientUpdatePipelinepipelinestagesblockersTypeDef = TypedDict(
    "_ClientUpdatePipelinepipelinestagesblockersTypeDef", {"name": str, "type": str}
)


class ClientUpdatePipelinepipelinestagesblockersTypeDef(
    _ClientUpdatePipelinepipelinestagesblockersTypeDef
):
    """
    Type definition for `ClientUpdatePipelinepipelinestages` `blockers`

    Reserved for future use.

    - **name** *(string) --* **[REQUIRED]**

      Reserved for future use.

    - **type** *(string) --* **[REQUIRED]**

      Reserved for future use.
    """


_RequiredClientUpdatePipelinepipelinestagesTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelinestagesTypeDef",
    {"name": str, "actions": List[ClientUpdatePipelinepipelinestagesactionsTypeDef]},
)
_OptionalClientUpdatePipelinepipelinestagesTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelinestagesTypeDef",
    {"blockers": List[ClientUpdatePipelinepipelinestagesblockersTypeDef]},
    total=False,
)


class ClientUpdatePipelinepipelinestagesTypeDef(
    _RequiredClientUpdatePipelinepipelinestagesTypeDef,
    _OptionalClientUpdatePipelinepipelinestagesTypeDef,
):
    """
    Type definition for `ClientUpdatePipelinepipeline` `stages`

    Represents information about a stage and its definition.

    - **name** *(string) --* **[REQUIRED]**

      The name of the stage.

    - **blockers** *(list) --*

      Reserved for future use.

      - *(dict) --*

        Reserved for future use.

        - **name** *(string) --* **[REQUIRED]**

          Reserved for future use.

        - **type** *(string) --* **[REQUIRED]**

          Reserved for future use.

    - **actions** *(list) --* **[REQUIRED]**

      The actions included in a stage.

      - *(dict) --*

        Represents information about an action declaration.

        - **name** *(string) --* **[REQUIRED]**

          The action declaration's name.

        - **actionTypeId** *(dict) --* **[REQUIRED]**

          Specifies the action type and the provider of the action.

          - **category** *(string) --* **[REQUIRED]**

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --* **[REQUIRED]**

            The creator of the action being called.

          - **provider** *(string) --* **[REQUIRED]**

            The provider of the service being called by the action. Valid providers are
            determined by the action category. For example, an action in the Deploy category type
            might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
            more information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --* **[REQUIRED]**

            A string that describes the action version.

        - **runOrder** *(integer) --*

          The order in which actions are run.

        - **configuration** *(dict) --*

          The action's configuration. These are key-value pairs that specify input values for an
          action. For more information, see `Action Structure Requirements in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          . For the list of configuration properties for the AWS CloudFormation action type in
          CodePipeline, see `Configuration Properties Reference
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
          in the *AWS CloudFormation User Guide* . For template snippets with examples, see
          `Using Parameter Override Functions with CodePipeline Pipelines
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
          in the *AWS CloudFormation User Guide* .

          The values can be represented in either JSON or YAML format. For example, the JSON
          configuration item format is as follows:

           *JSON:*

           ``"Configuration" : { Key : Value },``

          - *(string) --*

            - *(string) --*

        - **outputArtifacts** *(list) --*

          The name or ID of the result of the action declaration, such as a test or build
          artifact.

          - *(dict) --*

            Represents information about the output of an action.

            - **name** *(string) --* **[REQUIRED]**

              The name of the output of an artifact, such as "My App".

              The input artifact of an action must exactly match the output artifact declared in
              a preceding action, but the input artifact does not have to be the next action in
              strict sequence from the action that provided the output artifact. Actions in
              parallel can declare different output artifacts, which are in turn consumed by
              different following actions.

              Output artifact names must be unique within a pipeline.

        - **inputArtifacts** *(list) --*

          The name or ID of the artifact consumed by the action, such as a test or build artifact.

          - *(dict) --*

            Represents information about an artifact to be worked on, such as a test or build
            artifact.

            - **name** *(string) --* **[REQUIRED]**

              The name of the artifact to be worked on (for example, "My App").

              The input artifact of an action must exactly match the output artifact declared in
              a preceding action, but the input artifact does not have to be the next action in
              strict sequence from the action that provided the output artifact. Actions in
              parallel can declare different output artifacts, which are in turn consumed by
              different following actions.

        - **roleArn** *(string) --*

          The ARN of the IAM service role that performs the declared action. This is assumed
          through the roleArn for the pipeline.

        - **region** *(string) --*

          The action declaration's AWS Region, such as us-east-1.

        - **namespace** *(string) --*

          The variable namespace associated with the action. All variables produced as output by
          this action fall under this namespace.
    """


_RequiredClientUpdatePipelinepipelineTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": List[ClientUpdatePipelinepipelinestagesTypeDef],
    },
)
_OptionalClientUpdatePipelinepipelineTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinepipelineTypeDef",
    {
        "artifactStore": ClientUpdatePipelinepipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientUpdatePipelinepipelineartifactStoresTypeDef],
        "version": int,
    },
    total=False,
)


class ClientUpdatePipelinepipelineTypeDef(
    _RequiredClientUpdatePipelinepipelineTypeDef,
    _OptionalClientUpdatePipelinepipelineTypeDef,
):
    """
    Type definition for `ClientUpdatePipeline` `pipeline`

    The name of the pipeline to be updated.

    - **name** *(string) --* **[REQUIRED]**

      The name of the action to be performed.

    - **roleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no
      ``actionRoleArn`` , or to use to assume roles for actions with an ``actionRoleArn`` .

    - **artifactStore** *(dict) --*

      Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - **type** *(string) --* **[REQUIRED]**

        The type of the artifact store, such as S3.

      - **location** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name
        of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is
        created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the
        same AWS Region as the pipeline to store your pipeline artifacts.

      - **encryptionKey** *(dict) --*

        The encryption key used to encrypt the data in the artifact store, such as an AWS Key
        Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

        - **id** *(string) --* **[REQUIRED]**

          The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN,
          or the alias ARN.

          .. note::

            Aliases are recognized only in the account that created the customer master key (CMK).
            For cross-account actions, you can only use the key ID or key ARN to identify the key.

        - **type** *(string) --* **[REQUIRED]**

          The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
          creating or updating a pipeline, the value must be set to 'KMS'.

    - **artifactStores** *(dict) --*

      A mapping of ``artifactStore`` objects and their corresponding AWS Regions. There must be an
      artifact store for the pipeline Region and for each cross-region action in the pipeline.

      .. note::

        You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
        cannot use both. If you create a cross-region action in your pipeline, you must use
        ``artifactStores`` .

      - *(string) --*

        - *(dict) --*

          The Amazon S3 bucket where artifacts for the pipeline are stored.

          .. note::

            You must include either ``artifactStore`` or ``artifactStores`` in your pipeline, but you
            cannot use both. If you create a cross-region action in your pipeline, you must use
            ``artifactStores`` .

          - **type** *(string) --* **[REQUIRED]**

            The type of the artifact store, such as S3.

          - **location** *(string) --* **[REQUIRED]**

            The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the
            name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline
            artifacts is created for you based on the name of the pipeline. You can use any Amazon S3
            bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

          - **encryptionKey** *(dict) --*

            The encryption key used to encrypt the data in the artifact store, such as an AWS Key
            Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is
            used.

            - **id** *(string) --* **[REQUIRED]**

              The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key
              ARN, or the alias ARN.

              .. note::

                Aliases are recognized only in the account that created the customer master key
                (CMK). For cross-account actions, you can only use the key ID or key ARN to identify
                the key.

            - **type** *(string) --* **[REQUIRED]**

              The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When
              creating or updating a pipeline, the value must be set to 'KMS'.

    - **stages** *(list) --* **[REQUIRED]**

      The stage in which to perform the action.

      - *(dict) --*

        Represents information about a stage and its definition.

        - **name** *(string) --* **[REQUIRED]**

          The name of the stage.

        - **blockers** *(list) --*

          Reserved for future use.

          - *(dict) --*

            Reserved for future use.

            - **name** *(string) --* **[REQUIRED]**

              Reserved for future use.

            - **type** *(string) --* **[REQUIRED]**

              Reserved for future use.

        - **actions** *(list) --* **[REQUIRED]**

          The actions included in a stage.

          - *(dict) --*

            Represents information about an action declaration.

            - **name** *(string) --* **[REQUIRED]**

              The action declaration's name.

            - **actionTypeId** *(dict) --* **[REQUIRED]**

              Specifies the action type and the provider of the action.

              - **category** *(string) --* **[REQUIRED]**

                A category defines what kind of action can be taken in the stage, and constrains the
                provider type for the action. Valid categories are limited to one of the following
                values.

              - **owner** *(string) --* **[REQUIRED]**

                The creator of the action being called.

              - **provider** *(string) --* **[REQUIRED]**

                The provider of the service being called by the action. Valid providers are
                determined by the action category. For example, an action in the Deploy category type
                might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
                more information, see `Valid Action Types and Providers in CodePipeline
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
                .

              - **version** *(string) --* **[REQUIRED]**

                A string that describes the action version.

            - **runOrder** *(integer) --*

              The order in which actions are run.

            - **configuration** *(dict) --*

              The action's configuration. These are key-value pairs that specify input values for an
              action. For more information, see `Action Structure Requirements in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
              . For the list of configuration properties for the AWS CloudFormation action type in
              CodePipeline, see `Configuration Properties Reference
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html>`__
              in the *AWS CloudFormation User Guide* . For template snippets with examples, see
              `Using Parameter Override Functions with CodePipeline Pipelines
              <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html>`__
              in the *AWS CloudFormation User Guide* .

              The values can be represented in either JSON or YAML format. For example, the JSON
              configuration item format is as follows:

               *JSON:*

               ``"Configuration" : { Key : Value },``

              - *(string) --*

                - *(string) --*

            - **outputArtifacts** *(list) --*

              The name or ID of the result of the action declaration, such as a test or build
              artifact.

              - *(dict) --*

                Represents information about the output of an action.

                - **name** *(string) --* **[REQUIRED]**

                  The name of the output of an artifact, such as "My App".

                  The input artifact of an action must exactly match the output artifact declared in
                  a preceding action, but the input artifact does not have to be the next action in
                  strict sequence from the action that provided the output artifact. Actions in
                  parallel can declare different output artifacts, which are in turn consumed by
                  different following actions.

                  Output artifact names must be unique within a pipeline.

            - **inputArtifacts** *(list) --*

              The name or ID of the artifact consumed by the action, such as a test or build artifact.

              - *(dict) --*

                Represents information about an artifact to be worked on, such as a test or build
                artifact.

                - **name** *(string) --* **[REQUIRED]**

                  The name of the artifact to be worked on (for example, "My App").

                  The input artifact of an action must exactly match the output artifact declared in
                  a preceding action, but the input artifact does not have to be the next action in
                  strict sequence from the action that provided the output artifact. Actions in
                  parallel can declare different output artifacts, which are in turn consumed by
                  different following actions.

            - **roleArn** *(string) --*

              The ARN of the IAM service role that performs the declared action. This is assumed
              through the roleArn for the pipeline.

            - **region** *(string) --*

              The action declaration's AWS Region, such as us-east-1.

            - **namespace** *(string) --*

              The variable namespace associated with the action. All variables produced as output by
              this action fall under this namespace.

    - **version** *(integer) --*

      The version number of the pipeline. A new pipeline always has a version number of 1. This
      number is incremented when a pipeline is updated.
    """


_ListActionExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActionExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActionExecutionsPaginatePaginationConfigTypeDef(
    _ListActionExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginate` `PaginationConfig`

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


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsinput` `actionTypeId`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are
      determined by the action category. For example, an action in the Deploy category type
      might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
      more information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifacts` `s3location`

    The Amazon S3 artifact location for the action execution.

    - **bucket** *(string) --*

      The Amazon S3 artifact bucket for an action's artifacts.

    - **key** *(string) --*

      The artifact name.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsinput` `inputArtifacts`

    Artifact details for the action execution, such as the artifact location.

    - **name** *(string) --*

      The artifact object name for the action execution.

    - **s3location** *(dict) --*

      The Amazon S3 artifact location for the action execution.

      - **bucket** *(string) --*

        The Amazon S3 artifact bucket for an action's artifacts.

      - **key** *(string) --*

        The artifact name.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef",
    {
        "actionTypeId": ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef,
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef
        ],
        "namespace": str,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetails` `input`

    Input details for the action execution, such as role ARN, Region, and input artifacts.

    - **actionTypeId** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are
        determined by the action category. For example, an action in the Deploy category type
        might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
        more information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **configuration** *(dict) --*

      Configuration data for an action execution.

      - *(string) --*

        - *(string) --*

    - **resolvedConfiguration** *(dict) --*

      Configuration data for an action execution with all variable references replaced with
      their real values for the execution.

      - *(string) --*

        - *(string) --*

    - **roleArn** *(string) --*

      The ARN of the IAM service role that performs the declared action. This is assumed
      through the roleArn for the pipeline.

    - **region** *(string) --*

      The AWS Region for the action, such as us-east-1.

    - **inputArtifacts** *(list) --*

      Details of input artifacts of the action that correspond to the action execution.

      - *(dict) --*

        Artifact details for the action execution, such as the artifact location.

        - **name** *(string) --*

          The artifact object name for the action execution.

        - **s3location** *(dict) --*

          The Amazon S3 artifact location for the action execution.

          - **bucket** *(string) --*

            The Amazon S3 artifact bucket for an action's artifacts.

          - **key** *(string) --*

            The artifact name.

    - **namespace** *(string) --*

      The variable namespace associated with the action. All variables produced as output by
      this action fall under this namespace.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {
        "externalExecutionId": str,
        "externalExecutionSummary": str,
        "externalExecutionUrl": str,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsoutput` `executionResult`

    Execution result information listed in the output details for an action execution.

    - **externalExecutionId** *(string) --*

      The action provider's external ID for the action execution.

    - **externalExecutionSummary** *(string) --*

      The action provider's summary for the action execution.

    - **externalExecutionUrl** *(string) --*

      The deepest external link to the external resource (for example, a repository URL or
      deployment endpoint) that is used when running the action.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifacts` `s3location`

    The Amazon S3 artifact location for the action execution.

    - **bucket** *(string) --*

      The Amazon S3 artifact bucket for an action's artifacts.

    - **key** *(string) --*

      The artifact name.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetailsoutput` `outputArtifacts`

    Artifact details for the action execution, such as the artifact location.

    - **name** *(string) --*

      The artifact object name for the action execution.

    - **s3location** *(dict) --*

      The Amazon S3 artifact location for the action execution.

      - **bucket** *(string) --*

        The Amazon S3 artifact bucket for an action's artifacts.

      - **key** *(string) --*

        The artifact name.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponseactionExecutionDetails` `output`

    Output details for the action execution, such as the action execution result.

    - **outputArtifacts** *(list) --*

      Details of output artifacts of the action that correspond to the action execution.

      - *(dict) --*

        Artifact details for the action execution, such as the artifact location.

        - **name** *(string) --*

          The artifact object name for the action execution.

        - **s3location** *(dict) --*

          The Amazon S3 artifact location for the action execution.

          - **bucket** *(string) --*

            The Amazon S3 artifact bucket for an action's artifacts.

          - **key** *(string) --*

            The artifact name.

    - **executionResult** *(dict) --*

      Execution result information listed in the output details for an action execution.

      - **externalExecutionId** *(string) --*

        The action provider's external ID for the action execution.

      - **externalExecutionSummary** *(string) --*

        The action provider's summary for the action execution.

      - **externalExecutionUrl** *(string) --*

        The deepest external link to the external resource (for example, a repository URL or
        deployment endpoint) that is used when running the action.

    - **outputVariables** *(dict) --*

      The outputVariables field shows the key-value pairs that were output as part of that
      execution.

      - *(string) --*

        - *(string) --*
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": str,
        "input": ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef,
        "output": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginateResponse` `actionExecutionDetails`

    Returns information about an execution of an action, including the action execution ID, and
    the name, version, and timing of the action.

    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID for the action execution.

    - **actionExecutionId** *(string) --*

      The action execution ID.

    - **pipelineVersion** *(integer) --*

      The version of the pipeline where the action was run.

    - **stageName** *(string) --*

      The name of the stage that contains the action.

    - **actionName** *(string) --*

      The name of the action.

    - **startTime** *(datetime) --*

      The start time of the action execution.

    - **lastUpdateTime** *(datetime) --*

      The last update time of the action execution.

    - **status** *(string) --*

      The status of the action execution. Status categories are ``InProgress`` , ``Succeeded``
      , and ``Failed`` .

    - **input** *(dict) --*

      Input details for the action execution, such as role ARN, Region, and input artifacts.

      - **actionTypeId** *(dict) --*

        Represents information about an action type.

        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following
          values.

        - **owner** *(string) --*

          The creator of the action being called.

        - **provider** *(string) --*

          The provider of the service being called by the action. Valid providers are
          determined by the action category. For example, an action in the Deploy category type
          might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
          more information, see `Valid Action Types and Providers in CodePipeline
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
          .

        - **version** *(string) --*

          A string that describes the action version.

      - **configuration** *(dict) --*

        Configuration data for an action execution.

        - *(string) --*

          - *(string) --*

      - **resolvedConfiguration** *(dict) --*

        Configuration data for an action execution with all variable references replaced with
        their real values for the execution.

        - *(string) --*

          - *(string) --*

      - **roleArn** *(string) --*

        The ARN of the IAM service role that performs the declared action. This is assumed
        through the roleArn for the pipeline.

      - **region** *(string) --*

        The AWS Region for the action, such as us-east-1.

      - **inputArtifacts** *(list) --*

        Details of input artifacts of the action that correspond to the action execution.

        - *(dict) --*

          Artifact details for the action execution, such as the artifact location.

          - **name** *(string) --*

            The artifact object name for the action execution.

          - **s3location** *(dict) --*

            The Amazon S3 artifact location for the action execution.

            - **bucket** *(string) --*

              The Amazon S3 artifact bucket for an action's artifacts.

            - **key** *(string) --*

              The artifact name.

      - **namespace** *(string) --*

        The variable namespace associated with the action. All variables produced as output by
        this action fall under this namespace.

    - **output** *(dict) --*

      Output details for the action execution, such as the action execution result.

      - **outputArtifacts** *(list) --*

        Details of output artifacts of the action that correspond to the action execution.

        - *(dict) --*

          Artifact details for the action execution, such as the artifact location.

          - **name** *(string) --*

            The artifact object name for the action execution.

          - **s3location** *(dict) --*

            The Amazon S3 artifact location for the action execution.

            - **bucket** *(string) --*

              The Amazon S3 artifact bucket for an action's artifacts.

            - **key** *(string) --*

              The artifact name.

      - **executionResult** *(dict) --*

        Execution result information listed in the output details for an action execution.

        - **externalExecutionId** *(string) --*

          The action provider's external ID for the action execution.

        - **externalExecutionSummary** *(string) --*

          The action provider's summary for the action execution.

        - **externalExecutionUrl** *(string) --*

          The deepest external link to the external resource (for example, a repository URL or
          deployment endpoint) that is used when running the action.

      - **outputVariables** *(dict) --*

        The outputVariables field shows the key-value pairs that were output as part of that
        execution.

        - *(string) --*

          - *(string) --*
    """


_ListActionExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseTypeDef(
    _ListActionExecutionsPaginateResponseTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginate` `Response`

    - **actionExecutionDetails** *(list) --*

      The details for a list of recent executions, such as action execution ID.

      - *(dict) --*

        Returns information about an execution of an action, including the action execution ID, and
        the name, version, and timing of the action.

        - **pipelineExecutionId** *(string) --*

          The pipeline execution ID for the action execution.

        - **actionExecutionId** *(string) --*

          The action execution ID.

        - **pipelineVersion** *(integer) --*

          The version of the pipeline where the action was run.

        - **stageName** *(string) --*

          The name of the stage that contains the action.

        - **actionName** *(string) --*

          The name of the action.

        - **startTime** *(datetime) --*

          The start time of the action execution.

        - **lastUpdateTime** *(datetime) --*

          The last update time of the action execution.

        - **status** *(string) --*

          The status of the action execution. Status categories are ``InProgress`` , ``Succeeded``
          , and ``Failed`` .

        - **input** *(dict) --*

          Input details for the action execution, such as role ARN, Region, and input artifacts.

          - **actionTypeId** *(dict) --*

            Represents information about an action type.

            - **category** *(string) --*

              A category defines what kind of action can be taken in the stage, and constrains the
              provider type for the action. Valid categories are limited to one of the following
              values.

            - **owner** *(string) --*

              The creator of the action being called.

            - **provider** *(string) --*

              The provider of the service being called by the action. Valid providers are
              determined by the action category. For example, an action in the Deploy category type
              might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For
              more information, see `Valid Action Types and Providers in CodePipeline
              <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
              .

            - **version** *(string) --*

              A string that describes the action version.

          - **configuration** *(dict) --*

            Configuration data for an action execution.

            - *(string) --*

              - *(string) --*

          - **resolvedConfiguration** *(dict) --*

            Configuration data for an action execution with all variable references replaced with
            their real values for the execution.

            - *(string) --*

              - *(string) --*

          - **roleArn** *(string) --*

            The ARN of the IAM service role that performs the declared action. This is assumed
            through the roleArn for the pipeline.

          - **region** *(string) --*

            The AWS Region for the action, such as us-east-1.

          - **inputArtifacts** *(list) --*

            Details of input artifacts of the action that correspond to the action execution.

            - *(dict) --*

              Artifact details for the action execution, such as the artifact location.

              - **name** *(string) --*

                The artifact object name for the action execution.

              - **s3location** *(dict) --*

                The Amazon S3 artifact location for the action execution.

                - **bucket** *(string) --*

                  The Amazon S3 artifact bucket for an action's artifacts.

                - **key** *(string) --*

                  The artifact name.

          - **namespace** *(string) --*

            The variable namespace associated with the action. All variables produced as output by
            this action fall under this namespace.

        - **output** *(dict) --*

          Output details for the action execution, such as the action execution result.

          - **outputArtifacts** *(list) --*

            Details of output artifacts of the action that correspond to the action execution.

            - *(dict) --*

              Artifact details for the action execution, such as the artifact location.

              - **name** *(string) --*

                The artifact object name for the action execution.

              - **s3location** *(dict) --*

                The Amazon S3 artifact location for the action execution.

                - **bucket** *(string) --*

                  The Amazon S3 artifact bucket for an action's artifacts.

                - **key** *(string) --*

                  The artifact name.

          - **executionResult** *(dict) --*

            Execution result information listed in the output details for an action execution.

            - **externalExecutionId** *(string) --*

              The action provider's external ID for the action execution.

            - **externalExecutionSummary** *(string) --*

              The action provider's summary for the action execution.

            - **externalExecutionUrl** *(string) --*

              The deepest external link to the external resource (for example, a repository URL or
              deployment endpoint) that is used when running the action.

          - **outputVariables** *(dict) --*

            The outputVariables field shows the key-value pairs that were output as part of that
            execution.

            - *(string) --*

              - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListActionExecutionsPaginatefilterTypeDef = TypedDict(
    "_ListActionExecutionsPaginatefilterTypeDef",
    {"pipelineExecutionId": str},
    total=False,
)


class ListActionExecutionsPaginatefilterTypeDef(
    _ListActionExecutionsPaginatefilterTypeDef
):
    """
    Type definition for `ListActionExecutionsPaginate` `filter`

    Input information used to filter action execution history.

    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID used to filter action execution history.
    """


_ListActionTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActionTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListActionTypesPaginatePaginationConfigTypeDef(
    _ListActionTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListActionTypesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": str,
    },
    total=False,
)


class ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef(
    _ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponseactionTypes` `actionConfigurationProperties`

    Represents information about an action configuration property.

    - **name** *(string) --*

      The name of the action configuration property.

    - **required** *(boolean) --*

      Whether the configuration property is a required value.

    - **key** *(boolean) --*

      Whether the configuration property is a key.

    - **secret** *(boolean) --*

      Whether the configuration property is secret. Secrets are hidden from all calls
      except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
      ``PollForThirdPartyJobs`` .

      When updating a pipeline, passing * * * * * without changing any other values of the
      action preserves the previous value of the secret.

    - **queryable** *(boolean) --*

      Indicates that the property is used with ``PollForJobs`` . When creating a custom
      action, an action can have up to one queryable property. If it has one, that property
      must be both required and not secret.

      If you create a pipeline with a custom action type, and that custom action contains a
      queryable property, the value for that configuration property is subject to other
      restrictions. The value must be less than or equal to twenty (20) characters. The
      value can contain only alphanumeric characters, underscores, and hyphens.

    - **description** *(string) --*

      The description of the action configuration property that is displayed to users.

    - **type** *(string) --*

      The type of the configuration property.
    """


_ListActionTypesPaginateResponseactionTypesidTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesidTypeDef",
    {"category": str, "owner": str, "provider": str, "version": str},
    total=False,
)


class ListActionTypesPaginateResponseactionTypesidTypeDef(
    _ListActionTypesPaginateResponseactionTypesidTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponseactionTypes` `id`

    Represents information about an action type.

    - **category** *(string) --*

      A category defines what kind of action can be taken in the stage, and constrains the
      provider type for the action. Valid categories are limited to one of the following
      values.

    - **owner** *(string) --*

      The creator of the action being called.

    - **provider** *(string) --*

      The provider of the service being called by the action. Valid providers are determined
      by the action category. For example, an action in the Deploy category type might have a
      provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
      information, see `Valid Action Types and Providers in CodePipeline
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
      .

    - **version** *(string) --*

      A string that describes the action version.
    """


_ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef(
    _ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponseactionTypes` `inputArtifactDetails`

    The details of the input artifact for the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef(
    _ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponseactionTypes` `outputArtifactDetails`

    The details of the output artifact of the action, such as its commit ID.

    - **minimumCount** *(integer) --*

      The minimum number of artifacts allowed for the action type.

    - **maximumCount** *(integer) --*

      The maximum number of artifacts allowed for the action type.
    """


_ListActionTypesPaginateResponseactionTypessettingsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ListActionTypesPaginateResponseactionTypessettingsTypeDef(
    _ListActionTypesPaginateResponseactionTypessettingsTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponseactionTypes` `settings`

    The settings for the action type.

    - **thirdPartyConfigurationUrl** *(string) --*

      The URL of a sign-up page where users can sign up for an external service and perform
      initial configuration of the action provided by that service.

    - **entityUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that provides a deep link to the
      resources of the external system, such as the configuration page for an AWS CodeDeploy
      deployment group. This link is provided as part of the action display in the pipeline.

    - **executionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the top-level
      landing page for the external system, such as the console page for AWS CodeDeploy. This
      link is shown on the pipeline view page in the AWS CodePipeline console and provides a
      link to the execution entity of the external action.

    - **revisionUrlTemplate** *(string) --*

      The URL returned to the AWS CodePipeline console that contains a link to the page where
      customers can update or change the configuration of the external action.
    """


_ListActionTypesPaginateResponseactionTypesTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesTypeDef",
    {
        "id": ListActionTypesPaginateResponseactionTypesidTypeDef,
        "settings": ListActionTypesPaginateResponseactionTypessettingsTypeDef,
        "actionConfigurationProperties": List[
            ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef,
    },
    total=False,
)


class ListActionTypesPaginateResponseactionTypesTypeDef(
    _ListActionTypesPaginateResponseactionTypesTypeDef
):
    """
    Type definition for `ListActionTypesPaginateResponse` `actionTypes`

    Returns information about the details of an action type.

    - **id** *(dict) --*

      Represents information about an action type.

      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following
        values.

      - **owner** *(string) --*

        The creator of the action being called.

      - **provider** *(string) --*

        The provider of the service being called by the action. Valid providers are determined
        by the action category. For example, an action in the Deploy category type might have a
        provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
        information, see `Valid Action Types and Providers in CodePipeline
        <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
        .

      - **version** *(string) --*

        A string that describes the action version.

    - **settings** *(dict) --*

      The settings for the action type.

      - **thirdPartyConfigurationUrl** *(string) --*

        The URL of a sign-up page where users can sign up for an external service and perform
        initial configuration of the action provided by that service.

      - **entityUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that provides a deep link to the
        resources of the external system, such as the configuration page for an AWS CodeDeploy
        deployment group. This link is provided as part of the action display in the pipeline.

      - **executionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the top-level
        landing page for the external system, such as the console page for AWS CodeDeploy. This
        link is shown on the pipeline view page in the AWS CodePipeline console and provides a
        link to the execution entity of the external action.

      - **revisionUrlTemplate** *(string) --*

        The URL returned to the AWS CodePipeline console that contains a link to the page where
        customers can update or change the configuration of the external action.

    - **actionConfigurationProperties** *(list) --*

      The configuration properties for the action type.

      - *(dict) --*

        Represents information about an action configuration property.

        - **name** *(string) --*

          The name of the action configuration property.

        - **required** *(boolean) --*

          Whether the configuration property is a required value.

        - **key** *(boolean) --*

          Whether the configuration property is a key.

        - **secret** *(boolean) --*

          Whether the configuration property is secret. Secrets are hidden from all calls
          except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
          ``PollForThirdPartyJobs`` .

          When updating a pipeline, passing * * * * * without changing any other values of the
          action preserves the previous value of the secret.

        - **queryable** *(boolean) --*

          Indicates that the property is used with ``PollForJobs`` . When creating a custom
          action, an action can have up to one queryable property. If it has one, that property
          must be both required and not secret.

          If you create a pipeline with a custom action type, and that custom action contains a
          queryable property, the value for that configuration property is subject to other
          restrictions. The value must be less than or equal to twenty (20) characters. The
          value can contain only alphanumeric characters, underscores, and hyphens.

        - **description** *(string) --*

          The description of the action configuration property that is displayed to users.

        - **type** *(string) --*

          The type of the configuration property.

    - **inputArtifactDetails** *(dict) --*

      The details of the input artifact for the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.

    - **outputArtifactDetails** *(dict) --*

      The details of the output artifact of the action, such as its commit ID.

      - **minimumCount** *(integer) --*

        The minimum number of artifacts allowed for the action type.

      - **maximumCount** *(integer) --*

        The maximum number of artifacts allowed for the action type.
    """


_ListActionTypesPaginateResponseTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseTypeDef",
    {
        "actionTypes": List[ListActionTypesPaginateResponseactionTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListActionTypesPaginateResponseTypeDef(_ListActionTypesPaginateResponseTypeDef):
    """
    Type definition for `ListActionTypesPaginate` `Response`

    Represents the output of a ``ListActionTypes`` action.

    - **actionTypes** *(list) --*

      Provides details of the action types.

      - *(dict) --*

        Returns information about the details of an action type.

        - **id** *(dict) --*

          Represents information about an action type.

          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.

          - **owner** *(string) --*

            The creator of the action being called.

          - **provider** *(string) --*

            The provider of the service being called by the action. Valid providers are determined
            by the action category. For example, an action in the Deploy category type might have a
            provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more
            information, see `Valid Action Types and Providers in CodePipeline
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__
            .

          - **version** *(string) --*

            A string that describes the action version.

        - **settings** *(dict) --*

          The settings for the action type.

          - **thirdPartyConfigurationUrl** *(string) --*

            The URL of a sign-up page where users can sign up for an external service and perform
            initial configuration of the action provided by that service.

          - **entityUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that provides a deep link to the
            resources of the external system, such as the configuration page for an AWS CodeDeploy
            deployment group. This link is provided as part of the action display in the pipeline.

          - **executionUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that contains a link to the top-level
            landing page for the external system, such as the console page for AWS CodeDeploy. This
            link is shown on the pipeline view page in the AWS CodePipeline console and provides a
            link to the execution entity of the external action.

          - **revisionUrlTemplate** *(string) --*

            The URL returned to the AWS CodePipeline console that contains a link to the page where
            customers can update or change the configuration of the external action.

        - **actionConfigurationProperties** *(list) --*

          The configuration properties for the action type.

          - *(dict) --*

            Represents information about an action configuration property.

            - **name** *(string) --*

              The name of the action configuration property.

            - **required** *(boolean) --*

              Whether the configuration property is a required value.

            - **key** *(boolean) --*

              Whether the configuration property is a key.

            - **secret** *(boolean) --*

              Whether the configuration property is secret. Secrets are hidden from all calls
              except for ``GetJobDetails`` , ``GetThirdPartyJobDetails`` , ``PollForJobs`` , and
              ``PollForThirdPartyJobs`` .

              When updating a pipeline, passing * * * * * without changing any other values of the
              action preserves the previous value of the secret.

            - **queryable** *(boolean) --*

              Indicates that the property is used with ``PollForJobs`` . When creating a custom
              action, an action can have up to one queryable property. If it has one, that property
              must be both required and not secret.

              If you create a pipeline with a custom action type, and that custom action contains a
              queryable property, the value for that configuration property is subject to other
              restrictions. The value must be less than or equal to twenty (20) characters. The
              value can contain only alphanumeric characters, underscores, and hyphens.

            - **description** *(string) --*

              The description of the action configuration property that is displayed to users.

            - **type** *(string) --*

              The type of the configuration property.

        - **inputArtifactDetails** *(dict) --*

          The details of the input artifact for the action, such as its commit ID.

          - **minimumCount** *(integer) --*

            The minimum number of artifacts allowed for the action type.

          - **maximumCount** *(integer) --*

            The maximum number of artifacts allowed for the action type.

        - **outputArtifactDetails** *(dict) --*

          The details of the output artifact of the action, such as its commit ID.

          - **minimumCount** *(integer) --*

            The minimum number of artifacts allowed for the action type.

          - **maximumCount** *(integer) --*

            The maximum number of artifacts allowed for the action type.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPipelineExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPipelineExecutionsPaginatePaginationConfigTypeDef(
    _ListPipelineExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPipelineExecutionsPaginate` `PaginationConfig`

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


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef
):
    """
    Type definition for `ListPipelineExecutionsPaginateResponsepipelineExecutionSummaries` `sourceRevisions`

    Information about the version (or revision) of a source artifact that initiated a
    pipeline execution.

    - **actionName** *(string) --*

      The name of the action that processed the revision to the source artifact.

    - **revisionId** *(string) --*

      The system-generated unique ID that identifies the revision number of the artifact.

    - **revisionSummary** *(string) --*

      Summary information about the most recent revision of the artifact. For GitHub and
      AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
      the user-provided content of a ``codepipeline-artifact-revision-summary`` key
      specified in the object metadata.

    - **revisionUrl** *(string) --*

      The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
      CodeCommit repositories, the commit ID is linked to a commit details page.
    """


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef",
    {"triggerType": str, "triggerDetail": str},
    total=False,
)


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef
):
    """
    Type definition for `ListPipelineExecutionsPaginateResponsepipelineExecutionSummaries` `trigger`

    The interaction or event that started a pipeline execution, such as automated change
    detection or a ``StartPipelineExecution`` API call.

    - **triggerType** *(string) --*

      The type of change-detection method, command, or user interaction that started a
      pipeline execution.

    - **triggerDetail** *(string) --*

      Detail related to the event that started a pipeline execution, such as the webhook ARN
      of the webhook that triggered the pipeline execution or the user ARN for a
      user-initiated ``start-pipeline-execution`` CLI command.
    """


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef",
    {
        "pipelineExecutionId": str,
        "status": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List[
            ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef
        ],
        "trigger": ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef,
    },
    total=False,
)


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef
):
    """
    Type definition for `ListPipelineExecutionsPaginateResponse` `pipelineExecutionSummaries`

    Summary information about a pipeline execution.

    - **pipelineExecutionId** *(string) --*

      The ID of the pipeline execution.

    - **status** *(string) --*

      The status of the pipeline execution.

      * InProgress: The pipeline execution is currently running.

      * Succeeded: The pipeline execution was completed successfully.

      * Superseded: While this pipeline execution was waiting for the next stage to be
      completed, a newer pipeline execution advanced and continued through the pipeline instead.

      * Failed: The pipeline execution was not completed successfully.

    - **startTime** *(datetime) --*

      The date and time when the pipeline execution began, in timestamp format.

    - **lastUpdateTime** *(datetime) --*

      The date and time of the last change to the pipeline execution, in timestamp format.

    - **sourceRevisions** *(list) --*

      A list of the source artifact revisions that initiated a pipeline execution.

      - *(dict) --*

        Information about the version (or revision) of a source artifact that initiated a
        pipeline execution.

        - **actionName** *(string) --*

          The name of the action that processed the revision to the source artifact.

        - **revisionId** *(string) --*

          The system-generated unique ID that identifies the revision number of the artifact.

        - **revisionSummary** *(string) --*

          Summary information about the most recent revision of the artifact. For GitHub and
          AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
          the user-provided content of a ``codepipeline-artifact-revision-summary`` key
          specified in the object metadata.

        - **revisionUrl** *(string) --*

          The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
          CodeCommit repositories, the commit ID is linked to a commit details page.

    - **trigger** *(dict) --*

      The interaction or event that started a pipeline execution, such as automated change
      detection or a ``StartPipelineExecution`` API call.

      - **triggerType** *(string) --*

        The type of change-detection method, command, or user interaction that started a
        pipeline execution.

      - **triggerDetail** *(string) --*

        Detail related to the event that started a pipeline execution, such as the webhook ARN
        of the webhook that triggered the pipeline execution or the user ARN for a
        user-initiated ``start-pipeline-execution`` CLI command.
    """


_ListPipelineExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListPipelineExecutionsPaginateResponseTypeDef(
    _ListPipelineExecutionsPaginateResponseTypeDef
):
    """
    Type definition for `ListPipelineExecutionsPaginate` `Response`

    Represents the output of a ``ListPipelineExecutions`` action.

    - **pipelineExecutionSummaries** *(list) --*

      A list of executions in the history of a pipeline.

      - *(dict) --*

        Summary information about a pipeline execution.

        - **pipelineExecutionId** *(string) --*

          The ID of the pipeline execution.

        - **status** *(string) --*

          The status of the pipeline execution.

          * InProgress: The pipeline execution is currently running.

          * Succeeded: The pipeline execution was completed successfully.

          * Superseded: While this pipeline execution was waiting for the next stage to be
          completed, a newer pipeline execution advanced and continued through the pipeline instead.

          * Failed: The pipeline execution was not completed successfully.

        - **startTime** *(datetime) --*

          The date and time when the pipeline execution began, in timestamp format.

        - **lastUpdateTime** *(datetime) --*

          The date and time of the last change to the pipeline execution, in timestamp format.

        - **sourceRevisions** *(list) --*

          A list of the source artifact revisions that initiated a pipeline execution.

          - *(dict) --*

            Information about the version (or revision) of a source artifact that initiated a
            pipeline execution.

            - **actionName** *(string) --*

              The name of the action that processed the revision to the source artifact.

            - **revisionId** *(string) --*

              The system-generated unique ID that identifies the revision number of the artifact.

            - **revisionSummary** *(string) --*

              Summary information about the most recent revision of the artifact. For GitHub and
              AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions,
              the user-provided content of a ``codepipeline-artifact-revision-summary`` key
              specified in the object metadata.

            - **revisionUrl** *(string) --*

              The commit ID for the artifact revision. For artifacts stored in GitHub or AWS
              CodeCommit repositories, the commit ID is linked to a commit details page.

        - **trigger** *(dict) --*

          The interaction or event that started a pipeline execution, such as automated change
          detection or a ``StartPipelineExecution`` API call.

          - **triggerType** *(string) --*

            The type of change-detection method, command, or user interaction that started a
            pipeline execution.

          - **triggerDetail** *(string) --*

            Detail related to the event that started a pipeline execution, such as the webhook ARN
            of the webhook that triggered the pipeline execution or the user ARN for a
            user-initiated ``start-pipeline-execution`` CLI command.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(
    _ListPipelinesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPipelinesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPipelinesPaginateResponsepipelinesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)


class ListPipelinesPaginateResponsepipelinesTypeDef(
    _ListPipelinesPaginateResponsepipelinesTypeDef
):
    """
    Type definition for `ListPipelinesPaginateResponse` `pipelines`

    Returns a summary of a pipeline.

    - **name** *(string) --*

      The name of the pipeline.

    - **version** *(integer) --*

      The version number of the pipeline.

    - **created** *(datetime) --*

      The date and time the pipeline was created, in timestamp format.

    - **updated** *(datetime) --*

      The date and time of the last update to the pipeline, in timestamp format.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {
        "pipelines": List[ListPipelinesPaginateResponsepipelinesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    Type definition for `ListPipelinesPaginate` `Response`

    Represents the output of a ``ListPipelines`` action.

    - **pipelines** *(list) --*

      The list of pipelines.

      - *(dict) --*

        Returns a summary of a pipeline.

        - **name** *(string) --*

          The name of the pipeline.

        - **version** *(integer) --*

          The version number of the pipeline.

        - **created** *(datetime) --*

          The date and time the pipeline was created, in timestamp format.

        - **updated** *(datetime) --*

          The date and time of the last update to the pipeline, in timestamp format.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

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


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **tags** *(list) --*

      The tags for the resource.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListWebhooksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWebhooksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWebhooksPaginatePaginationConfigTypeDef(
    _ListWebhooksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListWebhooksPaginate` `PaginationConfig`

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


_ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef
):
    """
    Type definition for `ListWebhooksPaginateResponsewebhooksdefinition` `authenticationConfiguration`

    Properties that configure the authentication applied to incoming webhook trigger
    requests. The required properties depend on the authentication type. For GITHUB_HMAC,
    only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
    property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
    set.

    - **AllowedIPRange** *(string) --*

      The property used to configure acceptance of webhooks in an IP address range. For IP,
      only the ``AllowedIPRange`` property must be set. This property must be set to a
      valid CIDR range.

    - **SecretToken** *(string) --*

      The property used to configure GitHub authentication. For GITHUB_HMAC, only the
      ``SecretToken`` property must be set.
    """


_ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef
):
    """
    Type definition for `ListWebhooksPaginateResponsewebhooksdefinition` `filters`

    The event criteria that specify when a webhook notification is sent to your URL.

    - **jsonPath** *(string) --*

      A JsonPath expression that is applied to the body/payload of the webhook. The value
      selected by the JsonPath expression must match the value specified in the
      ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
      `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

    - **matchEquals** *(string) --*

      The value selected by the ``JsonPath`` expression must match what is supplied in
      the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
      target action configuration can be included as placeholders in this value by
      surrounding the action configuration key with curly brackets. For example, if the
      value supplied here is "refs/heads/{Branch}" and the target action has an action
      configuration property called "Branch" with a value of "master", the
      ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
      configuration properties for built-in action types, see `Pipeline Structure
      Reference Action Requirements
      <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
      .
    """


_ListWebhooksPaginateResponsewebhooksdefinitionTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef],
        "authentication": str,
        "authenticationConfiguration": ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)


class ListWebhooksPaginateResponsewebhooksdefinitionTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionTypeDef
):
    """
    Type definition for `ListWebhooksPaginateResponsewebhooks` `definition`

    The detail returned for each webhook, such as the webhook authentication type and filter
    rules.

    - **name** *(string) --*

      The name of the webhook.

    - **targetPipeline** *(string) --*

      The name of the pipeline you want to connect to the webhook.

    - **targetAction** *(string) --*

      The name of the action in a pipeline you want to connect to the webhook. The action
      must be from the source (first) stage of the pipeline.

    - **filters** *(list) --*

      A list of rules applied to the body/payload sent in the POST request to a webhook URL.
      All defined rules must pass for the request to be accepted and the pipeline started.

      - *(dict) --*

        The event criteria that specify when a webhook notification is sent to your URL.

        - **jsonPath** *(string) --*

          A JsonPath expression that is applied to the body/payload of the webhook. The value
          selected by the JsonPath expression must match the value specified in the
          ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
          `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

        - **matchEquals** *(string) --*

          The value selected by the ``JsonPath`` expression must match what is supplied in
          the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
          target action configuration can be included as placeholders in this value by
          surrounding the action configuration key with curly brackets. For example, if the
          value supplied here is "refs/heads/{Branch}" and the target action has an action
          configuration property called "Branch" with a value of "master", the
          ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
          configuration properties for built-in action types, see `Pipeline Structure
          Reference Action Requirements
          <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
          .

    - **authentication** *(string) --*

      Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

      * For information about the authentication scheme implemented by GITHUB_HMAC, see
      `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
      GitHub Developer website.

      * IP rejects webhooks trigger requests unless they originate from an IP address in the
      IP range whitelisted in the authentication configuration.

      * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

    - **authenticationConfiguration** *(dict) --*

      Properties that configure the authentication applied to incoming webhook trigger
      requests. The required properties depend on the authentication type. For GITHUB_HMAC,
      only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
      property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
      set.

      - **AllowedIPRange** *(string) --*

        The property used to configure acceptance of webhooks in an IP address range. For IP,
        only the ``AllowedIPRange`` property must be set. This property must be set to a
        valid CIDR range.

      - **SecretToken** *(string) --*

        The property used to configure GitHub authentication. For GITHUB_HMAC, only the
        ``SecretToken`` property must be set.
    """


_ListWebhooksPaginateResponsewebhookstagsTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhookstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ListWebhooksPaginateResponsewebhookstagsTypeDef(
    _ListWebhooksPaginateResponsewebhookstagsTypeDef
):
    """
    Type definition for `ListWebhooksPaginateResponsewebhooks` `tags`

    A tag is a key-value pair that is used to manage the resource.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ListWebhooksPaginateResponsewebhooksTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksTypeDef",
    {
        "definition": ListWebhooksPaginateResponsewebhooksdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ListWebhooksPaginateResponsewebhookstagsTypeDef],
    },
    total=False,
)


class ListWebhooksPaginateResponsewebhooksTypeDef(
    _ListWebhooksPaginateResponsewebhooksTypeDef
):
    """
    Type definition for `ListWebhooksPaginateResponse` `webhooks`

    The detail returned for each webhook after listing webhooks, such as the webhook URL, the
    webhook name, and the webhook ARN.

    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.

      - **name** *(string) --*

        The name of the webhook.

      - **targetPipeline** *(string) --*

        The name of the pipeline you want to connect to the webhook.

      - **targetAction** *(string) --*

        The name of the action in a pipeline you want to connect to the webhook. The action
        must be from the source (first) stage of the pipeline.

      - **filters** *(list) --*

        A list of rules applied to the body/payload sent in the POST request to a webhook URL.
        All defined rules must pass for the request to be accepted and the pipeline started.

        - *(dict) --*

          The event criteria that specify when a webhook notification is sent to your URL.

          - **jsonPath** *(string) --*

            A JsonPath expression that is applied to the body/payload of the webhook. The value
            selected by the JsonPath expression must match the value specified in the
            ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
            `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

          - **matchEquals** *(string) --*

            The value selected by the ``JsonPath`` expression must match what is supplied in
            the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
            target action configuration can be included as placeholders in this value by
            surrounding the action configuration key with curly brackets. For example, if the
            value supplied here is "refs/heads/{Branch}" and the target action has an action
            configuration property called "Branch" with a value of "master", the
            ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
            configuration properties for built-in action types, see `Pipeline Structure
            Reference Action Requirements
            <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
            .

      - **authentication** *(string) --*

        Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

        * For information about the authentication scheme implemented by GITHUB_HMAC, see
        `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
        GitHub Developer website.

        * IP rejects webhooks trigger requests unless they originate from an IP address in the
        IP range whitelisted in the authentication configuration.

        * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

      - **authenticationConfiguration** *(dict) --*

        Properties that configure the authentication applied to incoming webhook trigger
        requests. The required properties depend on the authentication type. For GITHUB_HMAC,
        only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
        property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
        set.

        - **AllowedIPRange** *(string) --*

          The property used to configure acceptance of webhooks in an IP address range. For IP,
          only the ``AllowedIPRange`` property must be set. This property must be set to a
          valid CIDR range.

        - **SecretToken** *(string) --*

          The property used to configure GitHub authentication. For GITHUB_HMAC, only the
          ``SecretToken`` property must be set.

    - **url** *(string) --*

      A unique URL generated by CodePipeline. When a POST request is made to this URL, the
      defined pipeline is started as long as the body of the post request satisfies the defined
      authentication and filtering conditions. Deleting and re-creating a webhook makes the old
      URL invalid and generates a new one.

    - **errorMessage** *(string) --*

      The text of the error message about the webhook.

    - **errorCode** *(string) --*

      The number code of the error.

    - **lastTriggered** *(datetime) --*

      The date and time a webhook was last successfully triggered, in timestamp format.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the webhook.

    - **tags** *(list) --*

      Specifies the tags applied to the webhook.

      - *(dict) --*

        A tag is a key-value pair that is used to manage the resource.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.
    """


_ListWebhooksPaginateResponseTypeDef = TypedDict(
    "_ListWebhooksPaginateResponseTypeDef",
    {"webhooks": List[ListWebhooksPaginateResponsewebhooksTypeDef]},
    total=False,
)


class ListWebhooksPaginateResponseTypeDef(_ListWebhooksPaginateResponseTypeDef):
    """
    Type definition for `ListWebhooksPaginate` `Response`

    - **webhooks** *(list) --*

      The JSON detail returned for each webhook in the list output for the ListWebhooks call.

      - *(dict) --*

        The detail returned for each webhook after listing webhooks, such as the webhook URL, the
        webhook name, and the webhook ARN.

        - **definition** *(dict) --*

          The detail returned for each webhook, such as the webhook authentication type and filter
          rules.

          - **name** *(string) --*

            The name of the webhook.

          - **targetPipeline** *(string) --*

            The name of the pipeline you want to connect to the webhook.

          - **targetAction** *(string) --*

            The name of the action in a pipeline you want to connect to the webhook. The action
            must be from the source (first) stage of the pipeline.

          - **filters** *(list) --*

            A list of rules applied to the body/payload sent in the POST request to a webhook URL.
            All defined rules must pass for the request to be accepted and the pipeline started.

            - *(dict) --*

              The event criteria that specify when a webhook notification is sent to your URL.

              - **jsonPath** *(string) --*

                A JsonPath expression that is applied to the body/payload of the webhook. The value
                selected by the JsonPath expression must match the value specified in the
                ``MatchEquals`` field. Otherwise, the request is ignored. For more information, see
                `Java JsonPath implementation <https://github.com/json-path/JsonPath>`__ in GitHub.

              - **matchEquals** *(string) --*

                The value selected by the ``JsonPath`` expression must match what is supplied in
                the ``MatchEquals`` field. Otherwise, the request is ignored. Properties from the
                target action configuration can be included as placeholders in this value by
                surrounding the action configuration key with curly brackets. For example, if the
                value supplied here is "refs/heads/{Branch}" and the target action has an action
                configuration property called "Branch" with a value of "master", the
                ``MatchEquals`` value is evaluated as "refs/heads/master". For a list of action
                configuration properties for built-in action types, see `Pipeline Structure
                Reference Action Requirements
                <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__
                .

          - **authentication** *(string) --*

            Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

            * For information about the authentication scheme implemented by GITHUB_HMAC, see
            `Securing your webhooks <https://developer.github.com/webhooks/securing/>`__ on the
            GitHub Developer website.

            * IP rejects webhooks trigger requests unless they originate from an IP address in the
            IP range whitelisted in the authentication configuration.

            * UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.

          - **authenticationConfiguration** *(dict) --*

            Properties that configure the authentication applied to incoming webhook trigger
            requests. The required properties depend on the authentication type. For GITHUB_HMAC,
            only the ``SecretToken`` property must be set. For IP, only the ``AllowedIPRange``
            property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be
            set.

            - **AllowedIPRange** *(string) --*

              The property used to configure acceptance of webhooks in an IP address range. For IP,
              only the ``AllowedIPRange`` property must be set. This property must be set to a
              valid CIDR range.

            - **SecretToken** *(string) --*

              The property used to configure GitHub authentication. For GITHUB_HMAC, only the
              ``SecretToken`` property must be set.

        - **url** *(string) --*

          A unique URL generated by CodePipeline. When a POST request is made to this URL, the
          defined pipeline is started as long as the body of the post request satisfies the defined
          authentication and filtering conditions. Deleting and re-creating a webhook makes the old
          URL invalid and generates a new one.

        - **errorMessage** *(string) --*

          The text of the error message about the webhook.

        - **errorCode** *(string) --*

          The number code of the error.

        - **lastTriggered** *(datetime) --*

          The date and time a webhook was last successfully triggered, in timestamp format.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the webhook.

        - **tags** *(list) --*

          Specifies the tags applied to the webhook.

          - *(dict) --*

            A tag is a key-value pair that is used to manage the resource.

            - **key** *(string) --*

              The tag's key.

            - **value** *(string) --*

              The tag's value.
    """
