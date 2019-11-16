"Main interface for opsworks type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "AppExistsWaitWaiterConfigTypeDef",
    "ClientCloneStackChefConfigurationTypeDef",
    "ClientCloneStackConfigurationManagerTypeDef",
    "ClientCloneStackCustomCookbooksSourceTypeDef",
    "ClientCloneStackResponseTypeDef",
    "ClientCreateAppAppSourceTypeDef",
    "ClientCreateAppDataSourcesTypeDef",
    "ClientCreateAppEnvironmentTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppSslConfigurationTypeDef",
    "ClientCreateDeploymentCommandTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsTypeDef",
    "ClientCreateInstanceResponseTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientCreateLayerCustomRecipesTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationTypeDef",
    "ClientCreateLayerResponseTypeDef",
    "ClientCreateLayerVolumeConfigurationsTypeDef",
    "ClientCreateStackChefConfigurationTypeDef",
    "ClientCreateStackConfigurationManagerTypeDef",
    "ClientCreateStackCustomCookbooksSourceTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    "ClientDescribeAgentVersionsResponseTypeDef",
    "ClientDescribeAppsResponseAppsAppSourceTypeDef",
    "ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    "ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    "ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    "ClientDescribeAppsResponseAppsTypeDef",
    "ClientDescribeAppsResponseTypeDef",
    "ClientDescribeCommandsResponseCommandsTypeDef",
    "ClientDescribeCommandsResponseTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    "ClientDescribeDeploymentsResponseTypeDef",
    "ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    "ClientDescribeEcsClustersResponseTypeDef",
    "ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    "ClientDescribeElasticIpsResponseTypeDef",
    "ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    "ClientDescribeElasticLoadBalancersResponseTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    "ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    "ClientDescribeMyUserProfileResponseTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    "ClientDescribeOperatingSystemsResponseTypeDef",
    "ClientDescribePermissionsResponsePermissionsTypeDef",
    "ClientDescribePermissionsResponseTypeDef",
    "ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    "ClientDescribeRaidArraysResponseTypeDef",
    "ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    "ClientDescribeRdsDbInstancesResponseTypeDef",
    "ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    "ClientDescribeServiceErrorsResponseTypeDef",
    "ClientDescribeStackProvisioningParametersResponseTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    "ClientDescribeStackSummaryResponseTypeDef",
    "ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    "ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    "ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    "ClientDescribeUserProfilesResponseTypeDef",
    "ClientDescribeVolumesResponseVolumesTypeDef",
    "ClientDescribeVolumesResponseTypeDef",
    "ClientGetHostnameSuggestionResponseTypeDef",
    "ClientGrantAccessResponseTemporaryCredentialTypeDef",
    "ClientGrantAccessResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRegisterEcsClusterResponseTypeDef",
    "ClientRegisterElasticIpResponseTypeDef",
    "ClientRegisterInstanceInstanceIdentityTypeDef",
    "ClientRegisterInstanceResponseTypeDef",
    "ClientRegisterVolumeResponseTypeDef",
    "ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    "ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    "ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    "ClientUpdateAppAppSourceTypeDef",
    "ClientUpdateAppDataSourcesTypeDef",
    "ClientUpdateAppEnvironmentTypeDef",
    "ClientUpdateAppSslConfigurationTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientUpdateLayerCustomRecipesTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    "ClientUpdateLayerVolumeConfigurationsTypeDef",
    "ClientUpdateStackChefConfigurationTypeDef",
    "ClientUpdateStackConfigurationManagerTypeDef",
    "ClientUpdateStackCustomCookbooksSourceTypeDef",
    "DeploymentSuccessfulWaitWaiterConfigTypeDef",
    "DescribeEcsClustersPaginatePaginationConfigTypeDef",
    "DescribeEcsClustersPaginateResponseEcsClustersTypeDef",
    "DescribeEcsClustersPaginateResponseTypeDef",
    "InstanceOnlineWaitWaiterConfigTypeDef",
    "InstanceRegisteredWaitWaiterConfigTypeDef",
    "InstanceStoppedWaitWaiterConfigTypeDef",
    "InstanceTerminatedWaitWaiterConfigTypeDef",
    "ServiceResourceCreateStackChefConfigurationTypeDef",
    "ServiceResourceCreateStackConfigurationManagerTypeDef",
    "ServiceResourceCreateStackCustomCookbooksSourceTypeDef",
    "StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "StackCreateLayerCloudWatchLogsConfigurationTypeDef",
    "StackCreateLayerCustomRecipesTypeDef",
    "StackCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    "StackCreateLayerLifecycleEventConfigurationTypeDef",
    "StackCreateLayerVolumeConfigurationsTypeDef",
)


_AppExistsWaitWaiterConfigTypeDef = TypedDict(
    "_AppExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class AppExistsWaitWaiterConfigTypeDef(_AppExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `AppExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ClientCloneStackChefConfigurationTypeDef = TypedDict(
    "_ClientCloneStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientCloneStackChefConfigurationTypeDef(
    _ClientCloneStackChefConfigurationTypeDef
):
    """
    Type definition for `ClientCloneStack` `ChefConfiguration`

    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.

    - **BerkshelfVersion** *(string) --*

      The Berkshelf version.
    """


_ClientCloneStackConfigurationManagerTypeDef = TypedDict(
    "_ClientCloneStackConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientCloneStackConfigurationManagerTypeDef(
    _ClientCloneStackConfigurationManagerTypeDef
):
    """
    Type definition for `ClientCloneStack` `ConfigurationManager`

    The configuration manager. When you clone a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to
      12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientCloneStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientCloneStackCustomCookbooksSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCloneStackCustomCookbooksSourceTypeDef(
    _ClientCloneStackCustomCookbooksSourceTypeDef
):
    """
    Type definition for `ClientCloneStack` `CustomCookbooksSource`

    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_ClientCloneStackResponseTypeDef = TypedDict(
    "_ClientCloneStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCloneStackResponseTypeDef(_ClientCloneStackResponseTypeDef):
    """
    Type definition for `ClientCloneStack` `Response`

    Contains the response to a ``CloneStack`` request.

    - **StackId** *(string) --*

      The cloned stack ID.
    """


_ClientCreateAppAppSourceTypeDef = TypedDict(
    "_ClientCreateAppAppSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCreateAppAppSourceTypeDef(_ClientCreateAppAppSourceTypeDef):
    """
    Type definition for `ClientCreateApp` `AppSource`

    A ``Source`` object that specifies the app repository.

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_ClientCreateAppDataSourcesTypeDef = TypedDict(
    "_ClientCreateAppDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientCreateAppDataSourcesTypeDef(_ClientCreateAppDataSourcesTypeDef):
    """
    Type definition for `ClientCreateApp` `DataSources`

    Describes an app's data source.

    - **Type** *(string) --*

      The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` ,
      ``RdsDbInstance`` , or ``None`` .

    - **Arn** *(string) --*

      The data source's ARN.

    - **DatabaseName** *(string) --*

      The database name.
    """


_RequiredClientCreateAppEnvironmentTypeDef = TypedDict(
    "_RequiredClientCreateAppEnvironmentTypeDef", {"Key": str, "Value": str}
)
_OptionalClientCreateAppEnvironmentTypeDef = TypedDict(
    "_OptionalClientCreateAppEnvironmentTypeDef", {"Secure": bool}, total=False
)


class ClientCreateAppEnvironmentTypeDef(
    _RequiredClientCreateAppEnvironmentTypeDef,
    _OptionalClientCreateAppEnvironmentTypeDef,
):
    """
    Type definition for `ClientCreateApp` `Environment`

    Represents an app's environment variable.

    - **Key** *(string) --* **[REQUIRED]**

      (Required) The environment variable's name, which can consist of up to 64 characters and must
      be specified. The name can contain upper- and lowercase letters, numbers, and underscores
      (_), but it must start with a letter or underscore.

    - **Value** *(string) --* **[REQUIRED]**

      (Optional) The environment variable's value, which can be left empty. If you specify a value,
      it can contain up to 256 characters, which must all be printable.

    - **Secure** *(boolean) --*

      (Optional) Whether the variable's value will be returned by the  DescribeApps action. To
      conceal an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` then
      returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure``
      is ``false`` .
    """


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef", {"AppId": str}, total=False
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    Type definition for `ClientCreateApp` `Response`

    Contains the response to a ``CreateApp`` request.

    - **AppId** *(string) --*

      The app ID.
    """


_RequiredClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateAppSslConfigurationTypeDef",
    {"Certificate": str, "PrivateKey": str},
)
_OptionalClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateAppSslConfigurationTypeDef", {"Chain": str}, total=False
)


class ClientCreateAppSslConfigurationTypeDef(
    _RequiredClientCreateAppSslConfigurationTypeDef,
    _OptionalClientCreateAppSslConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApp` `SslConfiguration`

    An ``SslConfiguration`` object with the SSL configuration.

    - **Certificate** *(string) --* **[REQUIRED]**

      The contents of the certificate's domain.crt file.

    - **PrivateKey** *(string) --* **[REQUIRED]**

      The private key; the contents of the certificate's domain.kex file.

    - **Chain** *(string) --*

      Optional. Can be used to specify an intermediate certificate authority key or client
      authentication.
    """


_RequiredClientCreateDeploymentCommandTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentCommandTypeDef", {"Name": str}
)
_OptionalClientCreateDeploymentCommandTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentCommandTypeDef",
    {"Args": Dict[str, List[str]]},
    total=False,
)


class ClientCreateDeploymentCommandTypeDef(
    _RequiredClientCreateDeploymentCommandTypeDef,
    _OptionalClientCreateDeploymentCommandTypeDef,
):
    """
    Type definition for `ClientCreateDeployment` `Command`

    A ``DeploymentCommand`` object that specifies the deployment command and any associated arguments.

    - **Name** *(string) --* **[REQUIRED]**

      Specifies the operation. You can specify only one command.

      For stacks, the following commands are available:

      * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an ``Args``
      parameter named ``recipes`` to the list of recipes to be executed. For example, to execute
      ``phpapp::appsetup`` , set ``Args`` to ``{"recipes":["phpapp::appsetup"]}`` .

      * ``install_dependencies`` : Install the stack's dependencies.

      * ``update_custom_cookbooks`` : Update the stack's custom cookbooks.

      * ``update_dependencies`` : Update the stack's dependencies.

      .. note::

        The update_dependencies and install_dependencies commands are supported only for Linux
        instances. You can run the commands successfully on Windows instances, but they do nothing.

      For apps, the following commands are available:

      * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter named
      ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The default setting
      is {"migrate":["false"]}.

      * ``rollback`` Roll the app back to the previous version. When you update an app, AWS OpsWorks
      Stacks stores the previous version, up to a maximum of five versions. You can use this command
      to roll an app back as many as four versions.

      * ``start`` : Start the app's web or application server.

      * ``stop`` : Stop the app's web or application server.

      * ``restart`` : Restart the app's web or application server.

      * ``undeploy`` : Undeploy the app.

    - **Args** *(dict) --*

      The arguments of those commands that take arguments. It should be set to a JSON object with the
      following format:

       ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...], ...}``

      The ``update_dependencies`` command takes two arguments:

      * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS you
      want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the ``allow_reboot``
      argument to true.

      * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if
      necessary, after installing the updates. This argument can be set to either ``true`` or
      ``false`` . The default value is ``false`` .

      For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the following.

       ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``

      - *(string) --*

        - *(list) --*

          - *(string) --*
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef", {"DeploymentId": str}, total=False
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

    Contains the response to a ``CreateDeployment`` request.

    - **DeploymentId** *(string) --*

      The deployment ID, which can be used with other requests to identify the deployment.
    """


_ClientCreateInstanceBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
    },
    total=False,
)


class ClientCreateInstanceBlockDeviceMappingsEbsTypeDef(
    _ClientCreateInstanceBlockDeviceMappingsEbsTypeDef
):
    """
    Type definition for `ClientCreateInstanceBlockDeviceMappings` `Ebs`

    An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is
    launched.

    - **SnapshotId** *(string) --*

      The snapshot ID.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports. For more
      information, see `EbsBlockDevice
      <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

    - **VolumeSize** *(integer) --*

      The volume size, in GiB. For more information, see `EbsBlockDevice
      <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

    - **VolumeType** *(string) --*

      The volume type. ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS
      (SSD) volumes, ``st1`` for Throughput Optimized hard disk drives (HDD), ``sc1`` for Cold
      HDD,and ``standard`` for Magnetic volumes.

      If you specify the ``io1`` volume type, you must also specify a value for the ``Iops``
      attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1.
      AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50
      x (volume size).

    - **DeleteOnTermination** *(boolean) --*

      Whether the volume is deleted on instance termination.
    """


_ClientCreateInstanceBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientCreateInstanceBlockDeviceMappingsTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": ClientCreateInstanceBlockDeviceMappingsEbsTypeDef,
    },
    total=False,
)


class ClientCreateInstanceBlockDeviceMappingsTypeDef(
    _ClientCreateInstanceBlockDeviceMappingsTypeDef
):
    """
    Type definition for `ClientCreateInstance` `BlockDeviceMappings`

    Describes a block device mapping. This data type maps directly to the Amazon EC2
    `BlockDeviceMapping
    <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ data
    type.

    - **DeviceName** *(string) --*

      The device name that is exposed to the instance, such as ``/dev/sdh`` . For the root device,
      you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and AWS
      OpsWorks Stacks will provide the correct device name.

    - **NoDevice** *(string) --*

      Suppresses the specified device included in the AMI's block device mapping.

    - **VirtualName** *(string) --*

      The virtual device name. For more information, see `BlockDeviceMapping
      <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ .

    - **Ebs** *(dict) --*

      An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is
      launched.

      - **SnapshotId** *(string) --*

        The snapshot ID.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports. For more
        information, see `EbsBlockDevice
        <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

      - **VolumeSize** *(integer) --*

        The volume size, in GiB. For more information, see `EbsBlockDevice
        <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

      - **VolumeType** *(string) --*

        The volume type. ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS
        (SSD) volumes, ``st1`` for Throughput Optimized hard disk drives (HDD), ``sc1`` for Cold
        HDD,and ``standard`` for Magnetic volumes.

        If you specify the ``io1`` volume type, you must also specify a value for the ``Iops``
        attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1.
        AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50
        x (volume size).

      - **DeleteOnTermination** *(boolean) --*

        Whether the volume is deleted on instance termination.
    """


_ClientCreateInstanceResponseTypeDef = TypedDict(
    "_ClientCreateInstanceResponseTypeDef", {"InstanceId": str}, total=False
)


class ClientCreateInstanceResponseTypeDef(_ClientCreateInstanceResponseTypeDef):
    """
    Type definition for `ClientCreateInstance` `Response`

    Contains the response to a ``CreateInstance`` request.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": str,
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": str,
        "Encoding": str,
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    """
    Type definition for `ClientCreateLayerCloudWatchLogsConfiguration` `LogStreams`

    Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
    about members of this data type, see the `CloudWatch Logs Agent Reference
    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **LogGroupName** *(string) --*

      Specifies the destination log group. A log group is created automatically if it doesn't
      already exist. Log group names can be between 1 and 512 characters long. Allowed characters
      include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
      (period).

    - **DatetimeFormat** *(string) --*

      Specifies how the time stamp is extracted from logs. For more information, see the
      `CloudWatch Logs Agent Reference
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **TimeZone** *(string) --*

      Specifies the time zone of log event time stamps.

    - **File** *(string) --*

      Specifies log files that you want to push to CloudWatch Logs.

       ``File`` can point to a specific file or multiple files (by using wild card characters
       such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
       based on file modification time. We recommend that you use wild card characters to specify
       a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
       ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
       use a wildcard to match multiple file types, such as ``access_log_80`` and
       ``access_log_443`` . To specify multiple, different file types, add another log stream
       entry to the configuration file, so that each log file type is stored in a different log
       group.

      Zipped files are not supported.

    - **FileFingerprintLines** *(string) --*

      Specifies the range of lines for identifying a file. The valid values are one number, or
      two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
      line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
      Logs unless all specified lines are available.

    - **MultiLineStartPattern** *(string) --*

      Specifies the pattern for identifying the start of a log message.

    - **InitialPosition** *(string) --*

      Specifies where to start to read data (start_of_file or end_of_file). The default is
      start_of_file. This setting is only used if there is no state persisted for that log stream.

    - **Encoding** *(string) --*

      Specifies the encoding of the log file so that the file can be read correctly. The default
      is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

    - **BufferDuration** *(integer) --*

      Specifies the time duration for the batching of log events. The minimum value is 5000ms and
      default value is 5000ms.

    - **BatchCount** *(integer) --*

      Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

    - **BatchSize** *(integer) --*

      Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
      default value is 32768 bytes. This size is calculated as the sum of all event messages in
      UTF-8, plus 26 bytes for each log event.
    """


_ClientCreateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[
            ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
        ],
    },
    total=False,
)


class ClientCreateLayerCloudWatchLogsConfigurationTypeDef(
    _ClientCreateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateLayer` `CloudWatchLogsConfiguration`

    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .

    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.

    - **LogStreams** *(list) --*

      A list of configuration options for CloudWatch Logs.

      - *(dict) --*

        Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
        about members of this data type, see the `CloudWatch Logs Agent Reference
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **LogGroupName** *(string) --*

          Specifies the destination log group. A log group is created automatically if it doesn't
          already exist. Log group names can be between 1 and 512 characters long. Allowed characters
          include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
          (period).

        - **DatetimeFormat** *(string) --*

          Specifies how the time stamp is extracted from logs. For more information, see the
          `CloudWatch Logs Agent Reference
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **TimeZone** *(string) --*

          Specifies the time zone of log event time stamps.

        - **File** *(string) --*

          Specifies log files that you want to push to CloudWatch Logs.

           ``File`` can point to a specific file or multiple files (by using wild card characters
           such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
           based on file modification time. We recommend that you use wild card characters to specify
           a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
           ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
           use a wildcard to match multiple file types, such as ``access_log_80`` and
           ``access_log_443`` . To specify multiple, different file types, add another log stream
           entry to the configuration file, so that each log file type is stored in a different log
           group.

          Zipped files are not supported.

        - **FileFingerprintLines** *(string) --*

          Specifies the range of lines for identifying a file. The valid values are one number, or
          two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
          line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
          Logs unless all specified lines are available.

        - **MultiLineStartPattern** *(string) --*

          Specifies the pattern for identifying the start of a log message.

        - **InitialPosition** *(string) --*

          Specifies where to start to read data (start_of_file or end_of_file). The default is
          start_of_file. This setting is only used if there is no state persisted for that log stream.

        - **Encoding** *(string) --*

          Specifies the encoding of the log file so that the file can be read correctly. The default
          is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

        - **BufferDuration** *(integer) --*

          Specifies the time duration for the batching of log events. The minimum value is 5000ms and
          default value is 5000ms.

        - **BatchCount** *(integer) --*

          Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

        - **BatchSize** *(integer) --*

          Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
          default value is 32768 bytes. This size is calculated as the sum of all event messages in
          UTF-8, plus 26 bytes for each log event.
    """


_ClientCreateLayerCustomRecipesTypeDef = TypedDict(
    "_ClientCreateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientCreateLayerCustomRecipesTypeDef(_ClientCreateLayerCustomRecipesTypeDef):
    """
    Type definition for `ClientCreateLayer` `CustomRecipes`

    A ``LayerCustomRecipes`` object that specifies the layer custom recipes.

    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.

      - *(string) --*

    - **Configure** *(list) --*

      An array of custom recipe names to be run following a ``configure`` event.

      - *(string) --*

    - **Deploy** *(list) --*

      An array of custom recipe names to be run following a ``deploy`` event.

      - *(string) --*

    - **Undeploy** *(list) --*

      An array of custom recipe names to be run following a ``undeploy`` event.

      - *(string) --*

    - **Shutdown** *(list) --*

      An array of custom recipe names to be run following a ``shutdown`` event.

      - *(string) --*
    """


_ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef(
    _ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    Type definition for `ClientCreateLayerLifecycleEventConfiguration` `Shutdown`

    A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

    - **ExecutionTimeout** *(integer) --*

      The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
      before shutting down an instance.

    - **DelayUntilElbConnectionsDrained** *(boolean) --*

      Whether to enable Elastic Load Balancing connection draining. For more information, see
      `Connection Draining
      <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_ClientCreateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_ClientCreateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class ClientCreateLayerLifecycleEventConfigurationTypeDef(
    _ClientCreateLayerLifecycleEventConfigurationTypeDef
):
    """
    Type definition for `ClientCreateLayer` `LifecycleEventConfiguration`

    A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to
    specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.

      - **DelayUntilElbConnectionsDrained** *(boolean) --*

        Whether to enable Elastic Load Balancing connection draining. For more information, see
        `Connection Draining
        <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_ClientCreateLayerResponseTypeDef = TypedDict(
    "_ClientCreateLayerResponseTypeDef", {"LayerId": str}, total=False
)


class ClientCreateLayerResponseTypeDef(_ClientCreateLayerResponseTypeDef):
    """
    Type definition for `ClientCreateLayer` `Response`

    Contains the response to a ``CreateLayer`` request.

    - **LayerId** *(string) --*

      The layer ID.
    """


_RequiredClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientCreateLayerVolumeConfigurationsTypeDef",
    {"MountPoint": str, "NumberOfDisks": int, "Size": int},
)
_OptionalClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientCreateLayerVolumeConfigurationsTypeDef",
    {"RaidLevel": int, "VolumeType": str, "Iops": int, "Encrypted": bool},
    total=False,
)


class ClientCreateLayerVolumeConfigurationsTypeDef(
    _RequiredClientCreateLayerVolumeConfigurationsTypeDef,
    _OptionalClientCreateLayerVolumeConfigurationsTypeDef,
):
    """
    Type definition for `ClientCreateLayer` `VolumeConfigurations`

    Describes an Amazon EBS volume configuration.

    - **MountPoint** *(string) --* **[REQUIRED]**

      The volume mount point. For example "/dev/sdh".

    - **RaidLevel** *(integer) --*

      The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

    - **NumberOfDisks** *(integer) --* **[REQUIRED]**

      The number of disks in the volume.

    - **Size** *(integer) --* **[REQUIRED]**

      The volume size.

    - **VolumeType** *(string) --*

      The volume type. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .

      * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum
      size of 1024 GiB.

      * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a
      maximum size of 16384 GiB.

      * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB
      and a maximum size of 16384 GiB.

      * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must
      have a minimum size of 500 GiB and a maximum size of 16384 GiB.

      * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size
      of 16384 GiB.

    - **Iops** *(integer) --*

      For PIOPS volumes, the IOPS per disk.

    - **Encrypted** *(boolean) --*

      Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon EBS
      Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
    """


_ClientCreateStackChefConfigurationTypeDef = TypedDict(
    "_ClientCreateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientCreateStackChefConfigurationTypeDef(
    _ClientCreateStackChefConfigurationTypeDef
):
    """
    Type definition for `ClientCreateStack` `ChefConfiguration`

    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.

    - **BerkshelfVersion** *(string) --*

      The Berkshelf version.
    """


_ClientCreateStackConfigurationManagerTypeDef = TypedDict(
    "_ClientCreateStackConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientCreateStackConfigurationManagerTypeDef(
    _ClientCreateStackConfigurationManagerTypeDef
):
    """
    Type definition for `ClientCreateStack` `ConfigurationManager`

    The configuration manager. When you create a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to
      12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientCreateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientCreateStackCustomCookbooksSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCreateStackCustomCookbooksSourceTypeDef(
    _ClientCreateStackCustomCookbooksSourceTypeDef
):
    """
    Type definition for `ClientCreateStack` `CustomCookbooksSource`

    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    Type definition for `ClientCreateStack` `Response`

    Contains the response to a ``CreateStack`` request.

    - **StackId** *(string) --*

      The stack ID, which is an opaque string that you use to identify the stack when performing
      actions such as ``DescribeStacks`` .
    """


_ClientCreateUserProfileResponseTypeDef = TypedDict(
    "_ClientCreateUserProfileResponseTypeDef", {"IamUserArn": str}, total=False
)


class ClientCreateUserProfileResponseTypeDef(_ClientCreateUserProfileResponseTypeDef):
    """
    Type definition for `ClientCreateUserProfile` `Response`

    Contains the response to a ``CreateUserProfile`` request.

    - **IamUserArn** *(string) --*

      The user's IAM ARN.
    """


_ClientDescribeAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeAgentVersionsConfigurationManagerTypeDef(
    _ClientDescribeAgentVersionsConfigurationManagerTypeDef
):
    """
    Type definition for `ClientDescribeAgentVersions` `ConfigurationManager`

    The configuration manager.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to
      12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef(
    _ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef
):
    """
    Type definition for `ClientDescribeAgentVersionsResponseAgentVersions` `ConfigurationManager`

    The configuration manager.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
      and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientDescribeAgentVersionsResponseAgentVersionsTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    {
        "Version": str,
        "ConfigurationManager": ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef,
    },
    total=False,
)


class ClientDescribeAgentVersionsResponseAgentVersionsTypeDef(
    _ClientDescribeAgentVersionsResponseAgentVersionsTypeDef
):
    """
    Type definition for `ClientDescribeAgentVersionsResponse` `AgentVersions`

    Describes an agent version.

    - **Version** *(string) --*

      The agent version.

    - **ConfigurationManager** *(dict) --*

      The configuration manager.

      - **Name** *(string) --*

        The name. This parameter must be set to "Chef".

      - **Version** *(string) --*

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
        and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientDescribeAgentVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseTypeDef",
    {"AgentVersions": List[ClientDescribeAgentVersionsResponseAgentVersionsTypeDef]},
    total=False,
)


class ClientDescribeAgentVersionsResponseTypeDef(
    _ClientDescribeAgentVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAgentVersions` `Response`

    Contains the response to a ``DescribeAgentVersions`` request.

    - **AgentVersions** *(list) --*

      The agent versions for the specified stack or configuration manager. Note that this value is
      the complete version number, not the abbreviated number used by the console.

      - *(dict) --*

        Describes an agent version.

        - **Version** *(string) --*

          The agent version.

        - **ConfigurationManager** *(dict) --*

          The configuration manager.

          - **Name** *(string) --*

            The name. This parameter must be set to "Chef".

          - **Version** *(string) --*

            The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
            and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientDescribeAppsResponseAppsAppSourceTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsAppSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientDescribeAppsResponseAppsAppSourceTypeDef(
    _ClientDescribeAppsResponseAppsAppSourceTypeDef
):
    """
    Type definition for `ClientDescribeAppsResponseApps` `AppSource`

    A ``Source`` object that describes the app repository.

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
      the user name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
      value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
      value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new
      versions of an application. One of the simplest approaches is to have branches or
      revisions in your repository that represent different versions that can potentially be
      deployed.
    """


_ClientDescribeAppsResponseAppsDataSourcesTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientDescribeAppsResponseAppsDataSourcesTypeDef(
    _ClientDescribeAppsResponseAppsDataSourcesTypeDef
):
    """
    Type definition for `ClientDescribeAppsResponseApps` `DataSources`

    Describes an app's data source.

    - **Type** *(string) --*

      The data source's type, ``AutoSelectOpsworksMysqlInstance`` ,
      ``OpsworksMysqlInstance`` , ``RdsDbInstance`` , or ``None`` .

    - **Arn** *(string) --*

      The data source's ARN.

    - **DatabaseName** *(string) --*

      The database name.
    """


_ClientDescribeAppsResponseAppsEnvironmentTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    {"Key": str, "Value": str, "Secure": bool},
    total=False,
)


class ClientDescribeAppsResponseAppsEnvironmentTypeDef(
    _ClientDescribeAppsResponseAppsEnvironmentTypeDef
):
    """
    Type definition for `ClientDescribeAppsResponseApps` `Environment`

    Represents an app's environment variable.

    - **Key** *(string) --*

      (Required) The environment variable's name, which can consist of up to 64 characters
      and must be specified. The name can contain upper- and lowercase letters, numbers,
      and underscores (_), but it must start with a letter or underscore.

    - **Value** *(string) --*

      (Optional) The environment variable's value, which can be left empty. If you specify
      a value, it can contain up to 256 characters, which must all be printable.

    - **Secure** *(boolean) --*

      (Optional) Whether the variable's value will be returned by the  DescribeApps action.
      To conceal an environment variable's value, set ``Secure`` to ``true`` .
      ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The
      default value for ``Secure`` is ``false`` .
    """


_ClientDescribeAppsResponseAppsSslConfigurationTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    {"Certificate": str, "PrivateKey": str, "Chain": str},
    total=False,
)


class ClientDescribeAppsResponseAppsSslConfigurationTypeDef(
    _ClientDescribeAppsResponseAppsSslConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeAppsResponseApps` `SslConfiguration`

    An ``SslConfiguration`` object with the SSL configuration.

    - **Certificate** *(string) --*

      The contents of the certificate's domain.crt file.

    - **PrivateKey** *(string) --*

      The private key; the contents of the certificate's domain.kex file.

    - **Chain** *(string) --*

      Optional. Can be used to specify an intermediate certificate authority key or client
      authentication.
    """


_ClientDescribeAppsResponseAppsTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List[ClientDescribeAppsResponseAppsDataSourcesTypeDef],
        "Type": str,
        "AppSource": ClientDescribeAppsResponseAppsAppSourceTypeDef,
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": ClientDescribeAppsResponseAppsSslConfigurationTypeDef,
        "Attributes": Dict[str, str],
        "CreatedAt": str,
        "Environment": List[ClientDescribeAppsResponseAppsEnvironmentTypeDef],
    },
    total=False,
)


class ClientDescribeAppsResponseAppsTypeDef(_ClientDescribeAppsResponseAppsTypeDef):
    """
    Type definition for `ClientDescribeAppsResponse` `Apps`

    A description of the app.

    - **AppId** *(string) --*

      The app ID.

    - **StackId** *(string) --*

      The app stack ID.

    - **Shortname** *(string) --*

      The app's short name.

    - **Name** *(string) --*

      The app name.

    - **Description** *(string) --*

      A description of the app.

    - **DataSources** *(list) --*

      The app's data sources.

      - *(dict) --*

        Describes an app's data source.

        - **Type** *(string) --*

          The data source's type, ``AutoSelectOpsworksMysqlInstance`` ,
          ``OpsworksMysqlInstance`` , ``RdsDbInstance`` , or ``None`` .

        - **Arn** *(string) --*

          The data source's ARN.

        - **DatabaseName** *(string) --*

          The database name.

    - **Type** *(string) --*

      The app type.

    - **AppSource** *(dict) --*

      A ``Source`` object that describes the app repository.

      - **Type** *(string) --*

        The repository type.

      - **Url** *(string) --*

        The source URL. The following is an example of an Amazon S3 source URL:
        ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

      - **Username** *(string) --*

        This parameter depends on the repository type.

        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
        the user name.

      - **Password** *(string) --*

        When included in a request, the parameter depends on the repository type.

        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

        * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

        For more information on how to safely handle IAM credentials, see
        `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
        <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
        value.

      - **SshKey** *(string) --*

        In requests, the repository's SSH key.

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
        value.

      - **Revision** *(string) --*

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new
        versions of an application. One of the simplest approaches is to have branches or
        revisions in your repository that represent different versions that can potentially be
        deployed.

    - **Domains** *(list) --*

      The app vhost settings with multiple domains separated by commas. For example:
      ``'www.example.com, example.com'``

      - *(string) --*

    - **EnableSsl** *(boolean) --*

      Whether to enable SSL for the app.

    - **SslConfiguration** *(dict) --*

      An ``SslConfiguration`` object with the SSL configuration.

      - **Certificate** *(string) --*

        The contents of the certificate's domain.crt file.

      - **PrivateKey** *(string) --*

        The private key; the contents of the certificate's domain.kex file.

      - **Chain** *(string) --*

        Optional. Can be used to specify an intermediate certificate authority key or client
        authentication.

    - **Attributes** *(dict) --*

      The stack attributes.

      - *(string) --*

        - *(string) --*

    - **CreatedAt** *(string) --*

      When the app was created.

    - **Environment** *(list) --*

      An array of ``EnvironmentVariable`` objects that specify environment variables to be
      associated with the app. After you deploy the app, these variables are defined on the
      associated app server instances. For more information, see `Environment Variables
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`__
      .

      .. note::

        There is no specific limit on the number of environment variables. However, the size of
        the associated data structure - which includes the variable names, values, and
        protected flag values - cannot exceed 20 KB. This limit should accommodate most if not
        all use cases, but if you do exceed it, you will cause an exception (API) with an
        "Environment: is too large (maximum is 20 KB)" message.

      - *(dict) --*

        Represents an app's environment variable.

        - **Key** *(string) --*

          (Required) The environment variable's name, which can consist of up to 64 characters
          and must be specified. The name can contain upper- and lowercase letters, numbers,
          and underscores (_), but it must start with a letter or underscore.

        - **Value** *(string) --*

          (Optional) The environment variable's value, which can be left empty. If you specify
          a value, it can contain up to 256 characters, which must all be printable.

        - **Secure** *(boolean) --*

          (Optional) Whether the variable's value will be returned by the  DescribeApps action.
          To conceal an environment variable's value, set ``Secure`` to ``true`` .
          ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The
          default value for ``Secure`` is ``false`` .
    """


_ClientDescribeAppsResponseTypeDef = TypedDict(
    "_ClientDescribeAppsResponseTypeDef",
    {"Apps": List[ClientDescribeAppsResponseAppsTypeDef]},
    total=False,
)


class ClientDescribeAppsResponseTypeDef(_ClientDescribeAppsResponseTypeDef):
    """
    Type definition for `ClientDescribeApps` `Response`

    Contains the response to a ``DescribeApps`` request.

    - **Apps** *(list) --*

      An array of ``App`` objects that describe the specified apps.

      - *(dict) --*

        A description of the app.

        - **AppId** *(string) --*

          The app ID.

        - **StackId** *(string) --*

          The app stack ID.

        - **Shortname** *(string) --*

          The app's short name.

        - **Name** *(string) --*

          The app name.

        - **Description** *(string) --*

          A description of the app.

        - **DataSources** *(list) --*

          The app's data sources.

          - *(dict) --*

            Describes an app's data source.

            - **Type** *(string) --*

              The data source's type, ``AutoSelectOpsworksMysqlInstance`` ,
              ``OpsworksMysqlInstance`` , ``RdsDbInstance`` , or ``None`` .

            - **Arn** *(string) --*

              The data source's ARN.

            - **DatabaseName** *(string) --*

              The database name.

        - **Type** *(string) --*

          The app type.

        - **AppSource** *(dict) --*

          A ``Source`` object that describes the app repository.

          - **Type** *(string) --*

            The repository type.

          - **Url** *(string) --*

            The source URL. The following is an example of an Amazon S3 source URL:
            ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

          - **Username** *(string) --*

            This parameter depends on the repository type.

            * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

            * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
            the user name.

          - **Password** *(string) --*

            When included in a request, the parameter depends on the repository type.

            * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

            * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

            For more information on how to safely handle IAM credentials, see
            `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
            <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
            value.

          - **SshKey** *(string) --*

            In requests, the repository's SSH key.

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
            value.

          - **Revision** *(string) --*

            The application's version. AWS OpsWorks Stacks enables you to easily deploy new
            versions of an application. One of the simplest approaches is to have branches or
            revisions in your repository that represent different versions that can potentially be
            deployed.

        - **Domains** *(list) --*

          The app vhost settings with multiple domains separated by commas. For example:
          ``'www.example.com, example.com'``

          - *(string) --*

        - **EnableSsl** *(boolean) --*

          Whether to enable SSL for the app.

        - **SslConfiguration** *(dict) --*

          An ``SslConfiguration`` object with the SSL configuration.

          - **Certificate** *(string) --*

            The contents of the certificate's domain.crt file.

          - **PrivateKey** *(string) --*

            The private key; the contents of the certificate's domain.kex file.

          - **Chain** *(string) --*

            Optional. Can be used to specify an intermediate certificate authority key or client
            authentication.

        - **Attributes** *(dict) --*

          The stack attributes.

          - *(string) --*

            - *(string) --*

        - **CreatedAt** *(string) --*

          When the app was created.

        - **Environment** *(list) --*

          An array of ``EnvironmentVariable`` objects that specify environment variables to be
          associated with the app. After you deploy the app, these variables are defined on the
          associated app server instances. For more information, see `Environment Variables
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`__
          .

          .. note::

            There is no specific limit on the number of environment variables. However, the size of
            the associated data structure - which includes the variable names, values, and
            protected flag values - cannot exceed 20 KB. This limit should accommodate most if not
            all use cases, but if you do exceed it, you will cause an exception (API) with an
            "Environment: is too large (maximum is 20 KB)" message.

          - *(dict) --*

            Represents an app's environment variable.

            - **Key** *(string) --*

              (Required) The environment variable's name, which can consist of up to 64 characters
              and must be specified. The name can contain upper- and lowercase letters, numbers,
              and underscores (_), but it must start with a letter or underscore.

            - **Value** *(string) --*

              (Optional) The environment variable's value, which can be left empty. If you specify
              a value, it can contain up to 256 characters, which must all be printable.

            - **Secure** *(boolean) --*

              (Optional) Whether the variable's value will be returned by the  DescribeApps action.
              To conceal an environment variable's value, set ``Secure`` to ``true`` .
              ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The
              default value for ``Secure`` is ``false`` .
    """


_ClientDescribeCommandsResponseCommandsTypeDef = TypedDict(
    "_ClientDescribeCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)


class ClientDescribeCommandsResponseCommandsTypeDef(
    _ClientDescribeCommandsResponseCommandsTypeDef
):
    """
    Type definition for `ClientDescribeCommandsResponse` `Commands`

    Describes a command.

    - **CommandId** *(string) --*

      The command ID.

    - **InstanceId** *(string) --*

      The ID of the instance where the command was executed.

    - **DeploymentId** *(string) --*

      The command deployment ID.

    - **CreatedAt** *(string) --*

      Date and time when the command was run.

    - **AcknowledgedAt** *(string) --*

      Date and time when the command was acknowledged.

    - **CompletedAt** *(string) --*

      Date when the command completed.

    - **Status** *(string) --*

      The command status:

      * failed

      * successful

      * skipped

      * pending

    - **ExitCode** *(integer) --*

      The command exit code.

    - **LogUrl** *(string) --*

      The URL of the command log.

    - **Type** *(string) --*

      The command type:

      * ``configure``

      * ``deploy``

      * ``execute_recipes``

      * ``install_dependencies``

      * ``restart``

      * ``rollback``

      * ``setup``

      * ``start``

      * ``stop``

      * ``undeploy``

      * ``update_custom_cookbooks``

      * ``update_dependencies``
    """


_ClientDescribeCommandsResponseTypeDef = TypedDict(
    "_ClientDescribeCommandsResponseTypeDef",
    {"Commands": List[ClientDescribeCommandsResponseCommandsTypeDef]},
    total=False,
)


class ClientDescribeCommandsResponseTypeDef(_ClientDescribeCommandsResponseTypeDef):
    """
    Type definition for `ClientDescribeCommands` `Response`

    Contains the response to a ``DescribeCommands`` request.

    - **Commands** *(list) --*

      An array of ``Command`` objects that describe each of the specified commands.

      - *(dict) --*

        Describes a command.

        - **CommandId** *(string) --*

          The command ID.

        - **InstanceId** *(string) --*

          The ID of the instance where the command was executed.

        - **DeploymentId** *(string) --*

          The command deployment ID.

        - **CreatedAt** *(string) --*

          Date and time when the command was run.

        - **AcknowledgedAt** *(string) --*

          Date and time when the command was acknowledged.

        - **CompletedAt** *(string) --*

          Date when the command completed.

        - **Status** *(string) --*

          The command status:

          * failed

          * successful

          * skipped

          * pending

        - **ExitCode** *(integer) --*

          The command exit code.

        - **LogUrl** *(string) --*

          The URL of the command log.

        - **Type** *(string) --*

          The command type:

          * ``configure``

          * ``deploy``

          * ``execute_recipes``

          * ``install_dependencies``

          * ``restart``

          * ``rollback``

          * ``setup``

          * ``start``

          * ``stop``

          * ``undeploy``

          * ``update_custom_cookbooks``

          * ``update_dependencies``
    """


_ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    {"Name": str, "Args": Dict[str, List[str]]},
    total=False,
)


class ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef(
    _ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentsResponseDeployments` `Command`

    Used to specify a stack or deployment command.

    - **Name** *(string) --*

      Specifies the operation. You can specify only one command.

      For stacks, the following commands are available:

      * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an
      ``Args`` parameter named ``recipes`` to the list of recipes to be executed. For
      example, to execute ``phpapp::appsetup`` , set ``Args`` to
      ``{"recipes":["phpapp::appsetup"]}`` .

      * ``install_dependencies`` : Install the stack's dependencies.

      * ``update_custom_cookbooks`` : Update the stack's custom cookbooks.

      * ``update_dependencies`` : Update the stack's dependencies.

      .. note::

        The update_dependencies and install_dependencies commands are supported only for
        Linux instances. You can run the commands successfully on Windows instances, but they
        do nothing.

      For apps, the following commands are available:

      * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter
      named ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The
      default setting is {"migrate":["false"]}.

      * ``rollback`` Roll the app back to the previous version. When you update an app, AWS
      OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can
      use this command to roll an app back as many as four versions.

      * ``start`` : Start the app's web or application server.

      * ``stop`` : Stop the app's web or application server.

      * ``restart`` : Restart the app's web or application server.

      * ``undeploy`` : Undeploy the app.

    - **Args** *(dict) --*

      The arguments of those commands that take arguments. It should be set to a JSON object
      with the following format:

       ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...],
       ...}``

      The ``update_dependencies`` command takes two arguments:

      * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS
      you want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the
      ``allow_reboot`` argument to true.

      * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the
      instances if necessary, after installing the updates. This argument can be set to
      either ``true`` or ``false`` . The default value is ``false`` .

      For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the
      following.

       ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``

      - *(string) --*

        - *(list) --*

          - *(string) --*
    """


_ClientDescribeDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    {
        "DeploymentId": str,
        "StackId": str,
        "AppId": str,
        "CreatedAt": str,
        "CompletedAt": str,
        "Duration": int,
        "IamUserArn": str,
        "Comment": str,
        "Command": ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef,
        "Status": str,
        "CustomJson": str,
        "InstanceIds": List[str],
    },
    total=False,
)


class ClientDescribeDeploymentsResponseDeploymentsTypeDef(
    _ClientDescribeDeploymentsResponseDeploymentsTypeDef
):
    """
    Type definition for `ClientDescribeDeploymentsResponse` `Deployments`

    Describes a deployment of a stack or app.

    - **DeploymentId** *(string) --*

      The deployment ID.

    - **StackId** *(string) --*

      The stack ID.

    - **AppId** *(string) --*

      The app ID.

    - **CreatedAt** *(string) --*

      Date when the deployment was created.

    - **CompletedAt** *(string) --*

      Date when the deployment completed.

    - **Duration** *(integer) --*

      The deployment duration.

    - **IamUserArn** *(string) --*

      The user's IAM ARN.

    - **Comment** *(string) --*

      A user-defined comment.

    - **Command** *(dict) --*

      Used to specify a stack or deployment command.

      - **Name** *(string) --*

        Specifies the operation. You can specify only one command.

        For stacks, the following commands are available:

        * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an
        ``Args`` parameter named ``recipes`` to the list of recipes to be executed. For
        example, to execute ``phpapp::appsetup`` , set ``Args`` to
        ``{"recipes":["phpapp::appsetup"]}`` .

        * ``install_dependencies`` : Install the stack's dependencies.

        * ``update_custom_cookbooks`` : Update the stack's custom cookbooks.

        * ``update_dependencies`` : Update the stack's dependencies.

        .. note::

          The update_dependencies and install_dependencies commands are supported only for
          Linux instances. You can run the commands successfully on Windows instances, but they
          do nothing.

        For apps, the following commands are available:

        * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter
        named ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The
        default setting is {"migrate":["false"]}.

        * ``rollback`` Roll the app back to the previous version. When you update an app, AWS
        OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can
        use this command to roll an app back as many as four versions.

        * ``start`` : Start the app's web or application server.

        * ``stop`` : Stop the app's web or application server.

        * ``restart`` : Restart the app's web or application server.

        * ``undeploy`` : Undeploy the app.

      - **Args** *(dict) --*

        The arguments of those commands that take arguments. It should be set to a JSON object
        with the following format:

         ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...],
         ...}``

        The ``update_dependencies`` command takes two arguments:

        * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS
        you want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the
        ``allow_reboot`` argument to true.

        * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the
        instances if necessary, after installing the updates. This argument can be set to
        either ``true`` or ``false`` . The default value is ``false`` .

        For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the
        following.

         ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``

        - *(string) --*

          - *(list) --*

            - *(string) --*

    - **Status** *(string) --*

      The deployment status:

      * running

      * successful

      * failed

    - **CustomJson** *(string) --*

      A string that contains user-defined custom JSON. It can be used to override the
      corresponding default stack configuration attribute values for stack or to pass data to
      recipes. The string should be in the following format:

       ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"``

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack
      Configuration Attributes
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

    - **InstanceIds** *(list) --*

      The IDs of the target instances.

      - *(string) --*
    """


_ClientDescribeDeploymentsResponseTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseTypeDef",
    {"Deployments": List[ClientDescribeDeploymentsResponseDeploymentsTypeDef]},
    total=False,
)


class ClientDescribeDeploymentsResponseTypeDef(
    _ClientDescribeDeploymentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDeployments` `Response`

    Contains the response to a ``DescribeDeployments`` request.

    - **Deployments** *(list) --*

      An array of ``Deployment`` objects that describe the deployments.

      - *(dict) --*

        Describes a deployment of a stack or app.

        - **DeploymentId** *(string) --*

          The deployment ID.

        - **StackId** *(string) --*

          The stack ID.

        - **AppId** *(string) --*

          The app ID.

        - **CreatedAt** *(string) --*

          Date when the deployment was created.

        - **CompletedAt** *(string) --*

          Date when the deployment completed.

        - **Duration** *(integer) --*

          The deployment duration.

        - **IamUserArn** *(string) --*

          The user's IAM ARN.

        - **Comment** *(string) --*

          A user-defined comment.

        - **Command** *(dict) --*

          Used to specify a stack or deployment command.

          - **Name** *(string) --*

            Specifies the operation. You can specify only one command.

            For stacks, the following commands are available:

            * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an
            ``Args`` parameter named ``recipes`` to the list of recipes to be executed. For
            example, to execute ``phpapp::appsetup`` , set ``Args`` to
            ``{"recipes":["phpapp::appsetup"]}`` .

            * ``install_dependencies`` : Install the stack's dependencies.

            * ``update_custom_cookbooks`` : Update the stack's custom cookbooks.

            * ``update_dependencies`` : Update the stack's dependencies.

            .. note::

              The update_dependencies and install_dependencies commands are supported only for
              Linux instances. You can run the commands successfully on Windows instances, but they
              do nothing.

            For apps, the following commands are available:

            * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter
            named ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The
            default setting is {"migrate":["false"]}.

            * ``rollback`` Roll the app back to the previous version. When you update an app, AWS
            OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can
            use this command to roll an app back as many as four versions.

            * ``start`` : Start the app's web or application server.

            * ``stop`` : Stop the app's web or application server.

            * ``restart`` : Restart the app's web or application server.

            * ``undeploy`` : Undeploy the app.

          - **Args** *(dict) --*

            The arguments of those commands that take arguments. It should be set to a JSON object
            with the following format:

             ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...],
             ...}``

            The ``update_dependencies`` command takes two arguments:

            * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS
            you want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the
            ``allow_reboot`` argument to true.

            * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the
            instances if necessary, after installing the updates. This argument can be set to
            either ``true`` or ``false`` . The default value is ``false`` .

            For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the
            following.

             ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``

            - *(string) --*

              - *(list) --*

                - *(string) --*

        - **Status** *(string) --*

          The deployment status:

          * running

          * successful

          * failed

        - **CustomJson** *(string) --*

          A string that contains user-defined custom JSON. It can be used to override the
          corresponding default stack configuration attribute values for stack or to pass data to
          recipes. The string should be in the following format:

           ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"``

          For more information on custom JSON, see `Use Custom JSON to Modify the Stack
          Configuration Attributes
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

        - **InstanceIds** *(list) --*

          The IDs of the target instances.

          - *(string) --*
    """


_ClientDescribeEcsClustersResponseEcsClustersTypeDef = TypedDict(
    "_ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)


class ClientDescribeEcsClustersResponseEcsClustersTypeDef(
    _ClientDescribeEcsClustersResponseEcsClustersTypeDef
):
    """
    Type definition for `ClientDescribeEcsClustersResponse` `EcsClusters`

    Describes a registered Amazon ECS cluster.

    - **EcsClusterArn** *(string) --*

      The cluster's ARN.

    - **EcsClusterName** *(string) --*

      The cluster name.

    - **StackId** *(string) --*

      The stack ID.

    - **RegisteredAt** *(string) --*

      The time and date that the cluster was registered with the stack.
    """


_ClientDescribeEcsClustersResponseTypeDef = TypedDict(
    "_ClientDescribeEcsClustersResponseTypeDef",
    {
        "EcsClusters": List[ClientDescribeEcsClustersResponseEcsClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEcsClustersResponseTypeDef(
    _ClientDescribeEcsClustersResponseTypeDef
):
    """
    Type definition for `ClientDescribeEcsClusters` `Response`

    Contains the response to a ``DescribeEcsClusters`` request.

    - **EcsClusters** *(list) --*

      A list of ``EcsCluster`` objects containing the cluster descriptions.

      - *(dict) --*

        Describes a registered Amazon ECS cluster.

        - **EcsClusterArn** *(string) --*

          The cluster's ARN.

        - **EcsClusterName** *(string) --*

          The cluster name.

        - **StackId** *(string) --*

          The stack ID.

        - **RegisteredAt** *(string) --*

          The time and date that the cluster was registered with the stack.

    - **NextToken** *(string) --*

      If a paginated request does not return all of the remaining results, this parameter is set to
      a token that you can assign to the request object's ``NextToken`` parameter to retrieve the
      next set of results. If the previous paginated request returned all of the remaining results,
      this parameter is set to ``null`` .
    """


_ClientDescribeElasticIpsResponseElasticIpsTypeDef = TypedDict(
    "_ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    {"Ip": str, "Name": str, "Domain": str, "Region": str, "InstanceId": str},
    total=False,
)


class ClientDescribeElasticIpsResponseElasticIpsTypeDef(
    _ClientDescribeElasticIpsResponseElasticIpsTypeDef
):
    """
    Type definition for `ClientDescribeElasticIpsResponse` `ElasticIps`

    Describes an Elastic IP address.

    - **Ip** *(string) --*

      The IP address.

    - **Name** *(string) --*

      The name.

    - **Domain** *(string) --*

      The domain.

    - **Region** *(string) --*

      The AWS region. For more information, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **InstanceId** *(string) --*

      The ID of the instance that the address is attached to.
    """


_ClientDescribeElasticIpsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticIpsResponseTypeDef",
    {"ElasticIps": List[ClientDescribeElasticIpsResponseElasticIpsTypeDef]},
    total=False,
)


class ClientDescribeElasticIpsResponseTypeDef(_ClientDescribeElasticIpsResponseTypeDef):
    """
    Type definition for `ClientDescribeElasticIps` `Response`

    Contains the response to a ``DescribeElasticIps`` request.

    - **ElasticIps** *(list) --*

      An ``ElasticIps`` object that describes the specified Elastic IP addresses.

      - *(dict) --*

        Describes an Elastic IP address.

        - **Ip** *(string) --*

          The IP address.

        - **Name** *(string) --*

          The name.

        - **Domain** *(string) --*

          The domain.

        - **Region** *(string) --*

          The AWS region. For more information, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **InstanceId** *(string) --*

          The ID of the instance that the address is attached to.
    """


_ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "Region": str,
        "DnsName": str,
        "StackId": str,
        "LayerId": str,
        "VpcId": str,
        "AvailabilityZones": List[str],
        "SubnetIds": List[str],
        "Ec2InstanceIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef(
    _ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef
):
    """
    Type definition for `ClientDescribeElasticLoadBalancersResponse` `ElasticLoadBalancers`

    Describes an Elastic Load Balancing instance.

    - **ElasticLoadBalancerName** *(string) --*

      The Elastic Load Balancing instance's name.

    - **Region** *(string) --*

      The instance's AWS region.

    - **DnsName** *(string) --*

      The instance's public DNS name.

    - **StackId** *(string) --*

      The ID of the stack that the instance is associated with.

    - **LayerId** *(string) --*

      The ID of the layer that the instance is attached to.

    - **VpcId** *(string) --*

      The VPC ID.

    - **AvailabilityZones** *(list) --*

      A list of Availability Zones.

      - *(string) --*

    - **SubnetIds** *(list) --*

      A list of subnet IDs, if the stack is running in a VPC.

      - *(string) --*

    - **Ec2InstanceIds** *(list) --*

      A list of the EC2 instances that the Elastic Load Balancing instance is managing traffic
      for.

      - *(string) --*
    """


_ClientDescribeElasticLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeElasticLoadBalancersResponseTypeDef",
    {
        "ElasticLoadBalancers": List[
            ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeElasticLoadBalancersResponseTypeDef(
    _ClientDescribeElasticLoadBalancersResponseTypeDef
):
    """
    Type definition for `ClientDescribeElasticLoadBalancers` `Response`

    Contains the response to a ``DescribeElasticLoadBalancers`` request.

    - **ElasticLoadBalancers** *(list) --*

      A list of ``ElasticLoadBalancer`` objects that describe the specified Elastic Load Balancing
      instances.

      - *(dict) --*

        Describes an Elastic Load Balancing instance.

        - **ElasticLoadBalancerName** *(string) --*

          The Elastic Load Balancing instance's name.

        - **Region** *(string) --*

          The instance's AWS region.

        - **DnsName** *(string) --*

          The instance's public DNS name.

        - **StackId** *(string) --*

          The ID of the stack that the instance is associated with.

        - **LayerId** *(string) --*

          The ID of the layer that the instance is attached to.

        - **VpcId** *(string) --*

          The VPC ID.

        - **AvailabilityZones** *(list) --*

          A list of Availability Zones.

          - *(string) --*

        - **SubnetIds** *(list) --*

          A list of subnet IDs, if the stack is running in a VPC.

          - *(string) --*

        - **Ec2InstanceIds** *(list) --*

          A list of the EC2 instances that the Elastic Load Balancing instance is managing traffic
          for.

          - *(string) --*
    """


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef
):
    """
    Type definition for `ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurations` `DownScaling`

    An ``AutoScalingThresholds`` object that describes the downscaling configuration, which
    defines how and when AWS OpsWorks Stacks reduces the number of instances.

    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.

    - **ThresholdsWaitTime** *(integer) --*

      The amount of time, in minutes, that the load must exceed a threshold before more
      instances are added or removed.

    - **IgnoreMetricsTime** *(integer) --*

      The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
      should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
      Stacks adds new instances following an upscaling event but the instances won't start
      reducing the load until they have been booted and configured. There is no point in
      raising additional scaling events during that operation, which typically takes several
      minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
      scaling events long enough to get the new instances online.

    - **CpuThreshold** *(float) --*

      The CPU utilization threshold, as a percent of the available CPU. A value of -1
      disables the threshold.

    - **MemoryThreshold** *(float) --*

      The memory utilization threshold, as a percent of the available memory. A value of -1
      disables the threshold.

    - **LoadThreshold** *(float) --*

      The load threshold. A value of -1 disables the threshold. For more information about
      how load is computed, see `Load (computing)
      <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

    - **Alarms** *(list) --*

      Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
      list of up to five alarm names, which are case sensitive and must be in the same region
      as the stack.

      .. note::

        To use custom alarms, you must update your service role to allow
        ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
        role for you when you first use this feature or you can edit the role manually. For
        more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
        <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
        .

      - *(string) --*
    """


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef
):
    """
    Type definition for `ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurations` `UpScaling`

    An ``AutoScalingThresholds`` object that describes the upscaling configuration, which
    defines how and when AWS OpsWorks Stacks increases the number of instances.

    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.

    - **ThresholdsWaitTime** *(integer) --*

      The amount of time, in minutes, that the load must exceed a threshold before more
      instances are added or removed.

    - **IgnoreMetricsTime** *(integer) --*

      The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
      should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
      Stacks adds new instances following an upscaling event but the instances won't start
      reducing the load until they have been booted and configured. There is no point in
      raising additional scaling events during that operation, which typically takes several
      minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
      scaling events long enough to get the new instances online.

    - **CpuThreshold** *(float) --*

      The CPU utilization threshold, as a percent of the available CPU. A value of -1
      disables the threshold.

    - **MemoryThreshold** *(float) --*

      The memory utilization threshold, as a percent of the available memory. A value of -1
      disables the threshold.

    - **LoadThreshold** *(float) --*

      The load threshold. A value of -1 disables the threshold. For more information about
      how load is computed, see `Load (computing)
      <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

    - **Alarms** *(list) --*

      Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
      list of up to five alarm names, which are case sensitive and must be in the same region
      as the stack.

      .. note::

        To use custom alarms, you must update your service role to allow
        ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
        role for you when you first use this feature or you can edit the role manually. For
        more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
        <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
        .

      - *(string) --*
    """


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    {
        "LayerId": str,
        "Enable": bool,
        "UpScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef,
        "DownScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef,
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBasedAutoScalingResponse` `LoadBasedAutoScalingConfigurations`

    Describes a layer's load-based auto scaling configuration.

    - **LayerId** *(string) --*

      The layer ID.

    - **Enable** *(boolean) --*

      Whether load-based auto scaling is enabled for the layer.

    - **UpScaling** *(dict) --*

      An ``AutoScalingThresholds`` object that describes the upscaling configuration, which
      defines how and when AWS OpsWorks Stacks increases the number of instances.

      - **InstanceCount** *(integer) --*

        The number of instances to add or remove when the load exceeds a threshold.

      - **ThresholdsWaitTime** *(integer) --*

        The amount of time, in minutes, that the load must exceed a threshold before more
        instances are added or removed.

      - **IgnoreMetricsTime** *(integer) --*

        The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
        should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
        Stacks adds new instances following an upscaling event but the instances won't start
        reducing the load until they have been booted and configured. There is no point in
        raising additional scaling events during that operation, which typically takes several
        minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
        scaling events long enough to get the new instances online.

      - **CpuThreshold** *(float) --*

        The CPU utilization threshold, as a percent of the available CPU. A value of -1
        disables the threshold.

      - **MemoryThreshold** *(float) --*

        The memory utilization threshold, as a percent of the available memory. A value of -1
        disables the threshold.

      - **LoadThreshold** *(float) --*

        The load threshold. A value of -1 disables the threshold. For more information about
        how load is computed, see `Load (computing)
        <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

      - **Alarms** *(list) --*

        Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
        list of up to five alarm names, which are case sensitive and must be in the same region
        as the stack.

        .. note::

          To use custom alarms, you must update your service role to allow
          ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
          role for you when you first use this feature or you can edit the role manually. For
          more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
          <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
          .

        - *(string) --*

    - **DownScaling** *(dict) --*

      An ``AutoScalingThresholds`` object that describes the downscaling configuration, which
      defines how and when AWS OpsWorks Stacks reduces the number of instances.

      - **InstanceCount** *(integer) --*

        The number of instances to add or remove when the load exceeds a threshold.

      - **ThresholdsWaitTime** *(integer) --*

        The amount of time, in minutes, that the load must exceed a threshold before more
        instances are added or removed.

      - **IgnoreMetricsTime** *(integer) --*

        The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
        should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
        Stacks adds new instances following an upscaling event but the instances won't start
        reducing the load until they have been booted and configured. There is no point in
        raising additional scaling events during that operation, which typically takes several
        minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
        scaling events long enough to get the new instances online.

      - **CpuThreshold** *(float) --*

        The CPU utilization threshold, as a percent of the available CPU. A value of -1
        disables the threshold.

      - **MemoryThreshold** *(float) --*

        The memory utilization threshold, as a percent of the available memory. A value of -1
        disables the threshold.

      - **LoadThreshold** *(float) --*

        The load threshold. A value of -1 disables the threshold. For more information about
        how load is computed, see `Load (computing)
        <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

      - **Alarms** *(list) --*

        Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
        list of up to five alarm names, which are case sensitive and must be in the same region
        as the stack.

        .. note::

          To use custom alarms, you must update your service role to allow
          ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
          role for you when you first use this feature or you can edit the role manually. For
          more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
          <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
          .

        - *(string) --*
    """


_ClientDescribeLoadBasedAutoScalingResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List[
            ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBasedAutoScaling` `Response`

    Contains the response to a ``DescribeLoadBasedAutoScaling`` request.

    - **LoadBasedAutoScalingConfigurations** *(list) --*

      An array of ``LoadBasedAutoScalingConfiguration`` objects that describe each layer's
      configuration.

      - *(dict) --*

        Describes a layer's load-based auto scaling configuration.

        - **LayerId** *(string) --*

          The layer ID.

        - **Enable** *(boolean) --*

          Whether load-based auto scaling is enabled for the layer.

        - **UpScaling** *(dict) --*

          An ``AutoScalingThresholds`` object that describes the upscaling configuration, which
          defines how and when AWS OpsWorks Stacks increases the number of instances.

          - **InstanceCount** *(integer) --*

            The number of instances to add or remove when the load exceeds a threshold.

          - **ThresholdsWaitTime** *(integer) --*

            The amount of time, in minutes, that the load must exceed a threshold before more
            instances are added or removed.

          - **IgnoreMetricsTime** *(integer) --*

            The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
            should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
            Stacks adds new instances following an upscaling event but the instances won't start
            reducing the load until they have been booted and configured. There is no point in
            raising additional scaling events during that operation, which typically takes several
            minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
            scaling events long enough to get the new instances online.

          - **CpuThreshold** *(float) --*

            The CPU utilization threshold, as a percent of the available CPU. A value of -1
            disables the threshold.

          - **MemoryThreshold** *(float) --*

            The memory utilization threshold, as a percent of the available memory. A value of -1
            disables the threshold.

          - **LoadThreshold** *(float) --*

            The load threshold. A value of -1 disables the threshold. For more information about
            how load is computed, see `Load (computing)
            <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

          - **Alarms** *(list) --*

            Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
            list of up to five alarm names, which are case sensitive and must be in the same region
            as the stack.

            .. note::

              To use custom alarms, you must update your service role to allow
              ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
              role for you when you first use this feature or you can edit the role manually. For
              more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
              <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
              .

            - *(string) --*

        - **DownScaling** *(dict) --*

          An ``AutoScalingThresholds`` object that describes the downscaling configuration, which
          defines how and when AWS OpsWorks Stacks reduces the number of instances.

          - **InstanceCount** *(integer) --*

            The number of instances to add or remove when the load exceeds a threshold.

          - **ThresholdsWaitTime** *(integer) --*

            The amount of time, in minutes, that the load must exceed a threshold before more
            instances are added or removed.

          - **IgnoreMetricsTime** *(integer) --*

            The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks
            should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks
            Stacks adds new instances following an upscaling event but the instances won't start
            reducing the load until they have been booted and configured. There is no point in
            raising additional scaling events during that operation, which typically takes several
            minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress
            scaling events long enough to get the new instances online.

          - **CpuThreshold** *(float) --*

            The CPU utilization threshold, as a percent of the available CPU. A value of -1
            disables the threshold.

          - **MemoryThreshold** *(float) --*

            The memory utilization threshold, as a percent of the available memory. A value of -1
            disables the threshold.

          - **LoadThreshold** *(float) --*

            The load threshold. A value of -1 disables the threshold. For more information about
            how load is computed, see `Load (computing)
            <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

          - **Alarms** *(list) --*

            Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a
            list of up to five alarm names, which are case sensitive and must be in the same region
            as the stack.

            .. note::

              To use custom alarms, you must update your service role to allow
              ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the
              role for you when you first use this feature or you can edit the role manually. For
              more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
              <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
              .

            - *(string) --*
    """


_ClientDescribeMyUserProfileResponseUserProfileTypeDef = TypedDict(
    "_ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    {"IamUserArn": str, "Name": str, "SshUsername": str, "SshPublicKey": str},
    total=False,
)


class ClientDescribeMyUserProfileResponseUserProfileTypeDef(
    _ClientDescribeMyUserProfileResponseUserProfileTypeDef
):
    """
    Type definition for `ClientDescribeMyUserProfileResponse` `UserProfile`

    A ``UserProfile`` object that describes the user's SSH information.

    - **IamUserArn** *(string) --*

      The user's IAM ARN.

    - **Name** *(string) --*

      The user's name.

    - **SshUsername** *(string) --*

      The user's SSH user name.

    - **SshPublicKey** *(string) --*

      The user's SSH public key.
    """


_ClientDescribeMyUserProfileResponseTypeDef = TypedDict(
    "_ClientDescribeMyUserProfileResponseTypeDef",
    {"UserProfile": ClientDescribeMyUserProfileResponseUserProfileTypeDef},
    total=False,
)


class ClientDescribeMyUserProfileResponseTypeDef(
    _ClientDescribeMyUserProfileResponseTypeDef
):
    """
    Type definition for `ClientDescribeMyUserProfile` `Response`

    Contains the response to a ``DescribeMyUserProfile`` request.

    - **UserProfile** *(dict) --*

      A ``UserProfile`` object that describes the user's SSH information.

      - **IamUserArn** *(string) --*

        The user's IAM ARN.

      - **Name** *(string) --*

        The user's name.

      - **SshUsername** *(string) --*

        The user's SSH user name.

      - **SshPublicKey** *(string) --*

        The user's SSH public key.
    """


_ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef(
    _ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef
):
    """
    Type definition for `ClientDescribeOperatingSystemsResponseOperatingSystems` `ConfigurationManagers`

    A block that contains information about the configuration manager (Chef) and the
    versions of the configuration manager that are supported for an operating system.

    - **Name** *(string) --*

      The name of the configuration manager, which is Chef.

    - **Version** *(string) --*

      The versions of the configuration manager that are supported by an operating system.
    """


_ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List[
            ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef
        ],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
    },
    total=False,
)


class ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef(
    _ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef
):
    """
    Type definition for `ClientDescribeOperatingSystemsResponse` `OperatingSystems`

    Describes supported operating systems in AWS OpsWorks Stacks.

    - **Name** *(string) --*

      The name of the operating system, such as ``Amazon Linux 2018.03`` .

    - **Id** *(string) --*

      The ID of a supported operating system, such as ``Amazon Linux 2018.03`` .

    - **Type** *(string) --*

      The type of a supported operating system, either ``Linux`` or ``Windows`` .

    - **ConfigurationManagers** *(list) --*

      Supported configuration manager name and versions for an AWS OpsWorks Stacks operating
      system.

      - *(dict) --*

        A block that contains information about the configuration manager (Chef) and the
        versions of the configuration manager that are supported for an operating system.

        - **Name** *(string) --*

          The name of the configuration manager, which is Chef.

        - **Version** *(string) --*

          The versions of the configuration manager that are supported by an operating system.

    - **ReportedName** *(string) --*

      A short name for the operating system manufacturer.

    - **ReportedVersion** *(string) --*

      The version of the operating system, including the release and edition, if applicable.

    - **Supported** *(boolean) --*

      Indicates that an operating system is not supported for new instances.
    """


_ClientDescribeOperatingSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseTypeDef",
    {
        "OperatingSystems": List[
            ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeOperatingSystemsResponseTypeDef(
    _ClientDescribeOperatingSystemsResponseTypeDef
):
    """
    Type definition for `ClientDescribeOperatingSystems` `Response`

    The response to a ``DescribeOperatingSystems`` request.

    - **OperatingSystems** *(list) --*

      Contains information in response to a ``DescribeOperatingSystems`` request.

      - *(dict) --*

        Describes supported operating systems in AWS OpsWorks Stacks.

        - **Name** *(string) --*

          The name of the operating system, such as ``Amazon Linux 2018.03`` .

        - **Id** *(string) --*

          The ID of a supported operating system, such as ``Amazon Linux 2018.03`` .

        - **Type** *(string) --*

          The type of a supported operating system, either ``Linux`` or ``Windows`` .

        - **ConfigurationManagers** *(list) --*

          Supported configuration manager name and versions for an AWS OpsWorks Stacks operating
          system.

          - *(dict) --*

            A block that contains information about the configuration manager (Chef) and the
            versions of the configuration manager that are supported for an operating system.

            - **Name** *(string) --*

              The name of the configuration manager, which is Chef.

            - **Version** *(string) --*

              The versions of the configuration manager that are supported by an operating system.

        - **ReportedName** *(string) --*

          A short name for the operating system manufacturer.

        - **ReportedVersion** *(string) --*

          The version of the operating system, including the release and edition, if applicable.

        - **Supported** *(boolean) --*

          Indicates that an operating system is not supported for new instances.
    """


_ClientDescribePermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribePermissionsResponsePermissionsTypeDef",
    {
        "StackId": str,
        "IamUserArn": str,
        "AllowSsh": bool,
        "AllowSudo": bool,
        "Level": str,
    },
    total=False,
)


class ClientDescribePermissionsResponsePermissionsTypeDef(
    _ClientDescribePermissionsResponsePermissionsTypeDef
):
    """
    Type definition for `ClientDescribePermissionsResponse` `Permissions`

    Describes stack or user permissions.

    - **StackId** *(string) --*

      A stack ID.

    - **IamUserArn** *(string) --*

      The Amazon Resource Name (ARN) for an AWS Identity and Access Management (IAM) role. For
      more information about IAM ARNs, see `Using Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

    - **AllowSsh** *(boolean) --*

      Whether the user can use SSH.

    - **AllowSudo** *(boolean) --*

      Whether the user can use **sudo** .

    - **Level** *(string) --*

      The user's permission level, which must be the following:

      * ``deny``

      * ``show``

      * ``deploy``

      * ``manage``

      * ``iam_only``

      For more information on the permissions associated with these levels, see `Managing User
      Permissions
      <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__
    """


_ClientDescribePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribePermissionsResponseTypeDef",
    {"Permissions": List[ClientDescribePermissionsResponsePermissionsTypeDef]},
    total=False,
)


class ClientDescribePermissionsResponseTypeDef(
    _ClientDescribePermissionsResponseTypeDef
):
    """
    Type definition for `ClientDescribePermissions` `Response`

    Contains the response to a ``DescribePermissions`` request.

    - **Permissions** *(list) --*

      An array of ``Permission`` objects that describe the stack permissions.

      * If the request object contains only a stack ID, the array contains a ``Permission`` object
      with permissions for each of the stack IAM ARNs.

      * If the request object contains only an IAM ARN, the array contains a ``Permission`` object
      with permissions for each of the user's stack IDs.

      * If the request contains a stack ID and an IAM ARN, the array contains a single
      ``Permission`` object with permissions for the specified stack and IAM ARN.

      - *(dict) --*

        Describes stack or user permissions.

        - **StackId** *(string) --*

          A stack ID.

        - **IamUserArn** *(string) --*

          The Amazon Resource Name (ARN) for an AWS Identity and Access Management (IAM) role. For
          more information about IAM ARNs, see `Using Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

        - **AllowSsh** *(boolean) --*

          Whether the user can use SSH.

        - **AllowSudo** *(boolean) --*

          Whether the user can use **sudo** .

        - **Level** *(string) --*

          The user's permission level, which must be the following:

          * ``deny``

          * ``show``

          * ``deploy``

          * ``manage``

          * ``iam_only``

          For more information on the permissions associated with these levels, see `Managing User
          Permissions
          <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__
    """


_ClientDescribeRaidArraysResponseRaidArraysTypeDef = TypedDict(
    "_ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    {
        "RaidArrayId": str,
        "InstanceId": str,
        "Name": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "AvailabilityZone": str,
        "CreatedAt": str,
        "StackId": str,
        "VolumeType": str,
        "Iops": int,
    },
    total=False,
)


class ClientDescribeRaidArraysResponseRaidArraysTypeDef(
    _ClientDescribeRaidArraysResponseRaidArraysTypeDef
):
    """
    Type definition for `ClientDescribeRaidArraysResponse` `RaidArrays`

    Describes an instance's RAID array.

    - **RaidArrayId** *(string) --*

      The array ID.

    - **InstanceId** *(string) --*

      The instance ID.

    - **Name** *(string) --*

      The array name.

    - **RaidLevel** *(integer) --*

      The `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

    - **NumberOfDisks** *(integer) --*

      The number of disks in the array.

    - **Size** *(integer) --*

      The array's size.

    - **Device** *(string) --*

      The array's Linux device. For example /dev/mdadm0.

    - **MountPoint** *(string) --*

      The array's mount point.

    - **AvailabilityZone** *(string) --*

      The array's Availability Zone. For more information, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **CreatedAt** *(string) --*

      When the RAID array was created.

    - **StackId** *(string) --*

      The stack ID.

    - **VolumeType** *(string) --*

      The volume type, standard or PIOPS.

    - **Iops** *(integer) --*

      For PIOPS volumes, the IOPS per disk.
    """


_ClientDescribeRaidArraysResponseTypeDef = TypedDict(
    "_ClientDescribeRaidArraysResponseTypeDef",
    {"RaidArrays": List[ClientDescribeRaidArraysResponseRaidArraysTypeDef]},
    total=False,
)


class ClientDescribeRaidArraysResponseTypeDef(_ClientDescribeRaidArraysResponseTypeDef):
    """
    Type definition for `ClientDescribeRaidArrays` `Response`

    Contains the response to a ``DescribeRaidArrays`` request.

    - **RaidArrays** *(list) --*

      A ``RaidArrays`` object that describes the specified RAID arrays.

      - *(dict) --*

        Describes an instance's RAID array.

        - **RaidArrayId** *(string) --*

          The array ID.

        - **InstanceId** *(string) --*

          The instance ID.

        - **Name** *(string) --*

          The array name.

        - **RaidLevel** *(integer) --*

          The `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

        - **NumberOfDisks** *(integer) --*

          The number of disks in the array.

        - **Size** *(integer) --*

          The array's size.

        - **Device** *(string) --*

          The array's Linux device. For example /dev/mdadm0.

        - **MountPoint** *(string) --*

          The array's mount point.

        - **AvailabilityZone** *(string) --*

          The array's Availability Zone. For more information, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **CreatedAt** *(string) --*

          When the RAID array was created.

        - **StackId** *(string) --*

          The stack ID.

        - **VolumeType** *(string) --*

          The volume type, standard or PIOPS.

        - **Iops** *(integer) --*

          For PIOPS volumes, the IOPS per disk.
    """


_ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef = TypedDict(
    "_ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbInstanceIdentifier": str,
        "DbUser": str,
        "DbPassword": str,
        "Region": str,
        "Address": str,
        "Engine": str,
        "StackId": str,
        "MissingOnRds": bool,
    },
    total=False,
)


class ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef(
    _ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef
):
    """
    Type definition for `ClientDescribeRdsDbInstancesResponse` `RdsDbInstances`

    Describes an Amazon RDS instance.

    - **RdsDbInstanceArn** *(string) --*

      The instance's ARN.

    - **DbInstanceIdentifier** *(string) --*

      The DB instance identifier.

    - **DbUser** *(string) --*

      The master user name.

    - **DbPassword** *(string) --*

      AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Region** *(string) --*

      The instance's AWS region.

    - **Address** *(string) --*

      The instance's address.

    - **Engine** *(string) --*

      The instance's database engine.

    - **StackId** *(string) --*

      The ID of the stack with which the instance is registered.

    - **MissingOnRds** *(boolean) --*

      Set to ``true`` if AWS OpsWorks Stacks is unable to discover the Amazon RDS instance. AWS
      OpsWorks Stacks attempts to discover the instance only once. If this value is set to
      ``true`` , you must deregister the instance, and then register it again.
    """


_ClientDescribeRdsDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeRdsDbInstancesResponseTypeDef",
    {"RdsDbInstances": List[ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef]},
    total=False,
)


class ClientDescribeRdsDbInstancesResponseTypeDef(
    _ClientDescribeRdsDbInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeRdsDbInstances` `Response`

    Contains the response to a ``DescribeRdsDbInstances`` request.

    - **RdsDbInstances** *(list) --*

      An a array of ``RdsDbInstance`` objects that describe the instances.

      - *(dict) --*

        Describes an Amazon RDS instance.

        - **RdsDbInstanceArn** *(string) --*

          The instance's ARN.

        - **DbInstanceIdentifier** *(string) --*

          The DB instance identifier.

        - **DbUser** *(string) --*

          The master user name.

        - **DbPassword** *(string) --*

          AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        - **Region** *(string) --*

          The instance's AWS region.

        - **Address** *(string) --*

          The instance's address.

        - **Engine** *(string) --*

          The instance's database engine.

        - **StackId** *(string) --*

          The ID of the stack with which the instance is registered.

        - **MissingOnRds** *(boolean) --*

          Set to ``true`` if AWS OpsWorks Stacks is unable to discover the Amazon RDS instance. AWS
          OpsWorks Stacks attempts to discover the instance only once. If this value is set to
          ``true`` , you must deregister the instance, and then register it again.
    """


_ClientDescribeServiceErrorsResponseServiceErrorsTypeDef = TypedDict(
    "_ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)


class ClientDescribeServiceErrorsResponseServiceErrorsTypeDef(
    _ClientDescribeServiceErrorsResponseServiceErrorsTypeDef
):
    """
    Type definition for `ClientDescribeServiceErrorsResponse` `ServiceErrors`

    Describes an AWS OpsWorks Stacks service error.

    - **ServiceErrorId** *(string) --*

      The error ID.

    - **StackId** *(string) --*

      The stack ID.

    - **InstanceId** *(string) --*

      The instance ID.

    - **Type** *(string) --*

      The error type.

    - **Message** *(string) --*

      A message that describes the error.

    - **CreatedAt** *(string) --*

      When the error occurred.
    """


_ClientDescribeServiceErrorsResponseTypeDef = TypedDict(
    "_ClientDescribeServiceErrorsResponseTypeDef",
    {"ServiceErrors": List[ClientDescribeServiceErrorsResponseServiceErrorsTypeDef]},
    total=False,
)


class ClientDescribeServiceErrorsResponseTypeDef(
    _ClientDescribeServiceErrorsResponseTypeDef
):
    """
    Type definition for `ClientDescribeServiceErrors` `Response`

    Contains the response to a ``DescribeServiceErrors`` request.

    - **ServiceErrors** *(list) --*

      An array of ``ServiceError`` objects that describe the specified service errors.

      - *(dict) --*

        Describes an AWS OpsWorks Stacks service error.

        - **ServiceErrorId** *(string) --*

          The error ID.

        - **StackId** *(string) --*

          The stack ID.

        - **InstanceId** *(string) --*

          The instance ID.

        - **Type** *(string) --*

          The error type.

        - **Message** *(string) --*

          A message that describes the error.

        - **CreatedAt** *(string) --*

          When the error occurred.
    """


_ClientDescribeStackProvisioningParametersResponseTypeDef = TypedDict(
    "_ClientDescribeStackProvisioningParametersResponseTypeDef",
    {"AgentInstallerUrl": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientDescribeStackProvisioningParametersResponseTypeDef(
    _ClientDescribeStackProvisioningParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackProvisioningParameters` `Response`

    Contains the response to a ``DescribeStackProvisioningParameters`` request.

    - **AgentInstallerUrl** *(string) --*

      The AWS OpsWorks Stacks agent installer's URL.

    - **Parameters** *(dict) --*

      An embedded object that contains the provisioning parameters.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
    },
    total=False,
)


class ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef(
    _ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef
):
    """
    Type definition for `ClientDescribeStackSummaryResponseStackSummary` `InstancesCount`

    An ``InstancesCount`` object with the number of instances in each status.

    - **Assigning** *(integer) --*

      The number of instances in the Assigning state.

    - **Booting** *(integer) --*

      The number of instances with ``booting`` status.

    - **ConnectionLost** *(integer) --*

      The number of instances with ``connection_lost`` status.

    - **Deregistering** *(integer) --*

      The number of instances in the Deregistering state.

    - **Online** *(integer) --*

      The number of instances with ``online`` status.

    - **Pending** *(integer) --*

      The number of instances with ``pending`` status.

    - **Rebooting** *(integer) --*

      The number of instances with ``rebooting`` status.

    - **Registered** *(integer) --*

      The number of instances in the Registered state.

    - **Registering** *(integer) --*

      The number of instances in the Registering state.

    - **Requested** *(integer) --*

      The number of instances with ``requested`` status.

    - **RunningSetup** *(integer) --*

      The number of instances with ``running_setup`` status.

    - **SetupFailed** *(integer) --*

      The number of instances with ``setup_failed`` status.

    - **ShuttingDown** *(integer) --*

      The number of instances with ``shutting_down`` status.

    - **StartFailed** *(integer) --*

      The number of instances with ``start_failed`` status.

    - **StopFailed** *(integer) --*

      The number of instances with ``stop_failed`` status.

    - **Stopped** *(integer) --*

      The number of instances with ``stopped`` status.

    - **Stopping** *(integer) --*

      The number of instances with ``stopping`` status.

    - **Terminated** *(integer) --*

      The number of instances with ``terminated`` status.

    - **Terminating** *(integer) --*

      The number of instances with ``terminating`` status.

    - **Unassigning** *(integer) --*

      The number of instances in the Unassigning state.
    """


_ClientDescribeStackSummaryResponseStackSummaryTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "LayersCount": int,
        "AppsCount": int,
        "InstancesCount": ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef,
    },
    total=False,
)


class ClientDescribeStackSummaryResponseStackSummaryTypeDef(
    _ClientDescribeStackSummaryResponseStackSummaryTypeDef
):
    """
    Type definition for `ClientDescribeStackSummaryResponse` `StackSummary`

    A ``StackSummary`` object that contains the results.

    - **StackId** *(string) --*

      The stack ID.

    - **Name** *(string) --*

      The stack name.

    - **Arn** *(string) --*

      The stack's ARN.

    - **LayersCount** *(integer) --*

      The number of layers.

    - **AppsCount** *(integer) --*

      The number of apps.

    - **InstancesCount** *(dict) --*

      An ``InstancesCount`` object with the number of instances in each status.

      - **Assigning** *(integer) --*

        The number of instances in the Assigning state.

      - **Booting** *(integer) --*

        The number of instances with ``booting`` status.

      - **ConnectionLost** *(integer) --*

        The number of instances with ``connection_lost`` status.

      - **Deregistering** *(integer) --*

        The number of instances in the Deregistering state.

      - **Online** *(integer) --*

        The number of instances with ``online`` status.

      - **Pending** *(integer) --*

        The number of instances with ``pending`` status.

      - **Rebooting** *(integer) --*

        The number of instances with ``rebooting`` status.

      - **Registered** *(integer) --*

        The number of instances in the Registered state.

      - **Registering** *(integer) --*

        The number of instances in the Registering state.

      - **Requested** *(integer) --*

        The number of instances with ``requested`` status.

      - **RunningSetup** *(integer) --*

        The number of instances with ``running_setup`` status.

      - **SetupFailed** *(integer) --*

        The number of instances with ``setup_failed`` status.

      - **ShuttingDown** *(integer) --*

        The number of instances with ``shutting_down`` status.

      - **StartFailed** *(integer) --*

        The number of instances with ``start_failed`` status.

      - **StopFailed** *(integer) --*

        The number of instances with ``stop_failed`` status.

      - **Stopped** *(integer) --*

        The number of instances with ``stopped`` status.

      - **Stopping** *(integer) --*

        The number of instances with ``stopping`` status.

      - **Terminated** *(integer) --*

        The number of instances with ``terminated`` status.

      - **Terminating** *(integer) --*

        The number of instances with ``terminating`` status.

      - **Unassigning** *(integer) --*

        The number of instances in the Unassigning state.
    """


_ClientDescribeStackSummaryResponseTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseTypeDef",
    {"StackSummary": ClientDescribeStackSummaryResponseStackSummaryTypeDef},
    total=False,
)


class ClientDescribeStackSummaryResponseTypeDef(
    _ClientDescribeStackSummaryResponseTypeDef
):
    """
    Type definition for `ClientDescribeStackSummary` `Response`

    Contains the response to a ``DescribeStackSummary`` request.

    - **StackSummary** *(dict) --*

      A ``StackSummary`` object that contains the results.

      - **StackId** *(string) --*

        The stack ID.

      - **Name** *(string) --*

        The stack name.

      - **Arn** *(string) --*

        The stack's ARN.

      - **LayersCount** *(integer) --*

        The number of layers.

      - **AppsCount** *(integer) --*

        The number of apps.

      - **InstancesCount** *(dict) --*

        An ``InstancesCount`` object with the number of instances in each status.

        - **Assigning** *(integer) --*

          The number of instances in the Assigning state.

        - **Booting** *(integer) --*

          The number of instances with ``booting`` status.

        - **ConnectionLost** *(integer) --*

          The number of instances with ``connection_lost`` status.

        - **Deregistering** *(integer) --*

          The number of instances in the Deregistering state.

        - **Online** *(integer) --*

          The number of instances with ``online`` status.

        - **Pending** *(integer) --*

          The number of instances with ``pending`` status.

        - **Rebooting** *(integer) --*

          The number of instances with ``rebooting`` status.

        - **Registered** *(integer) --*

          The number of instances in the Registered state.

        - **Registering** *(integer) --*

          The number of instances in the Registering state.

        - **Requested** *(integer) --*

          The number of instances with ``requested`` status.

        - **RunningSetup** *(integer) --*

          The number of instances with ``running_setup`` status.

        - **SetupFailed** *(integer) --*

          The number of instances with ``setup_failed`` status.

        - **ShuttingDown** *(integer) --*

          The number of instances with ``shutting_down`` status.

        - **StartFailed** *(integer) --*

          The number of instances with ``start_failed`` status.

        - **StopFailed** *(integer) --*

          The number of instances with ``stop_failed`` status.

        - **Stopped** *(integer) --*

          The number of instances with ``stopped`` status.

        - **Stopping** *(integer) --*

          The number of instances with ``stopping`` status.

        - **Terminated** *(integer) --*

          The number of instances with ``terminated`` status.

        - **Terminating** *(integer) --*

          The number of instances with ``terminating`` status.

        - **Unassigning** *(integer) --*

          The number of instances in the Unassigning state.
    """


_ClientDescribeStacksResponseStacksChefConfigurationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientDescribeStacksResponseStacksChefConfigurationTypeDef(
    _ClientDescribeStacksResponseStacksChefConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `ChefConfiguration`

    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the
    Berkshelf version. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.

    - **BerkshelfVersion** *(string) --*

      The Berkshelf version.
    """


_ClientDescribeStacksResponseStacksConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeStacksResponseStacksConfigurationManagerTypeDef(
    _ClientDescribeStacksResponseStacksConfigurationManagerTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `ConfigurationManager`

    The configuration manager.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
      and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef(
    _ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponseStacks` `CustomCookbooksSource`

    Contains the information required to retrieve an app or cookbook from a repository. For
    more information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
      the user name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
      value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
      value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new
      versions of an application. One of the simplest approaches is to have branches or
      revisions in your repository that represent different versions that can potentially be
      deployed.
    """


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[str, str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": ClientDescribeStacksResponseStacksConfigurationManagerTypeDef,
        "ChefConfiguration": ClientDescribeStacksResponseStacksChefConfigurationTypeDef,
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef,
        "DefaultSshKeyName": str,
        "CreatedAt": str,
        "DefaultRootDeviceType": str,
        "AgentVersion": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksTypeDef(
    _ClientDescribeStacksResponseStacksTypeDef
):
    """
    Type definition for `ClientDescribeStacksResponse` `Stacks`

    Describes a stack.

    - **StackId** *(string) --*

      The stack ID.

    - **Name** *(string) --*

      The stack name.

    - **Arn** *(string) --*

      The stack's ARN.

    - **Region** *(string) --*

      The stack AWS region, such as "ap-northeast-2". For more information about AWS regions,
      see `Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **VpcId** *(string) --*

      The VPC ID; applicable only if the stack is running in a VPC.

    - **Attributes** *(dict) --*

      The stack's attributes.

      - *(string) --*

        - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The stack AWS Identity and Access Management (IAM) role.

    - **DefaultInstanceProfileArn** *(string) --*

      The ARN of an IAM profile that is the default profile for all of the stack's EC2
      instances. For more information about IAM ARNs, see `Using Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

    - **DefaultOs** *(string) --*

      The stack's default operating system.

    - **HostnameTheme** *(string) --*

      The stack host name theme, with spaces replaced by underscores.

    - **DefaultAvailabilityZone** *(string) --*

      The stack's default Availability Zone. For more information, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **DefaultSubnetId** *(string) --*

      The default subnet ID; applicable only if the stack is running in a VPC.

    - **CustomJson** *(string) --*

      A JSON object that contains user-defined attributes to be added to the stack
      configuration and deployment attributes. You can use custom JSON to override the
      corresponding default stack configuration attribute values or to pass data to recipes.
      The string should be in the following format:

       ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"``

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack
      Configuration Attributes
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

    - **ConfigurationManager** *(dict) --*

      The configuration manager.

      - **Name** *(string) --*

        The name. This parameter must be set to "Chef".

      - **Version** *(string) --*

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
        and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

    - **ChefConfiguration** *(dict) --*

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the
      Berkshelf version. For more information, see `Create a New Stack
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      - **ManageBerkshelf** *(boolean) --*

        Whether to enable Berkshelf.

      - **BerkshelfVersion** *(string) --*

        The Berkshelf version.

    - **UseCustomCookbooks** *(boolean) --*

      Whether the stack uses custom cookbooks.

    - **UseOpsworksSecurityGroups** *(boolean) --*

      Whether the stack automatically associates the AWS OpsWorks Stacks built-in security
      groups with the stack's layers.

    - **CustomCookbooksSource** *(dict) --*

      Contains the information required to retrieve an app or cookbook from a repository. For
      more information, see `Adding Apps
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
      `Cookbooks and Recipes
      <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      - **Type** *(string) --*

        The repository type.

      - **Url** *(string) --*

        The source URL. The following is an example of an Amazon S3 source URL:
        ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

      - **Username** *(string) --*

        This parameter depends on the repository type.

        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
        the user name.

      - **Password** *(string) --*

        When included in a request, the parameter depends on the repository type.

        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

        * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

        For more information on how to safely handle IAM credentials, see
        `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
        <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
        value.

      - **SshKey** *(string) --*

        In requests, the repository's SSH key.

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
        value.

      - **Revision** *(string) --*

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new
        versions of an application. One of the simplest approaches is to have branches or
        revisions in your repository that represent different versions that can potentially be
        deployed.

    - **DefaultSshKeyName** *(string) --*

      A default Amazon EC2 key pair for the stack's instances. You can override this value when
      you create or update an instance.

    - **CreatedAt** *(string) --*

      The date when the stack was created.

    - **DefaultRootDeviceType** *(string) --*

      The default root device type. This value is used by default for all instances in the
      stack, but you can override it when you create an instance. For more information, see
      `Storage for the Root Device
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__
      .

    - **AgentVersion** *(string) --*

      The agent version. This parameter is set to ``LATEST`` for auto-update. or a version
      number for a fixed agent version.
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef]},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    Type definition for `ClientDescribeStacks` `Response`

    Contains the response to a ``DescribeStacks`` request.

    - **Stacks** *(list) --*

      An array of ``Stack`` objects that describe the stacks.

      - *(dict) --*

        Describes a stack.

        - **StackId** *(string) --*

          The stack ID.

        - **Name** *(string) --*

          The stack name.

        - **Arn** *(string) --*

          The stack's ARN.

        - **Region** *(string) --*

          The stack AWS region, such as "ap-northeast-2". For more information about AWS regions,
          see `Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **VpcId** *(string) --*

          The VPC ID; applicable only if the stack is running in a VPC.

        - **Attributes** *(dict) --*

          The stack's attributes.

          - *(string) --*

            - *(string) --*

        - **ServiceRoleArn** *(string) --*

          The stack AWS Identity and Access Management (IAM) role.

        - **DefaultInstanceProfileArn** *(string) --*

          The ARN of an IAM profile that is the default profile for all of the stack's EC2
          instances. For more information about IAM ARNs, see `Using Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

        - **DefaultOs** *(string) --*

          The stack's default operating system.

        - **HostnameTheme** *(string) --*

          The stack host name theme, with spaces replaced by underscores.

        - **DefaultAvailabilityZone** *(string) --*

          The stack's default Availability Zone. For more information, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **DefaultSubnetId** *(string) --*

          The default subnet ID; applicable only if the stack is running in a VPC.

        - **CustomJson** *(string) --*

          A JSON object that contains user-defined attributes to be added to the stack
          configuration and deployment attributes. You can use custom JSON to override the
          corresponding default stack configuration attribute values or to pass data to recipes.
          The string should be in the following format:

           ``"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"``

          For more information on custom JSON, see `Use Custom JSON to Modify the Stack
          Configuration Attributes
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

        - **ConfigurationManager** *(dict) --*

          The configuration manager.

          - **Name** *(string) --*

            The name. This parameter must be set to "Chef".

          - **Version** *(string) --*

            The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks,
            and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        - **ChefConfiguration** *(dict) --*

          A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the
          Berkshelf version. For more information, see `Create a New Stack
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

          - **ManageBerkshelf** *(boolean) --*

            Whether to enable Berkshelf.

          - **BerkshelfVersion** *(string) --*

            The Berkshelf version.

        - **UseCustomCookbooks** *(boolean) --*

          Whether the stack uses custom cookbooks.

        - **UseOpsworksSecurityGroups** *(boolean) --*

          Whether the stack automatically associates the AWS OpsWorks Stacks built-in security
          groups with the stack's layers.

        - **CustomCookbooksSource** *(dict) --*

          Contains the information required to retrieve an app or cookbook from a repository. For
          more information, see `Adding Apps
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
          `Cookbooks and Recipes
          <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

          - **Type** *(string) --*

            The repository type.

          - **Url** *(string) --*

            The source URL. The following is an example of an Amazon S3 source URL:
            ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

          - **Username** *(string) --*

            This parameter depends on the repository type.

            * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

            * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to
            the user name.

          - **Password** *(string) --*

            When included in a request, the parameter depends on the repository type.

            * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

            * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

            For more information on how to safely handle IAM credentials, see
            `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
            <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
            value.

          - **SshKey** *(string) --*

            In requests, the repository's SSH key.

            In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual
            value.

          - **Revision** *(string) --*

            The application's version. AWS OpsWorks Stacks enables you to easily deploy new
            versions of an application. One of the simplest approaches is to have branches or
            revisions in your repository that represent different versions that can potentially be
            deployed.

        - **DefaultSshKeyName** *(string) --*

          A default Amazon EC2 key pair for the stack's instances. You can override this value when
          you create or update an instance.

        - **CreatedAt** *(string) --*

          The date when the stack was created.

        - **DefaultRootDeviceType** *(string) --*

          The default root device type. This value is used by default for all instances in the
          stack, but you can override it when you create an instance. For more information, see
          `Storage for the Root Device
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__
          .

        - **AgentVersion** *(string) --*

          The agent version. This parameter is set to ``LATEST`` for auto-update. or a version
          number for a fixed agent version.
    """


_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef
):
    """
    Type definition for `ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurations` `AutoScalingSchedule`

    A ``WeeklyAutoScalingSchedule`` object with the instance schedule.

    - **Monday** *(dict) --*

      The schedule for Monday.

      - *(string) --*

        - *(string) --*

    - **Tuesday** *(dict) --*

      The schedule for Tuesday.

      - *(string) --*

        - *(string) --*

    - **Wednesday** *(dict) --*

      The schedule for Wednesday.

      - *(string) --*

        - *(string) --*

    - **Thursday** *(dict) --*

      The schedule for Thursday.

      - *(string) --*

        - *(string) --*

    - **Friday** *(dict) --*

      The schedule for Friday.

      - *(string) --*

        - *(string) --*

    - **Saturday** *(dict) --*

      The schedule for Saturday.

      - *(string) --*

        - *(string) --*

    - **Sunday** *(dict) --*

      The schedule for Sunday.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef,
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeTimeBasedAutoScalingResponse` `TimeBasedAutoScalingConfigurations`

    Describes an instance's time-based auto scaling configuration.

    - **InstanceId** *(string) --*

      The instance ID.

    - **AutoScalingSchedule** *(dict) --*

      A ``WeeklyAutoScalingSchedule`` object with the instance schedule.

      - **Monday** *(dict) --*

        The schedule for Monday.

        - *(string) --*

          - *(string) --*

      - **Tuesday** *(dict) --*

        The schedule for Tuesday.

        - *(string) --*

          - *(string) --*

      - **Wednesday** *(dict) --*

        The schedule for Wednesday.

        - *(string) --*

          - *(string) --*

      - **Thursday** *(dict) --*

        The schedule for Thursday.

        - *(string) --*

          - *(string) --*

      - **Friday** *(dict) --*

        The schedule for Friday.

        - *(string) --*

          - *(string) --*

      - **Saturday** *(dict) --*

        The schedule for Saturday.

        - *(string) --*

          - *(string) --*

      - **Sunday** *(dict) --*

        The schedule for Sunday.

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeTimeBasedAutoScalingResponseTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List[
            ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTypeDef
):
    """
    Type definition for `ClientDescribeTimeBasedAutoScaling` `Response`

    Contains the response to a ``DescribeTimeBasedAutoScaling`` request.

    - **TimeBasedAutoScalingConfigurations** *(list) --*

      An array of ``TimeBasedAutoScalingConfiguration`` objects that describe the configuration for
      the specified instances.

      - *(dict) --*

        Describes an instance's time-based auto scaling configuration.

        - **InstanceId** *(string) --*

          The instance ID.

        - **AutoScalingSchedule** *(dict) --*

          A ``WeeklyAutoScalingSchedule`` object with the instance schedule.

          - **Monday** *(dict) --*

            The schedule for Monday.

            - *(string) --*

              - *(string) --*

          - **Tuesday** *(dict) --*

            The schedule for Tuesday.

            - *(string) --*

              - *(string) --*

          - **Wednesday** *(dict) --*

            The schedule for Wednesday.

            - *(string) --*

              - *(string) --*

          - **Thursday** *(dict) --*

            The schedule for Thursday.

            - *(string) --*

              - *(string) --*

          - **Friday** *(dict) --*

            The schedule for Friday.

            - *(string) --*

              - *(string) --*

          - **Saturday** *(dict) --*

            The schedule for Saturday.

            - *(string) --*

              - *(string) --*

          - **Sunday** *(dict) --*

            The schedule for Sunday.

            - *(string) --*

              - *(string) --*
    """


_ClientDescribeUserProfilesResponseUserProfilesTypeDef = TypedDict(
    "_ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)


class ClientDescribeUserProfilesResponseUserProfilesTypeDef(
    _ClientDescribeUserProfilesResponseUserProfilesTypeDef
):
    """
    Type definition for `ClientDescribeUserProfilesResponse` `UserProfiles`

    Describes a user's SSH information.

    - **IamUserArn** *(string) --*

      The user's IAM ARN.

    - **Name** *(string) --*

      The user's name.

    - **SshUsername** *(string) --*

      The user's SSH user name.

    - **SshPublicKey** *(string) --*

      The user's SSH public key.

    - **AllowSelfManagement** *(boolean) --*

      Whether users can specify their own SSH public key through the My Settings page. For more
      information, see `Managing User Permissions
      <https://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`__ .
    """


_ClientDescribeUserProfilesResponseTypeDef = TypedDict(
    "_ClientDescribeUserProfilesResponseTypeDef",
    {"UserProfiles": List[ClientDescribeUserProfilesResponseUserProfilesTypeDef]},
    total=False,
)


class ClientDescribeUserProfilesResponseTypeDef(
    _ClientDescribeUserProfilesResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserProfiles` `Response`

    Contains the response to a ``DescribeUserProfiles`` request.

    - **UserProfiles** *(list) --*

      A ``Users`` object that describes the specified users.

      - *(dict) --*

        Describes a user's SSH information.

        - **IamUserArn** *(string) --*

          The user's IAM ARN.

        - **Name** *(string) --*

          The user's name.

        - **SshUsername** *(string) --*

          The user's SSH user name.

        - **SshPublicKey** *(string) --*

          The user's SSH public key.

        - **AllowSelfManagement** *(boolean) --*

          Whether users can specify their own SSH public key through the My Settings page. For more
          information, see `Managing User Permissions
          <https://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`__ .
    """


_ClientDescribeVolumesResponseVolumesTypeDef = TypedDict(
    "_ClientDescribeVolumesResponseVolumesTypeDef",
    {
        "VolumeId": str,
        "Ec2VolumeId": str,
        "Name": str,
        "RaidArrayId": str,
        "InstanceId": str,
        "Status": str,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "Region": str,
        "AvailabilityZone": str,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientDescribeVolumesResponseVolumesTypeDef(
    _ClientDescribeVolumesResponseVolumesTypeDef
):
    """
    Type definition for `ClientDescribeVolumesResponse` `Volumes`

    Describes an instance's Amazon EBS volume.

    - **VolumeId** *(string) --*

      The volume ID.

    - **Ec2VolumeId** *(string) --*

      The Amazon EC2 volume ID.

    - **Name** *(string) --*

      The volume name.

    - **RaidArrayId** *(string) --*

      The RAID array ID.

    - **InstanceId** *(string) --*

      The instance ID.

    - **Status** *(string) --*

      The value returned by `DescribeVolumes
      <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeVolumes.html>`__
      .

    - **Size** *(integer) --*

      The volume size.

    - **Device** *(string) --*

      The device name.

    - **MountPoint** *(string) --*

      The volume mount point. For example, "/mnt/disk1".

    - **Region** *(string) --*

      The AWS region. For more information about AWS regions, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **AvailabilityZone** *(string) --*

      The volume Availability Zone. For more information, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

    - **VolumeType** *(string) --*

      The volume type. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .

      * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a
      maximum size of 1024 GiB.

      * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a
      maximum size of 16384 GiB.

      * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1
      GiB and a maximum size of 16384 GiB.

      * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes
      must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

      * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum
      size of 16384 GiB.

    - **Iops** *(integer) --*

      For PIOPS volumes, the IOPS per disk.

    - **Encrypted** *(boolean) --*

      Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon
      EBS Encryption
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
    """


_ClientDescribeVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeVolumesResponseTypeDef",
    {"Volumes": List[ClientDescribeVolumesResponseVolumesTypeDef]},
    total=False,
)


class ClientDescribeVolumesResponseTypeDef(_ClientDescribeVolumesResponseTypeDef):
    """
    Type definition for `ClientDescribeVolumes` `Response`

    Contains the response to a ``DescribeVolumes`` request.

    - **Volumes** *(list) --*

      An array of volume IDs.

      - *(dict) --*

        Describes an instance's Amazon EBS volume.

        - **VolumeId** *(string) --*

          The volume ID.

        - **Ec2VolumeId** *(string) --*

          The Amazon EC2 volume ID.

        - **Name** *(string) --*

          The volume name.

        - **RaidArrayId** *(string) --*

          The RAID array ID.

        - **InstanceId** *(string) --*

          The instance ID.

        - **Status** *(string) --*

          The value returned by `DescribeVolumes
          <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeVolumes.html>`__
          .

        - **Size** *(integer) --*

          The volume size.

        - **Device** *(string) --*

          The device name.

        - **MountPoint** *(string) --*

          The volume mount point. For example, "/mnt/disk1".

        - **Region** *(string) --*

          The AWS region. For more information about AWS regions, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **AvailabilityZone** *(string) --*

          The volume Availability Zone. For more information, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

        - **VolumeType** *(string) --*

          The volume type. For more information, see `Amazon EBS Volume Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .

          * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a
          maximum size of 1024 GiB.

          * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a
          maximum size of 16384 GiB.

          * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1
          GiB and a maximum size of 16384 GiB.

          * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes
          must have a minimum size of 500 GiB and a maximum size of 16384 GiB.

          * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum
          size of 16384 GiB.

        - **Iops** *(integer) --*

          For PIOPS volumes, the IOPS per disk.

        - **Encrypted** *(boolean) --*

          Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon
          EBS Encryption
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
    """


_ClientGetHostnameSuggestionResponseTypeDef = TypedDict(
    "_ClientGetHostnameSuggestionResponseTypeDef",
    {"LayerId": str, "Hostname": str},
    total=False,
)


class ClientGetHostnameSuggestionResponseTypeDef(
    _ClientGetHostnameSuggestionResponseTypeDef
):
    """
    Type definition for `ClientGetHostnameSuggestion` `Response`

    Contains the response to a ``GetHostnameSuggestion`` request.

    - **LayerId** *(string) --*

      The layer ID.

    - **Hostname** *(string) --*

      The generated host name.
    """


_ClientGrantAccessResponseTemporaryCredentialTypeDef = TypedDict(
    "_ClientGrantAccessResponseTemporaryCredentialTypeDef",
    {"Username": str, "Password": str, "ValidForInMinutes": int, "InstanceId": str},
    total=False,
)


class ClientGrantAccessResponseTemporaryCredentialTypeDef(
    _ClientGrantAccessResponseTemporaryCredentialTypeDef
):
    """
    Type definition for `ClientGrantAccessResponse` `TemporaryCredential`

    A ``TemporaryCredential`` object that contains the data needed to log in to the instance by
    RDP clients, such as the Microsoft Remote Desktop Connection.

    - **Username** *(string) --*

      The user name.

    - **Password** *(string) --*

      The password.

    - **ValidForInMinutes** *(integer) --*

      The length of time (in minutes) that the grant is valid. When the grant expires, at the end
      of this period, the user will no longer be able to use the credentials to log in. If they
      are logged in at the time, they will be automatically logged out.

    - **InstanceId** *(string) --*

      The instance's AWS OpsWorks Stacks ID.
    """


_ClientGrantAccessResponseTypeDef = TypedDict(
    "_ClientGrantAccessResponseTypeDef",
    {"TemporaryCredential": ClientGrantAccessResponseTemporaryCredentialTypeDef},
    total=False,
)


class ClientGrantAccessResponseTypeDef(_ClientGrantAccessResponseTypeDef):
    """
    Type definition for `ClientGrantAccess` `Response`

    Contains the response to a ``GrantAccess`` request.

    - **TemporaryCredential** *(dict) --*

      A ``TemporaryCredential`` object that contains the data needed to log in to the instance by
      RDP clients, such as the Microsoft Remote Desktop Connection.

      - **Username** *(string) --*

        The user name.

      - **Password** *(string) --*

        The password.

      - **ValidForInMinutes** *(integer) --*

        The length of time (in minutes) that the grant is valid. When the grant expires, at the end
        of this period, the user will no longer be able to use the credentials to log in. If they
        are logged in at the time, they will be automatically logged out.

      - **InstanceId** *(string) --*

        The instance's AWS OpsWorks Stacks ID.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    Contains the response to a ``ListTags`` request.

    - **Tags** *(dict) --*

      A set of key-value pairs that contain tag keys and tag values that are attached to a stack or
      layer.

      - *(string) --*

        - *(string) --*

    - **NextToken** *(string) --*

      If a paginated request does not return all of the remaining results, this parameter is set to
      a token that you can assign to the request object's ``NextToken`` parameter to get the next
      set of results. If the previous paginated request returned all of the remaining results, this
      parameter is set to ``null`` .
    """


_ClientRegisterEcsClusterResponseTypeDef = TypedDict(
    "_ClientRegisterEcsClusterResponseTypeDef", {"EcsClusterArn": str}, total=False
)


class ClientRegisterEcsClusterResponseTypeDef(_ClientRegisterEcsClusterResponseTypeDef):
    """
    Type definition for `ClientRegisterEcsCluster` `Response`

    Contains the response to a ``RegisterEcsCluster`` request.

    - **EcsClusterArn** *(string) --*

      The cluster's ARN.
    """


_ClientRegisterElasticIpResponseTypeDef = TypedDict(
    "_ClientRegisterElasticIpResponseTypeDef", {"ElasticIp": str}, total=False
)


class ClientRegisterElasticIpResponseTypeDef(_ClientRegisterElasticIpResponseTypeDef):
    """
    Type definition for `ClientRegisterElasticIp` `Response`

    Contains the response to a ``RegisterElasticIp`` request.

    - **ElasticIp** *(string) --*

      The Elastic IP address.
    """


_ClientRegisterInstanceInstanceIdentityTypeDef = TypedDict(
    "_ClientRegisterInstanceInstanceIdentityTypeDef",
    {"Document": str, "Signature": str},
    total=False,
)


class ClientRegisterInstanceInstanceIdentityTypeDef(
    _ClientRegisterInstanceInstanceIdentityTypeDef
):
    """
    Type definition for `ClientRegisterInstance` `InstanceIdentity`

    An InstanceIdentity object that contains the instance's identity.

    - **Document** *(string) --*

      A JSON document that contains the metadata.

    - **Signature** *(string) --*

      A signature that can be used to verify the document's accuracy and authenticity.
    """


_ClientRegisterInstanceResponseTypeDef = TypedDict(
    "_ClientRegisterInstanceResponseTypeDef", {"InstanceId": str}, total=False
)


class ClientRegisterInstanceResponseTypeDef(_ClientRegisterInstanceResponseTypeDef):
    """
    Type definition for `ClientRegisterInstance` `Response`

    Contains the response to a ``RegisterInstanceResult`` request.

    - **InstanceId** *(string) --*

      The registered instance's AWS OpsWorks Stacks ID.
    """


_ClientRegisterVolumeResponseTypeDef = TypedDict(
    "_ClientRegisterVolumeResponseTypeDef", {"VolumeId": str}, total=False
)


class ClientRegisterVolumeResponseTypeDef(_ClientRegisterVolumeResponseTypeDef):
    """
    Type definition for `ClientRegisterVolume` `Response`

    Contains the response to a ``RegisterVolume`` request.

    - **VolumeId** *(string) --*

      The volume ID.
    """


_ClientSetLoadBasedAutoScalingDownScalingTypeDef = TypedDict(
    "_ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientSetLoadBasedAutoScalingDownScalingTypeDef(
    _ClientSetLoadBasedAutoScalingDownScalingTypeDef
):
    """
    Type definition for `ClientSetLoadBasedAutoScaling` `DownScaling`

    An ``AutoScalingThresholds`` object with the downscaling threshold configuration. If the load
    falls below these thresholds for a specified amount of time, AWS OpsWorks Stacks stops a
    specified number of instances.

    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.

    - **ThresholdsWaitTime** *(integer) --*

      The amount of time, in minutes, that the load must exceed a threshold before more instances are
      added or removed.

    - **IgnoreMetricsTime** *(integer) --*

      The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should
      ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds
      new instances following an upscaling event but the instances won't start reducing the load
      until they have been booted and configured. There is no point in raising additional scaling
      events during that operation, which typically takes several minutes. ``IgnoreMetricsTime``
      allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new
      instances online.

    - **CpuThreshold** *(float) --*

      The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the
      threshold.

    - **MemoryThreshold** *(float) --*

      The memory utilization threshold, as a percent of the available memory. A value of -1 disables
      the threshold.

    - **LoadThreshold** *(float) --*

      The load threshold. A value of -1 disables the threshold. For more information about how load
      is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

    - **Alarms** *(list) --*

      Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of
      up to five alarm names, which are case sensitive and must be in the same region as the stack.

      .. note::

        To use custom alarms, you must update your service role to allow
        ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for
        you when you first use this feature or you can edit the role manually. For more information,
        see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
        <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
        .

      - *(string) --*
    """


_ClientSetLoadBasedAutoScalingUpScalingTypeDef = TypedDict(
    "_ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientSetLoadBasedAutoScalingUpScalingTypeDef(
    _ClientSetLoadBasedAutoScalingUpScalingTypeDef
):
    """
    Type definition for `ClientSetLoadBasedAutoScaling` `UpScaling`

    An ``AutoScalingThresholds`` object with the upscaling threshold configuration. If the load
    exceeds these thresholds for a specified amount of time, AWS OpsWorks Stacks starts a specified
    number of instances.

    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.

    - **ThresholdsWaitTime** *(integer) --*

      The amount of time, in minutes, that the load must exceed a threshold before more instances are
      added or removed.

    - **IgnoreMetricsTime** *(integer) --*

      The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should
      ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds
      new instances following an upscaling event but the instances won't start reducing the load
      until they have been booted and configured. There is no point in raising additional scaling
      events during that operation, which typically takes several minutes. ``IgnoreMetricsTime``
      allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new
      instances online.

    - **CpuThreshold** *(float) --*

      The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the
      threshold.

    - **MemoryThreshold** *(float) --*

      The memory utilization threshold, as a percent of the available memory. A value of -1 disables
      the threshold.

    - **LoadThreshold** *(float) --*

      The load threshold. A value of -1 disables the threshold. For more information about how load
      is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

    - **Alarms** *(list) --*

      Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of
      up to five alarm names, which are case sensitive and must be in the same region as the stack.

      .. note::

        To use custom alarms, you must update your service role to allow
        ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for
        you when you first use this feature or you can edit the role manually. For more information,
        see `Allowing AWS OpsWorks Stacks to Act on Your Behalf
        <https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__
        .

      - *(string) --*
    """


_ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef = TypedDict(
    "_ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)


class ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef(
    _ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef
):
    """
    Type definition for `ClientSetTimeBasedAutoScaling` `AutoScalingSchedule`

    An ``AutoScalingSchedule`` with the instance schedule.

    - **Monday** *(dict) --*

      The schedule for Monday.

      - *(string) --*

        - *(string) --*

    - **Tuesday** *(dict) --*

      The schedule for Tuesday.

      - *(string) --*

        - *(string) --*

    - **Wednesday** *(dict) --*

      The schedule for Wednesday.

      - *(string) --*

        - *(string) --*

    - **Thursday** *(dict) --*

      The schedule for Thursday.

      - *(string) --*

        - *(string) --*

    - **Friday** *(dict) --*

      The schedule for Friday.

      - *(string) --*

        - *(string) --*

    - **Saturday** *(dict) --*

      The schedule for Saturday.

      - *(string) --*

        - *(string) --*

    - **Sunday** *(dict) --*

      The schedule for Sunday.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateAppAppSourceTypeDef = TypedDict(
    "_ClientUpdateAppAppSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientUpdateAppAppSourceTypeDef(_ClientUpdateAppAppSourceTypeDef):
    """
    Type definition for `ClientUpdateApp` `AppSource`

    A ``Source`` object that specifies the app repository.

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_ClientUpdateAppDataSourcesTypeDef = TypedDict(
    "_ClientUpdateAppDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientUpdateAppDataSourcesTypeDef(_ClientUpdateAppDataSourcesTypeDef):
    """
    Type definition for `ClientUpdateApp` `DataSources`

    Describes an app's data source.

    - **Type** *(string) --*

      The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` ,
      ``RdsDbInstance`` , or ``None`` .

    - **Arn** *(string) --*

      The data source's ARN.

    - **DatabaseName** *(string) --*

      The database name.
    """


_RequiredClientUpdateAppEnvironmentTypeDef = TypedDict(
    "_RequiredClientUpdateAppEnvironmentTypeDef", {"Key": str, "Value": str}
)
_OptionalClientUpdateAppEnvironmentTypeDef = TypedDict(
    "_OptionalClientUpdateAppEnvironmentTypeDef", {"Secure": bool}, total=False
)


class ClientUpdateAppEnvironmentTypeDef(
    _RequiredClientUpdateAppEnvironmentTypeDef,
    _OptionalClientUpdateAppEnvironmentTypeDef,
):
    """
    Type definition for `ClientUpdateApp` `Environment`

    Represents an app's environment variable.

    - **Key** *(string) --* **[REQUIRED]**

      (Required) The environment variable's name, which can consist of up to 64 characters and must
      be specified. The name can contain upper- and lowercase letters, numbers, and underscores
      (_), but it must start with a letter or underscore.

    - **Value** *(string) --* **[REQUIRED]**

      (Optional) The environment variable's value, which can be left empty. If you specify a value,
      it can contain up to 256 characters, which must all be printable.

    - **Secure** *(boolean) --*

      (Optional) Whether the variable's value will be returned by the  DescribeApps action. To
      conceal an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` then
      returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure``
      is ``false`` .
    """


_RequiredClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateAppSslConfigurationTypeDef",
    {"Certificate": str, "PrivateKey": str},
)
_OptionalClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateAppSslConfigurationTypeDef", {"Chain": str}, total=False
)


class ClientUpdateAppSslConfigurationTypeDef(
    _RequiredClientUpdateAppSslConfigurationTypeDef,
    _OptionalClientUpdateAppSslConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateApp` `SslConfiguration`

    An ``SslConfiguration`` object with the SSL configuration.

    - **Certificate** *(string) --* **[REQUIRED]**

      The contents of the certificate's domain.crt file.

    - **PrivateKey** *(string) --* **[REQUIRED]**

      The private key; the contents of the certificate's domain.kex file.

    - **Chain** *(string) --*

      Optional. Can be used to specify an intermediate certificate authority key or client
      authentication.
    """


_ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": str,
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": str,
        "Encoding": str,
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    """
    Type definition for `ClientUpdateLayerCloudWatchLogsConfiguration` `LogStreams`

    Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
    about members of this data type, see the `CloudWatch Logs Agent Reference
    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **LogGroupName** *(string) --*

      Specifies the destination log group. A log group is created automatically if it doesn't
      already exist. Log group names can be between 1 and 512 characters long. Allowed characters
      include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
      (period).

    - **DatetimeFormat** *(string) --*

      Specifies how the time stamp is extracted from logs. For more information, see the
      `CloudWatch Logs Agent Reference
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **TimeZone** *(string) --*

      Specifies the time zone of log event time stamps.

    - **File** *(string) --*

      Specifies log files that you want to push to CloudWatch Logs.

       ``File`` can point to a specific file or multiple files (by using wild card characters
       such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
       based on file modification time. We recommend that you use wild card characters to specify
       a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
       ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
       use a wildcard to match multiple file types, such as ``access_log_80`` and
       ``access_log_443`` . To specify multiple, different file types, add another log stream
       entry to the configuration file, so that each log file type is stored in a different log
       group.

      Zipped files are not supported.

    - **FileFingerprintLines** *(string) --*

      Specifies the range of lines for identifying a file. The valid values are one number, or
      two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
      line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
      Logs unless all specified lines are available.

    - **MultiLineStartPattern** *(string) --*

      Specifies the pattern for identifying the start of a log message.

    - **InitialPosition** *(string) --*

      Specifies where to start to read data (start_of_file or end_of_file). The default is
      start_of_file. This setting is only used if there is no state persisted for that log stream.

    - **Encoding** *(string) --*

      Specifies the encoding of the log file so that the file can be read correctly. The default
      is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

    - **BufferDuration** *(integer) --*

      Specifies the time duration for the batching of log events. The minimum value is 5000ms and
      default value is 5000ms.

    - **BatchCount** *(integer) --*

      Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

    - **BatchSize** *(integer) --*

      Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
      default value is 32768 bytes. This size is calculated as the sum of all event messages in
      UTF-8, plus 26 bytes for each log event.
    """


_ClientUpdateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[
            ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateLayerCloudWatchLogsConfigurationTypeDef(
    _ClientUpdateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateLayer` `CloudWatchLogsConfiguration`

    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .

    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.

    - **LogStreams** *(list) --*

      A list of configuration options for CloudWatch Logs.

      - *(dict) --*

        Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
        about members of this data type, see the `CloudWatch Logs Agent Reference
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **LogGroupName** *(string) --*

          Specifies the destination log group. A log group is created automatically if it doesn't
          already exist. Log group names can be between 1 and 512 characters long. Allowed characters
          include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
          (period).

        - **DatetimeFormat** *(string) --*

          Specifies how the time stamp is extracted from logs. For more information, see the
          `CloudWatch Logs Agent Reference
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **TimeZone** *(string) --*

          Specifies the time zone of log event time stamps.

        - **File** *(string) --*

          Specifies log files that you want to push to CloudWatch Logs.

           ``File`` can point to a specific file or multiple files (by using wild card characters
           such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
           based on file modification time. We recommend that you use wild card characters to specify
           a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
           ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
           use a wildcard to match multiple file types, such as ``access_log_80`` and
           ``access_log_443`` . To specify multiple, different file types, add another log stream
           entry to the configuration file, so that each log file type is stored in a different log
           group.

          Zipped files are not supported.

        - **FileFingerprintLines** *(string) --*

          Specifies the range of lines for identifying a file. The valid values are one number, or
          two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
          line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
          Logs unless all specified lines are available.

        - **MultiLineStartPattern** *(string) --*

          Specifies the pattern for identifying the start of a log message.

        - **InitialPosition** *(string) --*

          Specifies where to start to read data (start_of_file or end_of_file). The default is
          start_of_file. This setting is only used if there is no state persisted for that log stream.

        - **Encoding** *(string) --*

          Specifies the encoding of the log file so that the file can be read correctly. The default
          is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

        - **BufferDuration** *(integer) --*

          Specifies the time duration for the batching of log events. The minimum value is 5000ms and
          default value is 5000ms.

        - **BatchCount** *(integer) --*

          Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

        - **BatchSize** *(integer) --*

          Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
          default value is 32768 bytes. This size is calculated as the sum of all event messages in
          UTF-8, plus 26 bytes for each log event.
    """


_ClientUpdateLayerCustomRecipesTypeDef = TypedDict(
    "_ClientUpdateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientUpdateLayerCustomRecipesTypeDef(_ClientUpdateLayerCustomRecipesTypeDef):
    """
    Type definition for `ClientUpdateLayer` `CustomRecipes`

    A ``LayerCustomRecipes`` object that specifies the layer's custom recipes.

    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.

      - *(string) --*

    - **Configure** *(list) --*

      An array of custom recipe names to be run following a ``configure`` event.

      - *(string) --*

    - **Deploy** *(list) --*

      An array of custom recipe names to be run following a ``deploy`` event.

      - *(string) --*

    - **Undeploy** *(list) --*

      An array of custom recipe names to be run following a ``undeploy`` event.

      - *(string) --*

    - **Shutdown** *(list) --*

      An array of custom recipe names to be run following a ``shutdown`` event.

      - *(string) --*
    """


_ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef(
    _ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    Type definition for `ClientUpdateLayerLifecycleEventConfiguration` `Shutdown`

    A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

    - **ExecutionTimeout** *(integer) --*

      The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
      before shutting down an instance.

    - **DelayUntilElbConnectionsDrained** *(boolean) --*

      Whether to enable Elastic Load Balancing connection draining. For more information, see
      `Connection Draining
      <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_ClientUpdateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class ClientUpdateLayerLifecycleEventConfigurationTypeDef(
    _ClientUpdateLayerLifecycleEventConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateLayer` `LifecycleEventConfiguration`

    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.

      - **DelayUntilElbConnectionsDrained** *(boolean) --*

        Whether to enable Elastic Load Balancing connection draining. For more information, see
        `Connection Draining
        <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_RequiredClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientUpdateLayerVolumeConfigurationsTypeDef",
    {"MountPoint": str, "NumberOfDisks": int, "Size": int},
)
_OptionalClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientUpdateLayerVolumeConfigurationsTypeDef",
    {"RaidLevel": int, "VolumeType": str, "Iops": int, "Encrypted": bool},
    total=False,
)


class ClientUpdateLayerVolumeConfigurationsTypeDef(
    _RequiredClientUpdateLayerVolumeConfigurationsTypeDef,
    _OptionalClientUpdateLayerVolumeConfigurationsTypeDef,
):
    """
    Type definition for `ClientUpdateLayer` `VolumeConfigurations`

    Describes an Amazon EBS volume configuration.

    - **MountPoint** *(string) --* **[REQUIRED]**

      The volume mount point. For example "/dev/sdh".

    - **RaidLevel** *(integer) --*

      The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

    - **NumberOfDisks** *(integer) --* **[REQUIRED]**

      The number of disks in the volume.

    - **Size** *(integer) --* **[REQUIRED]**

      The volume size.

    - **VolumeType** *(string) --*

      The volume type. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .

      * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum
      size of 1024 GiB.

      * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a
      maximum size of 16384 GiB.

      * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB
      and a maximum size of 16384 GiB.

      * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must
      have a minimum size of 500 GiB and a maximum size of 16384 GiB.

      * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size
      of 16384 GiB.

    - **Iops** *(integer) --*

      For PIOPS volumes, the IOPS per disk.

    - **Encrypted** *(boolean) --*

      Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon EBS
      Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
    """


_ClientUpdateStackChefConfigurationTypeDef = TypedDict(
    "_ClientUpdateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientUpdateStackChefConfigurationTypeDef(
    _ClientUpdateStackChefConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateStack` `ChefConfiguration`

    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.

    - **BerkshelfVersion** *(string) --*

      The Berkshelf version.
    """


_ClientUpdateStackConfigurationManagerTypeDef = TypedDict(
    "_ClientUpdateStackConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientUpdateStackConfigurationManagerTypeDef(
    _ClientUpdateStackConfigurationManagerTypeDef
):
    """
    Type definition for `ClientUpdateStack` `ConfigurationManager`

    The configuration manager. When you update a stack, we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to
      12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ClientUpdateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientUpdateStackCustomCookbooksSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientUpdateStackCustomCookbooksSourceTypeDef(
    _ClientUpdateStackCustomCookbooksSourceTypeDef
):
    """
    Type definition for `ClientUpdateStack` `CustomCookbooksSource`

    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_DeploymentSuccessfulWaitWaiterConfigTypeDef = TypedDict(
    "_DeploymentSuccessfulWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DeploymentSuccessfulWaitWaiterConfigTypeDef(
    _DeploymentSuccessfulWaitWaiterConfigTypeDef
):
    """
    Type definition for `DeploymentSuccessfulWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_DescribeEcsClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEcsClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEcsClustersPaginatePaginationConfigTypeDef(
    _DescribeEcsClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEcsClustersPaginate` `PaginationConfig`

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


_DescribeEcsClustersPaginateResponseEcsClustersTypeDef = TypedDict(
    "_DescribeEcsClustersPaginateResponseEcsClustersTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)


class DescribeEcsClustersPaginateResponseEcsClustersTypeDef(
    _DescribeEcsClustersPaginateResponseEcsClustersTypeDef
):
    """
    Type definition for `DescribeEcsClustersPaginateResponse` `EcsClusters`

    Describes a registered Amazon ECS cluster.

    - **EcsClusterArn** *(string) --*

      The cluster's ARN.

    - **EcsClusterName** *(string) --*

      The cluster name.

    - **StackId** *(string) --*

      The stack ID.

    - **RegisteredAt** *(string) --*

      The time and date that the cluster was registered with the stack.
    """


_DescribeEcsClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeEcsClustersPaginateResponseTypeDef",
    {"EcsClusters": List[DescribeEcsClustersPaginateResponseEcsClustersTypeDef]},
    total=False,
)


class DescribeEcsClustersPaginateResponseTypeDef(
    _DescribeEcsClustersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEcsClustersPaginate` `Response`

    Contains the response to a ``DescribeEcsClusters`` request.

    - **EcsClusters** *(list) --*

      A list of ``EcsCluster`` objects containing the cluster descriptions.

      - *(dict) --*

        Describes a registered Amazon ECS cluster.

        - **EcsClusterArn** *(string) --*

          The cluster's ARN.

        - **EcsClusterName** *(string) --*

          The cluster name.

        - **StackId** *(string) --*

          The stack ID.

        - **RegisteredAt** *(string) --*

          The time and date that the cluster was registered with the stack.
    """


_InstanceOnlineWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceOnlineWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceOnlineWaitWaiterConfigTypeDef(_InstanceOnlineWaitWaiterConfigTypeDef):
    """
    Type definition for `InstanceOnlineWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_InstanceRegisteredWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceRegisteredWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceRegisteredWaitWaiterConfigTypeDef(
    _InstanceRegisteredWaitWaiterConfigTypeDef
):
    """
    Type definition for `InstanceRegisteredWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_InstanceStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceStoppedWaitWaiterConfigTypeDef(_InstanceStoppedWaitWaiterConfigTypeDef):
    """
    Type definition for `InstanceStoppedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_InstanceTerminatedWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceTerminatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceTerminatedWaitWaiterConfigTypeDef(
    _InstanceTerminatedWaitWaiterConfigTypeDef
):
    """
    Type definition for `InstanceTerminatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ServiceResourceCreateStackChefConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ServiceResourceCreateStackChefConfigurationTypeDef(
    _ServiceResourceCreateStackChefConfigurationTypeDef
):
    """
    Type definition for `ServiceResourceCreateStack` `ChefConfiguration`

    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.

    - **BerkshelfVersion** *(string) --*

      The Berkshelf version.
    """


_ServiceResourceCreateStackConfigurationManagerTypeDef = TypedDict(
    "_ServiceResourceCreateStackConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ServiceResourceCreateStackConfigurationManagerTypeDef(
    _ServiceResourceCreateStackConfigurationManagerTypeDef
):
    """
    Type definition for `ServiceResourceCreateStack` `ConfigurationManager`

    The configuration manager. When you create a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.

    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".

    - **Version** *(string) --*

      The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to
      12.2 for Windows stacks. The default value for Linux stacks is 11.4.
    """


_ServiceResourceCreateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ServiceResourceCreateStackCustomCookbooksSourceTypeDef",
    {
        "Type": str,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ServiceResourceCreateStackCustomCookbooksSourceTypeDef(
    _ServiceResourceCreateStackCustomCookbooksSourceTypeDef
):
    """
    Type definition for `ServiceResourceCreateStack` `CustomCookbooksSource`

    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

    - **Type** *(string) --*

      The repository type.

    - **Url** *(string) --*

      The source URL. The following is an example of an Amazon S3 source URL:
      ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

    - **Username** *(string) --*

      This parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID.

      * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user
      name.

    - **Password** *(string) --*

      When included in a request, the parameter depends on the repository type.

      * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key.

      * For HTTP bundles and Subversion repositories, set ``Password`` to the password.

      For more information on how to safely handle IAM credentials, see
      `https\\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html
      <https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **SshKey** *(string) --*

      In requests, the repository's SSH key.

      In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

    - **Revision** *(string) --*

      The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an
      application. One of the simplest approaches is to have branches or revisions in your repository
      that represent different versions that can potentially be deployed.
    """


_StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": str,
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": str,
        "Encoding": str,
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    """
    Type definition for `StackCreateLayerCloudWatchLogsConfiguration` `LogStreams`

    Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
    about members of this data type, see the `CloudWatch Logs Agent Reference
    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **LogGroupName** *(string) --*

      Specifies the destination log group. A log group is created automatically if it doesn't
      already exist. Log group names can be between 1 and 512 characters long. Allowed characters
      include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
      (period).

    - **DatetimeFormat** *(string) --*

      Specifies how the time stamp is extracted from logs. For more information, see the
      `CloudWatch Logs Agent Reference
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

    - **TimeZone** *(string) --*

      Specifies the time zone of log event time stamps.

    - **File** *(string) --*

      Specifies log files that you want to push to CloudWatch Logs.

       ``File`` can point to a specific file or multiple files (by using wild card characters
       such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
       based on file modification time. We recommend that you use wild card characters to specify
       a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
       ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
       use a wildcard to match multiple file types, such as ``access_log_80`` and
       ``access_log_443`` . To specify multiple, different file types, add another log stream
       entry to the configuration file, so that each log file type is stored in a different log
       group.

      Zipped files are not supported.

    - **FileFingerprintLines** *(string) --*

      Specifies the range of lines for identifying a file. The valid values are one number, or
      two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
      line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
      Logs unless all specified lines are available.

    - **MultiLineStartPattern** *(string) --*

      Specifies the pattern for identifying the start of a log message.

    - **InitialPosition** *(string) --*

      Specifies where to start to read data (start_of_file or end_of_file). The default is
      start_of_file. This setting is only used if there is no state persisted for that log stream.

    - **Encoding** *(string) --*

      Specifies the encoding of the log file so that the file can be read correctly. The default
      is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

    - **BufferDuration** *(integer) --*

      Specifies the time duration for the batching of log events. The minimum value is 5000ms and
      default value is 5000ms.

    - **BatchCount** *(integer) --*

      Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

    - **BatchSize** *(integer) --*

      Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
      default value is 32768 bytes. This size is calculated as the sum of all event messages in
      UTF-8, plus 26 bytes for each log event.
    """


_StackCreateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_StackCreateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[
            StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
        ],
    },
    total=False,
)


class StackCreateLayerCloudWatchLogsConfigurationTypeDef(
    _StackCreateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Type definition for `StackCreateLayer` `CloudWatchLogsConfiguration`

    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .

    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.

    - **LogStreams** *(list) --*

      A list of configuration options for CloudWatch Logs.

      - *(dict) --*

        Describes the Amazon CloudWatch logs configuration for a layer. For detailed information
        about members of this data type, see the `CloudWatch Logs Agent Reference
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **LogGroupName** *(string) --*

          Specifies the destination log group. A log group is created automatically if it doesn't
          already exist. Log group names can be between 1 and 512 characters long. Allowed characters
          include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.'
          (period).

        - **DatetimeFormat** *(string) --*

          Specifies how the time stamp is extracted from logs. For more information, see the
          `CloudWatch Logs Agent Reference
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

        - **TimeZone** *(string) --*

          Specifies the time zone of log event time stamps.

        - **File** *(string) --*

          Specifies log files that you want to push to CloudWatch Logs.

           ``File`` can point to a specific file or multiple files (by using wild card characters
           such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs,
           based on file modification time. We recommend that you use wild card characters to specify
           a series of files of the same type, such as ``access_log.2014-06-01-01`` ,
           ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't
           use a wildcard to match multiple file types, such as ``access_log_80`` and
           ``access_log_443`` . To specify multiple, different file types, add another log stream
           entry to the configuration file, so that each log file type is stored in a different log
           group.

          Zipped files are not supported.

        - **FileFingerprintLines** *(string) --*

          Specifies the range of lines for identifying a file. The valid values are one number, or
          two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first
          line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch
          Logs unless all specified lines are available.

        - **MultiLineStartPattern** *(string) --*

          Specifies the pattern for identifying the start of a log message.

        - **InitialPosition** *(string) --*

          Specifies where to start to read data (start_of_file or end_of_file). The default is
          start_of_file. This setting is only used if there is no state persisted for that log stream.

        - **Encoding** *(string) --*

          Specifies the encoding of the log file so that the file can be read correctly. The default
          is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

        - **BufferDuration** *(integer) --*

          Specifies the time duration for the batching of log events. The minimum value is 5000ms and
          default value is 5000ms.

        - **BatchCount** *(integer) --*

          Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

        - **BatchSize** *(integer) --*

          Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The
          default value is 32768 bytes. This size is calculated as the sum of all event messages in
          UTF-8, plus 26 bytes for each log event.
    """


_StackCreateLayerCustomRecipesTypeDef = TypedDict(
    "_StackCreateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class StackCreateLayerCustomRecipesTypeDef(_StackCreateLayerCustomRecipesTypeDef):
    """
    Type definition for `StackCreateLayer` `CustomRecipes`

    A ``LayerCustomRecipes`` object that specifies the layer custom recipes.

    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.

      - *(string) --*

    - **Configure** *(list) --*

      An array of custom recipe names to be run following a ``configure`` event.

      - *(string) --*

    - **Deploy** *(list) --*

      An array of custom recipe names to be run following a ``deploy`` event.

      - *(string) --*

    - **Undeploy** *(list) --*

      An array of custom recipe names to be run following a ``undeploy`` event.

      - *(string) --*

    - **Shutdown** *(list) --*

      An array of custom recipe names to be run following a ``shutdown`` event.

      - *(string) --*
    """


_StackCreateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_StackCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class StackCreateLayerLifecycleEventConfigurationShutdownTypeDef(
    _StackCreateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    Type definition for `StackCreateLayerLifecycleEventConfiguration` `Shutdown`

    A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

    - **ExecutionTimeout** *(integer) --*

      The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
      before shutting down an instance.

    - **DelayUntilElbConnectionsDrained** *(boolean) --*

      Whether to enable Elastic Load Balancing connection draining. For more information, see
      `Connection Draining
      <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_StackCreateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_StackCreateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": StackCreateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class StackCreateLayerLifecycleEventConfigurationTypeDef(
    _StackCreateLayerLifecycleEventConfigurationTypeDef
):
    """
    Type definition for `StackCreateLayer` `LifecycleEventConfiguration`

    A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to
    specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.

      - **DelayUntilElbConnectionsDrained** *(boolean) --*

        Whether to enable Elastic Load Balancing connection draining. For more information, see
        `Connection Draining
        <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__
    """


_RequiredStackCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredStackCreateLayerVolumeConfigurationsTypeDef",
    {"MountPoint": str, "NumberOfDisks": int, "Size": int},
)
_OptionalStackCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalStackCreateLayerVolumeConfigurationsTypeDef",
    {"RaidLevel": int, "VolumeType": str, "Iops": int, "Encrypted": bool},
    total=False,
)


class StackCreateLayerVolumeConfigurationsTypeDef(
    _RequiredStackCreateLayerVolumeConfigurationsTypeDef,
    _OptionalStackCreateLayerVolumeConfigurationsTypeDef,
):
    """
    Type definition for `StackCreateLayer` `VolumeConfigurations`

    Describes an Amazon EBS volume configuration.

    - **MountPoint** *(string) --* **[REQUIRED]**

      The volume mount point. For example "/dev/sdh".

    - **RaidLevel** *(integer) --*

      The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

    - **NumberOfDisks** *(integer) --* **[REQUIRED]**

      The number of disks in the volume.

    - **Size** *(integer) --* **[REQUIRED]**

      The volume size.

    - **VolumeType** *(string) --*

      The volume type. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ .

      * ``standard`` - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum
      size of 1024 GiB.

      * ``io1`` - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a
      maximum size of 16384 GiB.

      * ``gp2`` - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB
      and a maximum size of 16384 GiB.

      * ``st1`` - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must
      have a minimum size of 500 GiB and a maximum size of 16384 GiB.

      * ``sc1`` - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size
      of 16384 GiB.

    - **Iops** *(integer) --*

      For PIOPS volumes, the IOPS per disk.

    - **Encrypted** *(boolean) --*

      Specifies whether an Amazon EBS volume is encrypted. For more information, see `Amazon EBS
      Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ .
    """
