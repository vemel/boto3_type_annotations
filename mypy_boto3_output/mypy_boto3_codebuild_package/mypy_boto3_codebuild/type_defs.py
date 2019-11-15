"Main interface for codebuild type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


_ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef = TypedDict(
    "_ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef",
    {"id": str, "statusCode": str},
    total=False,
)


class ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef(
    _ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef
):
    """
    Type definition for `ClientBatchDeleteBuildsResponse` `buildsNotDeleted`

    Information about a build that could not be successfully deleted.

    - **id** *(string) --*

      The ID of the build that could not be successfully deleted.

    - **statusCode** *(string) --*

      Additional information about the build that could not be successfully deleted.
    """


_ClientBatchDeleteBuildsResponseTypeDef = TypedDict(
    "_ClientBatchDeleteBuildsResponseTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List[
            ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef
        ],
    },
    total=False,
)


class ClientBatchDeleteBuildsResponseTypeDef(_ClientBatchDeleteBuildsResponseTypeDef):
    """
    Type definition for `ClientBatchDeleteBuilds` `Response`

    - **buildsDeleted** *(list) --*

      The IDs of the builds that were successfully deleted.

      - *(string) --*

    - **buildsNotDeleted** *(list) --*

      Information about any builds that could not be successfully deleted.

      - *(dict) --*

        Information about a build that could not be successfully deleted.

        - **id** *(string) --*

          The ID of the build that could not be successfully deleted.

        - **statusCode** *(string) --*

          Additional information about the build that could not be successfully deleted.
    """


_ClientBatchGetBuildsResponsebuildsartifactsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsartifactsTypeDef(
    _ClientBatchGetBuildsResponsebuildsartifactsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `artifacts`

    Information about the output artifacts for the build.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientBatchGetBuildsResponsebuildscacheTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildscacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientBatchGetBuildsResponsebuildscacheTypeDef(
    _ClientBatchGetBuildsResponsebuildscacheTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `cache`

    Information about the cache for the build.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits.
      This mode is a good choice for projects with a clean working directory and a source
      that is a large Git repository. If you choose this option and your project does not use
      a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
      This mode is a good choice if your build scenario is not suited to one of the other
      three local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project
        sources. Cached items are overriden if a source item has the same name. Directories
        are specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildsenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive
        values, especially AWS secret key IDs and secret access keys. Environment
        variables can be displayed in plain text using the AWS CodeBuild console and the
        AWS Command Line Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
      Manager Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildsenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
      Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The
      valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientBatchGetBuildsResponsebuildsenvironmentTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `environment`

    Information about the build environment for this build.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an
      image with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values
      include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive
            values, especially AWS secret key IDs and secret access keys. Environment
            variables can be displayed in plain text using the AWS CodeBuild console and the
            AWS Command Line Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
          Manager Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding
      one of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
        Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The
        valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
      that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef(
    _ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `exportedEnvironmentVariables`

    Information about an exported environment variable.

    - **name** *(string) --*

      The name of this exported environment variable.

    - **value** *(string) --*

      The value assigned to this exported environment variable.

      .. note::

        During a build, the value of a variable is available starting with the ``install``
        phase. It can be updated between the start of the ``install`` phase and the end of
        the ``post_build`` phase. After the ``post_build`` phase ends, the value of
        exported variables cannot change.
    """


_ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef(
    _ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildslogs` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
      see `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef(
    _ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildslogs` `s3Logs`

    Information about S3 logs for a build project.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
      name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
      formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3
      build logs are encrypted.
    """


_ClientBatchGetBuildsResponsebuildslogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogs": ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogsTypeDef(
    _ClientBatchGetBuildsResponsebuildslogsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `logs`

    Information about the build's logs in Amazon CloudWatch Logs.

    - **groupName** *(string) --*

      The name of the Amazon CloudWatch Logs group for the build logs.

    - **streamName** *(string) --*

      The name of the Amazon CloudWatch Logs stream for the build logs.

    - **deepLink** *(string) --*

      The URL to an individual build log in Amazon CloudWatch Logs.

    - **s3DeepLink** *(string) --*

      The URL to a build log in an S3 bucket.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
        see `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about S3 logs for a build project.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
        name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
        formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3
        build logs are encrypted.
    """


_ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef(
    _ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `networkInterface`

    Describes a network interface.

    - **subnetId** *(string) --*

      The ID of the subnet.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.
    """


_ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef(
    _ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildsphases` `contexts`

    Additional information about a build phase that has an error. You can use this
    information for troubleshooting.

    - **statusCode** *(string) --*

      The status code for the context of the build phase.

    - **message** *(string) --*

      An explanation of the build phase's context. This might include a command ID and
      an exit code.
    """


_ClientBatchGetBuildsResponsebuildsphasesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsphasesTypeDef",
    {
        "phaseType": str,
        "phaseStatus": str,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsphasesTypeDef(
    _ClientBatchGetBuildsResponsebuildsphasesTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `phases`

    Information about a stage for a build.

    - **phaseType** *(string) --*

      The name of the build phase. Valid values include:

      * ``BUILD`` : Core build activities typically occur in this build phase.

      * ``COMPLETED`` : The build has been completed.

      * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

      * ``FINALIZING`` : The build process is completing in this build phase.

      * ``INSTALL`` : Installation activities typically occur in this build phase.

      * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

      * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

      * ``PROVISIONING`` : The build environment is being set up.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted
      builds.

      * ``SUBMITTED`` : The build has been submitted.

      * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
      location.

    - **phaseStatus** *(string) --*

      The current status of the build phase. Valid values include:

      * ``FAILED`` : The build phase failed.

      * ``FAULT`` : The build phase faulted.

      * ``IN_PROGRESS`` : The build phase is still in progress.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted
      builds.

      * ``STOPPED`` : The build phase stopped.

      * ``SUCCEEDED`` : The build phase succeeded.

      * ``TIMED_OUT`` : The build phase timed out.

    - **startTime** *(datetime) --*

      When the build phase started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build phase ended, expressed in Unix time format.

    - **durationInSeconds** *(integer) --*

      How long, in seconds, between the starting and ending times of the build's phase.

    - **contexts** *(list) --*

      Additional information about a build phase, especially to help troubleshoot a failed
      build.

      - *(dict) --*

        Additional information about a build phase that has an error. You can use this
        information for troubleshooting.

        - **statusCode** *(string) --*

          The status code for the context of the build phase.

        - **message** *(string) --*

          An explanation of the build phase's context. This might include a command ID and
          an exit code.
    """


_ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `secondaryArtifacts`

    Information about build output artifacts.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses
      the Shell Command Language. For example, you can append a date and time to your
      artifact name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that
      corresponds to the version of the source code you want to build. If a pull request ID
      is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
      ). If a branch name is specified, the branch's HEAD commit ID is used. If not
      specified, the default branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
      ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildssecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not
    get or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildssecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values
      include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in
      AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
      of the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
      that contains the source and the build spec. You must connect your AWS account to
      your Bitbucket account. Use the AWS CodeBuild console to start creating a build
      project. When you use the console to connect (or reconnect) with Bitbucket, on the
      Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
      you have connected to your Bitbucket account, you do not need to finish creating the
      build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
      use this connection, in the ``source`` object, set the ``auth`` object's ``type``
      value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not
      get or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source
      provider. This option is valid only when your source provider is GitHub, GitHub
      Enterprise, or Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientBatchGetBuildsResponsebuildssourceauthTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourceauthTypeDef(
    _ClientBatchGetBuildsResponsebuildssourceauthTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildssource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuildssource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientBatchGetBuildsResponsebuildssourceTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourceTypeDef(
    _ClientBatchGetBuildsResponsebuildssourceTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `source`

    Information about the source code to be built.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponsebuilds` `vpcConfig`

    If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
    parameter that identifies the VPC ID and the list of security group IDs and subnet IDs.
    The security groups and subnets must belong to the same VPC. You must provide at least
    one security group and one subnet ID.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientBatchGetBuildsResponsebuildsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": str,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientBatchGetBuildsResponsebuildsphasesTypeDef],
        "source": ClientBatchGetBuildsResponsebuildssourceTypeDef,
        "secondarySources": List[
            ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef
        ],
        "secondarySourceVersions": List[
            ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetBuildsResponsebuildsartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef
        ],
        "cache": ClientBatchGetBuildsResponsebuildscacheTypeDef,
        "environment": ClientBatchGetBuildsResponsebuildsenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientBatchGetBuildsResponsebuildslogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef,
        "networkInterface": ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsTypeDef(
    _ClientBatchGetBuildsResponsebuildsTypeDef
):
    """
    Type definition for `ClientBatchGetBuildsResponse` `builds`

    Information about a build.

    - **id** *(string) --*

      The unique ID for the build.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build.

    - **buildNumber** *(integer) --*

      The number of the build. For each project, the ``buildNumber`` of its first build is
      ``1`` . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build
      is deleted, the ``buildNumber`` of other builds does not change.

    - **startTime** *(datetime) --*

      When the build process started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build process ended, expressed in Unix time format.

    - **currentPhase** *(string) --*

      The current build phase.

    - **buildStatus** *(string) --*

      The current status of the build. Valid values include:

      * ``FAILED`` : The build failed.

      * ``FAULT`` : The build faulted.

      * ``IN_PROGRESS`` : The build is still in progress.

      * ``STOPPED`` : The build stopped.

      * ``SUCCEEDED`` : The build succeeded.

      * ``TIMED_OUT`` : The build timed out.

    - **sourceVersion** *(string) --*

      Any version identifier for the version of the source code to be built. If
      ``sourceVersion`` is specified at the project level, then this ``sourceVersion`` (at the
      build level) takes precedence.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **resolvedSourceVersion** *(string) --*

      An identifier for the version of this build's source code.

      * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

      * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

      * For Amazon Simple Storage Service (Amazon S3), this does not apply.

    - **projectName** *(string) --*

      The name of the AWS CodeBuild project.

    - **phases** *(list) --*

      Information about all previous build phases that are complete and information about any
      current build phase that is not yet complete.

      - *(dict) --*

        Information about a stage for a build.

        - **phaseType** *(string) --*

          The name of the build phase. Valid values include:

          * ``BUILD`` : Core build activities typically occur in this build phase.

          * ``COMPLETED`` : The build has been completed.

          * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

          * ``FINALIZING`` : The build process is completing in this build phase.

          * ``INSTALL`` : Installation activities typically occur in this build phase.

          * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

          * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

          * ``PROVISIONING`` : The build environment is being set up.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted
          builds.

          * ``SUBMITTED`` : The build has been submitted.

          * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
          location.

        - **phaseStatus** *(string) --*

          The current status of the build phase. Valid values include:

          * ``FAILED`` : The build phase failed.

          * ``FAULT`` : The build phase faulted.

          * ``IN_PROGRESS`` : The build phase is still in progress.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted
          builds.

          * ``STOPPED`` : The build phase stopped.

          * ``SUCCEEDED`` : The build phase succeeded.

          * ``TIMED_OUT`` : The build phase timed out.

        - **startTime** *(datetime) --*

          When the build phase started, expressed in Unix time format.

        - **endTime** *(datetime) --*

          When the build phase ended, expressed in Unix time format.

        - **durationInSeconds** *(integer) --*

          How long, in seconds, between the starting and ending times of the build's phase.

        - **contexts** *(list) --*

          Additional information about a build phase, especially to help troubleshoot a failed
          build.

          - *(dict) --*

            Additional information about a build phase that has an error. You can use this
            information for troubleshooting.

            - **statusCode** *(string) --*

              The status code for the context of the build phase.

            - **message** *(string) --*

              An explanation of the build phase's context. This might include a command ID and
              an exit code.

    - **source** *(dict) --*

      Information about the source code to be built.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS
        CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
        pipeline's source action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
        repository that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, ``
          *bucket-name* /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        GitHub account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to
        each repository you want to allow AWS CodeBuild to have access to, and then choose
        **Authorize application** . (After you have connected to your GitHub account, you do
        not need to finish creating the build project. You can leave the AWS CodeBuild
        console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
        set the ``auth`` object's ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
        When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
        **Confirm access to your account** page, choose **Grant access** . (After you have
        connected to your Bitbucket account, you do not need to finish creating the build
        project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
        this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
        ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source
        code to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source
        code to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get
        or set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents
          the OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source
          provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values
          include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in
          AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
          of the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
          that contains the source and the build spec. You must connect your AWS account to
          your Bitbucket account. Use the AWS CodeBuild console to start creating a build
          project. When you use the console to connect (or reconnect) with Bitbucket, on the
          Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
          you have connected to your Bitbucket account, you do not need to finish creating the
          build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
          use this connection, in the ``source`` object, set the ``auth`` object's ``type``
          value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not
          get or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source
          provider. This option is valid only when your source provider is GitHub, GitHub
          Enterprise, or Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name
      is specified, the branch's HEAD commit ID is used. If not specified, the default branch's
      HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
      of the source code you want to build. If a branch name is specified, the branch's HEAD
      commit ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that
          corresponds to the version of the source code you want to build. If a pull request ID
          is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
          ). If a branch name is specified, the branch's HEAD commit ID is used. If not
          specified, the default branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
          ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the output artifacts for the build.

      - **location** *(string) --*

        Information about the location of the build artifacts.

      - **sha256sum** *(string) --*

        The SHA-256 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **md5sum** *(string) --*

        The MD5 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact
        name. The name specified in a build spec file is calculated at build time and uses the
        Shell Command Language. For example, you can append a date and time to your artifact
        name so that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Information that tells you if encryption for build artifacts is disabled.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about build output artifacts.

        - **location** *(string) --*

          Information about the location of the build artifacts.

        - **sha256sum** *(string) --*

          The SHA-256 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **md5sum** *(string) --*

          The MD5 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses
          the Shell Command Language. For example, you can append a date and time to your
          artifact name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Information that tells you if encryption for build artifacts is disabled.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits.
        This mode is a good choice for projects with a clean working directory and a source
        that is a large Git repository. If you choose this option and your project does not use
        a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
        This mode is a good choice if your build scenario is not suited to one of the other
        three local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project
          sources. Cached items are overriden if a source item has the same name. Directories
          are specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an
        image with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values
        include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive
              values, especially AWS secret key IDs and secret access keys. Environment
              variables can be displayed in plain text using the AWS CodeBuild console and the
              AWS Command Line Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
            Manager Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding
        one of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
          Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The
          valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
        that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The name of a service role used for this build.

    - **logs** *(dict) --*

      Information about the build's logs in Amazon CloudWatch Logs.

      - **groupName** *(string) --*

        The name of the Amazon CloudWatch Logs group for the build logs.

      - **streamName** *(string) --*

        The name of the Amazon CloudWatch Logs stream for the build logs.

      - **deepLink** *(string) --*

        The URL to an individual build log in Amazon CloudWatch Logs.

      - **s3DeepLink** *(string) --*

        The URL to a build log in an S3 bucket.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
          see `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about S3 logs for a build project.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
          name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
          formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3
          build logs are encrypted.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does
      not get marked as completed.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **buildComplete** *(boolean) --*

      Whether the build is complete. True if complete; otherwise, false.

    - **initiator** *(string) --*

      The entity that started the build. Valid values include:

      * If AWS CodePipeline started the build, the pipeline's name (for example,
      ``codepipeline/my-demo-pipeline`` ).

      * If an AWS Identity and Access Management (IAM) user started the build, the user's name
      (for example, ``MyUserName`` ).

      * If the Jenkins plugin for AWS CodeBuild started the build, the string
      ``CodeBuild-Jenkins-Plugin`` .

    - **vpcConfig** *(dict) --*

      If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
      parameter that identifies the VPC ID and the list of security group IDs and subnet IDs.
      The security groups and subnets must belong to the same VPC. You must provide at least
      one security group and one subnet ID.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **networkInterface** *(dict) --*

      Describes a network interface.

      - **subnetId** *(string) --*

        The ID of the subnet.

      - **networkInterfaceId** *(string) --*

        The ID of the network interface.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your
        service role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **exportedEnvironmentVariables** *(list) --*

      A list of exported environment variables for this build.

      - *(dict) --*

        Information about an exported environment variable.

        - **name** *(string) --*

          The name of this exported environment variable.

        - **value** *(string) --*

          The value assigned to this exported environment variable.

          .. note::

            During a build, the value of a variable is available starting with the ``install``
            phase. It can be updated between the start of the ``install`` phase and the end of
            the ``post_build`` phase. After the ``post_build`` phase ends, the value of
            exported variables cannot change.
    """


_ClientBatchGetBuildsResponseTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponseTypeDef",
    {
        "builds": List[ClientBatchGetBuildsResponsebuildsTypeDef],
        "buildsNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetBuildsResponseTypeDef(_ClientBatchGetBuildsResponseTypeDef):
    """
    Type definition for `ClientBatchGetBuilds` `Response`

    - **builds** *(list) --*

      Information about the requested builds.

      - *(dict) --*

        Information about a build.

        - **id** *(string) --*

          The unique ID for the build.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the build.

        - **buildNumber** *(integer) --*

          The number of the build. For each project, the ``buildNumber`` of its first build is
          ``1`` . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build
          is deleted, the ``buildNumber`` of other builds does not change.

        - **startTime** *(datetime) --*

          When the build process started, expressed in Unix time format.

        - **endTime** *(datetime) --*

          When the build process ended, expressed in Unix time format.

        - **currentPhase** *(string) --*

          The current build phase.

        - **buildStatus** *(string) --*

          The current status of the build. Valid values include:

          * ``FAILED`` : The build failed.

          * ``FAULT`` : The build faulted.

          * ``IN_PROGRESS`` : The build is still in progress.

          * ``STOPPED`` : The build stopped.

          * ``SUCCEEDED`` : The build succeeded.

          * ``TIMED_OUT`` : The build timed out.

        - **sourceVersion** *(string) --*

          Any version identifier for the version of the source code to be built. If
          ``sourceVersion`` is specified at the project level, then this ``sourceVersion`` (at the
          build level) takes precedence.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
          the *AWS CodeBuild User Guide* .

        - **resolvedSourceVersion** *(string) --*

          An identifier for the version of this build's source code.

          * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

          * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

          * For Amazon Simple Storage Service (Amazon S3), this does not apply.

        - **projectName** *(string) --*

          The name of the AWS CodeBuild project.

        - **phases** *(list) --*

          Information about all previous build phases that are complete and information about any
          current build phase that is not yet complete.

          - *(dict) --*

            Information about a stage for a build.

            - **phaseType** *(string) --*

              The name of the build phase. Valid values include:

              * ``BUILD`` : Core build activities typically occur in this build phase.

              * ``COMPLETED`` : The build has been completed.

              * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

              * ``FINALIZING`` : The build process is completing in this build phase.

              * ``INSTALL`` : Installation activities typically occur in this build phase.

              * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

              * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

              * ``PROVISIONING`` : The build environment is being set up.

              * ``QUEUED`` : The build has been submitted and is queued behind other submitted
              builds.

              * ``SUBMITTED`` : The build has been submitted.

              * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
              location.

            - **phaseStatus** *(string) --*

              The current status of the build phase. Valid values include:

              * ``FAILED`` : The build phase failed.

              * ``FAULT`` : The build phase faulted.

              * ``IN_PROGRESS`` : The build phase is still in progress.

              * ``QUEUED`` : The build has been submitted and is queued behind other submitted
              builds.

              * ``STOPPED`` : The build phase stopped.

              * ``SUCCEEDED`` : The build phase succeeded.

              * ``TIMED_OUT`` : The build phase timed out.

            - **startTime** *(datetime) --*

              When the build phase started, expressed in Unix time format.

            - **endTime** *(datetime) --*

              When the build phase ended, expressed in Unix time format.

            - **durationInSeconds** *(integer) --*

              How long, in seconds, between the starting and ending times of the build's phase.

            - **contexts** *(list) --*

              Additional information about a build phase, especially to help troubleshoot a failed
              build.

              - *(dict) --*

                Additional information about a build phase that has an error. You can use this
                information for troubleshooting.

                - **statusCode** *(string) --*

                  The status code for the context of the build phase.

                - **message** *(string) --*

                  An explanation of the build phase's context. This might include a command ID and
                  an exit code.

        - **source** *(dict) --*

          Information about the source code to be built.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

        - **secondarySources** *(list) --*

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build input source code for the build project.

            - **type** *(string) --*

              The type of repository that contains the source code to be built. Valid values
              include:

              * ``BITBUCKET`` : The source code is in a Bitbucket repository.

              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
              pipeline in AWS CodePipeline.

              * ``GITHUB`` : The source code is in a GitHub repository.

              * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

              * ``NO_SOURCE`` : The project does not have input source code.

              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
              bucket.

            - **location** *(string) --*

              Information about the location of the source code to be built. Valid values include:

              * For source code settings that are specified in the source action of a pipeline in
              AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
              CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
              pipeline's source action instead of this value.

              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
              repository that contains the source code and the build spec (for example,
              ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
              of the following.

                * The path to the ZIP file that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                * The path to the folder that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

              * For source code in a GitHub repository, the HTTPS clone URL to the repository that
              contains the source and the build spec. You must connect your AWS account to your
              GitHub account. Use the AWS CodeBuild console to start creating a build project. When
              you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
              application** page, for **Organization access** , choose **Request access** next to
              each repository you want to allow AWS CodeBuild to have access to, and then choose
              **Authorize application** . (After you have connected to your GitHub account, you do
              not need to finish creating the build project. You can leave the AWS CodeBuild
              console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
              set the ``auth`` object's ``type`` value to ``OAUTH`` .

              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
              that contains the source and the build spec. You must connect your AWS account to
              your Bitbucket account. Use the AWS CodeBuild console to start creating a build
              project. When you use the console to connect (or reconnect) with Bitbucket, on the
              Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
              you have connected to your Bitbucket account, you do not need to finish creating the
              build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
              use this connection, in the ``source`` object, set the ``auth`` object's ``type``
              value to ``OAUTH`` .

            - **gitCloneDepth** *(integer) --*

              Information about the Git clone depth for the build project.

            - **gitSubmodulesConfig** *(dict) --*

              Information about the Git submodules configuration for the build project.

              - **fetchSubmodules** *(boolean) --*

                Set to true to fetch Git submodules for your AWS CodeBuild build project.

            - **buildspec** *(string) --*

              The build spec declaration to use for the builds in this build project.

              If this value is not specified, a build spec must be included along with the source
              code to be built.

            - **auth** *(dict) --*

              Information about the authorization settings for AWS CodeBuild to access the source
              code to be built.

              This information is for the AWS CodeBuild console's use only. Your code should not
              get or set this information directly.

              - **type** *(string) --*

                .. note::

                  This data type is deprecated and is no longer accurate or used.

                The authorization type to use. The only valid value is ``OAUTH`` , which represents
                the OAuth authorization type.

              - **resource** *(string) --*

                The resource value that applies to the specified authorization type.

            - **reportBuildStatus** *(boolean) --*

              Set to true to report the status of a build's start and finish to your source
              provider. This option is valid only when your source provider is GitHub, GitHub
              Enterprise, or Bitbucket. If this is set and you use a different source provider, an
              invalidInputException is thrown.

              .. note::

                The status of a build triggered by a webhook is always reported to your source
                provider.

            - **insecureSsl** *(boolean) --*

              Enable this flag to ignore SSL warnings while connecting to the project source code.

            - **sourceIdentifier** *(string) --*

              An identifier for this project source.

        - **secondarySourceVersions** *(list) --*

          An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name
          is specified, the branch's HEAD commit ID is used. If not specified, the default branch's
          HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
          of the source code you want to build. If a branch name is specified, the branch's HEAD
          commit ID is used. If not specified, the default branch's HEAD commit ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          - *(dict) --*

            A source identifier and its corresponding version.

            - **sourceIdentifier** *(string) --*

              An identifier for a source in the build project.

            - **sourceVersion** *(string) --*

              The source version for the corresponding source identifier. If specified, must be one
              of:

              * For AWS CodeCommit: the commit ID to use.

              * For GitHub: the commit ID, pull request ID, branch name, or tag name that
              corresponds to the version of the source code you want to build. If a pull request ID
              is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
              ). If a branch name is specified, the branch's HEAD commit ID is used. If not
              specified, the default branch's HEAD commit ID is used.

              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
              version of the source code you want to build. If a branch name is specified, the
              branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
              ID is used.

              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
              represents the build input ZIP file to use.

              For more information, see `Source Version Sample with CodeBuild
              <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
              in the *AWS CodeBuild User Guide* .

        - **artifacts** *(dict) --*

          Information about the output artifacts for the build.

          - **location** *(string) --*

            Information about the location of the build artifacts.

          - **sha256sum** *(string) --*

            The SHA-256 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **md5sum** *(string) --*

            The MD5 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Information that tells you if encryption for build artifacts is disabled.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

        - **secondaryArtifacts** *(list) --*

          An array of ``ProjectArtifacts`` objects.

          - *(dict) --*

            Information about build output artifacts.

            - **location** *(string) --*

              Information about the location of the build artifacts.

            - **sha256sum** *(string) --*

              The SHA-256 hash of the build artifact.

              You can use this hash along with a checksum tool to confirm file integrity and
              authenticity.

              .. note::

                This value is available only if the build project's ``packaging`` value is set to
                ``ZIP`` .

            - **md5sum** *(string) --*

              The MD5 hash of the build artifact.

              You can use this hash along with a checksum tool to confirm file integrity and
              authenticity.

              .. note::

                This value is available only if the build project's ``packaging`` value is set to
                ``ZIP`` .

            - **overrideArtifactName** *(boolean) --*

              If this flag is set, a name specified in the build spec file overrides the artifact
              name. The name specified in a build spec file is calculated at build time and uses
              the Shell Command Language. For example, you can append a date and time to your
              artifact name so that it is always unique.

            - **encryptionDisabled** *(boolean) --*

              Information that tells you if encryption for build artifacts is disabled.

            - **artifactIdentifier** *(string) --*

              An identifier for this artifact definition.

        - **cache** *(dict) --*

          Information about the cache for the build.

          - **type** *(string) --*

            The type of cache used by the build project. Valid values include:

            * ``NO_CACHE`` : The build project does not use any cache.

            * ``S3`` : The build project reads and writes from and to S3.

            * ``LOCAL`` : The build project stores a cache locally on a build host that is only
            available to that build host.

          - **location** *(string) --*

            Information about the cache location:

            * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

            * ``S3`` : This is the S3 bucket name/prefix.

          - **modes** *(list) --*

            If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
            modes at the same time.

            * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
            After the cache is created, subsequent builds pull only the change between commits.
            This mode is a good choice for projects with a clean working directory and a source
            that is a large Git repository. If you choose this option and your project does not use
            a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

            * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
            choice for projects that build or pull large Docker images. It can prevent the
            performance issues caused by pulling large Docker images down from the network.

            .. note::

                * You can use a Docker layer cache in the Linux environment only.

                * The ``privileged`` flag must be set so that your project has the required Docker
                permissions.

                * You should consider the security implications before you use a Docker layer cache.

            * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
            This mode is a good choice if your build scenario is not suited to one of the other
            three local cache modes. If you use a custom cache:

              * Only directories can be specified for caching. You cannot specify individual files.

              * Symlinks are used to reference cached directories.

              * Cached directories are linked to your build before it downloads its project
              sources. Cached items are overriden if a source item has the same name. Directories
              are specified using cache paths in the buildspec file.

            - *(string) --*

        - **environment** *(dict) --*

          Information about the build environment for this build.

          - **type** *(string) --*

            The type of build environment to use for related builds.

          - **image** *(string) --*

            The image tag or image digest that identifies the Docker image to use for this build
            project. Use the following formats:

            * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
            the tag "latest," use ``registry/repository:latest`` .

            * For an image digest: ``registry/repository@digest`` . For example, to specify an
            image with the digest
            "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
            ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
            .

          - **computeType** *(string) --*

            Information about the compute resources the build project uses. Available values
            include:

            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

            * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

            For more information, see `Build Environment Compute Types
            <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
            in the *AWS CodeBuild User Guide.*

          - **environmentVariables** *(list) --*

            A set of environment variables to make available to builds for this build project.

            - *(dict) --*

              Information about an environment variable for a build project or a build.

              - **name** *(string) --*

                The name or key of the environment variable.

              - **value** *(string) --*

                The value of the environment variable.

                .. warning::

                  We strongly discourage the use of environment variables to store sensitive
                  values, especially AWS secret key IDs and secret access keys. Environment
                  variables can be displayed in plain text using the AWS CodeBuild console and the
                  AWS Command Line Interface (AWS CLI).

              - **type** *(string) --*

                The type of environment variable. Valid values include:

                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                Manager Parameter Store.

                * ``PLAINTEXT`` : An environment variable in plaintext format.

                * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

          - **privilegedMode** *(boolean) --*

            Enables running the Docker daemon inside a Docker container. Set to true only if the
            build project is used to build Docker images. Otherwise, a build that attempts to
            interact with the Docker daemon fails. The default setting is ``false`` .

            You can initialize the Docker daemon during the install phase of your build by adding
            one of the following sets of commands to the install phase of your buildspec file:

            If the operating system's base image is Ubuntu Linux:

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

            If the operating system's base image is Alpine Linux and the previous command does not
            work, add the ``-t`` argument to ``timeout`` :

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

          - **certificate** *(string) --*

            The certificate to use with this build project.

          - **registryCredential** *(dict) --*

            The credentials for access to a private registry.

            - **credential** *(string) --*

              The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
              Manager.

              .. note::

                The ``credential`` can use the name of the credentials only if they exist in your
                current region.

            - **credentialProvider** *(string) --*

              The service that created the credentials to access a private Docker registry. The
              valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

          - **imagePullCredentialsType** *(string) --*

            The type of credentials AWS CodeBuild uses to pull images in your build. There are two
            valid values:

            * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
            that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

            * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

            When you use a cross-account or private registry image, you must use SERVICE_ROLE
            credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
            credentials.

        - **serviceRole** *(string) --*

          The name of a service role used for this build.

        - **logs** *(dict) --*

          Information about the build's logs in Amazon CloudWatch Logs.

          - **groupName** *(string) --*

            The name of the Amazon CloudWatch Logs group for the build logs.

          - **streamName** *(string) --*

            The name of the Amazon CloudWatch Logs stream for the build logs.

          - **deepLink** *(string) --*

            The URL to an individual build log in Amazon CloudWatch Logs.

          - **s3DeepLink** *(string) --*

            The URL to a build log in an S3 bucket.

          - **cloudWatchLogs** *(dict) --*

            Information about Amazon CloudWatch Logs for a build project.

            - **status** *(string) --*

              The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
              values are:

              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

            - **groupName** *(string) --*

              The group name of the logs in Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

            - **streamName** *(string) --*

              The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
              see `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

          - **s3Logs** *(dict) --*

            Information about S3 logs for a build project.

            - **status** *(string) --*

              The current status of the S3 build logs. Valid values are:

              * ``ENABLED`` : S3 build logs are enabled for this build project.

              * ``DISABLED`` : S3 build logs are not enabled for this build project.

            - **location** *(string) --*

              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
              name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
              formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your S3 build log output encrypted. By default S3
              build logs are encrypted.

        - **timeoutInMinutes** *(integer) --*

          How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does
          not get marked as completed.

        - **queuedTimeoutInMinutes** *(integer) --*

          The number of minutes a build is allowed to be queued before it times out.

        - **buildComplete** *(boolean) --*

          Whether the build is complete. True if complete; otherwise, false.

        - **initiator** *(string) --*

          The entity that started the build. Valid values include:

          * If AWS CodePipeline started the build, the pipeline's name (for example,
          ``codepipeline/my-demo-pipeline`` ).

          * If an AWS Identity and Access Management (IAM) user started the build, the user's name
          (for example, ``MyUserName`` ).

          * If the Jenkins plugin for AWS CodeBuild started the build, the string
          ``CodeBuild-Jenkins-Plugin`` .

        - **vpcConfig** *(dict) --*

          If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
          parameter that identifies the VPC ID and the list of security group IDs and subnet IDs.
          The security groups and subnets must belong to the same VPC. You must provide at least
          one security group and one subnet ID.

          - **vpcId** *(string) --*

            The ID of the Amazon VPC.

          - **subnets** *(list) --*

            A list of one or more subnet IDs in your Amazon VPC.

            - *(string) --*

          - **securityGroupIds** *(list) --*

            A list of one or more security groups IDs in your Amazon VPC.

            - *(string) --*

        - **networkInterface** *(dict) --*

          Describes a network interface.

          - **subnetId** *(string) --*

            The ID of the subnet.

          - **networkInterfaceId** *(string) --*

            The ID of the network interface.

        - **encryptionKey** *(string) --*

          The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
          encrypting the build output artifacts.

          .. note::

            You can use a cross-account KMS key to encrypt the build output artifacts if your
            service role has permission to that key.

          You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
          CMK's alias (using the format ``alias/*alias-name* `` ).

        - **exportedEnvironmentVariables** *(list) --*

          A list of exported environment variables for this build.

          - *(dict) --*

            Information about an exported environment variable.

            - **name** *(string) --*

              The name of this exported environment variable.

            - **value** *(string) --*

              The value assigned to this exported environment variable.

              .. note::

                During a build, the value of a variable is available starting with the ``install``
                phase. It can be updated between the start of the ``install`` phase and the end of
                the ``post_build`` phase. After the ``post_build`` phase ends, the value of
                exported variables cannot change.

    - **buildsNotFound** *(list) --*

      The IDs of builds for which information could not be found.

      - *(string) --*
    """


_ClientBatchGetProjectsResponseprojectsartifactsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsartifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsartifactsTypeDef(
    _ClientBatchGetProjectsResponseprojectsartifactsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `artifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service
      (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
      is not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      the output bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
      name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
        not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
      stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
      set the name to be a forward slash ("/"), the artifact is stored in the root of the
      output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to "``/`` ", the output artifact is stored in
      ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid
      only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
      set with another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientBatchGetProjectsResponseprojectsbadgeTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsbadgeTypeDef(
    _ClientBatchGetProjectsResponseprojectsbadgeTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `badge`

    Information about the build badge for the build project.

    - **badgeEnabled** *(boolean) --*

      Set this to true to generate a publicly accessible URL for your project's build badge.

    - **badgeRequestUrl** *(string) --*

      The publicly-accessible URL through which you can access the build badge for your
      project.

      The publicly accessible URL through which you can access the build badge for your
      project.
    """


_ClientBatchGetProjectsResponseprojectscacheTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectscacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientBatchGetProjectsResponseprojectscacheTypeDef(
    _ClientBatchGetProjectsResponseprojectscacheTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `cache`

    Information about the cache for the build project.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits.
      This mode is a good choice for projects with a clean working directory and a source
      that is a large Git repository. If you choose this option and your project does not use
      a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
      This mode is a good choice if your build scenario is not suited to one of the other
      three local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project
        sources. Cached items are overriden if a source item has the same name. Directories
        are specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectsenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive
        values, especially AWS secret key IDs and secret access keys. Environment
        variables can be displayed in plain text using the AWS CodeBuild console and the
        AWS Command Line Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
      Manager Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectsenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
      Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The
      valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientBatchGetProjectsResponseprojectsenvironmentTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `environment`

    Information about the build environment for this build project.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an
      image with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values
      include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive
            values, especially AWS secret key IDs and secret access keys. Environment
            variables can be displayed in plain text using the AWS CodeBuild console and the
            AWS Command Line Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
          Manager Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding
      one of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
        Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The
        valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
      that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectslogsConfig` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs
    are enabled by default.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
      see `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectslogsConfig` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not
    enabled by default.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
      name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
      formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3
      build logs are encrypted.
    """


_ClientBatchGetProjectsResponseprojectslogsConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `logsConfig`

    Information about logs for the build project. A project can create logs in Amazon
    CloudWatch Logs, an S3 bucket, or both.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs
      are enabled by default.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
        see `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not
      enabled by default.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
        name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
        formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3
        build logs are encrypted.
    """


_ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `secondaryArtifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service
      (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations
      instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
      because no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
      name and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
      because no build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
      is not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
      in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
      the name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
      because no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
        is not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
      stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
      name and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
      because no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
      you set the name to be a forward slash ("/"), the artifact is stored in the root of
      the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to "``/`` ", the output artifact is stored in
      ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts
      instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
      because no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses
      the Shell Command Language. For example, you can append a date and time to your
      artifact name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid
      only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
      set with another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that
      corresponds to the version of the source code you want to build. If a pull request ID
      is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
      ). If a branch name is specified, the branch's HEAD commit ID is used. If not
      specified, the default branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
      ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectssecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not
    get or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectssecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values
      include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in
      AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
      of the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
      that contains the source and the build spec. You must connect your AWS account to
      your Bitbucket account. Use the AWS CodeBuild console to start creating a build
      project. When you use the console to connect (or reconnect) with Bitbucket, on the
      Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
      you have connected to your Bitbucket account, you do not need to finish creating the
      build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
      use this connection, in the ``source`` object, set the ``auth`` object's ``type``
      value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not
      get or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source
      provider. This option is valid only when your source provider is GitHub, GitHub
      Enterprise, or Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientBatchGetProjectsResponseprojectssourceauthTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourceauthTypeDef(
    _ClientBatchGetProjectsResponseprojectssourceauthTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectssource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectssource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientBatchGetProjectsResponseprojectssourceTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourceTypeDef(
    _ClientBatchGetProjectsResponseprojectssourceTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `source`

    Information about the build input source code for this build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientBatchGetProjectsResponseprojectstagsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectstagsTypeDef(
    _ClientBatchGetProjectsResponseprojectstagsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `tags`

    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS CodeBuild.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `vpcConfig`

    Information about the VPC configuration that AWS CodeBuild accesses.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef",
    {"type": str, "pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef(
    _ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojectswebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --*

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of
      four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED``
      , and ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
      comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
      PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
      updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
      account ID matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
      ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
      request, Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular
      expression ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --*

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
      specifies one or more events. For example, the webhook filter ``PUSH,
      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
      created, and pull request updated events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular
      expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for
      its ``type`` and the pattern ``^refs/heads/`` triggers a build when the head
      reference is a branch with a reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not
      trigger a build. If true, then a webhook event that does not match the
      ``pattern`` triggers a build. If false, then a webhook event that matches the
      ``pattern`` triggers a build.
    """


_ClientBatchGetProjectsResponseprojectswebhookTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectswebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectswebhookTypeDef(
    _ClientBatchGetProjectsResponseprojectswebhookTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponseprojects` `webhook`

    Information about a webhook that connects repository events to a build project in AWS
    CodeBuild.

    - **url** *(string) --*

      The URL to the webhook.

    - **payloadUrl** *(string) --*

      The AWS CodeBuild endpoint where webhook events are sent.

    - **secret** *(string) --*

      The secret token of the associated repository.

      .. note::

        A Bitbucket webhook does not support ``secret`` .

    - **branchFilter** *(string) --*

      A regular expression used to determine which repository branches are built when a
      webhook is triggered. If the name of a branch matches the regular expression, then it
      is built. If ``branchFilter`` is empty, then all branches are built.

      .. note::

        It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

    - **filterGroups** *(list) --*

      An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
      triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
      ``type`` .

      For a build to be triggered, at least one filter group in the ``filterGroups`` array
      must pass. For a filter group to pass, each of its filters must pass.

      - *(list) --*

        - *(dict) --*

          A filter used to determine which webhooks trigger a build.

          - **type** *(string) --*

            The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
            ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

              EVENT

            A webhook event triggers a build when the provided ``pattern`` matches one of
            four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED``
            , and ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
            comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
            PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
            updated events.

            .. note::

              The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

              ACTOR_ACCOUNT_ID

            A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
            account ID matches the regular expression ``pattern`` .

              HEAD_REF

            A webhook event triggers a build when the head reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` and
            ``refs/tags/tag-name`` .

            Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
            request, Bitbucket push, and Bitbucket pull request events.

              BASE_REF

            A webhook event triggers a build when the base reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` .

            .. note::

              Works with pull request events only.

              FILE_PATH

            A webhook triggers a build when the path of a changed file matches the regular
            expression ``pattern`` .

            .. note::

              Works with GitHub and GitHub Enterprise push events only.

          - **pattern** *(string) --*

            For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
            specifies one or more events. For example, the webhook filter ``PUSH,
            PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
            created, and pull request updated events to trigger a build.

            For a ``WebHookFilter`` that uses any of the other filter types, a regular
            expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for
            its ``type`` and the pattern ``^refs/heads/`` triggers a build when the head
            reference is a branch with a reference name ``refs/heads/branch-name`` .

          - **excludeMatchedPattern** *(boolean) --*

            Used to indicate that the ``pattern`` determines which webhook events do not
            trigger a build. If true, then a webhook event that does not match the
            ``pattern`` triggers a build. If false, then a webhook event that matches the
            ``pattern`` triggers a build.

    - **lastModifiedSecret** *(datetime) --*

      A timestamp that indicates the last time a repository's secret token was modified.
    """


_ClientBatchGetProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientBatchGetProjectsResponseprojectssourceTypeDef,
        "secondarySources": List[
            ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef
        ],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetProjectsResponseprojectsartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef
        ],
        "cache": ClientBatchGetProjectsResponseprojectscacheTypeDef,
        "environment": ClientBatchGetProjectsResponseprojectsenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientBatchGetProjectsResponseprojectstagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientBatchGetProjectsResponseprojectswebhookTypeDef,
        "vpcConfig": ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef,
        "badge": ClientBatchGetProjectsResponseprojectsbadgeTypeDef,
        "logsConfig": ClientBatchGetProjectsResponseprojectslogsConfigTypeDef,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsTypeDef(
    _ClientBatchGetProjectsResponseprojectsTypeDef
):
    """
    Type definition for `ClientBatchGetProjectsResponse` `projects`

    Information about a build project.

    - **name** *(string) --*

      The name of the build project.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build project.

    - **description** *(string) --*

      A description that makes the build project easy to identify.

    - **source** *(dict) --*

      Information about the build input source code for this build project.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS
        CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
        pipeline's source action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
        repository that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, ``
          *bucket-name* /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        GitHub account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to
        each repository you want to allow AWS CodeBuild to have access to, and then choose
        **Authorize application** . (After you have connected to your GitHub account, you do
        not need to finish creating the build project. You can leave the AWS CodeBuild
        console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
        set the ``auth`` object's ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
        When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
        **Confirm access to your account** page, choose **Grant access** . (After you have
        connected to your Bitbucket account, you do not need to finish creating the build
        project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
        this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
        ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source
        code to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source
        code to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get
        or set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents
          the OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source
          provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values
          include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in
          AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
          of the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
          that contains the source and the build spec. You must connect your AWS account to
          your Bitbucket account. Use the AWS CodeBuild console to start creating a build
          project. When you use the console to connect (or reconnect) with Bitbucket, on the
          Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
          you have connected to your Bitbucket account, you do not need to finish creating the
          build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
          use this connection, in the ``source`` object, set the ``auth`` object's ``type``
          value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not
          get or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source
          provider. This option is valid only when your source provider is GitHub, GitHub
          Enterprise, or Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **sourceVersion** *(string) --*

      A version of the build input to be built for this project. If not specified, the latest
      version is used. If specified, it must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name
      is specified, the branch's HEAD commit ID is used. If not specified, the default branch's
      HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
      of the source code you want to build. If a branch name is specified, the branch's HEAD
      commit ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      If ``sourceVersion`` is specified at the build level, then that version takes precedence
      over this ``sourceVersion`` (at the project level).

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
      at the build level, then they take over these ``secondarySourceVersions`` (at the project
      level).

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that
          corresponds to the version of the source code you want to build. If a pull request ID
          is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
          ). If a branch name is specified, the branch's HEAD commit ID is used. If not
          specified, the default branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
          ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the build output artifacts for the build project.

      - **type** *(string) --*

        The type of build output artifact. Valid values include:

        * ``CODEPIPELINE`` : The build project has build output generated through AWS
        CodePipeline.

        .. note::

           The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

        * ``NO_ARTIFACTS`` : The build project does not produce any build output.

        * ``S3`` : The build project stores build output in Amazon Simple Storage Service
        (Amazon S3).

      - **location** *(string) --*

        Information about the build output artifact location:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output locations instead
        of AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
        no build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output bucket.

      - **path** *(string) --*

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
        no build output is produced.

        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
        is not specified, ``path`` is not used.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
        ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
        the output bucket at ``MyArtifacts/MyArtifact.zip`` .

      - **namespaceType** *(string) --*

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
        name and location to store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
        no build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
          not specified.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
        ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
        stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      - **name** *(string) --*

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
        no build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
        set the name to be a forward slash ("/"), the artifact is stored in the root of the
        output bucket.

        For example:

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
        and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
        ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
        "``/`` ", the output artifact is stored in the root of the output bucket.

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
        and ``name`` is set to "``/`` ", the output artifact is stored in
        ``MyArtifacts/*build-ID* `` .

      - **packaging** *(string) --*

        The type of build output artifact to create:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output artifacts instead
        of AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
        no build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
          build output. This is the default if ``packaging`` is not specified.

          * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
          build output.

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact
        name. The name specified in a build spec file is calculated at build time and uses the
        Shell Command Language. For example, you can append a date and time to your artifact
        name so that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your output artifacts encrypted. This option is valid
        only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
        set with another artifacts type, an invalidInputException is thrown.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about the build output artifacts for the build project.

        - **type** *(string) --*

          The type of build output artifact. Valid values include:

          * ``CODEPIPELINE`` : The build project has build output generated through AWS
          CodePipeline.

          .. note::

             The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

          * ``NO_ARTIFACTS`` : The build project does not produce any build output.

          * ``S3`` : The build project stores build output in Amazon Simple Storage Service
          (Amazon S3).

        - **location** *(string) --*

          Information about the build output artifact location:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output locations
          instead of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
          because no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output bucket.

        - **path** *(string) --*

          Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
          name and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
          because no build output is produced.

          * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
          is not specified, ``path`` is not used.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
          in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        - **namespaceType** *(string) --*

          Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
          the name and location to store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
          because no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

            * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
            is not specified.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
          stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        - **name** *(string) --*

          Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
          name and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
          because no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
          you set the name to be a forward slash ("/"), the artifact is stored in the root of
          the output bucket.

          For example:

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
          ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
          "``/`` ", the output artifact is stored in the root of the output bucket.

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to "``/`` ", the output artifact is stored in
          ``MyArtifacts/*build-ID* `` .

        - **packaging** *(string) --*

          The type of build output artifact to create:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output artifacts
          instead of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
          because no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
            build output. This is the default if ``packaging`` is not specified.

            * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
            build output.

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses
          the Shell Command Language. For example, you can append a date and time to your
          artifact name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your output artifacts encrypted. This option is valid
          only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
          set with another artifacts type, an invalidInputException is thrown.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build project.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits.
        This mode is a good choice for projects with a clean working directory and a source
        that is a large Git repository. If you choose this option and your project does not use
        a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
        This mode is a good choice if your build scenario is not suited to one of the other
        three local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project
          sources. Cached items are overriden if a source item has the same name. Directories
          are specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build project.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an
        image with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values
        include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive
              values, especially AWS secret key IDs and secret access keys. Environment
              variables can be displayed in plain text using the AWS CodeBuild console and the
              AWS Command Line Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
            Manager Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding
        one of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
          Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The
          valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
        that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild
      to interact with dependent AWS services on behalf of the AWS account.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing
      out any related build that did not get marked as completed. The default is 60 minutes.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your
        service role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **tags** *(list) --*

      The tags for this build project.

      These tags are available for use by AWS services that support AWS CodeBuild build project
      tags.

      - *(dict) --*

        A tag, consisting of a key and a value.

        This tag is available for use by AWS services that support tags in AWS CodeBuild.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.

    - **created** *(datetime) --*

      When the build project was created, expressed in Unix time format.

    - **lastModified** *(datetime) --*

      When the build project's settings were last modified, expressed in Unix time format.

    - **webhook** *(dict) --*

      Information about a webhook that connects repository events to a build project in AWS
      CodeBuild.

      - **url** *(string) --*

        The URL to the webhook.

      - **payloadUrl** *(string) --*

        The AWS CodeBuild endpoint where webhook events are sent.

      - **secret** *(string) --*

        The secret token of the associated repository.

        .. note::

          A Bitbucket webhook does not support ``secret`` .

      - **branchFilter** *(string) --*

        A regular expression used to determine which repository branches are built when a
        webhook is triggered. If the name of a branch matches the regular expression, then it
        is built. If ``branchFilter`` is empty, then all branches are built.

        .. note::

          It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

      - **filterGroups** *(list) --*

        An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
        triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
        ``type`` .

        For a build to be triggered, at least one filter group in the ``filterGroups`` array
        must pass. For a filter group to pass, each of its filters must pass.

        - *(list) --*

          - *(dict) --*

            A filter used to determine which webhooks trigger a build.

            - **type** *(string) --*

              The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
              ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                EVENT

              A webhook event triggers a build when the provided ``pattern`` matches one of
              four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED``
              , and ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
              comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
              PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
              updated events.

              .. note::

                The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                ACTOR_ACCOUNT_ID

              A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
              account ID matches the regular expression ``pattern`` .

                HEAD_REF

              A webhook event triggers a build when the head reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` and
              ``refs/tags/tag-name`` .

              Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
              request, Bitbucket push, and Bitbucket pull request events.

                BASE_REF

              A webhook event triggers a build when the base reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` .

              .. note::

                Works with pull request events only.

                FILE_PATH

              A webhook triggers a build when the path of a changed file matches the regular
              expression ``pattern`` .

              .. note::

                Works with GitHub and GitHub Enterprise push events only.

            - **pattern** *(string) --*

              For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
              specifies one or more events. For example, the webhook filter ``PUSH,
              PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
              created, and pull request updated events to trigger a build.

              For a ``WebHookFilter`` that uses any of the other filter types, a regular
              expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for
              its ``type`` and the pattern ``^refs/heads/`` triggers a build when the head
              reference is a branch with a reference name ``refs/heads/branch-name`` .

            - **excludeMatchedPattern** *(boolean) --*

              Used to indicate that the ``pattern`` determines which webhook events do not
              trigger a build. If true, then a webhook event that does not match the
              ``pattern`` triggers a build. If false, then a webhook event that matches the
              ``pattern`` triggers a build.

      - **lastModifiedSecret** *(datetime) --*

        A timestamp that indicates the last time a repository's secret token was modified.

    - **vpcConfig** *(dict) --*

      Information about the VPC configuration that AWS CodeBuild accesses.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **badge** *(dict) --*

      Information about the build badge for the build project.

      - **badgeEnabled** *(boolean) --*

        Set this to true to generate a publicly accessible URL for your project's build badge.

      - **badgeRequestUrl** *(string) --*

        The publicly-accessible URL through which you can access the build badge for your
        project.

        The publicly accessible URL through which you can access the build badge for your
        project.

    - **logsConfig** *(dict) --*

      Information about logs for the build project. A project can create logs in Amazon
      CloudWatch Logs, an S3 bucket, or both.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs
        are enabled by default.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
          see `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about logs built to an S3 bucket for a build project. S3 logs are not
        enabled by default.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
          name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
          formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3
          build logs are encrypted.
    """


_ClientBatchGetProjectsResponseTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseTypeDef",
    {
        "projects": List[ClientBatchGetProjectsResponseprojectsTypeDef],
        "projectsNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetProjectsResponseTypeDef(_ClientBatchGetProjectsResponseTypeDef):
    """
    Type definition for `ClientBatchGetProjects` `Response`

    - **projects** *(list) --*

      Information about the requested build projects.

      - *(dict) --*

        Information about a build project.

        - **name** *(string) --*

          The name of the build project.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the build project.

        - **description** *(string) --*

          A description that makes the build project easy to identify.

        - **source** *(dict) --*

          Information about the build input source code for this build project.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

        - **secondarySources** *(list) --*

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build input source code for the build project.

            - **type** *(string) --*

              The type of repository that contains the source code to be built. Valid values
              include:

              * ``BITBUCKET`` : The source code is in a Bitbucket repository.

              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
              pipeline in AWS CodePipeline.

              * ``GITHUB`` : The source code is in a GitHub repository.

              * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

              * ``NO_SOURCE`` : The project does not have input source code.

              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
              bucket.

            - **location** *(string) --*

              Information about the location of the source code to be built. Valid values include:

              * For source code settings that are specified in the source action of a pipeline in
              AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
              CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
              pipeline's source action instead of this value.

              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
              repository that contains the source code and the build spec (for example,
              ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one
              of the following.

                * The path to the ZIP file that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                * The path to the folder that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

              * For source code in a GitHub repository, the HTTPS clone URL to the repository that
              contains the source and the build spec. You must connect your AWS account to your
              GitHub account. Use the AWS CodeBuild console to start creating a build project. When
              you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
              application** page, for **Organization access** , choose **Request access** next to
              each repository you want to allow AWS CodeBuild to have access to, and then choose
              **Authorize application** . (After you have connected to your GitHub account, you do
              not need to finish creating the build project. You can leave the AWS CodeBuild
              console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
              set the ``auth`` object's ``type`` value to ``OAUTH`` .

              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
              that contains the source and the build spec. You must connect your AWS account to
              your Bitbucket account. Use the AWS CodeBuild console to start creating a build
              project. When you use the console to connect (or reconnect) with Bitbucket, on the
              Bitbucket **Confirm access to your account** page, choose **Grant access** . (After
              you have connected to your Bitbucket account, you do not need to finish creating the
              build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
              use this connection, in the ``source`` object, set the ``auth`` object's ``type``
              value to ``OAUTH`` .

            - **gitCloneDepth** *(integer) --*

              Information about the Git clone depth for the build project.

            - **gitSubmodulesConfig** *(dict) --*

              Information about the Git submodules configuration for the build project.

              - **fetchSubmodules** *(boolean) --*

                Set to true to fetch Git submodules for your AWS CodeBuild build project.

            - **buildspec** *(string) --*

              The build spec declaration to use for the builds in this build project.

              If this value is not specified, a build spec must be included along with the source
              code to be built.

            - **auth** *(dict) --*

              Information about the authorization settings for AWS CodeBuild to access the source
              code to be built.

              This information is for the AWS CodeBuild console's use only. Your code should not
              get or set this information directly.

              - **type** *(string) --*

                .. note::

                  This data type is deprecated and is no longer accurate or used.

                The authorization type to use. The only valid value is ``OAUTH`` , which represents
                the OAuth authorization type.

              - **resource** *(string) --*

                The resource value that applies to the specified authorization type.

            - **reportBuildStatus** *(boolean) --*

              Set to true to report the status of a build's start and finish to your source
              provider. This option is valid only when your source provider is GitHub, GitHub
              Enterprise, or Bitbucket. If this is set and you use a different source provider, an
              invalidInputException is thrown.

              .. note::

                The status of a build triggered by a webhook is always reported to your source
                provider.

            - **insecureSsl** *(boolean) --*

              Enable this flag to ignore SSL warnings while connecting to the project source code.

            - **sourceIdentifier** *(string) --*

              An identifier for this project source.

        - **sourceVersion** *(string) --*

          A version of the build input to be built for this project. If not specified, the latest
          version is used. If specified, it must be one of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name
          is specified, the branch's HEAD commit ID is used. If not specified, the default branch's
          HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
          of the source code you want to build. If a branch name is specified, the branch's HEAD
          commit ID is used. If not specified, the default branch's HEAD commit ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          If ``sourceVersion`` is specified at the build level, then that version takes precedence
          over this ``sourceVersion`` (at the project level).

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
          the *AWS CodeBuild User Guide* .

        - **secondarySourceVersions** *(list) --*

          An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
          at the build level, then they take over these ``secondarySourceVersions`` (at the project
          level).

          - *(dict) --*

            A source identifier and its corresponding version.

            - **sourceIdentifier** *(string) --*

              An identifier for a source in the build project.

            - **sourceVersion** *(string) --*

              The source version for the corresponding source identifier. If specified, must be one
              of:

              * For AWS CodeCommit: the commit ID to use.

              * For GitHub: the commit ID, pull request ID, branch name, or tag name that
              corresponds to the version of the source code you want to build. If a pull request ID
              is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25``
              ). If a branch name is specified, the branch's HEAD commit ID is used. If not
              specified, the default branch's HEAD commit ID is used.

              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
              version of the source code you want to build. If a branch name is specified, the
              branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
              ID is used.

              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
              represents the build input ZIP file to use.

              For more information, see `Source Version Sample with CodeBuild
              <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
              in the *AWS CodeBuild User Guide* .

        - **artifacts** *(dict) --*

          Information about the build output artifacts for the build project.

          - **type** *(string) --*

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
            is not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
            stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to "``/`` ", the output artifact is stored in
            ``MyArtifacts/*build-ID* `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
            set with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

        - **secondaryArtifacts** *(list) --*

          An array of ``ProjectArtifacts`` objects.

          - *(dict) --*

            Information about the build output artifacts for the build project.

            - **type** *(string) --*

              The type of build output artifact. Valid values include:

              * ``CODEPIPELINE`` : The build project has build output generated through AWS
              CodePipeline.

              .. note::

                 The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

              * ``NO_ARTIFACTS`` : The build project does not produce any build output.

              * ``S3`` : The build project stores build output in Amazon Simple Storage Service
              (Amazon S3).

            - **location** *(string) --*

              Information about the build output artifact location:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output locations
              instead of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
              because no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output bucket.

            - **path** *(string) --*

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
              because no build output is produced.

              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
              is not specified, ``path`` is not used.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
              in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

            - **namespaceType** *(string) --*

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
              the name and location to store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
              because no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
                is not specified.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
              stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            - **name** *(string) --*

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
              because no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
              you set the name to be a forward slash ("/"), the artifact is stored in the root of
              the output bucket.

              For example:

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
              ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
              "``/`` ", the output artifact is stored in the root of the output bucket.

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to "``/`` ", the output artifact is stored in
              ``MyArtifacts/*build-ID* `` .

            - **packaging** *(string) --*

              The type of build output artifact to create:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output artifacts
              instead of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
              because no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
                build output. This is the default if ``packaging`` is not specified.

                * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
                build output.

            - **overrideArtifactName** *(boolean) --*

              If this flag is set, a name specified in the build spec file overrides the artifact
              name. The name specified in a build spec file is calculated at build time and uses
              the Shell Command Language. For example, you can append a date and time to your
              artifact name so that it is always unique.

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your output artifacts encrypted. This option is valid
              only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
              set with another artifacts type, an invalidInputException is thrown.

            - **artifactIdentifier** *(string) --*

              An identifier for this artifact definition.

        - **cache** *(dict) --*

          Information about the cache for the build project.

          - **type** *(string) --*

            The type of cache used by the build project. Valid values include:

            * ``NO_CACHE`` : The build project does not use any cache.

            * ``S3`` : The build project reads and writes from and to S3.

            * ``LOCAL`` : The build project stores a cache locally on a build host that is only
            available to that build host.

          - **location** *(string) --*

            Information about the cache location:

            * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

            * ``S3`` : This is the S3 bucket name/prefix.

          - **modes** *(list) --*

            If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
            modes at the same time.

            * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
            After the cache is created, subsequent builds pull only the change between commits.
            This mode is a good choice for projects with a clean working directory and a source
            that is a large Git repository. If you choose this option and your project does not use
            a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

            * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
            choice for projects that build or pull large Docker images. It can prevent the
            performance issues caused by pulling large Docker images down from the network.

            .. note::

                * You can use a Docker layer cache in the Linux environment only.

                * The ``privileged`` flag must be set so that your project has the required Docker
                permissions.

                * You should consider the security implications before you use a Docker layer cache.

            * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file.
            This mode is a good choice if your build scenario is not suited to one of the other
            three local cache modes. If you use a custom cache:

              * Only directories can be specified for caching. You cannot specify individual files.

              * Symlinks are used to reference cached directories.

              * Cached directories are linked to your build before it downloads its project
              sources. Cached items are overriden if a source item has the same name. Directories
              are specified using cache paths in the buildspec file.

            - *(string) --*

        - **environment** *(dict) --*

          Information about the build environment for this build project.

          - **type** *(string) --*

            The type of build environment to use for related builds.

          - **image** *(string) --*

            The image tag or image digest that identifies the Docker image to use for this build
            project. Use the following formats:

            * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
            the tag "latest," use ``registry/repository:latest`` .

            * For an image digest: ``registry/repository@digest`` . For example, to specify an
            image with the digest
            "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
            ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
            .

          - **computeType** *(string) --*

            Information about the compute resources the build project uses. Available values
            include:

            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

            * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

            For more information, see `Build Environment Compute Types
            <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
            in the *AWS CodeBuild User Guide.*

          - **environmentVariables** *(list) --*

            A set of environment variables to make available to builds for this build project.

            - *(dict) --*

              Information about an environment variable for a build project or a build.

              - **name** *(string) --*

                The name or key of the environment variable.

              - **value** *(string) --*

                The value of the environment variable.

                .. warning::

                  We strongly discourage the use of environment variables to store sensitive
                  values, especially AWS secret key IDs and secret access keys. Environment
                  variables can be displayed in plain text using the AWS CodeBuild console and the
                  AWS Command Line Interface (AWS CLI).

              - **type** *(string) --*

                The type of environment variable. Valid values include:

                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                Manager Parameter Store.

                * ``PLAINTEXT`` : An environment variable in plaintext format.

                * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

          - **privilegedMode** *(boolean) --*

            Enables running the Docker daemon inside a Docker container. Set to true only if the
            build project is used to build Docker images. Otherwise, a build that attempts to
            interact with the Docker daemon fails. The default setting is ``false`` .

            You can initialize the Docker daemon during the install phase of your build by adding
            one of the following sets of commands to the install phase of your buildspec file:

            If the operating system's base image is Ubuntu Linux:

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

            If the operating system's base image is Alpine Linux and the previous command does not
            work, add the ``-t`` argument to ``timeout`` :

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

          - **certificate** *(string) --*

            The certificate to use with this build project.

          - **registryCredential** *(dict) --*

            The credentials for access to a private registry.

            - **credential** *(string) --*

              The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
              Manager.

              .. note::

                The ``credential`` can use the name of the credentials only if they exist in your
                current region.

            - **credentialProvider** *(string) --*

              The service that created the credentials to access a private Docker registry. The
              valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

          - **imagePullCredentialsType** *(string) --*

            The type of credentials AWS CodeBuild uses to pull images in your build. There are two
            valid values:

            * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
            that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

            * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

            When you use a cross-account or private registry image, you must use SERVICE_ROLE
            credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
            credentials.

        - **serviceRole** *(string) --*

          The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild
          to interact with dependent AWS services on behalf of the AWS account.

        - **timeoutInMinutes** *(integer) --*

          How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing
          out any related build that did not get marked as completed. The default is 60 minutes.

        - **queuedTimeoutInMinutes** *(integer) --*

          The number of minutes a build is allowed to be queued before it times out.

        - **encryptionKey** *(string) --*

          The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
          encrypting the build output artifacts.

          .. note::

            You can use a cross-account KMS key to encrypt the build output artifacts if your
            service role has permission to that key.

          You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
          CMK's alias (using the format ``alias/*alias-name* `` ).

        - **tags** *(list) --*

          The tags for this build project.

          These tags are available for use by AWS services that support AWS CodeBuild build project
          tags.

          - *(dict) --*

            A tag, consisting of a key and a value.

            This tag is available for use by AWS services that support tags in AWS CodeBuild.

            - **key** *(string) --*

              The tag's key.

            - **value** *(string) --*

              The tag's value.

        - **created** *(datetime) --*

          When the build project was created, expressed in Unix time format.

        - **lastModified** *(datetime) --*

          When the build project's settings were last modified, expressed in Unix time format.

        - **webhook** *(dict) --*

          Information about a webhook that connects repository events to a build project in AWS
          CodeBuild.

          - **url** *(string) --*

            The URL to the webhook.

          - **payloadUrl** *(string) --*

            The AWS CodeBuild endpoint where webhook events are sent.

          - **secret** *(string) --*

            The secret token of the associated repository.

            .. note::

              A Bitbucket webhook does not support ``secret`` .

          - **branchFilter** *(string) --*

            A regular expression used to determine which repository branches are built when a
            webhook is triggered. If the name of a branch matches the regular expression, then it
            is built. If ``branchFilter`` is empty, then all branches are built.

            .. note::

              It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

          - **filterGroups** *(list) --*

            An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
            triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
            ``type`` .

            For a build to be triggered, at least one filter group in the ``filterGroups`` array
            must pass. For a filter group to pass, each of its filters must pass.

            - *(list) --*

              - *(dict) --*

                A filter used to determine which webhooks trigger a build.

                - **type** *(string) --*

                  The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                  ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                    EVENT

                  A webhook event triggers a build when the provided ``pattern`` matches one of
                  four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED``
                  , and ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
                  comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
                  PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
                  updated events.

                  .. note::

                    The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                    ACTOR_ACCOUNT_ID

                  A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
                  account ID matches the regular expression ``pattern`` .

                    HEAD_REF

                  A webhook event triggers a build when the head reference matches the regular
                  expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                  ``refs/tags/tag-name`` .

                  Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
                  request, Bitbucket push, and Bitbucket pull request events.

                    BASE_REF

                  A webhook event triggers a build when the base reference matches the regular
                  expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                  .. note::

                    Works with pull request events only.

                    FILE_PATH

                  A webhook triggers a build when the path of a changed file matches the regular
                  expression ``pattern`` .

                  .. note::

                    Works with GitHub and GitHub Enterprise push events only.

                - **pattern** *(string) --*

                  For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
                  specifies one or more events. For example, the webhook filter ``PUSH,
                  PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                  created, and pull request updated events to trigger a build.

                  For a ``WebHookFilter`` that uses any of the other filter types, a regular
                  expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for
                  its ``type`` and the pattern ``^refs/heads/`` triggers a build when the head
                  reference is a branch with a reference name ``refs/heads/branch-name`` .

                - **excludeMatchedPattern** *(boolean) --*

                  Used to indicate that the ``pattern`` determines which webhook events do not
                  trigger a build. If true, then a webhook event that does not match the
                  ``pattern`` triggers a build. If false, then a webhook event that matches the
                  ``pattern`` triggers a build.

          - **lastModifiedSecret** *(datetime) --*

            A timestamp that indicates the last time a repository's secret token was modified.

        - **vpcConfig** *(dict) --*

          Information about the VPC configuration that AWS CodeBuild accesses.

          - **vpcId** *(string) --*

            The ID of the Amazon VPC.

          - **subnets** *(list) --*

            A list of one or more subnet IDs in your Amazon VPC.

            - *(string) --*

          - **securityGroupIds** *(list) --*

            A list of one or more security groups IDs in your Amazon VPC.

            - *(string) --*

        - **badge** *(dict) --*

          Information about the build badge for the build project.

          - **badgeEnabled** *(boolean) --*

            Set this to true to generate a publicly accessible URL for your project's build badge.

          - **badgeRequestUrl** *(string) --*

            The publicly-accessible URL through which you can access the build badge for your
            project.

            The publicly accessible URL through which you can access the build badge for your
            project.

        - **logsConfig** *(dict) --*

          Information about logs for the build project. A project can create logs in Amazon
          CloudWatch Logs, an S3 bucket, or both.

          - **cloudWatchLogs** *(dict) --*

            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs
            are enabled by default.

            - **status** *(string) --*

              The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
              values are:

              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

            - **groupName** *(string) --*

              The group name of the logs in Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

            - **streamName** *(string) --*

              The prefix of the stream name of the Amazon CloudWatch Logs. For more information,
              see `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

          - **s3Logs** *(dict) --*

            Information about logs built to an S3 bucket for a build project. S3 logs are not
            enabled by default.

            - **status** *(string) --*

              The current status of the S3 build logs. Valid values are:

              * ``ENABLED`` : S3 build logs are enabled for this build project.

              * ``DISABLED`` : S3 build logs are not enabled for this build project.

            - **location** *(string) --*

              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket
              name is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable
              formats are ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your S3 build log output encrypted. By default S3
              build logs are encrypted.

    - **projectsNotFound** *(list) --*

      The names of build projects for which information could not be found.

      - *(string) --*
    """


_ClientCreateProjectResponseprojectartifactsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectartifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectartifactsTypeDef(
    _ClientCreateProjectResponseprojectartifactsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `artifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
      S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
      not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
      , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
      bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
      name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
        not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
      in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
      set the name to be a forward slash ("/"), the artifact is stored in the root of the
      output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
      .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name.
      The name specified in a build spec file is calculated at build time and uses the Shell
      Command Language. For example, you can append a date and time to your artifact name so
      that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only
      if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
      another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientCreateProjectResponseprojectbadgeTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientCreateProjectResponseprojectbadgeTypeDef(
    _ClientCreateProjectResponseprojectbadgeTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `badge`

    Information about the build badge for the build project.

    - **badgeEnabled** *(boolean) --*

      Set this to true to generate a publicly accessible URL for your project's build badge.

    - **badgeRequestUrl** *(string) --*

      The publicly-accessible URL through which you can access the build badge for your project.

      The publicly accessible URL through which you can access the build badge for your project.
    """


_ClientCreateProjectResponseprojectcacheTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectcacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientCreateProjectResponseprojectcacheTypeDef(
    _ClientCreateProjectResponseprojectcacheTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `cache`

    Information about the cache for the build project.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits. This
      mode is a good choice for projects with a clean working directory and a source that is a
      large Git repository. If you choose this option and your project does not use a Git
      repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
      mode is a good choice if your build scenario is not suited to one of the other three
      local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources.
        Cached items are overriden if a source item has the same name. Directories are
        specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef(
    _ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef(
    _ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientCreateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentTypeDef(
    _ClientCreateProjectResponseprojectenvironmentTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `environment`

    Information about the build environment for this build project.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image
      with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one
      of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
      you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectlogsConfig` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
    enabled by default.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectlogsConfig` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
    by default.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
      is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build
      logs are encrypted.
    """


_ClientCreateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `logsConfig`

    Information about logs for the build project. A project can create logs in Amazon
    CloudWatch Logs, an S3 bucket, or both.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
      by default.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
        is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build
        logs are encrypted.
    """


_ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef(
    _ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `secondaryArtifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service
      (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
      is not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      the output bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
      name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
        not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
      stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
      set the name to be a forward slash ("/"), the artifact is stored in the root of the
      output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to "``/`` ", the output artifact is stored in
      ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid
      only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
      set with another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
      name is specified, the branch's HEAD commit ID is used. If not specified, the default
      branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
      is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientCreateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientCreateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientCreateProjectResponseprojectsourceauthTypeDef(
    _ClientCreateProjectResponseprojectsourceauthTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code
    to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or
    set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef(
    _ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientCreateProjectResponseprojectsourceTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsourceTypeDef(
    _ClientCreateProjectResponseprojectsourceTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `source`

    Information about the build input source code for this build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
      action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
      that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your GitHub
      account. Use the AWS CodeBuild console to start creating a build project. When you use
      the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to each
      repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
      application** . (After you have connected to your GitHub account, you do not need to
      finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
      AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
      ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
      access to your account** page, choose **Grant access** . (After you have connected to
      your Bitbucket account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code
      to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code
      to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or
      set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientCreateProjectResponseprojecttagsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojecttagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateProjectResponseprojecttagsTypeDef(
    _ClientCreateProjectResponseprojecttagsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `tags`

    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS CodeBuild.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientCreateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientCreateProjectResponseprojectvpcConfigTypeDef(
    _ClientCreateProjectResponseprojectvpcConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `vpcConfig`

    Information about the VPC configuration that AWS CodeBuild accesses.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {"type": str, "pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef(
    _ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseprojectwebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --*

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four
      event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
      comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
      PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
      updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
      account ID matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
      ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
      request, Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular
      expression ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --*

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
      specifies one or more events. For example, the webhook filter ``PUSH,
      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
      and pull request updated events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular
      expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
      ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
      is a branch with a reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not
      trigger a build. If true, then a webhook event that does not match the ``pattern``
      triggers a build. If false, then a webhook event that matches the ``pattern``
      triggers a build.
    """


_ClientCreateProjectResponseprojectwebhookTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientCreateProjectResponseprojectwebhookTypeDef(
    _ClientCreateProjectResponseprojectwebhookTypeDef
):
    """
    Type definition for `ClientCreateProjectResponseproject` `webhook`

    Information about a webhook that connects repository events to a build project in AWS
    CodeBuild.

    - **url** *(string) --*

      The URL to the webhook.

    - **payloadUrl** *(string) --*

      The AWS CodeBuild endpoint where webhook events are sent.

    - **secret** *(string) --*

      The secret token of the associated repository.

      .. note::

        A Bitbucket webhook does not support ``secret`` .

    - **branchFilter** *(string) --*

      A regular expression used to determine which repository branches are built when a webhook
      is triggered. If the name of a branch matches the regular expression, then it is built.
      If ``branchFilter`` is empty, then all branches are built.

      .. note::

        It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

    - **filterGroups** *(list) --*

      An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
      triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
      ``type`` .

      For a build to be triggered, at least one filter group in the ``filterGroups`` array must
      pass. For a filter group to pass, each of its filters must pass.

      - *(list) --*

        - *(dict) --*

          A filter used to determine which webhooks trigger a build.

          - **type** *(string) --*

            The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
            ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

              EVENT

            A webhook event triggers a build when the provided ``pattern`` matches one of four
            event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
            ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
            comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
            PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
            updated events.

            .. note::

              The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

              ACTOR_ACCOUNT_ID

            A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
            account ID matches the regular expression ``pattern`` .

              HEAD_REF

            A webhook event triggers a build when the head reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` and
            ``refs/tags/tag-name`` .

            Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
            request, Bitbucket push, and Bitbucket pull request events.

              BASE_REF

            A webhook event triggers a build when the base reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` .

            .. note::

              Works with pull request events only.

              FILE_PATH

            A webhook triggers a build when the path of a changed file matches the regular
            expression ``pattern`` .

            .. note::

              Works with GitHub and GitHub Enterprise push events only.

          - **pattern** *(string) --*

            For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
            specifies one or more events. For example, the webhook filter ``PUSH,
            PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
            and pull request updated events to trigger a build.

            For a ``WebHookFilter`` that uses any of the other filter types, a regular
            expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
            ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
            is a branch with a reference name ``refs/heads/branch-name`` .

          - **excludeMatchedPattern** *(boolean) --*

            Used to indicate that the ``pattern`` determines which webhook events do not
            trigger a build. If true, then a webhook event that does not match the ``pattern``
            triggers a build. If false, then a webhook event that matches the ``pattern``
            triggers a build.

    - **lastModifiedSecret** *(datetime) --*

      A timestamp that indicates the last time a repository's secret token was modified.
    """


_ClientCreateProjectResponseprojectTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientCreateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[
            ClientCreateProjectResponseprojectsecondarySourcesTypeDef
        ],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientCreateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef
        ],
        "cache": ClientCreateProjectResponseprojectcacheTypeDef,
        "environment": ClientCreateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientCreateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientCreateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientCreateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientCreateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientCreateProjectResponseprojectlogsConfigTypeDef,
    },
    total=False,
)


class ClientCreateProjectResponseprojectTypeDef(
    _ClientCreateProjectResponseprojectTypeDef
):
    """
    Type definition for `ClientCreateProjectResponse` `project`

    Information about the build project that was created.

    - **name** *(string) --*

      The name of the build project.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build project.

    - **description** *(string) --*

      A description that makes the build project easy to identify.

    - **source** *(dict) --*

      Information about the build input source code for this build project.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
        ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
        action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
        that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your GitHub
        account. Use the AWS CodeBuild console to start creating a build project. When you use
        the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to each
        repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
        application** . (After you have connected to your GitHub account, you do not need to
        finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
        AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
        ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
        access to your account** page, choose **Grant access** . (After you have connected to
        your Bitbucket account, you do not need to finish creating the build project. You can
        leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
        the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source code
        to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source code
        to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get or
        set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the
          OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
          When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
          **Confirm access to your account** page, choose **Grant access** . (After you have
          connected to your Bitbucket account, you do not need to finish creating the build
          project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
          this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
          ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get
          or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **sourceVersion** *(string) --*

      A version of the build input to be built for this project. If not specified, the latest
      version is used. If specified, it must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it
      must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit
      ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      If ``sourceVersion`` is specified at the build level, then that version takes precedence
      over this ``sourceVersion`` (at the project level).

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
      at the build level, then they take over these ``secondarySourceVersions`` (at the project
      level).

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
          name is specified, the branch's HEAD commit ID is used. If not specified, the default
          branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
          is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the build output artifacts for the build project.

      - **type** *(string) --*

        The type of build output artifact. Valid values include:

        * ``CODEPIPELINE`` : The build project has build output generated through AWS
        CodePipeline.

        .. note::

           The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

        * ``NO_ARTIFACTS`` : The build project does not produce any build output.

        * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
        S3).

      - **location** *(string) --*

        Information about the build output artifact location:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output locations instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output bucket.

      - **path** *(string) --*

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
        not specified, ``path`` is not used.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
        , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
        bucket at ``MyArtifacts/MyArtifact.zip`` .

      - **namespaceType** *(string) --*

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
        name and location to store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
          not specified.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
        ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
        in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      - **name** *(string) --*

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
        set the name to be a forward slash ("/"), the artifact is stored in the root of the
        output bucket.

        For example:

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
        ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
        ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
        "``/`` ", the output artifact is stored in the root of the output bucket.

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
        ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
        .

      - **packaging** *(string) --*

        The type of build output artifact to create:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output artifacts instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
          build output. This is the default if ``packaging`` is not specified.

          * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
          build output.

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact name.
        The name specified in a build spec file is calculated at build time and uses the Shell
        Command Language. For example, you can append a date and time to your artifact name so
        that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your output artifacts encrypted. This option is valid only
        if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
        another artifacts type, an invalidInputException is thrown.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about the build output artifacts for the build project.

        - **type** *(string) --*

          The type of build output artifact. Valid values include:

          * ``CODEPIPELINE`` : The build project has build output generated through AWS
          CodePipeline.

          .. note::

             The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

          * ``NO_ARTIFACTS`` : The build project does not produce any build output.

          * ``S3`` : The build project stores build output in Amazon Simple Storage Service
          (Amazon S3).

        - **location** *(string) --*

          Information about the build output artifact location:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output locations instead
          of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output bucket.

        - **path** *(string) --*

          Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
          is not specified, ``path`` is not used.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
          the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        - **namespaceType** *(string) --*

          Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
          name and location to store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

            * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
            not specified.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
          stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        - **name** *(string) --*

          Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
          set the name to be a forward slash ("/"), the artifact is stored in the root of the
          output bucket.

          For example:

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
          ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
          "``/`` ", the output artifact is stored in the root of the output bucket.

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to "``/`` ", the output artifact is stored in
          ``MyArtifacts/*build-ID* `` .

        - **packaging** *(string) --*

          The type of build output artifact to create:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output artifacts instead
          of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
            build output. This is the default if ``packaging`` is not specified.

            * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
            build output.

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses the
          Shell Command Language. For example, you can append a date and time to your artifact
          name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your output artifacts encrypted. This option is valid
          only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
          set with another artifacts type, an invalidInputException is thrown.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build project.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits. This
        mode is a good choice for projects with a clean working directory and a source that is a
        large Git repository. If you choose this option and your project does not use a Git
        repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
        mode is a good choice if your build scenario is not suited to one of the other three
        local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project sources.
          Cached items are overriden if a source item has the same name. Directories are
          specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build project.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an image
        with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive values,
              especially AWS secret key IDs and secret access keys. Environment variables can be
              displayed in plain text using the AWS CodeBuild console and the AWS Command Line
              Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
            Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding one
        of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The valid
          value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
        you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to
      interact with dependent AWS services on behalf of the AWS account.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out
      any related build that did not get marked as completed. The default is 60 minutes.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your service
        role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **tags** *(list) --*

      The tags for this build project.

      These tags are available for use by AWS services that support AWS CodeBuild build project
      tags.

      - *(dict) --*

        A tag, consisting of a key and a value.

        This tag is available for use by AWS services that support tags in AWS CodeBuild.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.

    - **created** *(datetime) --*

      When the build project was created, expressed in Unix time format.

    - **lastModified** *(datetime) --*

      When the build project's settings were last modified, expressed in Unix time format.

    - **webhook** *(dict) --*

      Information about a webhook that connects repository events to a build project in AWS
      CodeBuild.

      - **url** *(string) --*

        The URL to the webhook.

      - **payloadUrl** *(string) --*

        The AWS CodeBuild endpoint where webhook events are sent.

      - **secret** *(string) --*

        The secret token of the associated repository.

        .. note::

          A Bitbucket webhook does not support ``secret`` .

      - **branchFilter** *(string) --*

        A regular expression used to determine which repository branches are built when a webhook
        is triggered. If the name of a branch matches the regular expression, then it is built.
        If ``branchFilter`` is empty, then all branches are built.

        .. note::

          It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

      - **filterGroups** *(list) --*

        An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
        triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
        ``type`` .

        For a build to be triggered, at least one filter group in the ``filterGroups`` array must
        pass. For a filter group to pass, each of its filters must pass.

        - *(list) --*

          - *(dict) --*

            A filter used to determine which webhooks trigger a build.

            - **type** *(string) --*

              The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
              ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                EVENT

              A webhook event triggers a build when the provided ``pattern`` matches one of four
              event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
              ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
              comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
              PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
              updated events.

              .. note::

                The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                ACTOR_ACCOUNT_ID

              A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
              account ID matches the regular expression ``pattern`` .

                HEAD_REF

              A webhook event triggers a build when the head reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` and
              ``refs/tags/tag-name`` .

              Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
              request, Bitbucket push, and Bitbucket pull request events.

                BASE_REF

              A webhook event triggers a build when the base reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` .

              .. note::

                Works with pull request events only.

                FILE_PATH

              A webhook triggers a build when the path of a changed file matches the regular
              expression ``pattern`` .

              .. note::

                Works with GitHub and GitHub Enterprise push events only.

            - **pattern** *(string) --*

              For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
              specifies one or more events. For example, the webhook filter ``PUSH,
              PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
              and pull request updated events to trigger a build.

              For a ``WebHookFilter`` that uses any of the other filter types, a regular
              expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
              ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
              is a branch with a reference name ``refs/heads/branch-name`` .

            - **excludeMatchedPattern** *(boolean) --*

              Used to indicate that the ``pattern`` determines which webhook events do not
              trigger a build. If true, then a webhook event that does not match the ``pattern``
              triggers a build. If false, then a webhook event that matches the ``pattern``
              triggers a build.

      - **lastModifiedSecret** *(datetime) --*

        A timestamp that indicates the last time a repository's secret token was modified.

    - **vpcConfig** *(dict) --*

      Information about the VPC configuration that AWS CodeBuild accesses.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **badge** *(dict) --*

      Information about the build badge for the build project.

      - **badgeEnabled** *(boolean) --*

        Set this to true to generate a publicly accessible URL for your project's build badge.

      - **badgeRequestUrl** *(string) --*

        The publicly-accessible URL through which you can access the build badge for your project.

        The publicly accessible URL through which you can access the build badge for your project.

    - **logsConfig** *(dict) --*

      Information about logs for the build project. A project can create logs in Amazon
      CloudWatch Logs, an S3 bucket, or both.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
        enabled by default.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
        by default.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
          is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
          ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3 build
          logs are encrypted.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"project": ClientCreateProjectResponseprojectTypeDef},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    Type definition for `ClientCreateProject` `Response`

    - **project** *(dict) --*

      Information about the build project that was created.

      - **name** *(string) --*

        The name of the build project.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the build project.

      - **description** *(string) --*

        A description that makes the build project easy to identify.

      - **source** *(dict) --*

        Information about the build input source code for this build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
          ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
          action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
          that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your GitHub
          account. Use the AWS CodeBuild console to start creating a build project. When you use
          the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to each
          repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
          application** . (After you have connected to your GitHub account, you do not need to
          finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
          AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
          ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
          access to your account** page, choose **Grant access** . (After you have connected to
          your Bitbucket account, you do not need to finish creating the build project. You can
          leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
          the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source code
          to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source code
          to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get or
          set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents the
            OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

      - **secondarySources** *(list) --*

        An array of ``ProjectSource`` objects.

        - *(dict) --*

          Information about the build input source code for the build project.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

      - **sourceVersion** *(string) --*

        A version of the build input to be built for this project. If not specified, the latest
        version is used. If specified, it must be one of:

        * For AWS CodeCommit: the commit ID to use.

        * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
        the version of the source code you want to build. If a pull request ID is specified, it
        must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
        specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
        commit ID is used.

        * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
        the source code you want to build. If a branch name is specified, the branch's HEAD commit
        ID is used. If not specified, the default branch's HEAD commit ID is used.

        * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
        represents the build input ZIP file to use.

        If ``sourceVersion`` is specified at the build level, then that version takes precedence
        over this ``sourceVersion`` (at the project level).

        For more information, see `Source Version Sample with CodeBuild
        <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
        the *AWS CodeBuild User Guide* .

      - **secondarySourceVersions** *(list) --*

        An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
        at the build level, then they take over these ``secondarySourceVersions`` (at the project
        level).

        - *(dict) --*

          A source identifier and its corresponding version.

          - **sourceIdentifier** *(string) --*

            An identifier for a source in the build project.

          - **sourceVersion** *(string) --*

            The source version for the corresponding source identifier. If specified, must be one
            of:

            * For AWS CodeCommit: the commit ID to use.

            * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
            to the version of the source code you want to build. If a pull request ID is specified,
            it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
            name is specified, the branch's HEAD commit ID is used. If not specified, the default
            branch's HEAD commit ID is used.

            * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
            version of the source code you want to build. If a branch name is specified, the
            branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
            is used.

            * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
            represents the build input ZIP file to use.

            For more information, see `Source Version Sample with CodeBuild
            <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
            in the *AWS CodeBuild User Guide* .

      - **artifacts** *(dict) --*

        Information about the build output artifacts for the build project.

        - **type** *(string) --*

          The type of build output artifact. Valid values include:

          * ``CODEPIPELINE`` : The build project has build output generated through AWS
          CodePipeline.

          .. note::

             The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

          * ``NO_ARTIFACTS`` : The build project does not produce any build output.

          * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
          S3).

        - **location** *(string) --*

          Information about the build output artifact location:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output locations instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output bucket.

        - **path** *(string) --*

          Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
          not specified, ``path`` is not used.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
          , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
          bucket at ``MyArtifacts/MyArtifact.zip`` .

        - **namespaceType** *(string) --*

          Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
          name and location to store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

            * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
            not specified.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
          in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        - **name** *(string) --*

          Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
          set the name to be a forward slash ("/"), the artifact is stored in the root of the
          output bucket.

          For example:

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
          ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
          ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
          "``/`` ", the output artifact is stored in the root of the output bucket.

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
          ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
          .

        - **packaging** *(string) --*

          The type of build output artifact to create:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output artifacts instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
            build output. This is the default if ``packaging`` is not specified.

            * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
            build output.

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact name.
          The name specified in a build spec file is calculated at build time and uses the Shell
          Command Language. For example, you can append a date and time to your artifact name so
          that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your output artifacts encrypted. This option is valid only
          if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
          another artifacts type, an invalidInputException is thrown.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

      - **secondaryArtifacts** *(list) --*

        An array of ``ProjectArtifacts`` objects.

        - *(dict) --*

          Information about the build output artifacts for the build project.

          - **type** *(string) --*

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
            is not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
            stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to "``/`` ", the output artifact is stored in
            ``MyArtifacts/*build-ID* `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
            set with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

      - **cache** *(dict) --*

        Information about the cache for the build project.

        - **type** *(string) --*

          The type of cache used by the build project. Valid values include:

          * ``NO_CACHE`` : The build project does not use any cache.

          * ``S3`` : The build project reads and writes from and to S3.

          * ``LOCAL`` : The build project stores a cache locally on a build host that is only
          available to that build host.

        - **location** *(string) --*

          Information about the cache location:

          * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

          * ``S3`` : This is the S3 bucket name/prefix.

        - **modes** *(list) --*

          If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
          modes at the same time.

          * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
          After the cache is created, subsequent builds pull only the change between commits. This
          mode is a good choice for projects with a clean working directory and a source that is a
          large Git repository. If you choose this option and your project does not use a Git
          repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

          * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
          choice for projects that build or pull large Docker images. It can prevent the
          performance issues caused by pulling large Docker images down from the network.

          .. note::

              * You can use a Docker layer cache in the Linux environment only.

              * The ``privileged`` flag must be set so that your project has the required Docker
              permissions.

              * You should consider the security implications before you use a Docker layer cache.

          * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
          mode is a good choice if your build scenario is not suited to one of the other three
          local cache modes. If you use a custom cache:

            * Only directories can be specified for caching. You cannot specify individual files.

            * Symlinks are used to reference cached directories.

            * Cached directories are linked to your build before it downloads its project sources.
            Cached items are overriden if a source item has the same name. Directories are
            specified using cache paths in the buildspec file.

          - *(string) --*

      - **environment** *(dict) --*

        Information about the build environment for this build project.

        - **type** *(string) --*

          The type of build environment to use for related builds.

        - **image** *(string) --*

          The image tag or image digest that identifies the Docker image to use for this build
          project. Use the following formats:

          * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
          the tag "latest," use ``registry/repository:latest`` .

          * For an image digest: ``registry/repository@digest`` . For example, to specify an image
          with the digest
          "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
          ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
          .

        - **computeType** *(string) --*

          Information about the compute resources the build project uses. Available values include:

          * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

          * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

          * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

          For more information, see `Build Environment Compute Types
          <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
          in the *AWS CodeBuild User Guide.*

        - **environmentVariables** *(list) --*

          A set of environment variables to make available to builds for this build project.

          - *(dict) --*

            Information about an environment variable for a build project or a build.

            - **name** *(string) --*

              The name or key of the environment variable.

            - **value** *(string) --*

              The value of the environment variable.

              .. warning::

                We strongly discourage the use of environment variables to store sensitive values,
                especially AWS secret key IDs and secret access keys. Environment variables can be
                displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                Interface (AWS CLI).

            - **type** *(string) --*

              The type of environment variable. Valid values include:

              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
              Parameter Store.

              * ``PLAINTEXT`` : An environment variable in plaintext format.

              * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

        - **privilegedMode** *(boolean) --*

          Enables running the Docker daemon inside a Docker container. Set to true only if the
          build project is used to build Docker images. Otherwise, a build that attempts to
          interact with the Docker daemon fails. The default setting is ``false`` .

          You can initialize the Docker daemon during the install phase of your build by adding one
          of the following sets of commands to the install phase of your buildspec file:

          If the operating system's base image is Ubuntu Linux:

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

          If the operating system's base image is Alpine Linux and the previous command does not
          work, add the ``-t`` argument to ``timeout`` :

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

        - **certificate** *(string) --*

          The certificate to use with this build project.

        - **registryCredential** *(dict) --*

          The credentials for access to a private registry.

          - **credential** *(string) --*

            The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

            .. note::

              The ``credential`` can use the name of the credentials only if they exist in your
              current region.

          - **credentialProvider** *(string) --*

            The service that created the credentials to access a private Docker registry. The valid
            value, SECRETS_MANAGER, is for AWS Secrets Manager.

        - **imagePullCredentialsType** *(string) --*

          The type of credentials AWS CodeBuild uses to pull images in your build. There are two
          valid values:

          * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
          you modify your ECR repository policy to trust AWS CodeBuild's service principal.

          * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

          When you use a cross-account or private registry image, you must use SERVICE_ROLE
          credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
          credentials.

      - **serviceRole** *(string) --*

        The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to
        interact with dependent AWS services on behalf of the AWS account.

      - **timeoutInMinutes** *(integer) --*

        How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out
        any related build that did not get marked as completed. The default is 60 minutes.

      - **queuedTimeoutInMinutes** *(integer) --*

        The number of minutes a build is allowed to be queued before it times out.

      - **encryptionKey** *(string) --*

        The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
        encrypting the build output artifacts.

        .. note::

          You can use a cross-account KMS key to encrypt the build output artifacts if your service
          role has permission to that key.

        You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
        CMK's alias (using the format ``alias/*alias-name* `` ).

      - **tags** *(list) --*

        The tags for this build project.

        These tags are available for use by AWS services that support AWS CodeBuild build project
        tags.

        - *(dict) --*

          A tag, consisting of a key and a value.

          This tag is available for use by AWS services that support tags in AWS CodeBuild.

          - **key** *(string) --*

            The tag's key.

          - **value** *(string) --*

            The tag's value.

      - **created** *(datetime) --*

        When the build project was created, expressed in Unix time format.

      - **lastModified** *(datetime) --*

        When the build project's settings were last modified, expressed in Unix time format.

      - **webhook** *(dict) --*

        Information about a webhook that connects repository events to a build project in AWS
        CodeBuild.

        - **url** *(string) --*

          The URL to the webhook.

        - **payloadUrl** *(string) --*

          The AWS CodeBuild endpoint where webhook events are sent.

        - **secret** *(string) --*

          The secret token of the associated repository.

          .. note::

            A Bitbucket webhook does not support ``secret`` .

        - **branchFilter** *(string) --*

          A regular expression used to determine which repository branches are built when a webhook
          is triggered. If the name of a branch matches the regular expression, then it is built.
          If ``branchFilter`` is empty, then all branches are built.

          .. note::

            It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

        - **filterGroups** *(list) --*

          An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
          triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
          ``type`` .

          For a build to be triggered, at least one filter group in the ``filterGroups`` array must
          pass. For a filter group to pass, each of its filters must pass.

          - *(list) --*

            - *(dict) --*

              A filter used to determine which webhooks trigger a build.

              - **type** *(string) --*

                The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                  EVENT

                A webhook event triggers a build when the provided ``pattern`` matches one of four
                event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
                ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
                comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
                PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
                updated events.

                .. note::

                  The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                  ACTOR_ACCOUNT_ID

                A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
                account ID matches the regular expression ``pattern`` .

                  HEAD_REF

                A webhook event triggers a build when the head reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                ``refs/tags/tag-name`` .

                Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
                request, Bitbucket push, and Bitbucket pull request events.

                  BASE_REF

                A webhook event triggers a build when the base reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                .. note::

                  Works with pull request events only.

                  FILE_PATH

                A webhook triggers a build when the path of a changed file matches the regular
                expression ``pattern`` .

                .. note::

                  Works with GitHub and GitHub Enterprise push events only.

              - **pattern** *(string) --*

                For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
                specifies one or more events. For example, the webhook filter ``PUSH,
                PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
                and pull request updated events to trigger a build.

                For a ``WebHookFilter`` that uses any of the other filter types, a regular
                expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
                ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
                is a branch with a reference name ``refs/heads/branch-name`` .

              - **excludeMatchedPattern** *(boolean) --*

                Used to indicate that the ``pattern`` determines which webhook events do not
                trigger a build. If true, then a webhook event that does not match the ``pattern``
                triggers a build. If false, then a webhook event that matches the ``pattern``
                triggers a build.

        - **lastModifiedSecret** *(datetime) --*

          A timestamp that indicates the last time a repository's secret token was modified.

      - **vpcConfig** *(dict) --*

        Information about the VPC configuration that AWS CodeBuild accesses.

        - **vpcId** *(string) --*

          The ID of the Amazon VPC.

        - **subnets** *(list) --*

          A list of one or more subnet IDs in your Amazon VPC.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          A list of one or more security groups IDs in your Amazon VPC.

          - *(string) --*

      - **badge** *(dict) --*

        Information about the build badge for the build project.

        - **badgeEnabled** *(boolean) --*

          Set this to true to generate a publicly accessible URL for your project's build badge.

        - **badgeRequestUrl** *(string) --*

          The publicly-accessible URL through which you can access the build badge for your project.

          The publicly accessible URL through which you can access the build badge for your project.

      - **logsConfig** *(dict) --*

        Information about logs for the build project. A project can create logs in Amazon
        CloudWatch Logs, an S3 bucket, or both.

        - **cloudWatchLogs** *(dict) --*

          Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
          enabled by default.

          - **status** *(string) --*

            The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
            values are:

            * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

            * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

          - **groupName** *(string) --*

            The group name of the logs in Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

          - **streamName** *(string) --*

            The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

        - **s3Logs** *(dict) --*

          Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
          by default.

          - **status** *(string) --*

            The current status of the S3 build logs. Valid values are:

            * ``ENABLED`` : S3 build logs are enabled for this build project.

            * ``DISABLED`` : S3 build logs are not enabled for this build project.

          - **location** *(string) --*

            The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
            is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
            ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your S3 build log output encrypted. By default S3 build
            logs are encrypted.
    """


_RequiredClientCreateProjectartifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectartifactsTypeDef", {"type": str}
)
_OptionalClientCreateProjectartifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectartifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectartifactsTypeDef(
    _RequiredClientCreateProjectartifactsTypeDef,
    _OptionalClientCreateProjectartifactsTypeDef,
):
    """
    Type definition for `ClientCreateProject` `artifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and
      ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output bucket at
      ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the
      name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/`` ",
      the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_RequiredClientCreateProjectcacheTypeDef = TypedDict(
    "_RequiredClientCreateProjectcacheTypeDef", {"type": str}
)
_OptionalClientCreateProjectcacheTypeDef = TypedDict(
    "_OptionalClientCreateProjectcacheTypeDef",
    {"location": str, "modes": List[str]},
    total=False,
)


class ClientCreateProjectcacheTypeDef(
    _RequiredClientCreateProjectcacheTypeDef, _OptionalClientCreateProjectcacheTypeDef
):
    """
    Type definition for `ClientCreateProject` `cache`

    Stores recently used information so that it can be quickly accessed at a later time.

    - **type** *(string) --* **[REQUIRED]**

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache modes
      at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources. After the
      cache is created, subsequent builds pull only the change between commits. This mode is a good
      choice for projects with a clean working directory and a source that is a large Git repository.
      If you choose this option and your project does not use a Git repository (GitHub, GitHub
      Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good choice
      for projects that build or pull large Docker images. It can prevent the performance issues
      caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This mode
      is a good choice if your build scenario is not suited to one of the other three local cache
      modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources. Cached
        items are overriden if a source item has the same name. Directories are specified using cache
        paths in the buildspec file.

      - *(string) --*
    """


_RequiredClientCreateProjectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_RequiredClientCreateProjectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str},
)
_OptionalClientCreateProjectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_OptionalClientCreateProjectenvironmentenvironmentVariablesTypeDef",
    {"type": str},
    total=False,
)


class ClientCreateProjectenvironmentenvironmentVariablesTypeDef(
    _RequiredClientCreateProjectenvironmentenvironmentVariablesTypeDef,
    _OptionalClientCreateProjectenvironmentenvironmentVariablesTypeDef,
):
    """
    Type definition for `ClientCreateProjectenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --* **[REQUIRED]**

      The name or key of the environment variable.

    - **value** *(string) --* **[REQUIRED]**

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientCreateProjectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientCreateProjectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
)


class ClientCreateProjectenvironmentregistryCredentialTypeDef(
    _ClientCreateProjectenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientCreateProjectenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your current
        region.

    - **credentialProvider** *(string) --* **[REQUIRED]**

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_RequiredClientCreateProjectenvironmentTypeDef = TypedDict(
    "_RequiredClientCreateProjectenvironmentTypeDef",
    {"type": str, "image": str, "computeType": str},
)
_OptionalClientCreateProjectenvironmentTypeDef = TypedDict(
    "_OptionalClientCreateProjectenvironmentTypeDef",
    {
        "environmentVariables": List[
            ClientCreateProjectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientCreateProjectenvironmentTypeDef(
    _RequiredClientCreateProjectenvironmentTypeDef,
    _OptionalClientCreateProjectenvironmentTypeDef,
):
    """
    Type definition for `ClientCreateProject` `environment`

    Information about the build environment for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build environment to use for related builds.

    - **image** *(string) --* **[REQUIRED]**

      The image tag or image digest that identifies the Docker image to use for this build project.
      Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with the tag
      "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image with
      the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --* **[REQUIRED]**

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__ in
      the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --* **[REQUIRED]**

          The name or key of the environment variable.

        - **value** *(string) --* **[REQUIRED]**

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the build
      project is used to build Docker images. Otherwise, a build that attempts to interact with the
      Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one of
      the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
       --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not work,
      add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
       --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your current
          region.

      - **credentialProvider** *(string) --* **[REQUIRED]**

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid
      values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that you
      modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials.
      When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.
    """


_RequiredClientCreateProjectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientCreateProjectlogsConfigcloudWatchLogsTypeDef", {"status": str}
)
_OptionalClientCreateProjectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientCreateProjectlogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientCreateProjectlogsConfigcloudWatchLogsTypeDef(
    _RequiredClientCreateProjectlogsConfigcloudWatchLogsTypeDef,
    _OptionalClientCreateProjectlogsConfigcloudWatchLogsTypeDef,
):
    """
    Type definition for `ClientCreateProjectlogsConfig` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
    enabled by default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
      are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
      Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_RequiredClientCreateProjectlogsConfigs3LogsTypeDef = TypedDict(
    "_RequiredClientCreateProjectlogsConfigs3LogsTypeDef", {"status": str}
)
_OptionalClientCreateProjectlogsConfigs3LogsTypeDef = TypedDict(
    "_OptionalClientCreateProjectlogsConfigs3LogsTypeDef",
    {"location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientCreateProjectlogsConfigs3LogsTypeDef(
    _RequiredClientCreateProjectlogsConfigs3LogsTypeDef,
    _OptionalClientCreateProjectlogsConfigs3LogsTypeDef,
):
    """
    Type definition for `ClientCreateProjectlogsConfig` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
    default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
      ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
      are encrypted.
    """


_ClientCreateProjectlogsConfigTypeDef = TypedDict(
    "_ClientCreateProjectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientCreateProjectlogsConfigTypeDef(_ClientCreateProjectlogsConfigTypeDef):
    """
    Type definition for `ClientCreateProject` `logsConfig`

    Information about logs for the build project. These can be logs in Amazon CloudWatch Logs, logs
    uploaded to a specified S3 bucket, or both.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
        Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
      default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
        ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
        are encrypted.
    """


_RequiredClientCreateProjectsecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectsecondaryArtifactsTypeDef", {"type": str}
)
_OptionalClientCreateProjectsecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectsecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectsecondaryArtifactsTypeDef(
    _RequiredClientCreateProjectsecondaryArtifactsTypeDef,
    _OptionalClientCreateProjectsecondaryArtifactsTypeDef,
):
    """
    Type definition for `ClientCreateProject` `secondaryArtifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
      bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
      , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set
      the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/``
      ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientCreateProjectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientCreateProjectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
)


class ClientCreateProjectsecondarySourceVersionsTypeDef(
    _ClientCreateProjectsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientCreateProject` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --* **[REQUIRED]**

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --* **[REQUIRED]**

      The source version for the corresponding source identifier. If specified, must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it must
      use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit ID
      is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents
      the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in the
      *AWS CodeBuild User Guide* .
    """


_RequiredClientCreateProjectsecondarySourcesauthTypeDef = TypedDict(
    "_RequiredClientCreateProjectsecondarySourcesauthTypeDef", {"type": str}
)
_OptionalClientCreateProjectsecondarySourcesauthTypeDef = TypedDict(
    "_OptionalClientCreateProjectsecondarySourcesauthTypeDef",
    {"resource": str},
    total=False,
)


class ClientCreateProjectsecondarySourcesauthTypeDef(
    _RequiredClientCreateProjectsecondarySourcesauthTypeDef,
    _OptionalClientCreateProjectsecondarySourcesauthTypeDef,
):
    """
    Type definition for `ClientCreateProjectsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code to
    be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or set
    this information directly.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientCreateProjectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
)


class ClientCreateProjectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientCreateProjectsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientCreateProjectsecondarySourcesTypeDef = TypedDict(
    "_RequiredClientCreateProjectsecondarySourcesTypeDef", {"type": str}
)
_OptionalClientCreateProjectsecondarySourcesTypeDef = TypedDict(
    "_OptionalClientCreateProjectsecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectsecondarySourcesTypeDef(
    _RequiredClientCreateProjectsecondarySourcesTypeDef,
    _OptionalClientCreateProjectsecondarySourcesTypeDef,
):
    """
    Type definition for `ClientCreateProject` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action
      instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that
      contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the
      following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains
      the source and the build spec. You must connect your AWS account to your GitHub account. Use
      the AWS CodeBuild console to start creating a build project. When you use the console to
      connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for
      **Organization access** , choose **Request access** next to each repository you want to allow
      AWS CodeBuild to have access to, and then choose **Authorize application** . (After you have
      connected to your GitHub account, you do not need to finish creating the build project. You
      can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your Bitbucket
      account. Use the AWS CodeBuild console to start creating a build project. When you use the
      console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your
      account** page, choose **Grant access** . (After you have connected to your Bitbucket
      account, you do not need to finish creating the build project. You can leave the AWS
      CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the ``source``
      object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code to
      be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code to
      be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or set
      this information directly.

      - **type** *(string) --* **[REQUIRED]**

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider. This
      option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If
      this is set and you use a different source provider, an invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_RequiredClientCreateProjectsourceauthTypeDef = TypedDict(
    "_RequiredClientCreateProjectsourceauthTypeDef", {"type": str}
)
_OptionalClientCreateProjectsourceauthTypeDef = TypedDict(
    "_OptionalClientCreateProjectsourceauthTypeDef", {"resource": str}, total=False
)


class ClientCreateProjectsourceauthTypeDef(
    _RequiredClientCreateProjectsourceauthTypeDef,
    _OptionalClientCreateProjectsourceauthTypeDef,
):
    """
    Type definition for `ClientCreateProjectsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code to be
    built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or set
    this information directly.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth
      authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientCreateProjectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectsourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}
)


class ClientCreateProjectsourcegitSubmodulesConfigTypeDef(
    _ClientCreateProjectsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientCreateProjectsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientCreateProjectsourceTypeDef = TypedDict(
    "_RequiredClientCreateProjectsourceTypeDef", {"type": str}
)
_OptionalClientCreateProjectsourceTypeDef = TypedDict(
    "_OptionalClientCreateProjectsourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectsourceTypeDef(
    _RequiredClientCreateProjectsourceTypeDef, _OptionalClientCreateProjectsourceTypeDef
):
    """
    Type definition for `ClientCreateProject` `source`

    Information about the build input source code for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline
      in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action
      instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that
      contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID*
      .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the
      following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name* /*path*
        /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains
      the source and the build spec. You must connect your AWS account to your GitHub account. Use
      the AWS CodeBuild console to start creating a build project. When you use the console to
      connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for
      **Organization access** , choose **Request access** next to each repository you want to allow
      AWS CodeBuild to have access to, and then choose **Authorize application** . (After you have
      connected to your GitHub account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the
      ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your Bitbucket
      account. Use the AWS CodeBuild console to start creating a build project. When you use the
      console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your
      account** page, choose **Grant access** . (After you have connected to your Bitbucket account,
      you do not need to finish creating the build project. You can leave the AWS CodeBuild console.)
      To instruct AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
      object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code to be
      built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code to be
      built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or set
      this information directly.

      - **type** *(string) --* **[REQUIRED]**

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth
        authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider. This
      option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If
      this is set and you use a different source provider, an invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientCreateProjecttagsTypeDef = TypedDict(
    "_ClientCreateProjecttagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateProjecttagsTypeDef(_ClientCreateProjecttagsTypeDef):
    """
    Type definition for `ClientCreateProject` `tags`

    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS CodeBuild.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientCreateProjectvpcConfigTypeDef = TypedDict(
    "_ClientCreateProjectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientCreateProjectvpcConfigTypeDef(_ClientCreateProjectvpcConfigTypeDef):
    """
    Type definition for `ClientCreateProject` `vpcConfig`

    VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientCreateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookfilterGroupsTypeDef",
    {"type": str, "pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientCreateWebhookResponsewebhookfilterGroupsTypeDef(
    _ClientCreateWebhookResponsewebhookfilterGroupsTypeDef
):
    """
    Type definition for `ClientCreateWebhookResponsewebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --*

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four
      event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
      string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
      push, pull request created, and pull request updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
      account ID matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
      ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
      request, Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular
      expression ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --*

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
      specifies one or more events. For example, the webhook filter ``PUSH,
      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
      and pull request updated events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
      pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
      the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
      with a reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not trigger
      a build. If true, then a webhook event that does not match the ``pattern`` triggers a
      build. If false, then a webhook event that matches the ``pattern`` triggers a build.
    """


_ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientCreateWebhookResponsewebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientCreateWebhookResponsewebhookTypeDef(
    _ClientCreateWebhookResponsewebhookTypeDef
):
    """
    Type definition for `ClientCreateWebhookResponse` `webhook`

    Information about a webhook that connects repository events to a build project in AWS
    CodeBuild.

    - **url** *(string) --*

      The URL to the webhook.

    - **payloadUrl** *(string) --*

      The AWS CodeBuild endpoint where webhook events are sent.

    - **secret** *(string) --*

      The secret token of the associated repository.

      .. note::

        A Bitbucket webhook does not support ``secret`` .

    - **branchFilter** *(string) --*

      A regular expression used to determine which repository branches are built when a webhook
      is triggered. If the name of a branch matches the regular expression, then it is built. If
      ``branchFilter`` is empty, then all branches are built.

      .. note::

        It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

    - **filterGroups** *(list) --*

      An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
      triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
      ``type`` .

      For a build to be triggered, at least one filter group in the ``filterGroups`` array must
      pass. For a filter group to pass, each of its filters must pass.

      - *(list) --*

        - *(dict) --*

          A filter used to determine which webhooks trigger a build.

          - **type** *(string) --*

            The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
            ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

              EVENT

            A webhook event triggers a build when the provided ``pattern`` matches one of four
            event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
            ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
            string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
            push, pull request created, and pull request updated events.

            .. note::

              The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

              ACTOR_ACCOUNT_ID

            A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
            account ID matches the regular expression ``pattern`` .

              HEAD_REF

            A webhook event triggers a build when the head reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` and
            ``refs/tags/tag-name`` .

            Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
            request, Bitbucket push, and Bitbucket pull request events.

              BASE_REF

            A webhook event triggers a build when the base reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` .

            .. note::

              Works with pull request events only.

              FILE_PATH

            A webhook triggers a build when the path of a changed file matches the regular
            expression ``pattern`` .

            .. note::

              Works with GitHub and GitHub Enterprise push events only.

          - **pattern** *(string) --*

            For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
            specifies one or more events. For example, the webhook filter ``PUSH,
            PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
            and pull request updated events to trigger a build.

            For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
            pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
            the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
            with a reference name ``refs/heads/branch-name`` .

          - **excludeMatchedPattern** *(boolean) --*

            Used to indicate that the ``pattern`` determines which webhook events do not trigger
            a build. If true, then a webhook event that does not match the ``pattern`` triggers a
            build. If false, then a webhook event that matches the ``pattern`` triggers a build.

    - **lastModifiedSecret** *(datetime) --*

      A timestamp that indicates the last time a repository's secret token was modified.
    """


_ClientCreateWebhookResponseTypeDef = TypedDict(
    "_ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientCreateWebhookResponseTypeDef(_ClientCreateWebhookResponseTypeDef):
    """
    Type definition for `ClientCreateWebhook` `Response`

    - **webhook** *(dict) --*

      Information about a webhook that connects repository events to a build project in AWS
      CodeBuild.

      - **url** *(string) --*

        The URL to the webhook.

      - **payloadUrl** *(string) --*

        The AWS CodeBuild endpoint where webhook events are sent.

      - **secret** *(string) --*

        The secret token of the associated repository.

        .. note::

          A Bitbucket webhook does not support ``secret`` .

      - **branchFilter** *(string) --*

        A regular expression used to determine which repository branches are built when a webhook
        is triggered. If the name of a branch matches the regular expression, then it is built. If
        ``branchFilter`` is empty, then all branches are built.

        .. note::

          It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

      - **filterGroups** *(list) --*

        An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
        triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
        ``type`` .

        For a build to be triggered, at least one filter group in the ``filterGroups`` array must
        pass. For a filter group to pass, each of its filters must pass.

        - *(list) --*

          - *(dict) --*

            A filter used to determine which webhooks trigger a build.

            - **type** *(string) --*

              The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
              ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                EVENT

              A webhook event triggers a build when the provided ``pattern`` matches one of four
              event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
              ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
              string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
              push, pull request created, and pull request updated events.

              .. note::

                The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                ACTOR_ACCOUNT_ID

              A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
              account ID matches the regular expression ``pattern`` .

                HEAD_REF

              A webhook event triggers a build when the head reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` and
              ``refs/tags/tag-name`` .

              Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
              request, Bitbucket push, and Bitbucket pull request events.

                BASE_REF

              A webhook event triggers a build when the base reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` .

              .. note::

                Works with pull request events only.

                FILE_PATH

              A webhook triggers a build when the path of a changed file matches the regular
              expression ``pattern`` .

              .. note::

                Works with GitHub and GitHub Enterprise push events only.

            - **pattern** *(string) --*

              For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
              specifies one or more events. For example, the webhook filter ``PUSH,
              PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
              and pull request updated events to trigger a build.

              For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
              pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
              the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
              with a reference name ``refs/heads/branch-name`` .

            - **excludeMatchedPattern** *(boolean) --*

              Used to indicate that the ``pattern`` determines which webhook events do not trigger
              a build. If true, then a webhook event that does not match the ``pattern`` triggers a
              build. If false, then a webhook event that matches the ``pattern`` triggers a build.

      - **lastModifiedSecret** *(datetime) --*

        A timestamp that indicates the last time a repository's secret token was modified.
    """


_RequiredClientCreateWebhookfilterGroupsTypeDef = TypedDict(
    "_RequiredClientCreateWebhookfilterGroupsTypeDef", {"type": str, "pattern": str}
)
_OptionalClientCreateWebhookfilterGroupsTypeDef = TypedDict(
    "_OptionalClientCreateWebhookfilterGroupsTypeDef",
    {"excludeMatchedPattern": bool},
    total=False,
)


class ClientCreateWebhookfilterGroupsTypeDef(
    _RequiredClientCreateWebhookfilterGroupsTypeDef,
    _OptionalClientCreateWebhookfilterGroupsTypeDef,
):
    """
    Type definition for `ClientCreateWebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --* **[REQUIRED]**

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four event
      types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
      string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push,
      pull request created, and pull request updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID
      matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular expression
      ``pattern`` . For example, ``refs/heads/branch-name`` and ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request,
      Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular expression
      ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular expression
      ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --* **[REQUIRED]**

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that specifies
      one or more events. For example, the webhook filter ``PUSH, PULL_REQUEST_CREATED,
      PULL_REQUEST_UPDATED`` allows all push, pull request created, and pull request updated
      events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
      pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and the
      pattern ``^refs/heads/`` triggers a build when the head reference is a branch with a
      reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not trigger a
      build. If true, then a webhook event that does not match the ``pattern`` triggers a build.
      If false, then a webhook event that matches the ``pattern`` triggers a build.
    """


_ClientDeleteSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientDeleteSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)


class ClientDeleteSourceCredentialsResponseTypeDef(
    _ClientDeleteSourceCredentialsResponseTypeDef
):
    """
    Type definition for `ClientDeleteSourceCredentials` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the token.
    """


_ClientImportSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientImportSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)


class ClientImportSourceCredentialsResponseTypeDef(
    _ClientImportSourceCredentialsResponseTypeDef
):
    """
    Type definition for `ClientImportSourceCredentials` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the token.
    """


_ClientListBuildsForProjectResponseTypeDef = TypedDict(
    "_ClientListBuildsForProjectResponseTypeDef",
    {"ids": List[str], "nextToken": str},
    total=False,
)


class ClientListBuildsForProjectResponseTypeDef(
    _ClientListBuildsForProjectResponseTypeDef
):
    """
    Type definition for `ClientListBuildsForProject` `Response`

    - **ids** *(list) --*

      A list of build IDs for the specified build project, with each build ID representing a single
      build.

      - *(string) --*

    - **nextToken** *(string) --*

      If there are more than 100 items in the list, only the first 100 items are returned, along
      with a unique string called a *next token* . To get the next batch of items in the list, call
      this operation again, adding the next token to the call.
    """


_ClientListBuildsResponseTypeDef = TypedDict(
    "_ClientListBuildsResponseTypeDef",
    {"ids": List[str], "nextToken": str},
    total=False,
)


class ClientListBuildsResponseTypeDef(_ClientListBuildsResponseTypeDef):
    """
    Type definition for `ClientListBuilds` `Response`

    - **ids** *(list) --*

      A list of build IDs, with each build ID representing a single build.

      - *(string) --*

    - **nextToken** *(string) --*

      If there are more than 100 items in the list, only the first 100 items are returned, along
      with a unique string called a *next token* . To get the next batch of items in the list, call
      this operation again, adding the next token to the call.
    """


_ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef",
    {"name": str, "description": str, "versions": List[str]},
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef
):
    """
    Type definition for `ClientListCuratedEnvironmentImagesResponseplatformslanguages` `images`

    Information about a Docker image that is managed by AWS CodeBuild.

    - **name** *(string) --*

      The name of the Docker image.

    - **description** *(string) --*

      The description of the Docker image.

    - **versions** *(list) --*

      A list of environment image versions.

      - *(string) --*
    """


_ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef",
    {
        "language": str,
        "images": List[
            ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef
        ],
    },
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef
):
    """
    Type definition for `ClientListCuratedEnvironmentImagesResponseplatforms` `languages`

    A set of Docker images that are related by programming language and are managed by AWS
    CodeBuild.

    - **language** *(string) --*

      The programming language for the Docker images.

    - **images** *(list) --*

      The list of Docker images that are related by the specified programming language.

      - *(dict) --*

        Information about a Docker image that is managed by AWS CodeBuild.

        - **name** *(string) --*

          The name of the Docker image.

        - **description** *(string) --*

          The description of the Docker image.

        - **versions** *(list) --*

          A list of environment image versions.

          - *(string) --*
    """


_ClientListCuratedEnvironmentImagesResponseplatformsTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformsTypeDef",
    {
        "platform": str,
        "languages": List[
            ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef
        ],
    },
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformsTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformsTypeDef
):
    """
    Type definition for `ClientListCuratedEnvironmentImagesResponse` `platforms`

    A set of Docker images that are related by platform and are managed by AWS CodeBuild.

    - **platform** *(string) --*

      The platform's name.

    - **languages** *(list) --*

      The list of programming languages that are available for the specified platform.

      - *(dict) --*

        A set of Docker images that are related by programming language and are managed by AWS
        CodeBuild.

        - **language** *(string) --*

          The programming language for the Docker images.

        - **images** *(list) --*

          The list of Docker images that are related by the specified programming language.

          - *(dict) --*

            Information about a Docker image that is managed by AWS CodeBuild.

            - **name** *(string) --*

              The name of the Docker image.

            - **description** *(string) --*

              The description of the Docker image.

            - **versions** *(list) --*

              A list of environment image versions.

              - *(string) --*
    """


_ClientListCuratedEnvironmentImagesResponseTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseTypeDef",
    {"platforms": List[ClientListCuratedEnvironmentImagesResponseplatformsTypeDef]},
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseTypeDef(
    _ClientListCuratedEnvironmentImagesResponseTypeDef
):
    """
    Type definition for `ClientListCuratedEnvironmentImages` `Response`

    - **platforms** *(list) --*

      Information about supported platforms for Docker images that are managed by AWS CodeBuild.

      - *(dict) --*

        A set of Docker images that are related by platform and are managed by AWS CodeBuild.

        - **platform** *(string) --*

          The platform's name.

        - **languages** *(list) --*

          The list of programming languages that are available for the specified platform.

          - *(dict) --*

            A set of Docker images that are related by programming language and are managed by AWS
            CodeBuild.

            - **language** *(string) --*

              The programming language for the Docker images.

            - **images** *(list) --*

              The list of Docker images that are related by the specified programming language.

              - *(dict) --*

                Information about a Docker image that is managed by AWS CodeBuild.

                - **name** *(string) --*

                  The name of the Docker image.

                - **description** *(string) --*

                  The description of the Docker image.

                - **versions** *(list) --*

                  A list of environment image versions.

                  - *(string) --*
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"nextToken": str, "projects": List[str]},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    Type definition for `ClientListProjects` `Response`

    - **nextToken** *(string) --*

      If there are more than 100 items in the list, only the first 100 items are returned, along
      with a unique string called a *next token* . To get the next batch of items in the list, call
      this operation again, adding the next token to the call.

    - **projects** *(list) --*

      The list of build project names, with each build project name representing a single build
      project.

      - *(string) --*
    """


_ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef = TypedDict(
    "_ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef",
    {"arn": str, "serverType": str, "authType": str},
    total=False,
)


class ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef(
    _ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef
):
    """
    Type definition for `ClientListSourceCredentialsResponse` `sourceCredentialsInfos`

    Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket repository.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the token.

    - **serverType** *(string) --*

      The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, or
      BITBUCKET.

    - **authType** *(string) --*

      The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH,
      or PERSONAL_ACCESS_TOKEN.
    """


_ClientListSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientListSourceCredentialsResponseTypeDef",
    {
        "sourceCredentialsInfos": List[
            ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef
        ]
    },
    total=False,
)


class ClientListSourceCredentialsResponseTypeDef(
    _ClientListSourceCredentialsResponseTypeDef
):
    """
    Type definition for `ClientListSourceCredentials` `Response`

    - **sourceCredentialsInfos** *(list) --*

      A list of ``SourceCredentialsInfo`` objects. Each ``SourceCredentialsInfo`` object includes
      the authentication type, token ARN, and type of source provider for one set of credentials.

      - *(dict) --*

        Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket repository.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the token.

        - **serverType** *(string) --*

          The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, or
          BITBUCKET.

        - **authType** *(string) --*

          The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH,
          or PERSONAL_ACCESS_TOKEN.
    """


_ClientStartBuildResponsebuildartifactsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildartifactsTypeDef(
    _ClientStartBuildResponsebuildartifactsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `artifacts`

    Information about the output artifacts for the build.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name.
      The name specified in a build spec file is calculated at build time and uses the Shell
      Command Language. For example, you can append a date and time to your artifact name so
      that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientStartBuildResponsebuildcacheTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildcacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientStartBuildResponsebuildcacheTypeDef(
    _ClientStartBuildResponsebuildcacheTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `cache`

    Information about the cache for the build.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits. This
      mode is a good choice for projects with a clean working directory and a source that is a
      large Git repository. If you choose this option and your project does not use a Git
      repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
      mode is a good choice if your build scenario is not suited to one of the other three
      local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources.
        Cached items are overriden if a source item has the same name. Directories are
        specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef(
    _ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef(
    _ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientStartBuildResponsebuildenvironmentTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildenvironmentTypeDef(
    _ClientStartBuildResponsebuildenvironmentTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `environment`

    Information about the build environment for this build.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image
      with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one
      of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
      you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef(
    _ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `exportedEnvironmentVariables`

    Information about an exported environment variable.

    - **name** *(string) --*

      The name of this exported environment variable.

    - **value** *(string) --*

      The value assigned to this exported environment variable.

      .. note::

        During a build, the value of a variable is available starting with the ``install``
        phase. It can be updated between the start of the ``install`` phase and the end of
        the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
        variables cannot change.
    """


_ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef(
    _ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildlogs` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientStartBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogss3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStartBuildResponsebuildlogss3LogsTypeDef(
    _ClientStartBuildResponsebuildlogss3LogsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildlogs` `s3Logs`

    Information about S3 logs for a build project.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
      is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build
      logs are encrypted.
    """


_ClientStartBuildResponsebuildlogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogs": ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)


class ClientStartBuildResponsebuildlogsTypeDef(
    _ClientStartBuildResponsebuildlogsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `logs`

    Information about the build's logs in Amazon CloudWatch Logs.

    - **groupName** *(string) --*

      The name of the Amazon CloudWatch Logs group for the build logs.

    - **streamName** *(string) --*

      The name of the Amazon CloudWatch Logs stream for the build logs.

    - **deepLink** *(string) --*

      The URL to an individual build log in Amazon CloudWatch Logs.

    - **s3DeepLink** *(string) --*

      The URL to a build log in an S3 bucket.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about S3 logs for a build project.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
        is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build
        logs are encrypted.
    """


_ClientStartBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientStartBuildResponsebuildnetworkInterfaceTypeDef(
    _ClientStartBuildResponsebuildnetworkInterfaceTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `networkInterface`

    Describes a network interface.

    - **subnetId** *(string) --*

      The ID of the subnet.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.
    """


_ClientStartBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientStartBuildResponsebuildphasescontextsTypeDef(
    _ClientStartBuildResponsebuildphasescontextsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildphases` `contexts`

    Additional information about a build phase that has an error. You can use this
    information for troubleshooting.

    - **statusCode** *(string) --*

      The status code for the context of the build phase.

    - **message** *(string) --*

      An explanation of the build phase's context. This might include a command ID and an
      exit code.
    """


_ClientStartBuildResponsebuildphasesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildphasesTypeDef",
    {
        "phaseType": str,
        "phaseStatus": str,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStartBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)


class ClientStartBuildResponsebuildphasesTypeDef(
    _ClientStartBuildResponsebuildphasesTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `phases`

    Information about a stage for a build.

    - **phaseType** *(string) --*

      The name of the build phase. Valid values include:

      * ``BUILD`` : Core build activities typically occur in this build phase.

      * ``COMPLETED`` : The build has been completed.

      * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

      * ``FINALIZING`` : The build process is completing in this build phase.

      * ``INSTALL`` : Installation activities typically occur in this build phase.

      * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

      * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

      * ``PROVISIONING`` : The build environment is being set up.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

      * ``SUBMITTED`` : The build has been submitted.

      * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
      location.

    - **phaseStatus** *(string) --*

      The current status of the build phase. Valid values include:

      * ``FAILED`` : The build phase failed.

      * ``FAULT`` : The build phase faulted.

      * ``IN_PROGRESS`` : The build phase is still in progress.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

      * ``STOPPED`` : The build phase stopped.

      * ``SUCCEEDED`` : The build phase succeeded.

      * ``TIMED_OUT`` : The build phase timed out.

    - **startTime** *(datetime) --*

      When the build phase started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build phase ended, expressed in Unix time format.

    - **durationInSeconds** *(integer) --*

      How long, in seconds, between the starting and ending times of the build's phase.

    - **contexts** *(list) --*

      Additional information about a build phase, especially to help troubleshoot a failed
      build.

      - *(dict) --*

        Additional information about a build phase that has an error. You can use this
        information for troubleshooting.

        - **statusCode** *(string) --*

          The status code for the context of the build phase.

        - **message** *(string) --*

          An explanation of the build phase's context. This might include a command ID and an
          exit code.
    """


_ClientStartBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsecondaryArtifactsTypeDef(
    _ClientStartBuildResponsebuildsecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `secondaryArtifacts`

    Information about build output artifacts.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef(
    _ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
      name is specified, the branch's HEAD commit ID is used. If not specified, the default
      branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
      is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientStartBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesauthTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientStartBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientStartBuildResponsebuildsourceauthTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStartBuildResponsebuildsourceauthTypeDef(
    _ClientStartBuildResponsebuildsourceauthTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code
    to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or
    set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef(
    _ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuildsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientStartBuildResponsebuildsourceTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsourceTypeDef(
    _ClientStartBuildResponsebuildsourceTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `source`

    Information about the source code to be built.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
      action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
      that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your GitHub
      account. Use the AWS CodeBuild console to start creating a build project. When you use
      the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to each
      repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
      application** . (After you have connected to your GitHub account, you do not need to
      finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
      AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
      ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
      access to your account** page, choose **Grant access** . (After you have connected to
      your Bitbucket account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code
      to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code
      to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or
      set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientStartBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientStartBuildResponsebuildvpcConfigTypeDef(
    _ClientStartBuildResponsebuildvpcConfigTypeDef
):
    """
    Type definition for `ClientStartBuildResponsebuild` `vpcConfig`

    If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
    parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
    security groups and subnets must belong to the same VPC. You must provide at least one
    security group and one subnet ID.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientStartBuildResponsebuildTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": str,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStartBuildResponsebuildphasesTypeDef],
        "source": ClientStartBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStartBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientStartBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientStartBuildResponsebuildsecondaryArtifactsTypeDef
        ],
        "cache": ClientStartBuildResponsebuildcacheTypeDef,
        "environment": ClientStartBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStartBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStartBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStartBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
    },
    total=False,
)


class ClientStartBuildResponsebuildTypeDef(_ClientStartBuildResponsebuildTypeDef):
    """
    Type definition for `ClientStartBuildResponse` `build`

    Information about the build to be run.

    - **id** *(string) --*

      The unique ID for the build.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build.

    - **buildNumber** *(integer) --*

      The number of the build. For each project, the ``buildNumber`` of its first build is ``1``
      . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build is
      deleted, the ``buildNumber`` of other builds does not change.

    - **startTime** *(datetime) --*

      When the build process started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build process ended, expressed in Unix time format.

    - **currentPhase** *(string) --*

      The current build phase.

    - **buildStatus** *(string) --*

      The current status of the build. Valid values include:

      * ``FAILED`` : The build failed.

      * ``FAULT`` : The build faulted.

      * ``IN_PROGRESS`` : The build is still in progress.

      * ``STOPPED`` : The build stopped.

      * ``SUCCEEDED`` : The build succeeded.

      * ``TIMED_OUT`` : The build timed out.

    - **sourceVersion** *(string) --*

      Any version identifier for the version of the source code to be built. If ``sourceVersion``
      is specified at the project level, then this ``sourceVersion`` (at the build level) takes
      precedence.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **resolvedSourceVersion** *(string) --*

      An identifier for the version of this build's source code.

      * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

      * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

      * For Amazon Simple Storage Service (Amazon S3), this does not apply.

    - **projectName** *(string) --*

      The name of the AWS CodeBuild project.

    - **phases** *(list) --*

      Information about all previous build phases that are complete and information about any
      current build phase that is not yet complete.

      - *(dict) --*

        Information about a stage for a build.

        - **phaseType** *(string) --*

          The name of the build phase. Valid values include:

          * ``BUILD`` : Core build activities typically occur in this build phase.

          * ``COMPLETED`` : The build has been completed.

          * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

          * ``FINALIZING`` : The build process is completing in this build phase.

          * ``INSTALL`` : Installation activities typically occur in this build phase.

          * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

          * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

          * ``PROVISIONING`` : The build environment is being set up.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

          * ``SUBMITTED`` : The build has been submitted.

          * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
          location.

        - **phaseStatus** *(string) --*

          The current status of the build phase. Valid values include:

          * ``FAILED`` : The build phase failed.

          * ``FAULT`` : The build phase faulted.

          * ``IN_PROGRESS`` : The build phase is still in progress.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

          * ``STOPPED`` : The build phase stopped.

          * ``SUCCEEDED`` : The build phase succeeded.

          * ``TIMED_OUT`` : The build phase timed out.

        - **startTime** *(datetime) --*

          When the build phase started, expressed in Unix time format.

        - **endTime** *(datetime) --*

          When the build phase ended, expressed in Unix time format.

        - **durationInSeconds** *(integer) --*

          How long, in seconds, between the starting and ending times of the build's phase.

        - **contexts** *(list) --*

          Additional information about a build phase, especially to help troubleshoot a failed
          build.

          - *(dict) --*

            Additional information about a build phase that has an error. You can use this
            information for troubleshooting.

            - **statusCode** *(string) --*

              The status code for the context of the build phase.

            - **message** *(string) --*

              An explanation of the build phase's context. This might include a command ID and an
              exit code.

    - **source** *(dict) --*

      Information about the source code to be built.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
        ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
        action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
        that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your GitHub
        account. Use the AWS CodeBuild console to start creating a build project. When you use
        the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to each
        repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
        application** . (After you have connected to your GitHub account, you do not need to
        finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
        AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
        ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
        access to your account** page, choose **Grant access** . (After you have connected to
        your Bitbucket account, you do not need to finish creating the build project. You can
        leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
        the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source code
        to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source code
        to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get or
        set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the
          OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
          When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
          **Confirm access to your account** page, choose **Grant access** . (After you have
          connected to your Bitbucket account, you do not need to finish creating the build
          project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
          this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
          ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get
          or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it
      must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit
      ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
          name is specified, the branch's HEAD commit ID is used. If not specified, the default
          branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
          is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the output artifacts for the build.

      - **location** *(string) --*

        Information about the location of the build artifacts.

      - **sha256sum** *(string) --*

        The SHA-256 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **md5sum** *(string) --*

        The MD5 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact name.
        The name specified in a build spec file is calculated at build time and uses the Shell
        Command Language. For example, you can append a date and time to your artifact name so
        that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Information that tells you if encryption for build artifacts is disabled.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about build output artifacts.

        - **location** *(string) --*

          Information about the location of the build artifacts.

        - **sha256sum** *(string) --*

          The SHA-256 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **md5sum** *(string) --*

          The MD5 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses the
          Shell Command Language. For example, you can append a date and time to your artifact
          name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Information that tells you if encryption for build artifacts is disabled.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits. This
        mode is a good choice for projects with a clean working directory and a source that is a
        large Git repository. If you choose this option and your project does not use a Git
        repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
        mode is a good choice if your build scenario is not suited to one of the other three
        local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project sources.
          Cached items are overriden if a source item has the same name. Directories are
          specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an image
        with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive values,
              especially AWS secret key IDs and secret access keys. Environment variables can be
              displayed in plain text using the AWS CodeBuild console and the AWS Command Line
              Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
            Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding one
        of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The valid
          value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
        you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The name of a service role used for this build.

    - **logs** *(dict) --*

      Information about the build's logs in Amazon CloudWatch Logs.

      - **groupName** *(string) --*

        The name of the Amazon CloudWatch Logs group for the build logs.

      - **streamName** *(string) --*

        The name of the Amazon CloudWatch Logs stream for the build logs.

      - **deepLink** *(string) --*

        The URL to an individual build log in Amazon CloudWatch Logs.

      - **s3DeepLink** *(string) --*

        The URL to a build log in an S3 bucket.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about S3 logs for a build project.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
          is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
          ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3 build
          logs are encrypted.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not
      get marked as completed.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **buildComplete** *(boolean) --*

      Whether the build is complete. True if complete; otherwise, false.

    - **initiator** *(string) --*

      The entity that started the build. Valid values include:

      * If AWS CodePipeline started the build, the pipeline's name (for example,
      ``codepipeline/my-demo-pipeline`` ).

      * If an AWS Identity and Access Management (IAM) user started the build, the user's name
      (for example, ``MyUserName`` ).

      * If the Jenkins plugin for AWS CodeBuild started the build, the string
      ``CodeBuild-Jenkins-Plugin`` .

    - **vpcConfig** *(dict) --*

      If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
      parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
      security groups and subnets must belong to the same VPC. You must provide at least one
      security group and one subnet ID.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **networkInterface** *(dict) --*

      Describes a network interface.

      - **subnetId** *(string) --*

        The ID of the subnet.

      - **networkInterfaceId** *(string) --*

        The ID of the network interface.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your service
        role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **exportedEnvironmentVariables** *(list) --*

      A list of exported environment variables for this build.

      - *(dict) --*

        Information about an exported environment variable.

        - **name** *(string) --*

          The name of this exported environment variable.

        - **value** *(string) --*

          The value assigned to this exported environment variable.

          .. note::

            During a build, the value of a variable is available starting with the ``install``
            phase. It can be updated between the start of the ``install`` phase and the end of
            the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
            variables cannot change.
    """


_ClientStartBuildResponseTypeDef = TypedDict(
    "_ClientStartBuildResponseTypeDef",
    {"build": ClientStartBuildResponsebuildTypeDef},
    total=False,
)


class ClientStartBuildResponseTypeDef(_ClientStartBuildResponseTypeDef):
    """
    Type definition for `ClientStartBuild` `Response`

    - **build** *(dict) --*

      Information about the build to be run.

      - **id** *(string) --*

        The unique ID for the build.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the build.

      - **buildNumber** *(integer) --*

        The number of the build. For each project, the ``buildNumber`` of its first build is ``1``
        . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build is
        deleted, the ``buildNumber`` of other builds does not change.

      - **startTime** *(datetime) --*

        When the build process started, expressed in Unix time format.

      - **endTime** *(datetime) --*

        When the build process ended, expressed in Unix time format.

      - **currentPhase** *(string) --*

        The current build phase.

      - **buildStatus** *(string) --*

        The current status of the build. Valid values include:

        * ``FAILED`` : The build failed.

        * ``FAULT`` : The build faulted.

        * ``IN_PROGRESS`` : The build is still in progress.

        * ``STOPPED`` : The build stopped.

        * ``SUCCEEDED`` : The build succeeded.

        * ``TIMED_OUT`` : The build timed out.

      - **sourceVersion** *(string) --*

        Any version identifier for the version of the source code to be built. If ``sourceVersion``
        is specified at the project level, then this ``sourceVersion`` (at the build level) takes
        precedence.

        For more information, see `Source Version Sample with CodeBuild
        <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
        the *AWS CodeBuild User Guide* .

      - **resolvedSourceVersion** *(string) --*

        An identifier for the version of this build's source code.

        * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

        * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

        * For Amazon Simple Storage Service (Amazon S3), this does not apply.

      - **projectName** *(string) --*

        The name of the AWS CodeBuild project.

      - **phases** *(list) --*

        Information about all previous build phases that are complete and information about any
        current build phase that is not yet complete.

        - *(dict) --*

          Information about a stage for a build.

          - **phaseType** *(string) --*

            The name of the build phase. Valid values include:

            * ``BUILD`` : Core build activities typically occur in this build phase.

            * ``COMPLETED`` : The build has been completed.

            * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

            * ``FINALIZING`` : The build process is completing in this build phase.

            * ``INSTALL`` : Installation activities typically occur in this build phase.

            * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

            * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

            * ``PROVISIONING`` : The build environment is being set up.

            * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

            * ``SUBMITTED`` : The build has been submitted.

            * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
            location.

          - **phaseStatus** *(string) --*

            The current status of the build phase. Valid values include:

            * ``FAILED`` : The build phase failed.

            * ``FAULT`` : The build phase faulted.

            * ``IN_PROGRESS`` : The build phase is still in progress.

            * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

            * ``STOPPED`` : The build phase stopped.

            * ``SUCCEEDED`` : The build phase succeeded.

            * ``TIMED_OUT`` : The build phase timed out.

          - **startTime** *(datetime) --*

            When the build phase started, expressed in Unix time format.

          - **endTime** *(datetime) --*

            When the build phase ended, expressed in Unix time format.

          - **durationInSeconds** *(integer) --*

            How long, in seconds, between the starting and ending times of the build's phase.

          - **contexts** *(list) --*

            Additional information about a build phase, especially to help troubleshoot a failed
            build.

            - *(dict) --*

              Additional information about a build phase that has an error. You can use this
              information for troubleshooting.

              - **statusCode** *(string) --*

                The status code for the context of the build phase.

              - **message** *(string) --*

                An explanation of the build phase's context. This might include a command ID and an
                exit code.

      - **source** *(dict) --*

        Information about the source code to be built.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
          ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
          action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
          that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your GitHub
          account. Use the AWS CodeBuild console to start creating a build project. When you use
          the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to each
          repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
          application** . (After you have connected to your GitHub account, you do not need to
          finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
          AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
          ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
          access to your account** page, choose **Grant access** . (After you have connected to
          your Bitbucket account, you do not need to finish creating the build project. You can
          leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
          the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source code
          to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source code
          to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get or
          set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents the
            OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

      - **secondarySources** *(list) --*

        An array of ``ProjectSource`` objects.

        - *(dict) --*

          Information about the build input source code for the build project.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

      - **secondarySourceVersions** *(list) --*

        An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of:

        * For AWS CodeCommit: the commit ID to use.

        * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
        the version of the source code you want to build. If a pull request ID is specified, it
        must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
        specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
        commit ID is used.

        * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
        the source code you want to build. If a branch name is specified, the branch's HEAD commit
        ID is used. If not specified, the default branch's HEAD commit ID is used.

        * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
        represents the build input ZIP file to use.

        - *(dict) --*

          A source identifier and its corresponding version.

          - **sourceIdentifier** *(string) --*

            An identifier for a source in the build project.

          - **sourceVersion** *(string) --*

            The source version for the corresponding source identifier. If specified, must be one
            of:

            * For AWS CodeCommit: the commit ID to use.

            * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
            to the version of the source code you want to build. If a pull request ID is specified,
            it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
            name is specified, the branch's HEAD commit ID is used. If not specified, the default
            branch's HEAD commit ID is used.

            * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
            version of the source code you want to build. If a branch name is specified, the
            branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
            is used.

            * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
            represents the build input ZIP file to use.

            For more information, see `Source Version Sample with CodeBuild
            <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
            in the *AWS CodeBuild User Guide* .

      - **artifacts** *(dict) --*

        Information about the output artifacts for the build.

        - **location** *(string) --*

          Information about the location of the build artifacts.

        - **sha256sum** *(string) --*

          The SHA-256 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **md5sum** *(string) --*

          The MD5 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact name.
          The name specified in a build spec file is calculated at build time and uses the Shell
          Command Language. For example, you can append a date and time to your artifact name so
          that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Information that tells you if encryption for build artifacts is disabled.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

      - **secondaryArtifacts** *(list) --*

        An array of ``ProjectArtifacts`` objects.

        - *(dict) --*

          Information about build output artifacts.

          - **location** *(string) --*

            Information about the location of the build artifacts.

          - **sha256sum** *(string) --*

            The SHA-256 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **md5sum** *(string) --*

            The MD5 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Information that tells you if encryption for build artifacts is disabled.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

      - **cache** *(dict) --*

        Information about the cache for the build.

        - **type** *(string) --*

          The type of cache used by the build project. Valid values include:

          * ``NO_CACHE`` : The build project does not use any cache.

          * ``S3`` : The build project reads and writes from and to S3.

          * ``LOCAL`` : The build project stores a cache locally on a build host that is only
          available to that build host.

        - **location** *(string) --*

          Information about the cache location:

          * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

          * ``S3`` : This is the S3 bucket name/prefix.

        - **modes** *(list) --*

          If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
          modes at the same time.

          * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
          After the cache is created, subsequent builds pull only the change between commits. This
          mode is a good choice for projects with a clean working directory and a source that is a
          large Git repository. If you choose this option and your project does not use a Git
          repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

          * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
          choice for projects that build or pull large Docker images. It can prevent the
          performance issues caused by pulling large Docker images down from the network.

          .. note::

              * You can use a Docker layer cache in the Linux environment only.

              * The ``privileged`` flag must be set so that your project has the required Docker
              permissions.

              * You should consider the security implications before you use a Docker layer cache.

          * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
          mode is a good choice if your build scenario is not suited to one of the other three
          local cache modes. If you use a custom cache:

            * Only directories can be specified for caching. You cannot specify individual files.

            * Symlinks are used to reference cached directories.

            * Cached directories are linked to your build before it downloads its project sources.
            Cached items are overriden if a source item has the same name. Directories are
            specified using cache paths in the buildspec file.

          - *(string) --*

      - **environment** *(dict) --*

        Information about the build environment for this build.

        - **type** *(string) --*

          The type of build environment to use for related builds.

        - **image** *(string) --*

          The image tag or image digest that identifies the Docker image to use for this build
          project. Use the following formats:

          * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
          the tag "latest," use ``registry/repository:latest`` .

          * For an image digest: ``registry/repository@digest`` . For example, to specify an image
          with the digest
          "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
          ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
          .

        - **computeType** *(string) --*

          Information about the compute resources the build project uses. Available values include:

          * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

          * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

          * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

          For more information, see `Build Environment Compute Types
          <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
          in the *AWS CodeBuild User Guide.*

        - **environmentVariables** *(list) --*

          A set of environment variables to make available to builds for this build project.

          - *(dict) --*

            Information about an environment variable for a build project or a build.

            - **name** *(string) --*

              The name or key of the environment variable.

            - **value** *(string) --*

              The value of the environment variable.

              .. warning::

                We strongly discourage the use of environment variables to store sensitive values,
                especially AWS secret key IDs and secret access keys. Environment variables can be
                displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                Interface (AWS CLI).

            - **type** *(string) --*

              The type of environment variable. Valid values include:

              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
              Parameter Store.

              * ``PLAINTEXT`` : An environment variable in plaintext format.

              * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

        - **privilegedMode** *(boolean) --*

          Enables running the Docker daemon inside a Docker container. Set to true only if the
          build project is used to build Docker images. Otherwise, a build that attempts to
          interact with the Docker daemon fails. The default setting is ``false`` .

          You can initialize the Docker daemon during the install phase of your build by adding one
          of the following sets of commands to the install phase of your buildspec file:

          If the operating system's base image is Ubuntu Linux:

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

          If the operating system's base image is Alpine Linux and the previous command does not
          work, add the ``-t`` argument to ``timeout`` :

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

        - **certificate** *(string) --*

          The certificate to use with this build project.

        - **registryCredential** *(dict) --*

          The credentials for access to a private registry.

          - **credential** *(string) --*

            The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

            .. note::

              The ``credential`` can use the name of the credentials only if they exist in your
              current region.

          - **credentialProvider** *(string) --*

            The service that created the credentials to access a private Docker registry. The valid
            value, SECRETS_MANAGER, is for AWS Secrets Manager.

        - **imagePullCredentialsType** *(string) --*

          The type of credentials AWS CodeBuild uses to pull images in your build. There are two
          valid values:

          * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
          you modify your ECR repository policy to trust AWS CodeBuild's service principal.

          * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

          When you use a cross-account or private registry image, you must use SERVICE_ROLE
          credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
          credentials.

      - **serviceRole** *(string) --*

        The name of a service role used for this build.

      - **logs** *(dict) --*

        Information about the build's logs in Amazon CloudWatch Logs.

        - **groupName** *(string) --*

          The name of the Amazon CloudWatch Logs group for the build logs.

        - **streamName** *(string) --*

          The name of the Amazon CloudWatch Logs stream for the build logs.

        - **deepLink** *(string) --*

          The URL to an individual build log in Amazon CloudWatch Logs.

        - **s3DeepLink** *(string) --*

          The URL to a build log in an S3 bucket.

        - **cloudWatchLogs** *(dict) --*

          Information about Amazon CloudWatch Logs for a build project.

          - **status** *(string) --*

            The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
            values are:

            * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

            * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

          - **groupName** *(string) --*

            The group name of the logs in Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

          - **streamName** *(string) --*

            The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

        - **s3Logs** *(dict) --*

          Information about S3 logs for a build project.

          - **status** *(string) --*

            The current status of the S3 build logs. Valid values are:

            * ``ENABLED`` : S3 build logs are enabled for this build project.

            * ``DISABLED`` : S3 build logs are not enabled for this build project.

          - **location** *(string) --*

            The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
            is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
            ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your S3 build log output encrypted. By default S3 build
            logs are encrypted.

      - **timeoutInMinutes** *(integer) --*

        How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not
        get marked as completed.

      - **queuedTimeoutInMinutes** *(integer) --*

        The number of minutes a build is allowed to be queued before it times out.

      - **buildComplete** *(boolean) --*

        Whether the build is complete. True if complete; otherwise, false.

      - **initiator** *(string) --*

        The entity that started the build. Valid values include:

        * If AWS CodePipeline started the build, the pipeline's name (for example,
        ``codepipeline/my-demo-pipeline`` ).

        * If an AWS Identity and Access Management (IAM) user started the build, the user's name
        (for example, ``MyUserName`` ).

        * If the Jenkins plugin for AWS CodeBuild started the build, the string
        ``CodeBuild-Jenkins-Plugin`` .

      - **vpcConfig** *(dict) --*

        If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
        parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
        security groups and subnets must belong to the same VPC. You must provide at least one
        security group and one subnet ID.

        - **vpcId** *(string) --*

          The ID of the Amazon VPC.

        - **subnets** *(list) --*

          A list of one or more subnet IDs in your Amazon VPC.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          A list of one or more security groups IDs in your Amazon VPC.

          - *(string) --*

      - **networkInterface** *(dict) --*

        Describes a network interface.

        - **subnetId** *(string) --*

          The ID of the subnet.

        - **networkInterfaceId** *(string) --*

          The ID of the network interface.

      - **encryptionKey** *(string) --*

        The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
        encrypting the build output artifacts.

        .. note::

          You can use a cross-account KMS key to encrypt the build output artifacts if your service
          role has permission to that key.

        You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
        CMK's alias (using the format ``alias/*alias-name* `` ).

      - **exportedEnvironmentVariables** *(list) --*

        A list of exported environment variables for this build.

        - *(dict) --*

          Information about an exported environment variable.

          - **name** *(string) --*

            The name of this exported environment variable.

          - **value** *(string) --*

            The value assigned to this exported environment variable.

            .. note::

              During a build, the value of a variable is available starting with the ``install``
              phase. It can be updated between the start of the ``install`` phase and the end of
              the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
              variables cannot change.
    """


_RequiredClientStartBuildartifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildartifactsOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildartifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildartifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildartifactsOverrideTypeDef(
    _RequiredClientStartBuildartifactsOverrideTypeDef,
    _OptionalClientStartBuildartifactsOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `artifactsOverride`

    Build output artifact settings that override, for this build only, the latest ones already
    defined in the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and
      ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output bucket at
      ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the
      name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/`` ",
      the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_RequiredClientStartBuildcacheOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildcacheOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildcacheOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildcacheOverrideTypeDef",
    {"location": str, "modes": List[str]},
    total=False,
)


class ClientStartBuildcacheOverrideTypeDef(
    _RequiredClientStartBuildcacheOverrideTypeDef,
    _OptionalClientStartBuildcacheOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `cacheOverride`

    A ProjectCache object specified for this build that overrides the one defined in the build
    project.

    - **type** *(string) --* **[REQUIRED]**

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache modes
      at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources. After the
      cache is created, subsequent builds pull only the change between commits. This mode is a good
      choice for projects with a clean working directory and a source that is a large Git repository.
      If you choose this option and your project does not use a Git repository (GitHub, GitHub
      Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good choice
      for projects that build or pull large Docker images. It can prevent the performance issues
      caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This mode
      is a good choice if your build scenario is not suited to one of the other three local cache
      modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources. Cached
        items are overriden if a source item has the same name. Directories are specified using cache
        paths in the buildspec file.

      - *(string) --*
    """


_RequiredClientStartBuildenvironmentVariablesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildenvironmentVariablesOverrideTypeDef",
    {"name": str, "value": str},
)
_OptionalClientStartBuildenvironmentVariablesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildenvironmentVariablesOverrideTypeDef",
    {"type": str},
    total=False,
)


class ClientStartBuildenvironmentVariablesOverrideTypeDef(
    _RequiredClientStartBuildenvironmentVariablesOverrideTypeDef,
    _OptionalClientStartBuildenvironmentVariablesOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `environmentVariablesOverride`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --* **[REQUIRED]**

      The name or key of the environment variable.

    - **value** *(string) --* **[REQUIRED]**

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface
        (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientStartBuildgitSubmodulesConfigOverrideTypeDef = TypedDict(
    "_ClientStartBuildgitSubmodulesConfigOverrideTypeDef", {"fetchSubmodules": bool}
)


class ClientStartBuildgitSubmodulesConfigOverrideTypeDef(
    _ClientStartBuildgitSubmodulesConfigOverrideTypeDef
):
    """
    Type definition for `ClientStartBuild` `gitSubmodulesConfigOverride`

    Information about the Git submodules configuration for this build of an AWS CodeBuild build
    project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef", {"status": str}
)
_OptionalClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef(
    _RequiredClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef,
    _OptionalClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef,
):
    """
    Type definition for `ClientStartBuildlogsConfigOverride` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
    enabled by default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
      are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
      Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_RequiredClientStartBuildlogsConfigOverrides3LogsTypeDef = TypedDict(
    "_RequiredClientStartBuildlogsConfigOverrides3LogsTypeDef", {"status": str}
)
_OptionalClientStartBuildlogsConfigOverrides3LogsTypeDef = TypedDict(
    "_OptionalClientStartBuildlogsConfigOverrides3LogsTypeDef",
    {"location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStartBuildlogsConfigOverrides3LogsTypeDef(
    _RequiredClientStartBuildlogsConfigOverrides3LogsTypeDef,
    _OptionalClientStartBuildlogsConfigOverrides3LogsTypeDef,
):
    """
    Type definition for `ClientStartBuildlogsConfigOverride` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
    default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
      ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
      are encrypted.
    """


_ClientStartBuildlogsConfigOverrideTypeDef = TypedDict(
    "_ClientStartBuildlogsConfigOverrideTypeDef",
    {
        "cloudWatchLogs": ClientStartBuildlogsConfigOverridecloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildlogsConfigOverrides3LogsTypeDef,
    },
    total=False,
)


class ClientStartBuildlogsConfigOverrideTypeDef(
    _ClientStartBuildlogsConfigOverrideTypeDef
):
    """
    Type definition for `ClientStartBuild` `logsConfigOverride`

    Log settings for this build that override the log settings defined in the build project.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
        Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
      default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
        ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
        are encrypted.
    """


_ClientStartBuildregistryCredentialOverrideTypeDef = TypedDict(
    "_ClientStartBuildregistryCredentialOverrideTypeDef",
    {"credential": str, "credentialProvider": str},
)


class ClientStartBuildregistryCredentialOverrideTypeDef(
    _ClientStartBuildregistryCredentialOverrideTypeDef
):
    """
    Type definition for `ClientStartBuild` `registryCredentialOverride`

    The credentials for access to a private registry.

    - **credential** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your current
        region.

    - **credentialProvider** *(string) --* **[REQUIRED]**

      The service that created the credentials to access a private Docker registry. The valid value,
      SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_RequiredClientStartBuildsecondaryArtifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildsecondaryArtifactsOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildsecondaryArtifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildsecondaryArtifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildsecondaryArtifactsOverrideTypeDef(
    _RequiredClientStartBuildsecondaryArtifactsOverrideTypeDef,
    _OptionalClientStartBuildsecondaryArtifactsOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `secondaryArtifactsOverride`

    Information about the build output artifacts for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
      bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
      , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set
      the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/``
      ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_RequiredClientStartBuildsecondarySourcesOverrideauthTypeDef = TypedDict(
    "_RequiredClientStartBuildsecondarySourcesOverrideauthTypeDef", {"type": str}
)
_OptionalClientStartBuildsecondarySourcesOverrideauthTypeDef = TypedDict(
    "_OptionalClientStartBuildsecondarySourcesOverrideauthTypeDef",
    {"resource": str},
    total=False,
)


class ClientStartBuildsecondarySourcesOverrideauthTypeDef(
    _RequiredClientStartBuildsecondarySourcesOverrideauthTypeDef,
    _OptionalClientStartBuildsecondarySourcesOverrideauthTypeDef,
):
    """
    Type definition for `ClientStartBuildsecondarySourcesOverride` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code to
    be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or set
    this information directly.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStartBuildsecondarySourcesOverridegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildsecondarySourcesOverridegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
)


class ClientStartBuildsecondarySourcesOverridegitSubmodulesConfigTypeDef(
    _ClientStartBuildsecondarySourcesOverridegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientStartBuildsecondarySourcesOverride` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientStartBuildsecondarySourcesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildsecondarySourcesOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildsecondarySourcesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildsecondarySourcesOverrideTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildsecondarySourcesOverridegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildsecondarySourcesOverrideauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildsecondarySourcesOverrideTypeDef(
    _RequiredClientStartBuildsecondarySourcesOverrideTypeDef,
    _OptionalClientStartBuildsecondarySourcesOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `secondarySourcesOverride`

    Information about the build input source code for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action
      instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that
      contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the
      following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains
      the source and the build spec. You must connect your AWS account to your GitHub account. Use
      the AWS CodeBuild console to start creating a build project. When you use the console to
      connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for
      **Organization access** , choose **Request access** next to each repository you want to allow
      AWS CodeBuild to have access to, and then choose **Authorize application** . (After you have
      connected to your GitHub account, you do not need to finish creating the build project. You
      can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your Bitbucket
      account. Use the AWS CodeBuild console to start creating a build project. When you use the
      console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your
      account** page, choose **Grant access** . (After you have connected to your Bitbucket
      account, you do not need to finish creating the build project. You can leave the AWS
      CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the ``source``
      object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code to
      be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code to
      be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or set
      this information directly.

      - **type** *(string) --* **[REQUIRED]**

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider. This
      option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If
      this is set and you use a different source provider, an invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientStartBuildsecondarySourcesVersionOverrideTypeDef = TypedDict(
    "_ClientStartBuildsecondarySourcesVersionOverrideTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
)


class ClientStartBuildsecondarySourcesVersionOverrideTypeDef(
    _ClientStartBuildsecondarySourcesVersionOverrideTypeDef
):
    """
    Type definition for `ClientStartBuild` `secondarySourcesVersionOverride`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --* **[REQUIRED]**

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --* **[REQUIRED]**

      The source version for the corresponding source identifier. If specified, must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it must
      use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit ID
      is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents
      the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in the
      *AWS CodeBuild User Guide* .
    """


_RequiredClientStartBuildsourceAuthOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildsourceAuthOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildsourceAuthOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildsourceAuthOverrideTypeDef", {"resource": str}, total=False
)


class ClientStartBuildsourceAuthOverrideTypeDef(
    _RequiredClientStartBuildsourceAuthOverrideTypeDef,
    _OptionalClientStartBuildsourceAuthOverrideTypeDef,
):
    """
    Type definition for `ClientStartBuild` `sourceAuthOverride`

    An authorization type for this build that overrides the one defined in the build project. This
    override applies only if the build project's source is BitBucket or GitHub.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth
      authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStopBuildResponsebuildartifactsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildartifactsTypeDef(
    _ClientStopBuildResponsebuildartifactsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `artifacts`

    Information about the output artifacts for the build.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name.
      The name specified in a build spec file is calculated at build time and uses the Shell
      Command Language. For example, you can append a date and time to your artifact name so
      that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientStopBuildResponsebuildcacheTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildcacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientStopBuildResponsebuildcacheTypeDef(
    _ClientStopBuildResponsebuildcacheTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `cache`

    Information about the cache for the build.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits. This
      mode is a good choice for projects with a clean working directory and a source that is a
      large Git repository. If you choose this option and your project does not use a Git
      repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
      mode is a good choice if your build scenario is not suited to one of the other three
      local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources.
        Cached items are overriden if a source item has the same name. Directories are
        specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef(
    _ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef(
    _ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientStopBuildResponsebuildenvironmentTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildenvironmentTypeDef(
    _ClientStopBuildResponsebuildenvironmentTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `environment`

    Information about the build environment for this build.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image
      with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one
      of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
      you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef(
    _ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `exportedEnvironmentVariables`

    Information about an exported environment variable.

    - **name** *(string) --*

      The name of this exported environment variable.

    - **value** *(string) --*

      The value assigned to this exported environment variable.

      .. note::

        During a build, the value of a variable is available starting with the ``install``
        phase. It can be updated between the start of the ``install`` phase and the end of
        the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
        variables cannot change.
    """


_ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef(
    _ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildlogs` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientStopBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogss3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStopBuildResponsebuildlogss3LogsTypeDef(
    _ClientStopBuildResponsebuildlogss3LogsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildlogs` `s3Logs`

    Information about S3 logs for a build project.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
      is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build
      logs are encrypted.
    """


_ClientStopBuildResponsebuildlogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogs": ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStopBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)


class ClientStopBuildResponsebuildlogsTypeDef(_ClientStopBuildResponsebuildlogsTypeDef):
    """
    Type definition for `ClientStopBuildResponsebuild` `logs`

    Information about the build's logs in Amazon CloudWatch Logs.

    - **groupName** *(string) --*

      The name of the Amazon CloudWatch Logs group for the build logs.

    - **streamName** *(string) --*

      The name of the Amazon CloudWatch Logs stream for the build logs.

    - **deepLink** *(string) --*

      The URL to an individual build log in Amazon CloudWatch Logs.

    - **s3DeepLink** *(string) --*

      The URL to a build log in an S3 bucket.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about S3 logs for a build project.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
        is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build
        logs are encrypted.
    """


_ClientStopBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientStopBuildResponsebuildnetworkInterfaceTypeDef(
    _ClientStopBuildResponsebuildnetworkInterfaceTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `networkInterface`

    Describes a network interface.

    - **subnetId** *(string) --*

      The ID of the subnet.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.
    """


_ClientStopBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientStopBuildResponsebuildphasescontextsTypeDef(
    _ClientStopBuildResponsebuildphasescontextsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildphases` `contexts`

    Additional information about a build phase that has an error. You can use this
    information for troubleshooting.

    - **statusCode** *(string) --*

      The status code for the context of the build phase.

    - **message** *(string) --*

      An explanation of the build phase's context. This might include a command ID and an
      exit code.
    """


_ClientStopBuildResponsebuildphasesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildphasesTypeDef",
    {
        "phaseType": str,
        "phaseStatus": str,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStopBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)


class ClientStopBuildResponsebuildphasesTypeDef(
    _ClientStopBuildResponsebuildphasesTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `phases`

    Information about a stage for a build.

    - **phaseType** *(string) --*

      The name of the build phase. Valid values include:

      * ``BUILD`` : Core build activities typically occur in this build phase.

      * ``COMPLETED`` : The build has been completed.

      * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

      * ``FINALIZING`` : The build process is completing in this build phase.

      * ``INSTALL`` : Installation activities typically occur in this build phase.

      * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

      * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

      * ``PROVISIONING`` : The build environment is being set up.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

      * ``SUBMITTED`` : The build has been submitted.

      * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
      location.

    - **phaseStatus** *(string) --*

      The current status of the build phase. Valid values include:

      * ``FAILED`` : The build phase failed.

      * ``FAULT`` : The build phase faulted.

      * ``IN_PROGRESS`` : The build phase is still in progress.

      * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

      * ``STOPPED`` : The build phase stopped.

      * ``SUCCEEDED`` : The build phase succeeded.

      * ``TIMED_OUT`` : The build phase timed out.

    - **startTime** *(datetime) --*

      When the build phase started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build phase ended, expressed in Unix time format.

    - **durationInSeconds** *(integer) --*

      How long, in seconds, between the starting and ending times of the build's phase.

    - **contexts** *(list) --*

      Additional information about a build phase, especially to help troubleshoot a failed
      build.

      - *(dict) --*

        Additional information about a build phase that has an error. You can use this
        information for troubleshooting.

        - **statusCode** *(string) --*

          The status code for the context of the build phase.

        - **message** *(string) --*

          An explanation of the build phase's context. This might include a command ID and an
          exit code.
    """


_ClientStopBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsecondaryArtifactsTypeDef(
    _ClientStopBuildResponsebuildsecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `secondaryArtifacts`

    Information about build output artifacts.

    - **location** *(string) --*

      Information about the location of the build artifacts.

    - **sha256sum** *(string) --*

      The SHA-256 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **md5sum** *(string) --*

      The MD5 hash of the build artifact.

      You can use this hash along with a checksum tool to confirm file integrity and
      authenticity.

      .. note::

        This value is available only if the build project's ``packaging`` value is set to
        ``ZIP`` .

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Information that tells you if encryption for build artifacts is disabled.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef(
    _ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
      name is specified, the branch's HEAD commit ID is used. If not specified, the default
      branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
      is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientStopBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesauthTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientStopBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientStopBuildResponsebuildsourceauthTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStopBuildResponsebuildsourceauthTypeDef(
    _ClientStopBuildResponsebuildsourceauthTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code
    to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or
    set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef(
    _ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuildsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientStopBuildResponsebuildsourceTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsourceTypeDef(
    _ClientStopBuildResponsebuildsourceTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `source`

    Information about the source code to be built.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
      action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
      that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your GitHub
      account. Use the AWS CodeBuild console to start creating a build project. When you use
      the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to each
      repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
      application** . (After you have connected to your GitHub account, you do not need to
      finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
      AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
      ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
      access to your account** page, choose **Grant access** . (After you have connected to
      your Bitbucket account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code
      to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code
      to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or
      set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientStopBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientStopBuildResponsebuildvpcConfigTypeDef(
    _ClientStopBuildResponsebuildvpcConfigTypeDef
):
    """
    Type definition for `ClientStopBuildResponsebuild` `vpcConfig`

    If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
    parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
    security groups and subnets must belong to the same VPC. You must provide at least one
    security group and one subnet ID.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientStopBuildResponsebuildTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": str,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStopBuildResponsebuildphasesTypeDef],
        "source": ClientStopBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStopBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientStopBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientStopBuildResponsebuildsecondaryArtifactsTypeDef
        ],
        "cache": ClientStopBuildResponsebuildcacheTypeDef,
        "environment": ClientStopBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStopBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStopBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStopBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
    },
    total=False,
)


class ClientStopBuildResponsebuildTypeDef(_ClientStopBuildResponsebuildTypeDef):
    """
    Type definition for `ClientStopBuildResponse` `build`

    Information about the build.

    - **id** *(string) --*

      The unique ID for the build.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build.

    - **buildNumber** *(integer) --*

      The number of the build. For each project, the ``buildNumber`` of its first build is ``1``
      . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build is
      deleted, the ``buildNumber`` of other builds does not change.

    - **startTime** *(datetime) --*

      When the build process started, expressed in Unix time format.

    - **endTime** *(datetime) --*

      When the build process ended, expressed in Unix time format.

    - **currentPhase** *(string) --*

      The current build phase.

    - **buildStatus** *(string) --*

      The current status of the build. Valid values include:

      * ``FAILED`` : The build failed.

      * ``FAULT`` : The build faulted.

      * ``IN_PROGRESS`` : The build is still in progress.

      * ``STOPPED`` : The build stopped.

      * ``SUCCEEDED`` : The build succeeded.

      * ``TIMED_OUT`` : The build timed out.

    - **sourceVersion** *(string) --*

      Any version identifier for the version of the source code to be built. If ``sourceVersion``
      is specified at the project level, then this ``sourceVersion`` (at the build level) takes
      precedence.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **resolvedSourceVersion** *(string) --*

      An identifier for the version of this build's source code.

      * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

      * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

      * For Amazon Simple Storage Service (Amazon S3), this does not apply.

    - **projectName** *(string) --*

      The name of the AWS CodeBuild project.

    - **phases** *(list) --*

      Information about all previous build phases that are complete and information about any
      current build phase that is not yet complete.

      - *(dict) --*

        Information about a stage for a build.

        - **phaseType** *(string) --*

          The name of the build phase. Valid values include:

          * ``BUILD`` : Core build activities typically occur in this build phase.

          * ``COMPLETED`` : The build has been completed.

          * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

          * ``FINALIZING`` : The build process is completing in this build phase.

          * ``INSTALL`` : Installation activities typically occur in this build phase.

          * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

          * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

          * ``PROVISIONING`` : The build environment is being set up.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

          * ``SUBMITTED`` : The build has been submitted.

          * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
          location.

        - **phaseStatus** *(string) --*

          The current status of the build phase. Valid values include:

          * ``FAILED`` : The build phase failed.

          * ``FAULT`` : The build phase faulted.

          * ``IN_PROGRESS`` : The build phase is still in progress.

          * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

          * ``STOPPED`` : The build phase stopped.

          * ``SUCCEEDED`` : The build phase succeeded.

          * ``TIMED_OUT`` : The build phase timed out.

        - **startTime** *(datetime) --*

          When the build phase started, expressed in Unix time format.

        - **endTime** *(datetime) --*

          When the build phase ended, expressed in Unix time format.

        - **durationInSeconds** *(integer) --*

          How long, in seconds, between the starting and ending times of the build's phase.

        - **contexts** *(list) --*

          Additional information about a build phase, especially to help troubleshoot a failed
          build.

          - *(dict) --*

            Additional information about a build phase that has an error. You can use this
            information for troubleshooting.

            - **statusCode** *(string) --*

              The status code for the context of the build phase.

            - **message** *(string) --*

              An explanation of the build phase's context. This might include a command ID and an
              exit code.

    - **source** *(dict) --*

      Information about the source code to be built.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
        ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
        action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
        that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your GitHub
        account. Use the AWS CodeBuild console to start creating a build project. When you use
        the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to each
        repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
        application** . (After you have connected to your GitHub account, you do not need to
        finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
        AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
        ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
        access to your account** page, choose **Grant access** . (After you have connected to
        your Bitbucket account, you do not need to finish creating the build project. You can
        leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
        the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source code
        to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source code
        to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get or
        set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the
          OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
          When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
          **Confirm access to your account** page, choose **Grant access** . (After you have
          connected to your Bitbucket account, you do not need to finish creating the build
          project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
          this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
          ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get
          or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it
      must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit
      ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
          name is specified, the branch's HEAD commit ID is used. If not specified, the default
          branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
          is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the output artifacts for the build.

      - **location** *(string) --*

        Information about the location of the build artifacts.

      - **sha256sum** *(string) --*

        The SHA-256 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **md5sum** *(string) --*

        The MD5 hash of the build artifact.

        You can use this hash along with a checksum tool to confirm file integrity and
        authenticity.

        .. note::

          This value is available only if the build project's ``packaging`` value is set to
          ``ZIP`` .

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact name.
        The name specified in a build spec file is calculated at build time and uses the Shell
        Command Language. For example, you can append a date and time to your artifact name so
        that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Information that tells you if encryption for build artifacts is disabled.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about build output artifacts.

        - **location** *(string) --*

          Information about the location of the build artifacts.

        - **sha256sum** *(string) --*

          The SHA-256 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **md5sum** *(string) --*

          The MD5 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses the
          Shell Command Language. For example, you can append a date and time to your artifact
          name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Information that tells you if encryption for build artifacts is disabled.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits. This
        mode is a good choice for projects with a clean working directory and a source that is a
        large Git repository. If you choose this option and your project does not use a Git
        repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
        mode is a good choice if your build scenario is not suited to one of the other three
        local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project sources.
          Cached items are overriden if a source item has the same name. Directories are
          specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an image
        with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive values,
              especially AWS secret key IDs and secret access keys. Environment variables can be
              displayed in plain text using the AWS CodeBuild console and the AWS Command Line
              Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
            Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding one
        of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The valid
          value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
        you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The name of a service role used for this build.

    - **logs** *(dict) --*

      Information about the build's logs in Amazon CloudWatch Logs.

      - **groupName** *(string) --*

        The name of the Amazon CloudWatch Logs group for the build logs.

      - **streamName** *(string) --*

        The name of the Amazon CloudWatch Logs stream for the build logs.

      - **deepLink** *(string) --*

        The URL to an individual build log in Amazon CloudWatch Logs.

      - **s3DeepLink** *(string) --*

        The URL to a build log in an S3 bucket.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about S3 logs for a build project.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
          is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
          ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3 build
          logs are encrypted.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not
      get marked as completed.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **buildComplete** *(boolean) --*

      Whether the build is complete. True if complete; otherwise, false.

    - **initiator** *(string) --*

      The entity that started the build. Valid values include:

      * If AWS CodePipeline started the build, the pipeline's name (for example,
      ``codepipeline/my-demo-pipeline`` ).

      * If an AWS Identity and Access Management (IAM) user started the build, the user's name
      (for example, ``MyUserName`` ).

      * If the Jenkins plugin for AWS CodeBuild started the build, the string
      ``CodeBuild-Jenkins-Plugin`` .

    - **vpcConfig** *(dict) --*

      If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
      parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
      security groups and subnets must belong to the same VPC. You must provide at least one
      security group and one subnet ID.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **networkInterface** *(dict) --*

      Describes a network interface.

      - **subnetId** *(string) --*

        The ID of the subnet.

      - **networkInterfaceId** *(string) --*

        The ID of the network interface.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your service
        role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **exportedEnvironmentVariables** *(list) --*

      A list of exported environment variables for this build.

      - *(dict) --*

        Information about an exported environment variable.

        - **name** *(string) --*

          The name of this exported environment variable.

        - **value** *(string) --*

          The value assigned to this exported environment variable.

          .. note::

            During a build, the value of a variable is available starting with the ``install``
            phase. It can be updated between the start of the ``install`` phase and the end of
            the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
            variables cannot change.
    """


_ClientStopBuildResponseTypeDef = TypedDict(
    "_ClientStopBuildResponseTypeDef",
    {"build": ClientStopBuildResponsebuildTypeDef},
    total=False,
)


class ClientStopBuildResponseTypeDef(_ClientStopBuildResponseTypeDef):
    """
    Type definition for `ClientStopBuild` `Response`

    - **build** *(dict) --*

      Information about the build.

      - **id** *(string) --*

        The unique ID for the build.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the build.

      - **buildNumber** *(integer) --*

        The number of the build. For each project, the ``buildNumber`` of its first build is ``1``
        . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a build is
        deleted, the ``buildNumber`` of other builds does not change.

      - **startTime** *(datetime) --*

        When the build process started, expressed in Unix time format.

      - **endTime** *(datetime) --*

        When the build process ended, expressed in Unix time format.

      - **currentPhase** *(string) --*

        The current build phase.

      - **buildStatus** *(string) --*

        The current status of the build. Valid values include:

        * ``FAILED`` : The build failed.

        * ``FAULT`` : The build faulted.

        * ``IN_PROGRESS`` : The build is still in progress.

        * ``STOPPED`` : The build stopped.

        * ``SUCCEEDED`` : The build succeeded.

        * ``TIMED_OUT`` : The build timed out.

      - **sourceVersion** *(string) --*

        Any version identifier for the version of the source code to be built. If ``sourceVersion``
        is specified at the project level, then this ``sourceVersion`` (at the build level) takes
        precedence.

        For more information, see `Source Version Sample with CodeBuild
        <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
        the *AWS CodeBuild User Guide* .

      - **resolvedSourceVersion** *(string) --*

        An identifier for the version of this build's source code.

        * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

        * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

        * For Amazon Simple Storage Service (Amazon S3), this does not apply.

      - **projectName** *(string) --*

        The name of the AWS CodeBuild project.

      - **phases** *(list) --*

        Information about all previous build phases that are complete and information about any
        current build phase that is not yet complete.

        - *(dict) --*

          Information about a stage for a build.

          - **phaseType** *(string) --*

            The name of the build phase. Valid values include:

            * ``BUILD`` : Core build activities typically occur in this build phase.

            * ``COMPLETED`` : The build has been completed.

            * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

            * ``FINALIZING`` : The build process is completing in this build phase.

            * ``INSTALL`` : Installation activities typically occur in this build phase.

            * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

            * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

            * ``PROVISIONING`` : The build environment is being set up.

            * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

            * ``SUBMITTED`` : The build has been submitted.

            * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
            location.

          - **phaseStatus** *(string) --*

            The current status of the build phase. Valid values include:

            * ``FAILED`` : The build phase failed.

            * ``FAULT`` : The build phase faulted.

            * ``IN_PROGRESS`` : The build phase is still in progress.

            * ``QUEUED`` : The build has been submitted and is queued behind other submitted builds.

            * ``STOPPED`` : The build phase stopped.

            * ``SUCCEEDED`` : The build phase succeeded.

            * ``TIMED_OUT`` : The build phase timed out.

          - **startTime** *(datetime) --*

            When the build phase started, expressed in Unix time format.

          - **endTime** *(datetime) --*

            When the build phase ended, expressed in Unix time format.

          - **durationInSeconds** *(integer) --*

            How long, in seconds, between the starting and ending times of the build's phase.

          - **contexts** *(list) --*

            Additional information about a build phase, especially to help troubleshoot a failed
            build.

            - *(dict) --*

              Additional information about a build phase that has an error. You can use this
              information for troubleshooting.

              - **statusCode** *(string) --*

                The status code for the context of the build phase.

              - **message** *(string) --*

                An explanation of the build phase's context. This might include a command ID and an
                exit code.

      - **source** *(dict) --*

        Information about the source code to be built.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
          ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
          action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
          that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your GitHub
          account. Use the AWS CodeBuild console to start creating a build project. When you use
          the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to each
          repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
          application** . (After you have connected to your GitHub account, you do not need to
          finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
          AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
          ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
          access to your account** page, choose **Grant access** . (After you have connected to
          your Bitbucket account, you do not need to finish creating the build project. You can
          leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
          the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source code
          to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source code
          to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get or
          set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents the
            OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

      - **secondarySources** *(list) --*

        An array of ``ProjectSource`` objects.

        - *(dict) --*

          Information about the build input source code for the build project.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

      - **secondarySourceVersions** *(list) --*

        An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be one of:

        * For AWS CodeCommit: the commit ID to use.

        * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
        the version of the source code you want to build. If a pull request ID is specified, it
        must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
        specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
        commit ID is used.

        * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
        the source code you want to build. If a branch name is specified, the branch's HEAD commit
        ID is used. If not specified, the default branch's HEAD commit ID is used.

        * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
        represents the build input ZIP file to use.

        - *(dict) --*

          A source identifier and its corresponding version.

          - **sourceIdentifier** *(string) --*

            An identifier for a source in the build project.

          - **sourceVersion** *(string) --*

            The source version for the corresponding source identifier. If specified, must be one
            of:

            * For AWS CodeCommit: the commit ID to use.

            * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
            to the version of the source code you want to build. If a pull request ID is specified,
            it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
            name is specified, the branch's HEAD commit ID is used. If not specified, the default
            branch's HEAD commit ID is used.

            * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
            version of the source code you want to build. If a branch name is specified, the
            branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
            is used.

            * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
            represents the build input ZIP file to use.

            For more information, see `Source Version Sample with CodeBuild
            <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
            in the *AWS CodeBuild User Guide* .

      - **artifacts** *(dict) --*

        Information about the output artifacts for the build.

        - **location** *(string) --*

          Information about the location of the build artifacts.

        - **sha256sum** *(string) --*

          The SHA-256 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **md5sum** *(string) --*

          The MD5 hash of the build artifact.

          You can use this hash along with a checksum tool to confirm file integrity and
          authenticity.

          .. note::

            This value is available only if the build project's ``packaging`` value is set to
            ``ZIP`` .

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact name.
          The name specified in a build spec file is calculated at build time and uses the Shell
          Command Language. For example, you can append a date and time to your artifact name so
          that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Information that tells you if encryption for build artifacts is disabled.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

      - **secondaryArtifacts** *(list) --*

        An array of ``ProjectArtifacts`` objects.

        - *(dict) --*

          Information about build output artifacts.

          - **location** *(string) --*

            Information about the location of the build artifacts.

          - **sha256sum** *(string) --*

            The SHA-256 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **md5sum** *(string) --*

            The MD5 hash of the build artifact.

            You can use this hash along with a checksum tool to confirm file integrity and
            authenticity.

            .. note::

              This value is available only if the build project's ``packaging`` value is set to
              ``ZIP`` .

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Information that tells you if encryption for build artifacts is disabled.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

      - **cache** *(dict) --*

        Information about the cache for the build.

        - **type** *(string) --*

          The type of cache used by the build project. Valid values include:

          * ``NO_CACHE`` : The build project does not use any cache.

          * ``S3`` : The build project reads and writes from and to S3.

          * ``LOCAL`` : The build project stores a cache locally on a build host that is only
          available to that build host.

        - **location** *(string) --*

          Information about the cache location:

          * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

          * ``S3`` : This is the S3 bucket name/prefix.

        - **modes** *(list) --*

          If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
          modes at the same time.

          * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
          After the cache is created, subsequent builds pull only the change between commits. This
          mode is a good choice for projects with a clean working directory and a source that is a
          large Git repository. If you choose this option and your project does not use a Git
          repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

          * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
          choice for projects that build or pull large Docker images. It can prevent the
          performance issues caused by pulling large Docker images down from the network.

          .. note::

              * You can use a Docker layer cache in the Linux environment only.

              * The ``privileged`` flag must be set so that your project has the required Docker
              permissions.

              * You should consider the security implications before you use a Docker layer cache.

          * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
          mode is a good choice if your build scenario is not suited to one of the other three
          local cache modes. If you use a custom cache:

            * Only directories can be specified for caching. You cannot specify individual files.

            * Symlinks are used to reference cached directories.

            * Cached directories are linked to your build before it downloads its project sources.
            Cached items are overriden if a source item has the same name. Directories are
            specified using cache paths in the buildspec file.

          - *(string) --*

      - **environment** *(dict) --*

        Information about the build environment for this build.

        - **type** *(string) --*

          The type of build environment to use for related builds.

        - **image** *(string) --*

          The image tag or image digest that identifies the Docker image to use for this build
          project. Use the following formats:

          * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
          the tag "latest," use ``registry/repository:latest`` .

          * For an image digest: ``registry/repository@digest`` . For example, to specify an image
          with the digest
          "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
          ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
          .

        - **computeType** *(string) --*

          Information about the compute resources the build project uses. Available values include:

          * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

          * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

          * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

          For more information, see `Build Environment Compute Types
          <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
          in the *AWS CodeBuild User Guide.*

        - **environmentVariables** *(list) --*

          A set of environment variables to make available to builds for this build project.

          - *(dict) --*

            Information about an environment variable for a build project or a build.

            - **name** *(string) --*

              The name or key of the environment variable.

            - **value** *(string) --*

              The value of the environment variable.

              .. warning::

                We strongly discourage the use of environment variables to store sensitive values,
                especially AWS secret key IDs and secret access keys. Environment variables can be
                displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                Interface (AWS CLI).

            - **type** *(string) --*

              The type of environment variable. Valid values include:

              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
              Parameter Store.

              * ``PLAINTEXT`` : An environment variable in plaintext format.

              * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

        - **privilegedMode** *(boolean) --*

          Enables running the Docker daemon inside a Docker container. Set to true only if the
          build project is used to build Docker images. Otherwise, a build that attempts to
          interact with the Docker daemon fails. The default setting is ``false`` .

          You can initialize the Docker daemon during the install phase of your build by adding one
          of the following sets of commands to the install phase of your buildspec file:

          If the operating system's base image is Ubuntu Linux:

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

          If the operating system's base image is Alpine Linux and the previous command does not
          work, add the ``-t`` argument to ``timeout`` :

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

        - **certificate** *(string) --*

          The certificate to use with this build project.

        - **registryCredential** *(dict) --*

          The credentials for access to a private registry.

          - **credential** *(string) --*

            The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

            .. note::

              The ``credential`` can use the name of the credentials only if they exist in your
              current region.

          - **credentialProvider** *(string) --*

            The service that created the credentials to access a private Docker registry. The valid
            value, SECRETS_MANAGER, is for AWS Secrets Manager.

        - **imagePullCredentialsType** *(string) --*

          The type of credentials AWS CodeBuild uses to pull images in your build. There are two
          valid values:

          * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
          you modify your ECR repository policy to trust AWS CodeBuild's service principal.

          * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

          When you use a cross-account or private registry image, you must use SERVICE_ROLE
          credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
          credentials.

      - **serviceRole** *(string) --*

        The name of a service role used for this build.

      - **logs** *(dict) --*

        Information about the build's logs in Amazon CloudWatch Logs.

        - **groupName** *(string) --*

          The name of the Amazon CloudWatch Logs group for the build logs.

        - **streamName** *(string) --*

          The name of the Amazon CloudWatch Logs stream for the build logs.

        - **deepLink** *(string) --*

          The URL to an individual build log in Amazon CloudWatch Logs.

        - **s3DeepLink** *(string) --*

          The URL to a build log in an S3 bucket.

        - **cloudWatchLogs** *(dict) --*

          Information about Amazon CloudWatch Logs for a build project.

          - **status** *(string) --*

            The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
            values are:

            * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

            * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

          - **groupName** *(string) --*

            The group name of the logs in Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

          - **streamName** *(string) --*

            The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

        - **s3Logs** *(dict) --*

          Information about S3 logs for a build project.

          - **status** *(string) --*

            The current status of the S3 build logs. Valid values are:

            * ``ENABLED`` : S3 build logs are enabled for this build project.

            * ``DISABLED`` : S3 build logs are not enabled for this build project.

          - **location** *(string) --*

            The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
            is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
            ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your S3 build log output encrypted. By default S3 build
            logs are encrypted.

      - **timeoutInMinutes** *(integer) --*

        How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not
        get marked as completed.

      - **queuedTimeoutInMinutes** *(integer) --*

        The number of minutes a build is allowed to be queued before it times out.

      - **buildComplete** *(boolean) --*

        Whether the build is complete. True if complete; otherwise, false.

      - **initiator** *(string) --*

        The entity that started the build. Valid values include:

        * If AWS CodePipeline started the build, the pipeline's name (for example,
        ``codepipeline/my-demo-pipeline`` ).

        * If an AWS Identity and Access Management (IAM) user started the build, the user's name
        (for example, ``MyUserName`` ).

        * If the Jenkins plugin for AWS CodeBuild started the build, the string
        ``CodeBuild-Jenkins-Plugin`` .

      - **vpcConfig** *(dict) --*

        If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
        parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The
        security groups and subnets must belong to the same VPC. You must provide at least one
        security group and one subnet ID.

        - **vpcId** *(string) --*

          The ID of the Amazon VPC.

        - **subnets** *(list) --*

          A list of one or more subnet IDs in your Amazon VPC.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          A list of one or more security groups IDs in your Amazon VPC.

          - *(string) --*

      - **networkInterface** *(dict) --*

        Describes a network interface.

        - **subnetId** *(string) --*

          The ID of the subnet.

        - **networkInterfaceId** *(string) --*

          The ID of the network interface.

      - **encryptionKey** *(string) --*

        The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
        encrypting the build output artifacts.

        .. note::

          You can use a cross-account KMS key to encrypt the build output artifacts if your service
          role has permission to that key.

        You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
        CMK's alias (using the format ``alias/*alias-name* `` ).

      - **exportedEnvironmentVariables** *(list) --*

        A list of exported environment variables for this build.

        - *(dict) --*

          Information about an exported environment variable.

          - **name** *(string) --*

            The name of this exported environment variable.

          - **value** *(string) --*

            The value assigned to this exported environment variable.

            .. note::

              During a build, the value of a variable is available starting with the ``install``
              phase. It can be updated between the start of the ``install`` phase and the end of
              the ``post_build`` phase. After the ``post_build`` phase ends, the value of exported
              variables cannot change.
    """


_ClientUpdateProjectResponseprojectartifactsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectartifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectartifactsTypeDef(
    _ClientUpdateProjectResponseprojectartifactsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `artifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
      S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
      not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
      , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
      bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
      name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
        not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
      in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of AWS
      CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
      set the name to be a forward slash ("/"), the artifact is stored in the root of the
      output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
      .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name.
      The name specified in a build spec file is calculated at build time and uses the Shell
      Command Language. For example, you can append a date and time to your artifact name so
      that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only
      if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
      another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientUpdateProjectResponseprojectbadgeTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientUpdateProjectResponseprojectbadgeTypeDef(
    _ClientUpdateProjectResponseprojectbadgeTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `badge`

    Information about the build badge for the build project.

    - **badgeEnabled** *(boolean) --*

      Set this to true to generate a publicly accessible URL for your project's build badge.

    - **badgeRequestUrl** *(string) --*

      The publicly-accessible URL through which you can access the build badge for your project.

      The publicly accessible URL through which you can access the build badge for your project.
    """


_ClientUpdateProjectResponseprojectcacheTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectcacheTypeDef",
    {"type": str, "location": str, "modes": List[str]},
    total=False,
)


class ClientUpdateProjectResponseprojectcacheTypeDef(
    _ClientUpdateProjectResponseprojectcacheTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `cache`

    Information about the cache for the build project.

    - **type** *(string) --*

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only
      available to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
      modes at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
      After the cache is created, subsequent builds pull only the change between commits. This
      mode is a good choice for projects with a clean working directory and a source that is a
      large Git repository. If you choose this option and your project does not use a Git
      repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
      choice for projects that build or pull large Docker images. It can prevent the
      performance issues caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
      mode is a good choice if your build scenario is not suited to one of the other three
      local cache modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources.
        Cached items are overriden if a source item has the same name. Directories are
        specified using cache paths in the buildspec file.

      - *(string) --*
    """


_ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": str},
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --*

      The name or key of the environment variable.

    - **value** *(string) --*

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --*

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your
        current region.

    - **credentialProvider** *(string) --*

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_ClientUpdateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentTypeDef",
    {
        "type": str,
        "image": str,
        "computeType": str,
        "environmentVariables": List[
            ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `environment`

    Information about the build environment for this build project.

    - **type** *(string) --*

      The type of build environment to use for related builds.

    - **image** *(string) --*

      The image tag or image digest that identifies the Docker image to use for this build
      project. Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
      the tag "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image
      with the digest
      "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --*

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
      in the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --*

          The name or key of the environment variable.

        - **value** *(string) --*

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the
      build project is used to build Docker images. Otherwise, a build that attempts to
      interact with the Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one
      of the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not
      work, add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
       --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --*

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your
          current region.

      - **credentialProvider** *(string) --*

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two
      valid values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
      you modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE
      credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
      credentials.
    """


_ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": str, "groupName": str, "streamName": str},
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectlogsConfig` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
    enabled by default.

    - **status** *(string) --*

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
      values are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": str, "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectlogsConfig` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
    by default.

    - **status** *(string) --*

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
      is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build
      logs are encrypted.
    """


_ClientUpdateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `logsConfig`

    Information about logs for the build project. A project can create logs in Amazon
    CloudWatch Logs, an S3 bucket, or both.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.

      - **status** *(string) --*

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
        values are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
      by default.

      - **status** *(string) --*

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
        is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build
        logs are encrypted.
    """


_ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": str,
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef(
    _ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `secondaryArtifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --*

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS
      CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service
      (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output locations instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
      is not specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      the output bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
      name and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
        not specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
      stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
      and store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output names instead of
      AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
      set the name to be a forward slash ("/"), the artifact is stored in the root of the
      output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
      "``/`` ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to "``/`` ", the output artifact is stored in
      ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
      specified. This is because AWS CodePipeline manages its build output artifacts instead
      of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
      no build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
        build output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
        build output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact
      name. The name specified in a build spec file is calculated at build time and uses the
      Shell Command Language. For example, you can append a date and time to your artifact
      name so that it is always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid
      only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
      set with another artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --*

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --*

      The source version for the corresponding source identifier. If specified, must be one
      of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
      to the version of the source code you want to build. If a pull request ID is specified,
      it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
      name is specified, the branch's HEAD commit ID is used. If not specified, the default
      branch's HEAD commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
      version of the source code you want to build. If a branch name is specified, the
      branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
      is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
      in the *AWS CodeBuild User Guide* .
    """


_ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source
    code to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get
    or set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents
      the OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientUpdateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS
      CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
      pipeline's source action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
      repository that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, ``
        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      GitHub account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to
      each repository you want to allow AWS CodeBuild to have access to, and then choose
      **Authorize application** . (After you have connected to your GitHub account, you do
      not need to finish creating the build project. You can leave the AWS CodeBuild
      console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
      set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
      When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
      **Confirm access to your account** page, choose **Grant access** . (After you have
      connected to your Bitbucket account, you do not need to finish creating the build
      project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
      this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
      ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source
      code to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source
      code to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get
      or set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents
        the OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source
        provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientUpdateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsourceauthTypeDef(
    _ClientUpdateProjectResponseprojectsourceauthTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code
    to be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or
    set this information directly.

    - **type** *(string) --*

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef(
    _ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --*

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_ClientUpdateProjectResponseprojectsourceTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourceTypeDef",
    {
        "type": str,
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsourceTypeDef(
    _ClientUpdateProjectResponseprojectsourceTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `source`

    Information about the build input source code for this build project.

    - **type** *(string) --*

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
      bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
      action instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
      that contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
      the following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your GitHub
      account. Use the AWS CodeBuild console to start creating a build project. When you use
      the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
      application** page, for **Organization access** , choose **Request access** next to each
      repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
      application** . (After you have connected to your GitHub account, you do not need to
      finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
      AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
      ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your
      Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
      you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
      access to your account** page, choose **Grant access** . (After you have connected to
      your Bitbucket account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --*

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code
      to be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code
      to be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or
      set this information directly.

      - **type** *(string) --*

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider.
      This option is valid only when your source provider is GitHub, GitHub Enterprise, or
      Bitbucket. If this is set and you use a different source provider, an
      invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientUpdateProjectResponseprojecttagsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojecttagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateProjectResponseprojecttagsTypeDef(
    _ClientUpdateProjectResponseprojecttagsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `tags`

    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS CodeBuild.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientUpdateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientUpdateProjectResponseprojectvpcConfigTypeDef(
    _ClientUpdateProjectResponseprojectvpcConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `vpcConfig`

    Information about the VPC configuration that AWS CodeBuild accesses.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {"type": str, "pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef(
    _ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseprojectwebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --*

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four
      event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
      comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
      PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
      updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
      account ID matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
      ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
      request, Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular
      expression ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --*

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
      specifies one or more events. For example, the webhook filter ``PUSH,
      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
      and pull request updated events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular
      expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
      ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
      is a branch with a reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not
      trigger a build. If true, then a webhook event that does not match the ``pattern``
      triggers a build. If false, then a webhook event that matches the ``pattern``
      triggers a build.
    """


_ClientUpdateProjectResponseprojectwebhookTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectwebhookTypeDef(
    _ClientUpdateProjectResponseprojectwebhookTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponseproject` `webhook`

    Information about a webhook that connects repository events to a build project in AWS
    CodeBuild.

    - **url** *(string) --*

      The URL to the webhook.

    - **payloadUrl** *(string) --*

      The AWS CodeBuild endpoint where webhook events are sent.

    - **secret** *(string) --*

      The secret token of the associated repository.

      .. note::

        A Bitbucket webhook does not support ``secret`` .

    - **branchFilter** *(string) --*

      A regular expression used to determine which repository branches are built when a webhook
      is triggered. If the name of a branch matches the regular expression, then it is built.
      If ``branchFilter`` is empty, then all branches are built.

      .. note::

        It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

    - **filterGroups** *(list) --*

      An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
      triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
      ``type`` .

      For a build to be triggered, at least one filter group in the ``filterGroups`` array must
      pass. For a filter group to pass, each of its filters must pass.

      - *(list) --*

        - *(dict) --*

          A filter used to determine which webhooks trigger a build.

          - **type** *(string) --*

            The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
            ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

              EVENT

            A webhook event triggers a build when the provided ``pattern`` matches one of four
            event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
            ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
            comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
            PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
            updated events.

            .. note::

              The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

              ACTOR_ACCOUNT_ID

            A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
            account ID matches the regular expression ``pattern`` .

              HEAD_REF

            A webhook event triggers a build when the head reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` and
            ``refs/tags/tag-name`` .

            Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
            request, Bitbucket push, and Bitbucket pull request events.

              BASE_REF

            A webhook event triggers a build when the base reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` .

            .. note::

              Works with pull request events only.

              FILE_PATH

            A webhook triggers a build when the path of a changed file matches the regular
            expression ``pattern`` .

            .. note::

              Works with GitHub and GitHub Enterprise push events only.

          - **pattern** *(string) --*

            For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
            specifies one or more events. For example, the webhook filter ``PUSH,
            PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
            and pull request updated events to trigger a build.

            For a ``WebHookFilter`` that uses any of the other filter types, a regular
            expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
            ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
            is a branch with a reference name ``refs/heads/branch-name`` .

          - **excludeMatchedPattern** *(boolean) --*

            Used to indicate that the ``pattern`` determines which webhook events do not
            trigger a build. If true, then a webhook event that does not match the ``pattern``
            triggers a build. If false, then a webhook event that matches the ``pattern``
            triggers a build.

    - **lastModifiedSecret** *(datetime) --*

      A timestamp that indicates the last time a repository's secret token was modified.
    """


_ClientUpdateProjectResponseprojectTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientUpdateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[
            ClientUpdateProjectResponseprojectsecondarySourcesTypeDef
        ],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientUpdateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[
            ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef
        ],
        "cache": ClientUpdateProjectResponseprojectcacheTypeDef,
        "environment": ClientUpdateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientUpdateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientUpdateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientUpdateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientUpdateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientUpdateProjectResponseprojectlogsConfigTypeDef,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectTypeDef(
    _ClientUpdateProjectResponseprojectTypeDef
):
    """
    Type definition for `ClientUpdateProjectResponse` `project`

    Information about the build project that was changed.

    - **name** *(string) --*

      The name of the build project.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the build project.

    - **description** *(string) --*

      A description that makes the build project easy to identify.

    - **source** *(dict) --*

      Information about the build input source code for this build project.

      - **type** *(string) --*

        The type of repository that contains the source code to be built. Valid values include:

        * ``BITBUCKET`` : The source code is in a Bitbucket repository.

        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.

        * ``GITHUB`` : The source code is in a GitHub repository.

        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

        * ``NO_SOURCE`` : The project does not have input source code.

        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
        bucket.

      - **location** *(string) --*

        Information about the location of the source code to be built. Valid values include:

        * For source code settings that are specified in the source action of a pipeline in AWS
        CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
        ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
        action instead of this value.

        * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
        that contains the source code and the build spec (for example,
        ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

        * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
        the following.

          * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*object-name* .zip`` ).

          * The path to the folder that contains the source code (for example, `` *bucket-name*
          /*path* /*to* /*source-code* /*folder* /`` ).

        * For source code in a GitHub repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your GitHub
        account. Use the AWS CodeBuild console to start creating a build project. When you use
        the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
        application** page, for **Organization access** , choose **Request access** next to each
        repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
        application** . (After you have connected to your GitHub account, you do not need to
        finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
        AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
        ``type`` value to ``OAUTH`` .

        * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
        contains the source and the build spec. You must connect your AWS account to your
        Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
        you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
        access to your account** page, choose **Grant access** . (After you have connected to
        your Bitbucket account, you do not need to finish creating the build project. You can
        leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
        the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      - **gitCloneDepth** *(integer) --*

        Information about the Git clone depth for the build project.

      - **gitSubmodulesConfig** *(dict) --*

        Information about the Git submodules configuration for the build project.

        - **fetchSubmodules** *(boolean) --*

          Set to true to fetch Git submodules for your AWS CodeBuild build project.

      - **buildspec** *(string) --*

        The build spec declaration to use for the builds in this build project.

        If this value is not specified, a build spec must be included along with the source code
        to be built.

      - **auth** *(dict) --*

        Information about the authorization settings for AWS CodeBuild to access the source code
        to be built.

        This information is for the AWS CodeBuild console's use only. Your code should not get or
        set this information directly.

        - **type** *(string) --*

          .. note::

            This data type is deprecated and is no longer accurate or used.

          The authorization type to use. The only valid value is ``OAUTH`` , which represents the
          OAuth authorization type.

        - **resource** *(string) --*

          The resource value that applies to the specified authorization type.

      - **reportBuildStatus** *(boolean) --*

        Set to true to report the status of a build's start and finish to your source provider.
        This option is valid only when your source provider is GitHub, GitHub Enterprise, or
        Bitbucket. If this is set and you use a different source provider, an
        invalidInputException is thrown.

        .. note::

          The status of a build triggered by a webhook is always reported to your source provider.

      - **insecureSsl** *(boolean) --*

        Enable this flag to ignore SSL warnings while connecting to the project source code.

      - **sourceIdentifier** *(string) --*

        An identifier for this project source.

    - **secondarySources** *(list) --*

      An array of ``ProjectSource`` objects.

      - *(dict) --*

        Information about the build input source code for the build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS
          CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
          pipeline's source action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
          repository that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, ``
            *bucket-name* /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          GitHub account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to
          each repository you want to allow AWS CodeBuild to have access to, and then choose
          **Authorize application** . (After you have connected to your GitHub account, you do
          not need to finish creating the build project. You can leave the AWS CodeBuild
          console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
          set the ``auth`` object's ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
          When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
          **Confirm access to your account** page, choose **Grant access** . (After you have
          connected to your Bitbucket account, you do not need to finish creating the build
          project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
          this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
          ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source
          code to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source
          code to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get
          or set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents
            the OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source
            provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

    - **sourceVersion** *(string) --*

      A version of the build input to be built for this project. If not specified, the latest
      version is used. If specified, it must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it
      must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit
      ID is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
      represents the build input ZIP file to use.

      If ``sourceVersion`` is specified at the build level, then that version takes precedence
      over this ``sourceVersion`` (at the project level).

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
      the *AWS CodeBuild User Guide* .

    - **secondarySourceVersions** *(list) --*

      An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
      at the build level, then they take over these ``secondarySourceVersions`` (at the project
      level).

      - *(dict) --*

        A source identifier and its corresponding version.

        - **sourceIdentifier** *(string) --*

          An identifier for a source in the build project.

        - **sourceVersion** *(string) --*

          The source version for the corresponding source identifier. If specified, must be one
          of:

          * For AWS CodeCommit: the commit ID to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
          to the version of the source code you want to build. If a pull request ID is specified,
          it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
          name is specified, the branch's HEAD commit ID is used. If not specified, the default
          branch's HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
          version of the source code you want to build. If a branch name is specified, the
          branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
          is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
          in the *AWS CodeBuild User Guide* .

    - **artifacts** *(dict) --*

      Information about the build output artifacts for the build project.

      - **type** *(string) --*

        The type of build output artifact. Valid values include:

        * ``CODEPIPELINE`` : The build project has build output generated through AWS
        CodePipeline.

        .. note::

           The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

        * ``NO_ARTIFACTS`` : The build project does not produce any build output.

        * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
        S3).

      - **location** *(string) --*

        Information about the build output artifact location:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output locations instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output bucket.

      - **path** *(string) --*

        Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
        not specified, ``path`` is not used.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
        , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
        bucket at ``MyArtifacts/MyArtifact.zip`` .

      - **namespaceType** *(string) --*

        Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
        name and location to store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

          * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
          not specified.

        For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
        ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
        in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      - **name** *(string) --*

        Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
        and store the output artifact:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output names instead of AWS
        CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
        set the name to be a forward slash ("/"), the artifact is stored in the root of the
        output bucket.

        For example:

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
        ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
        ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
        "``/`` ", the output artifact is stored in the root of the output bucket.

        * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
        ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
        .

      - **packaging** *(string) --*

        The type of build output artifact to create:

        * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
        specified. This is because AWS CodePipeline manages its build output artifacts instead of
        AWS CodeBuild.

        * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
        build output is produced.

        * If ``type`` is set to ``S3`` , valid values include:

          * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
          build output. This is the default if ``packaging`` is not specified.

          * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
          build output.

      - **overrideArtifactName** *(boolean) --*

        If this flag is set, a name specified in the build spec file overrides the artifact name.
        The name specified in a build spec file is calculated at build time and uses the Shell
        Command Language. For example, you can append a date and time to your artifact name so
        that it is always unique.

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your output artifacts encrypted. This option is valid only
        if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
        another artifacts type, an invalidInputException is thrown.

      - **artifactIdentifier** *(string) --*

        An identifier for this artifact definition.

    - **secondaryArtifacts** *(list) --*

      An array of ``ProjectArtifacts`` objects.

      - *(dict) --*

        Information about the build output artifacts for the build project.

        - **type** *(string) --*

          The type of build output artifact. Valid values include:

          * ``CODEPIPELINE`` : The build project has build output generated through AWS
          CodePipeline.

          .. note::

             The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

          * ``NO_ARTIFACTS`` : The build project does not produce any build output.

          * ``S3`` : The build project stores build output in Amazon Simple Storage Service
          (Amazon S3).

        - **location** *(string) --*

          Information about the build output artifact location:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output locations instead
          of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output bucket.

        - **path** *(string) --*

          Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
          is not specified, ``path`` is not used.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
          the output bucket at ``MyArtifacts/MyArtifact.zip`` .

        - **namespaceType** *(string) --*

          Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
          name and location to store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

            * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
            not specified.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
          stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        - **name** *(string) --*

          Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
          set the name to be a forward slash ("/"), the artifact is stored in the root of the
          output bucket.

          For example:

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
          ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
          "``/`` ", the output artifact is stored in the root of the output bucket.

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
          and ``name`` is set to "``/`` ", the output artifact is stored in
          ``MyArtifacts/*build-ID* `` .

        - **packaging** *(string) --*

          The type of build output artifact to create:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output artifacts instead
          of AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
          no build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
            build output. This is the default if ``packaging`` is not specified.

            * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
            build output.

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact
          name. The name specified in a build spec file is calculated at build time and uses the
          Shell Command Language. For example, you can append a date and time to your artifact
          name so that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your output artifacts encrypted. This option is valid
          only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
          set with another artifacts type, an invalidInputException is thrown.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

    - **cache** *(dict) --*

      Information about the cache for the build project.

      - **type** *(string) --*

        The type of cache used by the build project. Valid values include:

        * ``NO_CACHE`` : The build project does not use any cache.

        * ``S3`` : The build project reads and writes from and to S3.

        * ``LOCAL`` : The build project stores a cache locally on a build host that is only
        available to that build host.

      - **location** *(string) --*

        Information about the cache location:

        * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

        * ``S3`` : This is the S3 bucket name/prefix.

      - **modes** *(list) --*

        If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
        modes at the same time.

        * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
        After the cache is created, subsequent builds pull only the change between commits. This
        mode is a good choice for projects with a clean working directory and a source that is a
        large Git repository. If you choose this option and your project does not use a Git
        repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

        * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
        choice for projects that build or pull large Docker images. It can prevent the
        performance issues caused by pulling large Docker images down from the network.

        .. note::

            * You can use a Docker layer cache in the Linux environment only.

            * The ``privileged`` flag must be set so that your project has the required Docker
            permissions.

            * You should consider the security implications before you use a Docker layer cache.

        * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
        mode is a good choice if your build scenario is not suited to one of the other three
        local cache modes. If you use a custom cache:

          * Only directories can be specified for caching. You cannot specify individual files.

          * Symlinks are used to reference cached directories.

          * Cached directories are linked to your build before it downloads its project sources.
          Cached items are overriden if a source item has the same name. Directories are
          specified using cache paths in the buildspec file.

        - *(string) --*

    - **environment** *(dict) --*

      Information about the build environment for this build project.

      - **type** *(string) --*

        The type of build environment to use for related builds.

      - **image** *(string) --*

        The image tag or image digest that identifies the Docker image to use for this build
        project. Use the following formats:

        * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
        the tag "latest," use ``registry/repository:latest`` .

        * For an image digest: ``registry/repository@digest`` . For example, to specify an image
        with the digest
        "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
        ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
        .

      - **computeType** *(string) --*

        Information about the compute resources the build project uses. Available values include:

        * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

        * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

        * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

        For more information, see `Build Environment Compute Types
        <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
        in the *AWS CodeBuild User Guide.*

      - **environmentVariables** *(list) --*

        A set of environment variables to make available to builds for this build project.

        - *(dict) --*

          Information about an environment variable for a build project or a build.

          - **name** *(string) --*

            The name or key of the environment variable.

          - **value** *(string) --*

            The value of the environment variable.

            .. warning::

              We strongly discourage the use of environment variables to store sensitive values,
              especially AWS secret key IDs and secret access keys. Environment variables can be
              displayed in plain text using the AWS CodeBuild console and the AWS Command Line
              Interface (AWS CLI).

          - **type** *(string) --*

            The type of environment variable. Valid values include:

            * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
            Parameter Store.

            * ``PLAINTEXT`` : An environment variable in plaintext format.

            * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

      - **privilegedMode** *(boolean) --*

        Enables running the Docker daemon inside a Docker container. Set to true only if the
        build project is used to build Docker images. Otherwise, a build that attempts to
        interact with the Docker daemon fails. The default setting is ``false`` .

        You can initialize the Docker daemon during the install phase of your build by adding one
        of the following sets of commands to the install phase of your buildspec file:

        If the operating system's base image is Ubuntu Linux:

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

        If the operating system's base image is Alpine Linux and the previous command does not
        work, add the ``-t`` argument to ``timeout`` :

         ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
         --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

         ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

      - **certificate** *(string) --*

        The certificate to use with this build project.

      - **registryCredential** *(dict) --*

        The credentials for access to a private registry.

        - **credential** *(string) --*

          The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

          .. note::

            The ``credential`` can use the name of the credentials only if they exist in your
            current region.

        - **credentialProvider** *(string) --*

          The service that created the credentials to access a private Docker registry. The valid
          value, SECRETS_MANAGER, is for AWS Secrets Manager.

      - **imagePullCredentialsType** *(string) --*

        The type of credentials AWS CodeBuild uses to pull images in your build. There are two
        valid values:

        * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
        you modify your ECR repository policy to trust AWS CodeBuild's service principal.

        * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

        When you use a cross-account or private registry image, you must use SERVICE_ROLE
        credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
        credentials.

    - **serviceRole** *(string) --*

      The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to
      interact with dependent AWS services on behalf of the AWS account.

    - **timeoutInMinutes** *(integer) --*

      How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out
      any related build that did not get marked as completed. The default is 60 minutes.

    - **queuedTimeoutInMinutes** *(integer) --*

      The number of minutes a build is allowed to be queued before it times out.

    - **encryptionKey** *(string) --*

      The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
      encrypting the build output artifacts.

      .. note::

        You can use a cross-account KMS key to encrypt the build output artifacts if your service
        role has permission to that key.

      You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
      CMK's alias (using the format ``alias/*alias-name* `` ).

    - **tags** *(list) --*

      The tags for this build project.

      These tags are available for use by AWS services that support AWS CodeBuild build project
      tags.

      - *(dict) --*

        A tag, consisting of a key and a value.

        This tag is available for use by AWS services that support tags in AWS CodeBuild.

        - **key** *(string) --*

          The tag's key.

        - **value** *(string) --*

          The tag's value.

    - **created** *(datetime) --*

      When the build project was created, expressed in Unix time format.

    - **lastModified** *(datetime) --*

      When the build project's settings were last modified, expressed in Unix time format.

    - **webhook** *(dict) --*

      Information about a webhook that connects repository events to a build project in AWS
      CodeBuild.

      - **url** *(string) --*

        The URL to the webhook.

      - **payloadUrl** *(string) --*

        The AWS CodeBuild endpoint where webhook events are sent.

      - **secret** *(string) --*

        The secret token of the associated repository.

        .. note::

          A Bitbucket webhook does not support ``secret`` .

      - **branchFilter** *(string) --*

        A regular expression used to determine which repository branches are built when a webhook
        is triggered. If the name of a branch matches the regular expression, then it is built.
        If ``branchFilter`` is empty, then all branches are built.

        .. note::

          It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

      - **filterGroups** *(list) --*

        An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
        triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
        ``type`` .

        For a build to be triggered, at least one filter group in the ``filterGroups`` array must
        pass. For a filter group to pass, each of its filters must pass.

        - *(list) --*

          - *(dict) --*

            A filter used to determine which webhooks trigger a build.

            - **type** *(string) --*

              The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
              ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                EVENT

              A webhook event triggers a build when the provided ``pattern`` matches one of four
              event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
              ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
              comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
              PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
              updated events.

              .. note::

                The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                ACTOR_ACCOUNT_ID

              A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
              account ID matches the regular expression ``pattern`` .

                HEAD_REF

              A webhook event triggers a build when the head reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` and
              ``refs/tags/tag-name`` .

              Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
              request, Bitbucket push, and Bitbucket pull request events.

                BASE_REF

              A webhook event triggers a build when the base reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` .

              .. note::

                Works with pull request events only.

                FILE_PATH

              A webhook triggers a build when the path of a changed file matches the regular
              expression ``pattern`` .

              .. note::

                Works with GitHub and GitHub Enterprise push events only.

            - **pattern** *(string) --*

              For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
              specifies one or more events. For example, the webhook filter ``PUSH,
              PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
              and pull request updated events to trigger a build.

              For a ``WebHookFilter`` that uses any of the other filter types, a regular
              expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
              ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
              is a branch with a reference name ``refs/heads/branch-name`` .

            - **excludeMatchedPattern** *(boolean) --*

              Used to indicate that the ``pattern`` determines which webhook events do not
              trigger a build. If true, then a webhook event that does not match the ``pattern``
              triggers a build. If false, then a webhook event that matches the ``pattern``
              triggers a build.

      - **lastModifiedSecret** *(datetime) --*

        A timestamp that indicates the last time a repository's secret token was modified.

    - **vpcConfig** *(dict) --*

      Information about the VPC configuration that AWS CodeBuild accesses.

      - **vpcId** *(string) --*

        The ID of the Amazon VPC.

      - **subnets** *(list) --*

        A list of one or more subnet IDs in your Amazon VPC.

        - *(string) --*

      - **securityGroupIds** *(list) --*

        A list of one or more security groups IDs in your Amazon VPC.

        - *(string) --*

    - **badge** *(dict) --*

      Information about the build badge for the build project.

      - **badgeEnabled** *(boolean) --*

        Set this to true to generate a publicly accessible URL for your project's build badge.

      - **badgeRequestUrl** *(string) --*

        The publicly-accessible URL through which you can access the build badge for your project.

        The publicly accessible URL through which you can access the build badge for your project.

    - **logsConfig** *(dict) --*

      Information about logs for the build project. A project can create logs in Amazon
      CloudWatch Logs, an S3 bucket, or both.

      - **cloudWatchLogs** *(dict) --*

        Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
        enabled by default.

        - **status** *(string) --*

          The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
          values are:

          * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

          * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

        - **groupName** *(string) --*

          The group name of the logs in Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

        - **streamName** *(string) --*

          The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
          `Working with Log Groups and Log Streams
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
          .

      - **s3Logs** *(dict) --*

        Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
        by default.

        - **status** *(string) --*

          The current status of the S3 build logs. Valid values are:

          * ``ENABLED`` : S3 build logs are enabled for this build project.

          * ``DISABLED`` : S3 build logs are not enabled for this build project.

        - **location** *(string) --*

          The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
          is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
          ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your S3 build log output encrypted. By default S3 build
          logs are encrypted.
    """


_ClientUpdateProjectResponseTypeDef = TypedDict(
    "_ClientUpdateProjectResponseTypeDef",
    {"project": ClientUpdateProjectResponseprojectTypeDef},
    total=False,
)


class ClientUpdateProjectResponseTypeDef(_ClientUpdateProjectResponseTypeDef):
    """
    Type definition for `ClientUpdateProject` `Response`

    - **project** *(dict) --*

      Information about the build project that was changed.

      - **name** *(string) --*

        The name of the build project.

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the build project.

      - **description** *(string) --*

        A description that makes the build project easy to identify.

      - **source** *(dict) --*

        Information about the build input source code for this build project.

        - **type** *(string) --*

          The type of repository that contains the source code to be built. Valid values include:

          * ``BITBUCKET`` : The source code is in a Bitbucket repository.

          * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

          * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
          pipeline in AWS CodePipeline.

          * ``GITHUB`` : The source code is in a GitHub repository.

          * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

          * ``NO_SOURCE`` : The project does not have input source code.

          * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
          bucket.

        - **location** *(string) --*

          Information about the location of the source code to be built. Valid values include:

          * For source code settings that are specified in the source action of a pipeline in AWS
          CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
          ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
          action instead of this value.

          * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
          that contains the source code and the build spec (for example,
          ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

          * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
          the following.

            * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*object-name* .zip`` ).

            * The path to the folder that contains the source code (for example, `` *bucket-name*
            /*path* /*to* /*source-code* /*folder* /`` ).

          * For source code in a GitHub repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your GitHub
          account. Use the AWS CodeBuild console to start creating a build project. When you use
          the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
          application** page, for **Organization access** , choose **Request access** next to each
          repository you want to allow AWS CodeBuild to have access to, and then choose **Authorize
          application** . (After you have connected to your GitHub account, you do not need to
          finish creating the build project. You can leave the AWS CodeBuild console.) To instruct
          AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth`` object's
          ``type`` value to ``OAUTH`` .

          * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
          contains the source and the build spec. You must connect your AWS account to your
          Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
          you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
          access to your account** page, choose **Grant access** . (After you have connected to
          your Bitbucket account, you do not need to finish creating the build project. You can
          leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
          the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

        - **gitCloneDepth** *(integer) --*

          Information about the Git clone depth for the build project.

        - **gitSubmodulesConfig** *(dict) --*

          Information about the Git submodules configuration for the build project.

          - **fetchSubmodules** *(boolean) --*

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        - **buildspec** *(string) --*

          The build spec declaration to use for the builds in this build project.

          If this value is not specified, a build spec must be included along with the source code
          to be built.

        - **auth** *(dict) --*

          Information about the authorization settings for AWS CodeBuild to access the source code
          to be built.

          This information is for the AWS CodeBuild console's use only. Your code should not get or
          set this information directly.

          - **type** *(string) --*

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents the
            OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        - **reportBuildStatus** *(boolean) --*

          Set to true to report the status of a build's start and finish to your source provider.
          This option is valid only when your source provider is GitHub, GitHub Enterprise, or
          Bitbucket. If this is set and you use a different source provider, an
          invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source provider.

        - **insecureSsl** *(boolean) --*

          Enable this flag to ignore SSL warnings while connecting to the project source code.

        - **sourceIdentifier** *(string) --*

          An identifier for this project source.

      - **secondarySources** *(list) --*

        An array of ``ProjectSource`` objects.

        - *(dict) --*

          Information about the build input source code for the build project.

          - **type** *(string) --*

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS
            CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
            pipeline's source action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
            repository that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            GitHub account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to
            each repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do
            not need to finish creating the build project. You can leave the AWS CodeBuild
            console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
            set the ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
            When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
            **Confirm access to your account** page, choose **Grant access** . (After you have
            connected to your Bitbucket account, you do not need to finish creating the build
            project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
            this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
            ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --*

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source
            code to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source
            code to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --*

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

      - **sourceVersion** *(string) --*

        A version of the build input to be built for this project. If not specified, the latest
        version is used. If specified, it must be one of:

        * For AWS CodeCommit: the commit ID to use.

        * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
        the version of the source code you want to build. If a pull request ID is specified, it
        must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
        specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
        commit ID is used.

        * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
        the source code you want to build. If a branch name is specified, the branch's HEAD commit
        ID is used. If not specified, the default branch's HEAD commit ID is used.

        * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
        represents the build input ZIP file to use.

        If ``sourceVersion`` is specified at the build level, then that version takes precedence
        over this ``sourceVersion`` (at the project level).

        For more information, see `Source Version Sample with CodeBuild
        <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
        the *AWS CodeBuild User Guide* .

      - **secondarySourceVersions** *(list) --*

        An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
        at the build level, then they take over these ``secondarySourceVersions`` (at the project
        level).

        - *(dict) --*

          A source identifier and its corresponding version.

          - **sourceIdentifier** *(string) --*

            An identifier for a source in the build project.

          - **sourceVersion** *(string) --*

            The source version for the corresponding source identifier. If specified, must be one
            of:

            * For AWS CodeCommit: the commit ID to use.

            * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds
            to the version of the source code you want to build. If a pull request ID is specified,
            it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch
            name is specified, the branch's HEAD commit ID is used. If not specified, the default
            branch's HEAD commit ID is used.

            * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
            version of the source code you want to build. If a branch name is specified, the
            branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
            is used.

            * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
            represents the build input ZIP file to use.

            For more information, see `Source Version Sample with CodeBuild
            <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
            in the *AWS CodeBuild User Guide* .

      - **artifacts** *(dict) --*

        Information about the build output artifacts for the build project.

        - **type** *(string) --*

          The type of build output artifact. Valid values include:

          * ``CODEPIPELINE`` : The build project has build output generated through AWS
          CodePipeline.

          .. note::

             The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

          * ``NO_ARTIFACTS`` : The build project does not produce any build output.

          * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon
          S3).

        - **location** *(string) --*

          Information about the build output artifact location:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output locations instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output bucket.

        - **path** *(string) --*

          Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
          not specified, ``path`` is not used.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE``
          , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
          bucket at ``MyArtifacts/MyArtifact.zip`` .

        - **namespaceType** *(string) --*

          Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
          name and location to store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

            * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
            not specified.

          For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
          ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
          in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

        - **name** *(string) --*

          Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
          and store the output artifact:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output names instead of AWS
          CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
          set the name to be a forward slash ("/"), the artifact is stored in the root of the
          output bucket.

          For example:

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
          ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
          ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
          "``/`` ", the output artifact is stored in the root of the output bucket.

          * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
          ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* ``
          .

        - **packaging** *(string) --*

          The type of build output artifact to create:

          * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
          specified. This is because AWS CodePipeline manages its build output artifacts instead of
          AWS CodeBuild.

          * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
          build output is produced.

          * If ``type`` is set to ``S3`` , valid values include:

            * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
            build output. This is the default if ``packaging`` is not specified.

            * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
            build output.

        - **overrideArtifactName** *(boolean) --*

          If this flag is set, a name specified in the build spec file overrides the artifact name.
          The name specified in a build spec file is calculated at build time and uses the Shell
          Command Language. For example, you can append a date and time to your artifact name so
          that it is always unique.

        - **encryptionDisabled** *(boolean) --*

          Set to true if you do not want your output artifacts encrypted. This option is valid only
          if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with
          another artifacts type, an invalidInputException is thrown.

        - **artifactIdentifier** *(string) --*

          An identifier for this artifact definition.

      - **secondaryArtifacts** *(list) --*

        An array of ``ProjectArtifacts`` objects.

        - *(dict) --*

          Information about the build output artifacts for the build project.

          - **type** *(string) --*

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
            is not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
            stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
            and ``name`` is set to "``/`` ", the output artifact is stored in
            ``MyArtifacts/*build-ID* `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
            set with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

      - **cache** *(dict) --*

        Information about the cache for the build project.

        - **type** *(string) --*

          The type of cache used by the build project. Valid values include:

          * ``NO_CACHE`` : The build project does not use any cache.

          * ``S3`` : The build project reads and writes from and to S3.

          * ``LOCAL`` : The build project stores a cache locally on a build host that is only
          available to that build host.

        - **location** *(string) --*

          Information about the cache location:

          * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

          * ``S3`` : This is the S3 bucket name/prefix.

        - **modes** *(list) --*

          If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
          modes at the same time.

          * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
          After the cache is created, subsequent builds pull only the change between commits. This
          mode is a good choice for projects with a clean working directory and a source that is a
          large Git repository. If you choose this option and your project does not use a Git
          repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

          * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
          choice for projects that build or pull large Docker images. It can prevent the
          performance issues caused by pulling large Docker images down from the network.

          .. note::

              * You can use a Docker layer cache in the Linux environment only.

              * The ``privileged`` flag must be set so that your project has the required Docker
              permissions.

              * You should consider the security implications before you use a Docker layer cache.

          * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
          mode is a good choice if your build scenario is not suited to one of the other three
          local cache modes. If you use a custom cache:

            * Only directories can be specified for caching. You cannot specify individual files.

            * Symlinks are used to reference cached directories.

            * Cached directories are linked to your build before it downloads its project sources.
            Cached items are overriden if a source item has the same name. Directories are
            specified using cache paths in the buildspec file.

          - *(string) --*

      - **environment** *(dict) --*

        Information about the build environment for this build project.

        - **type** *(string) --*

          The type of build environment to use for related builds.

        - **image** *(string) --*

          The image tag or image digest that identifies the Docker image to use for this build
          project. Use the following formats:

          * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
          the tag "latest," use ``registry/repository:latest`` .

          * For an image digest: ``registry/repository@digest`` . For example, to specify an image
          with the digest
          "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
          ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
          .

        - **computeType** *(string) --*

          Information about the compute resources the build project uses. Available values include:

          * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

          * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

          * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

          For more information, see `Build Environment Compute Types
          <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
          in the *AWS CodeBuild User Guide.*

        - **environmentVariables** *(list) --*

          A set of environment variables to make available to builds for this build project.

          - *(dict) --*

            Information about an environment variable for a build project or a build.

            - **name** *(string) --*

              The name or key of the environment variable.

            - **value** *(string) --*

              The value of the environment variable.

              .. warning::

                We strongly discourage the use of environment variables to store sensitive values,
                especially AWS secret key IDs and secret access keys. Environment variables can be
                displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                Interface (AWS CLI).

            - **type** *(string) --*

              The type of environment variable. Valid values include:

              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
              Parameter Store.

              * ``PLAINTEXT`` : An environment variable in plaintext format.

              * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

        - **privilegedMode** *(boolean) --*

          Enables running the Docker daemon inside a Docker container. Set to true only if the
          build project is used to build Docker images. Otherwise, a build that attempts to
          interact with the Docker daemon fails. The default setting is ``false`` .

          You can initialize the Docker daemon during the install phase of your build by adding one
          of the following sets of commands to the install phase of your buildspec file:

          If the operating system's base image is Ubuntu Linux:

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

          If the operating system's base image is Alpine Linux and the previous command does not
          work, add the ``-t`` argument to ``timeout`` :

           ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
           --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

           ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

        - **certificate** *(string) --*

          The certificate to use with this build project.

        - **registryCredential** *(dict) --*

          The credentials for access to a private registry.

          - **credential** *(string) --*

            The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

            .. note::

              The ``credential`` can use the name of the credentials only if they exist in your
              current region.

          - **credentialProvider** *(string) --*

            The service that created the credentials to access a private Docker registry. The valid
            value, SECRETS_MANAGER, is for AWS Secrets Manager.

        - **imagePullCredentialsType** *(string) --*

          The type of credentials AWS CodeBuild uses to pull images in your build. There are two
          valid values:

          * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
          you modify your ECR repository policy to trust AWS CodeBuild's service principal.

          * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

          When you use a cross-account or private registry image, you must use SERVICE_ROLE
          credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
          credentials.

      - **serviceRole** *(string) --*

        The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to
        interact with dependent AWS services on behalf of the AWS account.

      - **timeoutInMinutes** *(integer) --*

        How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out
        any related build that did not get marked as completed. The default is 60 minutes.

      - **queuedTimeoutInMinutes** *(integer) --*

        The number of minutes a build is allowed to be queued before it times out.

      - **encryptionKey** *(string) --*

        The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
        encrypting the build output artifacts.

        .. note::

          You can use a cross-account KMS key to encrypt the build output artifacts if your service
          role has permission to that key.

        You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
        CMK's alias (using the format ``alias/*alias-name* `` ).

      - **tags** *(list) --*

        The tags for this build project.

        These tags are available for use by AWS services that support AWS CodeBuild build project
        tags.

        - *(dict) --*

          A tag, consisting of a key and a value.

          This tag is available for use by AWS services that support tags in AWS CodeBuild.

          - **key** *(string) --*

            The tag's key.

          - **value** *(string) --*

            The tag's value.

      - **created** *(datetime) --*

        When the build project was created, expressed in Unix time format.

      - **lastModified** *(datetime) --*

        When the build project's settings were last modified, expressed in Unix time format.

      - **webhook** *(dict) --*

        Information about a webhook that connects repository events to a build project in AWS
        CodeBuild.

        - **url** *(string) --*

          The URL to the webhook.

        - **payloadUrl** *(string) --*

          The AWS CodeBuild endpoint where webhook events are sent.

        - **secret** *(string) --*

          The secret token of the associated repository.

          .. note::

            A Bitbucket webhook does not support ``secret`` .

        - **branchFilter** *(string) --*

          A regular expression used to determine which repository branches are built when a webhook
          is triggered. If the name of a branch matches the regular expression, then it is built.
          If ``branchFilter`` is empty, then all branches are built.

          .. note::

            It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

        - **filterGroups** *(list) --*

          An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
          triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
          ``type`` .

          For a build to be triggered, at least one filter group in the ``filterGroups`` array must
          pass. For a filter group to pass, each of its filters must pass.

          - *(list) --*

            - *(dict) --*

              A filter used to determine which webhooks trigger a build.

              - **type** *(string) --*

                The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                  EVENT

                A webhook event triggers a build when the provided ``pattern`` matches one of four
                event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
                ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
                comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
                PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
                updated events.

                .. note::

                  The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                  ACTOR_ACCOUNT_ID

                A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
                account ID matches the regular expression ``pattern`` .

                  HEAD_REF

                A webhook event triggers a build when the head reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                ``refs/tags/tag-name`` .

                Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
                request, Bitbucket push, and Bitbucket pull request events.

                  BASE_REF

                A webhook event triggers a build when the base reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                .. note::

                  Works with pull request events only.

                  FILE_PATH

                A webhook triggers a build when the path of a changed file matches the regular
                expression ``pattern`` .

                .. note::

                  Works with GitHub and GitHub Enterprise push events only.

              - **pattern** *(string) --*

                For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
                specifies one or more events. For example, the webhook filter ``PUSH,
                PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
                and pull request updated events to trigger a build.

                For a ``WebHookFilter`` that uses any of the other filter types, a regular
                expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
                ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
                is a branch with a reference name ``refs/heads/branch-name`` .

              - **excludeMatchedPattern** *(boolean) --*

                Used to indicate that the ``pattern`` determines which webhook events do not
                trigger a build. If true, then a webhook event that does not match the ``pattern``
                triggers a build. If false, then a webhook event that matches the ``pattern``
                triggers a build.

        - **lastModifiedSecret** *(datetime) --*

          A timestamp that indicates the last time a repository's secret token was modified.

      - **vpcConfig** *(dict) --*

        Information about the VPC configuration that AWS CodeBuild accesses.

        - **vpcId** *(string) --*

          The ID of the Amazon VPC.

        - **subnets** *(list) --*

          A list of one or more subnet IDs in your Amazon VPC.

          - *(string) --*

        - **securityGroupIds** *(list) --*

          A list of one or more security groups IDs in your Amazon VPC.

          - *(string) --*

      - **badge** *(dict) --*

        Information about the build badge for the build project.

        - **badgeEnabled** *(boolean) --*

          Set this to true to generate a publicly accessible URL for your project's build badge.

        - **badgeRequestUrl** *(string) --*

          The publicly-accessible URL through which you can access the build badge for your project.

          The publicly accessible URL through which you can access the build badge for your project.

      - **logsConfig** *(dict) --*

        Information about logs for the build project. A project can create logs in Amazon
        CloudWatch Logs, an S3 bucket, or both.

        - **cloudWatchLogs** *(dict) --*

          Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
          enabled by default.

          - **status** *(string) --*

            The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
            values are:

            * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

            * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

          - **groupName** *(string) --*

            The group name of the logs in Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

          - **streamName** *(string) --*

            The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
            `Working with Log Groups and Log Streams
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
            .

        - **s3Logs** *(dict) --*

          Information about logs built to an S3 bucket for a build project. S3 logs are not enabled
          by default.

          - **status** *(string) --*

            The current status of the S3 build logs. Valid values are:

            * ``ENABLED`` : S3 build logs are enabled for this build project.

            * ``DISABLED`` : S3 build logs are not enabled for this build project.

          - **location** *(string) --*

            The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
            is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
            ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your S3 build log output encrypted. By default S3 build
            logs are encrypted.
    """


_RequiredClientUpdateProjectartifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectartifactsTypeDef", {"type": str}
)
_OptionalClientUpdateProjectartifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectartifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectartifactsTypeDef(
    _RequiredClientUpdateProjectartifactsTypeDef,
    _OptionalClientUpdateProjectartifactsTypeDef,
):
    """
    Type definition for `ClientUpdateProject` `artifacts`

    Information to be changed about the build output artifacts for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` , and
      ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output bucket at
      ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set the
      name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/`` ",
      the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no build
      output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_RequiredClientUpdateProjectcacheTypeDef = TypedDict(
    "_RequiredClientUpdateProjectcacheTypeDef", {"type": str}
)
_OptionalClientUpdateProjectcacheTypeDef = TypedDict(
    "_OptionalClientUpdateProjectcacheTypeDef",
    {"location": str, "modes": List[str]},
    total=False,
)


class ClientUpdateProjectcacheTypeDef(
    _RequiredClientUpdateProjectcacheTypeDef, _OptionalClientUpdateProjectcacheTypeDef
):
    """
    Type definition for `ClientUpdateProject` `cache`

    Stores recently used information so that it can be quickly accessed at a later time.

    - **type** *(string) --* **[REQUIRED]**

      The type of cache used by the build project. Valid values include:

      * ``NO_CACHE`` : The build project does not use any cache.

      * ``S3`` : The build project reads and writes from and to S3.

      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.

    - **location** *(string) --*

      Information about the cache location:

      * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

      * ``S3`` : This is the S3 bucket name/prefix.

    - **modes** *(list) --*

      If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache modes
      at the same time.

      * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources. After the
      cache is created, subsequent builds pull only the change between commits. This mode is a good
      choice for projects with a clean working directory and a source that is a large Git repository.
      If you choose this option and your project does not use a Git repository (GitHub, GitHub
      Enterprise, or Bitbucket), the option is ignored.

      * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good choice
      for projects that build or pull large Docker images. It can prevent the performance issues
      caused by pulling large Docker images down from the network.

      .. note::

          * You can use a Docker layer cache in the Linux environment only.

          * The ``privileged`` flag must be set so that your project has the required Docker
          permissions.

          * You should consider the security implications before you use a Docker layer cache.

      * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This mode
      is a good choice if your build scenario is not suited to one of the other three local cache
      modes. If you use a custom cache:

        * Only directories can be specified for caching. You cannot specify individual files.

        * Symlinks are used to reference cached directories.

        * Cached directories are linked to your build before it downloads its project sources. Cached
        items are overriden if a source item has the same name. Directories are specified using cache
        paths in the buildspec file.

      - *(string) --*
    """


_RequiredClientUpdateProjectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_RequiredClientUpdateProjectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str},
)
_OptionalClientUpdateProjectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_OptionalClientUpdateProjectenvironmentenvironmentVariablesTypeDef",
    {"type": str},
    total=False,
)


class ClientUpdateProjectenvironmentenvironmentVariablesTypeDef(
    _RequiredClientUpdateProjectenvironmentenvironmentVariablesTypeDef,
    _OptionalClientUpdateProjectenvironmentenvironmentVariablesTypeDef,
):
    """
    Type definition for `ClientUpdateProjectenvironment` `environmentVariables`

    Information about an environment variable for a build project or a build.

    - **name** *(string) --* **[REQUIRED]**

      The name or key of the environment variable.

    - **value** *(string) --* **[REQUIRED]**

      The value of the environment variable.

      .. warning::

        We strongly discourage the use of environment variables to store sensitive values,
        especially AWS secret key IDs and secret access keys. Environment variables can be
        displayed in plain text using the AWS CodeBuild console and the AWS Command Line
        Interface (AWS CLI).

    - **type** *(string) --*

      The type of environment variable. Valid values include:

      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
      Parameter Store.

      * ``PLAINTEXT`` : An environment variable in plaintext format.

      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.
    """


_ClientUpdateProjectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientUpdateProjectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
)


class ClientUpdateProjectenvironmentregistryCredentialTypeDef(
    _ClientUpdateProjectenvironmentregistryCredentialTypeDef
):
    """
    Type definition for `ClientUpdateProjectenvironment` `registryCredential`

    The credentials for access to a private registry.

    - **credential** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your current
        region.

    - **credentialProvider** *(string) --* **[REQUIRED]**

      The service that created the credentials to access a private Docker registry. The valid
      value, SECRETS_MANAGER, is for AWS Secrets Manager.
    """


_RequiredClientUpdateProjectenvironmentTypeDef = TypedDict(
    "_RequiredClientUpdateProjectenvironmentTypeDef",
    {"type": str, "image": str, "computeType": str},
)
_OptionalClientUpdateProjectenvironmentTypeDef = TypedDict(
    "_OptionalClientUpdateProjectenvironmentTypeDef",
    {
        "environmentVariables": List[
            ClientUpdateProjectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": str,
    },
    total=False,
)


class ClientUpdateProjectenvironmentTypeDef(
    _RequiredClientUpdateProjectenvironmentTypeDef,
    _OptionalClientUpdateProjectenvironmentTypeDef,
):
    """
    Type definition for `ClientUpdateProject` `environment`

    Information to be changed about the build environment for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build environment to use for related builds.

    - **image** *(string) --* **[REQUIRED]**

      The image tag or image digest that identifies the Docker image to use for this build project.
      Use the following formats:

      * For an image tag: ``registry/repository:tag`` . For example, to specify an image with the tag
      "latest," use ``registry/repository:latest`` .

      * For an image digest: ``registry/repository@digest`` . For example, to specify an image with
      the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
      ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
      .

    - **computeType** *(string) --* **[REQUIRED]**

      Information about the compute resources the build project uses. Available values include:

      * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

      * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

      * ``BUILD_GENERAL1_LARGE`` : Use up to 15 GB memory and 8 vCPUs for builds.

      For more information, see `Build Environment Compute Types
      <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__ in
      the *AWS CodeBuild User Guide.*

    - **environmentVariables** *(list) --*

      A set of environment variables to make available to builds for this build project.

      - *(dict) --*

        Information about an environment variable for a build project or a build.

        - **name** *(string) --* **[REQUIRED]**

          The name or key of the environment variable.

        - **value** *(string) --* **[REQUIRED]**

          The value of the environment variable.

          .. warning::

            We strongly discourage the use of environment variables to store sensitive values,
            especially AWS secret key IDs and secret access keys. Environment variables can be
            displayed in plain text using the AWS CodeBuild console and the AWS Command Line
            Interface (AWS CLI).

        - **type** *(string) --*

          The type of environment variable. Valid values include:

          * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
          Parameter Store.

          * ``PLAINTEXT`` : An environment variable in plaintext format.

          * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

    - **privilegedMode** *(boolean) --*

      Enables running the Docker daemon inside a Docker container. Set to true only if the build
      project is used to build Docker images. Otherwise, a build that attempts to interact with the
      Docker daemon fails. The default setting is ``false`` .

      You can initialize the Docker daemon during the install phase of your build by adding one of
      the following sets of commands to the install phase of your buildspec file:

      If the operating system's base image is Ubuntu Linux:

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
       --storage-driver=overlay&``

       ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

      If the operating system's base image is Alpine Linux and the previous command does not work,
      add the ``-t`` argument to ``timeout`` :

       ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375
       --storage-driver=overlay&``

       ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

    - **certificate** *(string) --*

      The certificate to use with this build project.

    - **registryCredential** *(dict) --*

      The credentials for access to a private registry.

      - **credential** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

        .. note::

          The ``credential`` can use the name of the credentials only if they exist in your current
          region.

      - **credentialProvider** *(string) --* **[REQUIRED]**

        The service that created the credentials to access a private Docker registry. The valid
        value, SECRETS_MANAGER, is for AWS Secrets Manager.

    - **imagePullCredentialsType** *(string) --*

      The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid
      values:

      * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that you
      modify your ECR repository policy to trust AWS CodeBuild's service principal.

      * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

      When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials.
      When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.
    """


_RequiredClientUpdateProjectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectlogsConfigcloudWatchLogsTypeDef", {"status": str}
)
_OptionalClientUpdateProjectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectlogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientUpdateProjectlogsConfigcloudWatchLogsTypeDef(
    _RequiredClientUpdateProjectlogsConfigcloudWatchLogsTypeDef,
    _OptionalClientUpdateProjectlogsConfigcloudWatchLogsTypeDef,
):
    """
    Type definition for `ClientUpdateProjectlogsConfig` `cloudWatchLogs`

    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
    enabled by default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
      are:

      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

    - **groupName** *(string) --*

      The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
      Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .

    - **streamName** *(string) --*

      The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
      `Working with Log Groups and Log Streams
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
      .
    """


_RequiredClientUpdateProjectlogsConfigs3LogsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectlogsConfigs3LogsTypeDef", {"status": str}
)
_OptionalClientUpdateProjectlogsConfigs3LogsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectlogsConfigs3LogsTypeDef",
    {"location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientUpdateProjectlogsConfigs3LogsTypeDef(
    _RequiredClientUpdateProjectlogsConfigs3LogsTypeDef,
    _OptionalClientUpdateProjectlogsConfigs3LogsTypeDef,
):
    """
    Type definition for `ClientUpdateProjectlogsConfig` `s3Logs`

    Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
    default.

    - **status** *(string) --* **[REQUIRED]**

      The current status of the S3 build logs. Valid values are:

      * ``ENABLED`` : S3 build logs are enabled for this build project.

      * ``DISABLED`` : S3 build logs are not enabled for this build project.

    - **location** *(string) --*

      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
      ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
      ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
      are encrypted.
    """


_ClientUpdateProjectlogsConfigTypeDef = TypedDict(
    "_ClientUpdateProjectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientUpdateProjectlogsConfigTypeDef(_ClientUpdateProjectlogsConfigTypeDef):
    """
    Type definition for `ClientUpdateProject` `logsConfig`

    Information about logs for the build project. A project can create logs in Amazon CloudWatch
    Logs, logs in an S3 bucket, or both.

    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:

        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

      - **groupName** *(string) --*

        The group name of the logs in Amazon CloudWatch Logs. For more information, see `Working with
        Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

      - **streamName** *(string) --*

        The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
        `Working with Log Groups and Log Streams
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
        .

    - **s3Logs** *(dict) --*

      Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by
      default.

      - **status** *(string) --* **[REQUIRED]**

        The current status of the S3 build logs. Valid values are:

        * ``ENABLED`` : S3 build logs are enabled for this build project.

        * ``DISABLED`` : S3 build logs are not enabled for this build project.

      - **location** *(string) --*

        The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is
        ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
        ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

      - **encryptionDisabled** *(boolean) --*

        Set to true if you do not want your S3 build log output encrypted. By default S3 build logs
        are encrypted.
    """


_RequiredClientUpdateProjectsecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectsecondaryArtifactsTypeDef", {"type": str}
)
_OptionalClientUpdateProjectsecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectsecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": str,
        "name": str,
        "packaging": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectsecondaryArtifactsTypeDef(
    _RequiredClientUpdateProjectsecondaryArtifactsTypeDef,
    _OptionalClientUpdateProjectsecondaryArtifactsTypeDef,
):
    """
    Type definition for `ClientUpdateProject` `secondaryArtifacts`

    Information about the build output artifacts for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of build output artifact. Valid values include:

      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.

      .. note::

         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

      * ``S3`` : The build project stores build output in Amazon Simple Storage Service (Amazon S3).

    - **location** *(string) --*

      Information about the build output artifact location:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

    - **path** *(string) --*

      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is not
      specified, ``path`` is not used.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``NONE`` ,
      and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in the output
      bucket at ``MyArtifacts/MyArtifact.zip`` .

    - **namespaceType** *(string) --*

      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the name
      and location to store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

        * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is not
        specified.

      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
      , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

    - **name** *(string) --*

      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name and
      store the output artifact:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you set
      the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

      For example:

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
      ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to "``/``
      ", the output artifact is stored in the root of the output bucket.

      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
      ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID* `` .

    - **packaging** *(string) --*

      The type of build output artifact to create:

      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if specified.
      This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.

      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because no
      build output is produced.

      * If ``type`` is set to ``S3`` , valid values include:

        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the build
        output. This is the default if ``packaging`` is not specified.

        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the build
        output.

    - **overrideArtifactName** *(boolean) --*

      If this flag is set, a name specified in the build spec file overrides the artifact name. The
      name specified in a build spec file is calculated at build time and uses the Shell Command
      Language. For example, you can append a date and time to your artifact name so that it is
      always unique.

    - **encryptionDisabled** *(boolean) --*

      Set to true if you do not want your output artifacts encrypted. This option is valid only if
      your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another
      artifacts type, an invalidInputException is thrown.

    - **artifactIdentifier** *(string) --*

      An identifier for this artifact definition.
    """


_ClientUpdateProjectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientUpdateProjectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
)


class ClientUpdateProjectsecondarySourceVersionsTypeDef(
    _ClientUpdateProjectsecondarySourceVersionsTypeDef
):
    """
    Type definition for `ClientUpdateProject` `secondarySourceVersions`

    A source identifier and its corresponding version.

    - **sourceIdentifier** *(string) --* **[REQUIRED]**

      An identifier for a source in the build project.

    - **sourceVersion** *(string) --* **[REQUIRED]**

      The source version for the corresponding source identifier. If specified, must be one of:

      * For AWS CodeCommit: the commit ID to use.

      * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
      the version of the source code you want to build. If a pull request ID is specified, it must
      use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ). If a branch name is
      specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD
      commit ID is used.

      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of
      the source code you want to build. If a branch name is specified, the branch's HEAD commit ID
      is used. If not specified, the default branch's HEAD commit ID is used.

      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents
      the build input ZIP file to use.

      For more information, see `Source Version Sample with CodeBuild
      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in the
      *AWS CodeBuild User Guide* .
    """


_RequiredClientUpdateProjectsecondarySourcesauthTypeDef = TypedDict(
    "_RequiredClientUpdateProjectsecondarySourcesauthTypeDef", {"type": str}
)
_OptionalClientUpdateProjectsecondarySourcesauthTypeDef = TypedDict(
    "_OptionalClientUpdateProjectsecondarySourcesauthTypeDef",
    {"resource": str},
    total=False,
)


class ClientUpdateProjectsecondarySourcesauthTypeDef(
    _RequiredClientUpdateProjectsecondarySourcesauthTypeDef,
    _OptionalClientUpdateProjectsecondarySourcesauthTypeDef,
):
    """
    Type definition for `ClientUpdateProjectsecondarySources` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code to
    be built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or set
    this information directly.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the
      OAuth authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientUpdateProjectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
)


class ClientUpdateProjectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientUpdateProjectsecondarySourcesgitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectsecondarySources` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientUpdateProjectsecondarySourcesTypeDef = TypedDict(
    "_RequiredClientUpdateProjectsecondarySourcesTypeDef", {"type": str}
)
_OptionalClientUpdateProjectsecondarySourcesTypeDef = TypedDict(
    "_OptionalClientUpdateProjectsecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectsecondarySourcesTypeDef(
    _RequiredClientUpdateProjectsecondarySourcesTypeDef,
    _OptionalClientUpdateProjectsecondarySourcesTypeDef,
):
    """
    Type definition for `ClientUpdateProject` `secondarySources`

    Information about the build input source code for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
      pipeline in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action
      instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that
      contains the source code and the build spec (for example,
      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the
      following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains
      the source and the build spec. You must connect your AWS account to your GitHub account. Use
      the AWS CodeBuild console to start creating a build project. When you use the console to
      connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for
      **Organization access** , choose **Request access** next to each repository you want to allow
      AWS CodeBuild to have access to, and then choose **Authorize application** . (After you have
      connected to your GitHub account, you do not need to finish creating the build project. You
      can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
      the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your Bitbucket
      account. Use the AWS CodeBuild console to start creating a build project. When you use the
      console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your
      account** page, choose **Grant access** . (After you have connected to your Bitbucket
      account, you do not need to finish creating the build project. You can leave the AWS
      CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the ``source``
      object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code to
      be built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code to
      be built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or set
      this information directly.

      - **type** *(string) --* **[REQUIRED]**

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the
        OAuth authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider. This
      option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If
      this is set and you use a different source provider, an invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_RequiredClientUpdateProjectsourceauthTypeDef = TypedDict(
    "_RequiredClientUpdateProjectsourceauthTypeDef", {"type": str}
)
_OptionalClientUpdateProjectsourceauthTypeDef = TypedDict(
    "_OptionalClientUpdateProjectsourceauthTypeDef", {"resource": str}, total=False
)


class ClientUpdateProjectsourceauthTypeDef(
    _RequiredClientUpdateProjectsourceauthTypeDef,
    _OptionalClientUpdateProjectsourceauthTypeDef,
):
    """
    Type definition for `ClientUpdateProjectsource` `auth`

    Information about the authorization settings for AWS CodeBuild to access the source code to be
    built.

    This information is for the AWS CodeBuild console's use only. Your code should not get or set
    this information directly.

    - **type** *(string) --* **[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.

      The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth
      authorization type.

    - **resource** *(string) --*

      The resource value that applies to the specified authorization type.
    """


_ClientUpdateProjectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectsourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}
)


class ClientUpdateProjectsourcegitSubmodulesConfigTypeDef(
    _ClientUpdateProjectsourcegitSubmodulesConfigTypeDef
):
    """
    Type definition for `ClientUpdateProjectsource` `gitSubmodulesConfig`

    Information about the Git submodules configuration for the build project.

    - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientUpdateProjectsourceTypeDef = TypedDict(
    "_RequiredClientUpdateProjectsourceTypeDef", {"type": str}
)
_OptionalClientUpdateProjectsourceTypeDef = TypedDict(
    "_OptionalClientUpdateProjectsourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectsourceTypeDef(
    _RequiredClientUpdateProjectsourceTypeDef, _OptionalClientUpdateProjectsourceTypeDef
):
    """
    Type definition for `ClientUpdateProject` `source`

    Information to be changed about the build input source code for the build project.

    - **type** *(string) --* **[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:

      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline
      in AWS CodePipeline.

      * ``GITHUB`` : The source code is in a GitHub repository.

      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

      * ``NO_SOURCE`` : The project does not have input source code.

      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.

    - **location** *(string) --*

      Information about the location of the source code to be built. Valid values include:

      * For source code settings that are specified in the source action of a pipeline in AWS
      CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
      ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action
      instead of this value.

      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that
      contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID*
      .amazonaws.com/v1/repos/*repo-name* `` ).

      * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the
      following.

        * The path to the ZIP file that contains the source code (for example, `` *bucket-name*
        /*path* /*to* /*object-name* .zip`` ).

        * The path to the folder that contains the source code (for example, `` *bucket-name* /*path*
        /*to* /*source-code* /*folder* /`` ).

      * For source code in a GitHub repository, the HTTPS clone URL to the repository that contains
      the source and the build spec. You must connect your AWS account to your GitHub account. Use
      the AWS CodeBuild console to start creating a build project. When you use the console to
      connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for
      **Organization access** , choose **Request access** next to each repository you want to allow
      AWS CodeBuild to have access to, and then choose **Authorize application** . (After you have
      connected to your GitHub account, you do not need to finish creating the build project. You can
      leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the
      ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

      * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
      contains the source and the build spec. You must connect your AWS account to your Bitbucket
      account. Use the AWS CodeBuild console to start creating a build project. When you use the
      console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your
      account** page, choose **Grant access** . (After you have connected to your Bitbucket account,
      you do not need to finish creating the build project. You can leave the AWS CodeBuild console.)
      To instruct AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
      object's ``type`` value to ``OAUTH`` .

    - **gitCloneDepth** *(integer) --*

      Information about the Git clone depth for the build project.

    - **gitSubmodulesConfig** *(dict) --*

      Information about the Git submodules configuration for the build project.

      - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

        Set to true to fetch Git submodules for your AWS CodeBuild build project.

    - **buildspec** *(string) --*

      The build spec declaration to use for the builds in this build project.

      If this value is not specified, a build spec must be included along with the source code to be
      built.

    - **auth** *(dict) --*

      Information about the authorization settings for AWS CodeBuild to access the source code to be
      built.

      This information is for the AWS CodeBuild console's use only. Your code should not get or set
      this information directly.

      - **type** *(string) --* **[REQUIRED]**

        .. note::

          This data type is deprecated and is no longer accurate or used.

        The authorization type to use. The only valid value is ``OAUTH`` , which represents the OAuth
        authorization type.

      - **resource** *(string) --*

        The resource value that applies to the specified authorization type.

    - **reportBuildStatus** *(boolean) --*

      Set to true to report the status of a build's start and finish to your source provider. This
      option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If
      this is set and you use a different source provider, an invalidInputException is thrown.

      .. note::

        The status of a build triggered by a webhook is always reported to your source provider.

    - **insecureSsl** *(boolean) --*

      Enable this flag to ignore SSL warnings while connecting to the project source code.

    - **sourceIdentifier** *(string) --*

      An identifier for this project source.
    """


_ClientUpdateProjecttagsTypeDef = TypedDict(
    "_ClientUpdateProjecttagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateProjecttagsTypeDef(_ClientUpdateProjecttagsTypeDef):
    """
    Type definition for `ClientUpdateProject` `tags`

    A tag, consisting of a key and a value.

    This tag is available for use by AWS services that support tags in AWS CodeBuild.

    - **key** *(string) --*

      The tag's key.

    - **value** *(string) --*

      The tag's value.
    """


_ClientUpdateProjectvpcConfigTypeDef = TypedDict(
    "_ClientUpdateProjectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientUpdateProjectvpcConfigTypeDef(_ClientUpdateProjectvpcConfigTypeDef):
    """
    Type definition for `ClientUpdateProject` `vpcConfig`

    VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

    - **vpcId** *(string) --*

      The ID of the Amazon VPC.

    - **subnets** *(list) --*

      A list of one or more subnet IDs in your Amazon VPC.

      - *(string) --*

    - **securityGroupIds** *(list) --*

      A list of one or more security groups IDs in your Amazon VPC.

      - *(string) --*
    """


_ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef",
    {"type": str, "pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef(
    _ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef
):
    """
    Type definition for `ClientUpdateWebhookResponsewebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --*

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four
      event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
      string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
      push, pull request created, and pull request updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
      account ID matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
      ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
      request, Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular
      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular
      expression ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --*

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
      specifies one or more events. For example, the webhook filter ``PUSH,
      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
      and pull request updated events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
      pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
      the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
      with a reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not trigger
      a build. If true, then a webhook event that does not match the ``pattern`` triggers a
      build. If false, then a webhook event that matches the ``pattern`` triggers a build.
    """


_ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientUpdateWebhookResponsewebhookTypeDef(
    _ClientUpdateWebhookResponsewebhookTypeDef
):
    """
    Type definition for `ClientUpdateWebhookResponse` `webhook`

    Information about a repository's webhook that is associated with a project in AWS CodeBuild.

    - **url** *(string) --*

      The URL to the webhook.

    - **payloadUrl** *(string) --*

      The AWS CodeBuild endpoint where webhook events are sent.

    - **secret** *(string) --*

      The secret token of the associated repository.

      .. note::

        A Bitbucket webhook does not support ``secret`` .

    - **branchFilter** *(string) --*

      A regular expression used to determine which repository branches are built when a webhook
      is triggered. If the name of a branch matches the regular expression, then it is built. If
      ``branchFilter`` is empty, then all branches are built.

      .. note::

        It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

    - **filterGroups** *(list) --*

      An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
      triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
      ``type`` .

      For a build to be triggered, at least one filter group in the ``filterGroups`` array must
      pass. For a filter group to pass, each of its filters must pass.

      - *(list) --*

        - *(dict) --*

          A filter used to determine which webhooks trigger a build.

          - **type** *(string) --*

            The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
            ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

              EVENT

            A webhook event triggers a build when the provided ``pattern`` matches one of four
            event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
            ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
            string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
            push, pull request created, and pull request updated events.

            .. note::

              The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

              ACTOR_ACCOUNT_ID

            A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
            account ID matches the regular expression ``pattern`` .

              HEAD_REF

            A webhook event triggers a build when the head reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` and
            ``refs/tags/tag-name`` .

            Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
            request, Bitbucket push, and Bitbucket pull request events.

              BASE_REF

            A webhook event triggers a build when the base reference matches the regular
            expression ``pattern`` . For example, ``refs/heads/branch-name`` .

            .. note::

              Works with pull request events only.

              FILE_PATH

            A webhook triggers a build when the path of a changed file matches the regular
            expression ``pattern`` .

            .. note::

              Works with GitHub and GitHub Enterprise push events only.

          - **pattern** *(string) --*

            For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
            specifies one or more events. For example, the webhook filter ``PUSH,
            PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
            and pull request updated events to trigger a build.

            For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
            pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
            the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
            with a reference name ``refs/heads/branch-name`` .

          - **excludeMatchedPattern** *(boolean) --*

            Used to indicate that the ``pattern`` determines which webhook events do not trigger
            a build. If true, then a webhook event that does not match the ``pattern`` triggers a
            build. If false, then a webhook event that matches the ``pattern`` triggers a build.

    - **lastModifiedSecret** *(datetime) --*

      A timestamp that indicates the last time a repository's secret token was modified.
    """


_ClientUpdateWebhookResponseTypeDef = TypedDict(
    "_ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientUpdateWebhookResponseTypeDef(_ClientUpdateWebhookResponseTypeDef):
    """
    Type definition for `ClientUpdateWebhook` `Response`

    - **webhook** *(dict) --*

      Information about a repository's webhook that is associated with a project in AWS CodeBuild.

      - **url** *(string) --*

        The URL to the webhook.

      - **payloadUrl** *(string) --*

        The AWS CodeBuild endpoint where webhook events are sent.

      - **secret** *(string) --*

        The secret token of the associated repository.

        .. note::

          A Bitbucket webhook does not support ``secret`` .

      - **branchFilter** *(string) --*

        A regular expression used to determine which repository branches are built when a webhook
        is triggered. If the name of a branch matches the regular expression, then it is built. If
        ``branchFilter`` is empty, then all branches are built.

        .. note::

          It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

      - **filterGroups** *(list) --*

        An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
        triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
        ``type`` .

        For a build to be triggered, at least one filter group in the ``filterGroups`` array must
        pass. For a filter group to pass, each of its filters must pass.

        - *(list) --*

          - *(dict) --*

            A filter used to determine which webhooks trigger a build.

            - **type** *(string) --*

              The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
              ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                EVENT

              A webhook event triggers a build when the provided ``pattern`` matches one of four
              event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
              ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
              string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all
              push, pull request created, and pull request updated events.

              .. note::

                The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                ACTOR_ACCOUNT_ID

              A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
              account ID matches the regular expression ``pattern`` .

                HEAD_REF

              A webhook event triggers a build when the head reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` and
              ``refs/tags/tag-name`` .

              Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
              request, Bitbucket push, and Bitbucket pull request events.

                BASE_REF

              A webhook event triggers a build when the base reference matches the regular
              expression ``pattern`` . For example, ``refs/heads/branch-name`` .

              .. note::

                Works with pull request events only.

                FILE_PATH

              A webhook triggers a build when the path of a changed file matches the regular
              expression ``pattern`` .

              .. note::

                Works with GitHub and GitHub Enterprise push events only.

            - **pattern** *(string) --*

              For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
              specifies one or more events. For example, the webhook filter ``PUSH,
              PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
              and pull request updated events to trigger a build.

              For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
              pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and
              the pattern ``^refs/heads/`` triggers a build when the head reference is a branch
              with a reference name ``refs/heads/branch-name`` .

            - **excludeMatchedPattern** *(boolean) --*

              Used to indicate that the ``pattern`` determines which webhook events do not trigger
              a build. If true, then a webhook event that does not match the ``pattern`` triggers a
              build. If false, then a webhook event that matches the ``pattern`` triggers a build.

      - **lastModifiedSecret** *(datetime) --*

        A timestamp that indicates the last time a repository's secret token was modified.
    """


_RequiredClientUpdateWebhookfilterGroupsTypeDef = TypedDict(
    "_RequiredClientUpdateWebhookfilterGroupsTypeDef", {"type": str, "pattern": str}
)
_OptionalClientUpdateWebhookfilterGroupsTypeDef = TypedDict(
    "_OptionalClientUpdateWebhookfilterGroupsTypeDef",
    {"excludeMatchedPattern": bool},
    total=False,
)


class ClientUpdateWebhookfilterGroupsTypeDef(
    _RequiredClientUpdateWebhookfilterGroupsTypeDef,
    _OptionalClientUpdateWebhookfilterGroupsTypeDef,
):
    """
    Type definition for `ClientUpdateWebhook` `filterGroups`

    A filter used to determine which webhooks trigger a build.

    - **type** *(string) --* **[REQUIRED]**

      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

        EVENT

      A webhook event triggers a build when the provided ``pattern`` matches one of four event
      types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
      ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a comma-separated
      string. For example, ``PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push,
      pull request created, and pull request updated events.

      .. note::

        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

        ACTOR_ACCOUNT_ID

      A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID
      matches the regular expression ``pattern`` .

        HEAD_REF

      A webhook event triggers a build when the head reference matches the regular expression
      ``pattern`` . For example, ``refs/heads/branch-name`` and ``refs/tags/tag-name`` .

      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request,
      Bitbucket push, and Bitbucket pull request events.

        BASE_REF

      A webhook event triggers a build when the base reference matches the regular expression
      ``pattern`` . For example, ``refs/heads/branch-name`` .

      .. note::

        Works with pull request events only.

        FILE_PATH

      A webhook triggers a build when the path of a changed file matches the regular expression
      ``pattern`` .

      .. note::

        Works with GitHub and GitHub Enterprise push events only.

    - **pattern** *(string) --* **[REQUIRED]**

      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that specifies
      one or more events. For example, the webhook filter ``PUSH, PULL_REQUEST_CREATED,
      PULL_REQUEST_UPDATED`` allows all push, pull request created, and pull request updated
      events to trigger a build.

      For a ``WebHookFilter`` that uses any of the other filter types, a regular expression
      pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its ``type`` and the
      pattern ``^refs/heads/`` triggers a build when the head reference is a branch with a
      reference name ``refs/heads/branch-name`` .

    - **excludeMatchedPattern** *(boolean) --*

      Used to indicate that the ``pattern`` determines which webhook events do not trigger a
      build. If true, then a webhook event that does not match the ``pattern`` triggers a build.
      If false, then a webhook event that matches the ``pattern`` triggers a build.
    """


_ListBuildsForProjectPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsForProjectPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBuildsForProjectPaginatePaginationConfigTypeDef(
    _ListBuildsForProjectPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBuildsForProjectPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListBuildsForProjectPaginateResponseTypeDef = TypedDict(
    "_ListBuildsForProjectPaginateResponseTypeDef",
    {"ids": List[str], "NextToken": str},
    total=False,
)


class ListBuildsForProjectPaginateResponseTypeDef(
    _ListBuildsForProjectPaginateResponseTypeDef
):
    """
    Type definition for `ListBuildsForProjectPaginate` `Response`

    - **ids** *(list) --*

      A list of build IDs for the specified build project, with each build ID representing a single
      build.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListBuildsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBuildsPaginatePaginationConfigTypeDef(
    _ListBuildsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBuildsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListBuildsPaginateResponseTypeDef = TypedDict(
    "_ListBuildsPaginateResponseTypeDef",
    {"ids": List[str], "NextToken": str},
    total=False,
)


class ListBuildsPaginateResponseTypeDef(_ListBuildsPaginateResponseTypeDef):
    """
    Type definition for `ListBuildsPaginate` `Response`

    - **ids** *(list) --*

      A list of build IDs, with each build ID representing a single build.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
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

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[str], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    Type definition for `ListProjectsPaginate` `Response`

    - **projects** *(list) --*

      The list of build project names, with each build project name representing a single build
      project.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
