"Main interface for sagemaker-runtime type defs"
from __future__ import annotations

from typing_extensions import TypedDict


__all__ = ("ClientInvokeEndpointResponseTypeDef",)


_ClientInvokeEndpointResponseTypeDef = TypedDict(
    "_ClientInvokeEndpointResponseTypeDef",
    {"ContentType": str, "InvokedProductionVariant": str, "CustomAttributes": str},
    total=False,
)


class ClientInvokeEndpointResponseTypeDef(_ClientInvokeEndpointResponseTypeDef):
    """
    Type definition for `ClientInvokeEndpoint` `Response`

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
