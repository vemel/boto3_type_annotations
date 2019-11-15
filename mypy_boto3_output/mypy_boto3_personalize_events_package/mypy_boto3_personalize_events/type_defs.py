"Main interface for personalize-events type defs"
from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


_RequiredClientPutEventseventListTypeDef = TypedDict(
    "_RequiredClientPutEventseventListTypeDef",
    {"eventType": str, "properties": str, "sentAt": datetime},
)
_OptionalClientPutEventseventListTypeDef = TypedDict(
    "_OptionalClientPutEventseventListTypeDef", {"eventId": str}, total=False
)


class ClientPutEventseventListTypeDef(
    _RequiredClientPutEventseventListTypeDef, _OptionalClientPutEventseventListTypeDef
):
    """
    Type definition for `ClientPutEvents` `eventList`

    - **eventId** *(string) --*
    - **eventType** *(string) --* **[REQUIRED]**
    - **properties** *(string) --* **[REQUIRED]**
    - **sentAt** *(datetime) --* **[REQUIRED]**
    """
