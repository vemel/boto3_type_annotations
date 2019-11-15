"Main interface for sagemaker-runtime type defs"
from __future__ import annotations

from typing_extensions import TypedDict


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
      <http://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .

    - **ContentType** *(string) --*

      The MIME type of the inference returned in the response body.

    - **InvokedProductionVariant** *(string) --*

      Identifies the production variant that was invoked.

    - **CustomAttributes** *(string) --*
    """
