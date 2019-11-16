"Main interface for codestar type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateTeamMemberResponseTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectsourceCodedestinationcodeCommitTypeDef",
    "ClientCreateProjectsourceCodedestinationgitHubTypeDef",
    "ClientCreateProjectsourceCodedestinationTypeDef",
    "ClientCreateProjectsourceCodesources3TypeDef",
    "ClientCreateProjectsourceCodesourceTypeDef",
    "ClientCreateProjectsourceCodeTypeDef",
    "ClientCreateProjecttoolchainsources3TypeDef",
    "ClientCreateProjecttoolchainsourceTypeDef",
    "ClientCreateProjecttoolchainTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientDeleteProjectResponseTypeDef",
    "ClientDeleteUserProfileResponseTypeDef",
    "ClientDescribeProjectResponsestatusTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientDescribeUserProfileResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListResourcesResponseresourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientListTagsForProjectResponseTypeDef",
    "ClientListTeamMembersResponseteamMembersTypeDef",
    "ClientListTeamMembersResponseTypeDef",
    "ClientListUserProfilesResponseuserProfilesTypeDef",
    "ClientListUserProfilesResponseTypeDef",
    "ClientTagProjectResponseTypeDef",
    "ClientUpdateTeamMemberResponseTypeDef",
    "ClientUpdateUserProfileResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseresourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
    "ListTeamMembersPaginatePaginationConfigTypeDef",
    "ListTeamMembersPaginateResponseteamMembersTypeDef",
    "ListTeamMembersPaginateResponseTypeDef",
    "ListUserProfilesPaginatePaginationConfigTypeDef",
    "ListUserProfilesPaginateResponseuserProfilesTypeDef",
    "ListUserProfilesPaginateResponseTypeDef",
)


_ClientAssociateTeamMemberResponseTypeDef = TypedDict(
    "_ClientAssociateTeamMemberResponseTypeDef",
    {"clientRequestToken": str},
    total=False,
)


class ClientAssociateTeamMemberResponseTypeDef(
    _ClientAssociateTeamMemberResponseTypeDef
):
    """
    Type definition for `ClientAssociateTeamMember` `Response`

    - **clientRequestToken** *(string) --*

      The user- or system-generated token from the initial request that can be used to repeat the
      request.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"id": str, "arn": str, "clientRequestToken": str, "projectTemplateId": str},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    Type definition for `ClientCreateProject` `Response`

    - **id** *(string) --*

      The ID of the project.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the created project.

    - **clientRequestToken** *(string) --*

      A user- or system-generated token that identifies the entity that requested project creation.

    - **projectTemplateId** *(string) --*

      Reserved for future use.
    """


_ClientCreateProjectsourceCodedestinationcodeCommitTypeDef = TypedDict(
    "_ClientCreateProjectsourceCodedestinationcodeCommitTypeDef", {"name": str}
)


class ClientCreateProjectsourceCodedestinationcodeCommitTypeDef(
    _ClientCreateProjectsourceCodedestinationcodeCommitTypeDef
):
    """
    Type definition for `ClientCreateProjectsourceCodedestination` `codeCommit`

    Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is
    where the source code files provided with the project request will be uploaded after
    project creation.

    - **name** *(string) --* **[REQUIRED]**

      The name of the AWS CodeCommit repository to be created in AWS CodeStar.
    """


_RequiredClientCreateProjectsourceCodedestinationgitHubTypeDef = TypedDict(
    "_RequiredClientCreateProjectsourceCodedestinationgitHubTypeDef",
    {
        "name": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
    },
)
_OptionalClientCreateProjectsourceCodedestinationgitHubTypeDef = TypedDict(
    "_OptionalClientCreateProjectsourceCodedestinationgitHubTypeDef",
    {"description": str},
    total=False,
)


class ClientCreateProjectsourceCodedestinationgitHubTypeDef(
    _RequiredClientCreateProjectsourceCodedestinationgitHubTypeDef,
    _OptionalClientCreateProjectsourceCodedestinationgitHubTypeDef,
):
    """
    Type definition for `ClientCreateProjectsourceCodedestination` `gitHub`

    Information about the GitHub repository to be created in AWS CodeStar. This is where the
    source code files provided with the project request will be uploaded after project creation.

    - **name** *(string) --* **[REQUIRED]**

      Name of the GitHub repository to be created in AWS CodeStar.

    - **description** *(string) --*

      Description for the GitHub repository to be created in AWS CodeStar. This description
      displays in GitHub after the repository is created.

    - **type** *(string) --* **[REQUIRED]**

      The type of GitHub repository to be created in AWS CodeStar. Valid values are User or
      Organization.

    - **owner** *(string) --* **[REQUIRED]**

      The GitHub username for the owner of the GitHub repository to be created in AWS CodeStar.
      If this repository should be owned by a GitHub organization, provide its name.

    - **privateRepository** *(boolean) --* **[REQUIRED]**

      Whether the GitHub repository is to be a private repository.

    - **issuesEnabled** *(boolean) --* **[REQUIRED]**

      Whether to enable issues for the GitHub repository.

    - **token** *(string) --* **[REQUIRED]**

      The GitHub user's personal access token for the GitHub repository.
    """


_ClientCreateProjectsourceCodedestinationTypeDef = TypedDict(
    "_ClientCreateProjectsourceCodedestinationTypeDef",
    {
        "codeCommit": ClientCreateProjectsourceCodedestinationcodeCommitTypeDef,
        "gitHub": ClientCreateProjectsourceCodedestinationgitHubTypeDef,
    },
    total=False,
)


class ClientCreateProjectsourceCodedestinationTypeDef(
    _ClientCreateProjectsourceCodedestinationTypeDef
):
    """
    Type definition for `ClientCreateProjectsourceCode` `destination`

    The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub.
    After AWS CodeStar provisions the new repository, the source code files provided with the
    project request are placed in the repository.

    - **codeCommit** *(dict) --*

      Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is
      where the source code files provided with the project request will be uploaded after
      project creation.

      - **name** *(string) --* **[REQUIRED]**

        The name of the AWS CodeCommit repository to be created in AWS CodeStar.

    - **gitHub** *(dict) --*

      Information about the GitHub repository to be created in AWS CodeStar. This is where the
      source code files provided with the project request will be uploaded after project creation.

      - **name** *(string) --* **[REQUIRED]**

        Name of the GitHub repository to be created in AWS CodeStar.

      - **description** *(string) --*

        Description for the GitHub repository to be created in AWS CodeStar. This description
        displays in GitHub after the repository is created.

      - **type** *(string) --* **[REQUIRED]**

        The type of GitHub repository to be created in AWS CodeStar. Valid values are User or
        Organization.

      - **owner** *(string) --* **[REQUIRED]**

        The GitHub username for the owner of the GitHub repository to be created in AWS CodeStar.
        If this repository should be owned by a GitHub organization, provide its name.

      - **privateRepository** *(boolean) --* **[REQUIRED]**

        Whether the GitHub repository is to be a private repository.

      - **issuesEnabled** *(boolean) --* **[REQUIRED]**

        Whether to enable issues for the GitHub repository.

      - **token** *(string) --* **[REQUIRED]**

        The GitHub user's personal access token for the GitHub repository.
    """


_ClientCreateProjectsourceCodesources3TypeDef = TypedDict(
    "_ClientCreateProjectsourceCodesources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)


class ClientCreateProjectsourceCodesources3TypeDef(
    _ClientCreateProjectsourceCodesources3TypeDef
):
    """
    Type definition for `ClientCreateProjectsourceCodesource` `s3`

    Information about the Amazon S3 location where the source code files provided with the
    project request are stored.

    - **bucketName** *(string) --*

      The Amazon S3 bucket name where the source code files provided with the project request
      are stored.

    - **bucketKey** *(string) --*

      The Amazon S3 object key where the source code files provided with the project request
      are stored.
    """


_ClientCreateProjectsourceCodesourceTypeDef = TypedDict(
    "_ClientCreateProjectsourceCodesourceTypeDef",
    {"s3": ClientCreateProjectsourceCodesources3TypeDef},
)


class ClientCreateProjectsourceCodesourceTypeDef(
    _ClientCreateProjectsourceCodesourceTypeDef
):
    """
    Type definition for `ClientCreateProjectsourceCode` `source`

    The location where the source code files provided with the project request are stored. AWS
    CodeStar retrieves the files during project creation.

    - **s3** *(dict) --* **[REQUIRED]**

      Information about the Amazon S3 location where the source code files provided with the
      project request are stored.

      - **bucketName** *(string) --*

        The Amazon S3 bucket name where the source code files provided with the project request
        are stored.

      - **bucketKey** *(string) --*

        The Amazon S3 object key where the source code files provided with the project request
        are stored.
    """


_ClientCreateProjectsourceCodeTypeDef = TypedDict(
    "_ClientCreateProjectsourceCodeTypeDef",
    {
        "source": ClientCreateProjectsourceCodesourceTypeDef,
        "destination": ClientCreateProjectsourceCodedestinationTypeDef,
    },
)


class ClientCreateProjectsourceCodeTypeDef(_ClientCreateProjectsourceCodeTypeDef):
    """
    Type definition for `ClientCreateProject` `sourceCode`

    Location and destination information about the source code files provided with the project
    request. The source code is uploaded to the new project source repository after project
    creation.

    - **source** *(dict) --* **[REQUIRED]**

      The location where the source code files provided with the project request are stored. AWS
      CodeStar retrieves the files during project creation.

      - **s3** *(dict) --* **[REQUIRED]**

        Information about the Amazon S3 location where the source code files provided with the
        project request are stored.

        - **bucketName** *(string) --*

          The Amazon S3 bucket name where the source code files provided with the project request
          are stored.

        - **bucketKey** *(string) --*

          The Amazon S3 object key where the source code files provided with the project request
          are stored.

    - **destination** *(dict) --* **[REQUIRED]**

      The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub.
      After AWS CodeStar provisions the new repository, the source code files provided with the
      project request are placed in the repository.

      - **codeCommit** *(dict) --*

        Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is
        where the source code files provided with the project request will be uploaded after
        project creation.

        - **name** *(string) --* **[REQUIRED]**

          The name of the AWS CodeCommit repository to be created in AWS CodeStar.

      - **gitHub** *(dict) --*

        Information about the GitHub repository to be created in AWS CodeStar. This is where the
        source code files provided with the project request will be uploaded after project creation.

        - **name** *(string) --* **[REQUIRED]**

          Name of the GitHub repository to be created in AWS CodeStar.

        - **description** *(string) --*

          Description for the GitHub repository to be created in AWS CodeStar. This description
          displays in GitHub after the repository is created.

        - **type** *(string) --* **[REQUIRED]**

          The type of GitHub repository to be created in AWS CodeStar. Valid values are User or
          Organization.

        - **owner** *(string) --* **[REQUIRED]**

          The GitHub username for the owner of the GitHub repository to be created in AWS CodeStar.
          If this repository should be owned by a GitHub organization, provide its name.

        - **privateRepository** *(boolean) --* **[REQUIRED]**

          Whether the GitHub repository is to be a private repository.

        - **issuesEnabled** *(boolean) --* **[REQUIRED]**

          Whether to enable issues for the GitHub repository.

        - **token** *(string) --* **[REQUIRED]**

          The GitHub user's personal access token for the GitHub repository.
    """


_ClientCreateProjecttoolchainsources3TypeDef = TypedDict(
    "_ClientCreateProjecttoolchainsources3TypeDef",
    {"bucketName": str, "bucketKey": str},
    total=False,
)


class ClientCreateProjecttoolchainsources3TypeDef(
    _ClientCreateProjecttoolchainsources3TypeDef
):
    """
    Type definition for `ClientCreateProjecttoolchainsource` `s3`

    The Amazon S3 bucket where the toolchain template file provided with the project request is
    stored.

    - **bucketName** *(string) --*

      The Amazon S3 bucket name where the source code files provided with the project request are
      stored.

    - **bucketKey** *(string) --*

      The Amazon S3 object key where the source code files provided with the project request are
      stored.
    """


_ClientCreateProjecttoolchainsourceTypeDef = TypedDict(
    "_ClientCreateProjecttoolchainsourceTypeDef",
    {"s3": ClientCreateProjecttoolchainsources3TypeDef},
)


class ClientCreateProjecttoolchainsourceTypeDef(
    _ClientCreateProjecttoolchainsourceTypeDef
):
    """
    Type definition for `ClientCreateProjecttoolchain` `source`

    The Amazon S3 location where the toolchain template file provided with the project request is
    stored. AWS CodeStar retrieves the file during project creation.

    - **s3** *(dict) --* **[REQUIRED]**

      The Amazon S3 bucket where the toolchain template file provided with the project request is
      stored.

      - **bucketName** *(string) --*

        The Amazon S3 bucket name where the source code files provided with the project request are
        stored.

      - **bucketKey** *(string) --*

        The Amazon S3 object key where the source code files provided with the project request are
        stored.
    """


_RequiredClientCreateProjecttoolchainTypeDef = TypedDict(
    "_RequiredClientCreateProjecttoolchainTypeDef",
    {"source": ClientCreateProjecttoolchainsourceTypeDef},
)
_OptionalClientCreateProjecttoolchainTypeDef = TypedDict(
    "_OptionalClientCreateProjecttoolchainTypeDef",
    {"roleArn": str, "stackParameters": Dict[str, str]},
    total=False,
)


class ClientCreateProjecttoolchainTypeDef(
    _RequiredClientCreateProjecttoolchainTypeDef,
    _OptionalClientCreateProjecttoolchainTypeDef,
):
    """
    Type definition for `ClientCreateProject` `toolchain`

    The name of the toolchain template file submitted with the project request. If this parameter is
    specified, the request must also include the sourceCode parameter.

    - **source** *(dict) --* **[REQUIRED]**

      The Amazon S3 location where the toolchain template file provided with the project request is
      stored. AWS CodeStar retrieves the file during project creation.

      - **s3** *(dict) --* **[REQUIRED]**

        The Amazon S3 bucket where the toolchain template file provided with the project request is
        stored.

        - **bucketName** *(string) --*

          The Amazon S3 bucket name where the source code files provided with the project request are
          stored.

        - **bucketKey** *(string) --*

          The Amazon S3 object key where the source code files provided with the project request are
          stored.

    - **roleArn** *(string) --*

      The service role ARN for AWS CodeStar to use for the toolchain template during stack
      provisioning.

    - **stackParameters** *(dict) --*

      The list of parameter overrides to be passed into the toolchain template during stack
      provisioning, if any.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateUserProfileResponseTypeDef = TypedDict(
    "_ClientCreateUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)


class ClientCreateUserProfileResponseTypeDef(_ClientCreateUserProfileResponseTypeDef):
    """
    Type definition for `ClientCreateUserProfile` `Response`

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **displayName** *(string) --*

      The name that is displayed as the friendly name for the user in AWS CodeStar.

    - **emailAddress** *(string) --*

      The email address that is displayed as part of the user's profile in AWS CodeStar.

    - **sshPublicKey** *(string) --*

      The SSH public key associated with the user in AWS CodeStar. This is the public portion of
      the public/private keypair the user can use to access project resources if a project owner
      allows the user remote access to those resources.

    - **createdTimestamp** *(datetime) --*

      The date the user profile was created, in timestamp format.

    - **lastModifiedTimestamp** *(datetime) --*

      The date the user profile was last modified, in timestamp format.
    """


_ClientDeleteProjectResponseTypeDef = TypedDict(
    "_ClientDeleteProjectResponseTypeDef",
    {"stackId": str, "projectArn": str},
    total=False,
)


class ClientDeleteProjectResponseTypeDef(_ClientDeleteProjectResponseTypeDef):
    """
    Type definition for `ClientDeleteProject` `Response`

    - **stackId** *(string) --*

      The ID of the primary stack in AWS CloudFormation that will be deleted as part of deleting
      the project and its resources.

    - **projectArn** *(string) --*

      The Amazon Resource Name (ARN) of the deleted project.
    """


_ClientDeleteUserProfileResponseTypeDef = TypedDict(
    "_ClientDeleteUserProfileResponseTypeDef", {"userArn": str}, total=False
)


class ClientDeleteUserProfileResponseTypeDef(_ClientDeleteUserProfileResponseTypeDef):
    """
    Type definition for `ClientDeleteUserProfile` `Response`

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.
    """


_ClientDescribeProjectResponsestatusTypeDef = TypedDict(
    "_ClientDescribeProjectResponsestatusTypeDef",
    {"state": str, "reason": str},
    total=False,
)


class ClientDescribeProjectResponsestatusTypeDef(
    _ClientDescribeProjectResponsestatusTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponse` `status`

    The project creation or deletion status.

    - **state** *(string) --*

      The phase of completion for a project creation or deletion.

    - **reason** *(string) --*

      In the case of a project creation or deletion failure, a reason for the failure.
    """


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": ClientDescribeProjectResponsestatusTypeDef,
    },
    total=False,
)


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    Type definition for `ClientDescribeProject` `Response`

    - **name** *(string) --*

      The display name for the project.

    - **id** *(string) --*

      The ID of the project.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) for the project.

    - **description** *(string) --*

      The description of the project, if any.

    - **clientRequestToken** *(string) --*

      A user- or system-generated token that identifies the entity that requested project creation.

    - **createdTimeStamp** *(datetime) --*

      The date and time the project was created, in timestamp format.

    - **stackId** *(string) --*

      The ID of the primary stack in AWS CloudFormation used to generate resources for the project.

    - **projectTemplateId** *(string) --*

      The ID for the AWS CodeStar project template used to create the project.

    - **status** *(dict) --*

      The project creation or deletion status.

      - **state** *(string) --*

        The phase of completion for a project creation or deletion.

      - **reason** *(string) --*

        In the case of a project creation or deletion failure, a reason for the failure.
    """


_ClientDescribeUserProfileResponseTypeDef = TypedDict(
    "_ClientDescribeUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeUserProfileResponseTypeDef(
    _ClientDescribeUserProfileResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserProfile` `Response`

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user.

    - **displayName** *(string) --*

      The display name shown for the user in AWS CodeStar projects. For example, this could be set
      to both first and last name ("Mary Major") or a single name ("Mary"). The display name is
      also used to generate the initial icon associated with the user in AWS CodeStar projects. If
      spaces are included in the display name, the first character that appears after the space
      will be used as the second character in the user initial icon. The initial icon displays a
      maximum of two characters, so a display name with more than one space (for example "Mary Jane
      Major") would generate an initial icon using the first character and the first character
      after the space ("MJ", not "MM").

    - **emailAddress** *(string) --*

      The email address for the user. Optional.

    - **sshPublicKey** *(string) --*

      The SSH public key associated with the user. This SSH public key is associated with the user
      profile, and can be used in conjunction with the associated private key for access to project
      resources, such as Amazon EC2 instances, if a project owner grants remote access to those
      resources.

    - **createdTimestamp** *(datetime) --*

      The date and time when the user profile was created in AWS CodeStar, in timestamp format.

    - **lastModifiedTimestamp** *(datetime) --*

      The date and time when the user profile was last modified, in timestamp format.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef",
    {"projectId": str, "projectArn": str},
    total=False,
)


class ClientListProjectsResponseprojectsTypeDef(
    _ClientListProjectsResponseprojectsTypeDef
):
    """
    Type definition for `ClientListProjectsResponse` `projects`

    Information about the metadata for a project.

    - **projectId** *(string) --*

      The ID of the project.

    - **projectArn** *(string) --*

      The Amazon Resource Name (ARN) of the project.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    Type definition for `ClientListProjects` `Response`

    - **projects** *(list) --*

      A list of projects.

      - *(dict) --*

        Information about the metadata for a project.

        - **projectId** *(string) --*

          The ID of the project.

        - **projectArn** *(string) --*

          The Amazon Resource Name (ARN) of the project.

    - **nextToken** *(string) --*

      The continuation token to use when requesting the next set of results, if there are more
      results to be returned.
    """


_ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseresourcesTypeDef", {"id": str}, total=False
)


class ClientListResourcesResponseresourcesTypeDef(
    _ClientListResourcesResponseresourcesTypeDef
):
    """
    Type definition for `ClientListResourcesResponse` `resources`

    Information about a resource for a project.

    - **id** *(string) --*

      The Amazon Resource Name (ARN) of the resource.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    Type definition for `ClientListResources` `Response`

    - **resources** *(list) --*

      An array of resources associated with the project.

      - *(dict) --*

        Information about a resource for a project.

        - **id** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

    - **nextToken** *(string) --*

      The continuation token to use when requesting the next set of results, if there are more
      results to be returned.
    """


_ClientListTagsForProjectResponseTypeDef = TypedDict(
    "_ClientListTagsForProjectResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)


class ClientListTagsForProjectResponseTypeDef(_ClientListTagsForProjectResponseTypeDef):
    """
    Type definition for `ClientListTagsForProject` `Response`

    - **tags** *(dict) --*

      The tags for the project.

      - *(string) --*

        - *(string) --*

    - **nextToken** *(string) --*

      Reserved for future use.
    """


_ClientListTeamMembersResponseteamMembersTypeDef = TypedDict(
    "_ClientListTeamMembersResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ClientListTeamMembersResponseteamMembersTypeDef(
    _ClientListTeamMembersResponseteamMembersTypeDef
):
    """
    Type definition for `ClientListTeamMembersResponse` `teamMembers`

    Information about a team member in a project.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **projectRole** *(string) --*

      The role assigned to the user in the project. Project roles have different levels of
      access. For more information, see `Working with Teams
      <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the
      *AWS CodeStar User Guide* .

    - **remoteAccessAllowed** *(boolean) --*

      Whether the user is allowed to remotely access project resources using an SSH
      public/private key pair.
    """


_ClientListTeamMembersResponseTypeDef = TypedDict(
    "_ClientListTeamMembersResponseTypeDef",
    {
        "teamMembers": List[ClientListTeamMembersResponseteamMembersTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListTeamMembersResponseTypeDef(_ClientListTeamMembersResponseTypeDef):
    """
    Type definition for `ClientListTeamMembers` `Response`

    - **teamMembers** *(list) --*

      A list of team member objects for the project.

      - *(dict) --*

        Information about a team member in a project.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the user in IAM.

        - **projectRole** *(string) --*

          The role assigned to the user in the project. Project roles have different levels of
          access. For more information, see `Working with Teams
          <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the
          *AWS CodeStar User Guide* .

        - **remoteAccessAllowed** *(boolean) --*

          Whether the user is allowed to remotely access project resources using an SSH
          public/private key pair.

    - **nextToken** *(string) --*

      The continuation token to use when requesting the next set of results, if there are more
      results to be returned.
    """


_ClientListUserProfilesResponseuserProfilesTypeDef = TypedDict(
    "_ClientListUserProfilesResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)


class ClientListUserProfilesResponseuserProfilesTypeDef(
    _ClientListUserProfilesResponseuserProfilesTypeDef
):
    """
    Type definition for `ClientListUserProfilesResponse` `userProfiles`

    Information about a user's profile in AWS CodeStar.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **displayName** *(string) --*

      The display name of a user in AWS CodeStar. For example, this could be set to both first
      and last name ("Mary Major") or a single name ("Mary"). The display name is also used to
      generate the initial icon associated with the user in AWS CodeStar projects. If spaces
      are included in the display name, the first character that appears after the space will
      be used as the second character in the user initial icon. The initial icon displays a
      maximum of two characters, so a display name with more than one space (for example "Mary
      Jane Major") would generate an initial icon using the first character and the first
      character after the space ("MJ", not "MM").

    - **emailAddress** *(string) --*

      The email address associated with the user.

    - **sshPublicKey** *(string) --*

      The SSH public key associated with the user in AWS CodeStar. If a project owner allows
      the user remote access to project resources, this public key will be used along with the
      user's private key for SSH access.
    """


_ClientListUserProfilesResponseTypeDef = TypedDict(
    "_ClientListUserProfilesResponseTypeDef",
    {
        "userProfiles": List[ClientListUserProfilesResponseuserProfilesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListUserProfilesResponseTypeDef(_ClientListUserProfilesResponseTypeDef):
    """
    Type definition for `ClientListUserProfiles` `Response`

    - **userProfiles** *(list) --*

      All the user profiles configured in AWS CodeStar for an AWS account.

      - *(dict) --*

        Information about a user's profile in AWS CodeStar.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the user in IAM.

        - **displayName** *(string) --*

          The display name of a user in AWS CodeStar. For example, this could be set to both first
          and last name ("Mary Major") or a single name ("Mary"). The display name is also used to
          generate the initial icon associated with the user in AWS CodeStar projects. If spaces
          are included in the display name, the first character that appears after the space will
          be used as the second character in the user initial icon. The initial icon displays a
          maximum of two characters, so a display name with more than one space (for example "Mary
          Jane Major") would generate an initial icon using the first character and the first
          character after the space ("MJ", not "MM").

        - **emailAddress** *(string) --*

          The email address associated with the user.

        - **sshPublicKey** *(string) --*

          The SSH public key associated with the user in AWS CodeStar. If a project owner allows
          the user remote access to project resources, this public key will be used along with the
          user's private key for SSH access.

    - **nextToken** *(string) --*

      The continuation token to use when requesting the next set of results, if there are more
      results to be returned.
    """


_ClientTagProjectResponseTypeDef = TypedDict(
    "_ClientTagProjectResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientTagProjectResponseTypeDef(_ClientTagProjectResponseTypeDef):
    """
    Type definition for `ClientTagProject` `Response`

    - **tags** *(dict) --*

      The tags for the project.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateTeamMemberResponseTypeDef = TypedDict(
    "_ClientUpdateTeamMemberResponseTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ClientUpdateTeamMemberResponseTypeDef(_ClientUpdateTeamMemberResponseTypeDef):
    """
    Type definition for `ClientUpdateTeamMember` `Response`

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user whose team membership attributes were updated.

    - **projectRole** *(string) --*

      The project role granted to the user.

    - **remoteAccessAllowed** *(boolean) --*

      Whether a team member is allowed to remotely access project resources using the SSH public
      key associated with the user's profile.
    """


_ClientUpdateUserProfileResponseTypeDef = TypedDict(
    "_ClientUpdateUserProfileResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)


class ClientUpdateUserProfileResponseTypeDef(_ClientUpdateUserProfileResponseTypeDef):
    """
    Type definition for `ClientUpdateUserProfile` `Response`

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **displayName** *(string) --*

      The name that is displayed as the friendly name for the user in AWS CodeStar.

    - **emailAddress** *(string) --*

      The email address that is displayed as part of the user's profile in AWS CodeStar.

    - **sshPublicKey** *(string) --*

      The SSH public key associated with the user in AWS CodeStar. This is the public portion of
      the public/private keypair the user can use to access project resources if a project owner
      allows the user remote access to those resources.

    - **createdTimestamp** *(datetime) --*

      The date the user profile was created, in timestamp format.

    - **lastModifiedTimestamp** *(datetime) --*

      The date the user profile was last modified, in timestamp format.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(
    _ListProjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProjectsPaginate` `PaginationConfig`

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


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {"projectId": str, "projectArn": str},
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(
    _ListProjectsPaginateResponseprojectsTypeDef
):
    """
    Type definition for `ListProjectsPaginateResponse` `projects`

    Information about the metadata for a project.

    - **projectId** *(string) --*

      The ID of the project.

    - **projectArn** *(string) --*

      The Amazon Resource Name (ARN) of the project.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    Type definition for `ListProjectsPaginate` `Response`

    - **projects** *(list) --*

      A list of projects.

      - *(dict) --*

        Information about the metadata for a project.

        - **projectId** *(string) --*

          The ID of the project.

        - **projectArn** *(string) --*

          The Amazon Resource Name (ARN) of the project.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesPaginatePaginationConfigTypeDef(
    _ListResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourcesPaginate` `PaginationConfig`

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


_ListResourcesPaginateResponseresourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseresourcesTypeDef", {"id": str}, total=False
)


class ListResourcesPaginateResponseresourcesTypeDef(
    _ListResourcesPaginateResponseresourcesTypeDef
):
    """
    Type definition for `ListResourcesPaginateResponse` `resources`

    Information about a resource for a project.

    - **id** *(string) --*

      The Amazon Resource Name (ARN) of the resource.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {
        "resources": List[ListResourcesPaginateResponseresourcesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    Type definition for `ListResourcesPaginate` `Response`

    - **resources** *(list) --*

      An array of resources associated with the project.

      - *(dict) --*

        Information about a resource for a project.

        - **id** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTeamMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTeamMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTeamMembersPaginatePaginationConfigTypeDef(
    _ListTeamMembersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTeamMembersPaginate` `PaginationConfig`

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


_ListTeamMembersPaginateResponseteamMembersTypeDef = TypedDict(
    "_ListTeamMembersPaginateResponseteamMembersTypeDef",
    {"userArn": str, "projectRole": str, "remoteAccessAllowed": bool},
    total=False,
)


class ListTeamMembersPaginateResponseteamMembersTypeDef(
    _ListTeamMembersPaginateResponseteamMembersTypeDef
):
    """
    Type definition for `ListTeamMembersPaginateResponse` `teamMembers`

    Information about a team member in a project.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **projectRole** *(string) --*

      The role assigned to the user in the project. Project roles have different levels of
      access. For more information, see `Working with Teams
      <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the
      *AWS CodeStar User Guide* .

    - **remoteAccessAllowed** *(boolean) --*

      Whether the user is allowed to remotely access project resources using an SSH
      public/private key pair.
    """


_ListTeamMembersPaginateResponseTypeDef = TypedDict(
    "_ListTeamMembersPaginateResponseTypeDef",
    {
        "teamMembers": List[ListTeamMembersPaginateResponseteamMembersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListTeamMembersPaginateResponseTypeDef(_ListTeamMembersPaginateResponseTypeDef):
    """
    Type definition for `ListTeamMembersPaginate` `Response`

    - **teamMembers** *(list) --*

      A list of team member objects for the project.

      - *(dict) --*

        Information about a team member in a project.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the user in IAM.

        - **projectRole** *(string) --*

          The role assigned to the user in the project. Project roles have different levels of
          access. For more information, see `Working with Teams
          <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the
          *AWS CodeStar User Guide* .

        - **remoteAccessAllowed** *(boolean) --*

          Whether the user is allowed to remotely access project resources using an SSH
          public/private key pair.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListUserProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserProfilesPaginatePaginationConfigTypeDef(
    _ListUserProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUserProfilesPaginate` `PaginationConfig`

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


_ListUserProfilesPaginateResponseuserProfilesTypeDef = TypedDict(
    "_ListUserProfilesPaginateResponseuserProfilesTypeDef",
    {"userArn": str, "displayName": str, "emailAddress": str, "sshPublicKey": str},
    total=False,
)


class ListUserProfilesPaginateResponseuserProfilesTypeDef(
    _ListUserProfilesPaginateResponseuserProfilesTypeDef
):
    """
    Type definition for `ListUserProfilesPaginateResponse` `userProfiles`

    Information about a user's profile in AWS CodeStar.

    - **userArn** *(string) --*

      The Amazon Resource Name (ARN) of the user in IAM.

    - **displayName** *(string) --*

      The display name of a user in AWS CodeStar. For example, this could be set to both first
      and last name ("Mary Major") or a single name ("Mary"). The display name is also used to
      generate the initial icon associated with the user in AWS CodeStar projects. If spaces
      are included in the display name, the first character that appears after the space will
      be used as the second character in the user initial icon. The initial icon displays a
      maximum of two characters, so a display name with more than one space (for example "Mary
      Jane Major") would generate an initial icon using the first character and the first
      character after the space ("MJ", not "MM").

    - **emailAddress** *(string) --*

      The email address associated with the user.

    - **sshPublicKey** *(string) --*

      The SSH public key associated with the user in AWS CodeStar. If a project owner allows
      the user remote access to project resources, this public key will be used along with the
      user's private key for SSH access.
    """


_ListUserProfilesPaginateResponseTypeDef = TypedDict(
    "_ListUserProfilesPaginateResponseTypeDef",
    {
        "userProfiles": List[ListUserProfilesPaginateResponseuserProfilesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListUserProfilesPaginateResponseTypeDef(_ListUserProfilesPaginateResponseTypeDef):
    """
    Type definition for `ListUserProfilesPaginate` `Response`

    - **userProfiles** *(list) --*

      All the user profiles configured in AWS CodeStar for an AWS account.

      - *(dict) --*

        Information about a user's profile in AWS CodeStar.

        - **userArn** *(string) --*

          The Amazon Resource Name (ARN) of the user in IAM.

        - **displayName** *(string) --*

          The display name of a user in AWS CodeStar. For example, this could be set to both first
          and last name ("Mary Major") or a single name ("Mary"). The display name is also used to
          generate the initial icon associated with the user in AWS CodeStar projects. If spaces
          are included in the display name, the first character that appears after the space will
          be used as the second character in the user initial icon. The initial icon displays a
          maximum of two characters, so a display name with more than one space (for example "Mary
          Jane Major") would generate an initial icon using the first character and the first
          character after the space ("MJ", not "MM").

        - **emailAddress** *(string) --*

          The email address associated with the user.

        - **sshPublicKey** *(string) --*

          The SSH public key associated with the user in AWS CodeStar. If a project owner allows
          the user remote access to project resources, this public key will be used along with the
          user's private key for SSH access.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
