"Main interface for codepipeline Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codepipeline.type_defs import (
    ListActionExecutionsPaginatePaginationConfigTypeDef,
    ListActionExecutionsPaginateResponseTypeDef,
    ListActionExecutionsPaginatefilterTypeDef,
    ListActionTypesPaginatePaginationConfigTypeDef,
    ListActionTypesPaginateResponseTypeDef,
    ListPipelineExecutionsPaginatePaginationConfigTypeDef,
    ListPipelineExecutionsPaginateResponseTypeDef,
    ListPipelinesPaginatePaginationConfigTypeDef,
    ListPipelinesPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListWebhooksPaginatePaginationConfigTypeDef,
    ListWebhooksPaginateResponseTypeDef,
)


__all__ = (
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)


class ListActionExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_action_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineName: str,
        filter: ListActionExecutionsPaginatefilterTypeDef = None,
        PaginationConfig: ListActionExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListActionExecutionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_action_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListActionExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              pipelineName='string',
              filter={
                  'pipelineExecutionId': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline for which you want to list action execution history.

        :type filter: dict
        :param filter:

          Input information used to filter action execution history.

          - **pipelineExecutionId** *(string) --*

            The pipeline execution ID used to filter action execution history.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'actionExecutionDetails': [
                    {
                        'pipelineExecutionId': 'string',
                        'actionExecutionId': 'string',
                        'pipelineVersion': 123,
                        'stageName': 'string',
                        'actionName': 'string',
                        'startTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'status': 'InProgress'|'Succeeded'|'Failed',
                        'input': {
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'configuration': {
                                'string': 'string'
                            },
                            'resolvedConfiguration': {
                                'string': 'string'
                            },
                            'roleArn': 'string',
                            'region': 'string',
                            'inputArtifacts': [
                                {
                                    'name': 'string',
                                    's3location': {
                                        'bucket': 'string',
                                        'key': 'string'
                                    }
                                },
                            ],
                            'namespace': 'string'
                        },
                        'output': {
                            'outputArtifacts': [
                                {
                                    'name': 'string',
                                    's3location': {
                                        'bucket': 'string',
                                        'key': 'string'
                                    }
                                },
                            ],
                            'executionResult': {
                                'externalExecutionId': 'string',
                                'externalExecutionSummary': 'string',
                                'externalExecutionUrl': 'string'
                            },
                            'outputVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListActionTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_action_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        actionOwnerFilter: str = None,
        PaginationConfig: ListActionTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListActionTypesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_action_types`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListActionTypes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              actionOwnerFilter='AWS'|'ThirdParty'|'Custom',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type actionOwnerFilter: string
        :param actionOwnerFilter:

          Filters the list of action types to those created by a specified entity.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'actionTypes': [
                    {
                        'id': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'settings': {
                            'thirdPartyConfigurationUrl': 'string',
                            'entityUrlTemplate': 'string',
                            'executionUrlTemplate': 'string',
                            'revisionUrlTemplate': 'string'
                        },
                        'actionConfigurationProperties': [
                            {
                                'name': 'string',
                                'required': True|False,
                                'key': True|False,
                                'secret': True|False,
                                'queryable': True|False,
                                'description': 'string',
                                'type': 'String'|'Number'|'Boolean'
                            },
                        ],
                        'inputArtifactDetails': {
                            'minimumCount': 123,
                            'maximumCount': 123
                        },
                        'outputArtifactDetails': {
                            'minimumCount': 123,
                            'maximumCount': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_pipeline_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pipelineName: str,
        PaginationConfig: ListPipelineExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPipelineExecutionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_pipeline_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelineExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              pipelineName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**

          The name of the pipeline for which you want to get execution summary information.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pipelineExecutionSummaries': [
                    {
                        'pipelineExecutionId': 'string',
                        'status': 'InProgress'|'Succeeded'|'Superseded'|'Failed',
                        'startTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'sourceRevisions': [
                            {
                                'actionName': 'string',
                                'revisionId': 'string',
                                'revisionSummary': 'string',
                                'revisionUrl': 'string'
                            },
                        ],
                        'trigger': {
                            'triggerType':
                            'CreatePipeline'|'StartPipelineExecution'|'PollForSourceChanges'|'Webhook'
                            |'CloudWatchEvent'|'PutActionRevision',
                            'triggerDetail': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListPipelinesPaginator(Boto3Paginator):
    """
    Paginator for `list_pipelines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPipelinesPaginatePaginationConfigTypeDef = None
    ) -> ListPipelinesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_pipelines`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelines>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pipelines': [
                    {
                        'name': 'string',
                        'version': 123,
                        'created': datetime(2015, 1, 1),
                        'updated': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_tags_for_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListTagsForResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              resourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to get tags for.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListWebhooksPaginator(Boto3Paginator):
    """
    Paginator for `list_webhooks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListWebhooksPaginatePaginationConfigTypeDef = None
    ) -> ListWebhooksPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodePipeline.Client.list_webhooks`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListWebhooks>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhooks': [
                    {
                        'definition': {
                            'name': 'string',
                            'targetPipeline': 'string',
                            'targetAction': 'string',
                            'filters': [
                                {
                                    'jsonPath': 'string',
                                    'matchEquals': 'string'
                                },
                            ],
                            'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
                            'authenticationConfiguration': {
                                'AllowedIPRange': 'string',
                                'SecretToken': 'string'
                            }
                        },
                        'url': 'string',
                        'errorMessage': 'string',
                        'errorCode': 'string',
                        'lastTriggered': datetime(2015, 1, 1),
                        'arn': 'string',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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
