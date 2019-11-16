"Main interface for amplify type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAppResponseappautoBranchCreationConfigTypeDef",
    "ClientCreateAppResponseappcustomRulesTypeDef",
    "ClientCreateAppResponseappproductionBranchTypeDef",
    "ClientCreateAppResponseappTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppautoBranchCreationConfigTypeDef",
    "ClientCreateAppcustomRulesTypeDef",
    "ClientCreateBranchResponsebranchTypeDef",
    "ClientCreateBranchResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationTypeDef",
    "ClientCreateDomainAssociationResponseTypeDef",
    "ClientCreateDomainAssociationsubDomainSettingsTypeDef",
    "ClientCreateWebhookResponsewebhookTypeDef",
    "ClientCreateWebhookResponseTypeDef",
    "ClientDeleteAppResponseappautoBranchCreationConfigTypeDef",
    "ClientDeleteAppResponseappcustomRulesTypeDef",
    "ClientDeleteAppResponseappproductionBranchTypeDef",
    "ClientDeleteAppResponseappTypeDef",
    "ClientDeleteAppResponseTypeDef",
    "ClientDeleteBranchResponsebranchTypeDef",
    "ClientDeleteBranchResponseTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationTypeDef",
    "ClientDeleteDomainAssociationResponseTypeDef",
    "ClientDeleteJobResponsejobSummaryTypeDef",
    "ClientDeleteJobResponseTypeDef",
    "ClientDeleteWebhookResponsewebhookTypeDef",
    "ClientDeleteWebhookResponseTypeDef",
    "ClientGenerateAccessLogsResponseTypeDef",
    "ClientGetAppResponseappautoBranchCreationConfigTypeDef",
    "ClientGetAppResponseappcustomRulesTypeDef",
    "ClientGetAppResponseappproductionBranchTypeDef",
    "ClientGetAppResponseappTypeDef",
    "ClientGetAppResponseTypeDef",
    "ClientGetArtifactUrlResponseTypeDef",
    "ClientGetBranchResponsebranchTypeDef",
    "ClientGetBranchResponseTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationTypeDef",
    "ClientGetDomainAssociationResponseTypeDef",
    "ClientGetJobResponsejobstepsTypeDef",
    "ClientGetJobResponsejobsummaryTypeDef",
    "ClientGetJobResponsejobTypeDef",
    "ClientGetJobResponseTypeDef",
    "ClientGetWebhookResponsewebhookTypeDef",
    "ClientGetWebhookResponseTypeDef",
    "ClientListAppsResponseappsautoBranchCreationConfigTypeDef",
    "ClientListAppsResponseappscustomRulesTypeDef",
    "ClientListAppsResponseappsproductionBranchTypeDef",
    "ClientListAppsResponseappsTypeDef",
    "ClientListAppsResponseTypeDef",
    "ClientListArtifactsResponseartifactsTypeDef",
    "ClientListArtifactsResponseTypeDef",
    "ClientListBranchesResponsebranchesTypeDef",
    "ClientListBranchesResponseTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationsTypeDef",
    "ClientListDomainAssociationsResponseTypeDef",
    "ClientListJobsResponsejobSummariesTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebhooksResponsewebhooksTypeDef",
    "ClientListWebhooksResponseTypeDef",
    "ClientStartDeploymentResponsejobSummaryTypeDef",
    "ClientStartDeploymentResponseTypeDef",
    "ClientStartJobResponsejobSummaryTypeDef",
    "ClientStartJobResponseTypeDef",
    "ClientStopJobResponsejobSummaryTypeDef",
    "ClientStopJobResponseTypeDef",
    "ClientUpdateAppResponseappautoBranchCreationConfigTypeDef",
    "ClientUpdateAppResponseappcustomRulesTypeDef",
    "ClientUpdateAppResponseappproductionBranchTypeDef",
    "ClientUpdateAppResponseappTypeDef",
    "ClientUpdateAppResponseTypeDef",
    "ClientUpdateAppautoBranchCreationConfigTypeDef",
    "ClientUpdateAppcustomRulesTypeDef",
    "ClientUpdateBranchResponsebranchTypeDef",
    "ClientUpdateBranchResponseTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationTypeDef",
    "ClientUpdateDomainAssociationResponseTypeDef",
    "ClientUpdateDomainAssociationsubDomainSettingsTypeDef",
    "ClientUpdateWebhookResponsewebhookTypeDef",
    "ClientUpdateWebhookResponseTypeDef",
    "ListAppsPaginatePaginationConfigTypeDef",
    "ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef",
    "ListAppsPaginateResponseappscustomRulesTypeDef",
    "ListAppsPaginateResponseappsproductionBranchTypeDef",
    "ListAppsPaginateResponseappsTypeDef",
    "ListAppsPaginateResponseTypeDef",
    "ListBranchesPaginatePaginationConfigTypeDef",
    "ListBranchesPaginateResponsebranchesTypeDef",
    "ListBranchesPaginateResponseTypeDef",
    "ListDomainAssociationsPaginatePaginationConfigTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef",
    "ListDomainAssociationsPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobSummariesTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientCreateAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientCreateAppResponseappautoBranchCreationConfigTypeDef(
    _ClientCreateAppResponseappautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientCreateAppResponseapp` `autoBranchCreationConfig`

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


_ClientCreateAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientCreateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientCreateAppResponseappcustomRulesTypeDef(
    _ClientCreateAppResponseappcustomRulesTypeDef
):
    """
    Type definition for `ClientCreateAppResponseapp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientCreateAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientCreateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientCreateAppResponseappproductionBranchTypeDef(
    _ClientCreateAppResponseappproductionBranchTypeDef
):
    """
    Type definition for `ClientCreateAppResponseapp` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ClientCreateAppResponseappTypeDef = TypedDict(
    "_ClientCreateAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientCreateAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientCreateAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientCreateAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ClientCreateAppResponseappTypeDef(_ClientCreateAppResponseappTypeDef):
    """
    Type definition for `ClientCreateAppResponse` `app`

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


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef",
    {"app": ClientCreateAppResponseappTypeDef},
    total=False,
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    Type definition for `ClientCreateApp` `Response`

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


_ClientCreateAppautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientCreateAppautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientCreateAppautoBranchCreationConfigTypeDef(
    _ClientCreateAppautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientCreateApp` `autoBranchCreationConfig`

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


_RequiredClientCreateAppcustomRulesTypeDef = TypedDict(
    "_RequiredClientCreateAppcustomRulesTypeDef", {"source": str, "target": str}
)
_OptionalClientCreateAppcustomRulesTypeDef = TypedDict(
    "_OptionalClientCreateAppcustomRulesTypeDef",
    {"status": str, "condition": str},
    total=False,
)


class ClientCreateAppcustomRulesTypeDef(
    _RequiredClientCreateAppcustomRulesTypeDef,
    _OptionalClientCreateAppcustomRulesTypeDef,
):
    """
    Type definition for `ClientCreateApp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --* **[REQUIRED]**

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --* **[REQUIRED]**

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientCreateBranchResponsebranchTypeDef = TypedDict(
    "_ClientCreateBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ClientCreateBranchResponsebranchTypeDef(_ClientCreateBranchResponsebranchTypeDef):
    """
    Type definition for `ClientCreateBranchResponse` `branch`

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


_ClientCreateBranchResponseTypeDef = TypedDict(
    "_ClientCreateBranchResponseTypeDef",
    {"branch": ClientCreateBranchResponsebranchTypeDef},
    total=False,
)


class ClientCreateBranchResponseTypeDef(_ClientCreateBranchResponseTypeDef):
    """
    Type definition for `ClientCreateBranch` `Response`

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


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {"jobId": str, "fileUploadUrls": Dict[str, str], "zipUploadUrl": str},
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

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


_ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ClientCreateDomainAssociationResponsedomainAssociationsubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    """
    Type definition for `ClientCreateDomainAssociationResponsedomainAssociation` `subDomains`

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


_ClientCreateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDomainAssociationResponsedomainAssociationTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationTypeDef
):
    """
    Type definition for `ClientCreateDomainAssociationResponse` `domainAssociation`

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


_ClientCreateDomainAssociationResponseTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponseTypeDef",
    {
        "domainAssociation": ClientCreateDomainAssociationResponsedomainAssociationTypeDef
    },
    total=False,
)


class ClientCreateDomainAssociationResponseTypeDef(
    _ClientCreateDomainAssociationResponseTypeDef
):
    """
    Type definition for `ClientCreateDomainAssociation` `Response`

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


_ClientCreateDomainAssociationsubDomainSettingsTypeDef = TypedDict(
    "_ClientCreateDomainAssociationsubDomainSettingsTypeDef",
    {"prefix": str, "branchName": str},
)


class ClientCreateDomainAssociationsubDomainSettingsTypeDef(
    _ClientCreateDomainAssociationsubDomainSettingsTypeDef
):
    """
    Type definition for `ClientCreateDomainAssociation` `subDomainSettings`

    Setting for the Subdomain.

    - **prefix** *(string) --* **[REQUIRED]**

      Prefix setting for the Subdomain.

    - **branchName** *(string) --* **[REQUIRED]**

      Branch name setting for the Subdomain.
    """


_ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)


class ClientCreateWebhookResponsewebhookTypeDef(
    _ClientCreateWebhookResponsewebhookTypeDef
):
    """
    Type definition for `ClientCreateWebhookResponse` `webhook`

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


_ClientCreateWebhookResponseTypeDef = TypedDict(
    "_ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientCreateWebhookResponseTypeDef(_ClientCreateWebhookResponseTypeDef):
    """
    Type definition for `ClientCreateWebhook` `Response`

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


_ClientDeleteAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientDeleteAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientDeleteAppResponseappautoBranchCreationConfigTypeDef(
    _ClientDeleteAppResponseappautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientDeleteAppResponseapp` `autoBranchCreationConfig`

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


_ClientDeleteAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientDeleteAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientDeleteAppResponseappcustomRulesTypeDef(
    _ClientDeleteAppResponseappcustomRulesTypeDef
):
    """
    Type definition for `ClientDeleteAppResponseapp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientDeleteAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientDeleteAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientDeleteAppResponseappproductionBranchTypeDef(
    _ClientDeleteAppResponseappproductionBranchTypeDef
):
    """
    Type definition for `ClientDeleteAppResponseapp` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ClientDeleteAppResponseappTypeDef = TypedDict(
    "_ClientDeleteAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientDeleteAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientDeleteAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientDeleteAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ClientDeleteAppResponseappTypeDef(_ClientDeleteAppResponseappTypeDef):
    """
    Type definition for `ClientDeleteAppResponse` `app`

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


_ClientDeleteAppResponseTypeDef = TypedDict(
    "_ClientDeleteAppResponseTypeDef",
    {"app": ClientDeleteAppResponseappTypeDef},
    total=False,
)


class ClientDeleteAppResponseTypeDef(_ClientDeleteAppResponseTypeDef):
    """
    Type definition for `ClientDeleteApp` `Response`

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


_ClientDeleteBranchResponsebranchTypeDef = TypedDict(
    "_ClientDeleteBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ClientDeleteBranchResponsebranchTypeDef(_ClientDeleteBranchResponsebranchTypeDef):
    """
    Type definition for `ClientDeleteBranchResponse` `branch`

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


_ClientDeleteBranchResponseTypeDef = TypedDict(
    "_ClientDeleteBranchResponseTypeDef",
    {"branch": ClientDeleteBranchResponsebranchTypeDef},
    total=False,
)


class ClientDeleteBranchResponseTypeDef(_ClientDeleteBranchResponseTypeDef):
    """
    Type definition for `ClientDeleteBranch` `Response`

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


_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ClientDeleteDomainAssociationResponsedomainAssociationsubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    """
    Type definition for `ClientDeleteDomainAssociationResponsedomainAssociation` `subDomains`

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


_ClientDeleteDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteDomainAssociationResponsedomainAssociationTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationTypeDef
):
    """
    Type definition for `ClientDeleteDomainAssociationResponse` `domainAssociation`

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


_ClientDeleteDomainAssociationResponseTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponseTypeDef",
    {
        "domainAssociation": ClientDeleteDomainAssociationResponsedomainAssociationTypeDef
    },
    total=False,
)


class ClientDeleteDomainAssociationResponseTypeDef(
    _ClientDeleteDomainAssociationResponseTypeDef
):
    """
    Type definition for `ClientDeleteDomainAssociation` `Response`

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


_ClientDeleteJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientDeleteJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientDeleteJobResponsejobSummaryTypeDef(
    _ClientDeleteJobResponsejobSummaryTypeDef
):
    """
    Type definition for `ClientDeleteJobResponse` `jobSummary`

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


_ClientDeleteJobResponseTypeDef = TypedDict(
    "_ClientDeleteJobResponseTypeDef",
    {"jobSummary": ClientDeleteJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientDeleteJobResponseTypeDef(_ClientDeleteJobResponseTypeDef):
    """
    Type definition for `ClientDeleteJob` `Response`

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


_ClientDeleteWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientDeleteWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)


class ClientDeleteWebhookResponsewebhookTypeDef(
    _ClientDeleteWebhookResponsewebhookTypeDef
):
    """
    Type definition for `ClientDeleteWebhookResponse` `webhook`

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


_ClientDeleteWebhookResponseTypeDef = TypedDict(
    "_ClientDeleteWebhookResponseTypeDef",
    {"webhook": ClientDeleteWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientDeleteWebhookResponseTypeDef(_ClientDeleteWebhookResponseTypeDef):
    """
    Type definition for `ClientDeleteWebhook` `Response`

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


_ClientGenerateAccessLogsResponseTypeDef = TypedDict(
    "_ClientGenerateAccessLogsResponseTypeDef", {"logUrl": str}, total=False
)


class ClientGenerateAccessLogsResponseTypeDef(_ClientGenerateAccessLogsResponseTypeDef):
    """
    Type definition for `ClientGenerateAccessLogs` `Response`

    Result structure for the generate access logs request.

    - **logUrl** *(string) --*

      Pre-signed URL for the requested access logs.
    """


_ClientGetAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientGetAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientGetAppResponseappautoBranchCreationConfigTypeDef(
    _ClientGetAppResponseappautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientGetAppResponseapp` `autoBranchCreationConfig`

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


_ClientGetAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientGetAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientGetAppResponseappcustomRulesTypeDef(
    _ClientGetAppResponseappcustomRulesTypeDef
):
    """
    Type definition for `ClientGetAppResponseapp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientGetAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientGetAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientGetAppResponseappproductionBranchTypeDef(
    _ClientGetAppResponseappproductionBranchTypeDef
):
    """
    Type definition for `ClientGetAppResponseapp` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ClientGetAppResponseappTypeDef = TypedDict(
    "_ClientGetAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientGetAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientGetAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientGetAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ClientGetAppResponseappTypeDef(_ClientGetAppResponseappTypeDef):
    """
    Type definition for `ClientGetAppResponse` `app`

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


_ClientGetAppResponseTypeDef = TypedDict(
    "_ClientGetAppResponseTypeDef", {"app": ClientGetAppResponseappTypeDef}, total=False
)


class ClientGetAppResponseTypeDef(_ClientGetAppResponseTypeDef):
    """
    Type definition for `ClientGetApp` `Response`

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


_ClientGetArtifactUrlResponseTypeDef = TypedDict(
    "_ClientGetArtifactUrlResponseTypeDef",
    {"artifactId": str, "artifactUrl": str},
    total=False,
)


class ClientGetArtifactUrlResponseTypeDef(_ClientGetArtifactUrlResponseTypeDef):
    """
    Type definition for `ClientGetArtifactUrl` `Response`

    Result structure for the get artifact request.

    - **artifactId** *(string) --*

      Unique Id for a artifact.

    - **artifactUrl** *(string) --*

      Presigned url for the artifact.
    """


_ClientGetBranchResponsebranchTypeDef = TypedDict(
    "_ClientGetBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ClientGetBranchResponsebranchTypeDef(_ClientGetBranchResponsebranchTypeDef):
    """
    Type definition for `ClientGetBranchResponse` `branch`

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


_ClientGetBranchResponseTypeDef = TypedDict(
    "_ClientGetBranchResponseTypeDef",
    {"branch": ClientGetBranchResponsebranchTypeDef},
    total=False,
)


class ClientGetBranchResponseTypeDef(_ClientGetBranchResponseTypeDef):
    """
    Type definition for `ClientGetBranch` `Response`

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


_ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ClientGetDomainAssociationResponsedomainAssociationsubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    """
    Type definition for `ClientGetDomainAssociationResponsedomainAssociation` `subDomains`

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


_ClientGetDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainAssociationResponsedomainAssociationTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationTypeDef
):
    """
    Type definition for `ClientGetDomainAssociationResponse` `domainAssociation`

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


_ClientGetDomainAssociationResponseTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientGetDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)


class ClientGetDomainAssociationResponseTypeDef(
    _ClientGetDomainAssociationResponseTypeDef
):
    """
    Type definition for `ClientGetDomainAssociation` `Response`

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


_ClientGetJobResponsejobstepsTypeDef = TypedDict(
    "_ClientGetJobResponsejobstepsTypeDef",
    {
        "stepName": str,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "logUrl": str,
        "artifactsUrl": str,
        "testArtifactsUrl": str,
        "testConfigUrl": str,
        "screenshots": Dict[str, str],
        "statusReason": str,
        "context": str,
    },
    total=False,
)


class ClientGetJobResponsejobstepsTypeDef(_ClientGetJobResponsejobstepsTypeDef):
    """
    Type definition for `ClientGetJobResponsejob` `steps`

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


_ClientGetJobResponsejobsummaryTypeDef = TypedDict(
    "_ClientGetJobResponsejobsummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientGetJobResponsejobsummaryTypeDef(_ClientGetJobResponsejobsummaryTypeDef):
    """
    Type definition for `ClientGetJobResponsejob` `summary`

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
    """


_ClientGetJobResponsejobTypeDef = TypedDict(
    "_ClientGetJobResponsejobTypeDef",
    {
        "summary": ClientGetJobResponsejobsummaryTypeDef,
        "steps": List[ClientGetJobResponsejobstepsTypeDef],
    },
    total=False,
)


class ClientGetJobResponsejobTypeDef(_ClientGetJobResponsejobTypeDef):
    """
    Type definition for `ClientGetJobResponse` `job`

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


_ClientGetJobResponseTypeDef = TypedDict(
    "_ClientGetJobResponseTypeDef", {"job": ClientGetJobResponsejobTypeDef}, total=False
)


class ClientGetJobResponseTypeDef(_ClientGetJobResponseTypeDef):
    """
    Type definition for `ClientGetJob` `Response`

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


_ClientGetWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientGetWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)


class ClientGetWebhookResponsewebhookTypeDef(_ClientGetWebhookResponsewebhookTypeDef):
    """
    Type definition for `ClientGetWebhookResponse` `webhook`

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


_ClientGetWebhookResponseTypeDef = TypedDict(
    "_ClientGetWebhookResponseTypeDef",
    {"webhook": ClientGetWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientGetWebhookResponseTypeDef(_ClientGetWebhookResponseTypeDef):
    """
    Type definition for `ClientGetWebhook` `Response`

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


_ClientListAppsResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientListAppsResponseappsautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientListAppsResponseappsautoBranchCreationConfigTypeDef(
    _ClientListAppsResponseappsautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientListAppsResponseapps` `autoBranchCreationConfig`

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


_ClientListAppsResponseappscustomRulesTypeDef = TypedDict(
    "_ClientListAppsResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientListAppsResponseappscustomRulesTypeDef(
    _ClientListAppsResponseappscustomRulesTypeDef
):
    """
    Type definition for `ClientListAppsResponseapps` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientListAppsResponseappsproductionBranchTypeDef = TypedDict(
    "_ClientListAppsResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientListAppsResponseappsproductionBranchTypeDef(
    _ClientListAppsResponseappsproductionBranchTypeDef
):
    """
    Type definition for `ClientListAppsResponseapps` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ClientListAppsResponseappsTypeDef = TypedDict(
    "_ClientListAppsResponseappsTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientListAppsResponseappscustomRulesTypeDef],
        "productionBranch": ClientListAppsResponseappsproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientListAppsResponseappsautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ClientListAppsResponseappsTypeDef(_ClientListAppsResponseappsTypeDef):
    """
    Type definition for `ClientListAppsResponse` `apps`

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


_ClientListAppsResponseTypeDef = TypedDict(
    "_ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAppsResponseTypeDef(_ClientListAppsResponseTypeDef):
    """
    Type definition for `ClientListApps` `Response`

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


_ClientListArtifactsResponseartifactsTypeDef = TypedDict(
    "_ClientListArtifactsResponseartifactsTypeDef",
    {"artifactFileName": str, "artifactId": str},
    total=False,
)


class ClientListArtifactsResponseartifactsTypeDef(
    _ClientListArtifactsResponseartifactsTypeDef
):
    """
    Type definition for `ClientListArtifactsResponse` `artifacts`

    Structure for artifact.

    - **artifactFileName** *(string) --*

      File name for the artifact.

    - **artifactId** *(string) --*

      Unique Id for a artifact.
    """


_ClientListArtifactsResponseTypeDef = TypedDict(
    "_ClientListArtifactsResponseTypeDef",
    {"artifacts": List[ClientListArtifactsResponseartifactsTypeDef], "nextToken": str},
    total=False,
)


class ClientListArtifactsResponseTypeDef(_ClientListArtifactsResponseTypeDef):
    """
    Type definition for `ClientListArtifacts` `Response`

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


_ClientListBranchesResponsebranchesTypeDef = TypedDict(
    "_ClientListBranchesResponsebranchesTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ClientListBranchesResponsebranchesTypeDef(
    _ClientListBranchesResponsebranchesTypeDef
):
    """
    Type definition for `ClientListBranchesResponse` `branches`

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


_ClientListBranchesResponseTypeDef = TypedDict(
    "_ClientListBranchesResponseTypeDef",
    {"branches": List[ClientListBranchesResponsebranchesTypeDef], "nextToken": str},
    total=False,
)


class ClientListBranchesResponseTypeDef(_ClientListBranchesResponseTypeDef):
    """
    Type definition for `ClientListBranches` `Response`

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


_ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ClientListDomainAssociationsResponsedomainAssociationssubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef
):
    """
    Type definition for `ClientListDomainAssociationsResponsedomainAssociations` `subDomains`

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


_ClientListDomainAssociationsResponsedomainAssociationsTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationsTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef
        ],
    },
    total=False,
)


class ClientListDomainAssociationsResponsedomainAssociationsTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationsTypeDef
):
    """
    Type definition for `ClientListDomainAssociationsResponse` `domainAssociations`

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


_ClientListDomainAssociationsResponseTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponseTypeDef",
    {
        "domainAssociations": List[
            ClientListDomainAssociationsResponsedomainAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDomainAssociationsResponseTypeDef(
    _ClientListDomainAssociationsResponseTypeDef
):
    """
    Type definition for `ClientListDomainAssociations` `Response`

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


_ClientListJobsResponsejobSummariesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummariesTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientListJobsResponsejobSummariesTypeDef(
    _ClientListJobsResponsejobSummariesTypeDef
):
    """
    Type definition for `ClientListJobsResponse` `jobSummaries`

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


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobSummaries": List[ClientListJobsResponsejobSummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

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


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    Response for list tags.

    - **tags** *(dict) --*

      Tags result for response.

      - *(string) --*

        - *(string) --*
    """


_ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)


class ClientListWebhooksResponsewebhooksTypeDef(
    _ClientListWebhooksResponsewebhooksTypeDef
):
    """
    Type definition for `ClientListWebhooksResponse` `webhooks`

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
    """


_ClientListWebhooksResponseTypeDef = TypedDict(
    "_ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "nextToken": str},
    total=False,
)


class ClientListWebhooksResponseTypeDef(_ClientListWebhooksResponseTypeDef):
    """
    Type definition for `ClientListWebhooks` `Response`

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


_ClientStartDeploymentResponsejobSummaryTypeDef = TypedDict(
    "_ClientStartDeploymentResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientStartDeploymentResponsejobSummaryTypeDef(
    _ClientStartDeploymentResponsejobSummaryTypeDef
):
    """
    Type definition for `ClientStartDeploymentResponse` `jobSummary`

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


_ClientStartDeploymentResponseTypeDef = TypedDict(
    "_ClientStartDeploymentResponseTypeDef",
    {"jobSummary": ClientStartDeploymentResponsejobSummaryTypeDef},
    total=False,
)


class ClientStartDeploymentResponseTypeDef(_ClientStartDeploymentResponseTypeDef):
    """
    Type definition for `ClientStartDeployment` `Response`

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


_ClientStartJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientStartJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientStartJobResponsejobSummaryTypeDef(_ClientStartJobResponsejobSummaryTypeDef):
    """
    Type definition for `ClientStartJobResponse` `jobSummary`

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


_ClientStartJobResponseTypeDef = TypedDict(
    "_ClientStartJobResponseTypeDef",
    {"jobSummary": ClientStartJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientStartJobResponseTypeDef(_ClientStartJobResponseTypeDef):
    """
    Type definition for `ClientStartJob` `Response`

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


_ClientStopJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientStopJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ClientStopJobResponsejobSummaryTypeDef(_ClientStopJobResponsejobSummaryTypeDef):
    """
    Type definition for `ClientStopJobResponse` `jobSummary`

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


_ClientStopJobResponseTypeDef = TypedDict(
    "_ClientStopJobResponseTypeDef",
    {"jobSummary": ClientStopJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientStopJobResponseTypeDef(_ClientStopJobResponseTypeDef):
    """
    Type definition for `ClientStopJob` `Response`

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


_ClientUpdateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientUpdateAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientUpdateAppResponseappautoBranchCreationConfigTypeDef(
    _ClientUpdateAppResponseappautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseapp` `autoBranchCreationConfig`

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


_ClientUpdateAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientUpdateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientUpdateAppResponseappcustomRulesTypeDef(
    _ClientUpdateAppResponseappcustomRulesTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseapp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientUpdateAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientUpdateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientUpdateAppResponseappproductionBranchTypeDef(
    _ClientUpdateAppResponseappproductionBranchTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseapp` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ClientUpdateAppResponseappTypeDef = TypedDict(
    "_ClientUpdateAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientUpdateAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientUpdateAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientUpdateAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ClientUpdateAppResponseappTypeDef(_ClientUpdateAppResponseappTypeDef):
    """
    Type definition for `ClientUpdateAppResponse` `app`

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


_ClientUpdateAppResponseTypeDef = TypedDict(
    "_ClientUpdateAppResponseTypeDef",
    {"app": ClientUpdateAppResponseappTypeDef},
    total=False,
)


class ClientUpdateAppResponseTypeDef(_ClientUpdateAppResponseTypeDef):
    """
    Type definition for `ClientUpdateApp` `Response`

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


_ClientUpdateAppautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientUpdateAppautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ClientUpdateAppautoBranchCreationConfigTypeDef(
    _ClientUpdateAppautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ClientUpdateApp` `autoBranchCreationConfig`

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
    """


_RequiredClientUpdateAppcustomRulesTypeDef = TypedDict(
    "_RequiredClientUpdateAppcustomRulesTypeDef", {"source": str, "target": str}
)
_OptionalClientUpdateAppcustomRulesTypeDef = TypedDict(
    "_OptionalClientUpdateAppcustomRulesTypeDef",
    {"status": str, "condition": str},
    total=False,
)


class ClientUpdateAppcustomRulesTypeDef(
    _RequiredClientUpdateAppcustomRulesTypeDef,
    _OptionalClientUpdateAppcustomRulesTypeDef,
):
    """
    Type definition for `ClientUpdateApp` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --* **[REQUIRED]**

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --* **[REQUIRED]**

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ClientUpdateBranchResponsebranchTypeDef = TypedDict(
    "_ClientUpdateBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ClientUpdateBranchResponsebranchTypeDef(_ClientUpdateBranchResponsebranchTypeDef):
    """
    Type definition for `ClientUpdateBranchResponse` `branch`

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


_ClientUpdateBranchResponseTypeDef = TypedDict(
    "_ClientUpdateBranchResponseTypeDef",
    {"branch": ClientUpdateBranchResponsebranchTypeDef},
    total=False,
)


class ClientUpdateBranchResponseTypeDef(_ClientUpdateBranchResponseTypeDef):
    """
    Type definition for `ClientUpdateBranch` `Response`

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


_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ClientUpdateDomainAssociationResponsedomainAssociationsubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    """
    Type definition for `ClientUpdateDomainAssociationResponsedomainAssociation` `subDomains`

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


_ClientUpdateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDomainAssociationResponsedomainAssociationTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationTypeDef
):
    """
    Type definition for `ClientUpdateDomainAssociationResponse` `domainAssociation`

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


_ClientUpdateDomainAssociationResponseTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponseTypeDef",
    {
        "domainAssociation": ClientUpdateDomainAssociationResponsedomainAssociationTypeDef
    },
    total=False,
)


class ClientUpdateDomainAssociationResponseTypeDef(
    _ClientUpdateDomainAssociationResponseTypeDef
):
    """
    Type definition for `ClientUpdateDomainAssociation` `Response`

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


_ClientUpdateDomainAssociationsubDomainSettingsTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationsubDomainSettingsTypeDef",
    {"prefix": str, "branchName": str},
)


class ClientUpdateDomainAssociationsubDomainSettingsTypeDef(
    _ClientUpdateDomainAssociationsubDomainSettingsTypeDef
):
    """
    Type definition for `ClientUpdateDomainAssociation` `subDomainSettings`

    Setting for the Subdomain.

    - **prefix** *(string) --* **[REQUIRED]**

      Prefix setting for the Subdomain.

    - **branchName** *(string) --* **[REQUIRED]**

      Branch name setting for the Subdomain.
    """


_ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)


class ClientUpdateWebhookResponsewebhookTypeDef(
    _ClientUpdateWebhookResponsewebhookTypeDef
):
    """
    Type definition for `ClientUpdateWebhookResponse` `webhook`

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


_ClientUpdateWebhookResponseTypeDef = TypedDict(
    "_ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientUpdateWebhookResponseTypeDef(_ClientUpdateWebhookResponseTypeDef):
    """
    Type definition for `ClientUpdateWebhook` `Response`

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


_ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppsPaginatePaginationConfigTypeDef(_ListAppsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListAppsPaginate` `PaginationConfig`

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


_ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef",
    {
        "stage": str,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)


class ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef(
    _ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef
):
    """
    Type definition for `ListAppsPaginateResponseapps` `autoBranchCreationConfig`

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


_ListAppsPaginateResponseappscustomRulesTypeDef = TypedDict(
    "_ListAppsPaginateResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ListAppsPaginateResponseappscustomRulesTypeDef(
    _ListAppsPaginateResponseappscustomRulesTypeDef
):
    """
    Type definition for `ListAppsPaginateResponseapps` `customRules`

    Custom rewrite / redirect rule.

    - **source** *(string) --*

      The source pattern for a URL rewrite or redirect rule.

    - **target** *(string) --*

      The target pattern for a URL rewrite or redirect rule.

    - **status** *(string) --*

      The status code for a URL rewrite or redirect rule.

    - **condition** *(string) --*

      The condition for a URL rewrite or redirect rule, e.g. country code.
    """


_ListAppsPaginateResponseappsproductionBranchTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ListAppsPaginateResponseappsproductionBranchTypeDef(
    _ListAppsPaginateResponseappsproductionBranchTypeDef
):
    """
    Type definition for `ListAppsPaginateResponseapps` `productionBranch`

    Structure with Production Branch information.

    - **lastDeployTime** *(datetime) --*

      Last Deploy Time of Production Branch.

    - **status** *(string) --*

      Status of Production Branch.

    - **thumbnailUrl** *(string) --*

      Thumbnail URL for Production Branch.

    - **branchName** *(string) --*

      Branch Name for Production Branch.
    """


_ListAppsPaginateResponseappsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ListAppsPaginateResponseappscustomRulesTypeDef],
        "productionBranch": ListAppsPaginateResponseappsproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef,
    },
    total=False,
)


class ListAppsPaginateResponseappsTypeDef(_ListAppsPaginateResponseappsTypeDef):
    """
    Type definition for `ListAppsPaginateResponse` `apps`

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


_ListAppsPaginateResponseTypeDef = TypedDict(
    "_ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)


class ListAppsPaginateResponseTypeDef(_ListAppsPaginateResponseTypeDef):
    """
    Type definition for `ListAppsPaginate` `Response`

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


_ListBranchesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBranchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBranchesPaginatePaginationConfigTypeDef(
    _ListBranchesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBranchesPaginate` `PaginationConfig`

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


_ListBranchesPaginateResponsebranchesTypeDef = TypedDict(
    "_ListBranchesPaginateResponsebranchesTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": str,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class ListBranchesPaginateResponsebranchesTypeDef(
    _ListBranchesPaginateResponsebranchesTypeDef
):
    """
    Type definition for `ListBranchesPaginateResponse` `branches`

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


_ListBranchesPaginateResponseTypeDef = TypedDict(
    "_ListBranchesPaginateResponseTypeDef",
    {"branches": List[ListBranchesPaginateResponsebranchesTypeDef], "NextToken": str},
    total=False,
)


class ListBranchesPaginateResponseTypeDef(_ListBranchesPaginateResponseTypeDef):
    """
    Type definition for `ListBranchesPaginate` `Response`

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


_ListDomainAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainAssociationsPaginatePaginationConfigTypeDef(
    _ListDomainAssociationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDomainAssociationsPaginate` `PaginationConfig`

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


_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef
):
    """
    Type definition for `ListDomainAssociationsPaginateResponsedomainAssociationssubDomains` `subDomainSetting`

    Setting structure for the Subdomain.

    - **prefix** *(string) --*

      Prefix setting for the Subdomain.

    - **branchName** *(string) --*

      Branch name setting for the Subdomain.
    """


_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef
):
    """
    Type definition for `ListDomainAssociationsPaginateResponsedomainAssociations` `subDomains`

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


_ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": str,
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef
        ],
    },
    total=False,
)


class ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef
):
    """
    Type definition for `ListDomainAssociationsPaginateResponse` `domainAssociations`

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


_ListDomainAssociationsPaginateResponseTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponseTypeDef",
    {
        "domainAssociations": List[
            ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDomainAssociationsPaginateResponseTypeDef(
    _ListDomainAssociationsPaginateResponseTypeDef
):
    """
    Type definition for `ListDomainAssociationsPaginate` `Response`

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


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListJobsPaginate` `PaginationConfig`

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


_ListJobsPaginateResponsejobSummariesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummariesTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": str,
        "endTime": datetime,
        "jobType": str,
    },
    total=False,
)


class ListJobsPaginateResponsejobSummariesTypeDef(
    _ListJobsPaginateResponsejobSummariesTypeDef
):
    """
    Type definition for `ListJobsPaginateResponse` `jobSummaries`

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


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {
        "jobSummaries": List[ListJobsPaginateResponsejobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

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
