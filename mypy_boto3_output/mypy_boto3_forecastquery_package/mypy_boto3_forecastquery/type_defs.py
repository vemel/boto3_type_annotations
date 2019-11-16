"Main interface for forecastquery type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientQueryForecastResponseForecastPredictionsTypeDef",
    "ClientQueryForecastResponseForecastTypeDef",
    "ClientQueryForecastResponseTypeDef",
)


_ClientQueryForecastResponseForecastPredictionsTypeDef = TypedDict(
    "_ClientQueryForecastResponseForecastPredictionsTypeDef",
    {"Timestamp": str, "Value": float},
    total=False,
)


class ClientQueryForecastResponseForecastPredictionsTypeDef(
    _ClientQueryForecastResponseForecastPredictionsTypeDef
):
    """
    Type definition for `ClientQueryForecastResponseForecast` `Predictions`

    The forecast value for a specific date. Part of the  Forecast object.

    - **Timestamp** *(string) --*

      The timestamp of the specific forecast.

    - **Value** *(float) --*

      The forecast value.
    """


_ClientQueryForecastResponseForecastTypeDef = TypedDict(
    "_ClientQueryForecastResponseForecastTypeDef",
    {
        "Predictions": Dict[
            str, List[ClientQueryForecastResponseForecastPredictionsTypeDef]
        ]
    },
    total=False,
)


class ClientQueryForecastResponseForecastTypeDef(
    _ClientQueryForecastResponseForecastTypeDef
):
    """
    Type definition for `ClientQueryForecastResponse` `Forecast`

    The forecast.

    - **Predictions** *(dict) --*

      The forecast.

      The *string* of the string to array map is one of the following values:

      * mean

      * p10

      * p50

      * p90

      - *(string) --*

        - *(list) --*

          - *(dict) --*

            The forecast value for a specific date. Part of the  Forecast object.

            - **Timestamp** *(string) --*

              The timestamp of the specific forecast.

            - **Value** *(float) --*

              The forecast value.
    """


_ClientQueryForecastResponseTypeDef = TypedDict(
    "_ClientQueryForecastResponseTypeDef",
    {"Forecast": ClientQueryForecastResponseForecastTypeDef},
    total=False,
)


class ClientQueryForecastResponseTypeDef(_ClientQueryForecastResponseTypeDef):
    """
    Type definition for `ClientQueryForecast` `Response`

    - **Forecast** *(dict) --*

      The forecast.

      - **Predictions** *(dict) --*

        The forecast.

        The *string* of the string to array map is one of the following values:

        * mean

        * p10

        * p50

        * p90

        - *(string) --*

          - *(list) --*

            - *(dict) --*

              The forecast value for a specific date. Part of the  Forecast object.

              - **Timestamp** *(string) --*

                The timestamp of the specific forecast.

              - **Value** *(float) --*

                The forecast value.
    """
