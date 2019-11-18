"Main interface for amplify Client"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_amplify.client as client_scope

# pylint: disable=import-self
import mypy_boto3_amplify.paginator as paginator_scope
from mypy_boto3_amplify.type_defs import (
    ClientCreateAppResponseTypeDef,
    ClientCreateAppautoBranchCreationConfigTypeDef,
    ClientCreateAppcustomRulesTypeDef,
    ClientCreateBranchResponseTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDomainAssociationResponseTypeDef,
    ClientCreateDomainAssociationsubDomainSettingsTypeDef,
    ClientCreateWebhookResponseTypeDef,
    ClientDeleteAppResponseTypeDef,
    ClientDeleteBranchResponseTypeDef,
    ClientDeleteDomainAssociationResponseTypeDef,
    ClientDeleteJobResponseTypeDef,
    ClientDeleteWebhookResponseTypeDef,
    ClientGenerateAccessLogsResponseTypeDef,
    ClientGetAppResponseTypeDef,
    ClientGetArtifactUrlResponseTypeDef,
    ClientGetBranchResponseTypeDef,
    ClientGetDomainAssociationResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetWebhookResponseTypeDef,
    ClientListAppsResponseTypeDef,
    ClientListArtifactsResponseTypeDef,
    ClientListBranchesResponseTypeDef,
    ClientListDomainAssociationsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWebhooksResponseTypeDef,
    ClientStartDeploymentResponseTypeDef,
    ClientStartJobResponseTypeDef,
    ClientStopJobResponseTypeDef,
    ClientUpdateAppResponseTypeDef,
    ClientUpdateAppautoBranchCreationConfigTypeDef,
    ClientUpdateAppcustomRulesTypeDef,
    ClientUpdateBranchResponseTypeDef,
    ClientUpdateDomainAssociationResponseTypeDef,
    ClientUpdateDomainAssociationsubDomainSettingsTypeDef,
    ClientUpdateWebhookResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_app(
        self,
        name: str,
        description: str = None,
        repository: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        oauthToken: str = None,
        accessToken: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[ClientCreateAppcustomRulesTypeDef] = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: ClientCreateAppautoBranchCreationConfigTypeDef = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        Creates a new Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateApp>`_

        **Request Syntax**
        ::

          response = client.create_app(
              name='string',
              description='string',
              repository='string',
              platform='WEB',
              iamServiceRoleArn='string',
              oauthToken='string',
              accessToken='string',
              environmentVariables={
                  'string': 'string'
              },
              enableBranchAutoBuild=True|False,
              enableBasicAuth=True|False,
              basicAuthCredentials='string',
              customRules=[
                  {
                      'source': 'string',
                      'target': 'string',
                      'status': 'string',
                      'condition': 'string'
                  },
              ],
              tags={
                  'string': 'string'
              },
              buildSpec='string',
              enableAutoBranchCreation=True|False,
              autoBranchCreationPatterns=[
                  'string',
              ],
              autoBranchCreationConfig={
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
          )
        :type name: string
        :param name: **[REQUIRED]**

          Name for the Amplify App

        :type description: string
        :param description:

          Description for an Amplify App

        :type repository: string
        :param repository:

          Repository for an Amplify App

        :type platform: string
        :param platform:

          Platform / framework for an Amplify App

        :type iamServiceRoleArn: string
        :param iamServiceRoleArn:

          AWS IAM service role for an Amplify App

        :type oauthToken: string
        :param oauthToken:

          OAuth token for 3rd party source control system for an Amplify App, used to create webhook and
          read-only deploy key. OAuth token is not stored.

        :type accessToken: string
        :param accessToken:

          Personal Access token for 3rd party source control system for an Amplify App, used to create
          webhook and read-only deploy key. Token is not stored.

        :type environmentVariables: dict
        :param environmentVariables:

          Environment variables map for an Amplify App.

          - *(string) --*

            - *(string) --*

        :type enableBranchAutoBuild: boolean
        :param enableBranchAutoBuild:

          Enable the auto building of branches for an Amplify App.

        :type enableBasicAuth: boolean
        :param enableBasicAuth:

          Enable Basic Authorization for an Amplify App, this will apply to all branches part of this App.

        :type basicAuthCredentials: string
        :param basicAuthCredentials:

          Credentials for Basic Authorization for an Amplify App.

        :type customRules: list
        :param customRules:

          Custom rewrite / redirect rules for an Amplify App.

          - *(dict) --*

            Custom rewrite / redirect rule.

            - **source** *(string) --* **[REQUIRED]**

              The source pattern for a URL rewrite or redirect rule.

            - **target** *(string) --* **[REQUIRED]**

              The target pattern for a URL rewrite or redirect rule.

            - **status** *(string) --*

              The status code for a URL rewrite or redirect rule.

            - **condition** *(string) --*

              The condition for a URL rewrite or redirect rule, e.g. country code.

        :type tags: dict
        :param tags:

          Tag for an Amplify App

          - *(string) --*

            - *(string) --*

        :type buildSpec: string
        :param buildSpec:

          BuildSpec for an Amplify App

        :type enableAutoBranchCreation: boolean
        :param enableAutoBranchCreation:

          Enables automated branch creation for the Amplify App.

        :type autoBranchCreationPatterns: list
        :param autoBranchCreationPatterns:

          Automated branch creation glob patterns for the Amplify App.

          - *(string) --*

        :type autoBranchCreationConfig: dict
        :param autoBranchCreationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'app': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            - **app** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        stage: str = None,
        framework: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> ClientCreateBranchResponseTypeDef:
        """
        Creates a new Branch for an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateBranch>`_

        **Request Syntax**
        ::

          response = client.create_branch(
              appId='string',
              branchName='string',
              description='string',
              stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
              framework='string',
              enableNotification=True|False,
              enableAutoBuild=True|False,
              environmentVariables={
                  'string': 'string'
              },
              basicAuthCredentials='string',
              enableBasicAuth=True|False,
              tags={
                  'string': 'string'
              },
              buildSpec='string',
              ttl='string',
              displayName='string',
              enablePullRequestPreview=True|False,
              pullRequestEnvironmentName='string',
              backendEnvironmentArn='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch.

        :type description: string
        :param description:

          Description for the branch.

        :type stage: string
        :param stage:

          Stage for the branch.

        :type framework: string
        :param framework:

          Framework for the branch.

        :type enableNotification: boolean
        :param enableNotification:

          Enables notifications for the branch.

        :type enableAutoBuild: boolean
        :param enableAutoBuild:

          Enables auto building for the branch.

        :type environmentVariables: dict
        :param environmentVariables:

          Environment Variables for the branch.

          - *(string) --*

            - *(string) --*

        :type basicAuthCredentials: string
        :param basicAuthCredentials:

          Basic Authorization credentials for the branch.

        :type enableBasicAuth: boolean
        :param enableBasicAuth:

          Enables Basic Auth for the branch.

        :type tags: dict
        :param tags:

          Tag for the branch.

          - *(string) --*

            - *(string) --*

        :type buildSpec: string
        :param buildSpec:

          BuildSpec for the branch.

        :type ttl: string
        :param ttl:

          The content TTL for the website in seconds.

        :type displayName: string
        :param displayName:

          Display name for a branch, will use as the default domain prefix.

        :type enablePullRequestPreview: boolean
        :param enablePullRequestPreview:

          Enables Pull Request Preview for this branch.

        :type pullRequestEnvironmentName: string
        :param pullRequestEnvironmentName:

          The Amplify Environment name for the pull request.

        :type backendEnvironmentArn: string
        :param backendEnvironmentArn:

          ARN for a Backend Environment, part of an Amplify App.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branch': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for create branch request.

            - **branch** *(dict) --*

              Branch structure for an Amplify App.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self, appId: str, branchName: str, fileMap: Dict[str, str] = None
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        Create a deployment for manual deploy apps. (Apps are not connected to repository)

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateDeployment>`_

        **Request Syntax**
        ::

          response = client.create_deployment(
              appId='string',
              branchName='string',
              fileMap={
                  'string': 'string'
              }
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type fileMap: dict
        :param fileMap:

          Optional file map that contains file name as the key and file content md5 hash as the value. If
          this argument is provided, the service will generate different upload url per file. Otherwise,
          the service will only generate a single upload url for the zipped files.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'jobId': 'string',
                'fileUploadUrls': {
                    'string': 'string'
                },
                'zipUploadUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for create a new deployment.

            - **jobId** *(string) --*

              The jobId for this deployment, will supply to start deployment api.

            - **fileUploadUrls** *(dict) --*

              When the fileMap argument is provided in the request, the fileUploadUrls will contain a map
              of file names to upload url.

              - *(string) --*

                - *(string) --*

            - **zipUploadUrl** *(string) --*

              When the fileMap argument is NOT provided. This zipUploadUrl will be returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[ClientCreateDomainAssociationsubDomainSettingsTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> ClientCreateDomainAssociationResponseTypeDef:
        """
        Create a new DomainAssociation on an App

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateDomainAssociation>`_

        **Request Syntax**
        ::

          response = client.create_domain_association(
              appId='string',
              domainName='string',
              enableAutoSubDomain=True|False,
              subDomainSettings=[
                  {
                      'prefix': 'string',
                      'branchName': 'string'
                  },
              ]
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type domainName: string
        :param domainName: **[REQUIRED]**

          Domain name for the Domain Association.

        :type enableAutoSubDomain: boolean
        :param enableAutoSubDomain:

          Enables automated creation of Subdomains for branches. (Currently not supported)

        :type subDomainSettings: list
        :param subDomainSettings: **[REQUIRED]**

          Setting structure for the Subdomain.

          - *(dict) --*

            Setting for the Subdomain.

            - **prefix** *(string) --* **[REQUIRED]**

              Prefix setting for the Subdomain.

            - **branchName** *(string) --* **[REQUIRED]**

              Branch name setting for the Subdomain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'domainAssociation': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the create Domain Association request.

            - **domainAssociation** *(dict) --*

              Domain Association structure.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_webhook(
        self, appId: str, branchName: str, description: str = None
    ) -> ClientCreateWebhookResponseTypeDef:
        """
        Create a new webhook on an App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateWebhook>`_

        **Request Syntax**
        ::

          response = client.create_webhook(
              appId='string',
              branchName='string',
              description='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for a branch, part of an Amplify App.

        :type description: string
        :param description:

          Description for a webhook.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'webhookArn': 'string',
                    'webhookId': 'string',
                    'webhookUrl': 'string',
                    'branchName': 'string',
                    'description': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'updateTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the create webhook request.

            - **webhook** *(dict) --*

              Webhook structure.

              - **webhookArn** *(string) --*

                ARN for the webhook.

              - **webhookId** *(string) --*

                Id of the webhook.

              - **webhookUrl** *(string) --*

                Url of the webhook.

              - **branchName** *(string) --*

                Name for a branch, part of an Amplify App.

              - **description** *(string) --*

                Description for a webhook.

              - **createTime** *(datetime) --*

                Create date / time for a webhook.

              - **updateTime** *(datetime) --*

                Update date / time for a webhook.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app(self, appId: str) -> ClientDeleteAppResponseTypeDef:
        """
        Delete an existing Amplify App by appId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteApp>`_

        **Request Syntax**
        ::

          response = client.delete_app(
              appId='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'app': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for an Amplify App delete request.

            - **app** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_branch(
        self, appId: str, branchName: str
    ) -> ClientDeleteBranchResponseTypeDef:
        """
        Deletes a branch for an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteBranch>`_

        **Request Syntax**
        ::

          response = client.delete_branch(
              appId='string',
              branchName='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branch': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for delete branch request.

            - **branch** *(dict) --*

              Branch structure for an Amplify App.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_domain_association(
        self, appId: str, domainName: str
    ) -> ClientDeleteDomainAssociationResponseTypeDef:
        """
        Deletes a DomainAssociation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteDomainAssociation>`_

        **Request Syntax**
        ::

          response = client.delete_domain_association(
              appId='string',
              domainName='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type domainName: string
        :param domainName: **[REQUIRED]**

          Name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'domainAssociation': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            - **domainAssociation** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job(
        self, appId: str, branchName: str, jobId: str
    ) -> ClientDeleteJobResponseTypeDef:
        """
        Delete a job, for an Amplify branch, part of Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteJob>`_

        **Request Syntax**
        ::

          response = client.delete_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type jobId: string
        :param jobId: **[REQUIRED]**

          Unique Id for the Job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'jobSummary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the delete job request.

            - **jobSummary** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, webhookId: str) -> ClientDeleteWebhookResponseTypeDef:
        """
        Deletes a webhook.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteWebhook>`_

        **Request Syntax**
        ::

          response = client.delete_webhook(
              webhookId='string'
          )
        :type webhookId: string
        :param webhookId: **[REQUIRED]**

          Unique Id for a webhook.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'webhookArn': 'string',
                    'webhookId': 'string',
                    'webhookUrl': 'string',
                    'branchName': 'string',
                    'description': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'updateTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the delete webhook request.

            - **webhook** *(dict) --*

              Webhook structure.

              - **webhookArn** *(string) --*

                ARN for the webhook.

              - **webhookId** *(string) --*

                Id of the webhook.

              - **webhookUrl** *(string) --*

                Url of the webhook.

              - **branchName** *(string) --*

                Name for a branch, part of an Amplify App.

              - **description** *(string) --*

                Description for a webhook.

              - **createTime** *(datetime) --*

                Create date / time for a webhook.

              - **updateTime** *(datetime) --*

                Update date / time for a webhook.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_access_logs(
        self,
        domainName: str,
        appId: str,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> ClientGenerateAccessLogsResponseTypeDef:
        """
        Retrieve website access logs for a specific time range via a pre-signed URL.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GenerateAccessLogs>`_

        **Request Syntax**
        ::

          response = client.generate_access_logs(
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              domainName='string',
              appId='string'
          )
        :type startTime: datetime
        :param startTime:

          The time at which the logs should start, inclusive.

        :type endTime: datetime
        :param endTime:

          The time at which the logs should end, inclusive.

        :type domainName: string
        :param domainName: **[REQUIRED]**

          Name of the domain.

        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'logUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the generate access logs request.

            - **logUrl** *(string) --*

              Pre-signed URL for the requested access logs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app(self, appId: str) -> ClientGetAppResponseTypeDef:
        """
        Retrieves an existing Amplify App by appId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetApp>`_

        **Request Syntax**
        ::

          response = client.get_app(
              appId='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'app': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            - **app** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_artifact_url(self, artifactId: str) -> ClientGetArtifactUrlResponseTypeDef:
        """
        Retrieves artifact info that corresponds to a artifactId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetArtifactUrl>`_

        **Request Syntax**
        ::

          response = client.get_artifact_url(
              artifactId='string'
          )
        :type artifactId: string
        :param artifactId: **[REQUIRED]**

          Unique Id for a artifact.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'artifactId': 'string',
                'artifactUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the get artifact request.

            - **artifactId** *(string) --*

              Unique Id for a artifact.

            - **artifactUrl** *(string) --*

              Presigned url for the artifact.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_branch(self, appId: str, branchName: str) -> ClientGetBranchResponseTypeDef:
        """
        Retrieves a branch for an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetBranch>`_

        **Request Syntax**
        ::

          response = client.get_branch(
              appId='string',
              branchName='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branch': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            - **branch** *(dict) --*

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_association(
        self, appId: str, domainName: str
    ) -> ClientGetDomainAssociationResponseTypeDef:
        """
        Retrieves domain info that corresponds to an appId and domainName.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetDomainAssociation>`_

        **Request Syntax**
        ::

          response = client.get_domain_association(
              appId='string',
              domainName='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type domainName: string
        :param domainName: **[REQUIRED]**

          Name of the domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'domainAssociation': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the get Domain Association request.

            - **domainAssociation** *(dict) --*

              Domain Association structure.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(
        self, appId: str, branchName: str, jobId: str
    ) -> ClientGetJobResponseTypeDef:
        """
        Get a job for a branch, part of an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetJob>`_

        **Request Syntax**
        ::

          response = client.get_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type jobId: string
        :param jobId: **[REQUIRED]**

          Unique Id for the Job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'job': {
                    'summary': {
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
                    'steps': [
                        {
                            'stepName': 'string',
                            'startTime': datetime(2015, 1, 1),
                            'status':
                            'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                            'endTime': datetime(2015, 1, 1),
                            'logUrl': 'string',
                            'artifactsUrl': 'string',
                            'testArtifactsUrl': 'string',
                            'testConfigUrl': 'string',
                            'screenshots': {
                                'string': 'string'
                            },
                            'statusReason': 'string',
                            'context': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **job** *(dict) --*

              Structure for an execution job for an Amplify App.

              - **summary** *(dict) --*

                Summary for an execution job for an Amplify App.

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

              - **steps** *(list) --*

                Execution steps for an execution job, for an Amplify App.

                - *(dict) --*

                  Structure for an execution step for an execution job, for an Amplify App.

                  - **stepName** *(string) --*

                    Name of the execution step.

                  - **startTime** *(datetime) --*

                    Start date/ time of the execution step.

                  - **status** *(string) --*

                    Status of the execution step.

                  - **endTime** *(datetime) --*

                    End date/ time of the execution step.

                  - **logUrl** *(string) --*

                    URL to the logs for the execution step.

                  - **artifactsUrl** *(string) --*

                    URL to the artifact for the execution step.

                  - **testArtifactsUrl** *(string) --*

                    URL to the test artifact for the execution step.

                  - **testConfigUrl** *(string) --*

                    URL to the test config for the execution step.

                  - **screenshots** *(dict) --*

                    List of screenshot URLs for the execution step, if relevant.

                    - *(string) --*

                      - *(string) --*

                  - **statusReason** *(string) --*

                    The reason for current step status.

                  - **context** *(string) --*

                    The context for current step, will include build image if step is build.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_webhook(self, webhookId: str) -> ClientGetWebhookResponseTypeDef:
        """
        Retrieves webhook info that corresponds to a webhookId.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/GetWebhook>`_

        **Request Syntax**
        ::

          response = client.get_webhook(
              webhookId='string'
          )
        :type webhookId: string
        :param webhookId: **[REQUIRED]**

          Unique Id for a webhook.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'webhookArn': 'string',
                    'webhookId': 'string',
                    'webhookUrl': 'string',
                    'branchName': 'string',
                    'description': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'updateTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the get webhook request.

            - **webhook** *(dict) --*

              Webhook structure.

              - **webhookArn** *(string) --*

                ARN for the webhook.

              - **webhookId** *(string) --*

                Id of the webhook.

              - **webhookUrl** *(string) --*

                Url of the webhook.

              - **branchName** *(string) --*

                Name for a branch, part of an Amplify App.

              - **description** *(string) --*

                Description for a webhook.

              - **createTime** *(datetime) --*

                Create date / time for a webhook.

              - **updateTime** *(datetime) --*

                Update date / time for a webhook.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_apps(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListAppsResponseTypeDef:
        """
        Lists existing Amplify Apps.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListApps>`_

        **Request Syntax**
        ::

          response = client.list_apps(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          Pagination token. If non-null pagination token is returned in a result, then pass its value in
          another request to fetch more entries.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              Pagination token. Set to null to start listing Apps from start. If non-null pagination token
              is returned in a result, then pass its value in here to list more projects.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_artifacts(
        self,
        appId: str,
        branchName: str,
        jobId: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListArtifactsResponseTypeDef:
        """
        List artifacts with an app, a branch, a job and an artifact type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListArtifacts>`_

        **Request Syntax**
        ::

          response = client.list_artifacts(
              appId='string',
              branchName='string',
              jobId='string',
              nextToken='string',
              maxResults=123
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for a branch, part of an Amplify App.

        :type jobId: string
        :param jobId: **[REQUIRED]**

          Unique Id for an Job.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing artifacts from start. If non-null pagination token
          is returned in a result, then pass its value in here to list more artifacts.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'artifacts': [
                    {
                        'artifactFileName': 'string',
                        'artifactId': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the list artifacts request.

            - **artifacts** *(list) --*

              List of artifacts.

              - *(dict) --*

                Structure for artifact.

                - **artifactFileName** *(string) --*

                  File name for the artifact.

                - **artifactId** *(string) --*

                  Unique Id for a artifact.

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_branches(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListBranchesResponseTypeDef:
        """
        Lists branches for an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListBranches>`_

        **Request Syntax**
        ::

          response = client.list_branches(
              appId='string',
              nextToken='string',
              maxResults=123
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing branches from start. If a non-null pagination
          token is returned in a result, then pass its value in here to list more branches.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domain_associations(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListDomainAssociationsResponseTypeDef:
        """
        List domains with an app

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListDomainAssociations>`_

        **Request Syntax**
        ::

          response = client.list_domain_associations(
              appId='string',
              nextToken='string',
              maxResults=123
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing Apps from start. If non-null pagination token is
          returned in a result, then pass its value in here to list more projects.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListJobsResponseTypeDef:
        """
        List Jobs for a branch, part of an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListJobs>`_

        **Request Syntax**
        ::

          response = client.list_jobs(
              appId='string',
              branchName='string',
              nextToken='string',
              maxResults=123
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for a branch.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing steps from start. If a non-null pagination token
          is returned in a result, then pass its value in here to list more steps.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        List tags for resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          Resource arn used to list tags.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Response for list tags.

            - **tags** *(dict) --*

              Tags result for response.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_webhooks(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListWebhooksResponseTypeDef:
        """
        List webhooks with an app.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/ListWebhooks>`_

        **Request Syntax**
        ::

          response = client.list_webhooks(
              appId='string',
              nextToken='string',
              maxResults=123
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing webhooks from start. If non-null pagination token
          is returned in a result, then pass its value in here to list more webhooks.

        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhooks': [
                    {
                        'webhookArn': 'string',
                        'webhookId': 'string',
                        'webhookUrl': 'string',
                        'branchName': 'string',
                        'description': 'string',
                        'createTime': datetime(2015, 1, 1),
                        'updateTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the list webhooks request.

            - **webhooks** *(list) --*

              List of webhooks.

              - *(dict) --*

                Structure for webhook, which associates a webhook with an Amplify App.

                - **webhookArn** *(string) --*

                  ARN for the webhook.

                - **webhookId** *(string) --*

                  Id of the webhook.

                - **webhookUrl** *(string) --*

                  Url of the webhook.

                - **branchName** *(string) --*

                  Name for a branch, part of an Amplify App.

                - **description** *(string) --*

                  Description for a webhook.

                - **createTime** *(datetime) --*

                  Create date / time for a webhook.

                - **updateTime** *(datetime) --*

                  Update date / time for a webhook.

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_deployment(
        self, appId: str, branchName: str, jobId: str = None, sourceUrl: str = None
    ) -> ClientStartDeploymentResponseTypeDef:
        """
        Start a deployment for manual deploy apps. (Apps are not connected to repository)

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/StartDeployment>`_

        **Request Syntax**
        ::

          response = client.start_deployment(
              appId='string',
              branchName='string',
              jobId='string',
              sourceUrl='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type jobId: string
        :param jobId:

          The job id for this deployment, generated by create deployment request.

        :type sourceUrl: string
        :param sourceUrl:

          The sourceUrl for this deployment, used when calling start deployment without create deployment.
          SourceUrl can be any HTTP GET url that is public accessible and downloads a single zip.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'jobSummary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for start a deployment.

            - **jobSummary** *(dict) --*

              Summary for the Job.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_job(
        self,
        appId: str,
        branchName: str,
        jobType: str,
        jobId: str = None,
        jobReason: str = None,
        commitId: str = None,
        commitMessage: str = None,
        commitTime: datetime = None,
    ) -> ClientStartJobResponseTypeDef:
        """
        Starts a new job for a branch, part of an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/StartJob>`_

        **Request Syntax**
        ::

          response = client.start_job(
              appId='string',
              branchName='string',
              jobId='string',
              jobType='RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK',
              jobReason='string',
              commitId='string',
              commitMessage='string',
              commitTime=datetime(2015, 1, 1)
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type jobId: string
        :param jobId:

          Unique Id for an existing job. Required for "RETRY" JobType.

        :type jobType: string
        :param jobType: **[REQUIRED]**

          Type for the Job. Available JobTypes are: \\n "RELEASE": Start a new job with the latest change
          from the specified branch. Only available for apps that have connected to a repository. "RETRY":
          Retry an existing job. JobId is required for this type of job.

        :type jobReason: string
        :param jobReason:

          Descriptive reason for starting this job.

        :type commitId: string
        :param commitId:

          Commit Id from 3rd party repository provider for the Job.

        :type commitMessage: string
        :param commitMessage:

          Commit message from 3rd party repository provider for the Job.

        :type commitTime: datetime
        :param commitTime:

          Commit date / time for the Job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'jobSummary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for run job request.

            - **jobSummary** *(dict) --*

              Summary for the Job.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_job(
        self, appId: str, branchName: str, jobId: str
    ) -> ClientStopJobResponseTypeDef:
        """
        Stop a job that is in progress, for an Amplify branch, part of Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/StopJob>`_

        **Request Syntax**
        ::

          response = client.stop_job(
              appId='string',
              branchName='string',
              jobId='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch, for the Job.

        :type jobId: string
        :param jobId: **[REQUIRED]**

          Unique Id for the Job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'jobSummary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the stop job request.

            - **jobSummary** *(dict) --*

              Summary for the Job.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict:
        """
        Tag resource with tag key and value.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          Resource arn used to tag resource.

        :type tags: dict
        :param tags: **[REQUIRED]**

          Tags used to tag resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response for tag resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict:
        """
        Untag resource with resourceArn.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          Resource arn used to untag resource.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          Tag keys used to untag resource.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response for untag resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_app(
        self,
        appId: str,
        name: str = None,
        description: str = None,
        platform: str = None,
        iamServiceRoleArn: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[ClientUpdateAppcustomRulesTypeDef] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: ClientUpdateAppautoBranchCreationConfigTypeDef = None,
        repository: str = None,
        oauthToken: str = None,
        accessToken: str = None,
    ) -> ClientUpdateAppResponseTypeDef:
        """
        Updates an existing Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateApp>`_

        **Request Syntax**
        ::

          response = client.update_app(
              appId='string',
              name='string',
              description='string',
              platform='WEB',
              iamServiceRoleArn='string',
              environmentVariables={
                  'string': 'string'
              },
              enableBranchAutoBuild=True|False,
              enableBasicAuth=True|False,
              basicAuthCredentials='string',
              customRules=[
                  {
                      'source': 'string',
                      'target': 'string',
                      'status': 'string',
                      'condition': 'string'
                  },
              ],
              buildSpec='string',
              enableAutoBranchCreation=True|False,
              autoBranchCreationPatterns=[
                  'string',
              ],
              autoBranchCreationConfig={
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
              },
              repository='string',
              oauthToken='string',
              accessToken='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type name: string
        :param name:

          Name for an Amplify App.

        :type description: string
        :param description:

          Description for an Amplify App.

        :type platform: string
        :param platform:

          Platform for an Amplify App.

        :type iamServiceRoleArn: string
        :param iamServiceRoleArn:

          IAM service role for an Amplify App.

        :type environmentVariables: dict
        :param environmentVariables:

          Environment Variables for an Amplify App.

          - *(string) --*

            - *(string) --*

        :type enableBranchAutoBuild: boolean
        :param enableBranchAutoBuild:

          Enables branch auto-building for an Amplify App.

        :type enableBasicAuth: boolean
        :param enableBasicAuth:

          Enables Basic Authorization for an Amplify App.

        :type basicAuthCredentials: string
        :param basicAuthCredentials:

          Basic Authorization credentials for an Amplify App.

        :type customRules: list
        :param customRules:

          Custom redirect / rewrite rules for an Amplify App.

          - *(dict) --*

            Custom rewrite / redirect rule.

            - **source** *(string) --* **[REQUIRED]**

              The source pattern for a URL rewrite or redirect rule.

            - **target** *(string) --* **[REQUIRED]**

              The target pattern for a URL rewrite or redirect rule.

            - **status** *(string) --*

              The status code for a URL rewrite or redirect rule.

            - **condition** *(string) --*

              The condition for a URL rewrite or redirect rule, e.g. country code.

        :type buildSpec: string
        :param buildSpec:

          BuildSpec for an Amplify App.

        :type enableAutoBranchCreation: boolean
        :param enableAutoBranchCreation:

          Enables automated branch creation for the Amplify App.

        :type autoBranchCreationPatterns: list
        :param autoBranchCreationPatterns:

          Automated branch creation glob patterns for the Amplify App.

          - *(string) --*

        :type autoBranchCreationConfig: dict
        :param autoBranchCreationConfig:

          Automated branch creation branchConfig for the Amplify App.

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

        :type repository: string
        :param repository:

          Repository for an Amplify App

        :type oauthToken: string
        :param oauthToken:

          OAuth token for 3rd party source control system for an Amplify App, used to create webhook and
          read-only deploy key. OAuth token is not stored.

        :type accessToken: string
        :param accessToken:

          Personal Access token for 3rd party source control system for an Amplify App, used to create
          webhook and read-only deploy key. Token is not stored.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'app': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for an Amplify App update request.

            - **app** *(dict) --*

              App structure for the updated App.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        framework: str = None,
        stage: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> ClientUpdateBranchResponseTypeDef:
        """
        Updates a branch for an Amplify App.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateBranch>`_

        **Request Syntax**
        ::

          response = client.update_branch(
              appId='string',
              branchName='string',
              description='string',
              framework='string',
              stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
              enableNotification=True|False,
              enableAutoBuild=True|False,
              environmentVariables={
                  'string': 'string'
              },
              basicAuthCredentials='string',
              enableBasicAuth=True|False,
              buildSpec='string',
              ttl='string',
              displayName='string',
              enablePullRequestPreview=True|False,
              pullRequestEnvironmentName='string',
              backendEnvironmentArn='string'
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          Name for the branch.

        :type description: string
        :param description:

          Description for the branch.

        :type framework: string
        :param framework:

          Framework for the branch.

        :type stage: string
        :param stage:

          Stage for the branch.

        :type enableNotification: boolean
        :param enableNotification:

          Enables notifications for the branch.

        :type enableAutoBuild: boolean
        :param enableAutoBuild:

          Enables auto building for the branch.

        :type environmentVariables: dict
        :param environmentVariables:

          Environment Variables for the branch.

          - *(string) --*

            - *(string) --*

        :type basicAuthCredentials: string
        :param basicAuthCredentials:

          Basic Authorization credentials for the branch.

        :type enableBasicAuth: boolean
        :param enableBasicAuth:

          Enables Basic Auth for the branch.

        :type buildSpec: string
        :param buildSpec:

          BuildSpec for the branch.

        :type ttl: string
        :param ttl:

          The content TTL for the website in seconds.

        :type displayName: string
        :param displayName:

          Display name for a branch, will use as the default domain prefix.

        :type enablePullRequestPreview: boolean
        :param enablePullRequestPreview:

          Enables Pull Request Preview for this branch.

        :type pullRequestEnvironmentName: string
        :param pullRequestEnvironmentName:

          The Amplify Environment name for the pull request.

        :type backendEnvironmentArn: string
        :param backendEnvironmentArn:

          ARN for a Backend Environment, part of an Amplify App.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branch': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for update branch request.

            - **branch** *(dict) --*

              Branch structure for an Amplify App.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[ClientUpdateDomainAssociationsubDomainSettingsTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> ClientUpdateDomainAssociationResponseTypeDef:
        """
        Create a new DomainAssociation on an App

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateDomainAssociation>`_

        **Request Syntax**
        ::

          response = client.update_domain_association(
              appId='string',
              domainName='string',
              enableAutoSubDomain=True|False,
              subDomainSettings=[
                  {
                      'prefix': 'string',
                      'branchName': 'string'
                  },
              ]
          )
        :type appId: string
        :param appId: **[REQUIRED]**

          Unique Id for an Amplify App.

        :type domainName: string
        :param domainName: **[REQUIRED]**

          Name of the domain.

        :type enableAutoSubDomain: boolean
        :param enableAutoSubDomain:

          Enables automated creation of Subdomains for branches. (Currently not supported)

        :type subDomainSettings: list
        :param subDomainSettings: **[REQUIRED]**

          Setting structure for the Subdomain.

          - *(dict) --*

            Setting for the Subdomain.

            - **prefix** *(string) --* **[REQUIRED]**

              Prefix setting for the Subdomain.

            - **branchName** *(string) --* **[REQUIRED]**

              Branch name setting for the Subdomain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'domainAssociation': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the update Domain Association request.

            - **domainAssociation** *(dict) --*

              Domain Association structure.

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

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_webhook(
        self, webhookId: str, branchName: str = None, description: str = None
    ) -> ClientUpdateWebhookResponseTypeDef:
        """
        Update a webhook.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/UpdateWebhook>`_

        **Request Syntax**
        ::

          response = client.update_webhook(
              webhookId='string',
              branchName='string',
              description='string'
          )
        :type webhookId: string
        :param webhookId: **[REQUIRED]**

          Unique Id for a webhook.

        :type branchName: string
        :param branchName:

          Name for a branch, part of an Amplify App.

        :type description: string
        :param description:

          Description for a webhook.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'webhookArn': 'string',
                    'webhookId': 'string',
                    'webhookUrl': 'string',
                    'branchName': 'string',
                    'description': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'updateTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure for the update webhook request.

            - **webhook** *(dict) --*

              Webhook structure.

              - **webhookArn** *(string) --*

                ARN for the webhook.

              - **webhookId** *(string) --*

                Id of the webhook.

              - **webhookUrl** *(string) --*

                Url of the webhook.

              - **branchName** *(string) --*

                Name for a branch, part of an Amplify App.

              - **description** *(string) --*

                Description for a webhook.

              - **createTime** *(datetime) --*

                Create date / time for a webhook.

              - **updateTime** *(datetime) --*

                Update date / time for a webhook.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> paginator_scope.ListAppsPaginator:
        """
        Get Paginator for `list_apps` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_branches"]
    ) -> paginator_scope.ListBranchesPaginator:
        """
        Get Paginator for `list_branches` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_domain_associations"]
    ) -> paginator_scope.ListDomainAssociationsPaginator:
        """
        Get Paginator for `list_domain_associations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        Get Paginator for `list_jobs` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    DependentServiceFailureException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
