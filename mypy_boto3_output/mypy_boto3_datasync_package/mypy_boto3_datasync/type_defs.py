"Main interface for datasync type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAgentResponseTypeDef",
    "ClientCreateAgentTagsTypeDef",
    "ClientCreateLocationEfsEc2ConfigTypeDef",
    "ClientCreateLocationEfsResponseTypeDef",
    "ClientCreateLocationEfsTagsTypeDef",
    "ClientCreateLocationNfsMountOptionsTypeDef",
    "ClientCreateLocationNfsOnPremConfigTypeDef",
    "ClientCreateLocationNfsResponseTypeDef",
    "ClientCreateLocationNfsTagsTypeDef",
    "ClientCreateLocationS3ResponseTypeDef",
    "ClientCreateLocationS3S3ConfigTypeDef",
    "ClientCreateLocationS3TagsTypeDef",
    "ClientCreateLocationSmbMountOptionsTypeDef",
    "ClientCreateLocationSmbResponseTypeDef",
    "ClientCreateLocationSmbTagsTypeDef",
    "ClientCreateTaskExcludesTypeDef",
    "ClientCreateTaskOptionsTypeDef",
    "ClientCreateTaskResponseTypeDef",
    "ClientCreateTaskTagsTypeDef",
    "ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    "ClientDescribeAgentResponseTypeDef",
    "ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    "ClientDescribeLocationEfsResponseTypeDef",
    "ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    "ClientDescribeLocationNfsResponseOnPremConfigTypeDef",
    "ClientDescribeLocationNfsResponseTypeDef",
    "ClientDescribeLocationS3ResponseS3ConfigTypeDef",
    "ClientDescribeLocationS3ResponseTypeDef",
    "ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    "ClientDescribeLocationSmbResponseTypeDef",
    "ClientDescribeTaskExecutionResponseExcludesTypeDef",
    "ClientDescribeTaskExecutionResponseIncludesTypeDef",
    "ClientDescribeTaskExecutionResponseOptionsTypeDef",
    "ClientDescribeTaskExecutionResponseResultTypeDef",
    "ClientDescribeTaskExecutionResponseTypeDef",
    "ClientDescribeTaskResponseExcludesTypeDef",
    "ClientDescribeTaskResponseOptionsTypeDef",
    "ClientDescribeTaskResponseTypeDef",
    "ClientListAgentsResponseAgentsTypeDef",
    "ClientListAgentsResponseTypeDef",
    "ClientListLocationsResponseLocationsTypeDef",
    "ClientListLocationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    "ClientListTaskExecutionsResponseTypeDef",
    "ClientListTasksResponseTasksTypeDef",
    "ClientListTasksResponseTypeDef",
    "ClientStartTaskExecutionIncludesTypeDef",
    "ClientStartTaskExecutionOverrideOptionsTypeDef",
    "ClientStartTaskExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateTaskExcludesTypeDef",
    "ClientUpdateTaskOptionsTypeDef",
    "ListAgentsPaginatePaginationConfigTypeDef",
    "ListAgentsPaginateResponseAgentsTypeDef",
    "ListAgentsPaginateResponseTypeDef",
    "ListLocationsPaginatePaginationConfigTypeDef",
    "ListLocationsPaginateResponseLocationsTypeDef",
    "ListLocationsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTaskExecutionsPaginatePaginationConfigTypeDef",
    "ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef",
    "ListTaskExecutionsPaginateResponseTypeDef",
    "ListTasksPaginatePaginationConfigTypeDef",
    "ListTasksPaginateResponseTasksTypeDef",
    "ListTasksPaginateResponseTypeDef",
)


_ClientCreateAgentResponseTypeDef = TypedDict(
    "_ClientCreateAgentResponseTypeDef", {"AgentArn": str}, total=False
)


class ClientCreateAgentResponseTypeDef(_ClientCreateAgentResponseTypeDef):
    """
    Type definition for `ClientCreateAgent` `Response`

    CreateAgentResponse

    - **AgentArn** *(string) --*

      The Amazon Resource Name (ARN) of the agent. Use the ``ListAgents`` operation to return a
      list of agents for your account and AWS Region.
    """


_RequiredClientCreateAgentTagsTypeDef = TypedDict(
    "_RequiredClientCreateAgentTagsTypeDef", {"Key": str}
)
_OptionalClientCreateAgentTagsTypeDef = TypedDict(
    "_OptionalClientCreateAgentTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateAgentTagsTypeDef(
    _RequiredClientCreateAgentTagsTypeDef, _OptionalClientCreateAgentTagsTypeDef
):
    """
    Type definition for `ClientCreateAgent` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientCreateLocationEfsEc2ConfigTypeDef = TypedDict(
    "_ClientCreateLocationEfsEc2ConfigTypeDef",
    {"SubnetArn": str, "SecurityGroupArns": List[str]},
)


class ClientCreateLocationEfsEc2ConfigTypeDef(_ClientCreateLocationEfsEc2ConfigTypeDef):
    """
    Type definition for `ClientCreateLocationEfs` `Ec2Config`

    The subnet and security group that the Amazon EFS file system uses. The security group that you
    provide needs to be able to communicate with the security group on the mount target in the subnet
    specified.

    The exact relationship between security group M (of the mount target) and security group S (which
    you provide for DataSync to use at this stage) is as follows:

    * Security group M (which you associate with the mount target) must allow inbound access for the
    Transmission Control Protocol (TCP) on the NFS port (2049) from security group S. You can enable
    inbound connections either by IP address (CIDR range) or security group.

    * Security group S (provided to DataSync to access EFS) should have a rule that enables outbound
    connections to the NFS port on one of the file system’s mount targets. You can enable outbound
    connections either by IP address (CIDR range) or security group. For information about security
    groups and mount targets, see Security Groups for Amazon EC2 Instances and Mount Targets in the
    *Amazon EFS User Guide.*

    - **SubnetArn** *(string) --* **[REQUIRED]**

      The ARN of the subnet and the security group that DataSync uses to access the target EFS file
      system.

    - **SecurityGroupArns** *(list) --* **[REQUIRED]**

      The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2
      resource.

      - *(string) --*
    """


_ClientCreateLocationEfsResponseTypeDef = TypedDict(
    "_ClientCreateLocationEfsResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationEfsResponseTypeDef(_ClientCreateLocationEfsResponseTypeDef):
    """
    Type definition for `ClientCreateLocationEfs` `Response`

    CreateLocationEfs

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
    """


_RequiredClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationEfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationEfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationEfsTagsTypeDef(
    _RequiredClientCreateLocationEfsTagsTypeDef,
    _OptionalClientCreateLocationEfsTagsTypeDef,
):
    """
    Type definition for `ClientCreateLocationEfs` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientCreateLocationNfsMountOptionsTypeDef = TypedDict(
    "_ClientCreateLocationNfsMountOptionsTypeDef", {"Version": str}, total=False
)


class ClientCreateLocationNfsMountOptionsTypeDef(
    _ClientCreateLocationNfsMountOptionsTypeDef
):
    """
    Type definition for `ClientCreateLocationNfs` `MountOptions`

    The NFS mount options that DataSync can use to mount your NFS share.

    - **Version** *(string) --*

      The specific NFS version that you want DataSync to use to mount your NFS share. If the server
      refuses to use the version specified, the sync will fail. If you don't specify a version,
      DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a version based on
      negotiation with the NFS server.

      You can specify the following NFS versions:

      * **`NFSv3 <https://tools.ietf.org/html/rfc1813>`__ ** - stateless protocol version that allows
      for asynchronous writes on the server.

      * **`NFSv4.0 <https://tools.ietf.org/html/rfc3530>`__ ** - stateful, firewall-friendly protocol
      version that supports delegations and pseudo filesystems.

      * **`NFSv4.1 <https://tools.ietf.org/html/rfc5661>`__ ** - stateful protocol version that
      supports sessions, directory delegations, and parallel data processing. Version 4.1 also
      includes all features available in version 4.0.
    """


_ClientCreateLocationNfsOnPremConfigTypeDef = TypedDict(
    "_ClientCreateLocationNfsOnPremConfigTypeDef", {"AgentArns": List[str]}
)


class ClientCreateLocationNfsOnPremConfigTypeDef(
    _ClientCreateLocationNfsOnPremConfigTypeDef
):
    """
    Type definition for `ClientCreateLocationNfs` `OnPremConfig`

    Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect to an NFS
    server.

    - **AgentArns** *(list) --* **[REQUIRED]**

      ARNs)of the agents to use for an NFS location.

      - *(string) --*
    """


_ClientCreateLocationNfsResponseTypeDef = TypedDict(
    "_ClientCreateLocationNfsResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationNfsResponseTypeDef(_ClientCreateLocationNfsResponseTypeDef):
    """
    Type definition for `ClientCreateLocationNfs` `Response`

    CreateLocationNfsResponse

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the source NFS file system location that is created.
    """


_RequiredClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationNfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationNfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationNfsTagsTypeDef(
    _RequiredClientCreateLocationNfsTagsTypeDef,
    _OptionalClientCreateLocationNfsTagsTypeDef,
):
    """
    Type definition for `ClientCreateLocationNfs` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientCreateLocationS3ResponseTypeDef = TypedDict(
    "_ClientCreateLocationS3ResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationS3ResponseTypeDef(_ClientCreateLocationS3ResponseTypeDef):
    """
    Type definition for `ClientCreateLocationS3` `Response`

    CreateLocationS3Response

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the source Amazon S3 bucket location that is created.
    """


_ClientCreateLocationS3S3ConfigTypeDef = TypedDict(
    "_ClientCreateLocationS3S3ConfigTypeDef", {"BucketAccessRoleArn": str}
)


class ClientCreateLocationS3S3ConfigTypeDef(_ClientCreateLocationS3S3ConfigTypeDef):
    """
    Type definition for `ClientCreateLocationS3` `S3Config`

    The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used
    to access an Amazon S3 bucket.

    For detailed information about using such a role, see Creating a Location for Amazon S3 in the
    *AWS DataSync User Guide* .

    - **BucketAccessRoleArn** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3
      operation.
    """


_RequiredClientCreateLocationS3TagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationS3TagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationS3TagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationS3TagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationS3TagsTypeDef(
    _RequiredClientCreateLocationS3TagsTypeDef,
    _OptionalClientCreateLocationS3TagsTypeDef,
):
    """
    Type definition for `ClientCreateLocationS3` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientCreateLocationSmbMountOptionsTypeDef = TypedDict(
    "_ClientCreateLocationSmbMountOptionsTypeDef", {"Version": str}, total=False
)


class ClientCreateLocationSmbMountOptionsTypeDef(
    _ClientCreateLocationSmbMountOptionsTypeDef
):
    """
    Type definition for `ClientCreateLocationSmb` `MountOptions`

    The mount options used by DataSync to access the SMB server.

    - **Version** *(string) --*

      The specific SMB version that you want DataSync to use to mount your SMB share. If you don't
      specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects
      a version based on negotiation with the SMB server.
    """


_ClientCreateLocationSmbResponseTypeDef = TypedDict(
    "_ClientCreateLocationSmbResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationSmbResponseTypeDef(_ClientCreateLocationSmbResponseTypeDef):
    """
    Type definition for `ClientCreateLocationSmb` `Response`

    CreateLocationSmbResponse

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the source SMB file system location that is created.
    """


_RequiredClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationSmbTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationSmbTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationSmbTagsTypeDef(
    _RequiredClientCreateLocationSmbTagsTypeDef,
    _OptionalClientCreateLocationSmbTagsTypeDef,
):
    """
    Type definition for `ClientCreateLocationSmb` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientCreateTaskExcludesTypeDef = TypedDict(
    "_ClientCreateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientCreateTaskExcludesTypeDef(_ClientCreateTaskExcludesTypeDef):
    """
    Type definition for `ClientCreateTask` `Excludes`

    Specifies which files, folders and objects to include or exclude when transferring files from
    source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns are
      delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientCreateTaskOptionsTypeDef = TypedDict(
    "_ClientCreateTaskOptionsTypeDef",
    {
        "VerifyMode": str,
        "OverwriteMode": str,
        "Atime": str,
        "Mtime": str,
        "Uid": str,
        "Gid": str,
        "PreserveDeletedFiles": str,
        "PreserveDevices": str,
        "PosixPermissions": str,
        "BytesPerSecond": int,
        "TaskQueueing": str,
    },
    total=False,
)


class ClientCreateTaskOptionsTypeDef(_ClientCreateTaskOptionsTypeDef):
    """
    Type definition for `ClientCreateTask` `Options`

    The set of configuration options that control the behavior of a single execution of the task that
    occurs when you call ``StartTaskExecution`` . You can configure these options to preserve
    metadata such as user ID (UID) and group ID (GID), file permissions, data integrity verification,
    and so on.

    For each individual task execution, you can override these options by specifying the
    ``OverrideOptions`` before starting a the task execution. For more information, see the operation.

    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end of
      a task execution after all data and metadata have been transferred.

      Default value: POINT_IN_TIME_CONSISTENT.

      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

      NONE: Skip verification.

    - **OverwriteMode** *(string) --*

      A value that determines whether files at the destination should be overwritten or preserved
      when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
      file, even if the destination file differs from the source file. If you modify files in the
      destination and you sync the files, you can use this value to protect against overwriting those
      changes.

      Some storage classes have specific behaviors that can affect your S3 storage cost. For detailed
      information, see  using-storage-classes in the *AWS DataSync User Guide* .

    - **Atime** *(string) --*

      A file metadata value that shows the last time a file was accessed (that is, when the file was
      read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the
      original ``Atime`` attribute on all source files (that is, the version before the PREPARING
      phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync
      can only do this on a best-effort basis.

      Default value: BEST_EFFORT.

      BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

      NONE: Ignore ``Atime`` .

      .. note::

        If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

        If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

    - **Mtime** *(string) --*

      A value that indicates the last time that a file was modified (that is, a file was written to)
      before the PREPARING phase.

      Default value: PRESERVE.

      PRESERVE: Preserve original ``Mtime`` (recommended)

      NONE: Ignore ``Mtime`` .

      .. note::

        If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

        If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

    - **Uid** *(string) --*

      The user ID (UID) of the file's owner.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

      NONE: Ignore UID and GID.

    - **Gid** *(string) --*

      The group ID (GID) of the file's owners.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

      NONE: Ignore UID and GID.

    - **PreserveDeletedFiles** *(string) --*

      A value that specifies whether files in the destination that don't exist in the source file
      system should be preserved. This option can affect your storage cost. If your task deletes
      objects, you might incur minimum storage duration charges for certain storage classes. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      Default value: PRESERVE.

      PRESERVE: Ignore such destination files (recommended).

      REMOVE: Delete destination files that aren’t present in the source.

    - **PreserveDevices** *(string) --*

      A value that determines whether AWS DataSync should preserve the metadata of block and
      character devices in the source file system, and recreate the files with that device name and
      metadata on the destination.

      .. note::

        AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and
        don't return an end-of-file (EOF) marker.

      Default value: NONE.

      NONE: Ignore special devices (recommended).

      PRESERVE: Preserve character and block device metadata. This option isn't currently supported
      for Amazon EFS.

    - **PosixPermissions** *(string) --*

      A value that determines which users or groups can access a file for a specific purpose such as
      reading, writing, or execution of the file.

      Default value: PRESERVE.

      PRESERVE: Preserve POSIX-style permissions (recommended).

      NONE: Ignore permissions.

      .. note::

        AWS DataSync can preserve extant permissions of a source location.

    - **BytesPerSecond** *(integer) --*

      A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync
      to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

    - **TaskQueueing** *(string) --*

      A value that determines whether tasks should be queued before executing the tasks. If set to
      ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

      If you use the same agent to run multiple tasks you can enable the tasks to run in series. For
      more information see  task-queue .
    """


_ClientCreateTaskResponseTypeDef = TypedDict(
    "_ClientCreateTaskResponseTypeDef", {"TaskArn": str}, total=False
)


class ClientCreateTaskResponseTypeDef(_ClientCreateTaskResponseTypeDef):
    """
    Type definition for `ClientCreateTask` `Response`

    CreateTaskResponse

    - **TaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the task.
    """


_RequiredClientCreateTaskTagsTypeDef = TypedDict(
    "_RequiredClientCreateTaskTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTaskTagsTypeDef = TypedDict(
    "_OptionalClientCreateTaskTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTaskTagsTypeDef(
    _RequiredClientCreateTaskTagsTypeDef, _OptionalClientCreateTaskTagsTypeDef
):
    """
    Type definition for `ClientCreateTask` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientDescribeAgentResponsePrivateLinkConfigTypeDef = TypedDict(
    "_ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)


class ClientDescribeAgentResponsePrivateLinkConfigTypeDef(
    _ClientDescribeAgentResponsePrivateLinkConfigTypeDef
):
    """
    Type definition for `ClientDescribeAgentResponse` `PrivateLinkConfig`

    The subnet and the security group that DataSync used to access a VPC endpoint.

    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint that is configured for an agent. An agent that is configured
      with a VPC endpoint will not be accessible over the public Internet.

    - **PrivateLinkEndpoint** *(string) --*

      The private endpoint that is configured for an agent that has access to IP addresses in a
      `PrivateLink <https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html>`__ .
      An agent that is configured with this endpoint will not be accessible over the public
      Internet.

    - **SubnetArns** *(list) --*

      The Amazon Resource Names (ARNs) of the subnets that are configured for an agent activated
      in a VPC or an agent that has access to a VPC endpoint.

      - *(string) --*

    - **SecurityGroupArns** *(list) --*

      The Amazon Resource Names (ARNs) of the security groups that are configured for the EC2
      resource that hosts an agent activated in a VPC or an agent that has access to a VPC
      endpoint.

      - *(string) --*
    """


_ClientDescribeAgentResponseTypeDef = TypedDict(
    "_ClientDescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": str,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": str,
        "PrivateLinkConfig": ClientDescribeAgentResponsePrivateLinkConfigTypeDef,
    },
    total=False,
)


class ClientDescribeAgentResponseTypeDef(_ClientDescribeAgentResponseTypeDef):
    """
    Type definition for `ClientDescribeAgent` `Response`

    DescribeAgentResponse

    - **AgentArn** *(string) --*

      The Amazon Resource Name (ARN) of the agent.

    - **Name** *(string) --*

      The name of the agent.

    - **Status** *(string) --*

      The status of the agent. If the status is ONLINE, then the agent is configured properly and
      is available to use. The Running status is the normal running status for an agent. If the
      status is OFFLINE, the agent's VM is turned off or the agent is in an unhealthy state. When
      the issue that caused the unhealthy state is resolved, the agent returns to ONLINE status.

    - **LastConnectionTime** *(datetime) --*

      The time that the agent last connected to DataSyc.

    - **CreationTime** *(datetime) --*

      The time that the agent was activated (that is, created in your account).

    - **EndpointType** *(string) --*

      The type of endpoint that your agent is connected to. If the endpoint is a VPC endpoint, the
      agent is not accessible over the public Internet.

    - **PrivateLinkConfig** *(dict) --*

      The subnet and the security group that DataSync used to access a VPC endpoint.

      - **VpcEndpointId** *(string) --*

        The ID of the VPC endpoint that is configured for an agent. An agent that is configured
        with a VPC endpoint will not be accessible over the public Internet.

      - **PrivateLinkEndpoint** *(string) --*

        The private endpoint that is configured for an agent that has access to IP addresses in a
        `PrivateLink <https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html>`__ .
        An agent that is configured with this endpoint will not be accessible over the public
        Internet.

      - **SubnetArns** *(list) --*

        The Amazon Resource Names (ARNs) of the subnets that are configured for an agent activated
        in a VPC or an agent that has access to a VPC endpoint.

        - *(string) --*

      - **SecurityGroupArns** *(list) --*

        The Amazon Resource Names (ARNs) of the security groups that are configured for the EC2
        resource that hosts an agent activated in a VPC or an agent that has access to a VPC
        endpoint.

        - *(string) --*
    """


_ClientDescribeLocationEfsResponseEc2ConfigTypeDef = TypedDict(
    "_ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    {"SubnetArn": str, "SecurityGroupArns": List[str]},
    total=False,
)


class ClientDescribeLocationEfsResponseEc2ConfigTypeDef(
    _ClientDescribeLocationEfsResponseEc2ConfigTypeDef
):
    """
    Type definition for `ClientDescribeLocationEfsResponse` `Ec2Config`

    The subnet and the security group that DataSync uses to access target EFS file system. The
    subnet must have at least one mount target for that file system. The security group that you
    provide needs to be able to communicate with the security group on the mount target in the
    subnet specified.

    - **SubnetArn** *(string) --*

      The ARN of the subnet and the security group that DataSync uses to access the target EFS
      file system.

    - **SecurityGroupArns** *(list) --*

      The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon
      EC2 resource.

      - *(string) --*
    """


_ClientDescribeLocationEfsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": ClientDescribeLocationEfsResponseEc2ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationEfsResponseTypeDef(
    _ClientDescribeLocationEfsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLocationEfs` `Response`

    DescribeLocationEfsResponse

    - **LocationArn** *(string) --*

      The Amazon resource Name (ARN) of the EFS location that was described.

    - **LocationUri** *(string) --*

      The URL of the EFS location that was described.

    - **Ec2Config** *(dict) --*

      The subnet and the security group that DataSync uses to access target EFS file system. The
      subnet must have at least one mount target for that file system. The security group that you
      provide needs to be able to communicate with the security group on the mount target in the
      subnet specified.

      - **SubnetArn** *(string) --*

        The ARN of the subnet and the security group that DataSync uses to access the target EFS
        file system.

      - **SecurityGroupArns** *(list) --*

        The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon
        EC2 resource.

        - *(string) --*

    - **CreationTime** *(datetime) --*

      The time that the EFS location was created.
    """


_ClientDescribeLocationNfsResponseMountOptionsTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    {"Version": str},
    total=False,
)


class ClientDescribeLocationNfsResponseMountOptionsTypeDef(
    _ClientDescribeLocationNfsResponseMountOptionsTypeDef
):
    """
    Type definition for `ClientDescribeLocationNfsResponse` `MountOptions`

    The NFS mount options that DataSync used to mount your NFS share.

    - **Version** *(string) --*

      The specific NFS version that you want DataSync to use to mount your NFS share. If the
      server refuses to use the version specified, the sync will fail. If you don't specify a
      version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a
      version based on negotiation with the NFS server.

      You can specify the following NFS versions:

      * **`NFSv3 <https://tools.ietf.org/html/rfc1813>`__ ** - stateless protocol version that
      allows for asynchronous writes on the server.

      * **`NFSv4.0 <https://tools.ietf.org/html/rfc3530>`__ ** - stateful, firewall-friendly
      protocol version that supports delegations and pseudo filesystems.

      * **`NFSv4.1 <https://tools.ietf.org/html/rfc5661>`__ ** - stateful protocol version that
      supports sessions, directory delegations, and parallel data processing. Version 4.1 also
      includes all features available in version 4.0.
    """


_ClientDescribeLocationNfsResponseOnPremConfigTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseOnPremConfigTypeDef",
    {"AgentArns": List[str]},
    total=False,
)


class ClientDescribeLocationNfsResponseOnPremConfigTypeDef(
    _ClientDescribeLocationNfsResponseOnPremConfigTypeDef
):
    """
    Type definition for `ClientDescribeLocationNfsResponse` `OnPremConfig`

    A list of Amazon Resource Names (ARNs) of agents to use for a Network File System (NFS)
    location.

    - **AgentArns** *(list) --*

      ARNs)of the agents to use for an NFS location.

      - *(string) --*
    """


_ClientDescribeLocationNfsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": ClientDescribeLocationNfsResponseOnPremConfigTypeDef,
        "MountOptions": ClientDescribeLocationNfsResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationNfsResponseTypeDef(
    _ClientDescribeLocationNfsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLocationNfs` `Response`

    DescribeLocationNfsResponse

    - **LocationArn** *(string) --*

      The Amazon resource Name (ARN) of the NFS location that was described.

    - **LocationUri** *(string) --*

      The URL of the source NFS location that was described.

    - **OnPremConfig** *(dict) --*

      A list of Amazon Resource Names (ARNs) of agents to use for a Network File System (NFS)
      location.

      - **AgentArns** *(list) --*

        ARNs)of the agents to use for an NFS location.

        - *(string) --*

    - **MountOptions** *(dict) --*

      The NFS mount options that DataSync used to mount your NFS share.

      - **Version** *(string) --*

        The specific NFS version that you want DataSync to use to mount your NFS share. If the
        server refuses to use the version specified, the sync will fail. If you don't specify a
        version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a
        version based on negotiation with the NFS server.

        You can specify the following NFS versions:

        * **`NFSv3 <https://tools.ietf.org/html/rfc1813>`__ ** - stateless protocol version that
        allows for asynchronous writes on the server.

        * **`NFSv4.0 <https://tools.ietf.org/html/rfc3530>`__ ** - stateful, firewall-friendly
        protocol version that supports delegations and pseudo filesystems.

        * **`NFSv4.1 <https://tools.ietf.org/html/rfc5661>`__ ** - stateful protocol version that
        supports sessions, directory delegations, and parallel data processing. Version 4.1 also
        includes all features available in version 4.0.

    - **CreationTime** *(datetime) --*

      The time that the NFS location was created.
    """


_ClientDescribeLocationS3ResponseS3ConfigTypeDef = TypedDict(
    "_ClientDescribeLocationS3ResponseS3ConfigTypeDef",
    {"BucketAccessRoleArn": str},
    total=False,
)


class ClientDescribeLocationS3ResponseS3ConfigTypeDef(
    _ClientDescribeLocationS3ResponseS3ConfigTypeDef
):
    """
    Type definition for `ClientDescribeLocationS3Response` `S3Config`

    The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is
    used to access an Amazon S3 bucket.

    For detailed information about using such a role, see Creating a Location for Amazon S3 in
    the *AWS DataSync User Guide* .

    - **BucketAccessRoleArn** *(string) --*

      The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3
      operation.
    """


_ClientDescribeLocationS3ResponseTypeDef = TypedDict(
    "_ClientDescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": str,
        "S3Config": ClientDescribeLocationS3ResponseS3ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationS3ResponseTypeDef(_ClientDescribeLocationS3ResponseTypeDef):
    """
    Type definition for `ClientDescribeLocationS3` `Response`

    DescribeLocationS3Response

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon S3 bucket location.

    - **LocationUri** *(string) --*

      The URL of the Amazon S3 location that was described.

    - **S3StorageClass** *(string) --*

      The Amazon S3 storage class that you chose to store your files in when this location is used
      as a task destination. For more information about S3 storage classes, see `Amazon S3 Storage
      Classes <https://aws.amazon.com/s3/storage-classes/>`__ in the *Amazon Simple Storage Service
      Developer Guide* . Some storage classes have behaviors that can affect your S3 storage cost.
      For detailed information, see  using-storage-classes .

    - **S3Config** *(dict) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is
      used to access an Amazon S3 bucket.

      For detailed information about using such a role, see Creating a Location for Amazon S3 in
      the *AWS DataSync User Guide* .

      - **BucketAccessRoleArn** *(string) --*

        The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3
        operation.

    - **CreationTime** *(datetime) --*

      The time that the Amazon S3 bucket location was created.
    """


_ClientDescribeLocationSmbResponseMountOptionsTypeDef = TypedDict(
    "_ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    {"Version": str},
    total=False,
)


class ClientDescribeLocationSmbResponseMountOptionsTypeDef(
    _ClientDescribeLocationSmbResponseMountOptionsTypeDef
):
    """
    Type definition for `ClientDescribeLocationSmbResponse` `MountOptions`

    The mount options that are available for DataSync to use to access an SMB location.

    - **Version** *(string) --*

      The specific SMB version that you want DataSync to use to mount your SMB share. If you
      don't specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync
      automatically selects a version based on negotiation with the SMB server.
    """


_ClientDescribeLocationSmbResponseTypeDef = TypedDict(
    "_ClientDescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": ClientDescribeLocationSmbResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationSmbResponseTypeDef(
    _ClientDescribeLocationSmbResponseTypeDef
):
    """
    Type definition for `ClientDescribeLocationSmb` `Response`

    DescribeLocationSmbResponse

    - **LocationArn** *(string) --*

      The Amazon resource Name (ARN) of the SMB location that was described.

    - **LocationUri** *(string) --*

      The URL of the source SBM location that was described.

    - **AgentArns** *(list) --*

      The Amazon Resource Name (ARN) of the source SMB file system location that is created.

      - *(string) --*

    - **User** *(string) --*

      The user who can mount the share, has the permissions to access files and folders in the SMB
      share.

    - **Domain** *(string) --*

      The name of the Windows domain that the SMB server belongs to.

    - **MountOptions** *(dict) --*

      The mount options that are available for DataSync to use to access an SMB location.

      - **Version** *(string) --*

        The specific SMB version that you want DataSync to use to mount your SMB share. If you
        don't specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync
        automatically selects a version based on negotiation with the SMB server.

    - **CreationTime** *(datetime) --*

      The time that the SMB location was created.
    """


_ClientDescribeTaskExecutionResponseExcludesTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseExcludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientDescribeTaskExecutionResponseExcludesTypeDef(
    _ClientDescribeTaskExecutionResponseExcludesTypeDef
):
    """
    Type definition for `ClientDescribeTaskExecutionResponse` `Excludes`

    Specifies which files, folders and objects to include or exclude when transferring files
    from source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns
      are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientDescribeTaskExecutionResponseIncludesTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseIncludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientDescribeTaskExecutionResponseIncludesTypeDef(
    _ClientDescribeTaskExecutionResponseIncludesTypeDef
):
    """
    Type definition for `ClientDescribeTaskExecutionResponse` `Includes`

    Specifies which files, folders and objects to include or exclude when transferring files
    from source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns
      are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientDescribeTaskExecutionResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseOptionsTypeDef",
    {
        "VerifyMode": str,
        "OverwriteMode": str,
        "Atime": str,
        "Mtime": str,
        "Uid": str,
        "Gid": str,
        "PreserveDeletedFiles": str,
        "PreserveDevices": str,
        "PosixPermissions": str,
        "BytesPerSecond": int,
        "TaskQueueing": str,
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseOptionsTypeDef(
    _ClientDescribeTaskExecutionResponseOptionsTypeDef
):
    """
    Type definition for `ClientDescribeTaskExecutionResponse` `Options`

    Represents the options that are available to control the behavior of a  StartTaskExecution
    operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and
    file permissions, and also overwriting files in the destination, data integrity verification,
    and so on.

    A task has a set of default options associated with it. If you don't specify an option in
    StartTaskExecution , the default value is used. You can override the defaults options on each
    task execution by specifying an overriding ``Options`` value to  StartTaskExecution .

    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the
      end of a task execution after all data and metadata have been transferred.

      Default value: POINT_IN_TIME_CONSISTENT.

      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

      NONE: Skip verification.

    - **OverwriteMode** *(string) --*

      A value that determines whether files at the destination should be overwritten or preserved
      when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
      file, even if the destination file differs from the source file. If you modify files in the
      destination and you sync the files, you can use this value to protect against overwriting
      those changes.

      Some storage classes have specific behaviors that can affect your S3 storage cost. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

    - **Atime** *(string) --*

      A file metadata value that shows the last time a file was accessed (that is, when the file
      was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve
      the original ``Atime`` attribute on all source files (that is, the version before the
      PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so
      AWS DataSync can only do this on a best-effort basis.

      Default value: BEST_EFFORT.

      BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

      NONE: Ignore ``Atime`` .

      .. note::

        If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

        If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

    - **Mtime** *(string) --*

      A value that indicates the last time that a file was modified (that is, a file was written
      to) before the PREPARING phase.

      Default value: PRESERVE.

      PRESERVE: Preserve original ``Mtime`` (recommended)

      NONE: Ignore ``Mtime`` .

      .. note::

        If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

        If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

    - **Uid** *(string) --*

      The user ID (UID) of the file's owner.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

      NONE: Ignore UID and GID.

    - **Gid** *(string) --*

      The group ID (GID) of the file's owners.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

      NONE: Ignore UID and GID.

    - **PreserveDeletedFiles** *(string) --*

      A value that specifies whether files in the destination that don't exist in the source file
      system should be preserved. This option can affect your storage cost. If your task deletes
      objects, you might incur minimum storage duration charges for certain storage classes. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      Default value: PRESERVE.

      PRESERVE: Ignore such destination files (recommended).

      REMOVE: Delete destination files that aren’t present in the source.

    - **PreserveDevices** *(string) --*

      A value that determines whether AWS DataSync should preserve the metadata of block and
      character devices in the source file system, and recreate the files with that device name
      and metadata on the destination.

      .. note::

        AWS DataSync can't sync the actual contents of such devices, because they are nonterminal
        and don't return an end-of-file (EOF) marker.

      Default value: NONE.

      NONE: Ignore special devices (recommended).

      PRESERVE: Preserve character and block device metadata. This option isn't currently
      supported for Amazon EFS.

    - **PosixPermissions** *(string) --*

      A value that determines which users or groups can access a file for a specific purpose such
      as reading, writing, or execution of the file.

      Default value: PRESERVE.

      PRESERVE: Preserve POSIX-style permissions (recommended).

      NONE: Ignore permissions.

      .. note::

        AWS DataSync can preserve extant permissions of a source location.

    - **BytesPerSecond** *(integer) --*

      A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS
      DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

    - **TaskQueueing** *(string) --*

      A value that determines whether tasks should be queued before executing the tasks. If set
      to ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

      If you use the same agent to run multiple tasks you can enable the tasks to run in series.
      For more information see  task-queue .
    """


_ClientDescribeTaskExecutionResponseResultTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseResultTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": str,
        "TransferDuration": int,
        "TransferStatus": str,
        "VerifyDuration": int,
        "VerifyStatus": str,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseResultTypeDef(
    _ClientDescribeTaskExecutionResponseResultTypeDef
):
    """
    Type definition for `ClientDescribeTaskExecutionResponse` `Result`

    The result of the task execution.

    - **PrepareDuration** *(integer) --*

      The total time in milliseconds that AWS DataSync spent in the PREPARING phase.

    - **PrepareStatus** *(string) --*

      The status of the PREPARING phase.

    - **TransferDuration** *(integer) --*

      The total time in milliseconds that AWS DataSync spent in the TRANSFERRING phase.

    - **TransferStatus** *(string) --*

      The status of the TRANSFERRING Phase.

    - **VerifyDuration** *(integer) --*

      The total time in milliseconds that AWS DataSync spent in the VERIFYING phase.

    - **VerifyStatus** *(string) --*

      The status of the VERIFYING Phase.

    - **ErrorCode** *(string) --*

      Errors that AWS DataSync encountered during execution of the task. You can use this error
      code to help troubleshoot issues.

    - **ErrorDetail** *(string) --*

      Detailed description of an error that was encountered during the task execution. You can
      use this information to help troubleshoot issues.
    """


_ClientDescribeTaskExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": str,
        "Options": ClientDescribeTaskExecutionResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskExecutionResponseExcludesTypeDef],
        "Includes": List[ClientDescribeTaskExecutionResponseIncludesTypeDef],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": ClientDescribeTaskExecutionResponseResultTypeDef,
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseTypeDef(
    _ClientDescribeTaskExecutionResponseTypeDef
):
    """
    Type definition for `ClientDescribeTaskExecution` `Response`

    DescribeTaskExecutionResponse

    - **TaskExecutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the task execution that was described. ``TaskExecutionArn``
      is hierarchical and includes ``TaskArn`` for the task that was executed.

      For example, a ``TaskExecution`` value with the ARN
      ``arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b``
      executed the task with the ARN
      ``arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2`` .

    - **Status** *(string) --*

      The status of the task execution.

      For detailed information about task execution statuses, see Understanding Task Statuses in
      the *AWS DataSync User Guide.*

    - **Options** *(dict) --*

      Represents the options that are available to control the behavior of a  StartTaskExecution
      operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and
      file permissions, and also overwriting files in the destination, data integrity verification,
      and so on.

      A task has a set of default options associated with it. If you don't specify an option in
      StartTaskExecution , the default value is used. You can override the defaults options on each
      task execution by specifying an overriding ``Options`` value to  StartTaskExecution .

      - **VerifyMode** *(string) --*

        A value that determines whether a data integrity verification should be performed at the
        end of a task execution after all data and metadata have been transferred.

        Default value: POINT_IN_TIME_CONSISTENT.

        POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

        ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

        NONE: Skip verification.

      - **OverwriteMode** *(string) --*

        A value that determines whether files at the destination should be overwritten or preserved
        when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
        file, even if the destination file differs from the source file. If you modify files in the
        destination and you sync the files, you can use this value to protect against overwriting
        those changes.

        Some storage classes have specific behaviors that can affect your S3 storage cost. For
        detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      - **Atime** *(string) --*

        A file metadata value that shows the last time a file was accessed (that is, when the file
        was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve
        the original ``Atime`` attribute on all source files (that is, the version before the
        PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so
        AWS DataSync can only do this on a best-effort basis.

        Default value: BEST_EFFORT.

        BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

        NONE: Ignore ``Atime`` .

        .. note::

          If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

          If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

      - **Mtime** *(string) --*

        A value that indicates the last time that a file was modified (that is, a file was written
        to) before the PREPARING phase.

        Default value: PRESERVE.

        PRESERVE: Preserve original ``Mtime`` (recommended)

        NONE: Ignore ``Mtime`` .

        .. note::

          If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

          If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

      - **Uid** *(string) --*

        The user ID (UID) of the file's owner.

        Default value: INT_VALUE. This preserves the integer value of the ID.

        INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

        NONE: Ignore UID and GID.

      - **Gid** *(string) --*

        The group ID (GID) of the file's owners.

        Default value: INT_VALUE. This preserves the integer value of the ID.

        INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

        NONE: Ignore UID and GID.

      - **PreserveDeletedFiles** *(string) --*

        A value that specifies whether files in the destination that don't exist in the source file
        system should be preserved. This option can affect your storage cost. If your task deletes
        objects, you might incur minimum storage duration charges for certain storage classes. For
        detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

        Default value: PRESERVE.

        PRESERVE: Ignore such destination files (recommended).

        REMOVE: Delete destination files that aren’t present in the source.

      - **PreserveDevices** *(string) --*

        A value that determines whether AWS DataSync should preserve the metadata of block and
        character devices in the source file system, and recreate the files with that device name
        and metadata on the destination.

        .. note::

          AWS DataSync can't sync the actual contents of such devices, because they are nonterminal
          and don't return an end-of-file (EOF) marker.

        Default value: NONE.

        NONE: Ignore special devices (recommended).

        PRESERVE: Preserve character and block device metadata. This option isn't currently
        supported for Amazon EFS.

      - **PosixPermissions** *(string) --*

        A value that determines which users or groups can access a file for a specific purpose such
        as reading, writing, or execution of the file.

        Default value: PRESERVE.

        PRESERVE: Preserve POSIX-style permissions (recommended).

        NONE: Ignore permissions.

        .. note::

          AWS DataSync can preserve extant permissions of a source location.

      - **BytesPerSecond** *(integer) --*

        A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS
        DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

      - **TaskQueueing** *(string) --*

        A value that determines whether tasks should be queued before executing the tasks. If set
        to ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

        If you use the same agent to run multiple tasks you can enable the tasks to run in series.
        For more information see  task-queue .

    - **Excludes** *(list) --*

      A list of filter rules that determines which files to exclude from a task. The list should
      contain a single filter string that consists of the patterns to exclude. The patterns are
      delimited by "|" (that is, a pipe), for example: ``"/folder1|/folder2"``

      - *(dict) --*

        Specifies which files, folders and objects to include or exclude when transferring files
        from source to destination.

        - **FilterType** *(string) --*

          The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

        - **Value** *(string) --*

          A single filter string that consists of the patterns to include or exclude. The patterns
          are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``

    - **Includes** *(list) --*

      A list of filter rules that determines which files to include when running a task. The list
      should contain a single filter string that consists of the patterns to include. The patterns
      are delimited by "|" (that is, a pipe), for example: ``"/folder1|/folder2"``

      - *(dict) --*

        Specifies which files, folders and objects to include or exclude when transferring files
        from source to destination.

        - **FilterType** *(string) --*

          The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

        - **Value** *(string) --*

          A single filter string that consists of the patterns to include or exclude. The patterns
          are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``

    - **StartTime** *(datetime) --*

      The time that the task execution was started.

    - **EstimatedFilesToTransfer** *(integer) --*

      The expected number of files that is to be transferred over the network. This value is
      calculated during the PREPARING phase, before the TRANSFERRING phase. This value is the
      expected number of files to be transferred. It's calculated based on comparing the content of
      the source and destination locations and finding the delta that needs to be transferred.

    - **EstimatedBytesToTransfer** *(integer) --*

      The estimated physical number of bytes that is to be transferred over the network.

    - **FilesTransferred** *(integer) --*

      The actual number of files that was transferred over the network. This value is calculated
      and updated on an ongoing basis during the TRANSFERRING phase. It's updated periodically when
      each file is read from the source and sent over the network.

      If failures occur during a transfer, this value can be less than ``EstimatedFilesToTransfer``
      . This value can also be greater than ``EstimatedFilesTransferred`` in some cases. This
      element is implementation-specific for some location types, so don't use it as an indicator
      for a correct file number or to monitor your task execution.

    - **BytesWritten** *(integer) --*

      The number of logical bytes written to the destination AWS storage resource.

    - **BytesTransferred** *(integer) --*

      The physical number of bytes transferred over the network.

    - **Result** *(dict) --*

      The result of the task execution.

      - **PrepareDuration** *(integer) --*

        The total time in milliseconds that AWS DataSync spent in the PREPARING phase.

      - **PrepareStatus** *(string) --*

        The status of the PREPARING phase.

      - **TransferDuration** *(integer) --*

        The total time in milliseconds that AWS DataSync spent in the TRANSFERRING phase.

      - **TransferStatus** *(string) --*

        The status of the TRANSFERRING Phase.

      - **VerifyDuration** *(integer) --*

        The total time in milliseconds that AWS DataSync spent in the VERIFYING phase.

      - **VerifyStatus** *(string) --*

        The status of the VERIFYING Phase.

      - **ErrorCode** *(string) --*

        Errors that AWS DataSync encountered during execution of the task. You can use this error
        code to help troubleshoot issues.

      - **ErrorDetail** *(string) --*

        Detailed description of an error that was encountered during the task execution. You can
        use this information to help troubleshoot issues.
    """


_ClientDescribeTaskResponseExcludesTypeDef = TypedDict(
    "_ClientDescribeTaskResponseExcludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientDescribeTaskResponseExcludesTypeDef(
    _ClientDescribeTaskResponseExcludesTypeDef
):
    """
    Type definition for `ClientDescribeTaskResponse` `Excludes`

    Specifies which files, folders and objects to include or exclude when transferring files
    from source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns
      are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientDescribeTaskResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeTaskResponseOptionsTypeDef",
    {
        "VerifyMode": str,
        "OverwriteMode": str,
        "Atime": str,
        "Mtime": str,
        "Uid": str,
        "Gid": str,
        "PreserveDeletedFiles": str,
        "PreserveDevices": str,
        "PosixPermissions": str,
        "BytesPerSecond": int,
        "TaskQueueing": str,
    },
    total=False,
)


class ClientDescribeTaskResponseOptionsTypeDef(
    _ClientDescribeTaskResponseOptionsTypeDef
):
    """
    Type definition for `ClientDescribeTaskResponse` `Options`

    The set of configuration options that control the behavior of a single execution of the task
    that occurs when you call ``StartTaskExecution`` . You can configure these options to
    preserve metadata such as user ID (UID) and group (GID), file permissions, data integrity
    verification, and so on.

    For each individual task execution, you can override these options by specifying the
    overriding ``OverrideOptions`` value to operation.

    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the
      end of a task execution after all data and metadata have been transferred.

      Default value: POINT_IN_TIME_CONSISTENT.

      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

      NONE: Skip verification.

    - **OverwriteMode** *(string) --*

      A value that determines whether files at the destination should be overwritten or preserved
      when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
      file, even if the destination file differs from the source file. If you modify files in the
      destination and you sync the files, you can use this value to protect against overwriting
      those changes.

      Some storage classes have specific behaviors that can affect your S3 storage cost. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

    - **Atime** *(string) --*

      A file metadata value that shows the last time a file was accessed (that is, when the file
      was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve
      the original ``Atime`` attribute on all source files (that is, the version before the
      PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so
      AWS DataSync can only do this on a best-effort basis.

      Default value: BEST_EFFORT.

      BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

      NONE: Ignore ``Atime`` .

      .. note::

        If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

        If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

    - **Mtime** *(string) --*

      A value that indicates the last time that a file was modified (that is, a file was written
      to) before the PREPARING phase.

      Default value: PRESERVE.

      PRESERVE: Preserve original ``Mtime`` (recommended)

      NONE: Ignore ``Mtime`` .

      .. note::

        If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

        If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

    - **Uid** *(string) --*

      The user ID (UID) of the file's owner.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

      NONE: Ignore UID and GID.

    - **Gid** *(string) --*

      The group ID (GID) of the file's owners.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

      NONE: Ignore UID and GID.

    - **PreserveDeletedFiles** *(string) --*

      A value that specifies whether files in the destination that don't exist in the source file
      system should be preserved. This option can affect your storage cost. If your task deletes
      objects, you might incur minimum storage duration charges for certain storage classes. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      Default value: PRESERVE.

      PRESERVE: Ignore such destination files (recommended).

      REMOVE: Delete destination files that aren’t present in the source.

    - **PreserveDevices** *(string) --*

      A value that determines whether AWS DataSync should preserve the metadata of block and
      character devices in the source file system, and recreate the files with that device name
      and metadata on the destination.

      .. note::

        AWS DataSync can't sync the actual contents of such devices, because they are nonterminal
        and don't return an end-of-file (EOF) marker.

      Default value: NONE.

      NONE: Ignore special devices (recommended).

      PRESERVE: Preserve character and block device metadata. This option isn't currently
      supported for Amazon EFS.

    - **PosixPermissions** *(string) --*

      A value that determines which users or groups can access a file for a specific purpose such
      as reading, writing, or execution of the file.

      Default value: PRESERVE.

      PRESERVE: Preserve POSIX-style permissions (recommended).

      NONE: Ignore permissions.

      .. note::

        AWS DataSync can preserve extant permissions of a source location.

    - **BytesPerSecond** *(integer) --*

      A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS
      DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

    - **TaskQueueing** *(string) --*

      A value that determines whether tasks should be queued before executing the tasks. If set
      to ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

      If you use the same agent to run multiple tasks you can enable the tasks to run in series.
      For more information see  task-queue .
    """


_ClientDescribeTaskResponseTypeDef = TypedDict(
    "_ClientDescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": str,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": ClientDescribeTaskResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskResponseExcludesTypeDef],
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeTaskResponseTypeDef(_ClientDescribeTaskResponseTypeDef):
    """
    Type definition for `ClientDescribeTask` `Response`

    DescribeTaskResponse

    - **TaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the task that was described.

    - **Status** *(string) --*

      The status of the task that was described.

      For detailed information about task execution statuses, see Understanding Task Statuses in
      the *AWS DataSync User Guide.*

    - **Name** *(string) --*

      The name of the task that was described.

    - **CurrentTaskExecutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the task execution that is syncing files.

    - **SourceLocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the source file system's location.

    - **DestinationLocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS storage resource's location.

    - **CloudWatchLogGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that was used to monitor
      and log events in the task.

      For more information on these groups, see Working with Log Groups and Log Streams in the
      *Amazon CloudWatch User Guide* .

    - **SourceNetworkInterfaceArns** *(list) --*

      The Amazon Resource Name (ARN) of the source ENIs (Elastic Network Interface) that was
      created for your subnet.

      - *(string) --*

    - **DestinationNetworkInterfaceArns** *(list) --*

      The Amazon Resource Name (ARN) of the destination ENIs (Elastic Network Interface) that was
      created for your subnet.

      - *(string) --*

    - **Options** *(dict) --*

      The set of configuration options that control the behavior of a single execution of the task
      that occurs when you call ``StartTaskExecution`` . You can configure these options to
      preserve metadata such as user ID (UID) and group (GID), file permissions, data integrity
      verification, and so on.

      For each individual task execution, you can override these options by specifying the
      overriding ``OverrideOptions`` value to operation.

      - **VerifyMode** *(string) --*

        A value that determines whether a data integrity verification should be performed at the
        end of a task execution after all data and metadata have been transferred.

        Default value: POINT_IN_TIME_CONSISTENT.

        POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

        ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

        NONE: Skip verification.

      - **OverwriteMode** *(string) --*

        A value that determines whether files at the destination should be overwritten or preserved
        when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
        file, even if the destination file differs from the source file. If you modify files in the
        destination and you sync the files, you can use this value to protect against overwriting
        those changes.

        Some storage classes have specific behaviors that can affect your S3 storage cost. For
        detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      - **Atime** *(string) --*

        A file metadata value that shows the last time a file was accessed (that is, when the file
        was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve
        the original ``Atime`` attribute on all source files (that is, the version before the
        PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so
        AWS DataSync can only do this on a best-effort basis.

        Default value: BEST_EFFORT.

        BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

        NONE: Ignore ``Atime`` .

        .. note::

          If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

          If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

      - **Mtime** *(string) --*

        A value that indicates the last time that a file was modified (that is, a file was written
        to) before the PREPARING phase.

        Default value: PRESERVE.

        PRESERVE: Preserve original ``Mtime`` (recommended)

        NONE: Ignore ``Mtime`` .

        .. note::

          If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

          If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

      - **Uid** *(string) --*

        The user ID (UID) of the file's owner.

        Default value: INT_VALUE. This preserves the integer value of the ID.

        INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

        NONE: Ignore UID and GID.

      - **Gid** *(string) --*

        The group ID (GID) of the file's owners.

        Default value: INT_VALUE. This preserves the integer value of the ID.

        INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

        NONE: Ignore UID and GID.

      - **PreserveDeletedFiles** *(string) --*

        A value that specifies whether files in the destination that don't exist in the source file
        system should be preserved. This option can affect your storage cost. If your task deletes
        objects, you might incur minimum storage duration charges for certain storage classes. For
        detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

        Default value: PRESERVE.

        PRESERVE: Ignore such destination files (recommended).

        REMOVE: Delete destination files that aren’t present in the source.

      - **PreserveDevices** *(string) --*

        A value that determines whether AWS DataSync should preserve the metadata of block and
        character devices in the source file system, and recreate the files with that device name
        and metadata on the destination.

        .. note::

          AWS DataSync can't sync the actual contents of such devices, because they are nonterminal
          and don't return an end-of-file (EOF) marker.

        Default value: NONE.

        NONE: Ignore special devices (recommended).

        PRESERVE: Preserve character and block device metadata. This option isn't currently
        supported for Amazon EFS.

      - **PosixPermissions** *(string) --*

        A value that determines which users or groups can access a file for a specific purpose such
        as reading, writing, or execution of the file.

        Default value: PRESERVE.

        PRESERVE: Preserve POSIX-style permissions (recommended).

        NONE: Ignore permissions.

        .. note::

          AWS DataSync can preserve extant permissions of a source location.

      - **BytesPerSecond** *(integer) --*

        A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS
        DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

      - **TaskQueueing** *(string) --*

        A value that determines whether tasks should be queued before executing the tasks. If set
        to ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

        If you use the same agent to run multiple tasks you can enable the tasks to run in series.
        For more information see  task-queue .

    - **Excludes** *(list) --*

      A list of filter rules that determines which files to exclude from a task. The list should
      contain a single filter string that consists of the patterns to exclude. The patterns are
      delimited by "|" (that is, a pipe), for example: ``"/folder1|/folder2"``

      - *(dict) --*

        Specifies which files, folders and objects to include or exclude when transferring files
        from source to destination.

        - **FilterType** *(string) --*

          The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

        - **Value** *(string) --*

          A single filter string that consists of the patterns to include or exclude. The patterns
          are delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``

    - **ErrorCode** *(string) --*

      Errors that AWS DataSync encountered during execution of the task. You can use this error
      code to help troubleshoot issues.

    - **ErrorDetail** *(string) --*

      Detailed description of an error that was encountered during the task execution. You can use
      this information to help troubleshoot issues.

    - **CreationTime** *(datetime) --*

      The time that the task was created.
    """


_ClientListAgentsResponseAgentsTypeDef = TypedDict(
    "_ClientListAgentsResponseAgentsTypeDef",
    {"AgentArn": str, "Name": str, "Status": str},
    total=False,
)


class ClientListAgentsResponseAgentsTypeDef(_ClientListAgentsResponseAgentsTypeDef):
    """
    Type definition for `ClientListAgentsResponse` `Agents`

    Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
    contains a list of agents when the  ListAgents operation is called.

    - **AgentArn** *(string) --*

      The Amazon Resource Name (ARN) of the agent.

    - **Name** *(string) --*

      The name of the agent.

    - **Status** *(string) --*

      The status of the agent.
    """


_ClientListAgentsResponseTypeDef = TypedDict(
    "_ClientListAgentsResponseTypeDef",
    {"Agents": List[ClientListAgentsResponseAgentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAgentsResponseTypeDef(_ClientListAgentsResponseTypeDef):
    """
    Type definition for `ClientListAgents` `Response`

    ListAgentsResponse

    - **Agents** *(list) --*

      A list of agents in your account.

      - *(dict) --*

        Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
        contains a list of agents when the  ListAgents operation is called.

        - **AgentArn** *(string) --*

          The Amazon Resource Name (ARN) of the agent.

        - **Name** *(string) --*

          The name of the agent.

        - **Status** *(string) --*

          The status of the agent.

    - **NextToken** *(string) --*

      An opaque string that indicates the position at which to begin returning the next list of
      agents.
    """


_ClientListLocationsResponseLocationsTypeDef = TypedDict(
    "_ClientListLocationsResponseLocationsTypeDef",
    {"LocationArn": str, "LocationUri": str},
    total=False,
)


class ClientListLocationsResponseLocationsTypeDef(
    _ClientListLocationsResponseLocationsTypeDef
):
    """
    Type definition for `ClientListLocationsResponse` `Locations`

    Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
    that contains a list of locations when the  ListLocations operation is called.

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
      EFS, the location is the export path. For Amazon S3, the location is the prefix path that
      you want to mount and use as the root of the location.

    - **LocationUri** *(string) --*

      Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a
      list of locations when the  ListLocations operation is called.

      Format: ``TYPE://GLOBAL_ID/SUBDIR`` .

      TYPE designates the type of location. Valid values: NFS | EFS | S3.

      GLOBAL_ID is the globally unique identifier of the resource that backs the location. An
      example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket
      name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name
      compliant with Domain Name Service (DNS).

      SUBDIR is a valid file system path, delimited by forward slashes as is the *nix
      convention. For NFS and Amazon EFS, it's the export path to mount the location. For
      Amazon S3, it's the prefix path that you mount to and treat as the root of the location.
    """


_ClientListLocationsResponseTypeDef = TypedDict(
    "_ClientListLocationsResponseTypeDef",
    {"Locations": List[ClientListLocationsResponseLocationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListLocationsResponseTypeDef(_ClientListLocationsResponseTypeDef):
    """
    Type definition for `ClientListLocations` `Response`

    ListLocationsResponse

    - **Locations** *(list) --*

      An array that contains a list of locations.

      - *(dict) --*

        Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
        that contains a list of locations when the  ListLocations operation is called.

        - **LocationArn** *(string) --*

          The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
          EFS, the location is the export path. For Amazon S3, the location is the prefix path that
          you want to mount and use as the root of the location.

        - **LocationUri** *(string) --*

          Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a
          list of locations when the  ListLocations operation is called.

          Format: ``TYPE://GLOBAL_ID/SUBDIR`` .

          TYPE designates the type of location. Valid values: NFS | EFS | S3.

          GLOBAL_ID is the globally unique identifier of the resource that backs the location. An
          example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket
          name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name
          compliant with Domain Name Service (DNS).

          SUBDIR is a valid file system path, delimited by forward slashes as is the *nix
          convention. For NFS and Amazon EFS, it's the export path to mount the location. For
          Amazon S3, it's the prefix path that you mount to and treat as the root of the location.

    - **NextToken** *(string) --*

      An opaque string that indicates the position at which to begin returning the next list of
      locations.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --*

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    ListTagsForResourceResponse

    - **Tags** *(list) --*

      Array of resource tags.

      - *(dict) --*

        Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
        that contains a list of tasks when the  ListTagsForResource operation is called.

        - **Key** *(string) --*

          The key for an AWS resource tag.

        - **Value** *(string) --*

          The value for an AWS resource tag.

    - **NextToken** *(string) --*

      An opaque string that indicates the position at which to begin returning the next list of
      resource tags.
    """


_ClientListTaskExecutionsResponseTaskExecutionsTypeDef = TypedDict(
    "_ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    {"TaskExecutionArn": str, "Status": str},
    total=False,
)


class ClientListTaskExecutionsResponseTaskExecutionsTypeDef(
    _ClientListTaskExecutionsResponseTaskExecutionsTypeDef
):
    """
    Type definition for `ClientListTaskExecutionsResponse` `TaskExecutions`

    Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
    an array that contains a list of specific invocations of a task when  ListTaskExecutions
    operation is called.

    - **TaskExecutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the task that was executed.

    - **Status** *(string) --*

      The status of a task execution.
    """


_ClientListTaskExecutionsResponseTypeDef = TypedDict(
    "_ClientListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List[ClientListTaskExecutionsResponseTaskExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTaskExecutionsResponseTypeDef(_ClientListTaskExecutionsResponseTypeDef):
    """
    Type definition for `ClientListTaskExecutions` `Response`

    ListTaskExecutionsResponse

    - **TaskExecutions** *(list) --*

      A list of executed tasks.

      - *(dict) --*

        Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
        an array that contains a list of specific invocations of a task when  ListTaskExecutions
        operation is called.

        - **TaskExecutionArn** *(string) --*

          The Amazon Resource Name (ARN) of the task that was executed.

        - **Status** *(string) --*

          The status of a task execution.

    - **NextToken** *(string) --*

      An opaque string that indicates the position at which to begin returning the next list of
      executed tasks.
    """


_ClientListTasksResponseTasksTypeDef = TypedDict(
    "_ClientListTasksResponseTasksTypeDef",
    {"TaskArn": str, "Status": str, "Name": str},
    total=False,
)


class ClientListTasksResponseTasksTypeDef(_ClientListTasksResponseTasksTypeDef):
    """
    Type definition for `ClientListTasksResponse` `Tasks`

    Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
    contains a list of tasks when the  ListTasks operation is called. A task includes the
    source and destination file systems to sync and the options to use for the tasks.

    - **TaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the task.

    - **Status** *(string) --*

      The status of the task.

    - **Name** *(string) --*

      The name of the task.
    """


_ClientListTasksResponseTypeDef = TypedDict(
    "_ClientListTasksResponseTypeDef",
    {"Tasks": List[ClientListTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)


class ClientListTasksResponseTypeDef(_ClientListTasksResponseTypeDef):
    """
    Type definition for `ClientListTasks` `Response`

    ListTasksResponse

    - **Tasks** *(list) --*

      A list of all the tasks that are returned.

      - *(dict) --*

        Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
        contains a list of tasks when the  ListTasks operation is called. A task includes the
        source and destination file systems to sync and the options to use for the tasks.

        - **TaskArn** *(string) --*

          The Amazon Resource Name (ARN) of the task.

        - **Status** *(string) --*

          The status of the task.

        - **Name** *(string) --*

          The name of the task.

    - **NextToken** *(string) --*

      An opaque string that indicates the position at which to begin returning the next list of
      tasks.
    """


_ClientStartTaskExecutionIncludesTypeDef = TypedDict(
    "_ClientStartTaskExecutionIncludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientStartTaskExecutionIncludesTypeDef(_ClientStartTaskExecutionIncludesTypeDef):
    """
    Type definition for `ClientStartTaskExecution` `Includes`

    Specifies which files, folders and objects to include or exclude when transferring files from
    source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns are
      delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientStartTaskExecutionOverrideOptionsTypeDef = TypedDict(
    "_ClientStartTaskExecutionOverrideOptionsTypeDef",
    {
        "VerifyMode": str,
        "OverwriteMode": str,
        "Atime": str,
        "Mtime": str,
        "Uid": str,
        "Gid": str,
        "PreserveDeletedFiles": str,
        "PreserveDevices": str,
        "PosixPermissions": str,
        "BytesPerSecond": int,
        "TaskQueueing": str,
    },
    total=False,
)


class ClientStartTaskExecutionOverrideOptionsTypeDef(
    _ClientStartTaskExecutionOverrideOptionsTypeDef
):
    """
    Type definition for `ClientStartTaskExecution` `OverrideOptions`

    Represents the options that are available to control the behavior of a  StartTaskExecution
    operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file
    permissions, and also overwriting files in the destination, data integrity verification, and so
    on.

    A task has a set of default options associated with it. If you don't specify an option in
    StartTaskExecution , the default value is used. You can override the defaults options on each
    task execution by specifying an overriding ``Options`` value to  StartTaskExecution .

    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end of
      a task execution after all data and metadata have been transferred.

      Default value: POINT_IN_TIME_CONSISTENT.

      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

      NONE: Skip verification.

    - **OverwriteMode** *(string) --*

      A value that determines whether files at the destination should be overwritten or preserved
      when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
      file, even if the destination file differs from the source file. If you modify files in the
      destination and you sync the files, you can use this value to protect against overwriting those
      changes.

      Some storage classes have specific behaviors that can affect your S3 storage cost. For detailed
      information, see  using-storage-classes in the *AWS DataSync User Guide* .

    - **Atime** *(string) --*

      A file metadata value that shows the last time a file was accessed (that is, when the file was
      read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the
      original ``Atime`` attribute on all source files (that is, the version before the PREPARING
      phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync
      can only do this on a best-effort basis.

      Default value: BEST_EFFORT.

      BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

      NONE: Ignore ``Atime`` .

      .. note::

        If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

        If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

    - **Mtime** *(string) --*

      A value that indicates the last time that a file was modified (that is, a file was written to)
      before the PREPARING phase.

      Default value: PRESERVE.

      PRESERVE: Preserve original ``Mtime`` (recommended)

      NONE: Ignore ``Mtime`` .

      .. note::

        If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

        If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

    - **Uid** *(string) --*

      The user ID (UID) of the file's owner.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

      NONE: Ignore UID and GID.

    - **Gid** *(string) --*

      The group ID (GID) of the file's owners.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

      NONE: Ignore UID and GID.

    - **PreserveDeletedFiles** *(string) --*

      A value that specifies whether files in the destination that don't exist in the source file
      system should be preserved. This option can affect your storage cost. If your task deletes
      objects, you might incur minimum storage duration charges for certain storage classes. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      Default value: PRESERVE.

      PRESERVE: Ignore such destination files (recommended).

      REMOVE: Delete destination files that aren’t present in the source.

    - **PreserveDevices** *(string) --*

      A value that determines whether AWS DataSync should preserve the metadata of block and
      character devices in the source file system, and recreate the files with that device name and
      metadata on the destination.

      .. note::

        AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and
        don't return an end-of-file (EOF) marker.

      Default value: NONE.

      NONE: Ignore special devices (recommended).

      PRESERVE: Preserve character and block device metadata. This option isn't currently supported
      for Amazon EFS.

    - **PosixPermissions** *(string) --*

      A value that determines which users or groups can access a file for a specific purpose such as
      reading, writing, or execution of the file.

      Default value: PRESERVE.

      PRESERVE: Preserve POSIX-style permissions (recommended).

      NONE: Ignore permissions.

      .. note::

        AWS DataSync can preserve extant permissions of a source location.

    - **BytesPerSecond** *(integer) --*

      A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync
      to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

    - **TaskQueueing** *(string) --*

      A value that determines whether tasks should be queued before executing the tasks. If set to
      ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

      If you use the same agent to run multiple tasks you can enable the tasks to run in series. For
      more information see  task-queue .
    """


_ClientStartTaskExecutionResponseTypeDef = TypedDict(
    "_ClientStartTaskExecutionResponseTypeDef", {"TaskExecutionArn": str}, total=False
)


class ClientStartTaskExecutionResponseTypeDef(_ClientStartTaskExecutionResponseTypeDef):
    """
    Type definition for `ClientStartTaskExecution` `Response`

    StartTaskExecutionResponse

    - **TaskExecutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the specific task execution that was started.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    Type definition for `ClientTagResource` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --* **[REQUIRED]**

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ClientUpdateTaskExcludesTypeDef = TypedDict(
    "_ClientUpdateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientUpdateTaskExcludesTypeDef(_ClientUpdateTaskExcludesTypeDef):
    """
    Type definition for `ClientUpdateTask` `Excludes`

    Specifies which files, folders and objects to include or exclude when transferring files from
    source to destination.

    - **FilterType** *(string) --*

      The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

    - **Value** *(string) --*

      A single filter string that consists of the patterns to include or exclude. The patterns are
      delimited by "|" (that is, a pipe), for example: ``/folder1|/folder2``
    """


_ClientUpdateTaskOptionsTypeDef = TypedDict(
    "_ClientUpdateTaskOptionsTypeDef",
    {
        "VerifyMode": str,
        "OverwriteMode": str,
        "Atime": str,
        "Mtime": str,
        "Uid": str,
        "Gid": str,
        "PreserveDeletedFiles": str,
        "PreserveDevices": str,
        "PosixPermissions": str,
        "BytesPerSecond": int,
        "TaskQueueing": str,
    },
    total=False,
)


class ClientUpdateTaskOptionsTypeDef(_ClientUpdateTaskOptionsTypeDef):
    """
    Type definition for `ClientUpdateTask` `Options`

    Represents the options that are available to control the behavior of a  StartTaskExecution
    operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file
    permissions, and also overwriting files in the destination, data integrity verification, and so
    on.

    A task has a set of default options associated with it. If you don't specify an option in
    StartTaskExecution , the default value is used. You can override the defaults options on each
    task execution by specifying an overriding ``Options`` value to  StartTaskExecution .

    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end of
      a task execution after all data and metadata have been transferred.

      Default value: POINT_IN_TIME_CONSISTENT.

      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).

      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.

      NONE: Skip verification.

    - **OverwriteMode** *(string) --*

      A value that determines whether files at the destination should be overwritten or preserved
      when copying files. If set to ``NEVER`` a destination file will not be replaced by a source
      file, even if the destination file differs from the source file. If you modify files in the
      destination and you sync the files, you can use this value to protect against overwriting those
      changes.

      Some storage classes have specific behaviors that can affect your S3 storage cost. For detailed
      information, see  using-storage-classes in the *AWS DataSync User Guide* .

    - **Atime** *(string) --*

      A file metadata value that shows the last time a file was accessed (that is, when the file was
      read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the
      original ``Atime`` attribute on all source files (that is, the version before the PREPARING
      phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync
      can only do this on a best-effort basis.

      Default value: BEST_EFFORT.

      BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).

      NONE: Ignore ``Atime`` .

      .. note::

        If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.

        If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.

    - **Mtime** *(string) --*

      A value that indicates the last time that a file was modified (that is, a file was written to)
      before the PREPARING phase.

      Default value: PRESERVE.

      PRESERVE: Preserve original ``Mtime`` (recommended)

      NONE: Ignore ``Mtime`` .

      .. note::

        If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.

        If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.

    - **Uid** *(string) --*

      The user ID (UID) of the file's owner.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).

      NONE: Ignore UID and GID.

    - **Gid** *(string) --*

      The group ID (GID) of the file's owners.

      Default value: INT_VALUE. This preserves the integer value of the ID.

      INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).

      NONE: Ignore UID and GID.

    - **PreserveDeletedFiles** *(string) --*

      A value that specifies whether files in the destination that don't exist in the source file
      system should be preserved. This option can affect your storage cost. If your task deletes
      objects, you might incur minimum storage duration charges for certain storage classes. For
      detailed information, see  using-storage-classes in the *AWS DataSync User Guide* .

      Default value: PRESERVE.

      PRESERVE: Ignore such destination files (recommended).

      REMOVE: Delete destination files that aren’t present in the source.

    - **PreserveDevices** *(string) --*

      A value that determines whether AWS DataSync should preserve the metadata of block and
      character devices in the source file system, and recreate the files with that device name and
      metadata on the destination.

      .. note::

        AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and
        don't return an end-of-file (EOF) marker.

      Default value: NONE.

      NONE: Ignore special devices (recommended).

      PRESERVE: Preserve character and block device metadata. This option isn't currently supported
      for Amazon EFS.

    - **PosixPermissions** *(string) --*

      A value that determines which users or groups can access a file for a specific purpose such as
      reading, writing, or execution of the file.

      Default value: PRESERVE.

      PRESERVE: Preserve POSIX-style permissions (recommended).

      NONE: Ignore permissions.

      .. note::

        AWS DataSync can preserve extant permissions of a source location.

    - **BytesPerSecond** *(integer) --*

      A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync
      to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).

    - **TaskQueueing** *(string) --*

      A value that determines whether tasks should be queued before executing the tasks. If set to
      ``Enabled`` , the tasks will queued. The default is ``Enabled`` .

      If you use the same agent to run multiple tasks you can enable the tasks to run in series. For
      more information see  task-queue .
    """


_ListAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAgentsPaginatePaginationConfigTypeDef(
    _ListAgentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAgentsPaginate` `PaginationConfig`

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


_ListAgentsPaginateResponseAgentsTypeDef = TypedDict(
    "_ListAgentsPaginateResponseAgentsTypeDef",
    {"AgentArn": str, "Name": str, "Status": str},
    total=False,
)


class ListAgentsPaginateResponseAgentsTypeDef(_ListAgentsPaginateResponseAgentsTypeDef):
    """
    Type definition for `ListAgentsPaginateResponse` `Agents`

    Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
    contains a list of agents when the  ListAgents operation is called.

    - **AgentArn** *(string) --*

      The Amazon Resource Name (ARN) of the agent.

    - **Name** *(string) --*

      The name of the agent.

    - **Status** *(string) --*

      The status of the agent.
    """


_ListAgentsPaginateResponseTypeDef = TypedDict(
    "_ListAgentsPaginateResponseTypeDef",
    {"Agents": List[ListAgentsPaginateResponseAgentsTypeDef]},
    total=False,
)


class ListAgentsPaginateResponseTypeDef(_ListAgentsPaginateResponseTypeDef):
    """
    Type definition for `ListAgentsPaginate` `Response`

    ListAgentsResponse

    - **Agents** *(list) --*

      A list of agents in your account.

      - *(dict) --*

        Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
        contains a list of agents when the  ListAgents operation is called.

        - **AgentArn** *(string) --*

          The Amazon Resource Name (ARN) of the agent.

        - **Name** *(string) --*

          The name of the agent.

        - **Status** *(string) --*

          The status of the agent.
    """


_ListLocationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLocationsPaginatePaginationConfigTypeDef(
    _ListLocationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLocationsPaginate` `PaginationConfig`

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


_ListLocationsPaginateResponseLocationsTypeDef = TypedDict(
    "_ListLocationsPaginateResponseLocationsTypeDef",
    {"LocationArn": str, "LocationUri": str},
    total=False,
)


class ListLocationsPaginateResponseLocationsTypeDef(
    _ListLocationsPaginateResponseLocationsTypeDef
):
    """
    Type definition for `ListLocationsPaginateResponse` `Locations`

    Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
    that contains a list of locations when the  ListLocations operation is called.

    - **LocationArn** *(string) --*

      The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
      EFS, the location is the export path. For Amazon S3, the location is the prefix path that
      you want to mount and use as the root of the location.

    - **LocationUri** *(string) --*

      Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a
      list of locations when the  ListLocations operation is called.

      Format: ``TYPE://GLOBAL_ID/SUBDIR`` .

      TYPE designates the type of location. Valid values: NFS | EFS | S3.

      GLOBAL_ID is the globally unique identifier of the resource that backs the location. An
      example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket
      name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name
      compliant with Domain Name Service (DNS).

      SUBDIR is a valid file system path, delimited by forward slashes as is the *nix
      convention. For NFS and Amazon EFS, it's the export path to mount the location. For
      Amazon S3, it's the prefix path that you mount to and treat as the root of the location.
    """


_ListLocationsPaginateResponseTypeDef = TypedDict(
    "_ListLocationsPaginateResponseTypeDef",
    {"Locations": List[ListLocationsPaginateResponseLocationsTypeDef]},
    total=False,
)


class ListLocationsPaginateResponseTypeDef(_ListLocationsPaginateResponseTypeDef):
    """
    Type definition for `ListLocationsPaginate` `Response`

    ListLocationsResponse

    - **Locations** *(list) --*

      An array that contains a list of locations.

      - *(dict) --*

        Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
        that contains a list of locations when the  ListLocations operation is called.

        - **LocationArn** *(string) --*

          The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
          EFS, the location is the export path. For Amazon S3, the location is the prefix path that
          you want to mount and use as the root of the location.

        - **LocationUri** *(string) --*

          Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a
          list of locations when the  ListLocations operation is called.

          Format: ``TYPE://GLOBAL_ID/SUBDIR`` .

          TYPE designates the type of location. Valid values: NFS | EFS | S3.

          GLOBAL_ID is the globally unique identifier of the resource that backs the location. An
          example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket
          name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name
          compliant with Domain Name Service (DNS).

          SUBDIR is a valid file system path, delimited by forward slashes as is the *nix
          convention. For NFS and Amazon EFS, it's the export path to mount the location. For
          Amazon S3, it's the prefix path that you mount to and treat as the root of the location.
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


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

    Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
    that contains a list of tasks when the  ListTagsForResource operation is called.

    - **Key** *(string) --*

      The key for an AWS resource tag.

    - **Value** *(string) --*

      The value for an AWS resource tag.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    ListTagsForResourceResponse

    - **Tags** *(list) --*

      Array of resource tags.

      - *(dict) --*

        Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
        that contains a list of tasks when the  ListTagsForResource operation is called.

        - **Key** *(string) --*

          The key for an AWS resource tag.

        - **Value** *(string) --*

          The value for an AWS resource tag.
    """


_ListTaskExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTaskExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTaskExecutionsPaginatePaginationConfigTypeDef(
    _ListTaskExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTaskExecutionsPaginate` `PaginationConfig`

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


_ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef = TypedDict(
    "_ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef",
    {"TaskExecutionArn": str, "Status": str},
    total=False,
)


class ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef(
    _ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef
):
    """
    Type definition for `ListTaskExecutionsPaginateResponse` `TaskExecutions`

    Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
    an array that contains a list of specific invocations of a task when  ListTaskExecutions
    operation is called.

    - **TaskExecutionArn** *(string) --*

      The Amazon Resource Name (ARN) of the task that was executed.

    - **Status** *(string) --*

      The status of a task execution.
    """


_ListTaskExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListTaskExecutionsPaginateResponseTypeDef",
    {"TaskExecutions": List[ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef]},
    total=False,
)


class ListTaskExecutionsPaginateResponseTypeDef(
    _ListTaskExecutionsPaginateResponseTypeDef
):
    """
    Type definition for `ListTaskExecutionsPaginate` `Response`

    ListTaskExecutionsResponse

    - **TaskExecutions** *(list) --*

      A list of executed tasks.

      - *(dict) --*

        Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
        an array that contains a list of specific invocations of a task when  ListTaskExecutions
        operation is called.

        - **TaskExecutionArn** *(string) --*

          The Amazon Resource Name (ARN) of the task that was executed.

        - **Status** *(string) --*

          The status of a task execution.
    """


_ListTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTasksPaginatePaginationConfigTypeDef(
    _ListTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTasksPaginate` `PaginationConfig`

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


_ListTasksPaginateResponseTasksTypeDef = TypedDict(
    "_ListTasksPaginateResponseTasksTypeDef",
    {"TaskArn": str, "Status": str, "Name": str},
    total=False,
)


class ListTasksPaginateResponseTasksTypeDef(_ListTasksPaginateResponseTasksTypeDef):
    """
    Type definition for `ListTasksPaginateResponse` `Tasks`

    Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
    contains a list of tasks when the  ListTasks operation is called. A task includes the
    source and destination file systems to sync and the options to use for the tasks.

    - **TaskArn** *(string) --*

      The Amazon Resource Name (ARN) of the task.

    - **Status** *(string) --*

      The status of the task.

    - **Name** *(string) --*

      The name of the task.
    """


_ListTasksPaginateResponseTypeDef = TypedDict(
    "_ListTasksPaginateResponseTypeDef",
    {"Tasks": List[ListTasksPaginateResponseTasksTypeDef]},
    total=False,
)


class ListTasksPaginateResponseTypeDef(_ListTasksPaginateResponseTypeDef):
    """
    Type definition for `ListTasksPaginate` `Response`

    ListTasksResponse

    - **Tasks** *(list) --*

      A list of all the tasks that are returned.

      - *(dict) --*

        Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
        contains a list of tasks when the  ListTasks operation is called. A task includes the
        source and destination file systems to sync and the options to use for the tasks.

        - **TaskArn** *(string) --*

          The Amazon Resource Name (ARN) of the task.

        - **Status** *(string) --*

          The status of the task.

        - **Name** *(string) --*

          The name of the task.
    """
