"Main interface for personalize-events Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):
    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
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

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str) -> Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str) -> Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """

    # pylint: disable=arguments-differ
    def put_events(
        self, trackingId: str, sessionId: str, eventList: List[Any], userId: str = None
    ) -> None:
        """
        Records user interaction event data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/personalize-events-2018-03-22/PutEvents>`_

        **Request Syntax**
        ::

          response = client.put_events(
              trackingId='string',
              userId='string',
              sessionId='string',
              eventList=[
                  {
                      'eventId': 'string',
                      'eventType': 'string',
                      'properties': 'string',
                      'sentAt': datetime(2015, 1, 1)
                  },
              ]
          )
        :type trackingId: string
        :param trackingId: **[REQUIRED]**

          The tracking ID for the event. The ID is generated by a call to the `CreateEventTracker
          <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html>`__ API.

        :type userId: string
        :param userId:

          The user associated with the event.

        :type sessionId: string
        :param sessionId: **[REQUIRED]**

          The session ID associated with the user's visit.

        :type eventList: list
        :param eventList: **[REQUIRED]**

          A list of event data from the session.

          - *(dict) --*

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

        :returns: None
        """
