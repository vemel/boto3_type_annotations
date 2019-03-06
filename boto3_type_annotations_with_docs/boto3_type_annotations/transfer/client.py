from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def create_server(self, IdentityProviderDetails: Dict = None, IdentityProviderType: str = None, LoggingRole: str = None, Tags: List = None) -> Dict:
        """
        Instantiates an autoscaling virtual server based on Secure File Transfer Protocol (SFTP) in AWS. The call returns the ``ServerId`` property assigned by the service to the newly created server. Reference this ``ServerId`` property when you make updates to your server, or work with users.
        The response returns the ``ServerId`` value for the newly created server.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/CreateServer>`_
        
        **Request Syntax**
        ::
          response = client.create_server(
              IdentityProviderDetails={
                  'Url': 'string',
                  'InvocationRole': 'string'
              },
              IdentityProviderType='SERVICE_MANAGED'|'API_GATEWAY',
              LoggingRole='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerId** *(string) --* 
              The service-assigned ID of the SFTP server that is created.
        :type IdentityProviderDetails: dict
        :param IdentityProviderDetails:
          An array containing all of the information required to call a customer-supplied authentication API. This parameter is not required when the ``IdentityProviderType`` value of server that is created uses the ``SERVICE_MANAGED`` authentication method.
          - **Url** *(string) --*
            The ``IdentityProviderDetail`` parameter contains the location of the service endpoint used to authenticate users.
          - **InvocationRole** *(string) --*
            The ``Role`` parameter provides the type of ``InvocationRole`` used to authenticate the user account.
        :type IdentityProviderType: string
        :param IdentityProviderType:
          The mode of authentication enabled for this service. The default value is ``SERVICE_MANAGED`` , which allows you to store and access SFTP user credentials within the service. An ``IdentityProviderType`` value of ``API_GATEWAY`` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
        :type LoggingRole: string
        :param LoggingRole:
          A value that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
        :type Tags: list
        :param Tags:
          Key-value pairs that can be used to group and search for servers.
          - *(dict) --*
            Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
            - **Key** *(string) --* **[REQUIRED]**
              The name assigned to the tag that you create.
            - **Value** *(string) --* **[REQUIRED]**
              This property contains one or more values that you assigned to the key name you create.
        :rtype: dict
        :returns:
        """
        pass

    def create_user(self, Role: str, ServerId: str, UserName: str, HomeDirectory: str = None, Policy: str = None, SshPublicKeyBody: str = None, Tags: List = None) -> Dict:
        """
        Adds a user and associate them with an existing Secure File Transfer Protocol (SFTP) server. Using parameters for ``CreateUser`` , you can specify the user name, set the home directory, store the user's public key, and assign the user's AWS Identity and Access Management (IAM) role. You can also optionally add a scope-down policy, and assign metadata with tags that can be used to group and search for users.
        The response returns the ``UserName`` and ``ServerId`` values of the new user for that server.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/CreateUser>`_
        
        **Request Syntax**
        ::
          response = client.create_user(
              HomeDirectory='string',
              Policy='string',
              Role='string',
              ServerId='string',
              SshPublicKeyBody='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              UserName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string',
                'UserName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerId** *(string) --* 
              The ID of the SFTP server that the user is attached to.
            - **UserName** *(string) --* 
              A unique string that identifies a user account associated with an SFTP server.
        :type HomeDirectory: string
        :param HomeDirectory:
          The landing directory (folder) for a user when they log in to the server using their SFTP client. An example is ``/home/*username* `` .
        :type Policy: string
        :param Policy:
          A scope-down policy for your user so you can use the same IAM role across multiple users. This policy scopes down user access to portions of their Amazon S3 bucket. Variables you can use inside this policy include ``${Transfer:UserName}`` , ``${Transfer:HomeDirectory}`` , and ``${Transfer:HomeBucket}`` .
        :type Role: string
        :param Role: **[REQUIRED]**
          The IAM role that controls your user’s access to your Amazon S3 bucket. The policies attached to this role will determine the level of access you want to provide your users when transferring files into and out of your Amazon S3 bucket or buckets. The IAM role should also contain a trust relationship that allows the SFTP server to access your resources when servicing your SFTP user’s transfer requests.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server instance. This is the specific SFTP server that you added your user to.
        :type SshPublicKeyBody: string
        :param SshPublicKeyBody:
          The public portion of the Secure Shall (SSH) key used to authenticate the user to the SFTP server.
        :type Tags: list
        :param Tags:
          Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.
          - *(dict) --*
            Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
            - **Key** *(string) --* **[REQUIRED]**
              The name assigned to the tag that you create.
            - **Value** *(string) --* **[REQUIRED]**
              This property contains one or more values that you assigned to the key name you create.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          A unique string that identifies a user and is associated with a server as specified by the ``ServerId`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_server(self, ServerId: str):
        """
        Deletes the Secure File Transfer Protocol (SFTP) server that you specify. If you used ``SERVICE_MANAGED`` as your ``IdentityProviderType`` , you need to delete all users associated with this server before deleting the server itself
        No response returns from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DeleteServer>`_
        
        **Request Syntax**
        ::
          response = client.delete_server(
              ServerId='string'
          )
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A unique system-assigned identifier for an SFTP server instance.
        :returns: None
        """
        pass

    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str):
        """
        Deletes a user's Secure Shell (SSH) public key.
        No response is returned from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DeleteSshPublicKey>`_
        
        **Request Syntax**
        ::
          response = client.delete_ssh_public_key(
              ServerId='string',
              SshPublicKeyId='string',
              UserName='string'
          )
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for a Secure File Transfer Protocol (SFTP) server instance that has the user assigned to it.
        :type SshPublicKeyId: string
        :param SshPublicKeyId: **[REQUIRED]**
          A unique identifier used to reference your user’s specific SSH key.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          A unique string that identifies a user whose public key is being deleted.
        :returns: None
        """
        pass

    def delete_user(self, ServerId: str, UserName: str):
        """
        Deletes the user belonging to the server you specify.
        No response returns from this call.
        .. note::
          When you delete a user from a server, the user's information is lost.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DeleteUser>`_
        
        **Request Syntax**
        ::
          response = client.delete_user(
              ServerId='string',
              UserName='string'
          )
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server instance that has the user assigned to it.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          A unique string that identifies a user that is being deleted from the server.
        :returns: None
        """
        pass

    def describe_server(self, ServerId: str) -> Dict:
        """
        Describes the server that you specify by passing the ``ServerId`` parameter.
        The response contains a description of the server's properties.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeServer>`_
        
        **Request Syntax**
        ::
          response = client.describe_server(
              ServerId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Server': {
                    'Arn': 'string',
                    'IdentityProviderDetails': {
                        'Url': 'string',
                        'InvocationRole': 'string'
                    },
                    'IdentityProviderType': 'SERVICE_MANAGED'|'API_GATEWAY',
                    'LoggingRole': 'string',
                    'ServerId': 'string',
                    'State': 'OFFLINE'|'ONLINE'|'STARTING'|'STOPPING'|'START_FAILED'|'STOP_FAILED',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'UserCount': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Server** *(dict) --* 
              An array containing the properties of the server with the ``ServerID`` you specified.
              - **Arn** *(string) --* 
                Specifies the unique Amazon Resource Name (ARN) for the server to be described.
              - **IdentityProviderDetails** *(dict) --* 
                Specifies information to call a customer-supplied authentication API. This field is not populated when the ``IdentityProviderType`` of the server is ``SERVICE_MANAGED`` >.
                - **Url** *(string) --* 
                  The ``IdentityProviderDetail`` parameter contains the location of the service endpoint used to authenticate users.
                - **InvocationRole** *(string) --* 
                  The ``Role`` parameter provides the type of ``InvocationRole`` used to authenticate the user account.
              - **IdentityProviderType** *(string) --* 
                This property defines the mode of authentication method enabled for this service. A value of ``SERVICE_MANAGED`` , means that you are using this Server to store and access SFTP user credentials within the service. A value of ``API_GATEWAY`` indicates that you have integrated an API Gateway endpoint that will be invoked for authenticating your user into the service.
              - **LoggingRole** *(string) --* 
                This property is an AWS Identity and Access Management (IAM) entity that allows the server to turn on Amazon CloudWatch logging for Amazon S3 events. When set, user activity can be view in your CloudWatch logs.
              - **ServerId** *(string) --* 
                This property is a unique system assigned identifier for the SFTP server that you instantiate.
              - **State** *(string) --* 
                The condition of the SFTP server for the server that was described. A value of ``ONLINE`` indicates that the server can accept jobs and transfer files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file transfer operations.
                The states of ``STARTING`` and ``STOPPING`` indicated that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.
              - **Tags** *(list) --* 
                This property contains the key-value pairs that you can use to search for and group servers that were assigned to the server that was described.
                - *(dict) --* 
                  Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
                  - **Key** *(string) --* 
                    The name assigned to the tag that you create.
                  - **Value** *(string) --* 
                    This property contains one or more values that you assigned to the key name you create.
              - **UserCount** *(integer) --* 
                The number of users that are assigned to the SFTP server you specified with the ``ServerId`` .
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server.
        :rtype: dict
        :returns:
        """
        pass

    def describe_user(self, ServerId: str, UserName: str) -> Dict:
        """
        Describes the user assigned to a specific server, as identified by its ``ServerId`` property.
        The response from this call returns the properties of the user associated with the ``ServerId`` value that was specified.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeUser>`_
        
        **Request Syntax**
        ::
          response = client.describe_user(
              ServerId='string',
              UserName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string',
                'User': {
                    'Arn': 'string',
                    'HomeDirectory': 'string',
                    'Policy': 'string',
                    'Role': 'string',
                    'SshPublicKeys': [
                        {
                            'DateImported': datetime(2015, 1, 1),
                            'SshPublicKeyBody': 'string',
                            'SshPublicKeyId': 'string'
                        },
                    ],
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'UserName': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerId** *(string) --* 
              A system-assigned unique identifier for an SFTP server that has this user assigned.
            - **User** *(dict) --* 
              An array containing the properties of the user account for the ``ServerID`` value that you specified.
              - **Arn** *(string) --* 
                This property contains the unique Amazon Resource Name (ARN) for the user that was requested to be described.
              - **HomeDirectory** *(string) --* 
                This property specifies the landing directory (or folder) which is the location that files are written to or read from in an Amazon S3 bucket for the described user. An example would be: ``/*bucket_name* /home/*username* `` .
              - **Policy** *(string) --* 
                Specifies the name of the policy in use for the described user.
              - **Role** *(string) --* 
                This property specifies the IAM role that controls your user’s access to your Amazon S3 bucket. The policies attached to this role will determine the level of access you want to provide your users when transferring files into and out of your Amazon S3 bucket or buckets. The IAM role should also contain a trust relationship that allows the SFTP server to access your resources when servicing your SFTP user’s transfer requests.
              - **SshPublicKeys** *(list) --* 
                This property contains the public key portion of the Secure Shell (SSH) keys stored for the described user.
                - *(dict) --* 
                  Provides information about the public Secure Shell (SSH) key that is associated with a user account for a specific server (as identified by ``ServerId`` ). The information returned includes the date the key was imported, the public key contents, and the public key ID. A user can store more than one SSH public key associated with their user name on a specific SFTP server.
                  - **DateImported** *(datetime) --* 
                    The date that the public key was added to the user account.
                  - **SshPublicKeyBody** *(string) --* 
                    The content of the SSH public key as specified by the ``PublicKeyId`` .
                  - **SshPublicKeyId** *(string) --* 
                    The ``SshPublicKeyId`` parameter contains the identifier of the public key.
              - **Tags** *(list) --* 
                This property contains the key-value pairs for the user requested. Tag can be used to search for and group users for a variety of purposes.
                - *(dict) --* 
                  Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
                  - **Key** *(string) --* 
                    The name assigned to the tag that you create.
                  - **Value** *(string) --* 
                    This property contains one or more values that you assigned to the key name you create.
              - **UserName** *(string) --* 
                This property is the name of the user that was requested to be described. User names are used for authentication purposes. This is the string that will be used by your user when they log in to your SFTP server.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server that has this user assigned.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the AWS Transfer service and perform file transfer tasks.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def import_ssh_public_key(self, ServerId: str, SshPublicKeyBody: str, UserName: str) -> Dict:
        """
        Adds a Secure Shell (SSH) public key to a user account identified by a ``UserName`` value assigned to a specific server, identified by ``ServerId`` .
        The response returns the ``UserName`` value, the ``ServerId`` value, and the name of the ``SshPublicKeyId`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ImportSshPublicKey>`_
        
        **Request Syntax**
        ::
          response = client.import_ssh_public_key(
              ServerId='string',
              SshPublicKeyBody='string',
              UserName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string',
                'SshPublicKeyId': 'string',
                'UserName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            This response identifies the user, server they belong to, and the identifier of the SSH public key associated with that user. A user can have more than one key on each server that they are associate with.
            - **ServerId** *(string) --* 
              A system-assigned unique identifier for an SFTP server.
            - **SshPublicKeyId** *(string) --* 
              This identifier is the name given to a public key by the system that was imported.
            - **UserName** *(string) --* 
              A user name assigned to the ``ServerID`` value that you specified.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server.
        :type SshPublicKeyBody: string
        :param SshPublicKeyBody: **[REQUIRED]**
          The public key portion of an SSH key pair.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The name of the user account that is assigned to one or more servers.
        :rtype: dict
        :returns:
        """
        pass

    def list_servers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists the Secure File Transfer Protocol (SFTP) servers that are associated with your AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ListServers>`_
        
        **Request Syntax**
        ::
          response = client.list_servers(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'Servers': [
                    {
                        'Arn': 'string',
                        'IdentityProviderType': 'SERVICE_MANAGED'|'API_GATEWAY',
                        'LoggingRole': 'string',
                        'ServerId': 'string',
                        'State': 'OFFLINE'|'ONLINE'|'STARTING'|'STOPPING'|'START_FAILED'|'STOP_FAILED',
                        'UserCount': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              When you can get additional results from the ``ListServers`` operation, a ``NextToken`` parameter is returned in the output. In a following command, you can pass in the ``NextToken`` parameter to continue listing additional servers.
            - **Servers** *(list) --* 
              An array of servers that were listed.
              - *(dict) --* 
                Returns properties of the server that was specified.
                - **Arn** *(string) --* 
                  The unique Amazon Resource Name (ARN) for the server to be listed.
                - **IdentityProviderType** *(string) --* 
                  The authentication method used to validate a user for the server that was specified. listed. This can include Secure Shell (SSH), user name and password combinations, or your own custom authentication method. Valid values include ``SERVICE_MANAGED`` or ``API_GATEWAY`` .
                - **LoggingRole** *(string) --* 
                  The AWS Identity and Access Management entity that allows the server to turn on Amazon CloudWatch logging.
                - **ServerId** *(string) --* 
                  This value is the unique system assigned identifier for the SFTP servers that were listed.
                - **State** *(string) --* 
                  This property describes the condition of the SFTP server for the server that was described. A value of ``ONLINE`` > indicates that the server can accept jobs and transfer files. A ``State`` value of ``OFFLINE`` means that the server cannot perform file transfer operations.
                  The states of ``STARTING`` and ``STOPPING`` indicated that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.
                - **UserCount** *(integer) --* 
                  This property is a numeric value that indicates the number of users that are assigned to the SFTP server you specified with the ``ServerId`` .
        :type MaxResults: integer
        :param MaxResults:
          Specifies the number of servers to return as a response to the ``ListServers`` query.
        :type NextToken: string
        :param NextToken:
          When additional results are obtained from the ListServers command, a ``NextToken`` parameter is returned in the output. You can then pass the ``NextToken`` parameter in a subsequent command to continue listing additional servers.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, Arn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists all of the tags associated with the Amazon Resource Number (ARN) you specify. The resource can be a user, server, or role.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              Arn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Arn': 'string',
                'NextToken': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Arn** *(string) --* 
              This value is the ARN you specified to list the tags of.
            - **NextToken** *(string) --* 
              When you can get additional results from the ``ListTagsForResource`` call, a ``NextToken`` parameter is returned in the output. You can then pass in a subsequent command the ``NextToken`` parameter to continue listing additional tags.
            - **Tags** *(list) --* 
              Key-value pairs that are assigned to a resource, usually for the purpose of grouping and searching for items. Tags are metadata that you define that you can use for any purpose.
              - *(dict) --* 
                Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
                - **Key** *(string) --* 
                  The name assigned to the tag that you create.
                - **Value** *(string) --* 
                  This property contains one or more values that you assigned to the key name you create.
        :type Arn: string
        :param Arn: **[REQUIRED]**
          Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific AWS resource, such as a server, user, or role.
        :type MaxResults: integer
        :param MaxResults:
          Specifies the number of tags to return as a response to the ``ListTagsForResource`` request.
        :type NextToken: string
        :param NextToken:
          When you request additional results from the ``ListTagsForResource`` call, a ``NextToken`` parameter is returned in the input. You can then pass in a subsequent command the ``NextToken`` parameter to continue listing additional tags.
        :rtype: dict
        :returns:
        """
        pass

    def list_users(self, ServerId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists the users for the server that you specify by passing the ``ServerId`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ListUsers>`_
        
        **Request Syntax**
        ::
          response = client.list_users(
              MaxResults=123,
              NextToken='string',
              ServerId='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'ServerId': 'string',
                'Users': [
                    {
                        'Arn': 'string',
                        'HomeDirectory': 'string',
                        'Role': 'string',
                        'SshPublicKeyCount': 123,
                        'UserName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              When you can get additional results from the ``ListUsers`` call, a ``NextToken`` parameter is returned in the output. You can then pass in a subsequent command the ``NextToken`` parameter to continue listing additional users.
            - **ServerId** *(string) --* 
              A system-assigned unique identifier for an SFTP server that the users are assigned to.
            - **Users** *(list) --* 
              Returns the user accounts and their properties for the ``ServerId`` value that you specify.
              - *(dict) --* 
                Returns properties of the user that you specify.
                - **Arn** *(string) --* 
                  This property is the unique Amazon Resource Name (ARN) for the user that you wish to learn about.
                - **HomeDirectory** *(string) --* 
                  This value specifies the location that files are written to or read from an Amazon S3 bucket for the user you specify by their ARN.
                - **Role** *(string) --* 
                  The role in use by this user. A *role* is an AWS Identity and Access Management (IAM) entity that in this case allows the SFTP server to act on a user's behalf. It allows the server to inherit the trust relationship that enables that user to perform file operations to their Amazon S3 bucket.
                - **SshPublicKeyCount** *(integer) --* 
                  This value is the number of SSH public keys stored for the user you specified.
                - **UserName** *(string) --* 
                  The name of the user whose ARN was specified. User names are used for authentication purposes.
        :type MaxResults: integer
        :param MaxResults:
          Specifies the number of users to return as a response to the ``ListUsers`` request.
        :type NextToken: string
        :param NextToken:
          When you can get additional results from the ``ListUsers`` call, a ``NextToken`` parameter is returned in the output. You can then pass in a subsequent command the ``NextToken`` parameter to continue listing additional users.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for a Secure File Transfer Protocol (SFTP) server that has users are assigned to it.
        :rtype: dict
        :returns:
        """
        pass

    def start_server(self, ServerId: str):
        """
        Changes the state of a Secure File Transfer Protocol (SFTP) server from ``OFFLINE`` to ``ONLINE`` . It has no impact on an SFTP server that is already ``ONLINE`` . An ``ONLINE`` server can accept and process file transfer jobs.
        The state of ``STARTING`` indicates that the server is in an intermediate state, either not fully able to respond, or not fully online. The values of ``START_FAILED`` can indicate an error condition. 
        No response is returned from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/StartServer>`_
        
        **Request Syntax**
        ::
          response = client.start_server(
              ServerId='string'
          )
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server that you start.
        :returns: None
        """
        pass

    def stop_server(self, ServerId: str):
        """
        Changes the state of an SFTP server from ``ONLINE`` to ``OFFLINE`` . An ``OFFLINE`` server cannot accept and process file transfer jobs. Information tied to your server such as server and user properties are not affected by stopping your server. Stopping a server will not reduce or impact your Secure File Transfer Protocol (SFTP) endpoint billing.
        The states of ``STOPPING`` indicates that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of ``STOP_FAILED`` can indicate an error condition.
        No response is returned from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/StopServer>`_
        
        **Request Syntax**
        ::
          response = client.stop_server(
              ServerId='string'
          )
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server that you stopped.
        :returns: None
        """
        pass

    def tag_resource(self, Arn: str, Tags: List):
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.
        There is no response returned from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              Arn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**
          An Amazon Resource Name (ARN) for a specific AWS resource, such as a server, user, or role.
        :type Tags: list
        :param Tags: **[REQUIRED]**
          Key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to user accounts for any purpose.
          - *(dict) --*
            Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called ``Group`` and assign the values ``Research`` and ``Accounting`` to that group.
            - **Key** *(string) --* **[REQUIRED]**
              The name assigned to the tag that you create.
            - **Value** *(string) --* **[REQUIRED]**
              This property contains one or more values that you assigned to the key name you create.
        :returns: None
        """
        pass

    def test_identity_provider(self, ServerId: str, UserName: str, UserPassword: str = None) -> Dict:
        """
        If the ``IdentityProviderType`` of the server is ``API_Gateway`` , tests whether your API Gateway is set up successfully. We highly recommend that you call this method to test your authentication method as soon as you create your server. By doing so, you can troubleshoot issues with the API Gateway integration to ensure that your users can successfully use the service.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/TestIdentityProvider>`_
        
        **Request Syntax**
        ::
          response = client.test_identity_provider(
              ServerId='string',
              UserName='string',
              UserPassword='string'
          )
        
        **Response Syntax**
        ::
            {
                'Message': 'string',
                'StatusCode': 123,
                'Url': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Message** *(string) --* 
              The result of the authorization test as a message. 
            - **StatusCode** *(integer) --* 
              The HTTP status code that is the response from your API Gateway.
            - **Url** *(string) --* 
              The endpoint of the service used to authenticate a user.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system assigned identifier for a specific server. That server\'s user authentication method is tested with a user name and password.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          This request parameter is name of the user account to be tested.
        :type UserPassword: string
        :param UserPassword:
          The password of the user account to be tested.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, Arn: str, TagKeys: List):
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.
        No response is returned from this call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              Arn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**
          This is the value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.
          - *(string) --*
        :returns: None
        """
        pass

    def update_server(self, ServerId: str, IdentityProviderDetails: Dict = None, LoggingRole: str = None) -> Dict:
        """
        Updates the server properties after that server has been created.
        The ``UpdateServer`` call returns the ``ServerId`` of the Secure File Transfer Protocol (SFTP) server you updated.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/UpdateServer>`_
        
        **Request Syntax**
        ::
          response = client.update_server(
              IdentityProviderDetails={
                  'Url': 'string',
                  'InvocationRole': 'string'
              },
              LoggingRole='string',
              ServerId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerId** *(string) --* 
              A system-assigned unique identifier for an SFTP server that the user account is assigned to.
        :type IdentityProviderDetails: dict
        :param IdentityProviderDetails:
          This response parameter is an array containing all of the information required to call a customer\'s authentication API method.
          - **Url** *(string) --*
            The ``IdentityProviderDetail`` parameter contains the location of the service endpoint used to authenticate users.
          - **InvocationRole** *(string) --*
            The ``Role`` parameter provides the type of ``InvocationRole`` used to authenticate the user account.
        :type LoggingRole: string
        :param LoggingRole:
          Changes the AWS Identity and Access Management (IAM) role that allows Amazon S3 events to be logged in Amazon CloudWatch, turning logging on or off.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server instance that the user account is assigned to.
        :rtype: dict
        :returns:
        """
        pass

    def update_user(self, ServerId: str, UserName: str, HomeDirectory: str = None, Policy: str = None, Role: str = None) -> Dict:
        """
        Assigns new properties to a user. Parameters you pass modify any or all of the following: the home directory, role, and policy for the ``UserName`` and ``ServerId`` you specify.
        The response returns the ``ServerId`` and the ``UserName`` for the updated user.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/UpdateUser>`_
        
        **Request Syntax**
        ::
          response = client.update_user(
              HomeDirectory='string',
              Policy='string',
              Role='string',
              ServerId='string',
              UserName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerId': 'string',
                'UserName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
             ``UpdateUserResponse`` returns the user name and server identifier for the request to update a user's properties.
            - **ServerId** *(string) --* 
              A system-assigned unique identifier for an SFTP server instance that the user account is assigned to.
            - **UserName** *(string) --* 
              The unique identifier for a user that is assigned to the SFTP server instance that was specified in the request.
        :type HomeDirectory: string
        :param HomeDirectory:
          The HomeDirectory parameter specifies the landing directory (folder) for a user when they log in to the server using their client. An example would be: ``/home/*username* `` .
        :type Policy: string
        :param Policy:
          Allows you to supply a scope-down policy for your user so you can use the same AWS Identity and Access Management (IAM) role across multiple users. The policy scopes down users access to portions of your Amazon S3 bucket. Variables you can use inside this policy include ``${Transfer:UserName}`` , ``${Transfer:HomeDirectory}`` , and ``${Transfer:HomeBucket}`` .
        :type Role: string
        :param Role:
          The IAM role that controls your user’s access to your Amazon S3 bucket. The policies attached to this role will determine the level of access you want to provide your users when transferring files into and out of your Amazon S3 bucket or buckets. The IAM role should also contain a trust relationship that allows the Secure File Transfer Protocol (SFTP) server to access your resources when servicing your SFTP user’s transfer requests.
        :type ServerId: string
        :param ServerId: **[REQUIRED]**
          A system-assigned unique identifier for an SFTP server instance that the user account is assigned to.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          A unique string that identifies a user and is associated with a server as specified by the ServerId. This is the string that will be used by your user when they log in to your SFTP server.
        :rtype: dict
        :returns:
        """
        pass
