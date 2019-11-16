"Main interface for personalize-runtime type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef",
    "ClientGetPersonalizedRankingResponseTypeDef",
    "ClientGetRecommendationsResponseitemListTypeDef",
    "ClientGetRecommendationsResponseTypeDef",
)


_ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef = TypedDict(
    "_ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef",
    {"itemId": str},
    total=False,
)


class ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef(
    _ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef
):
    """
    Type definition for `ClientGetPersonalizedRankingResponse` `personalizedRanking`

    An object that identifies an item.

    The and APIs return a list of ``PredictedItem`` s.

    - **itemId** *(string) --*

      The recommended item ID.
    """


_ClientGetPersonalizedRankingResponseTypeDef = TypedDict(
    "_ClientGetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List[
            ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef
        ]
    },
    total=False,
)


class ClientGetPersonalizedRankingResponseTypeDef(
    _ClientGetPersonalizedRankingResponseTypeDef
):
    """
    Type definition for `ClientGetPersonalizedRanking` `Response`

    - **personalizedRanking** *(list) --*

      A list of items in order of most likely interest to the user.

      - *(dict) --*

        An object that identifies an item.

        The and APIs return a list of ``PredictedItem`` s.

        - **itemId** *(string) --*

          The recommended item ID.
    """


_ClientGetRecommendationsResponseitemListTypeDef = TypedDict(
    "_ClientGetRecommendationsResponseitemListTypeDef", {"itemId": str}, total=False
)


class ClientGetRecommendationsResponseitemListTypeDef(
    _ClientGetRecommendationsResponseitemListTypeDef
):
    """
    Type definition for `ClientGetRecommendationsResponse` `itemList`

    An object that identifies an item.

    The and APIs return a list of ``PredictedItem`` s.

    - **itemId** *(string) --*

      The recommended item ID.
    """


_ClientGetRecommendationsResponseTypeDef = TypedDict(
    "_ClientGetRecommendationsResponseTypeDef",
    {"itemList": List[ClientGetRecommendationsResponseitemListTypeDef]},
    total=False,
)


class ClientGetRecommendationsResponseTypeDef(_ClientGetRecommendationsResponseTypeDef):
    """
    Type definition for `ClientGetRecommendations` `Response`

    - **itemList** *(list) --*

      A list of recommendations.

      - *(dict) --*

        An object that identifies an item.

        The and APIs return a list of ``PredictedItem`` s.

        - **itemId** *(string) --*

          The recommended item ID.
    """
