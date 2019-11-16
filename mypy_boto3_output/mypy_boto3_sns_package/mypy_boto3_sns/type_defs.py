"Main interface for sns type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ClientConfirmSubscriptionResponseTypeDef",
    "ClientCreatePlatformApplicationResponseTypeDef",
    "ClientCreatePlatformEndpointResponseTypeDef",
    "ClientCreateTopicResponseTypeDef",
    "ClientCreateTopicTagsTypeDef",
    "ClientGetEndpointAttributesResponseTypeDef",
    "ClientGetPlatformApplicationAttributesResponseTypeDef",
    "ClientGetSmsAttributesResponseTypeDef",
    "ClientGetSubscriptionAttributesResponseTypeDef",
    "ClientGetTopicAttributesResponseTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    "ClientListEndpointsByPlatformApplicationResponseTypeDef",
    "ClientListPhoneNumbersOptedOutResponseTypeDef",
    "ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    "ClientListPlatformApplicationsResponseTypeDef",
    "ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsByTopicResponseTypeDef",
    "ClientListSubscriptionsResponseSubscriptionsTypeDef",
    "ClientListSubscriptionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTopicsResponseTopicsTypeDef",
    "ClientListTopicsResponseTypeDef",
    "ClientPublishMessageAttributesTypeDef",
    "ClientPublishResponseTypeDef",
    "ClientSubscribeResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef",
    "ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef",
    "ListEndpointsByPlatformApplicationPaginateResponseTypeDef",
    "ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef",
    "ListPhoneNumbersOptedOutPaginateResponseTypeDef",
    "ListPlatformApplicationsPaginatePaginationConfigTypeDef",
    "ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef",
    "ListPlatformApplicationsPaginateResponseTypeDef",
    "ListSubscriptionsByTopicPaginatePaginationConfigTypeDef",
    "ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef",
    "ListSubscriptionsByTopicPaginateResponseTypeDef",
    "ListSubscriptionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionsPaginateResponseSubscriptionsTypeDef",
    "ListSubscriptionsPaginateResponseTypeDef",
    "ListTopicsPaginatePaginationConfigTypeDef",
    "ListTopicsPaginateResponseTopicsTypeDef",
    "ListTopicsPaginateResponseTypeDef",
    "PlatformEndpointPublishMessageAttributesTypeDef",
    "PlatformEndpointPublishResponseTypeDef",
    "ServiceResourceCreateTopicTagsTypeDef",
    "TopicPublishMessageAttributesTypeDef",
    "TopicPublishResponseTypeDef",
)


_ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "_ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef",
    {"isOptedOut": bool},
    total=False,
)


class ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef(
    _ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef
):
    """
    Type definition for `ClientCheckIfPhoneNumberIsOptedOut` `Response`

    The response from the ``CheckIfPhoneNumberIsOptedOut`` action.

    - **isOptedOut** *(boolean) --*

      Indicates whether the phone number is opted out:

      * ``true`` – The phone number is opted out, meaning you cannot publish SMS messages to it.

      * ``false`` – The phone number is opted in, meaning you can publish SMS messages to it.
    """


_ClientConfirmSubscriptionResponseTypeDef = TypedDict(
    "_ClientConfirmSubscriptionResponseTypeDef", {"SubscriptionArn": str}, total=False
)


class ClientConfirmSubscriptionResponseTypeDef(
    _ClientConfirmSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientConfirmSubscription` `Response`

    Response for ConfirmSubscriptions action.

    - **SubscriptionArn** *(string) --*

      The ARN of the created subscription.
    """


_ClientCreatePlatformApplicationResponseTypeDef = TypedDict(
    "_ClientCreatePlatformApplicationResponseTypeDef",
    {"PlatformApplicationArn": str},
    total=False,
)


class ClientCreatePlatformApplicationResponseTypeDef(
    _ClientCreatePlatformApplicationResponseTypeDef
):
    """
    Type definition for `ClientCreatePlatformApplication` `Response`

    Response from CreatePlatformApplication action.

    - **PlatformApplicationArn** *(string) --*

      PlatformApplicationArn is returned.
    """


_ClientCreatePlatformEndpointResponseTypeDef = TypedDict(
    "_ClientCreatePlatformEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)


class ClientCreatePlatformEndpointResponseTypeDef(
    _ClientCreatePlatformEndpointResponseTypeDef
):
    """
    Type definition for `ClientCreatePlatformEndpoint` `Response`

    Response from CreateEndpoint action.

    - **EndpointArn** *(string) --*

      EndpointArn returned from CreateEndpoint action.
    """


_ClientCreateTopicResponseTypeDef = TypedDict(
    "_ClientCreateTopicResponseTypeDef", {"TopicArn": str}, total=False
)


class ClientCreateTopicResponseTypeDef(_ClientCreateTopicResponseTypeDef):
    """
    Type definition for `ClientCreateTopic` `Response`

    Response from CreateTopic action.

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) assigned to the created topic.
    """


_ClientCreateTopicTagsTypeDef = TypedDict(
    "_ClientCreateTopicTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateTopicTagsTypeDef(_ClientCreateTopicTagsTypeDef):
    """
    Type definition for `ClientCreateTopic` `Tags`

    The list of tags to be added to the specified topic.

    - **Key** *(string) --* **[REQUIRED]**

      The required key portion of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The optional value portion of the tag.
    """


_ClientGetEndpointAttributesResponseTypeDef = TypedDict(
    "_ClientGetEndpointAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetEndpointAttributesResponseTypeDef(
    _ClientGetEndpointAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetEndpointAttributes` `Response`

    Response from GetEndpointAttributes of the EndpointArn.

    - **Attributes** *(dict) --*

      Attributes include the following:

      * ``CustomUserData`` – arbitrary user data to associate with the endpoint. Amazon SNS does
      not use this data. The data must be in UTF-8 format and less than 2KB.

      * ``Enabled`` – flag that enables/disables delivery to the endpoint. Amazon SNS will set this
      to false when a notification service indicates to Amazon SNS that the endpoint is invalid.
      Users can set it back to true, typically after updating Token.

      * ``Token`` – device token, also referred to as a registration id, for an app and mobile
      device. This is returned from the notification service when an app and mobile device are
      registered with the notification service.

      - *(string) --*

        - *(string) --*
    """


_ClientGetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "_ClientGetPlatformApplicationAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetPlatformApplicationAttributesResponseTypeDef(
    _ClientGetPlatformApplicationAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetPlatformApplicationAttributes` `Response`

    Response for GetPlatformApplicationAttributes action.

    - **Attributes** *(dict) --*

      Attributes include the following:

      * ``EventEndpointCreated`` – Topic ARN to which EndpointCreated event notifications should be
      sent.

      * ``EventEndpointDeleted`` – Topic ARN to which EndpointDeleted event notifications should be
      sent.

      * ``EventEndpointUpdated`` – Topic ARN to which EndpointUpdate event notifications should be
      sent.

      * ``EventDeliveryFailure`` – Topic ARN to which DeliveryFailure event notifications should be
      sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.

      - *(string) --*

        - *(string) --*
    """


_ClientGetSmsAttributesResponseTypeDef = TypedDict(
    "_ClientGetSmsAttributesResponseTypeDef",
    {"attributes": Dict[str, str]},
    total=False,
)


class ClientGetSmsAttributesResponseTypeDef(_ClientGetSmsAttributesResponseTypeDef):
    """
    Type definition for `ClientGetSmsAttributes` `Response`

    The response from the ``GetSMSAttributes`` request.

    - **attributes** *(dict) --*

      The SMS attribute names and their values.

      - *(string) --*

        - *(string) --*
    """


_ClientGetSubscriptionAttributesResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetSubscriptionAttributesResponseTypeDef(
    _ClientGetSubscriptionAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetSubscriptionAttributes` `Response`

    Response for GetSubscriptionAttributes action.

    - **Attributes** *(dict) --*

      A map of the subscription's attributes. Attributes in this map include the following:

      * ``ConfirmationWasAuthenticated`` – ``true`` if the subscription confirmation request was
      authenticated.

      * ``DeliveryPolicy`` – The JSON serialization of the subscription's delivery policy.

      * ``EffectiveDeliveryPolicy`` – The JSON serialization of the effective delivery policy that
      takes into account the topic delivery policy and account system defaults.

      * ``FilterPolicy`` – The filter policy JSON that is assigned to the subscription.

      * ``Owner`` – The AWS account ID of the subscription's owner.

      * ``PendingConfirmation`` – ``true`` if the subscription hasn't been confirmed. To confirm a
      pending subscription, call the ``ConfirmSubscription`` action with a confirmation token.

      * ``RawMessageDelivery`` – ``true`` if raw message delivery is enabled for the subscription.
      Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints.

      * ``SubscriptionArn`` – The subscription's ARN.

      * ``TopicArn`` – The topic ARN that the subscription is associated with.

      - *(string) --*

        - *(string) --*
    """


_ClientGetTopicAttributesResponseTypeDef = TypedDict(
    "_ClientGetTopicAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetTopicAttributesResponseTypeDef(_ClientGetTopicAttributesResponseTypeDef):
    """
    Type definition for `ClientGetTopicAttributes` `Response`

    Response for GetTopicAttributes action.

    - **Attributes** *(dict) --*

      A map of the topic's attributes. Attributes in this map include the following:

      * ``TopicArn`` – the topic's ARN

      * ``Owner`` – the AWS account ID of the topic's owner

      * ``Policy`` – the JSON serialization of the topic's access control policy

      * ``DisplayName`` – the human-readable name used in the "From" field for notifications to
      email and email-json endpoints

      * ``SubscriptionsPending`` – the number of subscriptions pending confirmation on this topic

      * ``SubscriptionsConfirmed`` – the number of confirmed subscriptions on this topic

      * ``SubscriptionsDeleted`` – the number of deleted subscriptions on this topic

      * ``DeliveryPolicy`` – the JSON serialization of the topic's delivery policy

      * ``EffectiveDeliveryPolicy`` – the JSON serialization of the effective delivery policy that
      takes into account system defaults

      - *(string) --*

        - *(string) --*
    """


_ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef = TypedDict(
    "_ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef(
    _ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef
):
    """
    Type definition for `ClientListEndpointsByPlatformApplicationResponse` `Endpoints`

    Endpoint for mobile app and device.

    - **EndpointArn** *(string) --*

      EndpointArn for mobile app and device.

    - **Attributes** *(dict) --*

      Attributes for endpoint.

      - *(string) --*

        - *(string) --*
    """


_ClientListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "_ClientListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List[
            ClientListEndpointsByPlatformApplicationResponseEndpointsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointsByPlatformApplicationResponseTypeDef(
    _ClientListEndpointsByPlatformApplicationResponseTypeDef
):
    """
    Type definition for `ClientListEndpointsByPlatformApplication` `Response`

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

    - **NextToken** *(string) --*

      NextToken string is returned when calling ListEndpointsByPlatformApplication action if
      additional records are available after the first page results.
    """


_ClientListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersOptedOutResponseTypeDef",
    {"phoneNumbers": List[str], "nextToken": str},
    total=False,
)


class ClientListPhoneNumbersOptedOutResponseTypeDef(
    _ClientListPhoneNumbersOptedOutResponseTypeDef
):
    """
    Type definition for `ClientListPhoneNumbersOptedOut` `Response`

    The response from the ``ListPhoneNumbersOptedOut`` action.

    - **phoneNumbers** *(list) --*

      A list of phone numbers that are opted out of receiving SMS messages. The list is paginated,
      and each page can contain up to 100 phone numbers.

      - *(string) --*

    - **nextToken** *(string) --*

      A ``NextToken`` string is returned when you call the ``ListPhoneNumbersOptedOut`` action if
      additional records are available after the first page of results.
    """


_ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef = TypedDict(
    "_ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef(
    _ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
):
    """
    Type definition for `ClientListPlatformApplicationsResponse` `PlatformApplications`

    Platform application object.

    - **PlatformApplicationArn** *(string) --*

      PlatformApplicationArn for platform application object.

    - **Attributes** *(dict) --*

      Attributes for platform application object.

      - *(string) --*

        - *(string) --*
    """


_ClientListPlatformApplicationsResponseTypeDef = TypedDict(
    "_ClientListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List[
            ClientListPlatformApplicationsResponsePlatformApplicationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPlatformApplicationsResponseTypeDef(
    _ClientListPlatformApplicationsResponseTypeDef
):
    """
    Type definition for `ClientListPlatformApplications` `Response`

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

    - **NextToken** *(string) --*

      NextToken string is returned when calling ListPlatformApplications action if additional
      records are available after the first page results.
    """


_ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef = TypedDict(
    "_ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
    },
    total=False,
)


class ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef(
    _ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef
):
    """
    Type definition for `ClientListSubscriptionsByTopicResponse` `Subscriptions`

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


_ClientListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "_ClientListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List[
            ClientListSubscriptionsByTopicResponseSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscriptionsByTopicResponseTypeDef(
    _ClientListSubscriptionsByTopicResponseTypeDef
):
    """
    Type definition for `ClientListSubscriptionsByTopic` `Response`

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

    - **NextToken** *(string) --*

      Token to pass along to the next ``ListSubscriptionsByTopic`` request. This element is
      returned if there are more subscriptions to retrieve.
    """


_ClientListSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "_ClientListSubscriptionsResponseSubscriptionsTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
    },
    total=False,
)


class ClientListSubscriptionsResponseSubscriptionsTypeDef(
    _ClientListSubscriptionsResponseSubscriptionsTypeDef
):
    """
    Type definition for `ClientListSubscriptionsResponse` `Subscriptions`

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


_ClientListSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[ClientListSubscriptionsResponseSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscriptionsResponseTypeDef(_ClientListSubscriptionsResponseTypeDef):
    """
    Type definition for `ClientListSubscriptions` `Response`

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

    - **NextToken** *(string) --*

      Token to pass along to the next ``ListSubscriptions`` request. This element is returned if
      there are more subscriptions to retrieve.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    The list of tags to be added to the specified topic.

    - **Key** *(string) --*

      The required key portion of the tag.

    - **Value** *(string) --*

      The optional value portion of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The tags associated with the specified topic.

      - *(dict) --*

        The list of tags to be added to the specified topic.

        - **Key** *(string) --*

          The required key portion of the tag.

        - **Value** *(string) --*

          The optional value portion of the tag.
    """


_ClientListTopicsResponseTopicsTypeDef = TypedDict(
    "_ClientListTopicsResponseTopicsTypeDef", {"TopicArn": str}, total=False
)


class ClientListTopicsResponseTopicsTypeDef(_ClientListTopicsResponseTopicsTypeDef):
    """
    Type definition for `ClientListTopicsResponse` `Topics`

    A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
    attributes, use ``GetTopicAttributes`` .

    - **TopicArn** *(string) --*

      The topic's ARN.
    """


_ClientListTopicsResponseTypeDef = TypedDict(
    "_ClientListTopicsResponseTypeDef",
    {"Topics": List[ClientListTopicsResponseTopicsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTopicsResponseTypeDef(_ClientListTopicsResponseTypeDef):
    """
    Type definition for `ClientListTopics` `Response`

    Response for ListTopics action.

    - **Topics** *(list) --*

      A list of topic ARNs.

      - *(dict) --*

        A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
        attributes, use ``GetTopicAttributes`` .

        - **TopicArn** *(string) --*

          The topic's ARN.

    - **NextToken** *(string) --*

      Token to pass along to the next ``ListTopics`` request. This element is returned if there are
      additional topics to retrieve.
    """


_RequiredClientPublishMessageAttributesTypeDef = TypedDict(
    "_RequiredClientPublishMessageAttributesTypeDef", {"DataType": str}
)
_OptionalClientPublishMessageAttributesTypeDef = TypedDict(
    "_OptionalClientPublishMessageAttributesTypeDef",
    {"StringValue": str, "BinaryValue": bytes},
    total=False,
)


class ClientPublishMessageAttributesTypeDef(
    _RequiredClientPublishMessageAttributesTypeDef,
    _OptionalClientPublishMessageAttributesTypeDef,
):
    """
    Type definition for `ClientPublish` `MessageAttributes`

    The user-specified message attribute value. For string data types, the value attribute has
    the same restrictions on the content as the message body. For more information, see `Publish
    <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .

    Name, type, and value must not be empty or null. In addition, the message body should not be
    empty or null. All parts of the message attribute, including name, type, and value, are
    included in the message size restriction, which is currently 256 KB (262,144 bytes). For more
    information, see `Using Amazon SNS Message Attributes
    <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SNS supports the following logical data types: String, String.Array, Number, and
      Binary. For more information, see `Message Attribute Data Types
      <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__
      .

    - **StringValue** *(string) --*

      Strings are Unicode with UTF8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, for example, compressed data, encrypted
      data, or images.
    """


_ClientPublishResponseTypeDef = TypedDict(
    "_ClientPublishResponseTypeDef", {"MessageId": str}, total=False
)


class ClientPublishResponseTypeDef(_ClientPublishResponseTypeDef):
    """
    Type definition for `ClientPublish` `Response`

    Response for Publish action.

    - **MessageId** *(string) --*

      Unique identifier assigned to the published message.

      Length Constraint: Maximum 100 characters
    """


_ClientSubscribeResponseTypeDef = TypedDict(
    "_ClientSubscribeResponseTypeDef", {"SubscriptionArn": str}, total=False
)


class ClientSubscribeResponseTypeDef(_ClientSubscribeResponseTypeDef):
    """
    Type definition for `ClientSubscribe` `Response`

    Response for Subscribe action.

    - **SubscriptionArn** *(string) --*

      The ARN of the subscription if it is confirmed, or the string "pending confirmation" if the
      subscription requires confirmation. However, if the API request parameter
      ``ReturnSubscriptionArn`` is true, then the value is always the subscription ARN, even if the
      subscription requires confirmation.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    The list of tags to be added to the specified topic.

    - **Key** *(string) --* **[REQUIRED]**

      The required key portion of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The optional value portion of the tag.
    """


_ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef(
    _ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEndpointsByPlatformApplicationPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef",
    {"EndpointArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef(
    _ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef
):
    """
    Type definition for `ListEndpointsByPlatformApplicationPaginateResponse` `Endpoints`

    Endpoint for mobile app and device.

    - **EndpointArn** *(string) --*

      EndpointArn for mobile app and device.

    - **Attributes** *(dict) --*

      Attributes for endpoint.

      - *(string) --*

        - *(string) --*
    """


_ListEndpointsByPlatformApplicationPaginateResponseTypeDef = TypedDict(
    "_ListEndpointsByPlatformApplicationPaginateResponseTypeDef",
    {
        "Endpoints": List[
            ListEndpointsByPlatformApplicationPaginateResponseEndpointsTypeDef
        ]
    },
    total=False,
)


class ListEndpointsByPlatformApplicationPaginateResponseTypeDef(
    _ListEndpointsByPlatformApplicationPaginateResponseTypeDef
):
    """
    Type definition for `ListEndpointsByPlatformApplicationPaginate` `Response`

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


_ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef(
    _ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPhoneNumbersOptedOutPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPhoneNumbersOptedOutPaginateResponseTypeDef = TypedDict(
    "_ListPhoneNumbersOptedOutPaginateResponseTypeDef",
    {"phoneNumbers": List[str], "NextToken": str},
    total=False,
)


class ListPhoneNumbersOptedOutPaginateResponseTypeDef(
    _ListPhoneNumbersOptedOutPaginateResponseTypeDef
):
    """
    Type definition for `ListPhoneNumbersOptedOutPaginate` `Response`

    The response from the ``ListPhoneNumbersOptedOut`` action.

    - **phoneNumbers** *(list) --*

      A list of phone numbers that are opted out of receiving SMS messages. The list is paginated,
      and each page can contain up to 100 phone numbers.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPlatformApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPlatformApplicationsPaginatePaginationConfigTypeDef(
    _ListPlatformApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPlatformApplicationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef",
    {"PlatformApplicationArn": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef(
    _ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef
):
    """
    Type definition for `ListPlatformApplicationsPaginateResponse` `PlatformApplications`

    Platform application object.

    - **PlatformApplicationArn** *(string) --*

      PlatformApplicationArn for platform application object.

    - **Attributes** *(dict) --*

      Attributes for platform application object.

      - *(string) --*

        - *(string) --*
    """


_ListPlatformApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListPlatformApplicationsPaginateResponseTypeDef",
    {
        "PlatformApplications": List[
            ListPlatformApplicationsPaginateResponsePlatformApplicationsTypeDef
        ]
    },
    total=False,
)


class ListPlatformApplicationsPaginateResponseTypeDef(
    _ListPlatformApplicationsPaginateResponseTypeDef
):
    """
    Type definition for `ListPlatformApplicationsPaginate` `Response`

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


_ListSubscriptionsByTopicPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionsByTopicPaginatePaginationConfigTypeDef(
    _ListSubscriptionsByTopicPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSubscriptionsByTopicPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
    },
    total=False,
)


class ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef(
    _ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef
):
    """
    Type definition for `ListSubscriptionsByTopicPaginateResponse` `Subscriptions`

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


_ListSubscriptionsByTopicPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionsByTopicPaginateResponseTypeDef",
    {
        "Subscriptions": List[
            ListSubscriptionsByTopicPaginateResponseSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ListSubscriptionsByTopicPaginateResponseTypeDef(
    _ListSubscriptionsByTopicPaginateResponseTypeDef
):
    """
    Type definition for `ListSubscriptionsByTopicPaginate` `Response`

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


_ListSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSubscriptionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSubscriptionsPaginateResponseSubscriptionsTypeDef = TypedDict(
    "_ListSubscriptionsPaginateResponseSubscriptionsTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
    },
    total=False,
)


class ListSubscriptionsPaginateResponseSubscriptionsTypeDef(
    _ListSubscriptionsPaginateResponseSubscriptionsTypeDef
):
    """
    Type definition for `ListSubscriptionsPaginateResponse` `Subscriptions`

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


_ListSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionsPaginateResponseTypeDef",
    {"Subscriptions": List[ListSubscriptionsPaginateResponseSubscriptionsTypeDef]},
    total=False,
)


class ListSubscriptionsPaginateResponseTypeDef(
    _ListSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `ListSubscriptionsPaginate` `Response`

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


_ListTopicsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTopicsPaginatePaginationConfigTypeDef(
    _ListTopicsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTopicsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTopicsPaginateResponseTopicsTypeDef = TypedDict(
    "_ListTopicsPaginateResponseTopicsTypeDef", {"TopicArn": str}, total=False
)


class ListTopicsPaginateResponseTopicsTypeDef(_ListTopicsPaginateResponseTopicsTypeDef):
    """
    Type definition for `ListTopicsPaginateResponse` `Topics`

    A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
    attributes, use ``GetTopicAttributes`` .

    - **TopicArn** *(string) --*

      The topic's ARN.
    """


_ListTopicsPaginateResponseTypeDef = TypedDict(
    "_ListTopicsPaginateResponseTypeDef",
    {"Topics": List[ListTopicsPaginateResponseTopicsTypeDef]},
    total=False,
)


class ListTopicsPaginateResponseTypeDef(_ListTopicsPaginateResponseTypeDef):
    """
    Type definition for `ListTopicsPaginate` `Response`

    Response for ListTopics action.

    - **Topics** *(list) --*

      A list of topic ARNs.

      - *(dict) --*

        A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
        attributes, use ``GetTopicAttributes`` .

        - **TopicArn** *(string) --*

          The topic's ARN.
    """


_RequiredPlatformEndpointPublishMessageAttributesTypeDef = TypedDict(
    "_RequiredPlatformEndpointPublishMessageAttributesTypeDef", {"DataType": str}
)
_OptionalPlatformEndpointPublishMessageAttributesTypeDef = TypedDict(
    "_OptionalPlatformEndpointPublishMessageAttributesTypeDef",
    {"StringValue": str, "BinaryValue": bytes},
    total=False,
)


class PlatformEndpointPublishMessageAttributesTypeDef(
    _RequiredPlatformEndpointPublishMessageAttributesTypeDef,
    _OptionalPlatformEndpointPublishMessageAttributesTypeDef,
):
    """
    Type definition for `PlatformEndpointPublish` `MessageAttributes`

    The user-specified message attribute value. For string data types, the value attribute has
    the same restrictions on the content as the message body. For more information, see `Publish
    <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .

    Name, type, and value must not be empty or null. In addition, the message body should not be
    empty or null. All parts of the message attribute, including name, type, and value, are
    included in the message size restriction, which is currently 256 KB (262,144 bytes). For more
    information, see `Using Amazon SNS Message Attributes
    <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SNS supports the following logical data types: String, String.Array, Number, and
      Binary. For more information, see `Message Attribute Data Types
      <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__
      .

    - **StringValue** *(string) --*

      Strings are Unicode with UTF8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, for example, compressed data, encrypted
      data, or images.
    """


_PlatformEndpointPublishResponseTypeDef = TypedDict(
    "_PlatformEndpointPublishResponseTypeDef", {"MessageId": str}, total=False
)


class PlatformEndpointPublishResponseTypeDef(_PlatformEndpointPublishResponseTypeDef):
    """
    Type definition for `PlatformEndpointPublish` `Response`

    Response for Publish action.

    - **MessageId** *(string) --*

      Unique identifier assigned to the published message.

      Length Constraint: Maximum 100 characters
    """


_ServiceResourceCreateTopicTagsTypeDef = TypedDict(
    "_ServiceResourceCreateTopicTagsTypeDef", {"Key": str, "Value": str}
)


class ServiceResourceCreateTopicTagsTypeDef(_ServiceResourceCreateTopicTagsTypeDef):
    """
    Type definition for `ServiceResourceCreateTopic` `Tags`

    The list of tags to be added to the specified topic.

    - **Key** *(string) --* **[REQUIRED]**

      The required key portion of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      The optional value portion of the tag.
    """


_RequiredTopicPublishMessageAttributesTypeDef = TypedDict(
    "_RequiredTopicPublishMessageAttributesTypeDef", {"DataType": str}
)
_OptionalTopicPublishMessageAttributesTypeDef = TypedDict(
    "_OptionalTopicPublishMessageAttributesTypeDef",
    {"StringValue": str, "BinaryValue": bytes},
    total=False,
)


class TopicPublishMessageAttributesTypeDef(
    _RequiredTopicPublishMessageAttributesTypeDef,
    _OptionalTopicPublishMessageAttributesTypeDef,
):
    """
    Type definition for `TopicPublish` `MessageAttributes`

    The user-specified message attribute value. For string data types, the value attribute has
    the same restrictions on the content as the message body. For more information, see `Publish
    <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .

    Name, type, and value must not be empty or null. In addition, the message body should not be
    empty or null. All parts of the message attribute, including name, type, and value, are
    included in the message size restriction, which is currently 256 KB (262,144 bytes). For more
    information, see `Using Amazon SNS Message Attributes
    <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SNS supports the following logical data types: String, String.Array, Number, and
      Binary. For more information, see `Message Attribute Data Types
      <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__
      .

    - **StringValue** *(string) --*

      Strings are Unicode with UTF8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, for example, compressed data, encrypted
      data, or images.
    """


_TopicPublishResponseTypeDef = TypedDict(
    "_TopicPublishResponseTypeDef", {"MessageId": str}, total=False
)


class TopicPublishResponseTypeDef(_TopicPublishResponseTypeDef):
    """
    Type definition for `TopicPublish` `Response`

    Response for Publish action.

    - **MessageId** *(string) --*

      Unique identifier assigned to the published message.

      Length Constraint: Maximum 100 characters
    """
