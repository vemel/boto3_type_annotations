"Main interface for amplify Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_amplify.type_defs import (
    ListAppsPaginatePaginationConfigTypeDef,
    ListAppsPaginateResponseTypeDef,
    ListBranchesPaginatePaginationConfigTypeDef,
    ListBranchesPaginateResponseTypeDef,
    ListDomainAssociationsPaginatePaginationConfigTypeDef,
    ListDomainAssociationsPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
)


__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)


class ListAppsPaginator(Boto3Paginator):
    """
    Paginator for `list_apps`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAppsPaginatePaginationConfigTypeDef = None
    ) -> ListAppsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_apps`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListApps>`_

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
                'apps': [
                    {
                        'appId': 'string',
                        'appArn': 'string',
                        'name': 'string',
                        'tags': {
                            'string': 'string'
                        },
                        'description': 'string',
                        'repository': 'string',
                        'platform': 'WEB',
                        'createTime': datetime(2015, 1, 1),
                        'updateTime': datetime(2015, 1, 1),
                        'iamServiceRoleArn': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'defaultDomain': 'string',
                        'enableBranchAutoBuild': True|False,
                        'enableBasicAuth': True|False,
                        'basicAuthCredentials': 'string',
                        'customRules': [
                            {
                                'source': 'string',
                                'target': 'string',
                                'status': 'string',
                                'condition': 'string'
                            },
                        ],
                        'productionBranch': {
                            'lastDeployTime': datetime(2015, 1, 1),
                            'status': 'string',
                            'thumbnailUrl': 'string',
                            'branchName': 'string'
                        },
                        'buildSpec': 'string',
                        'enableAutoBranchCreation': True|False,
                        'autoBranchCreationPatterns': [
                            'string',
                        ],
                        'autoBranchCreationConfig': {
                            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                            'framework': 'string',
                            'enableAutoBuild': True|False,
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'basicAuthCredentials': 'string',
                            'enableBasicAuth': True|False,
                            'buildSpec': 'string',
                            'enablePullRequestPreview': True|False,
                            'pullRequestEnvironmentName': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for an Amplify App list request.

            - **apps** *(list) --*

              List of Amplify Apps.

              - *(dict) --*

                Amplify App represents different branches of a repository for building, deploying, and
                hosting.

                - **appId** *(string) --*

                  Unique Id for the Amplify App.

                - **appArn** *(string) --*

                  ARN for the Amplify App.

                - **name** *(string) --*

                  Name for the Amplify App.

                - **tags** *(dict) --*

                  Tag for Amplify App.

                  - *(string) --*

                    - *(string) --*

                - **description** *(string) --*

                  Description for the Amplify App.

                - **repository** *(string) --*

                  Repository for the Amplify App.

                - **platform** *(string) --*

                  Platform for the Amplify App.

                - **createTime** *(datetime) --*

                  Create date / time for the Amplify App.

                - **updateTime** *(datetime) --*

                  Update date / time for the Amplify App.

                - **iamServiceRoleArn** *(string) --*

                  IAM service role ARN for the Amplify App.

                - **environmentVariables** *(dict) --*

                  Environment Variables for the Amplify App.

                  - *(string) --*

                    - *(string) --*

                - **defaultDomain** *(string) --*

                  Default domain for the Amplify App.

                - **enableBranchAutoBuild** *(boolean) --*

                  Enables auto-building of branches for the Amplify App.

                - **enableBasicAuth** *(boolean) --*

                  Enables Basic Authorization for branches for the Amplify App.

                - **basicAuthCredentials** *(string) --*

                  Basic Authorization credentials for branches for the Amplify App.

                - **customRules** *(list) --*

                  Custom redirect / rewrite rules for the Amplify App.

                  - *(dict) --*

                    Custom rewrite / redirect rule.

                    - **source** *(string) --*

                      The source pattern for a URL rewrite or redirect rule.

                    - **target** *(string) --*

                      The target pattern for a URL rewrite or redirect rule.

                    - **status** *(string) --*

                      The status code for a URL rewrite or redirect rule.

                    - **condition** *(string) --*

                      The condition for a URL rewrite or redirect rule, e.g. country code.

                - **productionBranch** *(dict) --*

                  Structure with Production Branch information.

                  - **lastDeployTime** *(datetime) --*

                    Last Deploy Time of Production Branch.

                  - **status** *(string) --*

                    Status of Production Branch.

                  - **thumbnailUrl** *(string) --*

                    Thumbnail URL for Production Branch.

                  - **branchName** *(string) --*

                    Branch Name for Production Branch.

                - **buildSpec** *(string) --*

                  BuildSpec content for Amplify App.

                - **enableAutoBranchCreation** *(boolean) --*

                  Enables automated branch creation for the Amplify App.

                - **autoBranchCreationPatterns** *(list) --*

                  Automated branch creation glob patterns for the Amplify App.

                  - *(string) --*

                - **autoBranchCreationConfig** *(dict) --*

                  Automated branch creation config for the Amplify App.

                  - **stage** *(string) --*

                    Stage for the auto created branch.

                  - **framework** *(string) --*

                    Framework for the auto created branch.

                  - **enableAutoBuild** *(boolean) --*

                    Enables auto building for the auto created branch.

                  - **environmentVariables** *(dict) --*

                    Environment Variables for the auto created branch.

                    - *(string) --*

                      - *(string) --*

                  - **basicAuthCredentials** *(string) --*

                    Basic Authorization credentials for the auto created branch.

                  - **enableBasicAuth** *(boolean) --*

                    Enables Basic Auth for the auto created branch.

                  - **buildSpec** *(string) --*

                    BuildSpec for the auto created branch.

                  - **enablePullRequestPreview** *(boolean) --*

                    Enables Pull Request Preview for auto created branch.

                  - **pullRequestEnvironmentName** *(string) --*

                    The Amplify Environment name for the pull request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListBranchesPaginator(Boto3Paginator):
    """
    Paginator for `list_branches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appId: str,
        PaginationConfig: ListBranchesPaginatePaginationConfigTypeDef = None,
    ) -> ListBranchesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Amplify.Client.list_branches`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListBranches>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              appId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

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
                'branches': [
                    {
                        'branchArn': 'string',
                        'branchName': 'string',
                        'description': 'string',
                        'tags': {
                            'string': 'string'
                        },
                        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                        'displayName': 'string',
                        'enableNotification': True|False,
                        'createTime': datetime(2015, 1, 1),
                        'updateTime': datetime(2015, 1, 1),
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'enableAutoBuild': True|False,
                        'customDomains': [
                            'string',
                        ],
                        'framework': 'string',
                        'activeJobId': 'string',
                        'totalNumberOfJobs': 'string',
                        'enableBasicAuth': True|False,
                        'thumbnailUrl': 'string',
                        'basicAuthCredentials': 'string',
                        'buildSpec': 'string',
                        'ttl': 'string',
                        'associatedResources': [
                            'string',
                        ],
                        'enablePullRequestPreview': True|False,
                        'pullRequestEnvironmentName': 'string',
                        'destinationBranch': 'string',
                        'sourceBranch': 'string',
                        'backendEnvironmentArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for list branches request.

            - **branches** *(list) --*

              List of branches for an Amplify App.

              - *(dict) --*

                Branch for an Amplify App, which maps to a 3rd party repository branch.

                - **branchArn** *(string) --*

                  ARN for a branch, part of an Amplify App.

                - **branchName** *(string) --*

                  Name for a branch, part of an Amplify App.

                - **description** *(string) --*

                  Description for a branch, part of an Amplify App.

                - **tags** *(dict) --*

                  Tag for branch for Amplify App.

                  - *(string) --*

                    - *(string) --*

                - **stage** *(string) --*

                  Stage for a branch, part of an Amplify App.

                - **displayName** *(string) --*

                  Display name for a branch, will use as the default domain prefix.

                - **enableNotification** *(boolean) --*

                  Enables notifications for a branch, part of an Amplify App.

                - **createTime** *(datetime) --*

                  Creation date and time for a branch, part of an Amplify App.

                - **updateTime** *(datetime) --*

                  Last updated date and time for a branch, part of an Amplify App.

                - **environmentVariables** *(dict) --*

                  Environment Variables specific to a branch, part of an Amplify App.

                  - *(string) --*

                    - *(string) --*

                - **enableAutoBuild** *(boolean) --*

                  Enables auto-building on push for a branch, part of an Amplify App.

                - **customDomains** *(list) --*

                  Custom domains for a branch, part of an Amplify App.

                  - *(string) --*

                - **framework** *(string) --*

                  Framework for a branch, part of an Amplify App.

                - **activeJobId** *(string) --*

                  Id of the active job for a branch, part of an Amplify App.

                - **totalNumberOfJobs** *(string) --*

                  Total number of Jobs part of an Amplify App.

                - **enableBasicAuth** *(boolean) --*

                  Enables Basic Authorization for a branch, part of an Amplify App.

                - **thumbnailUrl** *(string) --*

                  Thumbnail URL for the branch.

                - **basicAuthCredentials** *(string) --*

                  Basic Authorization credentials for a branch, part of an Amplify App.

                - **buildSpec** *(string) --*

                  BuildSpec content for branch for Amplify App.

                - **ttl** *(string) --*

                  The content TTL for the website in seconds.

                - **associatedResources** *(list) --*

                  List of custom resources that are linked to this branch.

                  - *(string) --*

                - **enablePullRequestPreview** *(boolean) --*

                  Enables Pull Request Preview for this branch.

                - **pullRequestEnvironmentName** *(string) --*

                  The Amplify Environment name for the pull request.

                - **destinationBranch** *(string) --*

                  The destination branch if the branch is a pull request branch.

                - **sourceBranch** *(string) --*

                  The source branch if the branch is a pull request branch.

                - **backendEnvironmentArn** *(string) --*

                  ARN for a Backend Environment, part of an Amplify App.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDomainAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `list_domain_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appId: str,
        PaginationConfig: ListDomainAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> ListDomainAssociationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Amplify.Client.list_domain_associations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListDomainAssociations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              appId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

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
                'domainAssociations': [
                    {
                        'domainAssociationArn': 'string',
                        'domainName': 'string',
                        'enableAutoSubDomain': True|False,
                        'domainStatus':
                        'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'
                        |'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
                        'statusReason': 'string',
                        'certificateVerificationDNSRecord': 'string',
                        'subDomains': [
                            {
                                'subDomainSetting': {
                                    'prefix': 'string',
                                    'branchName': 'string'
                                },
                                'verified': True|False,
                                'dnsRecord': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the list Domain Association request.

            - **domainAssociations** *(list) --*

              List of Domain Associations.

              - *(dict) --*

                Structure for Domain Association, which associates a custom domain with an Amplify App.

                - **domainAssociationArn** *(string) --*

                  ARN for the Domain Association.

                - **domainName** *(string) --*

                  Name of the domain.

                - **enableAutoSubDomain** *(boolean) --*

                  Enables automated creation of Subdomains for branches. (Currently not supported)

                - **domainStatus** *(string) --*

                  Status fo the Domain Association.

                - **statusReason** *(string) --*

                  Reason for the current status of the Domain Association.

                - **certificateVerificationDNSRecord** *(string) --*

                  DNS Record for certificate verification.

                - **subDomains** *(list) --*

                  Subdomains for the Domain Association.

                  - *(dict) --*

                    Subdomain for the Domain Association.

                    - **subDomainSetting** *(dict) --*

                      Setting structure for the Subdomain.

                      - **prefix** *(string) --*

                        Prefix setting for the Subdomain.

                      - **branchName** *(string) --*

                        Branch name setting for the Subdomain.

                    - **verified** *(boolean) --*

                      Verified status of the Subdomain

                    - **dnsRecord** *(string) --*

                      DNS record for the Subdomain.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appId: str,
        branchName: str,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Amplify.Client.list_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              appId='string',
              branchName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for a branch.

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
                'jobSummaries': [
                    {
                        'jobArn': 'string',
                        'jobId': 'string',
                        'commitId': 'string',
                        'commitMessage': 'string',
                        'commitTime': datetime(2015, 1, 1),
                        'startTime': datetime(2015, 1, 1),
                        'status':
                        'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                        'endTime': datetime(2015, 1, 1),
                        'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Maximum number of records to list in a single response.

            - **jobSummaries** *(list) --*

              Result structure for list job result request.

              - *(dict) --*

                Structure for the summary of a Job.

                - **jobArn** *(string) --*

                  Arn for the Job.

                - **jobId** *(string) --*

                  Unique Id for the Job.

                - **commitId** *(string) --*

                  Commit Id from 3rd party repository provider for the Job.

                - **commitMessage** *(string) --*

                  Commit message from 3rd party repository provider for the Job.

                - **commitTime** *(datetime) --*

                  Commit date / time for the Job.

                - **startTime** *(datetime) --*

                  Start date / time for the Job.

                - **status** *(string) --*

                  Status for the Job.

                - **endTime** *(datetime) --*

                  End date / time for the Job.

                - **jobType** *(string) --*

                  Type for the Job. \\n "RELEASE": Manually released from source by using StartJob API.
                  "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by
                  WebHooks.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
