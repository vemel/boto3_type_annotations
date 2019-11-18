"Main interface for iot-data Client"
from __future__ import annotations

from typing import Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot_data.client as client_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_thing_shadow(self, thingName: str) -> Dict:
        """
        Deletes the thing shadow for the specified thing.

        For more information, see `DeleteThingShadow
        <http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html>`__ in the *AWS
        IoT Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/DeleteThingShadow>`_

        **Request Syntax**
        ::

          response = client.delete_thing_shadow(
              thingName='string'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]**

          The name of the thing.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'payload': StreamingBody()
            }
          **Response Structure**

          - *(dict) --*

            The output from the DeleteThingShadow operation.

            - **payload** (:class:`.StreamingBody`) --

              The state information, in JSON format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_thing_shadow(self, thingName: str) -> Dict:
        """
        Gets the thing shadow for the specified thing.

        For more information, see `GetThingShadow
        <http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html>`__ in the *AWS IoT
        Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/GetThingShadow>`_

        **Request Syntax**
        ::

          response = client.get_thing_shadow(
              thingName='string'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]**

          The name of the thing.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'payload': StreamingBody()
            }
          **Response Structure**

          - *(dict) --*

            The output from the GetThingShadow operation.

            - **payload** (:class:`.StreamingBody`) --

              The state information, in JSON format.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish(
        self, topic: str, qos: int = None, payload: Union[bytes, IO] = None
    ) -> None:
        """
        Publishes state information.

        For more information, see `HTTP Protocol
        <http://docs.aws.amazon.com/iot/latest/developerguide/protocols.html#http>`__ in the *AWS IoT
        Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/Publish>`_

        **Request Syntax**
        ::

          response = client.publish(
              topic='string',
              qos=123,
              payload=b'bytes'|file
          )
        :type topic: string
        :param topic: **[REQUIRED]**

          The name of the MQTT topic.

        :type qos: integer
        :param qos:

          The Quality of Service (QoS) level.

        :type payload: bytes or seekable file-like object
        :param payload:

          The state information, in JSON format.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_thing_shadow(self, thingName: str, payload: Union[bytes, IO]) -> Dict:
        """
        Updates the thing shadow for the specified thing.

        For more information, see `UpdateThingShadow
        <http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html>`__ in the *AWS
        IoT Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/UpdateThingShadow>`_

        **Request Syntax**
        ::

          response = client.update_thing_shadow(
              thingName='string',
              payload=b'bytes'|file
          )
        :type thingName: string
        :param thingName: **[REQUIRED]**

          The name of the thing.

        :type payload: bytes or seekable file-like object
        :param payload: **[REQUIRED]**

          The state information, in JSON format.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'payload': StreamingBody()
            }
          **Response Structure**

          - *(dict) --*

            The output from the UpdateThingShadow operation.

            - **payload** (:class:`.StreamingBody`) --

              The state information, in JSON format.

        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    RequestEntityTooLargeException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    UnsupportedDocumentEncodingException: Boto3ClientError
