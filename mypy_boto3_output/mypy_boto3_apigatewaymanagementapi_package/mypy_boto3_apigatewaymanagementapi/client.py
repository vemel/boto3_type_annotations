"Main interface for apigatewaymanagementapi Client"
from __future__ import annotations

from typing import Dict, IO, Union
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from mypy_boto3_apigatewaymanagementapi.type_defs import (
    ClientGetConnectionResponseTypeDef,
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
    def delete_connection(self, ConnectionId: str) -> None:
        """
        Delete the connection with the provided id.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewaymanagementapi-2018-11-29/DeleteConnection>`_

        **Request Syntax**
        ::

          response = client.delete_connection(
              ConnectionId='string'
          )
        :type ConnectionId: string
        :param ConnectionId: **[REQUIRED]**

        :returns: None
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
    def get_connection(self, ConnectionId: str) -> ClientGetConnectionResponseTypeDef:
        """
        Get information about the connection with the provided id.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewaymanagementapi-2018-11-29/GetConnection>`_

        **Request Syntax**
        ::

          response = client.get_connection(
              ConnectionId='string'
          )
        :type ConnectionId: string
        :param ConnectionId: **[REQUIRED]**

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConnectedAt': datetime(2015, 1, 1),
                'Identity': {
                    'SourceIp': 'string',
                    'UserAgent': 'string'
                },
                'LastActiveAt': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **ConnectedAt** *(datetime) --*

              The time in ISO 8601 format for when the connection was established.

            - **Identity** *(dict) --*

              - **SourceIp** *(string) --*

                The source IP address of the TCP connection making the request to API Gateway.

              - **UserAgent** *(string) --*

                The User Agent of the API caller.

            - **LastActiveAt** *(datetime) --*

              The time in ISO 8601 format for when the connection was last active.

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
    def post_to_connection(self, Data: Union[bytes, IO], ConnectionId: str) -> None:
        """
        Sends the provided data to the specified connection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewaymanagementapi-2018-11-29/PostToConnection>`_

        **Request Syntax**
        ::

          response = client.post_to_connection(
              Data=b'bytes'|file,
              ConnectionId='string'
          )
        :type Data: bytes or seekable file-like object
        :param Data: **[REQUIRED]**

          The data to be sent to the client specified by its connection id.

        :type ConnectionId: string
        :param ConnectionId: **[REQUIRED]**

          The identifier of the connection that a specific client is using.

        :returns: None
        """
