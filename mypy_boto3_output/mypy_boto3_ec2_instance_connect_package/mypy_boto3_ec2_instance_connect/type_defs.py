"Main interface for ec2-instance-connect type defs"
from __future__ import annotations

from typing_extensions import TypedDict


__all__ = ("ClientSendSshPublicKeyResponseTypeDef",)


_ClientSendSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientSendSshPublicKeyResponseTypeDef",
    {"RequestId": str, "Success": bool},
    total=False,
)


class ClientSendSshPublicKeyResponseTypeDef(_ClientSendSshPublicKeyResponseTypeDef):
    """
    Type definition for `ClientSendSshPublicKey` `Response`

    - **RequestId** *(string) --*

      The request ID as logged by EC2 Connect. Please provide this when contacting AWS Support.

    - **Success** *(boolean) --*

      Indicates request success.
    """
