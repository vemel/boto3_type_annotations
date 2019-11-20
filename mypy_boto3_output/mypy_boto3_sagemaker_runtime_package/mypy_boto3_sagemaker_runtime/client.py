"Main interface for sagemaker-runtime Client"
from __future__ import annotations

from typing import Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sagemaker_runtime.client as client_scope
from mypy_boto3_sagemaker_runtime.type_defs import ClientInvokeEndpointResponseTypeDef


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
    def invoke_endpoint(
        self,
        EndpointName: str,
        Body: Union[bytes, IO],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetModel: str = None,
    ) -> ClientInvokeEndpointResponseTypeDef:
        """
        After you deploy a model into production using Amazon SageMaker hosting services, your client
        applications use this API to get inferences from the model hosted at the specified endpoint.

        For an overview of Amazon SageMaker, see `How It Works
        <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ .

        Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might
        add additional headers. You should not rely on the behavior of headers outside those enumerated in
        the request syntax.

        Calls to ``InvokeEndpoint`` are authenticated by using AWS Signature Version 4. For information,
        see `Authenticating Requests (AWS Signature Version 4)
        <http://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html>`__ in the
        *Amazon S3 API Reference* .

        A customer's model containers must respond to requests within 60 seconds. The model itself can have
        a maximum processing time of 60 seconds before responding to the /invocations. If your model is
        going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70
        seconds.

        .. note::

          Endpoints are scoped to an individual account, and are not public. The URL does not contain the
          account ID, but Amazon SageMaker determines the account ID from the authentication token that is
          supplied by the caller.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.sagemaker-2017-05-13/InvokeEndpoint>`_

        **Request Syntax**
        ::

          response = client.invoke_endpoint(
              EndpointName='string',
              Body=b'bytes'|file,
              ContentType='string',
              Accept='string',
              CustomAttributes='string',
              TargetModel='string'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name of the endpoint that you specified when you created the endpoint using the
          `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ API.

        :type Body: bytes or seekable file-like object
        :param Body: **[REQUIRED]**

          Provides input data, in the format specified in the ``ContentType`` request header. Amazon
          SageMaker passes all of the data in the body to the model.

          For information about the format of the request body, see `Common Data Formats—Inference
          <https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .

        :type ContentType: string
        :param ContentType:

          The MIME type of the input data in the request body.

        :type Accept: string
        :param Accept:

          The desired MIME type of the inference in the response.

        :type CustomAttributes: string
        :param CustomAttributes:

          Provides additional information about a request for an inference submitted to a model hosted at
          an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You
          could use this value, for example, to provide an ID that you can use to track a request or to
          provide other metadata that a service endpoint was programmed to process. The value must consist
          of no more than 1024 visible US-ASCII characters as specified in `Section 3.3.6. Field Value
          Components <https://tools.ietf.org/html/rfc7230#section-3.2.6>`__ of the Hypertext Transfer
          Protocol (HTTP/1.1). This feature is currently supported in the AWS SDKs but not in the Amazon
          SageMaker Python SDK.

        :type TargetModel: string
        :param TargetModel:

          Specifies the model to be requested for an inference when invoking a multi-model endpoint.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Body': StreamingBody(),
                'ContentType': 'string',
                'InvokedProductionVariant': 'string',
                'CustomAttributes': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Body** (:class:`.StreamingBody`) --

              Includes the inference provided by the model.

              For information about the format of the response body, see `Common Data Formats—Inference
              <https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .

            - **ContentType** *(string) --*

              The MIME type of the inference returned in the response body.

            - **InvokedProductionVariant** *(string) --*

              Identifies the production variant that was invoked.

            - **CustomAttributes** *(string) --*

              Provides additional information in the response about the inference returned by a model
              hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded
              verbatim. You could use this value, for example, to return an ID received in the
              ``CustomAttributes`` header of a request or other metadata that a service endpoint was
              programmed to produce. The value must consist of no more than 1024 visible US-ASCII
              characters as specified in `Section 3.3.6. Field Value Components
              <https://tools.ietf.org/html/rfc7230#section-3.2.6>`__ of the Hypertext Transfer Protocol
              (HTTP/1.1). If the customer wants the custom attribute returned, the model must set the
              custom attribute to be included on the way back.

              This feature is currently supported in the AWS SDKs but not in the Amazon SageMaker Python
              SDK.

        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailure: Boto3ClientError
    ModelError: Boto3ClientError
    ServiceUnavailable: Boto3ClientError
    ValidationError: Boto3ClientError
