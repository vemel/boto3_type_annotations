"Main interface for efs type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateFileSystemResponseSizeInBytesTypeDef",
    "ClientCreateFileSystemResponseTagsTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateMountTargetResponseTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientDescribeLifecycleConfigurationResponseTypeDef",
    "ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    "ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    "ClientDescribeMountTargetsResponseTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseTypeDef",
    "ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    "ClientUpdateFileSystemResponseTagsTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    "DescribeFileSystemsPaginateResponseTypeDef",
    "DescribeMountTargetsPaginatePaginationConfigTypeDef",
    "DescribeMountTargetsPaginateResponseMountTargetsTypeDef",
    "DescribeMountTargetsPaginateResponseTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponseTagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
)


_ClientCreateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientCreateFileSystemResponseSizeInBytesTypeDef(
    _ClientCreateFileSystemResponseSizeInBytesTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponse` `SizeInBytes`

    The latest known metered size (in bytes) of data stored in the file system, in its ``Value``
    field, and the time at which that size was determined in its ``Timestamp`` field. The
    ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The
    ``SizeInBytes`` value doesn't represent the size of a consistent snapshot of the file system,
    but it is eventually consistent when there are no writes to the file system. That is,
    ``SizeInBytes`` represents actual size only if the file system is not modified for a period
    longer than a couple of hours. Otherwise, the value is not the exact size that the file
    system was at any point in time.

    - **Value** *(integer) --*

      The latest known metered size (in bytes) of data stored in the file system.

    - **Timestamp** *(datetime) --*

      The time at which the size of data, returned in the ``Value`` field, was determined. The
      value is the integer number of seconds since 1970-01-01T00:00:00Z.

    - **ValueInIA** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Infrequent Access storage
      class.

    - **ValueInStandard** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Standard storage class.
    """


_ClientCreateFileSystemResponseTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateFileSystemResponseTagsTypeDef(
    _ClientCreateFileSystemResponseTagsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponse` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
    can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_ClientCreateFileSystemResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": str,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientCreateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": str,
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientCreateFileSystemResponseTagsTypeDef],
    },
    total=False,
)


class ClientCreateFileSystemResponseTypeDef(_ClientCreateFileSystemResponseTypeDef):
    """
    Type definition for `ClientCreateFileSystem` `Response`

    A description of the file system.

    - **OwnerId** *(string) --*

      The AWS account that created the file system. If the file system was created by an IAM user,
      the parent account to which the user belongs is the owner.

    - **CreationToken** *(string) --*

      The opaque string specified in the request.

    - **FileSystemId** *(string) --*

      The ID of the file system, assigned by Amazon EFS.

    - **CreationTime** *(datetime) --*

      The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

    - **LifeCycleState** *(string) --*

      The lifecycle phase of the file system.

    - **Name** *(string) --*

      You can add tags to a file system, including a ``Name`` tag. For more information, see
      CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
      this field.

    - **NumberOfMountTargets** *(integer) --*

      The current number of mount targets that the file system has. For more information, see
      CreateMountTarget .

    - **SizeInBytes** *(dict) --*

      The latest known metered size (in bytes) of data stored in the file system, in its ``Value``
      field, and the time at which that size was determined in its ``Timestamp`` field. The
      ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The
      ``SizeInBytes`` value doesn't represent the size of a consistent snapshot of the file system,
      but it is eventually consistent when there are no writes to the file system. That is,
      ``SizeInBytes`` represents actual size only if the file system is not modified for a period
      longer than a couple of hours. Otherwise, the value is not the exact size that the file
      system was at any point in time.

      - **Value** *(integer) --*

        The latest known metered size (in bytes) of data stored in the file system.

      - **Timestamp** *(datetime) --*

        The time at which the size of data, returned in the ``Value`` field, was determined. The
        value is the integer number of seconds since 1970-01-01T00:00:00Z.

      - **ValueInIA** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Infrequent Access storage
        class.

      - **ValueInStandard** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Standard storage class.

    - **PerformanceMode** *(string) --*

      The performance mode of the file system.

    - **Encrypted** *(boolean) --*

      A Boolean value that, if true, indicates that the file system is encrypted.

    - **KmsKeyId** *(string) --*

      The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to
      protect the encrypted file system.

    - **ThroughputMode** *(string) --*

      The throughput mode for a file system. There are two throughput modes to choose from for your
      file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
      ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You can
      decrease your file system's throughput in Provisioned Throughput mode or change between the
      throughput modes as long as it’s been more than 24 hours since the last decrease or
      throughput mode change.

    - **ProvisionedThroughputInMibps** *(float) --*

      The throughput, measured in MiB/s, that you want to provision for a file system. Valid values
      are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit on
      throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For
      more information, see `Amazon EFS Limits That You Can Increase
      <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
      User Guide.*

    - **Tags** *(list) --*

      The tags associated with the file system, presented as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
        can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.
    """


_ClientCreateFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateFileSystemTagsTypeDef(_ClientCreateFileSystemTagsTypeDef):
    """
    Type definition for `ClientCreateFileSystem` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be
    represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --* **[REQUIRED]**

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag key.
    """


_ClientCreateMountTargetResponseTypeDef = TypedDict(
    "_ClientCreateMountTargetResponseTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)


class ClientCreateMountTargetResponseTypeDef(_ClientCreateMountTargetResponseTypeDef):
    """
    Type definition for `ClientCreateMountTarget` `Response`

    Provides a description of a mount target.

    - **OwnerId** *(string) --*

      AWS account ID that owns the resource.

    - **MountTargetId** *(string) --*

      System-assigned mount target ID.

    - **FileSystemId** *(string) --*

      The ID of the file system for which the mount target is intended.

    - **SubnetId** *(string) --*

      The ID of the mount target's subnet.

    - **LifeCycleState** *(string) --*

      Lifecycle state of the mount target.

    - **IpAddress** *(string) --*

      Address at which the file system can be mounted by using the mount target.

    - **NetworkInterfaceId** *(string) --*

      The ID of the network interface that Amazon EFS created when it created the mount target.
    """


_ClientCreateTagsTagsTypeDef = TypedDict(
    "_ClientCreateTagsTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateTagsTagsTypeDef(_ClientCreateTagsTagsTypeDef):
    """
    Type definition for `ClientCreateTags` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be
    represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --* **[REQUIRED]**

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --* **[REQUIRED]**

      The value of the tag key.
    """


_ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `SizeInBytes`

    The latest known metered size (in bytes) of data stored in the file system, in its
    ``Value`` field, and the time at which that size was determined in its ``Timestamp``
    field. The ``Timestamp`` value is the integer number of seconds since
    1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
    consistent snapshot of the file system, but it is eventually consistent when there are no
    writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
    file system is not modified for a period longer than a couple of hours. Otherwise, the
    value is not the exact size that the file system was at any point in time.

    - **Value** *(integer) --*

      The latest known metered size (in bytes) of data stored in the file system.

    - **Timestamp** *(datetime) --*

      The time at which the size of data, returned in the ``Value`` field, was determined.
      The value is the integer number of seconds since 1970-01-01T00:00:00Z.

    - **ValueInIA** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Infrequent Access
      storage class.

    - **ValueInStandard** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Standard storage class.
    """


_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers
    that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": str,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef,
        "PerformanceMode": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": str,
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponse` `FileSystems`

    A description of the file system.

    - **OwnerId** *(string) --*

      The AWS account that created the file system. If the file system was created by an IAM
      user, the parent account to which the user belongs is the owner.

    - **CreationToken** *(string) --*

      The opaque string specified in the request.

    - **FileSystemId** *(string) --*

      The ID of the file system, assigned by Amazon EFS.

    - **CreationTime** *(datetime) --*

      The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

    - **LifeCycleState** *(string) --*

      The lifecycle phase of the file system.

    - **Name** *(string) --*

      You can add tags to a file system, including a ``Name`` tag. For more information, see
      CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
      this field.

    - **NumberOfMountTargets** *(integer) --*

      The current number of mount targets that the file system has. For more information, see
      CreateMountTarget .

    - **SizeInBytes** *(dict) --*

      The latest known metered size (in bytes) of data stored in the file system, in its
      ``Value`` field, and the time at which that size was determined in its ``Timestamp``
      field. The ``Timestamp`` value is the integer number of seconds since
      1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
      consistent snapshot of the file system, but it is eventually consistent when there are no
      writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
      file system is not modified for a period longer than a couple of hours. Otherwise, the
      value is not the exact size that the file system was at any point in time.

      - **Value** *(integer) --*

        The latest known metered size (in bytes) of data stored in the file system.

      - **Timestamp** *(datetime) --*

        The time at which the size of data, returned in the ``Value`` field, was determined.
        The value is the integer number of seconds since 1970-01-01T00:00:00Z.

      - **ValueInIA** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Infrequent Access
        storage class.

      - **ValueInStandard** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Standard storage class.

    - **PerformanceMode** *(string) --*

      The performance mode of the file system.

    - **Encrypted** *(boolean) --*

      A Boolean value that, if true, indicates that the file system is encrypted.

    - **KmsKeyId** *(string) --*

      The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used
      to protect the encrypted file system.

    - **ThroughputMode** *(string) --*

      The throughput mode for a file system. There are two throughput modes to choose from for
      your file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
      ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You
      can decrease your file system's throughput in Provisioned Throughput mode or change
      between the throughput modes as long as it’s been more than 24 hours since the last
      decrease or throughput mode change.

    - **ProvisionedThroughputInMibps** *(float) --*

      The throughput, measured in MiB/s, that you want to provision for a file system. Valid
      values are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit
      on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS
      Support. For more information, see `Amazon EFS Limits That You Can Increase
      <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
      User Guide.*

    - **Tags** *(list) --*

      The tags associated with the file system, presented as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers
        that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.
    """


_ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseTypeDef(
    _ClientDescribeFileSystemsResponseTypeDef
):
    """
    Type definition for `ClientDescribeFileSystems` `Response`

    - **Marker** *(string) --*

      Present if provided by caller in the request (String).

    - **FileSystems** *(list) --*

      An array of file system descriptions.

      - *(dict) --*

        A description of the file system.

        - **OwnerId** *(string) --*

          The AWS account that created the file system. If the file system was created by an IAM
          user, the parent account to which the user belongs is the owner.

        - **CreationToken** *(string) --*

          The opaque string specified in the request.

        - **FileSystemId** *(string) --*

          The ID of the file system, assigned by Amazon EFS.

        - **CreationTime** *(datetime) --*

          The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

        - **LifeCycleState** *(string) --*

          The lifecycle phase of the file system.

        - **Name** *(string) --*

          You can add tags to a file system, including a ``Name`` tag. For more information, see
          CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
          this field.

        - **NumberOfMountTargets** *(integer) --*

          The current number of mount targets that the file system has. For more information, see
          CreateMountTarget .

        - **SizeInBytes** *(dict) --*

          The latest known metered size (in bytes) of data stored in the file system, in its
          ``Value`` field, and the time at which that size was determined in its ``Timestamp``
          field. The ``Timestamp`` value is the integer number of seconds since
          1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
          consistent snapshot of the file system, but it is eventually consistent when there are no
          writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
          file system is not modified for a period longer than a couple of hours. Otherwise, the
          value is not the exact size that the file system was at any point in time.

          - **Value** *(integer) --*

            The latest known metered size (in bytes) of data stored in the file system.

          - **Timestamp** *(datetime) --*

            The time at which the size of data, returned in the ``Value`` field, was determined.
            The value is the integer number of seconds since 1970-01-01T00:00:00Z.

          - **ValueInIA** *(integer) --*

            The latest known metered size (in bytes) of data stored in the Infrequent Access
            storage class.

          - **ValueInStandard** *(integer) --*

            The latest known metered size (in bytes) of data stored in the Standard storage class.

        - **PerformanceMode** *(string) --*

          The performance mode of the file system.

        - **Encrypted** *(boolean) --*

          A Boolean value that, if true, indicates that the file system is encrypted.

        - **KmsKeyId** *(string) --*

          The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used
          to protect the encrypted file system.

        - **ThroughputMode** *(string) --*

          The throughput mode for a file system. There are two throughput modes to choose from for
          your file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
          ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You
          can decrease your file system's throughput in Provisioned Throughput mode or change
          between the throughput modes as long as it’s been more than 24 hours since the last
          decrease or throughput mode change.

        - **ProvisionedThroughputInMibps** *(float) --*

          The throughput, measured in MiB/s, that you want to provision for a file system. Valid
          values are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit
          on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS
          Support. For more information, see `Amazon EFS Limits That You Can Increase
          <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
          User Guide.*

        - **Tags** *(list) --*

          The tags associated with the file system, presented as an array of ``Tag`` objects.

          - *(dict) --*

            A tag is a key-value pair. Allowed characters are letters, white space, and numbers
            that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

            - **Key** *(string) --*

              The tag key (String). The key can't start with ``aws:`` .

            - **Value** *(string) --*

              The value of the tag key.

    - **NextMarker** *(string) --*

      Present if there are more file systems than returned in the response (String). You can use
      the ``NextMarker`` in the subsequent request to fetch the descriptions.
    """


_ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "_ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {"TransitionToIA": str},
    total=False,
)


class ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef(
    _ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
):
    """
    Type definition for `ClientDescribeLifecycleConfigurationResponse` `LifecyclePolicies`

    Describes a policy used by EFS lifecycle management to transition files to the Infrequent
    Access (IA) storage class.

    - **TransitionToIA** *(string) --*

      A value that describes the period of time that a file is not accessed, after which it
      transitions to the IA storage class. Metadata operations such as listing the contents of
      a directory don't count as file access events.
    """


_ClientDescribeLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleConfigurationResponseTypeDef",
    {
        "LifecyclePolicies": List[
            ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLifecycleConfigurationResponseTypeDef(
    _ClientDescribeLifecycleConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeLifecycleConfiguration` `Response`

    - **LifecyclePolicies** *(list) --*

      An array of lifecycle management policies. Currently, EFS supports a maximum of one policy
      per file system.

      - *(dict) --*

        Describes a policy used by EFS lifecycle management to transition files to the Infrequent
        Access (IA) storage class.

        - **TransitionToIA** *(string) --*

          A value that describes the period of time that a file is not accessed, after which it
          transitions to the IA storage class. Metadata operations such as listing the contents of
          a directory don't count as file access events.
    """


_ClientDescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)


class ClientDescribeMountTargetSecurityGroupsResponseTypeDef(
    _ClientDescribeMountTargetSecurityGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeMountTargetSecurityGroups` `Response`

    - **SecurityGroups** *(list) --*

      An array of security groups.

      - *(string) --*
    """


_ClientDescribeMountTargetsResponseMountTargetsTypeDef = TypedDict(
    "_ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)


class ClientDescribeMountTargetsResponseMountTargetsTypeDef(
    _ClientDescribeMountTargetsResponseMountTargetsTypeDef
):
    """
    Type definition for `ClientDescribeMountTargetsResponse` `MountTargets`

    Provides a description of a mount target.

    - **OwnerId** *(string) --*

      AWS account ID that owns the resource.

    - **MountTargetId** *(string) --*

      System-assigned mount target ID.

    - **FileSystemId** *(string) --*

      The ID of the file system for which the mount target is intended.

    - **SubnetId** *(string) --*

      The ID of the mount target's subnet.

    - **LifeCycleState** *(string) --*

      Lifecycle state of the mount target.

    - **IpAddress** *(string) --*

      Address at which the file system can be mounted by using the mount target.

    - **NetworkInterfaceId** *(string) --*

      The ID of the network interface that Amazon EFS created when it created the mount target.
    """


_ClientDescribeMountTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[ClientDescribeMountTargetsResponseMountTargetsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeMountTargetsResponseTypeDef(
    _ClientDescribeMountTargetsResponseTypeDef
):
    """
    Type definition for `ClientDescribeMountTargets` `Response`

    - **Marker** *(string) --*

      If the request included the ``Marker`` , the response returns that value in this field.

    - **MountTargets** *(list) --*

      Returns the file system's mount targets as an array of ``MountTargetDescription`` objects.

      - *(dict) --*

        Provides a description of a mount target.

        - **OwnerId** *(string) --*

          AWS account ID that owns the resource.

        - **MountTargetId** *(string) --*

          System-assigned mount target ID.

        - **FileSystemId** *(string) --*

          The ID of the file system for which the mount target is intended.

        - **SubnetId** *(string) --*

          The ID of the mount target's subnet.

        - **LifeCycleState** *(string) --*

          Lifecycle state of the mount target.

        - **IpAddress** *(string) --*

          Address at which the file system can be mounted by using the mount target.

        - **NetworkInterfaceId** *(string) --*

          The ID of the network interface that Amazon EFS created when it created the mount target.

    - **NextMarker** *(string) --*

      If a value is present, there are more mount targets to return. In a subsequent request, you
      can provide ``Marker`` in your request with this value to retrieve the next set of mount
      targets.
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    """
    Type definition for `ClientDescribeTagsResponse` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
    can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {
        "Marker": str,
        "Tags": List[ClientDescribeTagsResponseTagsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **Marker** *(string) --*

      If the request included a ``Marker`` , the response returns that value in this field.

    - **Tags** *(list) --*

      Returns tags associated with the file system as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
        can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.

    - **NextMarker** *(string) --*

      If a value is present, there are more tags to return. In a subsequent request, you can
      provide the value of ``NextMarker`` as the value of the ``Marker`` parameter in your next
      request to retrieve the next set of tags.
    """


_ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    {"TransitionToIA": str},
    total=False,
)


class ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef(
    _ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef
):
    """
    Type definition for `ClientPutLifecycleConfiguration` `LifecyclePolicies`

    Describes a policy used by EFS lifecycle management to transition files to the Infrequent
    Access (IA) storage class.

    - **TransitionToIA** *(string) --*

      A value that describes the period of time that a file is not accessed, after which it
      transitions to the IA storage class. Metadata operations such as listing the contents of a
      directory don't count as file access events.
    """


_ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {"TransitionToIA": str},
    total=False,
)


class ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef(
    _ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef
):
    """
    Type definition for `ClientPutLifecycleConfigurationResponse` `LifecyclePolicies`

    Describes a policy used by EFS lifecycle management to transition files to the Infrequent
    Access (IA) storage class.

    - **TransitionToIA** *(string) --*

      A value that describes the period of time that a file is not accessed, after which it
      transitions to the IA storage class. Metadata operations such as listing the contents of
      a directory don't count as file access events.
    """


_ClientPutLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationResponseTypeDef",
    {
        "LifecyclePolicies": List[
            ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef
        ]
    },
    total=False,
)


class ClientPutLifecycleConfigurationResponseTypeDef(
    _ClientPutLifecycleConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutLifecycleConfiguration` `Response`

    - **LifecyclePolicies** *(list) --*

      An array of lifecycle management policies. Currently, EFS supports a maximum of one policy
      per file system.

      - *(dict) --*

        Describes a policy used by EFS lifecycle management to transition files to the Infrequent
        Access (IA) storage class.

        - **TransitionToIA** *(string) --*

          A value that describes the period of time that a file is not accessed, after which it
          transitions to the IA storage class. Metadata operations such as listing the contents of
          a directory don't count as file access events.
    """


_ClientUpdateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientUpdateFileSystemResponseSizeInBytesTypeDef(
    _ClientUpdateFileSystemResponseSizeInBytesTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponse` `SizeInBytes`

    The latest known metered size (in bytes) of data stored in the file system, in its ``Value``
    field, and the time at which that size was determined in its ``Timestamp`` field. The
    ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The
    ``SizeInBytes`` value doesn't represent the size of a consistent snapshot of the file system,
    but it is eventually consistent when there are no writes to the file system. That is,
    ``SizeInBytes`` represents actual size only if the file system is not modified for a period
    longer than a couple of hours. Otherwise, the value is not the exact size that the file
    system was at any point in time.

    - **Value** *(integer) --*

      The latest known metered size (in bytes) of data stored in the file system.

    - **Timestamp** *(datetime) --*

      The time at which the size of data, returned in the ``Value`` field, was determined. The
      value is the integer number of seconds since 1970-01-01T00:00:00Z.

    - **ValueInIA** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Infrequent Access storage
      class.

    - **ValueInStandard** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Standard storage class.
    """


_ClientUpdateFileSystemResponseTagsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateFileSystemResponseTagsTypeDef(
    _ClientUpdateFileSystemResponseTagsTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponse` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
    can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": str,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientUpdateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": str,
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientUpdateFileSystemResponseTagsTypeDef],
    },
    total=False,
)


class ClientUpdateFileSystemResponseTypeDef(_ClientUpdateFileSystemResponseTypeDef):
    """
    Type definition for `ClientUpdateFileSystem` `Response`

    A description of the file system.

    - **OwnerId** *(string) --*

      The AWS account that created the file system. If the file system was created by an IAM user,
      the parent account to which the user belongs is the owner.

    - **CreationToken** *(string) --*

      The opaque string specified in the request.

    - **FileSystemId** *(string) --*

      The ID of the file system, assigned by Amazon EFS.

    - **CreationTime** *(datetime) --*

      The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

    - **LifeCycleState** *(string) --*

      The lifecycle phase of the file system.

    - **Name** *(string) --*

      You can add tags to a file system, including a ``Name`` tag. For more information, see
      CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
      this field.

    - **NumberOfMountTargets** *(integer) --*

      The current number of mount targets that the file system has. For more information, see
      CreateMountTarget .

    - **SizeInBytes** *(dict) --*

      The latest known metered size (in bytes) of data stored in the file system, in its ``Value``
      field, and the time at which that size was determined in its ``Timestamp`` field. The
      ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The
      ``SizeInBytes`` value doesn't represent the size of a consistent snapshot of the file system,
      but it is eventually consistent when there are no writes to the file system. That is,
      ``SizeInBytes`` represents actual size only if the file system is not modified for a period
      longer than a couple of hours. Otherwise, the value is not the exact size that the file
      system was at any point in time.

      - **Value** *(integer) --*

        The latest known metered size (in bytes) of data stored in the file system.

      - **Timestamp** *(datetime) --*

        The time at which the size of data, returned in the ``Value`` field, was determined. The
        value is the integer number of seconds since 1970-01-01T00:00:00Z.

      - **ValueInIA** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Infrequent Access storage
        class.

      - **ValueInStandard** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Standard storage class.

    - **PerformanceMode** *(string) --*

      The performance mode of the file system.

    - **Encrypted** *(boolean) --*

      A Boolean value that, if true, indicates that the file system is encrypted.

    - **KmsKeyId** *(string) --*

      The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to
      protect the encrypted file system.

    - **ThroughputMode** *(string) --*

      The throughput mode for a file system. There are two throughput modes to choose from for your
      file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
      ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You can
      decrease your file system's throughput in Provisioned Throughput mode or change between the
      throughput modes as long as it’s been more than 24 hours since the last decrease or
      throughput mode change.

    - **ProvisionedThroughputInMibps** *(float) --*

      The throughput, measured in MiB/s, that you want to provision for a file system. Valid values
      are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit on
      throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For
      more information, see `Amazon EFS Limits That You Can Increase
      <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
      User Guide.*

    - **Tags** *(list) --*

      The tags associated with the file system, presented as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
        can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.
    """


_DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFileSystemsPaginatePaginationConfigTypeDef(
    _DescribeFileSystemsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginate` `PaginationConfig`

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


_DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `SizeInBytes`

    The latest known metered size (in bytes) of data stored in the file system, in its
    ``Value`` field, and the time at which that size was determined in its ``Timestamp``
    field. The ``Timestamp`` value is the integer number of seconds since
    1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
    consistent snapshot of the file system, but it is eventually consistent when there are no
    writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
    file system is not modified for a period longer than a couple of hours. Otherwise, the
    value is not the exact size that the file system was at any point in time.

    - **Value** *(integer) --*

      The latest known metered size (in bytes) of data stored in the file system.

    - **Timestamp** *(datetime) --*

      The time at which the size of data, returned in the ``Value`` field, was determined.
      The value is the integer number of seconds since 1970-01-01T00:00:00Z.

    - **ValueInIA** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Infrequent Access
      storage class.

    - **ValueInStandard** *(integer) --*

      The latest known metered size (in bytes) of data stored in the Standard storage class.
    """


_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers
    that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": str,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef,
        "PerformanceMode": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": str,
        "ProvisionedThroughputInMibps": float,
        "Tags": List[DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef],
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponse` `FileSystems`

    A description of the file system.

    - **OwnerId** *(string) --*

      The AWS account that created the file system. If the file system was created by an IAM
      user, the parent account to which the user belongs is the owner.

    - **CreationToken** *(string) --*

      The opaque string specified in the request.

    - **FileSystemId** *(string) --*

      The ID of the file system, assigned by Amazon EFS.

    - **CreationTime** *(datetime) --*

      The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

    - **LifeCycleState** *(string) --*

      The lifecycle phase of the file system.

    - **Name** *(string) --*

      You can add tags to a file system, including a ``Name`` tag. For more information, see
      CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
      this field.

    - **NumberOfMountTargets** *(integer) --*

      The current number of mount targets that the file system has. For more information, see
      CreateMountTarget .

    - **SizeInBytes** *(dict) --*

      The latest known metered size (in bytes) of data stored in the file system, in its
      ``Value`` field, and the time at which that size was determined in its ``Timestamp``
      field. The ``Timestamp`` value is the integer number of seconds since
      1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
      consistent snapshot of the file system, but it is eventually consistent when there are no
      writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
      file system is not modified for a period longer than a couple of hours. Otherwise, the
      value is not the exact size that the file system was at any point in time.

      - **Value** *(integer) --*

        The latest known metered size (in bytes) of data stored in the file system.

      - **Timestamp** *(datetime) --*

        The time at which the size of data, returned in the ``Value`` field, was determined.
        The value is the integer number of seconds since 1970-01-01T00:00:00Z.

      - **ValueInIA** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Infrequent Access
        storage class.

      - **ValueInStandard** *(integer) --*

        The latest known metered size (in bytes) of data stored in the Standard storage class.

    - **PerformanceMode** *(string) --*

      The performance mode of the file system.

    - **Encrypted** *(boolean) --*

      A Boolean value that, if true, indicates that the file system is encrypted.

    - **KmsKeyId** *(string) --*

      The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used
      to protect the encrypted file system.

    - **ThroughputMode** *(string) --*

      The throughput mode for a file system. There are two throughput modes to choose from for
      your file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
      ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You
      can decrease your file system's throughput in Provisioned Throughput mode or change
      between the throughput modes as long as it’s been more than 24 hours since the last
      decrease or throughput mode change.

    - **ProvisionedThroughputInMibps** *(float) --*

      The throughput, measured in MiB/s, that you want to provision for a file system. Valid
      values are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit
      on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS
      Support. For more information, see `Amazon EFS Limits That You Can Increase
      <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
      User Guide.*

    - **Tags** *(list) --*

      The tags associated with the file system, presented as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers
        that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.
    """


_DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseTypeDef(
    _DescribeFileSystemsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginate` `Response`

    - **Marker** *(string) --*

      Present if provided by caller in the request (String).

    - **FileSystems** *(list) --*

      An array of file system descriptions.

      - *(dict) --*

        A description of the file system.

        - **OwnerId** *(string) --*

          The AWS account that created the file system. If the file system was created by an IAM
          user, the parent account to which the user belongs is the owner.

        - **CreationToken** *(string) --*

          The opaque string specified in the request.

        - **FileSystemId** *(string) --*

          The ID of the file system, assigned by Amazon EFS.

        - **CreationTime** *(datetime) --*

          The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

        - **LifeCycleState** *(string) --*

          The lifecycle phase of the file system.

        - **Name** *(string) --*

          You can add tags to a file system, including a ``Name`` tag. For more information, see
          CreateFileSystem . If the file system has a ``Name`` tag, Amazon EFS returns the value in
          this field.

        - **NumberOfMountTargets** *(integer) --*

          The current number of mount targets that the file system has. For more information, see
          CreateMountTarget .

        - **SizeInBytes** *(dict) --*

          The latest known metered size (in bytes) of data stored in the file system, in its
          ``Value`` field, and the time at which that size was determined in its ``Timestamp``
          field. The ``Timestamp`` value is the integer number of seconds since
          1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn't represent the size of a
          consistent snapshot of the file system, but it is eventually consistent when there are no
          writes to the file system. That is, ``SizeInBytes`` represents actual size only if the
          file system is not modified for a period longer than a couple of hours. Otherwise, the
          value is not the exact size that the file system was at any point in time.

          - **Value** *(integer) --*

            The latest known metered size (in bytes) of data stored in the file system.

          - **Timestamp** *(datetime) --*

            The time at which the size of data, returned in the ``Value`` field, was determined.
            The value is the integer number of seconds since 1970-01-01T00:00:00Z.

          - **ValueInIA** *(integer) --*

            The latest known metered size (in bytes) of data stored in the Infrequent Access
            storage class.

          - **ValueInStandard** *(integer) --*

            The latest known metered size (in bytes) of data stored in the Standard storage class.

        - **PerformanceMode** *(string) --*

          The performance mode of the file system.

        - **Encrypted** *(boolean) --*

          A Boolean value that, if true, indicates that the file system is encrypted.

        - **KmsKeyId** *(string) --*

          The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used
          to protect the encrypted file system.

        - **ThroughputMode** *(string) --*

          The throughput mode for a file system. There are two throughput modes to choose from for
          your file system: ``bursting`` and ``provisioned`` . If you set ``ThroughputMode`` to
          ``provisioned`` , you must also set a value for ``ProvisionedThroughPutInMibps`` . You
          can decrease your file system's throughput in Provisioned Throughput mode or change
          between the throughput modes as long as it’s been more than 24 hours since the last
          decrease or throughput mode change.

        - **ProvisionedThroughputInMibps** *(float) --*

          The throughput, measured in MiB/s, that you want to provision for a file system. Valid
          values are 1-1024. Required if ``ThroughputMode`` is set to ``provisioned`` . The limit
          on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS
          Support. For more information, see `Amazon EFS Limits That You Can Increase
          <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS
          User Guide.*

        - **Tags** *(list) --*

          The tags associated with the file system, presented as an array of ``Tag`` objects.

          - *(dict) --*

            A tag is a key-value pair. Allowed characters are letters, white space, and numbers
            that can be represented in UTF-8, and the following characters:``+ - = . _ : /``

            - **Key** *(string) --*

              The tag key (String). The key can't start with ``aws:`` .

            - **Value** *(string) --*

              The value of the tag key.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeMountTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMountTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMountTargetsPaginatePaginationConfigTypeDef(
    _DescribeMountTargetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeMountTargetsPaginate` `PaginationConfig`

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


_DescribeMountTargetsPaginateResponseMountTargetsTypeDef = TypedDict(
    "_DescribeMountTargetsPaginateResponseMountTargetsTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)


class DescribeMountTargetsPaginateResponseMountTargetsTypeDef(
    _DescribeMountTargetsPaginateResponseMountTargetsTypeDef
):
    """
    Type definition for `DescribeMountTargetsPaginateResponse` `MountTargets`

    Provides a description of a mount target.

    - **OwnerId** *(string) --*

      AWS account ID that owns the resource.

    - **MountTargetId** *(string) --*

      System-assigned mount target ID.

    - **FileSystemId** *(string) --*

      The ID of the file system for which the mount target is intended.

    - **SubnetId** *(string) --*

      The ID of the mount target's subnet.

    - **LifeCycleState** *(string) --*

      Lifecycle state of the mount target.

    - **IpAddress** *(string) --*

      Address at which the file system can be mounted by using the mount target.

    - **NetworkInterfaceId** *(string) --*

      The ID of the network interface that Amazon EFS created when it created the mount target.
    """


_DescribeMountTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeMountTargetsPaginateResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[DescribeMountTargetsPaginateResponseMountTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeMountTargetsPaginateResponseTypeDef(
    _DescribeMountTargetsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeMountTargetsPaginate` `Response`

    - **Marker** *(string) --*

      If the request included the ``Marker`` , the response returns that value in this field.

    - **MountTargets** *(list) --*

      Returns the file system's mount targets as an array of ``MountTargetDescription`` objects.

      - *(dict) --*

        Provides a description of a mount target.

        - **OwnerId** *(string) --*

          AWS account ID that owns the resource.

        - **MountTargetId** *(string) --*

          System-assigned mount target ID.

        - **FileSystemId** *(string) --*

          The ID of the file system for which the mount target is intended.

        - **SubnetId** *(string) --*

          The ID of the mount target's subnet.

        - **LifeCycleState** *(string) --*

          Lifecycle state of the mount target.

        - **IpAddress** *(string) --*

          Address at which the file system can be mounted by using the mount target.

        - **NetworkInterfaceId** *(string) --*

          The ID of the network interface that Amazon EFS created when it created the mount target.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(
    _DescribeTagsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTagsPaginate` `PaginationConfig`

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


_DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeTagsPaginateResponseTagsTypeDef(_DescribeTagsPaginateResponseTagsTypeDef):
    """
    Type definition for `DescribeTagsPaginateResponse` `Tags`

    A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
    can be represented in UTF-8, and the following characters:``+ - = . _ : /``

    - **Key** *(string) --*

      The tag key (String). The key can't start with ``aws:`` .

    - **Value** *(string) --*

      The value of the tag key.
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {
        "Marker": str,
        "Tags": List[DescribeTagsPaginateResponseTagsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    Type definition for `DescribeTagsPaginate` `Response`

    - **Marker** *(string) --*

      If the request included a ``Marker`` , the response returns that value in this field.

    - **Tags** *(list) --*

      Returns tags associated with the file system as an array of ``Tag`` objects.

      - *(dict) --*

        A tag is a key-value pair. Allowed characters are letters, white space, and numbers that
        can be represented in UTF-8, and the following characters:``+ - = . _ : /``

        - **Key** *(string) --*

          The tag key (String). The key can't start with ``aws:`` .

        - **Value** *(string) --*

          The value of the tag key.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
