"Main interface for codedeploy Paginators"
from __future__ import annotations

from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codedeploy.type_defs import (
    ListApplicationRevisionsPaginatePaginationConfigTypeDef,
    ListApplicationRevisionsPaginateResponseTypeDef,
    ListApplicationsPaginatePaginationConfigTypeDef,
    ListApplicationsPaginateResponseTypeDef,
    ListDeploymentConfigsPaginatePaginationConfigTypeDef,
    ListDeploymentConfigsPaginateResponseTypeDef,
    ListDeploymentGroupsPaginatePaginationConfigTypeDef,
    ListDeploymentGroupsPaginateResponseTypeDef,
    ListDeploymentInstancesPaginatePaginationConfigTypeDef,
    ListDeploymentInstancesPaginateResponseTypeDef,
    ListDeploymentTargetsPaginatePaginationConfigTypeDef,
    ListDeploymentTargetsPaginateResponseTypeDef,
    ListDeploymentsPaginatePaginationConfigTypeDef,
    ListDeploymentsPaginateResponseTypeDef,
    ListDeploymentsPaginatecreateTimeRangeTypeDef,
    ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef,
    ListGitHubAccountTokenNamesPaginateResponseTypeDef,
    ListOnPremisesInstancesPaginatePaginationConfigTypeDef,
    ListOnPremisesInstancesPaginateResponseTypeDef,
    ListOnPremisesInstancesPaginatetagFiltersTypeDef,
)


__all__ = (
    "ListApplicationRevisionsPaginator",
    "ListApplicationsPaginator",
    "ListDeploymentConfigsPaginator",
    "ListDeploymentGroupsPaginator",
    "ListDeploymentInstancesPaginator",
    "ListDeploymentTargetsPaginator",
    "ListDeploymentsPaginator",
    "ListGitHubAccountTokenNamesPaginator",
    "ListOnPremisesInstancesPaginator",
)


class ListApplicationRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `list_application_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str,
        sortBy: str = None,
        sortOrder: str = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: str = None,
        PaginationConfig: ListApplicationRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationRevisionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_application_revisions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplicationRevisions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              applicationName='string',
              sortBy='registerTime'|'firstUsedTime'|'lastUsedTime',
              sortOrder='ascending'|'descending',
              s3Bucket='string',
              s3KeyPrefix='string',
              deployed='include'|'exclude'|'ignore',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type sortBy: string
        :param sortBy:

          The column name to use to sort the list results:

          * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy.

          * firstUsedTime: Sort by the time the revisions were first used in a deployment.

          * lastUsedTime: Sort by the time the revisions were last used in a deployment.

          If not specified or set to null, the results are returned in an arbitrary order.

        :type sortOrder: string
        :param sortOrder:

          The order in which to sort the list results:

          * ascending: ascending order.

          * descending: descending order.

          If not specified, the results are sorted in ascending order.

          If set to null, the results are sorted in an arbitrary order.

        :type s3Bucket: string
        :param s3Bucket:

          An Amazon S3 bucket name to limit the search for revisions.

          If set to null, all of the user's buckets are searched.

        :type s3KeyPrefix: string
        :param s3KeyPrefix:

          A key prefix for the set of Amazon S3 objects to limit the search for revisions.

        :type deployed: string
        :param deployed:

          Whether to list revisions based on whether the revision is the target revision of an deployment
          group:

          * include: List revisions that are target revisions of a deployment group.

          * exclude: Do not list revisions that are target revisions of a deployment group.

          * ignore: List all revisions.

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
                'revisions': [
                    {
                        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        },
                        'appSpecContent': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListApplicationRevisions operation.

            - **revisions** *(list) --*

              A list of locations that contain the matching revisions.

              - *(dict) --*

                Information about the location of an application revision.

                - **revisionType** *(string) --*

                  The type of application revision:

                  * S3: An application revision stored in Amazon S3.

                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

                - **s3Location** *(dict) --*

                  Information about the location of a revision stored in Amazon S3.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket where the application revision is stored.

                  - **key** *(string) --*

                    The name of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                  - **bundleType** *(string) --*

                    The file type of the application revision. Must be one of the following:

                    * tar: A tar archive file.

                    * tgz: A compressed tar archive file.

                    * zip: A zip archive file.

                  - **version** *(string) --*

                    A specific version of the Amazon S3 object that represents the bundled artifacts for
                    the application revision.

                    If the version is not specified, the system uses the most recent version by default.

                  - **eTag** *(string) --*

                    The ETag of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                    If the ETag is not specified as an input parameter, ETag validation of the object is
                    skipped.

                - **gitHubLocation** *(dict) --*

                  Information about the location of application artifacts stored in GitHub.

                  - **repository** *(string) --*

                    The GitHub account and repository pair that stores a reference to the commit that
                    represents the bundled artifacts for the application revision.

                    Specified as account/repository.

                  - **commitId** *(string) --*

                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
                    application revision.

                - **string** *(dict) --*

                  Information about the location of an AWS Lambda deployment revision stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string. It includes information about
                    which Lambda function to update and optional Lambda functions that validate deployment
                    lifecycle events.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

                - **appSpecContent** *(dict) --*

                  The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
                  formatted as JSON or YAML and stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string.

                    For an AWS Lambda deployment, the content includes a Lambda function name, the alias
                    for its original version, and the alias for its replacement version. The deployment
                    shifts traffic from the original version of the Lambda function to the replacement
                    version.

                    For an Amazon ECS deployment, the content includes the task name, information about the
                    load balancer that serves traffic to the container, and more.

                    For both types of deployments, the content can specify Lambda functions that run at
                    specified hooks, such as ``BeforeInstall`` , during a deployment.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListApplicationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_applications`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplications>`_

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
                'applications': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListApplications operation.

            - **applications** *(list) --*

              A list of application names.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDeploymentConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListDeploymentConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentConfigsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_deployment_configs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentConfigs>`_

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
                'deploymentConfigsList': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentConfigs operation.

            - **deploymentConfigsList** *(list) --*

              A list of deployment configurations, including built-in configurations such as
              CodeDeployDefault.OneAtATime.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDeploymentGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str,
        PaginationConfig: ListDeploymentGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_deployment_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              applicationName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

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
                'applicationName': 'string',
                'deploymentGroups': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentGroups operation.

            - **applicationName** *(string) --*

              The application name.

            - **deploymentGroups** *(list) --*

              A list of deployment group names.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDeploymentInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[str] = None,
        instanceTypeFilter: List[str] = None,
        PaginationConfig: ListDeploymentInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentInstancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_deployment_instances`.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentInstances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              deploymentId='string',
              instanceStatusFilter=[
                  'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
              ],
              instanceTypeFilter=[
                  'Blue'|'Green',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment.

        :type instanceStatusFilter: list
        :param instanceStatusFilter:

          A subset of instances to list by status:

          * Pending: Include those instances with pending deployments.

          * InProgress: Include those instances where deployments are still in progress.

          * Succeeded: Include those instances with successful deployments.

          * Failed: Include those instances with failed deployments.

          * Skipped: Include those instances with skipped deployments.

          * Unknown: Include those instances with deployments in an unknown state.

          - *(string) --*

        :type instanceTypeFilter: list
        :param instanceTypeFilter:

          The set of instances in a blue/green deployment, either those in the original environment
          ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view instance
          information.

          - *(string) --*

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
                'instancesList': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentInstances operation.

            - **instancesList** *(list) --*

              A list of instance IDs.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDeploymentTargetsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[str, List[str]] = None,
        PaginationConfig: ListDeploymentTargetsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentTargetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_deployment_targets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentTargets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              deploymentId='string',
              targetFilters={
                  'string': [
                      'string',
                  ]
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a deployment.

        :type targetFilters: dict
        :param targetFilters:

          A key used to filter the returned targets. The two valid values are:

          * ``TargetStatus`` - A ``TargetStatus`` filter string can be ``Failed`` , ``InProgress`` ,
          ``Pending`` , ``Ready`` , ``Skipped`` , ``Succeeded`` , or ``Unknown`` .

          * ``ServerInstanceLabel`` - A ``ServerInstanceLabel`` filter string can be ``Blue`` or ``Green`` .

          - *(string) --*

            - *(list) --*

              - *(string) --*

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
                'targetIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **targetIds** *(list) --*

              The unique IDs of deployment targets.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[str] = None,
        createTimeRange: ListDeploymentsPaginatecreateTimeRangeTypeDef = None,
        PaginationConfig: ListDeploymentsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_deployments`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeployments>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              applicationName='string',
              deploymentGroupName='string',
              includeOnlyStatuses=[
                  'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
              ],
              createTimeRange={
                  'start': datetime(2015, 1, 1),
                  'end': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type applicationName: string
        :param applicationName:

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

          .. note::

            If ``applicationName`` is specified, then ``deploymentGroupName`` must be specified. If it is
            not specified, then ``deploymentGroupName`` must not be specified.

        :type deploymentGroupName: string
        :param deploymentGroupName:

          The name of a deployment group for the specified application.

          .. note::

            If ``deploymentGroupName`` is specified, then ``applicationName`` must be specified. If it is
            not specified, then ``applicationName`` must not be specified.

        :type includeOnlyStatuses: list
        :param includeOnlyStatuses:

          A subset of deployments to list by status:

          * Created: Include created deployments in the resulting list.

          * Queued: Include queued deployments in the resulting list.

          * In Progress: Include in-progress deployments in the resulting list.

          * Succeeded: Include successful deployments in the resulting list.

          * Failed: Include failed deployments in the resulting list.

          * Stopped: Include stopped deployments in the resulting list.

          - *(string) --*

        :type createTimeRange: dict
        :param createTimeRange:

          A time range (start and end) for returning a subset of the list of deployments.

          - **start** *(datetime) --*

            The start time of the time range.

            .. note::

              Specify null to leave the start time open-ended.

          - **end** *(datetime) --*

            The end time of the time range.

            .. note::

              Specify null to leave the end time open-ended.

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
                'deployments': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeployments operation.

            - **deployments** *(list) --*

              A list of deployment IDs.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListGitHubAccountTokenNamesPaginator(Boto3Paginator):
    """
    Paginator for `list_git_hub_account_token_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef = None,
    ) -> ListGitHubAccountTokenNamesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_git_hub_account_token_names`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListGitHubAccountTokenNames>`_

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
                'tokenNameList': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListGitHubAccountTokenNames operation.

            - **tokenNameList** *(list) --*

              A list of names of connections to GitHub accounts.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListOnPremisesInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_on_premises_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registrationStatus: str = None,
        tagFilters: List[ListOnPremisesInstancesPaginatetagFiltersTypeDef] = None,
        PaginationConfig: ListOnPremisesInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListOnPremisesInstancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeDeploy.Client.list_on_premises_instances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListOnPremisesInstances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registrationStatus='Registered'|'Deregistered',
              tagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type registrationStatus: string
        :param registrationStatus:

          The registration status of the on-premises instances:

          * Deregistered: Include deregistered on-premises instances in the resulting list.

          * Registered: Include registered on-premises instances in the resulting list.

        :type tagFilters: list
        :param tagFilters:

          The on-premises instance tags that are used to restrict the on-premises instance names returned.

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

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
                'instanceNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of the list on-premises instances operation.

            - **instanceNames** *(list) --*

              The list of matching on-premises instance names.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
