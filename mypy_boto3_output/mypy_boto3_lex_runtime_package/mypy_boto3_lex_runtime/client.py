"Main interface for lex-runtime Client"
from __future__ import annotations

from typing import Dict, IO, List, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lex_runtime.client as client_scope
from mypy_boto3_lex_runtime.type_defs import (
    ClientDeleteSessionResponseTypeDef,
    ClientGetSessionResponseTypeDef,
    ClientPostContentResponseTypeDef,
    ClientPostTextResponseTypeDef,
    ClientPutSessionResponseTypeDef,
    ClientPutSessiondialogActionTypeDef,
    ClientPutSessionrecentIntentSummaryViewTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_session(
        self, botName: str, botAlias: str, userId: str
    ) -> ClientDeleteSessionResponseTypeDef:
        """
        Removes session information for a specified bot, alias, and user ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/DeleteSession>`_

        **Request Syntax**
        ::

          response = client.delete_session(
              botName='string',
              botAlias='string',
              userId='string'
          )
        :type botName: string
        :param botName: **[REQUIRED]**

          The name of the bot that contains the session data.

        :type botAlias: string
        :param botAlias: **[REQUIRED]**

          The alias in use for the bot that contains the session data.

        :type userId: string
        :param userId: **[REQUIRED]**

          The identifier of the user associated with the session data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'botName': 'string',
                'botAlias': 'string',
                'userId': 'string',
                'sessionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **botName** *(string) --*

              The name of the bot associated with the session data.

            - **botAlias** *(string) --*

              The alias in use for the bot associated with the session data.

            - **userId** *(string) --*

              The ID of the client application user.

            - **sessionId** *(string) --*

              The unique identifier for the session.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        checkpointLabelFilter: str = None,
    ) -> ClientGetSessionResponseTypeDef:
        """
        Returns session information for a specified bot, alias, and user ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/GetSession>`_

        **Request Syntax**
        ::

          response = client.get_session(
              botName='string',
              botAlias='string',
              userId='string',
              checkpointLabelFilter='string'
          )
        :type botName: string
        :param botName: **[REQUIRED]**

          The name of the bot that contains the session data.

        :type botAlias: string
        :param botAlias: **[REQUIRED]**

          The alias in use for the bot that contains the session data.

        :type userId: string
        :param userId: **[REQUIRED]**

          The ID of the client application user. Amazon Lex uses this to identify a user's conversation
          with your bot.

        :type checkpointLabelFilter: string
        :param checkpointLabelFilter:

          A string used to filter the intents returned in the ``recentIntentSummaryView`` structure.

          When you specify a filter, only intents with their ``checkpointLabel`` field set to that string
          are returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'recentIntentSummaryView': [
                    {
                        'intentName': 'string',
                        'checkpointLabel': 'string',
                        'slots': {
                            'string': 'string'
                        },
                        'confirmationStatus': 'None'|'Confirmed'|'Denied',
                        'dialogActionType': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Close'|'Delegate',
                        'fulfillmentState': 'Fulfilled'|'Failed'|'ReadyForFulfillment',
                        'slotToElicit': 'string'
                    },
                ],
                'sessionAttributes': {
                    'string': 'string'
                },
                'sessionId': 'string',
                'dialogAction': {
                    'type': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Close'|'Delegate',
                    'intentName': 'string',
                    'slots': {
                        'string': 'string'
                    },
                    'slotToElicit': 'string',
                    'fulfillmentState': 'Fulfilled'|'Failed'|'ReadyForFulfillment',
                    'message': 'string',
                    'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **recentIntentSummaryView** *(list) --*

              An array of information about the intents used in the session. The array can contain a
              maximum of three summaries. If more than three intents are used in the session, the
              ``recentIntentSummaryView`` operation contains information about the last three intents used.

              If you set the ``checkpointLabelFilter`` parameter in the request, the array contains only
              the intents with the specified label.

              - *(dict) --*

                Provides information about the state of an intent. You can use this information to get the
                current state of an intent so that you can process the intent, or so that you can return
                the intent to its previous state.

                - **intentName** *(string) --*

                  The name of the intent.

                - **checkpointLabel** *(string) --*

                  A user-defined label that identifies a particular intent. You can use this label to
                  return to a previous intent.

                  Use the ``checkpointLabelFilter`` parameter of the ``GetSessionRequest`` operation to
                  filter the intents returned by the operation to those with only the specified label.

                - **slots** *(dict) --*

                  Map of the slots that have been gathered and their values.

                  - *(string) --*

                    - *(string) --*

                - **confirmationStatus** *(string) --*

                  The status of the intent after the user responds to the confirmation prompt. If the user
                  confirms the intent, Amazon Lex sets this field to ``Confirmed`` . If the user denies the
                  intent, Amazon Lex sets this value to ``Denied`` . The possible values are:

                  * ``Confirmed`` - The user has responded "Yes" to the confirmation prompt, confirming
                  that the intent is complete and that it is ready to be fulfilled.

                  * ``Denied`` - The user has responded "No" to the confirmation prompt.

                  * ``None`` - The user has never been prompted for confirmation; or, the user was prompted
                  but did not confirm or deny the prompt.

                - **dialogActionType** *(string) --*

                  The next action that the bot should take in its interaction with the user. The possible
                  values are:

                  * ``ConfirmIntent`` - The next action is asking the user if the intent is complete and
                  ready to be fulfilled. This is a yes/no question such as "Place the order?"

                  * ``Close`` - Indicates that the there will not be a response from the user. For example,
                  the statement "Your order has been placed" does not require a response.

                  * ``ElicitIntent`` - The next action is to determine the intent that the user wants to
                  fulfill.

                  * ``ElicitSlot`` - The next action is to elicit a slot value from the user.

                - **fulfillmentState** *(string) --*

                  The fulfillment state of the intent. The possible values are:

                  * ``Failed`` - The Lambda function associated with the intent failed to fulfill the
                  intent.

                  * ``Fulfilled`` - The intent has fulfilled by the Lambda function associated with the
                  intent.

                  * ``ReadyForFulfillment`` - All of the information necessary for the intent is present
                  and the intent ready to be fulfilled by the client application.

                - **slotToElicit** *(string) --*

                  The next slot to elicit from the user. If there is not slot to elicit, the field is blank.

            - **sessionAttributes** *(dict) --*

              Map of key/value pairs representing the session-specific context information. It contains
              application information passed between Amazon Lex and a client application.

              - *(string) --*

                - *(string) --*

            - **sessionId** *(string) --*

              A unique identifier for the session.

            - **dialogAction** *(dict) --*

              Describes the current state of the bot.

              - **type** *(string) --*

                The next action that the bot should take in its interaction with the user. The possible
                values are:

                * ``ConfirmIntent`` - The next action is asking the user if the intent is complete and
                ready to be fulfilled. This is a yes/no question such as "Place the order?"

                * ``Close`` - Indicates that the there will not be a response from the user. For example,
                the statement "Your order has been placed" does not require a response.

                * ``Delegate`` - The next action is determined by Amazon Lex.

                * ``ElicitIntent`` - The next action is to determine the intent that the user wants to
                fulfill.

                * ``ElicitSlot`` - The next action is to elicit a slot value from the user.

              - **intentName** *(string) --*

                The name of the intent.

              - **slots** *(dict) --*

                Map of the slots that have been gathered and their values.

                - *(string) --*

                  - *(string) --*

              - **slotToElicit** *(string) --*

                The name of the slot that should be elicited from the user.

              - **fulfillmentState** *(string) --*

                The fulfillment state of the intent. The possible values are:

                * ``Failed`` - The Lambda function associated with the intent failed to fulfill the intent.

                * ``Fulfilled`` - The intent has fulfilled by the Lambda function associated with the
                intent.

                * ``ReadyForFulfillment`` - All of the information necessary for the intent is present and
                the intent ready to be fulfilled by the client application.

              - **message** *(string) --*

                The message that should be shown to the user. If you don't specify a message, Amazon Lex
                will use the message configured for the intent.

              - **messageFormat** *(string) --*

                * ``PlainText`` - The message contains plain UTF-8 text.

                * ``CustomPayload`` - The message is a custom format for the client.

                * ``SSML`` - The message contains text formatted for voice output.

                * ``Composite`` - The message contains an escaped JSON object containing one or more
                messages. For more information, see `Message Groups
                <https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html>`__ .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_content(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        contentType: str,
        inputStream: Union[bytes, IO],
        sessionAttributes: str = None,
        requestAttributes: str = None,
        accept: str = None,
    ) -> ClientPostContentResponseTypeDef:
        """
        Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio
        requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning
        model that it built for the bot.

        The ``PostContent`` operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to
        achieve higher speech recognition accuracy in telephone audio applications.

        In response, Amazon Lex returns the next message to convey to the user. Consider the following
        example messages:

        * For a user input "I would like a pizza," Amazon Lex might return a response with a message
        eliciting slot data (for example, ``PizzaSize`` ): "What size pizza would you like?".

        * After the user provides all of the pizza order information, Amazon Lex might return a response
        with a message to get user confirmation: "Order the pizza?".

        * After the user replies "Yes" to the confirmation prompt, Amazon Lex might return a conclusion
        statement: "Thank you, your cheese pizza has been ordered.".

        Not all Amazon Lex messages require a response from the user. For example, conclusion statements do
        not require a response. Some messages require only a yes or no response. In addition to the
        ``message`` , Amazon Lex provides additional context about the message in the response that you can
        use to enhance client behavior, such as displaying the appropriate client user interface. Consider
        the following examples:

        * If the message is to elicit slot data, Amazon Lex returns the following context information:

          * ``x-amz-lex-dialog-state`` header set to ``ElicitSlot``

          * ``x-amz-lex-intent-name`` header set to the intent name in the current context

          * ``x-amz-lex-slot-to-elicit`` header set to the slot name for which the ``message`` is eliciting
          information

          * ``x-amz-lex-slots`` header set to a map of slots configured for the intent with their current
          values

        * If the message is a confirmation prompt, the ``x-amz-lex-dialog-state`` header is set to
        ``Confirmation`` and the ``x-amz-lex-slot-to-elicit`` header is omitted.

        * If the message is a clarification prompt configured for the intent, indicating that the user
        intent is not understood, the ``x-amz-dialog-state`` header is set to ``ElicitIntent`` and the
        ``x-amz-slot-to-elicit`` header is omitted.

        In addition, Amazon Lex also returns your application-specific ``sessionAttributes`` . For more
        information, see `Managing Conversation Context
        <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PostContent>`_

        **Request Syntax**
        ::

          response = client.post_content(
              botName='string',
              botAlias='string',
              userId='string',
              sessionAttributes={...}|[...]|123|123.4|'string'|True|None,
              requestAttributes={...}|[...]|123|123.4|'string'|True|None,
              contentType='string',
              accept='string',
              inputStream=b'bytes'|file
          )
        :type botName: string
        :param botName: **[REQUIRED]**

          Name of the Amazon Lex bot.

        :type botAlias: string
        :param botAlias: **[REQUIRED]**

          Alias of the Amazon Lex bot.

        :type userId: string
        :param userId: **[REQUIRED]**

          The ID of the client application user. Amazon Lex uses this to identify a user's conversation
          with your bot. At runtime, each request must contain the ``userID`` field.

          To decide the user ID to use for your application, consider the following factors.

          * The ``userID`` field must not contain any personally identifiable information of the user, for
          example, name, personal identification numbers, or other end user personal information.

          * If you want a user to start a conversation on one device and continue on another device, use a
          user-specific identifier.

          * If you want the same user to be able to have two independent conversations on two different
          devices, choose a device-specific identifier.

          * A user can't have two independent conversations with two different versions of the same bot.
          For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If
          you anticipate that a user will need to have conversation with two different versions, for
          example, while testing, include the bot alias in the user ID to separate the two conversations.

        :type sessionAttributes: JSON serializable
        :param sessionAttributes:

          You pass this value as the ``x-amz-lex-session-attributes`` HTTP header.

          Application-specific information passed between Amazon Lex and a client application. The value
          must be a JSON serialized and base64 encoded map with string keys and values. The total size of
          the ``sessionAttributes`` and ``requestAttributes`` headers is limited to 12 KB.

          For more information, see `Setting Session Attributes
          <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs>`__ .

        :type requestAttributes: JSON serializable
        :param requestAttributes:

          You pass this value as the ``x-amz-lex-request-attributes`` HTTP header.

          Request-specific information passed between Amazon Lex and a client application. The value must
          be a JSON serialized and base64 encoded map with string keys and values. The total size of the
          ``requestAttributes`` and ``sessionAttributes`` headers is limited to 12 KB.

          The namespace ``x-amz-lex:`` is reserved for special attributes. Don't create any request
          attributes with the prefix ``x-amz-lex:`` .

          For more information, see `Setting Request Attributes
          <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs>`__ .

        :type contentType: string
        :param contentType: **[REQUIRED]**

          You pass this value as the ``Content-Type`` HTTP header.

          Indicates the audio format or text. The header value must start with one of the following
          prefixes:

          * PCM format, audio data must be in little-endian byte order.

            * audio/l16; rate=16000; channels=1

            * audio/x-l16; sample-rate=16000; channel-count=1

            * audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false

          * Opus format

            * audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4

          * Text format

            * text/plain; charset=utf-8

        :type accept: string
        :param accept:

          You pass this value as the ``Accept`` HTTP header.

          The message Amazon Lex returns in the response can be either text or speech based on the
          ``Accept`` HTTP header value in the request.

          * If the value is ``text/plain; charset=utf-8`` , Amazon Lex returns text in the response.

          * If the value begins with ``audio/`` , Amazon Lex returns speech in the response. Amazon Lex
          uses Amazon Polly to generate the speech (using the configuration you specified in the ``Accept``
          header). For example, if you specify ``audio/mpeg`` as the value, Amazon Lex returns speech in
          the MPEG format.

          * If the value is ``audio/pcm`` , the speech returned is ``audio/pcm`` in 16-bit, little endian
          format.

          * The following are the accepted values:

            * audio/mpeg

            * audio/ogg

            * audio/pcm

            * text/plain; charset=utf-8

            * audio/* (defaults to mpeg)

        :type inputStream: bytes or seekable file-like object
        :param inputStream: **[REQUIRED]**

          User input in PCM or Opus audio format or text format as described in the ``Content-Type`` HTTP
          header.

          You can stream audio data to Amazon Lex or you can create a local buffer that captures all of the
          audio data before sending. In general, you get better performance if you stream audio data rather
          than buffering the data locally.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contentType': 'string',
                'intentName': 'string',
                'slots': {...}|[...]|123|123.4|'string'|True|None,
                'sessionAttributes': {...}|[...]|123|123.4|'string'|True|None,
                'message': 'string',
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState':
                'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'inputTranscript': 'string',
                'audioStream': StreamingBody()
            }
          **Response Structure**

          - *(dict) --*

            - **contentType** *(string) --*

              Content type as specified in the ``Accept`` HTTP header in the request.

            - **intentName** *(string) --*

              Current user intent that Amazon Lex is aware of.

            - **slots** (JSON serializable) --

              Map of zero or more intent slots (name/value pairs) Amazon Lex detected from the user input
              during the conversation. The field is base-64 encoded.

              Amazon Lex creates a resolution list containing likely values for a slot. The value that it
              returns is determined by the ``valueSelectionStrategy`` selected when the slot type was
              created or updated. If ``valueSelectionStrategy`` is set to ``ORIGINAL_VALUE`` , the value
              provided by the user is returned, if the user value is similar to the slot values. If
              ``valueSelectionStrategy`` is set to ``TOP_RESOLUTION`` Amazon Lex returns the first value in
              the resolution list or, if there is no resolution list, null. If you don't specify a
              ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

            - **sessionAttributes** (JSON serializable) --

              Map of key/value pairs representing the session-specific context information.

            - **message** *(string) --*

              The message to convey to the user. The message can come from the bot's configuration or from
              a Lambda function.

              If the intent is not configured with a Lambda function, or if the Lambda function returned
              ``Delegate`` as the ``dialogAction.type`` in its response, Amazon Lex decides on the next
              course of action and selects an appropriate message from the bot's configuration based on the
              current interaction context. For example, if Amazon Lex isn't able to understand user input,
              it uses a clarification prompt message.

              When you create an intent you can assign messages to groups. When messages are assigned to
              groups Amazon Lex returns one message from each group in the response. The message field is
              an escaped JSON string containing the messages. For more information about the structure of
              the JSON string returned, see  msg-prompts-formats .

              If the Lambda function returns a message, Amazon Lex passes it to the client in its response.

            - **messageFormat** *(string) --*

              The format of the response message. One of the following values:

              * ``PlainText`` - The message contains plain UTF-8 text.

              * ``CustomPayload`` - The message is a custom format for the client.

              * ``SSML`` - The message contains text formatted for voice output.

              * ``Composite`` - The message contains an escaped JSON object containing one or more messages
              from the groups that messages were assigned to when the intent was created.

            - **dialogState** *(string) --*

              Identifies the current state of the user interaction. Amazon Lex returns one of the following
              values as ``dialogState`` . The client can optionally use this information to customize the
              user interface.

              * ``ElicitIntent`` - Amazon Lex wants to elicit the user's intent. Consider the following
              examples:  For example, a user might utter an intent ("I want to order a pizza"). If Amazon
              Lex cannot infer the user intent from this utterance, it will return this dialog state.

              * ``ConfirmIntent`` - Amazon Lex is expecting a "yes" or "no" response.  For example, Amazon
              Lex wants user confirmation before fulfilling an intent. Instead of a simple "yes" or "no"
              response, a user might respond with additional information. For example, "yes, but make it a
              thick crust pizza" or "no, I want to order a drink." Amazon Lex can process such additional
              information (in these examples, update the crust type slot or change the intent from
              OrderPizza to OrderDrink).

              * ``ElicitSlot`` - Amazon Lex is expecting the value of a slot for the current intent.  For
              example, suppose that in the response Amazon Lex sends this message: "What size pizza would
              you like?". A user might reply with the slot value (e.g., "medium"). The user might also
              provide additional information in the response (e.g., "medium thick crust pizza"). Amazon Lex
              can process such additional information appropriately.

              * ``Fulfilled`` - Conveys that the Lambda function has successfully fulfilled the intent.

              * ``ReadyForFulfillment`` - Conveys that the client has to fulfill the request.

              * ``Failed`` - Conveys that the conversation with the user failed.  This can happen for
              various reasons, including that the user does not provide an appropriate response to prompts
              from the service (you can configure how many times Amazon Lex can prompt a user for specific
              information), or if the Lambda function fails to fulfill the intent.

            - **slotToElicit** *(string) --*

              If the ``dialogState`` value is ``ElicitSlot`` , returns the name of the slot for which
              Amazon Lex is eliciting a value.

            - **inputTranscript** *(string) --*

              The text used to process the request.

              If the input was an audio stream, the ``inputTranscript`` field contains the text extracted
              from the audio stream. This is the text that is actually processed to recognize intents and
              slot values. You can use this information to determine if Amazon Lex is correctly processing
              the audio that you send.

            - **audioStream** (:class:`.StreamingBody`) --

              The prompt (or statement) to convey to the user. This is based on the bot configuration and
              context. For example, if Amazon Lex did not understand the user intent, it sends the
              ``clarificationPrompt`` configured for the bot. If the intent requires confirmation before
              taking the fulfillment action, it sends the ``confirmationPrompt`` . Another example: Suppose
              that the Lambda function successfully fulfilled the intent, and sent a message to convey to
              the user. Then Amazon Lex sends that message in the response.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_text(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        inputText: str,
        sessionAttributes: Dict[str, str] = None,
        requestAttributes: Dict[str, str] = None,
    ) -> ClientPostTextResponseTypeDef:
        """
        Sends user input to Amazon Lex. Client applications can use this API to send requests to Amazon Lex
        at runtime. Amazon Lex then interprets the user input using the machine learning model it built for
        the bot.

        In response, Amazon Lex returns the next ``message`` to convey to the user an optional
        ``responseCard`` to display. Consider the following example messages:

        * For a user input "I would like a pizza", Amazon Lex might return a response with a message
        eliciting slot data (for example, PizzaSize): "What size pizza would you like?"

        * After the user provides all of the pizza order information, Amazon Lex might return a response
        with a message to obtain user confirmation "Proceed with the pizza order?".

        * After the user replies to a confirmation prompt with a "yes", Amazon Lex might return a
        conclusion statement: "Thank you, your cheese pizza has been ordered.".

        Not all Amazon Lex messages require a user response. For example, a conclusion statement does not
        require a response. Some messages require only a "yes" or "no" user response. In addition to the
        ``message`` , Amazon Lex provides additional context about the message in the response that you
        might use to enhance client behavior, for example, to display the appropriate client user
        interface. These are the ``slotToElicit`` , ``dialogState`` , ``intentName`` , and ``slots`` fields
        in the response. Consider the following examples:

        * If the message is to elicit slot data, Amazon Lex returns the following context information:

          * ``dialogState`` set to ElicitSlot

          * ``intentName`` set to the intent name in the current context

          * ``slotToElicit`` set to the slot name for which the ``message`` is eliciting information

          * ``slots`` set to a map of slots, configured for the intent, with currently known values

        * If the message is a confirmation prompt, the ``dialogState`` is set to ConfirmIntent and
        ``SlotToElicit`` is set to null.

        * If the message is a clarification prompt (configured for the intent) that indicates that user
        intent is not understood, the ``dialogState`` is set to ElicitIntent and ``slotToElicit`` is set to
        null.

        In addition, Amazon Lex also returns your application-specific ``sessionAttributes`` . For more
        information, see `Managing Conversation Context
        <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PostText>`_

        **Request Syntax**
        ::

          response = client.post_text(
              botName='string',
              botAlias='string',
              userId='string',
              sessionAttributes={
                  'string': 'string'
              },
              requestAttributes={
                  'string': 'string'
              },
              inputText='string'
          )
        :type botName: string
        :param botName: **[REQUIRED]**

          The name of the Amazon Lex bot.

        :type botAlias: string
        :param botAlias: **[REQUIRED]**

          The alias of the Amazon Lex bot.

        :type userId: string
        :param userId: **[REQUIRED]**

          The ID of the client application user. Amazon Lex uses this to identify a user's conversation
          with your bot. At runtime, each request must contain the ``userID`` field.

          To decide the user ID to use for your application, consider the following factors.

          * The ``userID`` field must not contain any personally identifiable information of the user, for
          example, name, personal identification numbers, or other end user personal information.

          * If you want a user to start a conversation on one device and continue on another device, use a
          user-specific identifier.

          * If you want the same user to be able to have two independent conversations on two different
          devices, choose a device-specific identifier.

          * A user can't have two independent conversations with two different versions of the same bot.
          For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If
          you anticipate that a user will need to have conversation with two different versions, for
          example, while testing, include the bot alias in the user ID to separate the two conversations.

        :type sessionAttributes: dict
        :param sessionAttributes:

          Application-specific information passed between Amazon Lex and a client application.

          For more information, see `Setting Session Attributes
          <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs>`__ .

          - *(string) --*

            - *(string) --*

        :type requestAttributes: dict
        :param requestAttributes:

          Request-specific information passed between Amazon Lex and a client application.

          The namespace ``x-amz-lex:`` is reserved for special attributes. Don't create any request
          attributes with the prefix ``x-amz-lex:`` .

          For more information, see `Setting Request Attributes
          <https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs>`__ .

          - *(string) --*

            - *(string) --*

        :type inputText: string
        :param inputText: **[REQUIRED]**

          The text that the user entered (Amazon Lex interprets this text).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'intentName': 'string',
                'slots': {
                    'string': 'string'
                },
                'sessionAttributes': {
                    'string': 'string'
                },
                'message': 'string',
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState':
                'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'responseCard': {
                    'version': 'string',
                    'contentType': 'application/vnd.amazonaws.card.generic',
                    'genericAttachments': [
                        {
                            'title': 'string',
                            'subTitle': 'string',
                            'attachmentLinkUrl': 'string',
                            'imageUrl': 'string',
                            'buttons': [
                                {
                                    'text': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **intentName** *(string) --*

              The current user intent that Amazon Lex is aware of.

            - **slots** *(dict) --*

              The intent slots that Amazon Lex detected from the user input in the conversation.

              Amazon Lex creates a resolution list containing likely values for a slot. The value that it
              returns is determined by the ``valueSelectionStrategy`` selected when the slot type was
              created or updated. If ``valueSelectionStrategy`` is set to ``ORIGINAL_VALUE`` , the value
              provided by the user is returned, if the user value is similar to the slot values. If
              ``valueSelectionStrategy`` is set to ``TOP_RESOLUTION`` Amazon Lex returns the first value in
              the resolution list or, if there is no resolution list, null. If you don't specify a
              ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

              - *(string) --*

                - *(string) --*

            - **sessionAttributes** *(dict) --*

              A map of key-value pairs representing the session-specific context information.

              - *(string) --*

                - *(string) --*

            - **message** *(string) --*

              The message to convey to the user. The message can come from the bot's configuration or from
              a Lambda function.

              If the intent is not configured with a Lambda function, or if the Lambda function returned
              ``Delegate`` as the ``dialogAction.type`` its response, Amazon Lex decides on the next course
              of action and selects an appropriate message from the bot's configuration based on the
              current interaction context. For example, if Amazon Lex isn't able to understand user input,
              it uses a clarification prompt message.

              When you create an intent you can assign messages to groups. When messages are assigned to
              groups Amazon Lex returns one message from each group in the response. The message field is
              an escaped JSON string containing the messages. For more information about the structure of
              the JSON string returned, see  msg-prompts-formats .

              If the Lambda function returns a message, Amazon Lex passes it to the client in its response.

            - **messageFormat** *(string) --*

              The format of the response message. One of the following values:

              * ``PlainText`` - The message contains plain UTF-8 text.

              * ``CustomPayload`` - The message is a custom format defined by the Lambda function.

              * ``SSML`` - The message contains text formatted for voice output.

              * ``Composite`` - The message contains an escaped JSON object containing one or more messages
              from the groups that messages were assigned to when the intent was created.

            - **dialogState** *(string) --*

              Identifies the current state of the user interaction. Amazon Lex returns one of the following
              values as ``dialogState`` . The client can optionally use this information to customize the
              user interface.

              * ``ElicitIntent`` - Amazon Lex wants to elicit user intent.  For example, a user might utter
              an intent ("I want to order a pizza"). If Amazon Lex cannot infer the user intent from this
              utterance, it will return this dialogState.

              * ``ConfirmIntent`` - Amazon Lex is expecting a "yes" or "no" response.  For example, Amazon
              Lex wants user confirmation before fulfilling an intent.  Instead of a simple "yes" or "no,"
              a user might respond with additional information. For example, "yes, but make it thick crust
              pizza" or "no, I want to order a drink". Amazon Lex can process such additional information
              (in these examples, update the crust type slot value, or change intent from OrderPizza to
              OrderDrink).

              * ``ElicitSlot`` - Amazon Lex is expecting a slot value for the current intent.  For example,
              suppose that in the response Amazon Lex sends this message: "What size pizza would you
              like?". A user might reply with the slot value (e.g., "medium"). The user might also provide
              additional information in the response (e.g., "medium thick crust pizza"). Amazon Lex can
              process such additional information appropriately.

              * ``Fulfilled`` - Conveys that the Lambda function configured for the intent has successfully
              fulfilled the intent.

              * ``ReadyForFulfillment`` - Conveys that the client has to fulfill the intent.

              * ``Failed`` - Conveys that the conversation with the user failed.  This can happen for
              various reasons including that the user did not provide an appropriate response to prompts
              from the service (you can configure how many times Amazon Lex can prompt a user for specific
              information), or the Lambda function failed to fulfill the intent.

            - **slotToElicit** *(string) --*

              If the ``dialogState`` value is ``ElicitSlot`` , returns the name of the slot for which
              Amazon Lex is eliciting a value.

            - **responseCard** *(dict) --*

              Represents the options that the user has to respond to the current prompt. Response Card can
              come from the bot configuration (in the Amazon Lex console, choose the settings button next
              to a slot) or from a code hook (Lambda function).

              - **version** *(string) --*

                The version of the response card format.

              - **contentType** *(string) --*

                The content type of the response.

              - **genericAttachments** *(list) --*

                An array of attachment objects representing options.

                - *(dict) --*

                  Represents an option rendered to the user when a prompt is shown. It could be an image, a
                  button, a link, or text.

                  - **title** *(string) --*

                    The title of the option.

                  - **subTitle** *(string) --*

                    The subtitle shown below the title.

                  - **attachmentLinkUrl** *(string) --*

                    The URL of an attachment to the response card.

                  - **imageUrl** *(string) --*

                    The URL of an image that is displayed to the user.

                  - **buttons** *(list) --*

                    The list of options to show to the user.

                    - *(dict) --*

                      Represents an option to be shown on the client platform (Facebook, Slack, etc.)

                      - **text** *(string) --*

                        Text that is visible to the user on the button.

                      - **value** *(string) --*

                        The value sent to Amazon Lex when a user chooses the button. For example, consider
                        button text "NYC." When the user chooses the button, the value sent can be "New
                        York City."

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_session(
        self,
        botName: str,
        botAlias: str,
        userId: str,
        sessionAttributes: Dict[str, str] = None,
        dialogAction: ClientPutSessiondialogActionTypeDef = None,
        recentIntentSummaryView: List[
            ClientPutSessionrecentIntentSummaryViewTypeDef
        ] = None,
        accept: str = None,
    ) -> ClientPutSessionResponseTypeDef:
        """
        Creates a new session or modifies an existing session with an Amazon Lex bot. Use this operation to
        enable your application to set the state of the bot.

        For more information, see `Managing Sessions
        <https://docs.aws.amazon.com/lex/latest/dg/how-session-api.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/runtime.lex-2016-11-28/PutSession>`_

        **Request Syntax**
        ::

          response = client.put_session(
              botName='string',
              botAlias='string',
              userId='string',
              sessionAttributes={
                  'string': 'string'
              },
              dialogAction={
                  'type': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Close'|'Delegate',
                  'intentName': 'string',
                  'slots': {
                      'string': 'string'
                  },
                  'slotToElicit': 'string',
                  'fulfillmentState': 'Fulfilled'|'Failed'|'ReadyForFulfillment',
                  'message': 'string',
                  'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite'
              },
              recentIntentSummaryView=[
                  {
                      'intentName': 'string',
                      'checkpointLabel': 'string',
                      'slots': {
                          'string': 'string'
                      },
                      'confirmationStatus': 'None'|'Confirmed'|'Denied',
                      'dialogActionType': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Close'|'Delegate',
                      'fulfillmentState': 'Fulfilled'|'Failed'|'ReadyForFulfillment',
                      'slotToElicit': 'string'
                  },
              ],
              accept='string'
          )
        :type botName: string
        :param botName: **[REQUIRED]**

          The name of the bot that contains the session data.

        :type botAlias: string
        :param botAlias: **[REQUIRED]**

          The alias in use for the bot that contains the session data.

        :type userId: string
        :param userId: **[REQUIRED]**

          The ID of the client application user. Amazon Lex uses this to identify a user's conversation
          with your bot.

        :type sessionAttributes: dict
        :param sessionAttributes:

          Map of key/value pairs representing the session-specific context information. It contains
          application information passed between Amazon Lex and a client application.

          - *(string) --*

            - *(string) --*

        :type dialogAction: dict
        :param dialogAction:

          Sets the next action that the bot should take to fulfill the conversation.

          - **type** *(string) --* **[REQUIRED]**

            The next action that the bot should take in its interaction with the user. The possible values
            are:

            * ``ConfirmIntent`` - The next action is asking the user if the intent is complete and ready to
            be fulfilled. This is a yes/no question such as "Place the order?"

            * ``Close`` - Indicates that the there will not be a response from the user. For example, the
            statement "Your order has been placed" does not require a response.

            * ``Delegate`` - The next action is determined by Amazon Lex.

            * ``ElicitIntent`` - The next action is to determine the intent that the user wants to fulfill.

            * ``ElicitSlot`` - The next action is to elicit a slot value from the user.

          - **intentName** *(string) --*

            The name of the intent.

          - **slots** *(dict) --*

            Map of the slots that have been gathered and their values.

            - *(string) --*

              - *(string) --*

          - **slotToElicit** *(string) --*

            The name of the slot that should be elicited from the user.

          - **fulfillmentState** *(string) --*

            The fulfillment state of the intent. The possible values are:

            * ``Failed`` - The Lambda function associated with the intent failed to fulfill the intent.

            * ``Fulfilled`` - The intent has fulfilled by the Lambda function associated with the intent.

            * ``ReadyForFulfillment`` - All of the information necessary for the intent is present and the
            intent ready to be fulfilled by the client application.

          - **message** *(string) --*

            The message that should be shown to the user. If you don't specify a message, Amazon Lex will
            use the message configured for the intent.

          - **messageFormat** *(string) --*

            * ``PlainText`` - The message contains plain UTF-8 text.

            * ``CustomPayload`` - The message is a custom format for the client.

            * ``SSML`` - The message contains text formatted for voice output.

            * ``Composite`` - The message contains an escaped JSON object containing one or more messages.
            For more information, see `Message Groups
            <https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html>`__ .

        :type recentIntentSummaryView: list
        :param recentIntentSummaryView:

          A summary of the recent intents for the bot. You can use the intent summary view to set a
          checkpoint label on an intent and modify attributes of intents. You can also use it to remove or
          add intent summary objects to the list.

          An intent that you modify or add to the list must make sense for the bot. For example, the intent
          name must be valid for the bot. You must provide valid values for:

          * ``intentName``

          * slot names

          * ``slotToElict``

          If you send the ``recentIntentSummaryView`` parameter in a ``PutSession`` request, the contents
          of the new summary view replaces the old summary view. For example, if a ``GetSession`` request
          returns three intents in the summary view and you call ``PutSession`` with one intent in the
          summary view, the next call to ``GetSession`` will only return one intent.

          - *(dict) --*

            Provides information about the state of an intent. You can use this information to get the
            current state of an intent so that you can process the intent, or so that you can return the
            intent to its previous state.

            - **intentName** *(string) --*

              The name of the intent.

            - **checkpointLabel** *(string) --*

              A user-defined label that identifies a particular intent. You can use this label to return to
              a previous intent.

              Use the ``checkpointLabelFilter`` parameter of the ``GetSessionRequest`` operation to filter
              the intents returned by the operation to those with only the specified label.

            - **slots** *(dict) --*

              Map of the slots that have been gathered and their values.

              - *(string) --*

                - *(string) --*

            - **confirmationStatus** *(string) --*

              The status of the intent after the user responds to the confirmation prompt. If the user
              confirms the intent, Amazon Lex sets this field to ``Confirmed`` . If the user denies the
              intent, Amazon Lex sets this value to ``Denied`` . The possible values are:

              * ``Confirmed`` - The user has responded "Yes" to the confirmation prompt, confirming that
              the intent is complete and that it is ready to be fulfilled.

              * ``Denied`` - The user has responded "No" to the confirmation prompt.

              * ``None`` - The user has never been prompted for confirmation; or, the user was prompted but
              did not confirm or deny the prompt.

            - **dialogActionType** *(string) --* **[REQUIRED]**

              The next action that the bot should take in its interaction with the user. The possible
              values are:

              * ``ConfirmIntent`` - The next action is asking the user if the intent is complete and ready
              to be fulfilled. This is a yes/no question such as "Place the order?"

              * ``Close`` - Indicates that the there will not be a response from the user. For example, the
              statement "Your order has been placed" does not require a response.

              * ``ElicitIntent`` - The next action is to determine the intent that the user wants to
              fulfill.

              * ``ElicitSlot`` - The next action is to elicit a slot value from the user.

            - **fulfillmentState** *(string) --*

              The fulfillment state of the intent. The possible values are:

              * ``Failed`` - The Lambda function associated with the intent failed to fulfill the intent.

              * ``Fulfilled`` - The intent has fulfilled by the Lambda function associated with the intent.

              * ``ReadyForFulfillment`` - All of the information necessary for the intent is present and
              the intent ready to be fulfilled by the client application.

            - **slotToElicit** *(string) --*

              The next slot to elicit from the user. If there is not slot to elicit, the field is blank.

        :type accept: string
        :param accept:

          The message that Amazon Lex returns in the response can be either text or speech based depending
          on the value of this field.

          * If the value is ``text/plain; charset=utf-8`` , Amazon Lex returns text in the response.

          * If the value begins with ``audio/`` , Amazon Lex returns speech in the response. Amazon Lex
          uses Amazon Polly to generate the speech in the configuration that you specify. For example, if
          you specify ``audio/mpeg`` as the value, Amazon Lex returns speech in the MPEG format.

          * If the value is ``audio/pcm`` , the speech is returned as ``audio/pcm`` in 16-bit, little
          endian format.

          * The following are the accepted values:

            * ``audio/mpeg``

            * ``audio/ogg``

            * ``audio/pcm``

            * ``audio/*`` (defaults to mpeg)

            * ``text/plain; charset=utf-8``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contentType': 'string',
                'intentName': 'string',
                'slots': {...}|[...]|123|123.4|'string'|True|None,
                'sessionAttributes': {...}|[...]|123|123.4|'string'|True|None,
                'message': 'string',
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState':
                'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'audioStream': StreamingBody(),
                'sessionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **contentType** *(string) --*

              Content type as specified in the ``Accept`` HTTP header in the request.

            - **intentName** *(string) --*

              The name of the current intent.

            - **slots** (JSON serializable) --

              Map of zero or more intent slots Amazon Lex detected from the user input during the
              conversation.

              Amazon Lex creates a resolution list containing likely values for a slot. The value that it
              returns is determined by the ``valueSelectionStrategy`` selected when the slot type was
              created or updated. If ``valueSelectionStrategy`` is set to ``ORIGINAL_VALUE`` , the value
              provided by the user is returned, if the user value is similar to the slot values. If
              ``valueSelectionStrategy`` is set to ``TOP_RESOLUTION`` Amazon Lex returns the first value in
              the resolution list or, if there is no resolution list, null. If you don't specify a
              ``valueSelectionStrategy`` the default is ``ORIGINAL_VALUE`` .

            - **sessionAttributes** (JSON serializable) --

              Map of key/value pairs representing session-specific context information.

            - **message** *(string) --*

              The next message that should be presented to the user.

            - **messageFormat** *(string) --*

              The format of the response message. One of the following values:

              * ``PlainText`` - The message contains plain UTF-8 text.

              * ``CustomPayload`` - The message is a custom format for the client.

              * ``SSML`` - The message contains text formatted for voice output.

              * ``Composite`` - The message contains an escaped JSON object containing one or more messages
              from the groups that messages were assigned to when the intent was created.

            - **dialogState** *(string) --*

              * ``ConfirmIntent`` - Amazon Lex is expecting a "yes" or "no" response to confirm the intent
              before fulfilling an intent.

              * ``ElicitIntent`` - Amazon Lex wants to elicit the user's intent.

              * ``ElicitSlot`` - Amazon Lex is expecting the value of a slot for the current intent.

              * ``Failed`` - Conveys that the conversation with the user has failed. This can happen for
              various reasons, including the user does not provide an appropriate response to prompts from
              the service, or if the Lambda function fails to fulfill the intent.

              * ``Fulfilled`` - Conveys that the Lambda function has sucessfully fulfilled the intent.

              * ``ReadyForFulfillment`` - Conveys that the client has to fulfill the intent.

            - **slotToElicit** *(string) --*

              If the ``dialogState`` is ``ElicitSlot`` , returns the name of the slot for which Amazon Lex
              is eliciting a value.

            - **audioStream** (:class:`.StreamingBody`) --

              The audio version of the message to convey to the user.

            - **sessionId** *(string) --*

              A unique identifier for the session.

        """


class Exceptions:
    BadGatewayException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    DependencyFailedException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LoopDetectedException: Boto3ClientError
    NotAcceptableException: Boto3ClientError
    NotFoundException: Boto3ClientError
    RequestTimeoutException: Boto3ClientError
    UnsupportedMediaTypeException: Boto3ClientError
