"Main interface for sns Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sns.type_defs import (
    ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef,
    ListEndpointsByPlatformApplicationPaginateResponseTypeDef,
    ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef,
    ListPhoneNumbersOptedOutPaginateResponseTypeDef,
    ListPlatformApplicationsPaginatePaginationConfigTypeDef,
    ListPlatformApplicationsPaginateResponseTypeDef,
    ListSubscriptionsByTopicPaginatePaginationConfigTypeDef,
    ListSubscriptionsByTopicPaginateResponseTypeDef,
    ListSubscriptionsPaginatePaginationConfigTypeDef,
    ListSubscriptionsPaginateResponseTypeDef,
    ListTopicsPaginatePaginationConfigTypeDef,
    ListTopicsPaginateResponseTypeDef,
)


__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListTopicsPaginator",
)


class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    """
    Paginator for `list_endpoints_by_platform_application`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PlatformApplicationArn: str,
        PaginationConfig: ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef = None,
    ) -> ListEndpointsByPlatformApplicationPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SNS.Client.list_endpoints_by_platform_application`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListEndpointsByPlatformApplication>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PlatformApplicationArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoints': [
                    {
                        'EndpointArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response for ListEndpointsByPlatformApplication action.

            - **Endpoints** *(list) --*

              Endpoints returned for ListEndpointsByPlatformApplication action.

              - *(dict) --*

                Endpoint for mobile app and device.

                - **EndpointArn** *(string) --*

                  EndpointArn for mobile app and device.

                - **Attributes** *(dict) --*

                  Attributes for endpoint.

                  - *(string) --*

                    - *(string) --*

        """


class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    """
    Paginator for `list_phone_numbers_opted_out`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef = None,
    ) -> ListPhoneNumbersOptedOutPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SNS.Client.list_phone_numbers_opted_out`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPhoneNumbersOptedOut>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'phoneNumbers': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response from the ``ListPhoneNumbersOptedOut`` action.

            - **phoneNumbers** *(list) --*

              A list of phone numbers that are opted out of receiving SMS messages. The list is paginated,
              and each page can contain up to 100 phone numbers.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListPlatformApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_platform_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListPlatformApplicationsPaginatePaginationConfigTypeDef = None,
    ) -> ListPlatformApplicationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SNS.Client.list_platform_applications`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PlatformApplications': [
                    {
                        'PlatformApplicationArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response for ListPlatformApplications action.

            - **PlatformApplications** *(list) --*

              Platform applications returned when calling ListPlatformApplications action.

              - *(dict) --*

                Platform application object.

                - **PlatformApplicationArn** *(string) --*

                  PlatformApplicationArn for platform application object.

                - **Attributes** *(dict) --*

                  Attributes for platform application object.

                  - *(string) --*

                    - *(string) --*

        """


class ListSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSubscriptionsPaginatePaginationConfigTypeDef = None
    ) -> ListSubscriptionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SNS.Client.list_subscriptions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response for ListSubscriptions action

            - **Subscriptions** *(list) --*

              A list of subscriptions.

              - *(dict) --*

                A wrapper type for the attributes of an Amazon SNS subscription.

                - **SubscriptionArn** *(string) --*

                  The subscription's ARN.

                - **Owner** *(string) --*

                  The subscription's owner.

                - **Protocol** *(string) --*

                  The subscription's protocol.

                - **Endpoint** *(string) --*

                  The subscription's endpoint (format depends on the protocol).

                - **TopicArn** *(string) --*

                  The ARN of the subscription's topic.

        """


class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    """
    Paginator for `list_subscriptions_by_topic`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TopicArn: str,
        PaginationConfig: ListSubscriptionsByTopicPaginatePaginationConfigTypeDef = None,
    ) -> ListSubscriptionsByTopicPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`SNS.Client.list_subscriptions_by_topic`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptionsByTopic>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              TopicArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic for which you wish to find subscriptions.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response for ListSubscriptionsByTopic action.

            - **Subscriptions** *(list) --*

              A list of subscriptions.

              - *(dict) --*

                A wrapper type for the attributes of an Amazon SNS subscription.

                - **SubscriptionArn** *(string) --*

                  The subscription's ARN.

                - **Owner** *(string) --*

                  The subscription's owner.

                - **Protocol** *(string) --*

                  The subscription's protocol.

                - **Endpoint** *(string) --*

                  The subscription's endpoint (format depends on the protocol).

                - **TopicArn** *(string) --*

                  The ARN of the subscription's topic.

        """


class ListTopicsPaginator(Boto3Paginator):
    """
    Paginator for `list_topics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTopicsPaginatePaginationConfigTypeDef = None
    ) -> ListTopicsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_topics`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Topics': [
                    {
                        'TopicArn': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response for ListTopics action.

            - **Topics** *(list) --*

              A list of topic ARNs.

              - *(dict) --*

                A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
                attributes, use ``GetTopicAttributes`` .

                - **TopicArn** *(string) --*

                  The topic's ARN.

        """
