"Main interface for ec2-instance-connect Client"
from __future__ import annotations

from typing import Dict
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from mypy_boto3_ec2_instance_connect.type_defs import (
    ClientSendSshPublicKeyResponseTypeDef,
)


class Client(BaseClient):
    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str) -> Paginator:
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

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str) -> Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """

    # pylint: disable=arguments-differ
    def send_ssh_public_key(
        self,
        InstanceId: str,
        InstanceOSUser: str,
        SSHPublicKey: str,
        AvailabilityZone: str,
    ) -> ClientSendSshPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to a particular OS user on a given EC2 instance for 60 seconds.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ec2-instance-connect-2018-04-02/SendSSHPublicKey>`_

        **Request Syntax**
        ::

          response = client.send_ssh_public_key(
              InstanceId='string',
              InstanceOSUser='string',
              SSHPublicKey='string',
              AvailabilityZone='string'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The EC2 instance you wish to publish the SSH key to.

        :type InstanceOSUser: string
        :param InstanceOSUser: **[REQUIRED]**

          The OS user on the EC2 instance whom the key may be used to authenticate as.

        :type SSHPublicKey: string
        :param SSHPublicKey: **[REQUIRED]**

          The public key to be published to the instance. To use it after publication you must have the
          matching private key.

        :type AvailabilityZone: string
        :param AvailabilityZone: **[REQUIRED]**

          The availability zone the EC2 instance was launched in.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestId': 'string',
                'Success': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **RequestId** *(string) --*

              The request ID as logged by EC2 Connect. Please provide this when contacting AWS Support.

            - **Success** *(boolean) --*

              Indicates request success.

        """
