"Main interface for cloudsearchdomain type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientSearchResponsefacetsbucketsTypeDef",
    "ClientSearchResponsefacetsTypeDef",
    "ClientSearchResponsehitshitTypeDef",
    "ClientSearchResponsehitsTypeDef",
    "ClientSearchResponsestatsTypeDef",
    "ClientSearchResponsestatusTypeDef",
    "ClientSearchResponseTypeDef",
    "ClientSuggestResponsestatusTypeDef",
    "ClientSuggestResponsesuggestsuggestionsTypeDef",
    "ClientSuggestResponsesuggestTypeDef",
    "ClientSuggestResponseTypeDef",
    "ClientUploadDocumentsResponsewarningsTypeDef",
    "ClientUploadDocumentsResponseTypeDef",
)


_ClientSearchResponsefacetsbucketsTypeDef = TypedDict(
    "_ClientSearchResponsefacetsbucketsTypeDef",
    {"value": str, "count": int},
    total=False,
)


class ClientSearchResponsefacetsbucketsTypeDef(
    _ClientSearchResponsefacetsbucketsTypeDef
):
    """
    Type definition for `ClientSearchResponsefacets` `buckets`

    A container for facet information.

    - **value** *(string) --*

      The facet value being counted.

    - **count** *(integer) --*

      The number of hits that contain the facet value in the specified facet field.
    """


_ClientSearchResponsefacetsTypeDef = TypedDict(
    "_ClientSearchResponsefacetsTypeDef",
    {"buckets": List[ClientSearchResponsefacetsbucketsTypeDef]},
    total=False,
)


class ClientSearchResponsefacetsTypeDef(_ClientSearchResponsefacetsTypeDef):
    """
    Type definition for `ClientSearchResponse` `facets`

    A container for the calculated facet values and counts.

    - **buckets** *(list) --*

      A list of the calculated facet values and counts.

      - *(dict) --*

        A container for facet information.

        - **value** *(string) --*

          The facet value being counted.

        - **count** *(integer) --*

          The number of hits that contain the facet value in the specified facet field.
    """


_ClientSearchResponsehitshitTypeDef = TypedDict(
    "_ClientSearchResponsehitshitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)


class ClientSearchResponsehitshitTypeDef(_ClientSearchResponsehitshitTypeDef):
    """
    Type definition for `ClientSearchResponsehits` `hit`

    Information about a document that matches the search request.

    - **id** *(string) --*

      The document ID of a document that matches the search request.

    - **fields** *(dict) --*

      The fields returned from a document that matches the search request.

      - *(string) --*

        - *(list) --*

          - *(string) --*

    - **exprs** *(dict) --*

      The expressions returned from a document that matches the search request.

      - *(string) --*

        - *(string) --*

    - **highlights** *(dict) --*

      The highlights returned from a document that matches the search request.

      - *(string) --*

        - *(string) --*
    """


_ClientSearchResponsehitsTypeDef = TypedDict(
    "_ClientSearchResponsehitsTypeDef",
    {
        "found": int,
        "start": int,
        "cursor": str,
        "hit": List[ClientSearchResponsehitshitTypeDef],
    },
    total=False,
)


class ClientSearchResponsehitsTypeDef(_ClientSearchResponsehitsTypeDef):
    """
    Type definition for `ClientSearchResponse` `hits`

    The documents that match the search criteria.

    - **found** *(integer) --*

      The total number of documents that match the search request.

    - **start** *(integer) --*

      The index of the first matching document.

    - **cursor** *(string) --*

      A cursor that can be used to retrieve the next set of matching documents when you want to
      page through a large result set.

    - **hit** *(list) --*

      A document that matches the search request.

      - *(dict) --*

        Information about a document that matches the search request.

        - **id** *(string) --*

          The document ID of a document that matches the search request.

        - **fields** *(dict) --*

          The fields returned from a document that matches the search request.

          - *(string) --*

            - *(list) --*

              - *(string) --*

        - **exprs** *(dict) --*

          The expressions returned from a document that matches the search request.

          - *(string) --*

            - *(string) --*

        - **highlights** *(dict) --*

          The highlights returned from a document that matches the search request.

          - *(string) --*

            - *(string) --*
    """


_ClientSearchResponsestatsTypeDef = TypedDict(
    "_ClientSearchResponsestatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)


class ClientSearchResponsestatsTypeDef(_ClientSearchResponsestatsTypeDef):
    """
    Type definition for `ClientSearchResponse` `stats`

    The statistics for a field calculated in the request.

    - **min** *(string) --*

      The minimum value found in the specified field in the result set.

      If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
      ``min`` is the string representation of a double-precision 64-bit floating point value.
      If the field is ``date`` or ``date-array`` , ``min`` is the string representation of a
      date with the format specified in `IETF RFC3339 <http://tools.ietf.org/html/rfc3339>`__
      : yyyy-mm-ddTHH:mm:ss.SSSZ.

    - **max** *(string) --*

      The maximum value found in the specified field in the result set.

      If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
      ``max`` is the string representation of a double-precision 64-bit floating point value.
      If the field is ``date`` or ``date-array`` , ``max`` is the string representation of a
      date with the format specified in `IETF RFC3339 <http://tools.ietf.org/html/rfc3339>`__
      : yyyy-mm-ddTHH:mm:ss.SSSZ.

    - **count** *(integer) --*

      The number of documents that contain a value in the specified field in the result set.

    - **missing** *(integer) --*

      The number of documents that do not contain a value in the specified field in the
      result set.

    - **sum** *(float) --*

      The sum of the field values across the documents in the result set. ``null`` for date
      fields.

    - **sumOfSquares** *(float) --*

      The sum of all field values in the result set squared.

    - **mean** *(string) --*

      The average of the values found in the specified field in the result set.

      If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
      ``mean`` is the string representation of a double-precision 64-bit floating point
      value. If the field is ``date`` or ``date-array`` , ``mean`` is the string
      representation of a date with the format specified in `IETF RFC3339
      <http://tools.ietf.org/html/rfc3339>`__ : yyyy-mm-ddTHH:mm:ss.SSSZ.

    - **stddev** *(float) --*

      The standard deviation of the values in the specified field in the result set.
    """


_ClientSearchResponsestatusTypeDef = TypedDict(
    "_ClientSearchResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)


class ClientSearchResponsestatusTypeDef(_ClientSearchResponsestatusTypeDef):
    """
    Type definition for `ClientSearchResponse` `status`

    The status information returned for the search request.

    - **timems** *(integer) --*

      How long it took to process the request, in milliseconds.

    - **rid** *(string) --*

      The encrypted resource ID for the request.
    """


_ClientSearchResponseTypeDef = TypedDict(
    "_ClientSearchResponseTypeDef",
    {
        "status": ClientSearchResponsestatusTypeDef,
        "hits": ClientSearchResponsehitsTypeDef,
        "facets": Dict[str, ClientSearchResponsefacetsTypeDef],
        "stats": Dict[str, ClientSearchResponsestatsTypeDef],
    },
    total=False,
)


class ClientSearchResponseTypeDef(_ClientSearchResponseTypeDef):
    """
    Type definition for `ClientSearch` `Response`

    The result of a ``Search`` request. Contains the documents that match the specified search
    criteria and any requested fields, highlights, and facet information.

    - **status** *(dict) --*

      The status information returned for the search request.

      - **timems** *(integer) --*

        How long it took to process the request, in milliseconds.

      - **rid** *(string) --*

        The encrypted resource ID for the request.

    - **hits** *(dict) --*

      The documents that match the search criteria.

      - **found** *(integer) --*

        The total number of documents that match the search request.

      - **start** *(integer) --*

        The index of the first matching document.

      - **cursor** *(string) --*

        A cursor that can be used to retrieve the next set of matching documents when you want to
        page through a large result set.

      - **hit** *(list) --*

        A document that matches the search request.

        - *(dict) --*

          Information about a document that matches the search request.

          - **id** *(string) --*

            The document ID of a document that matches the search request.

          - **fields** *(dict) --*

            The fields returned from a document that matches the search request.

            - *(string) --*

              - *(list) --*

                - *(string) --*

          - **exprs** *(dict) --*

            The expressions returned from a document that matches the search request.

            - *(string) --*

              - *(string) --*

          - **highlights** *(dict) --*

            The highlights returned from a document that matches the search request.

            - *(string) --*

              - *(string) --*

    - **facets** *(dict) --*

      The requested facet information.

      - *(string) --*

        - *(dict) --*

          A container for the calculated facet values and counts.

          - **buckets** *(list) --*

            A list of the calculated facet values and counts.

            - *(dict) --*

              A container for facet information.

              - **value** *(string) --*

                The facet value being counted.

              - **count** *(integer) --*

                The number of hits that contain the facet value in the specified facet field.

    - **stats** *(dict) --*

      The requested field statistics information.

      - *(string) --*

        - *(dict) --*

          The statistics for a field calculated in the request.

          - **min** *(string) --*

            The minimum value found in the specified field in the result set.

            If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
            ``min`` is the string representation of a double-precision 64-bit floating point value.
            If the field is ``date`` or ``date-array`` , ``min`` is the string representation of a
            date with the format specified in `IETF RFC3339 <http://tools.ietf.org/html/rfc3339>`__
            : yyyy-mm-ddTHH:mm:ss.SSSZ.

          - **max** *(string) --*

            The maximum value found in the specified field in the result set.

            If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
            ``max`` is the string representation of a double-precision 64-bit floating point value.
            If the field is ``date`` or ``date-array`` , ``max`` is the string representation of a
            date with the format specified in `IETF RFC3339 <http://tools.ietf.org/html/rfc3339>`__
            : yyyy-mm-ddTHH:mm:ss.SSSZ.

          - **count** *(integer) --*

            The number of documents that contain a value in the specified field in the result set.

          - **missing** *(integer) --*

            The number of documents that do not contain a value in the specified field in the
            result set.

          - **sum** *(float) --*

            The sum of the field values across the documents in the result set. ``null`` for date
            fields.

          - **sumOfSquares** *(float) --*

            The sum of all field values in the result set squared.

          - **mean** *(string) --*

            The average of the values found in the specified field in the result set.

            If the field is numeric (``int`` , ``int-array`` , ``double`` , or ``double-array`` ),
            ``mean`` is the string representation of a double-precision 64-bit floating point
            value. If the field is ``date`` or ``date-array`` , ``mean`` is the string
            representation of a date with the format specified in `IETF RFC3339
            <http://tools.ietf.org/html/rfc3339>`__ : yyyy-mm-ddTHH:mm:ss.SSSZ.

          - **stddev** *(float) --*

            The standard deviation of the values in the specified field in the result set.
    """


_ClientSuggestResponsestatusTypeDef = TypedDict(
    "_ClientSuggestResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)


class ClientSuggestResponsestatusTypeDef(_ClientSuggestResponsestatusTypeDef):
    """
    Type definition for `ClientSuggestResponse` `status`

    The status of a ``SuggestRequest`` . Contains the resource ID (``rid`` ) and how long it took
    to process the request (``timems`` ).

    - **timems** *(integer) --*

      How long it took to process the request, in milliseconds.

    - **rid** *(string) --*

      The encrypted resource ID for the request.
    """


_ClientSuggestResponsesuggestsuggestionsTypeDef = TypedDict(
    "_ClientSuggestResponsesuggestsuggestionsTypeDef",
    {"suggestion": str, "score": int, "id": str},
    total=False,
)


class ClientSuggestResponsesuggestsuggestionsTypeDef(
    _ClientSuggestResponsesuggestsuggestionsTypeDef
):
    """
    Type definition for `ClientSuggestResponsesuggest` `suggestions`

    An autocomplete suggestion that matches the query string specified in a
    ``SuggestRequest`` .

    - **suggestion** *(string) --*

      The string that matches the query string specified in the ``SuggestRequest`` .

    - **score** *(integer) --*

      The relevance score of a suggested match.

    - **id** *(string) --*

      The document ID of the suggested document.
    """


_ClientSuggestResponsesuggestTypeDef = TypedDict(
    "_ClientSuggestResponsesuggestTypeDef",
    {
        "query": str,
        "found": int,
        "suggestions": List[ClientSuggestResponsesuggestsuggestionsTypeDef],
    },
    total=False,
)


class ClientSuggestResponsesuggestTypeDef(_ClientSuggestResponsesuggestTypeDef):
    """
    Type definition for `ClientSuggestResponse` `suggest`

    Container for the matching search suggestion information.

    - **query** *(string) --*

      The query string specified in the suggest request.

    - **found** *(integer) --*

      The number of documents that were found to match the query string.

    - **suggestions** *(list) --*

      The documents that match the query string.

      - *(dict) --*

        An autocomplete suggestion that matches the query string specified in a
        ``SuggestRequest`` .

        - **suggestion** *(string) --*

          The string that matches the query string specified in the ``SuggestRequest`` .

        - **score** *(integer) --*

          The relevance score of a suggested match.

        - **id** *(string) --*

          The document ID of the suggested document.
    """


_ClientSuggestResponseTypeDef = TypedDict(
    "_ClientSuggestResponseTypeDef",
    {
        "status": ClientSuggestResponsestatusTypeDef,
        "suggest": ClientSuggestResponsesuggestTypeDef,
    },
    total=False,
)


class ClientSuggestResponseTypeDef(_ClientSuggestResponseTypeDef):
    """
    Type definition for `ClientSuggest` `Response`

    Contains the response to a ``Suggest`` request.

    - **status** *(dict) --*

      The status of a ``SuggestRequest`` . Contains the resource ID (``rid`` ) and how long it took
      to process the request (``timems`` ).

      - **timems** *(integer) --*

        How long it took to process the request, in milliseconds.

      - **rid** *(string) --*

        The encrypted resource ID for the request.

    - **suggest** *(dict) --*

      Container for the matching search suggestion information.

      - **query** *(string) --*

        The query string specified in the suggest request.

      - **found** *(integer) --*

        The number of documents that were found to match the query string.

      - **suggestions** *(list) --*

        The documents that match the query string.

        - *(dict) --*

          An autocomplete suggestion that matches the query string specified in a
          ``SuggestRequest`` .

          - **suggestion** *(string) --*

            The string that matches the query string specified in the ``SuggestRequest`` .

          - **score** *(integer) --*

            The relevance score of a suggested match.

          - **id** *(string) --*

            The document ID of the suggested document.
    """


_ClientUploadDocumentsResponsewarningsTypeDef = TypedDict(
    "_ClientUploadDocumentsResponsewarningsTypeDef", {"message": str}, total=False
)


class ClientUploadDocumentsResponsewarningsTypeDef(
    _ClientUploadDocumentsResponsewarningsTypeDef
):
    """
    Type definition for `ClientUploadDocumentsResponse` `warnings`

    A warning returned by the document service when an issue is discovered while processing an
    upload request.

    - **message** *(string) --*

      The description for a warning returned by the document service.
    """


_ClientUploadDocumentsResponseTypeDef = TypedDict(
    "_ClientUploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List[ClientUploadDocumentsResponsewarningsTypeDef],
    },
    total=False,
)


class ClientUploadDocumentsResponseTypeDef(_ClientUploadDocumentsResponseTypeDef):
    """
    Type definition for `ClientUploadDocuments` `Response`

    Contains the response to an ``UploadDocuments`` request.

    - **status** *(string) --*

      The status of an ``UploadDocumentsRequest`` .

    - **adds** *(integer) --*

      The number of documents that were added to the search domain.

    - **deletes** *(integer) --*

      The number of documents that were deleted from the search domain.

    - **warnings** *(list) --*

      Any warnings returned by the document service about the documents being uploaded.

      - *(dict) --*

        A warning returned by the document service when an issue is discovered while processing an
        upload request.

        - **message** *(string) --*

          The description for a warning returned by the document service.
    """
