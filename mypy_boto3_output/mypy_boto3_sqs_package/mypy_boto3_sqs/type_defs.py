"Main interface for sqs type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientChangeMessageVisibilityBatchEntriesTypeDef",
    "ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    "ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    "ClientChangeMessageVisibilityBatchResponseTypeDef",
    "ClientCreateQueueResponseTypeDef",
    "ClientDeleteMessageBatchEntriesTypeDef",
    "ClientDeleteMessageBatchResponseFailedTypeDef",
    "ClientDeleteMessageBatchResponseSuccessfulTypeDef",
    "ClientDeleteMessageBatchResponseTypeDef",
    "ClientGetQueueAttributesResponseTypeDef",
    "ClientGetQueueUrlResponseTypeDef",
    "ClientListDeadLetterSourceQueuesResponseTypeDef",
    "ClientListQueueTagsResponseTypeDef",
    "ClientListQueuesResponseTypeDef",
    "ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    "ClientReceiveMessageResponseMessagesTypeDef",
    "ClientReceiveMessageResponseTypeDef",
    "ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    "ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    "ClientSendMessageBatchEntriesTypeDef",
    "ClientSendMessageBatchResponseFailedTypeDef",
    "ClientSendMessageBatchResponseSuccessfulTypeDef",
    "ClientSendMessageBatchResponseTypeDef",
    "ClientSendMessageMessageAttributesTypeDef",
    "ClientSendMessageMessageSystemAttributesTypeDef",
    "ClientSendMessageResponseTypeDef",
    "QueueChangeMessageVisibilityBatchEntriesTypeDef",
    "QueueChangeMessageVisibilityBatchResponseFailedTypeDef",
    "QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    "QueueChangeMessageVisibilityBatchResponseTypeDef",
    "QueueDeleteMessagesEntriesTypeDef",
    "QueueDeleteMessagesResponseFailedTypeDef",
    "QueueDeleteMessagesResponseSuccessfulTypeDef",
    "QueueDeleteMessagesResponseTypeDef",
    "QueueSendMessageMessageAttributesTypeDef",
    "QueueSendMessageMessageSystemAttributesTypeDef",
    "QueueSendMessageResponseTypeDef",
    "QueueSendMessagesEntriesMessageAttributesTypeDef",
    "QueueSendMessagesEntriesMessageSystemAttributesTypeDef",
    "QueueSendMessagesEntriesTypeDef",
    "QueueSendMessagesResponseFailedTypeDef",
    "QueueSendMessagesResponseSuccessfulTypeDef",
    "QueueSendMessagesResponseTypeDef",
)


_RequiredClientChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_RequiredClientChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str},
)
_OptionalClientChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_OptionalClientChangeMessageVisibilityBatchEntriesTypeDef",
    {"VisibilityTimeout": int},
    total=False,
)


class ClientChangeMessageVisibilityBatchEntriesTypeDef(
    _RequiredClientChangeMessageVisibilityBatchEntriesTypeDef,
    _OptionalClientChangeMessageVisibilityBatchEntriesTypeDef,
):
    """
    Type definition for `ClientChangeMessageVisibilityBatch` `Entries`

    Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch
    .``

    .. warning::

      All of the following list parameters must be prefixed with
      ``ChangeMessageVisibilityBatchRequestEntry.n`` , where ``n`` is an integer value starting
      with ``1`` . For example, a parameter list for this action might look like this:

     ``&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2``

     ``&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle``

     ``&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45``

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for this particular receipt handle used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

    - **ReceiptHandle** *(string) --* **[REQUIRED]**

      A receipt handle.

    - **VisibilityTimeout** *(integer) --*

      The new value (in seconds) for the message's visibility timeout.
    """


_ClientChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientChangeMessageVisibilityBatchResponseFailedTypeDef(
    _ClientChangeMessageVisibilityBatchResponseFailedTypeDef
):
    """
    Type definition for `ClientChangeMessageVisibilityBatchResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    {"Id": str},
    total=False,
)


class ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef(
    _ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef
):
    """
    Type definition for `ClientChangeMessageVisibilityBatchResponse` `Successful`

    Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``

    - **Id** *(string) --*

      Represents a message whose visibility timeout has been changed successfully.
    """


_ClientChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientChangeMessageVisibilityBatchResponseTypeDef(
    _ClientChangeMessageVisibilityBatchResponseTypeDef
):
    """
    Type definition for `ClientChangeMessageVisibilityBatch` `Response`

    For each message in the batch, the response contains a ``
    ChangeMessageVisibilityBatchResultEntry `` tag if the message succeeds or a ``
    BatchResultErrorEntry `` tag if the message fails.

    - **Successful** *(list) --*

      A list of ``  ChangeMessageVisibilityBatchResultEntry `` items.

      - *(dict) --*

        Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``

        - **Id** *(string) --*

          Represents a message whose visibility timeout has been changed successfully.

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """


_ClientCreateQueueResponseTypeDef = TypedDict(
    "_ClientCreateQueueResponseTypeDef", {"QueueUrl": str}, total=False
)


class ClientCreateQueueResponseTypeDef(_ClientCreateQueueResponseTypeDef):
    """
    Type definition for `ClientCreateQueue` `Response`

    Returns the ``QueueUrl`` attribute of the created queue.

    - **QueueUrl** *(string) --*

      The URL of the created Amazon SQS queue.
    """


_ClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_ClientDeleteMessageBatchEntriesTypeDef", {"Id": str, "ReceiptHandle": str}
)


class ClientDeleteMessageBatchEntriesTypeDef(_ClientDeleteMessageBatchEntriesTypeDef):
    """
    Type definition for `ClientDeleteMessageBatch` `Entries`

    Encloses a receipt handle and an identifier for it.

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for this particular receipt handle. This is used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

    - **ReceiptHandle** *(string) --* **[REQUIRED]**

      A receipt handle.
    """


_ClientDeleteMessageBatchResponseFailedTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientDeleteMessageBatchResponseFailedTypeDef(
    _ClientDeleteMessageBatchResponseFailedTypeDef
):
    """
    Type definition for `ClientDeleteMessageBatchResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_ClientDeleteMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class ClientDeleteMessageBatchResponseSuccessfulTypeDef(
    _ClientDeleteMessageBatchResponseSuccessfulTypeDef
):
    """
    Type definition for `ClientDeleteMessageBatchResponse` `Successful`

    Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``

    - **Id** *(string) --*

      Represents a successfully deleted message.
    """


_ClientDeleteMessageBatchResponseTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientDeleteMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientDeleteMessageBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientDeleteMessageBatchResponseTypeDef(_ClientDeleteMessageBatchResponseTypeDef):
    """
    Type definition for `ClientDeleteMessageBatch` `Response`

    For each message in the batch, the response contains a ``  DeleteMessageBatchResultEntry `` tag
    if the message is deleted or a ``  BatchResultErrorEntry `` tag if the message can't be deleted.

    - **Successful** *(list) --*

      A list of ``  DeleteMessageBatchResultEntry `` items.

      - *(dict) --*

        Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``

        - **Id** *(string) --*

          Represents a successfully deleted message.

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """


_ClientGetQueueAttributesResponseTypeDef = TypedDict(
    "_ClientGetQueueAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetQueueAttributesResponseTypeDef(_ClientGetQueueAttributesResponseTypeDef):
    """
    Type definition for `ClientGetQueueAttributes` `Response`

    A list of returned queue attributes.

    - **Attributes** *(dict) --*

      A map of attributes to their respective values.

      - *(string) --*

        - *(string) --*
    """


_ClientGetQueueUrlResponseTypeDef = TypedDict(
    "_ClientGetQueueUrlResponseTypeDef", {"QueueUrl": str}, total=False
)


class ClientGetQueueUrlResponseTypeDef(_ClientGetQueueUrlResponseTypeDef):
    """
    Type definition for `ClientGetQueueUrl` `Response`

    For more information, see `Interpreting Responses
    <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-responses.html>`__
    in the *Amazon Simple Queue Service Developer Guide* .

    - **QueueUrl** *(string) --*

      The URL of the queue.
    """


_ClientListDeadLetterSourceQueuesResponseTypeDef = TypedDict(
    "_ClientListDeadLetterSourceQueuesResponseTypeDef",
    {"queueUrls": List[str]},
    total=False,
)


class ClientListDeadLetterSourceQueuesResponseTypeDef(
    _ClientListDeadLetterSourceQueuesResponseTypeDef
):
    """
    Type definition for `ClientListDeadLetterSourceQueues` `Response`

    A list of your dead letter source queues.

    - **queueUrls** *(list) --*

      A list of source queue URLs that have the ``RedrivePolicy`` queue attribute configured with a
      dead-letter queue.

      - *(string) --*
    """


_ClientListQueueTagsResponseTypeDef = TypedDict(
    "_ClientListQueueTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListQueueTagsResponseTypeDef(_ClientListQueueTagsResponseTypeDef):
    """
    Type definition for `ClientListQueueTags` `Response`

    - **Tags** *(dict) --*

      The list of all tags added to the specified queue.

      - *(string) --*

        - *(string) --*
    """


_ClientListQueuesResponseTypeDef = TypedDict(
    "_ClientListQueuesResponseTypeDef", {"QueueUrls": List[str]}, total=False
)


class ClientListQueuesResponseTypeDef(_ClientListQueuesResponseTypeDef):
    """
    Type definition for `ClientListQueues` `Response`

    A list of your queues.

    - **QueueUrls** *(list) --*

      A list of queue URLs, up to 1,000 entries.

      - *(string) --*
    """


_ClientReceiveMessageResponseMessagesMessageAttributesTypeDef = TypedDict(
    "_ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientReceiveMessageResponseMessagesMessageAttributesTypeDef(
    _ClientReceiveMessageResponseMessagesMessageAttributesTypeDef
):
    """
    Type definition for `ClientReceiveMessageResponseMessages` `MessageAttributes`

    The user-specified message attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more
    information, see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
     parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are
     part of the message size restriction (256 KB or 262,144 bytes).

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see
      `ASCII Printable Characters
      <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data,
      encrypted data, or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --*

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message
      Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_ClientReceiveMessageResponseMessagesTypeDef = TypedDict(
    "_ClientReceiveMessageResponseMessagesTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[str, str],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[
            str, ClientReceiveMessageResponseMessagesMessageAttributesTypeDef
        ],
    },
    total=False,
)


class ClientReceiveMessageResponseMessagesTypeDef(
    _ClientReceiveMessageResponseMessagesTypeDef
):
    """
    Type definition for `ClientReceiveMessageResponse` `Messages`

    An Amazon SQS message.

    - **MessageId** *(string) --*

      A unique identifier for the message. A ``MessageId`` is considered unique across all AWS
      accounts for an extended period of time.

    - **ReceiptHandle** *(string) --*

      An identifier associated with the act of receiving the message. A new receipt handle is
      returned every time you receive a message. When deleting a message, you provide the last
      received receipt handle to delete the message.

    - **MD5OfBody** *(string) --*

      An MD5 digest of the non-URL-encoded message body string.

    - **Body** *(string) --*

      The message's contents (not URL-encoded).

    - **Attributes** *(dict) --*

      A map of the attributes requested in ``  ReceiveMessage `` to their respective values.
      Supported attributes:

      * ``ApproximateReceiveCount``

      * ``ApproximateFirstReceiveTimestamp``

      * ``MessageDeduplicationId``

      * ``MessageGroupId``

      * ``SenderId``

      * ``SentTimestamp``

      * ``SequenceNumber``

       ``ApproximateFirstReceiveTimestamp`` and ``SentTimestamp`` are each returned as an
       integer representing the `epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ in
       milliseconds.

      - *(string) --*

        - *(string) --*

    - **MD5OfMessageAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
      to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
      message before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MessageAttributes** *(dict) --*

      Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more
      information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      - *(string) --*

        - *(dict) --*

          The user-specified message attribute value. For string data types, the ``Value``
          attribute has the same restrictions on the content as the message body. For more
          information, see ``  SendMessage .``

           ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
           parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are
           part of the message size restriction (256 KB or 262,144 bytes).

          - **StringValue** *(string) --*

            Strings are Unicode with UTF-8 binary encoding. For a list of code values, see
            `ASCII Printable Characters
            <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

          - **BinaryValue** *(bytes) --*

            Binary type attributes can store any binary data, such as compressed data,
            encrypted data, or images.

          - **StringListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(string) --*

          - **BinaryListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(bytes) --*

          - **DataType** *(string) --*

            Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
            ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

            You can also append custom labels. For more information, see `Amazon SQS Message
            Attributes
            <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
            in the *Amazon Simple Queue Service Developer Guide* .
    """


_ClientReceiveMessageResponseTypeDef = TypedDict(
    "_ClientReceiveMessageResponseTypeDef",
    {"Messages": List[ClientReceiveMessageResponseMessagesTypeDef]},
    total=False,
)


class ClientReceiveMessageResponseTypeDef(_ClientReceiveMessageResponseTypeDef):
    """
    Type definition for `ClientReceiveMessage` `Response`

    A list of received messages.

    - **Messages** *(list) --*

      A list of messages.

      - *(dict) --*

        An Amazon SQS message.

        - **MessageId** *(string) --*

          A unique identifier for the message. A ``MessageId`` is considered unique across all AWS
          accounts for an extended period of time.

        - **ReceiptHandle** *(string) --*

          An identifier associated with the act of receiving the message. A new receipt handle is
          returned every time you receive a message. When deleting a message, you provide the last
          received receipt handle to delete the message.

        - **MD5OfBody** *(string) --*

          An MD5 digest of the non-URL-encoded message body string.

        - **Body** *(string) --*

          The message's contents (not URL-encoded).

        - **Attributes** *(dict) --*

          A map of the attributes requested in ``  ReceiveMessage `` to their respective values.
          Supported attributes:

          * ``ApproximateReceiveCount``

          * ``ApproximateFirstReceiveTimestamp``

          * ``MessageDeduplicationId``

          * ``MessageGroupId``

          * ``SenderId``

          * ``SentTimestamp``

          * ``SequenceNumber``

           ``ApproximateFirstReceiveTimestamp`` and ``SentTimestamp`` are each returned as an
           integer representing the `epoch time <http://en.wikipedia.org/wiki/Unix_time>`__ in
           milliseconds.

          - *(string) --*

            - *(string) --*

        - **MD5OfMessageAttributes** *(string) --*

          An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
          to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
          message before creating the MD5 digest. For information about MD5, see `RFC1321
          <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **MessageAttributes** *(dict) --*

          Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more
          information, see `Amazon SQS Message Attributes
          <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
          in the *Amazon Simple Queue Service Developer Guide* .

          - *(string) --*

            - *(dict) --*

              The user-specified message attribute value. For string data types, the ``Value``
              attribute has the same restrictions on the content as the message body. For more
              information, see ``  SendMessage .``

               ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
               parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are
               part of the message size restriction (256 KB or 262,144 bytes).

              - **StringValue** *(string) --*

                Strings are Unicode with UTF-8 binary encoding. For a list of code values, see
                `ASCII Printable Characters
                <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

              - **BinaryValue** *(bytes) --*

                Binary type attributes can store any binary data, such as compressed data,
                encrypted data, or images.

              - **StringListValues** *(list) --*

                Not implemented. Reserved for future use.

                - *(string) --*

              - **BinaryListValues** *(list) --*

                Not implemented. Reserved for future use.

                - *(bytes) --*

              - **DataType** *(string) --*

                Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
                ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

                You can also append custom labels. For more information, see `Amazon SQS Message
                Attributes
                <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
                in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredClientSendMessageBatchEntriesMessageAttributesTypeDef = TypedDict(
    "_RequiredClientSendMessageBatchEntriesMessageAttributesTypeDef", {"DataType": str}
)
_OptionalClientSendMessageBatchEntriesMessageAttributesTypeDef = TypedDict(
    "_OptionalClientSendMessageBatchEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class ClientSendMessageBatchEntriesMessageAttributesTypeDef(
    _RequiredClientSendMessageBatchEntriesMessageAttributesTypeDef,
    _OptionalClientSendMessageBatchEntriesMessageAttributesTypeDef,
):
    """
    Type definition for `ClientSendMessageBatchEntries` `MessageAttributes`

    The user-specified message attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more
    information, see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
     parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part
     of the message size restriction (256 KB or 262,144 bytes).

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
      .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted
      data, or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message
      Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredClientSendMessageBatchEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_RequiredClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    {"DataType": str},
)
_OptionalClientSendMessageBatchEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_OptionalClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef(
    _RequiredClientSendMessageBatchEntriesMessageSystemAttributesTypeDef,
    _OptionalClientSendMessageBatchEntriesMessageSystemAttributesTypeDef,
):
    """
    Type definition for `ClientSendMessageBatchEntries` `MessageSystemAttributes`

    The user-specified message system attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more
    information, see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
      .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted
      data, or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message
      Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientSendMessageBatchEntriesTypeDef", {"Id": str, "MessageBody": str}
)
_OptionalClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientSendMessageBatchEntriesTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[
            str, ClientSendMessageBatchEntriesMessageAttributesTypeDef
        ],
        "MessageSystemAttributes": Dict[
            str, ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class ClientSendMessageBatchEntriesTypeDef(
    _RequiredClientSendMessageBatchEntriesTypeDef,
    _OptionalClientSendMessageBatchEntriesTypeDef,
):
    """
    Type definition for `ClientSendMessageBatch` `Entries`

    Contains the details of a single Amazon SQS message along with an ``Id`` .

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for a message in this batch used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

        This identifier can have up to 80 characters. The following characters are accepted:
        alphanumeric characters, hyphens(-), and underscores (_).

    - **MessageBody** *(string) --* **[REQUIRED]**

      The body of the message.

    - **DelaySeconds** *(integer) --*

      The length of time, in seconds, for which a specific message is delayed. Valid values: 0 to
      900. Maximum: 15 minutes. Messages with a positive ``DelaySeconds`` value become available
      for processing after the delay period is finished. If you don't specify a value, the default
      value for the queue is applied.

      .. note::

        When you set ``FifoQueue`` , you can't set ``DelaySeconds`` per message. You can set this
        parameter only on a queue level.

    - **MessageAttributes** *(dict) --*

      Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more
      information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      - *(string) --*

        - *(dict) --*

          The user-specified message attribute value. For string data types, the ``Value``
          attribute has the same restrictions on the content as the message body. For more
          information, see ``  SendMessage .``

           ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
           parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part
           of the message size restriction (256 KB or 262,144 bytes).

          - **StringValue** *(string) --*

            Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
            Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
            .

          - **BinaryValue** *(bytes) --*

            Binary type attributes can store any binary data, such as compressed data, encrypted
            data, or images.

          - **StringListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(string) --*

          - **BinaryListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(bytes) --*

          - **DataType** *(string) --* **[REQUIRED]**

            Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
            ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

            You can also append custom labels. For more information, see `Amazon SQS Message
            Attributes
            <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
            in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageSystemAttributes** *(dict) --*

      The message system attribute to send Each message system attribute consists of a ``Name`` ,
      ``Type`` , and ``Value`` .

      .. warning::

        * Currently, the only supported message system attribute is ``AWSTraceHeader`` . Its type
        must be ``String`` and its value must be a correctly formatted AWS X-Ray trace string.

        * The size of a message system attribute doesn't count towards the total size of a message.

      - *(string) --*

        - *(dict) --*

          The user-specified message system attribute value. For string data types, the ``Value``
          attribute has the same restrictions on the content as the message body. For more
          information, see ``  SendMessage .``

           ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

          - **StringValue** *(string) --*

            Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
            Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
            .

          - **BinaryValue** *(bytes) --*

            Binary type attributes can store any binary data, such as compressed data, encrypted
            data, or images.

          - **StringListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(string) --*

          - **BinaryListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(bytes) --*

          - **DataType** *(string) --* **[REQUIRED]**

            Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
            ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

            You can also append custom labels. For more information, see `Amazon SQS Message
            Attributes
            <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
            in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageDeduplicationId** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The token used for deduplication of messages within a 5-minute minimum deduplication
      interval. If a message with a particular ``MessageDeduplicationId`` is sent successfully,
      subsequent messages with the same ``MessageDeduplicationId`` are accepted successfully but
      aren't delivered. For more information, see `Exactly-Once Processing
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      * Every message must have a unique ``MessageDeduplicationId`` ,

        * You may provide a ``MessageDeduplicationId`` explicitly.

        * If you aren't able to provide a ``MessageDeduplicationId`` and you enable
        ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate
        the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the
        message).

        * If you don't provide a ``MessageDeduplicationId`` and the queue doesn't have
        ``ContentBasedDeduplication`` set, the action fails with an error.

        * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId``
        overrides the generated one.

      * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent
      within the deduplication interval are treated as duplicates and only one copy of the message
      is delivered.

      * If you send one message with ``ContentBasedDeduplication`` enabled and then another message
      with a ``MessageDeduplicationId`` that is the same as the one generated for the first
      ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of
      the message is delivered.

      .. note::

        The ``MessageDeduplicationId`` is available to the consumer of the message (this can be
        useful for troubleshooting delivery issues).

        If a message is sent successfully but the acknowledgement is lost and the message is resent
        with the same ``MessageDeduplicationId`` after the deduplication interval, Amazon SQS can't
        detect duplicate messages.

        Amazon SQS continues to keep track of the message deduplication ID even after the message
        is received and deleted.

      The length of ``MessageDeduplicationId`` is 128 characters. ``MessageDeduplicationId`` can
      contain alphanumeric characters (``a-z`` , ``A-Z`` , ``0-9`` ) and punctuation
      (``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~`` ).

      For best practices of using ``MessageDeduplicationId`` , see `Using the
      MessageDeduplicationId Property
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageGroupId** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The tag that specifies that a message belongs to a specific message group. Messages that
      belong to the same message group are processed in a FIFO manner (however, messages in
      different message groups might be processed out of order). To interleave multiple ordered
      streams within a single queue, use ``MessageGroupId`` values (for example, session data for
      multiple users). In this scenario, multiple consumers can process the queue, but the session
      data of each user is processed in a FIFO fashion.

      * You must associate a non-empty ``MessageGroupId`` with a message. If you don't provide a
      ``MessageGroupId`` , the action fails.

      * ``ReceiveMessage`` might return messages with multiple ``MessageGroupId`` values. For each
      ``MessageGroupId`` , the messages are sorted by time sent. The caller can't specify a
      ``MessageGroupId`` .

      The length of ``MessageGroupId`` is 128 characters. Valid values: alphanumeric characters and
      punctuation ``(!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)`` .

      For best practices of using ``MessageGroupId`` , see `Using the MessageGroupId Property
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      .. warning::

         ``MessageGroupId`` is required for FIFO queues. You can't use it for Standard queues.
    """


_ClientSendMessageBatchResponseFailedTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientSendMessageBatchResponseFailedTypeDef(
    _ClientSendMessageBatchResponseFailedTypeDef
):
    """
    Type definition for `ClientSendMessageBatchResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_ClientSendMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseSuccessfulTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)


class ClientSendMessageBatchResponseSuccessfulTypeDef(
    _ClientSendMessageBatchResponseSuccessfulTypeDef
):
    """
    Type definition for `ClientSendMessageBatchResponse` `Successful`

    Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``

    - **Id** *(string) --*

      An identifier for the message in this batch.

    - **MessageId** *(string) --*

      An identifier for the message.

    - **MD5OfMessageBody** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
      to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
      message before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
      to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
      message before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageSystemAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message system attribute string. You can use this
      attribute to verify that Amazon SQS received the message correctly. Amazon SQS
      URL-decodes the message before creating the MD5 digest. For information about MD5, see
      `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **SequenceNumber** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The large, non-consecutive number that Amazon SQS assigns to each message.

      The length of ``SequenceNumber`` is 128 bits. As ``SequenceNumber`` continues to increase
      for a particular ``MessageGroupId`` .
    """


_ClientSendMessageBatchResponseTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientSendMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientSendMessageBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientSendMessageBatchResponseTypeDef(_ClientSendMessageBatchResponseTypeDef):
    """
    Type definition for `ClientSendMessageBatch` `Response`

    For each message in the batch, the response contains a ``  SendMessageBatchResultEntry `` tag
    if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.

    - **Successful** *(list) --*

      A list of ``  SendMessageBatchResultEntry `` items.

      - *(dict) --*

        Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``

        - **Id** *(string) --*

          An identifier for the message in this batch.

        - **MessageId** *(string) --*

          An identifier for the message.

        - **MD5OfMessageBody** *(string) --*

          An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
          to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
          message before creating the MD5 digest. For information about MD5, see `RFC1321
          <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **MD5OfMessageAttributes** *(string) --*

          An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
          to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
          message before creating the MD5 digest. For information about MD5, see `RFC1321
          <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **MD5OfMessageSystemAttributes** *(string) --*

          An MD5 digest of the non-URL-encoded message system attribute string. You can use this
          attribute to verify that Amazon SQS received the message correctly. Amazon SQS
          URL-decodes the message before creating the MD5 digest. For information about MD5, see
          `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **SequenceNumber** *(string) --*

          This parameter applies only to FIFO (first-in-first-out) queues.

          The large, non-consecutive number that Amazon SQS assigns to each message.

          The length of ``SequenceNumber`` is 128 bits. As ``SequenceNumber`` continues to increase
          for a particular ``MessageGroupId`` .

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items with error details about each message that can't
      be enqueued.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """


_RequiredClientSendMessageMessageAttributesTypeDef = TypedDict(
    "_RequiredClientSendMessageMessageAttributesTypeDef", {"DataType": str}
)
_OptionalClientSendMessageMessageAttributesTypeDef = TypedDict(
    "_OptionalClientSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class ClientSendMessageMessageAttributesTypeDef(
    _RequiredClientSendMessageMessageAttributesTypeDef,
    _OptionalClientSendMessageMessageAttributesTypeDef,
):
    """
    Type definition for `ClientSendMessage` `MessageAttributes`

    The user-specified message attribute value. For string data types, the ``Value`` attribute
    has the same restrictions on the content as the message body. For more information, see ``
    SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All parts of
     the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part of the
     message size restriction (256 KB or 262,144 bytes).

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted data,
      or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredClientSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_RequiredClientSendMessageMessageSystemAttributesTypeDef", {"DataType": str}
)
_OptionalClientSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_OptionalClientSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class ClientSendMessageMessageSystemAttributesTypeDef(
    _RequiredClientSendMessageMessageSystemAttributesTypeDef,
    _OptionalClientSendMessageMessageSystemAttributesTypeDef,
):
    """
    Type definition for `ClientSendMessage` `MessageSystemAttributes`

    The user-specified message system attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more information,
    see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted data,
      or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_ClientSendMessageResponseTypeDef = TypedDict(
    "_ClientSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)


class ClientSendMessageResponseTypeDef(_ClientSendMessageResponseTypeDef):
    """
    Type definition for `ClientSendMessage` `Response`

    The ``MD5OfMessageBody`` and ``MessageId`` elements.

    - **MD5OfMessageBody** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
      verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
      before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
      verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
      before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageSystemAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message system attribute string. You can use this
      attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes
      the message before creating the MD5 digest.

    - **MessageId** *(string) --*

      An attribute containing the ``MessageId`` of the message sent to the queue. For more
      information, see `Queue and Message Identifiers
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

    - **SequenceNumber** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The large, non-consecutive number that Amazon SQS assigns to each message.

      The length of ``SequenceNumber`` is 128 bits. ``SequenceNumber`` continues to increase for a
      particular ``MessageGroupId`` .
    """


_RequiredQueueChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_RequiredQueueChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str},
)
_OptionalQueueChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_OptionalQueueChangeMessageVisibilityBatchEntriesTypeDef",
    {"VisibilityTimeout": int},
    total=False,
)


class QueueChangeMessageVisibilityBatchEntriesTypeDef(
    _RequiredQueueChangeMessageVisibilityBatchEntriesTypeDef,
    _OptionalQueueChangeMessageVisibilityBatchEntriesTypeDef,
):
    """
    Type definition for `QueueChangeMessageVisibilityBatch` `Entries`

    Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch
    .``

    .. warning::

      All of the following list parameters must be prefixed with
      ``ChangeMessageVisibilityBatchRequestEntry.n`` , where ``n`` is an integer value starting
      with ``1`` . For example, a parameter list for this action might look like this:

     ``&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2``

     ``&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle``

     ``&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45``

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for this particular receipt handle used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

    - **ReceiptHandle** *(string) --* **[REQUIRED]**

      A receipt handle.

    - **VisibilityTimeout** *(integer) --*

      The new value (in seconds) for the message's visibility timeout.
    """


_QueueChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueChangeMessageVisibilityBatchResponseFailedTypeDef(
    _QueueChangeMessageVisibilityBatchResponseFailedTypeDef
):
    """
    Type definition for `QueueChangeMessageVisibilityBatchResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    {"Id": str},
    total=False,
)


class QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef(
    _QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef
):
    """
    Type definition for `QueueChangeMessageVisibilityBatchResponse` `Successful`

    Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``

    - **Id** *(string) --*

      Represents a message whose visibility timeout has been changed successfully.
    """


_QueueChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[QueueChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)


class QueueChangeMessageVisibilityBatchResponseTypeDef(
    _QueueChangeMessageVisibilityBatchResponseTypeDef
):
    """
    Type definition for `QueueChangeMessageVisibilityBatch` `Response`

    For each message in the batch, the response contains a ``
    ChangeMessageVisibilityBatchResultEntry `` tag if the message succeeds or a ``
    BatchResultErrorEntry `` tag if the message fails.

    - **Successful** *(list) --*

      A list of ``  ChangeMessageVisibilityBatchResultEntry `` items.

      - *(dict) --*

        Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``

        - **Id** *(string) --*

          Represents a message whose visibility timeout has been changed successfully.

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """


_QueueDeleteMessagesEntriesTypeDef = TypedDict(
    "_QueueDeleteMessagesEntriesTypeDef", {"Id": str, "ReceiptHandle": str}
)


class QueueDeleteMessagesEntriesTypeDef(_QueueDeleteMessagesEntriesTypeDef):
    """
    Type definition for `QueueDeleteMessages` `Entries`

    Encloses a receipt handle and an identifier for it.

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for this particular receipt handle. This is used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

    - **ReceiptHandle** *(string) --* **[REQUIRED]**

      A receipt handle.
    """


_QueueDeleteMessagesResponseFailedTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueDeleteMessagesResponseFailedTypeDef(
    _QueueDeleteMessagesResponseFailedTypeDef
):
    """
    Type definition for `QueueDeleteMessagesResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_QueueDeleteMessagesResponseSuccessfulTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class QueueDeleteMessagesResponseSuccessfulTypeDef(
    _QueueDeleteMessagesResponseSuccessfulTypeDef
):
    """
    Type definition for `QueueDeleteMessagesResponse` `Successful`

    Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``

    - **Id** *(string) --*

      Represents a successfully deleted message.
    """


_QueueDeleteMessagesResponseTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseTypeDef",
    {
        "Successful": List[QueueDeleteMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueDeleteMessagesResponseFailedTypeDef],
    },
    total=False,
)


class QueueDeleteMessagesResponseTypeDef(_QueueDeleteMessagesResponseTypeDef):
    """
    Type definition for `QueueDeleteMessages` `Response`

    For each message in the batch, the response contains a ``  DeleteMessageBatchResultEntry `` tag
    if the message is deleted or a ``  BatchResultErrorEntry `` tag if the message can't be deleted.

    - **Successful** *(list) --*

      A list of ``  DeleteMessageBatchResultEntry `` items.

      - *(dict) --*

        Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``

        - **Id** *(string) --*

          Represents a successfully deleted message.

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """


_RequiredQueueSendMessageMessageAttributesTypeDef = TypedDict(
    "_RequiredQueueSendMessageMessageAttributesTypeDef", {"DataType": str}
)
_OptionalQueueSendMessageMessageAttributesTypeDef = TypedDict(
    "_OptionalQueueSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class QueueSendMessageMessageAttributesTypeDef(
    _RequiredQueueSendMessageMessageAttributesTypeDef,
    _OptionalQueueSendMessageMessageAttributesTypeDef,
):
    """
    Type definition for `QueueSendMessage` `MessageAttributes`

    The user-specified message attribute value. For string data types, the ``Value`` attribute
    has the same restrictions on the content as the message body. For more information, see ``
    SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All parts of
     the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part of the
     message size restriction (256 KB or 262,144 bytes).

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted data,
      or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredQueueSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_RequiredQueueSendMessageMessageSystemAttributesTypeDef", {"DataType": str}
)
_OptionalQueueSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_OptionalQueueSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class QueueSendMessageMessageSystemAttributesTypeDef(
    _RequiredQueueSendMessageMessageSystemAttributesTypeDef,
    _OptionalQueueSendMessageMessageSystemAttributesTypeDef,
):
    """
    Type definition for `QueueSendMessage` `MessageSystemAttributes`

    The user-specified message system attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more information,
    see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted data,
      or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_QueueSendMessageResponseTypeDef = TypedDict(
    "_QueueSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)


class QueueSendMessageResponseTypeDef(_QueueSendMessageResponseTypeDef):
    """
    Type definition for `QueueSendMessage` `Response`

    The ``MD5OfMessageBody`` and ``MessageId`` elements.

    - **MD5OfMessageBody** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
      verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
      before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
      verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
      before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageSystemAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message system attribute string. You can use this
      attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes
      the message before creating the MD5 digest.

    - **MessageId** *(string) --*

      An attribute containing the ``MessageId`` of the message sent to the queue. For more
      information, see `Queue and Message Identifiers
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

    - **SequenceNumber** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The large, non-consecutive number that Amazon SQS assigns to each message.

      The length of ``SequenceNumber`` is 128 bits. ``SequenceNumber`` continues to increase for a
      particular ``MessageGroupId`` .
    """


_RequiredQueueSendMessagesEntriesMessageAttributesTypeDef = TypedDict(
    "_RequiredQueueSendMessagesEntriesMessageAttributesTypeDef", {"DataType": str}
)
_OptionalQueueSendMessagesEntriesMessageAttributesTypeDef = TypedDict(
    "_OptionalQueueSendMessagesEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class QueueSendMessagesEntriesMessageAttributesTypeDef(
    _RequiredQueueSendMessagesEntriesMessageAttributesTypeDef,
    _OptionalQueueSendMessagesEntriesMessageAttributesTypeDef,
):
    """
    Type definition for `QueueSendMessagesEntries` `MessageAttributes`

    The user-specified message attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more
    information, see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
     parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part
     of the message size restriction (256 KB or 262,144 bytes).

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
      .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted
      data, or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message
      Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredQueueSendMessagesEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_RequiredQueueSendMessagesEntriesMessageSystemAttributesTypeDef", {"DataType": str}
)
_OptionalQueueSendMessagesEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_OptionalQueueSendMessagesEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class QueueSendMessagesEntriesMessageSystemAttributesTypeDef(
    _RequiredQueueSendMessagesEntriesMessageSystemAttributesTypeDef,
    _OptionalQueueSendMessagesEntriesMessageSystemAttributesTypeDef,
):
    """
    Type definition for `QueueSendMessagesEntries` `MessageSystemAttributes`

    The user-specified message system attribute value. For string data types, the ``Value``
    attribute has the same restrictions on the content as the message body. For more
    information, see ``  SendMessage .``

     ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

    - **StringValue** *(string) --*

      Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
      Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
      .

    - **BinaryValue** *(bytes) --*

      Binary type attributes can store any binary data, such as compressed data, encrypted
      data, or images.

    - **StringListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(string) --*

    - **BinaryListValues** *(list) --*

      Not implemented. Reserved for future use.

      - *(bytes) --*

    - **DataType** *(string) --* **[REQUIRED]**

      Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
      ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

      You can also append custom labels. For more information, see `Amazon SQS Message
      Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
    """


_RequiredQueueSendMessagesEntriesTypeDef = TypedDict(
    "_RequiredQueueSendMessagesEntriesTypeDef", {"Id": str, "MessageBody": str}
)
_OptionalQueueSendMessagesEntriesTypeDef = TypedDict(
    "_OptionalQueueSendMessagesEntriesTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[
            str, QueueSendMessagesEntriesMessageAttributesTypeDef
        ],
        "MessageSystemAttributes": Dict[
            str, QueueSendMessagesEntriesMessageSystemAttributesTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class QueueSendMessagesEntriesTypeDef(
    _RequiredQueueSendMessagesEntriesTypeDef, _OptionalQueueSendMessagesEntriesTypeDef
):
    """
    Type definition for `QueueSendMessages` `Entries`

    Contains the details of a single Amazon SQS message along with an ``Id`` .

    - **Id** *(string) --* **[REQUIRED]**

      An identifier for a message in this batch used to communicate the result.

      .. note::

        The ``Id`` s of a batch request need to be unique within a request

        This identifier can have up to 80 characters. The following characters are accepted:
        alphanumeric characters, hyphens(-), and underscores (_).

    - **MessageBody** *(string) --* **[REQUIRED]**

      The body of the message.

    - **DelaySeconds** *(integer) --*

      The length of time, in seconds, for which a specific message is delayed. Valid values: 0 to
      900. Maximum: 15 minutes. Messages with a positive ``DelaySeconds`` value become available
      for processing after the delay period is finished. If you don't specify a value, the default
      value for the queue is applied.

      .. note::

        When you set ``FifoQueue`` , you can't set ``DelaySeconds`` per message. You can set this
        parameter only on a queue level.

    - **MessageAttributes** *(dict) --*

      Each message attribute consists of a ``Name`` , ``Type`` , and ``Value`` . For more
      information, see `Amazon SQS Message Attributes
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      - *(string) --*

        - *(dict) --*

          The user-specified message attribute value. For string data types, the ``Value``
          attribute has the same restrictions on the content as the message body. For more
          information, see ``  SendMessage .``

           ``Name`` , ``type`` , ``value`` and the message body must not be empty or null. All
           parts of the message attribute, including ``Name`` , ``Type`` , and ``Value`` , are part
           of the message size restriction (256 KB or 262,144 bytes).

          - **StringValue** *(string) --*

            Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
            Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
            .

          - **BinaryValue** *(bytes) --*

            Binary type attributes can store any binary data, such as compressed data, encrypted
            data, or images.

          - **StringListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(string) --*

          - **BinaryListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(bytes) --*

          - **DataType** *(string) --* **[REQUIRED]**

            Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
            ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

            You can also append custom labels. For more information, see `Amazon SQS Message
            Attributes
            <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
            in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageSystemAttributes** *(dict) --*

      The message system attribute to send Each message system attribute consists of a ``Name`` ,
      ``Type`` , and ``Value`` .

      .. warning::

        * Currently, the only supported message system attribute is ``AWSTraceHeader`` . Its type
        must be ``String`` and its value must be a correctly formatted AWS X-Ray trace string.

        * The size of a message system attribute doesn't count towards the total size of a message.

      - *(string) --*

        - *(dict) --*

          The user-specified message system attribute value. For string data types, the ``Value``
          attribute has the same restrictions on the content as the message body. For more
          information, see ``  SendMessage .``

           ``Name`` , ``type`` , ``value`` and the message body must not be empty or null.

          - **StringValue** *(string) --*

            Strings are Unicode with UTF-8 binary encoding. For a list of code values, see `ASCII
            Printable Characters <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__
            .

          - **BinaryValue** *(bytes) --*

            Binary type attributes can store any binary data, such as compressed data, encrypted
            data, or images.

          - **StringListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(string) --*

          - **BinaryListValues** *(list) --*

            Not implemented. Reserved for future use.

            - *(bytes) --*

          - **DataType** *(string) --* **[REQUIRED]**

            Amazon SQS supports the following logical data types: ``String`` , ``Number`` , and
            ``Binary`` . For the ``Number`` data type, you must use ``StringValue`` .

            You can also append custom labels. For more information, see `Amazon SQS Message
            Attributes
            <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-attributes.html>`__
            in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageDeduplicationId** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The token used for deduplication of messages within a 5-minute minimum deduplication
      interval. If a message with a particular ``MessageDeduplicationId`` is sent successfully,
      subsequent messages with the same ``MessageDeduplicationId`` are accepted successfully but
      aren't delivered. For more information, see `Exactly-Once Processing
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      * Every message must have a unique ``MessageDeduplicationId`` ,

        * You may provide a ``MessageDeduplicationId`` explicitly.

        * If you aren't able to provide a ``MessageDeduplicationId`` and you enable
        ``ContentBasedDeduplication`` for your queue, Amazon SQS uses a SHA-256 hash to generate
        the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the
        message).

        * If you don't provide a ``MessageDeduplicationId`` and the queue doesn't have
        ``ContentBasedDeduplication`` set, the action fails with an error.

        * If the queue has ``ContentBasedDeduplication`` set, your ``MessageDeduplicationId``
        overrides the generated one.

      * When ``ContentBasedDeduplication`` is in effect, messages with identical content sent
      within the deduplication interval are treated as duplicates and only one copy of the message
      is delivered.

      * If you send one message with ``ContentBasedDeduplication`` enabled and then another message
      with a ``MessageDeduplicationId`` that is the same as the one generated for the first
      ``MessageDeduplicationId`` , the two messages are treated as duplicates and only one copy of
      the message is delivered.

      .. note::

        The ``MessageDeduplicationId`` is available to the consumer of the message (this can be
        useful for troubleshooting delivery issues).

        If a message is sent successfully but the acknowledgement is lost and the message is resent
        with the same ``MessageDeduplicationId`` after the deduplication interval, Amazon SQS can't
        detect duplicate messages.

        Amazon SQS continues to keep track of the message deduplication ID even after the message
        is received and deleted.

      The length of ``MessageDeduplicationId`` is 128 characters. ``MessageDeduplicationId`` can
      contain alphanumeric characters (``a-z`` , ``A-Z`` , ``0-9`` ) and punctuation
      (``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~`` ).

      For best practices of using ``MessageDeduplicationId`` , see `Using the
      MessageDeduplicationId Property
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

    - **MessageGroupId** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The tag that specifies that a message belongs to a specific message group. Messages that
      belong to the same message group are processed in a FIFO manner (however, messages in
      different message groups might be processed out of order). To interleave multiple ordered
      streams within a single queue, use ``MessageGroupId`` values (for example, session data for
      multiple users). In this scenario, multiple consumers can process the queue, but the session
      data of each user is processed in a FIFO fashion.

      * You must associate a non-empty ``MessageGroupId`` with a message. If you don't provide a
      ``MessageGroupId`` , the action fails.

      * ``ReceiveMessage`` might return messages with multiple ``MessageGroupId`` values. For each
      ``MessageGroupId`` , the messages are sorted by time sent. The caller can't specify a
      ``MessageGroupId`` .

      The length of ``MessageGroupId`` is 128 characters. Valid values: alphanumeric characters and
      punctuation ``(!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)`` .

      For best practices of using ``MessageGroupId`` , see `Using the MessageGroupId Property
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .

      .. warning::

         ``MessageGroupId`` is required for FIFO queues. You can't use it for Standard queues.
    """


_QueueSendMessagesResponseFailedTypeDef = TypedDict(
    "_QueueSendMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueSendMessagesResponseFailedTypeDef(_QueueSendMessagesResponseFailedTypeDef):
    """
    Type definition for `QueueSendMessagesResponse` `Failed`

    Gives a detailed description of the result of an action on each entry in the request.

    - **Id** *(string) --*

      The ``Id`` of an entry in a batch request.

    - **SenderFault** *(boolean) --*

      Specifies whether the error happened due to the producer.

    - **Code** *(string) --*

      An error code representing why the action failed on this entry.

    - **Message** *(string) --*

      A message explaining why the action failed on this entry.
    """


_QueueSendMessagesResponseSuccessfulTypeDef = TypedDict(
    "_QueueSendMessagesResponseSuccessfulTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)


class QueueSendMessagesResponseSuccessfulTypeDef(
    _QueueSendMessagesResponseSuccessfulTypeDef
):
    """
    Type definition for `QueueSendMessagesResponse` `Successful`

    Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``

    - **Id** *(string) --*

      An identifier for the message in this batch.

    - **MessageId** *(string) --*

      An identifier for the message.

    - **MD5OfMessageBody** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
      to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
      message before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
      to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
      message before creating the MD5 digest. For information about MD5, see `RFC1321
      <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **MD5OfMessageSystemAttributes** *(string) --*

      An MD5 digest of the non-URL-encoded message system attribute string. You can use this
      attribute to verify that Amazon SQS received the message correctly. Amazon SQS
      URL-decodes the message before creating the MD5 digest. For information about MD5, see
      `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .

    - **SequenceNumber** *(string) --*

      This parameter applies only to FIFO (first-in-first-out) queues.

      The large, non-consecutive number that Amazon SQS assigns to each message.

      The length of ``SequenceNumber`` is 128 bits. As ``SequenceNumber`` continues to increase
      for a particular ``MessageGroupId`` .
    """


_QueueSendMessagesResponseTypeDef = TypedDict(
    "_QueueSendMessagesResponseTypeDef",
    {
        "Successful": List[QueueSendMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueSendMessagesResponseFailedTypeDef],
    },
    total=False,
)


class QueueSendMessagesResponseTypeDef(_QueueSendMessagesResponseTypeDef):
    """
    Type definition for `QueueSendMessages` `Response`

    For each message in the batch, the response contains a ``  SendMessageBatchResultEntry `` tag
    if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.

    - **Successful** *(list) --*

      A list of ``  SendMessageBatchResultEntry `` items.

      - *(dict) --*

        Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``

        - **Id** *(string) --*

          An identifier for the message in this batch.

        - **MessageId** *(string) --*

          An identifier for the message.

        - **MD5OfMessageBody** *(string) --*

          An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
          to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
          message before creating the MD5 digest. For information about MD5, see `RFC1321
          <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **MD5OfMessageAttributes** *(string) --*

          An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute
          to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the
          message before creating the MD5 digest. For information about MD5, see `RFC1321
          <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **MD5OfMessageSystemAttributes** *(string) --*

          An MD5 digest of the non-URL-encoded message system attribute string. You can use this
          attribute to verify that Amazon SQS received the message correctly. Amazon SQS
          URL-decodes the message before creating the MD5 digest. For information about MD5, see
          `RFC1321 <https://www.ietf.org/rfc/rfc1321.txt>`__ .

        - **SequenceNumber** *(string) --*

          This parameter applies only to FIFO (first-in-first-out) queues.

          The large, non-consecutive number that Amazon SQS assigns to each message.

          The length of ``SequenceNumber`` is 128 bits. As ``SequenceNumber`` continues to increase
          for a particular ``MessageGroupId`` .

    - **Failed** *(list) --*

      A list of ``  BatchResultErrorEntry `` items with error details about each message that can't
      be enqueued.

      - *(dict) --*

        Gives a detailed description of the result of an action on each entry in the request.

        - **Id** *(string) --*

          The ``Id`` of an entry in a batch request.

        - **SenderFault** *(boolean) --*

          Specifies whether the error happened due to the producer.

        - **Code** *(string) --*

          An error code representing why the action failed on this entry.

        - **Message** *(string) --*

          A message explaining why the action failed on this entry.
    """
