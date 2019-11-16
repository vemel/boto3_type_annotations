"Main interface for apigatewaymanagementapi type defs"
from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


__all__ = (
    "ClientGetConnectionResponseIdentityTypeDef",
    "ClientGetConnectionResponseTypeDef",
)


_ClientGetConnectionResponseIdentityTypeDef = TypedDict(
    "_ClientGetConnectionResponseIdentityTypeDef",
    {"SourceIp": str, "UserAgent": str},
    total=False,
)


class ClientGetConnectionResponseIdentityTypeDef(
    _ClientGetConnectionResponseIdentityTypeDef
):
    """
    Type definition for `ClientGetConnectionResponse` `Identity`

    - **SourceIp** *(string) --*

      The source IP address of the TCP connection making the request to API Gateway.

    - **UserAgent** *(string) --*

      The User Agent of the API caller.
    """


_ClientGetConnectionResponseTypeDef = TypedDict(
    "_ClientGetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": ClientGetConnectionResponseIdentityTypeDef,
        "LastActiveAt": datetime,
    },
    total=False,
)


class ClientGetConnectionResponseTypeDef(_ClientGetConnectionResponseTypeDef):
    """
    Type definition for `ClientGetConnection` `Response`

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
