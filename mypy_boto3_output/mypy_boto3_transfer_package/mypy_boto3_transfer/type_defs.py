"Main interface for transfer type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateServerEndpointDetailsTypeDef",
    "ClientCreateServerIdentityProviderDetailsTypeDef",
    "ClientCreateServerResponseTypeDef",
    "ClientCreateServerTagsTypeDef",
    "ClientCreateUserHomeDirectoryMappingsTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientDescribeServerResponseServerEndpointDetailsTypeDef",
    "ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    "ClientDescribeServerResponseServerTagsTypeDef",
    "ClientDescribeServerResponseServerTypeDef",
    "ClientDescribeServerResponseTypeDef",
    "ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    "ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    "ClientDescribeUserResponseUserTagsTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientImportSshPublicKeyResponseTypeDef",
    "ClientListServersResponseServersTypeDef",
    "ClientListServersResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestIdentityProviderResponseTypeDef",
    "ClientUpdateServerEndpointDetailsTypeDef",
    "ClientUpdateServerIdentityProviderDetailsTypeDef",
    "ClientUpdateServerResponseTypeDef",
    "ClientUpdateUserHomeDirectoryMappingsTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ListServersPaginatePaginationConfigTypeDef",
    "ListServersPaginateResponseServersTypeDef",
    "ListServersPaginateResponseTypeDef",
)


_ClientCreateServerEndpointDetailsTypeDef = TypedDict(
    "_ClientCreateServerEndpointDetailsTypeDef", {"VpcEndpointId": str}, total=False
)


class ClientCreateServerEndpointDetailsTypeDef(
    _ClientCreateServerEndpointDetailsTypeDef
):
    """
    Type definition for `ClientCreateServer` `EndpointDetails`

    The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP
    server. This parameter is required when you specify a value for the ``EndpointType`` parameter.

    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint.
    """


_ClientCreateServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientCreateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientCreateServerIdentityProviderDetailsTypeDef(
    _ClientCreateServerIdentityProviderDetailsTypeDef
):
    """
    Type definition for `ClientCreateServer` `IdentityProviderDetails`

    This parameter is required when the ``IdentityProviderType`` is set to ``API_GATEWAY`` . Accepts
    an array containing all of the information required to call a customer-supplied authentication
    API, including the API Gateway URL. This property is not required when the
    ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .

    - **Url** *(string) --*

      The ``Url`` parameter provides contains the location of the service endpoint used to
      authenticate users.

    - **InvocationRole** *(string) --*

      The ``InvocationRole`` parameter provides the type of ``InvocationRole`` used to authenticate
      the user account.
    """


_ClientCreateServerResponseTypeDef = TypedDict(
    "_ClientCreateServerResponseTypeDef", {"ServerId": str}, total=False
)


class ClientCreateServerResponseTypeDef(_ClientCreateServerResponseTypeDef):
    """
    Type definition for `ClientCreateServer` `Response`

    - **ServerId** *(string) --*

      The service-assigned ID of the SFTP server that is created.
    """


_ClientCreateServerTagsTypeDef = TypedDict(
    "_ClientCreateServerTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateServerTagsTypeDef(_ClientCreateServerTagsTypeDef):
    """
    Type definition for `ClientCreateServer` `Tags`

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
    for and group a resource for various purposes. You can apply tags to servers, users, and roles.
    A tag key can take more than one value. For example, to group servers for accounting purposes,
    you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting``
    to that group.

    - **Key** *(string) --* **[REQUIRED]**

      The name assigned to the tag that you create.

    - **Value** *(string) --* **[REQUIRED]**

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientCreateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientCreateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}
)


class ClientCreateUserHomeDirectoryMappingsTypeDef(
    _ClientCreateUserHomeDirectoryMappingsTypeDef
):
    """
    Type definition for `ClientCreateUser` `HomeDirectoryMappings`

    Represents an object that contains entries and a targets for ``HomeDirectoryMappings`` .

    - **Entry** *(string) --* **[REQUIRED]**

      Represents an entry and a target for ``HomeDirectoryMappings`` .

    - **Target** *(string) --* **[REQUIRED]**

      Represents the map target that is used in a ``HomeDirectorymapEntry`` .
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    - **ServerId** *(string) --*

      The ID of the SFTP server that the user is attached to.

    - **UserName** *(string) --*

      A unique string that identifies a user account associated with an SFTP server.
    """


_ClientCreateUserTagsTypeDef = TypedDict(
    "_ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateUserTagsTypeDef(_ClientCreateUserTagsTypeDef):
    """
    Type definition for `ClientCreateUser` `Tags`

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
    for and group a resource for various purposes. You can apply tags to servers, users, and roles.
    A tag key can take more than one value. For example, to group servers for accounting purposes,
    you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting``
    to that group.

    - **Key** *(string) --* **[REQUIRED]**

      The name assigned to the tag that you create.

    - **Value** *(string) --* **[REQUIRED]**

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientDescribeServerResponseServerEndpointDetailsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerEndpointDetailsTypeDef",
    {"VpcEndpointId": str},
    total=False,
)


class ClientDescribeServerResponseServerEndpointDetailsTypeDef(
    _ClientDescribeServerResponseServerEndpointDetailsTypeDef
):
    """
    Type definition for `ClientDescribeServerResponseServer` `EndpointDetails`

    The virtual private cloud (VPC) endpoint settings that you configured for your SFTP server.

    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint.
    """


_ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef(
    _ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef
):
    """
    Type definition for `ClientDescribeServerResponseServer` `IdentityProviderDetails`

    Specifies information to call a customer-supplied authentication API. This field is not
    populated when the ``IdentityProviderType`` of the server is ``SERVICE_MANAGED`` >.

    - **Url** *(string) --*

      The ``Url`` parameter provides contains the location of the service endpoint used to
      authenticate users.

    - **InvocationRole** *(string) --*

      The ``InvocationRole`` parameter provides the type of ``InvocationRole`` used to
      authenticate the user account.
    """


_ClientDescribeServerResponseServerTagsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeServerResponseServerTagsTypeDef(
    _ClientDescribeServerResponseServerTagsTypeDef
):
    """
    Type definition for `ClientDescribeServerResponseServer` `Tags`

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to
    search for and group a resource for various purposes. You can apply tags to servers,
    users, and roles. A tag key can take more than one value. For example, to group servers
    for accounting purposes, you might create a tag called ``Group`` and assign the values
    ``Research`` and ``Accounting`` to that group.

    - **Key** *(string) --*

      The name assigned to the tag that you create.

    - **Value** *(string) --*

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientDescribeServerResponseServerTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerTypeDef",
    {
        "Arn": str,
        "EndpointDetails": ClientDescribeServerResponseServerEndpointDetailsTypeDef,
        "EndpointType": str,
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef,
        "IdentityProviderType": str,
        "LoggingRole": str,
        "ServerId": str,
        "State": str,
        "Tags": List[ClientDescribeServerResponseServerTagsTypeDef],
        "UserCount": int,
    },
    total=False,
)


class ClientDescribeServerResponseServerTypeDef(
    _ClientDescribeServerResponseServerTypeDef
):
    """
    Type definition for `ClientDescribeServerResponse` `Server`

    An array containing the properties of the server with the ``ServerID`` you specified.

    - **Arn** *(string) --*

      Specifies the unique Amazon Resource Name (ARN) for the server to be described.

    - **EndpointDetails** *(dict) --*

      The virtual private cloud (VPC) endpoint settings that you configured for your SFTP server.

      - **VpcEndpointId** *(string) --*

        The ID of the VPC endpoint.

    - **EndpointType** *(string) --*

      The type of endpoint that your SFTP server is connected to. If your SFTP server is
      connected to a VPC endpoint, your server isn't accessible over the public internet.

    - **HostKeyFingerprint** *(string) --*

      This value contains the message-digest algorithm (MD5) hash of the server's host key. This
      value is equivalent to the output of the ``ssh-keygen -l -E md5 -f my-new-server-key``
      command.

    - **IdentityProviderDetails** *(dict) --*

      Specifies information to call a customer-supplied authentication API. This field is not
      populated when the ``IdentityProviderType`` of the server is ``SERVICE_MANAGED`` >.

      - **Url** *(string) --*

        The ``Url`` parameter provides contains the location of the service endpoint used to
        authenticate users.

      - **InvocationRole** *(string) --*

        The ``InvocationRole`` parameter provides the type of ``InvocationRole`` used to
        authenticate the user account.

    - **IdentityProviderType** *(string) --*

      This property defines the mode of authentication method enabled for this service. A value
      of ``SERVICE_MANAGED`` means that you are using this server to store and access SFTP user
      credentials within the service. A value of ``API_GATEWAY`` indicates that you have
      integrated an API Gateway endpoint that will be invoked for authenticating your user into
      the service.

    - **LoggingRole** *(string) --*

      This property is an AWS Identity and Access Management (IAM) entity that allows the server
      to turn on Amazon CloudWatch logging for Amazon S3 events. When set, user activity can be
      viewed in your CloudWatch logs.

    - **ServerId** *(string) --*

      This property is a unique system-assigned identifier for the SFTP server that you
      instantiate.

    - **State** *(string) --*

      The condition of the SFTP server for the server that was described. A value of ``ONLINE``
      indicates that the server can accept jobs and transfer files. A ``State`` value of
      ``OFFLINE`` means that the server cannot perform file transfer operations.

      The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an intermediate
      state, either not fully able to respond, or not fully offline. The values of
      ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

    - **Tags** *(list) --*

      This property contains the key-value pairs that you can use to search for and group servers
      that were assigned to the server that was described.

      - *(dict) --*

        Creates a key-value pair for a specific resource. Tags are metadata that you can use to
        search for and group a resource for various purposes. You can apply tags to servers,
        users, and roles. A tag key can take more than one value. For example, to group servers
        for accounting purposes, you might create a tag called ``Group`` and assign the values
        ``Research`` and ``Accounting`` to that group.

        - **Key** *(string) --*

          The name assigned to the tag that you create.

        - **Value** *(string) --*

          This property contains one or more values that you assigned to the key name you create.

    - **UserCount** *(integer) --*

      The number of users that are assigned to the SFTP server you specified with the
      ``ServerId`` .
    """


_ClientDescribeServerResponseTypeDef = TypedDict(
    "_ClientDescribeServerResponseTypeDef",
    {"Server": ClientDescribeServerResponseServerTypeDef},
    total=False,
)


class ClientDescribeServerResponseTypeDef(_ClientDescribeServerResponseTypeDef):
    """
    Type definition for `ClientDescribeServer` `Response`

    - **Server** *(dict) --*

      An array containing the properties of the server with the ``ServerID`` you specified.

      - **Arn** *(string) --*

        Specifies the unique Amazon Resource Name (ARN) for the server to be described.

      - **EndpointDetails** *(dict) --*

        The virtual private cloud (VPC) endpoint settings that you configured for your SFTP server.

        - **VpcEndpointId** *(string) --*

          The ID of the VPC endpoint.

      - **EndpointType** *(string) --*

        The type of endpoint that your SFTP server is connected to. If your SFTP server is
        connected to a VPC endpoint, your server isn't accessible over the public internet.

      - **HostKeyFingerprint** *(string) --*

        This value contains the message-digest algorithm (MD5) hash of the server's host key. This
        value is equivalent to the output of the ``ssh-keygen -l -E md5 -f my-new-server-key``
        command.

      - **IdentityProviderDetails** *(dict) --*

        Specifies information to call a customer-supplied authentication API. This field is not
        populated when the ``IdentityProviderType`` of the server is ``SERVICE_MANAGED`` >.

        - **Url** *(string) --*

          The ``Url`` parameter provides contains the location of the service endpoint used to
          authenticate users.

        - **InvocationRole** *(string) --*

          The ``InvocationRole`` parameter provides the type of ``InvocationRole`` used to
          authenticate the user account.

      - **IdentityProviderType** *(string) --*

        This property defines the mode of authentication method enabled for this service. A value
        of ``SERVICE_MANAGED`` means that you are using this server to store and access SFTP user
        credentials within the service. A value of ``API_GATEWAY`` indicates that you have
        integrated an API Gateway endpoint that will be invoked for authenticating your user into
        the service.

      - **LoggingRole** *(string) --*

        This property is an AWS Identity and Access Management (IAM) entity that allows the server
        to turn on Amazon CloudWatch logging for Amazon S3 events. When set, user activity can be
        viewed in your CloudWatch logs.

      - **ServerId** *(string) --*

        This property is a unique system-assigned identifier for the SFTP server that you
        instantiate.

      - **State** *(string) --*

        The condition of the SFTP server for the server that was described. A value of ``ONLINE``
        indicates that the server can accept jobs and transfer files. A ``State`` value of
        ``OFFLINE`` means that the server cannot perform file transfer operations.

        The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an intermediate
        state, either not fully able to respond, or not fully offline. The values of
        ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

      - **Tags** *(list) --*

        This property contains the key-value pairs that you can use to search for and group servers
        that were assigned to the server that was described.

        - *(dict) --*

          Creates a key-value pair for a specific resource. Tags are metadata that you can use to
          search for and group a resource for various purposes. You can apply tags to servers,
          users, and roles. A tag key can take more than one value. For example, to group servers
          for accounting purposes, you might create a tag called ``Group`` and assign the values
          ``Research`` and ``Accounting`` to that group.

          - **Key** *(string) --*

            The name assigned to the tag that you create.

          - **Value** *(string) --*

            This property contains one or more values that you assigned to the key name you create.

      - **UserCount** *(integer) --*

        The number of users that are assigned to the SFTP server you specified with the
        ``ServerId`` .
    """


_ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    {"Entry": str, "Target": str},
    total=False,
)


class ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef(
    _ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef
):
    """
    Type definition for `ClientDescribeUserResponseUser` `HomeDirectoryMappings`

    Represents an object that contains entries and a targets for ``HomeDirectoryMappings`` .

    - **Entry** *(string) --*

      Represents an entry and a target for ``HomeDirectoryMappings`` .

    - **Target** *(string) --*

      Represents the map target that is used in a ``HomeDirectorymapEntry`` .
    """


_ClientDescribeUserResponseUserSshPublicKeysTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    {"DateImported": datetime, "SshPublicKeyBody": str, "SshPublicKeyId": str},
    total=False,
)


class ClientDescribeUserResponseUserSshPublicKeysTypeDef(
    _ClientDescribeUserResponseUserSshPublicKeysTypeDef
):
    """
    Type definition for `ClientDescribeUserResponseUser` `SshPublicKeys`

    Provides information about the public Secure Shell (SSH) key that is associated with a
    user account for a specific server (as identified by ``ServerId`` ). The information
    returned includes the date the key was imported, the public key contents, and the public
    key ID. A user can store more than one SSH public key associated with their user name on
    a specific SFTP server.

    - **DateImported** *(datetime) --*

      The date that the public key was added to the user account.

    - **SshPublicKeyBody** *(string) --*

      The content of the SSH public key as specified by the ``PublicKeyId`` .

    - **SshPublicKeyId** *(string) --*

      The ``SshPublicKeyId`` parameter contains the identifier of the public key.
    """


_ClientDescribeUserResponseUserTagsTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeUserResponseUserTagsTypeDef(
    _ClientDescribeUserResponseUserTagsTypeDef
):
    """
    Type definition for `ClientDescribeUserResponseUser` `Tags`

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to
    search for and group a resource for various purposes. You can apply tags to servers,
    users, and roles. A tag key can take more than one value. For example, to group servers
    for accounting purposes, you might create a tag called ``Group`` and assign the values
    ``Research`` and ``Accounting`` to that group.

    - **Key** *(string) --*

      The name assigned to the tag that you create.

    - **Value** *(string) --*

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryMappings": List[
            ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef
        ],
        "HomeDirectoryType": str,
        "Policy": str,
        "Role": str,
        "SshPublicKeys": List[ClientDescribeUserResponseUserSshPublicKeysTypeDef],
        "Tags": List[ClientDescribeUserResponseUserTagsTypeDef],
        "UserName": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    """
    Type definition for `ClientDescribeUserResponse` `User`

    An array containing the properties of the user account for the ``ServerID`` value that you
    specified.

    - **Arn** *(string) --*

      This property contains the unique Amazon Resource Name (ARN) for the user that was
      requested to be described.

    - **HomeDirectory** *(string) --*

      This property specifies the landing directory (or folder), which is the location that files
      are written to or read from in an Amazon S3 bucket for the described user. An example is
      ``/*your s3 bucket name* /home/*username* `` .

    - **HomeDirectoryMappings** *(list) --*

      Logical directory mappings that you specified for what S3 paths and keys should be visible
      to your user and how you want to make them visible. You will need to specify the "``Entry``
      " and "``Target`` " pair, where ``Entry`` shows how the path is made visible and ``Target``
      is the actual S3 path. If you only specify a target, it will be displayed as is. You will
      need to also make sure that your AWS IAM Role provides access to paths in ``Target`` .

      In most cases, you can use this value instead of the scope down policy to lock your user
      down to the designated home directory ("chroot"). To do this, you can set ``Entry`` to '/'
      and set ``Target`` to the HomeDirectory parameter value.

      In most cases, you can use this value instead of the scope down policy to lock your user
      down to the designated home directory ("chroot"). To do this, you can set ``Entry`` to '/'
      and set ``Target`` to the HomeDirectory parameter value.

      - *(dict) --*

        Represents an object that contains entries and a targets for ``HomeDirectoryMappings`` .

        - **Entry** *(string) --*

          Represents an entry and a target for ``HomeDirectoryMappings`` .

        - **Target** *(string) --*

          Represents the map target that is used in a ``HomeDirectorymapEntry`` .

    - **HomeDirectoryType** *(string) --*

      The type of landing directory (folder) you mapped for your users' to see when they log into
      the SFTP server. If you set it to ``PATH`` , the user will see the absolute Amazon S3
      bucket paths as is in their SFTP clients. If you set it ``LOGICAL`` , you will need to
      provide mappings in the ``HomeDirectoryMappings`` for how you want to make S3 paths visible
      to your user.

    - **Policy** *(string) --*

      Specifies the name of the policy in use for the described user.

    - **Role** *(string) --*

      This property specifies the IAM role that controls your user's access to your Amazon S3
      bucket. The policies attached to this role will determine the level of access you want to
      provide your users when transferring files into and out of your Amazon S3 bucket or
      buckets. The IAM role should also contain a trust relationship that allows the SFTP server
      to access your resources when servicing your SFTP user's transfer requests.

    - **SshPublicKeys** *(list) --*

      This property contains the public key portion of the Secure Shell (SSH) keys stored for the
      described user.

      - *(dict) --*

        Provides information about the public Secure Shell (SSH) key that is associated with a
        user account for a specific server (as identified by ``ServerId`` ). The information
        returned includes the date the key was imported, the public key contents, and the public
        key ID. A user can store more than one SSH public key associated with their user name on
        a specific SFTP server.

        - **DateImported** *(datetime) --*

          The date that the public key was added to the user account.

        - **SshPublicKeyBody** *(string) --*

          The content of the SSH public key as specified by the ``PublicKeyId`` .

        - **SshPublicKeyId** *(string) --*

          The ``SshPublicKeyId`` parameter contains the identifier of the public key.

    - **Tags** *(list) --*

      This property contains the key-value pairs for the user requested. Tag can be used to
      search for and group users for a variety of purposes.

      - *(dict) --*

        Creates a key-value pair for a specific resource. Tags are metadata that you can use to
        search for and group a resource for various purposes. You can apply tags to servers,
        users, and roles. A tag key can take more than one value. For example, to group servers
        for accounting purposes, you might create a tag called ``Group`` and assign the values
        ``Research`` and ``Accounting`` to that group.

        - **Key** *(string) --*

          The name assigned to the tag that you create.

        - **Value** *(string) --*

          This property contains one or more values that you assigned to the key name you create.

    - **UserName** *(string) --*

      This property is the name of the user that was requested to be described. User names are
      used for authentication purposes. This is the string that will be used by your user when
      they log in to your SFTP server.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"ServerId": str, "User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    Type definition for `ClientDescribeUser` `Response`

    - **ServerId** *(string) --*

      A system-assigned unique identifier for an SFTP server that has this user assigned.

    - **User** *(dict) --*

      An array containing the properties of the user account for the ``ServerID`` value that you
      specified.

      - **Arn** *(string) --*

        This property contains the unique Amazon Resource Name (ARN) for the user that was
        requested to be described.

      - **HomeDirectory** *(string) --*

        This property specifies the landing directory (or folder), which is the location that files
        are written to or read from in an Amazon S3 bucket for the described user. An example is
        ``/*your s3 bucket name* /home/*username* `` .

      - **HomeDirectoryMappings** *(list) --*

        Logical directory mappings that you specified for what S3 paths and keys should be visible
        to your user and how you want to make them visible. You will need to specify the "``Entry``
        " and "``Target`` " pair, where ``Entry`` shows how the path is made visible and ``Target``
        is the actual S3 path. If you only specify a target, it will be displayed as is. You will
        need to also make sure that your AWS IAM Role provides access to paths in ``Target`` .

        In most cases, you can use this value instead of the scope down policy to lock your user
        down to the designated home directory ("chroot"). To do this, you can set ``Entry`` to '/'
        and set ``Target`` to the HomeDirectory parameter value.

        In most cases, you can use this value instead of the scope down policy to lock your user
        down to the designated home directory ("chroot"). To do this, you can set ``Entry`` to '/'
        and set ``Target`` to the HomeDirectory parameter value.

        - *(dict) --*

          Represents an object that contains entries and a targets for ``HomeDirectoryMappings`` .

          - **Entry** *(string) --*

            Represents an entry and a target for ``HomeDirectoryMappings`` .

          - **Target** *(string) --*

            Represents the map target that is used in a ``HomeDirectorymapEntry`` .

      - **HomeDirectoryType** *(string) --*

        The type of landing directory (folder) you mapped for your users' to see when they log into
        the SFTP server. If you set it to ``PATH`` , the user will see the absolute Amazon S3
        bucket paths as is in their SFTP clients. If you set it ``LOGICAL`` , you will need to
        provide mappings in the ``HomeDirectoryMappings`` for how you want to make S3 paths visible
        to your user.

      - **Policy** *(string) --*

        Specifies the name of the policy in use for the described user.

      - **Role** *(string) --*

        This property specifies the IAM role that controls your user's access to your Amazon S3
        bucket. The policies attached to this role will determine the level of access you want to
        provide your users when transferring files into and out of your Amazon S3 bucket or
        buckets. The IAM role should also contain a trust relationship that allows the SFTP server
        to access your resources when servicing your SFTP user's transfer requests.

      - **SshPublicKeys** *(list) --*

        This property contains the public key portion of the Secure Shell (SSH) keys stored for the
        described user.

        - *(dict) --*

          Provides information about the public Secure Shell (SSH) key that is associated with a
          user account for a specific server (as identified by ``ServerId`` ). The information
          returned includes the date the key was imported, the public key contents, and the public
          key ID. A user can store more than one SSH public key associated with their user name on
          a specific SFTP server.

          - **DateImported** *(datetime) --*

            The date that the public key was added to the user account.

          - **SshPublicKeyBody** *(string) --*

            The content of the SSH public key as specified by the ``PublicKeyId`` .

          - **SshPublicKeyId** *(string) --*

            The ``SshPublicKeyId`` parameter contains the identifier of the public key.

      - **Tags** *(list) --*

        This property contains the key-value pairs for the user requested. Tag can be used to
        search for and group users for a variety of purposes.

        - *(dict) --*

          Creates a key-value pair for a specific resource. Tags are metadata that you can use to
          search for and group a resource for various purposes. You can apply tags to servers,
          users, and roles. A tag key can take more than one value. For example, to group servers
          for accounting purposes, you might create a tag called ``Group`` and assign the values
          ``Research`` and ``Accounting`` to that group.

          - **Key** *(string) --*

            The name assigned to the tag that you create.

          - **Value** *(string) --*

            This property contains one or more values that you assigned to the key name you create.

      - **UserName** *(string) --*

        This property is the name of the user that was requested to be described. User names are
        used for authentication purposes. This is the string that will be used by your user when
        they log in to your SFTP server.
    """


_ClientImportSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientImportSshPublicKeyResponseTypeDef",
    {"ServerId": str, "SshPublicKeyId": str, "UserName": str},
    total=False,
)


class ClientImportSshPublicKeyResponseTypeDef(_ClientImportSshPublicKeyResponseTypeDef):
    """
    Type definition for `ClientImportSshPublicKey` `Response`

    This response identifies the user, the server they belong to, and the identifier of the SSH
    public key associated with that user. A user can have more than one key on each server that
    they are associated with.

    - **ServerId** *(string) --*

      A system-assigned unique identifier for an SFTP server.

    - **SshPublicKeyId** *(string) --*

      This identifier is the name given to a public key by the system that was imported.

    - **UserName** *(string) --*

      A user name assigned to the ``ServerID`` value that you specified.
    """


_ClientListServersResponseServersTypeDef = TypedDict(
    "_ClientListServersResponseServersTypeDef",
    {
        "Arn": str,
        "IdentityProviderType": str,
        "EndpointType": str,
        "LoggingRole": str,
        "ServerId": str,
        "State": str,
        "UserCount": int,
    },
    total=False,
)


class ClientListServersResponseServersTypeDef(_ClientListServersResponseServersTypeDef):
    """
    Type definition for `ClientListServersResponse` `Servers`

    Returns properties of the server that was specified.

    - **Arn** *(string) --*

      The unique Amazon Resource Name (ARN) for the server to be listed.

    - **IdentityProviderType** *(string) --*

      The authentication method used to validate a user for the server that was specified. This
      can include Secure Shell (SSH), user name and password combinations, or your own custom
      authentication method. Valid values include ``SERVICE_MANAGED`` or ``API_GATEWAY`` .

    - **EndpointType** *(string) --*

      The type of VPC endpoint that your SFTP server is connected to. If your SFTP server is
      connected to a VPC endpoint, your server isn't accessible over the public internet.

    - **LoggingRole** *(string) --*

      The AWS Identity and Access Management entity that allows the server to turn on Amazon
      CloudWatch logging.

    - **ServerId** *(string) --*

      This value is the unique system assigned identifier for the SFTP servers that were listed.

    - **State** *(string) --*

      This property describes the condition of the SFTP server for the server that was
      described. A value of ``ONLINE`` > indicates that the server can accept jobs and transfer
      files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file
      transfer operations.

      The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an
      intermediate state, either not fully able to respond, or not fully offline. The values of
      ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

    - **UserCount** *(integer) --*

      This property is a numeric value that indicates the number of users that are assigned to
      the SFTP server you specified with the ``ServerId`` .
    """


_ClientListServersResponseTypeDef = TypedDict(
    "_ClientListServersResponseTypeDef",
    {"NextToken": str, "Servers": List[ClientListServersResponseServersTypeDef]},
    total=False,
)


class ClientListServersResponseTypeDef(_ClientListServersResponseTypeDef):
    """
    Type definition for `ClientListServers` `Response`

    - **NextToken** *(string) --*

      When you can get additional results from the ``ListServers`` operation, a ``NextToken``
      parameter is returned in the output. In a following command, you can pass in the
      ``NextToken`` parameter to continue listing additional servers.

    - **Servers** *(list) --*

      An array of servers that were listed.

      - *(dict) --*

        Returns properties of the server that was specified.

        - **Arn** *(string) --*

          The unique Amazon Resource Name (ARN) for the server to be listed.

        - **IdentityProviderType** *(string) --*

          The authentication method used to validate a user for the server that was specified. This
          can include Secure Shell (SSH), user name and password combinations, or your own custom
          authentication method. Valid values include ``SERVICE_MANAGED`` or ``API_GATEWAY`` .

        - **EndpointType** *(string) --*

          The type of VPC endpoint that your SFTP server is connected to. If your SFTP server is
          connected to a VPC endpoint, your server isn't accessible over the public internet.

        - **LoggingRole** *(string) --*

          The AWS Identity and Access Management entity that allows the server to turn on Amazon
          CloudWatch logging.

        - **ServerId** *(string) --*

          This value is the unique system assigned identifier for the SFTP servers that were listed.

        - **State** *(string) --*

          This property describes the condition of the SFTP server for the server that was
          described. A value of ``ONLINE`` > indicates that the server can accept jobs and transfer
          files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file
          transfer operations.

          The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an
          intermediate state, either not fully able to respond, or not fully offline. The values of
          ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

        - **UserCount** *(integer) --*

          This property is a numeric value that indicates the number of users that are assigned to
          the SFTP server you specified with the ``ServerId`` .
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

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to
    search for and group a resource for various purposes. You can apply tags to servers, users,
    and roles. A tag key can take more than one value. For example, to group servers for
    accounting purposes, you might create a tag called ``Group`` and assign the values
    ``Research`` and ``Accounting`` to that group.

    - **Key** *(string) --*

      The name assigned to the tag that you create.

    - **Value** *(string) --*

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "Arn": str,
        "NextToken": str,
        "Tags": List[ClientListTagsForResourceResponseTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Arn** *(string) --*

      This value is the ARN you specified to list the tags of.

    - **NextToken** *(string) --*

      When you can get additional results from the ``ListTagsForResource`` call, a ``NextToken``
      parameter is returned in the output. You can then pass in a subsequent command to the
      ``NextToken`` parameter to continue listing additional tags.

    - **Tags** *(list) --*

      Key-value pairs that are assigned to a resource, usually for the purpose of grouping and
      searching for items. Tags are metadata that you define.

      - *(dict) --*

        Creates a key-value pair for a specific resource. Tags are metadata that you can use to
        search for and group a resource for various purposes. You can apply tags to servers, users,
        and roles. A tag key can take more than one value. For example, to group servers for
        accounting purposes, you might create a tag called ``Group`` and assign the values
        ``Research`` and ``Accounting`` to that group.

        - **Key** *(string) --*

          The name assigned to the tag that you create.

        - **Value** *(string) --*

          This property contains one or more values that you assigned to the key name you create.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryType": str,
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    Returns properties of the user that you specify.

    - **Arn** *(string) --*

      This property is the unique Amazon Resource Name (ARN) for the user that you want to
      learn about.

    - **HomeDirectory** *(string) --*

      This value specifies the location that files are written to or read from an Amazon S3
      bucket for the user you specify by their ARN.

    - **HomeDirectoryType** *(string) --*

      The type of landing directory (folder) you mapped for your users' home directory. If you
      set it to ``PATH`` , the user will see the absolute Amazon S3 bucket paths as is in their
      SFTP clients. If you set it ``LOGICAL`` , you will need to provide mappings in the
      ``HomeDirectoryMappings`` for how you want to make S3 paths visible to your user.

    - **Role** *(string) --*

      The role in use by this user. A *role* is an AWS Identity and Access Management (IAM)
      entity that, in this case, allows the SFTP server to act on a user's behalf. It allows
      the server to inherit the trust relationship that enables that user to perform file
      operations to their Amazon S3 bucket.

    - **SshPublicKeyCount** *(integer) --*

      This value is the number of SSH public keys stored for the user you specified.

    - **UserName** *(string) --*

      The name of the user whose ARN was specified. User names are used for authentication
      purposes.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Users": List[ClientListUsersResponseUsersTypeDef],
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **NextToken** *(string) --*

      When you can get additional results from the ``ListUsers`` call, a ``NextToken`` parameter is
      returned in the output. You can then pass in a subsequent command to the ``NextToken``
      parameter to continue listing additional users.

    - **ServerId** *(string) --*

      A system-assigned unique identifier for an SFTP server that the users are assigned to.

    - **Users** *(list) --*

      Returns the user accounts and their properties for the ``ServerId`` value that you specify.

      - *(dict) --*

        Returns properties of the user that you specify.

        - **Arn** *(string) --*

          This property is the unique Amazon Resource Name (ARN) for the user that you want to
          learn about.

        - **HomeDirectory** *(string) --*

          This value specifies the location that files are written to or read from an Amazon S3
          bucket for the user you specify by their ARN.

        - **HomeDirectoryType** *(string) --*

          The type of landing directory (folder) you mapped for your users' home directory. If you
          set it to ``PATH`` , the user will see the absolute Amazon S3 bucket paths as is in their
          SFTP clients. If you set it ``LOGICAL`` , you will need to provide mappings in the
          ``HomeDirectoryMappings`` for how you want to make S3 paths visible to your user.

        - **Role** *(string) --*

          The role in use by this user. A *role* is an AWS Identity and Access Management (IAM)
          entity that, in this case, allows the SFTP server to act on a user's behalf. It allows
          the server to inherit the trust relationship that enables that user to perform file
          operations to their Amazon S3 bucket.

        - **SshPublicKeyCount** *(integer) --*

          This value is the number of SSH public keys stored for the user you specified.

        - **UserName** *(string) --*

          The name of the user whose ARN was specified. User names are used for authentication
          purposes.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
    for and group a resource for various purposes. You can apply tags to servers, users, and roles.
    A tag key can take more than one value. For example, to group servers for accounting purposes,
    you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting``
    to that group.

    - **Key** *(string) --* **[REQUIRED]**

      The name assigned to the tag that you create.

    - **Value** *(string) --* **[REQUIRED]**

      This property contains one or more values that you assigned to the key name you create.
    """


_ClientTestIdentityProviderResponseTypeDef = TypedDict(
    "_ClientTestIdentityProviderResponseTypeDef",
    {"Response": str, "StatusCode": int, "Message": str, "Url": str},
    total=False,
)


class ClientTestIdentityProviderResponseTypeDef(
    _ClientTestIdentityProviderResponseTypeDef
):
    """
    Type definition for `ClientTestIdentityProvider` `Response`

    - **Response** *(string) --*

      The response that is returned from your API Gateway.

    - **StatusCode** *(integer) --*

      The HTTP status code that is the response from your API Gateway.

    - **Message** *(string) --*

      A message that indicates whether the test was successful or not.

    - **Url** *(string) --*

      The endpoint of the service used to authenticate a user.
    """


_ClientUpdateServerEndpointDetailsTypeDef = TypedDict(
    "_ClientUpdateServerEndpointDetailsTypeDef", {"VpcEndpointId": str}, total=False
)


class ClientUpdateServerEndpointDetailsTypeDef(
    _ClientUpdateServerEndpointDetailsTypeDef
):
    """
    Type definition for `ClientUpdateServer` `EndpointDetails`

    The virtual private cloud (VPC) endpoint settings that are configured for your SFTP server. With
    a VPC endpoint, your SFTP server isn't accessible over the public internet.

    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint.
    """


_ClientUpdateServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientUpdateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientUpdateServerIdentityProviderDetailsTypeDef(
    _ClientUpdateServerIdentityProviderDetailsTypeDef
):
    """
    Type definition for `ClientUpdateServer` `IdentityProviderDetails`

    This response parameter is an array containing all of the information required to call a
    customer's authentication API method.

    - **Url** *(string) --*

      The ``Url`` parameter provides contains the location of the service endpoint used to
      authenticate users.

    - **InvocationRole** *(string) --*

      The ``InvocationRole`` parameter provides the type of ``InvocationRole`` used to authenticate
      the user account.
    """


_ClientUpdateServerResponseTypeDef = TypedDict(
    "_ClientUpdateServerResponseTypeDef", {"ServerId": str}, total=False
)


class ClientUpdateServerResponseTypeDef(_ClientUpdateServerResponseTypeDef):
    """
    Type definition for `ClientUpdateServer` `Response`

    - **ServerId** *(string) --*

      A system-assigned unique identifier for an SFTP server that the user account is assigned to.
    """


_ClientUpdateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientUpdateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}
)


class ClientUpdateUserHomeDirectoryMappingsTypeDef(
    _ClientUpdateUserHomeDirectoryMappingsTypeDef
):
    """
    Type definition for `ClientUpdateUser` `HomeDirectoryMappings`

    Represents an object that contains entries and a targets for ``HomeDirectoryMappings`` .

    - **Entry** *(string) --* **[REQUIRED]**

      Represents an entry and a target for ``HomeDirectoryMappings`` .

    - **Target** *(string) --* **[REQUIRED]**

      Represents the map target that is used in a ``HomeDirectorymapEntry`` .
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    Type definition for `ClientUpdateUser` `Response`

     ``UpdateUserResponse`` returns the user name and server identifier for the request to update a
     user's properties.

    - **ServerId** *(string) --*

      A system-assigned unique identifier for an SFTP server instance that the user account is
      assigned to.

    - **UserName** *(string) --*

      The unique identifier for a user that is assigned to the SFTP server instance that was
      specified in the request.
    """


_ListServersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServersPaginatePaginationConfigTypeDef(
    _ListServersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServersPaginate` `PaginationConfig`

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


_ListServersPaginateResponseServersTypeDef = TypedDict(
    "_ListServersPaginateResponseServersTypeDef",
    {
        "Arn": str,
        "IdentityProviderType": str,
        "EndpointType": str,
        "LoggingRole": str,
        "ServerId": str,
        "State": str,
        "UserCount": int,
    },
    total=False,
)


class ListServersPaginateResponseServersTypeDef(
    _ListServersPaginateResponseServersTypeDef
):
    """
    Type definition for `ListServersPaginateResponse` `Servers`

    Returns properties of the server that was specified.

    - **Arn** *(string) --*

      The unique Amazon Resource Name (ARN) for the server to be listed.

    - **IdentityProviderType** *(string) --*

      The authentication method used to validate a user for the server that was specified. This
      can include Secure Shell (SSH), user name and password combinations, or your own custom
      authentication method. Valid values include ``SERVICE_MANAGED`` or ``API_GATEWAY`` .

    - **EndpointType** *(string) --*

      The type of VPC endpoint that your SFTP server is connected to. If your SFTP server is
      connected to a VPC endpoint, your server isn't accessible over the public internet.

    - **LoggingRole** *(string) --*

      The AWS Identity and Access Management entity that allows the server to turn on Amazon
      CloudWatch logging.

    - **ServerId** *(string) --*

      This value is the unique system assigned identifier for the SFTP servers that were listed.

    - **State** *(string) --*

      This property describes the condition of the SFTP server for the server that was
      described. A value of ``ONLINE`` > indicates that the server can accept jobs and transfer
      files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file
      transfer operations.

      The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an
      intermediate state, either not fully able to respond, or not fully offline. The values of
      ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

    - **UserCount** *(integer) --*

      This property is a numeric value that indicates the number of users that are assigned to
      the SFTP server you specified with the ``ServerId`` .
    """


_ListServersPaginateResponseTypeDef = TypedDict(
    "_ListServersPaginateResponseTypeDef",
    {"Servers": List[ListServersPaginateResponseServersTypeDef]},
    total=False,
)


class ListServersPaginateResponseTypeDef(_ListServersPaginateResponseTypeDef):
    """
    Type definition for `ListServersPaginate` `Response`

    - **Servers** *(list) --*

      An array of servers that were listed.

      - *(dict) --*

        Returns properties of the server that was specified.

        - **Arn** *(string) --*

          The unique Amazon Resource Name (ARN) for the server to be listed.

        - **IdentityProviderType** *(string) --*

          The authentication method used to validate a user for the server that was specified. This
          can include Secure Shell (SSH), user name and password combinations, or your own custom
          authentication method. Valid values include ``SERVICE_MANAGED`` or ``API_GATEWAY`` .

        - **EndpointType** *(string) --*

          The type of VPC endpoint that your SFTP server is connected to. If your SFTP server is
          connected to a VPC endpoint, your server isn't accessible over the public internet.

        - **LoggingRole** *(string) --*

          The AWS Identity and Access Management entity that allows the server to turn on Amazon
          CloudWatch logging.

        - **ServerId** *(string) --*

          This value is the unique system assigned identifier for the SFTP servers that were listed.

        - **State** *(string) --*

          This property describes the condition of the SFTP server for the server that was
          described. A value of ``ONLINE`` > indicates that the server can accept jobs and transfer
          files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file
          transfer operations.

          The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an
          intermediate state, either not fully able to respond, or not fully offline. The values of
          ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

        - **UserCount** *(integer) --*

          This property is a numeric value that indicates the number of users that are assigned to
          the SFTP server you specified with the ``ServerId`` .
    """
