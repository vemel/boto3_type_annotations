"Main interface for personalize-events type defs"
from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


__all__ = ("ClientPutEventseventListTypeDef",)


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

    Represents user interaction event information sent using the ``PutEvents`` API.

    - **eventId** *(string) --*

      An ID associated with the event. If an event ID is not provided, Amazon Personalize generates
      a unique ID for the event. An event ID is not used as an input to the model. Amazon
      Personalize uses the event ID to distinquish unique events. Any subsequent events after the
      first with the same event ID are not used in model training.

    - **eventType** *(string) --* **[REQUIRED]**

      The type of event. This property corresponds to the ``EVENT_TYPE`` field of the Interactions
      schema.

    - **properties** *(string) --* **[REQUIRED]**

      A string map of event-specific data that you might choose to record. For example, if a user
      rates a movie on your site, you might send the movie ID and rating, and the number of movie
      ratings made by the user.

      Each item in the map consists of a key-value pair. For example,

       ``{"itemId": "movie1"}``

       ``{"itemId": "movie2", "eventValue": "4.5"}``

       ``{"itemId": "movie3", "eventValue": "3", "numberOfRatings": "12"}``

      The keys use camel case names that match the fields in the Interactions schema. The
      ``itemId`` and ``eventValue`` keys correspond to the ``ITEM_ID`` and ``EVENT_VALUE`` fields.
      In the above example, the ``eventType`` might be 'MovieRating' with ``eventValue`` being the
      rating. The ``numberOfRatings`` would match the 'NUMBER_OF_RATINGS' field defined in the
      Interactions schema.

    - **sentAt** *(datetime) --* **[REQUIRED]**

      The timestamp on the client side when the event occurred.
    """
