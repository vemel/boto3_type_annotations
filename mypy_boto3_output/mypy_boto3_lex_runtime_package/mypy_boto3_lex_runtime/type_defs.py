"Main interface for lex-runtime type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientDeleteSessionResponseTypeDef",
    "ClientGetSessionResponsedialogActionTypeDef",
    "ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    "ClientGetSessionResponseTypeDef",
    "ClientPostContentResponseTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    "ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    "ClientPostTextResponseresponseCardTypeDef",
    "ClientPostTextResponseTypeDef",
    "ClientPutSessionResponseTypeDef",
    "ClientPutSessiondialogActionTypeDef",
    "ClientPutSessionrecentIntentSummaryViewTypeDef",
)


_ClientDeleteSessionResponseTypeDef = TypedDict(
    "_ClientDeleteSessionResponseTypeDef",
    {"botName": str, "botAlias": str, "userId": str, "sessionId": str},
    total=False,
)


class ClientDeleteSessionResponseTypeDef(_ClientDeleteSessionResponseTypeDef):
    """
    Type definition for `ClientDeleteSession` `Response`

    - **botName** *(string) --*

      The name of the bot associated with the session data.

    - **botAlias** *(string) --*

      The alias in use for the bot associated with the session data.

    - **userId** *(string) --*

      The ID of the client application user.

    - **sessionId** *(string) --*

      The unique identifier for the session.
    """


_ClientGetSessionResponsedialogActionTypeDef = TypedDict(
    "_ClientGetSessionResponsedialogActionTypeDef",
    {
        "type": str,
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": str,
        "message": str,
        "messageFormat": str,
    },
    total=False,
)


class ClientGetSessionResponsedialogActionTypeDef(
    _ClientGetSessionResponsedialogActionTypeDef
):
    """
    Type definition for `ClientGetSessionResponse` `dialogAction`

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


_ClientGetSessionResponserecentIntentSummaryViewTypeDef = TypedDict(
    "_ClientGetSessionResponserecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": str,
        "dialogActionType": str,
        "fulfillmentState": str,
        "slotToElicit": str,
    },
    total=False,
)


class ClientGetSessionResponserecentIntentSummaryViewTypeDef(
    _ClientGetSessionResponserecentIntentSummaryViewTypeDef
):
    """
    Type definition for `ClientGetSessionResponse` `recentIntentSummaryView`

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
    """


_ClientGetSessionResponseTypeDef = TypedDict(
    "_ClientGetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[
            ClientGetSessionResponserecentIntentSummaryViewTypeDef
        ],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": ClientGetSessionResponsedialogActionTypeDef,
    },
    total=False,
)


class ClientGetSessionResponseTypeDef(_ClientGetSessionResponseTypeDef):
    """
    Type definition for `ClientGetSession` `Response`

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


_ClientPostContentResponseTypeDef = TypedDict(
    "_ClientPostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "message": str,
        "messageFormat": str,
        "dialogState": str,
        "slotToElicit": str,
        "inputTranscript": str,
    },
    total=False,
)


class ClientPostContentResponseTypeDef(_ClientPostContentResponseTypeDef):
    """
    Type definition for `ClientPostContent` `Response`

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


_ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef",
    {"text": str, "value": str},
    total=False,
)


class ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef(
    _ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef
):
    """
    Type definition for `ClientPostTextResponseresponseCardgenericAttachments` `buttons`

    Represents an option to be shown on the client platform (Facebook, Slack, etc.)

    - **text** *(string) --*

      Text that is visible to the user on the button.

    - **value** *(string) --*

      The value sent to Amazon Lex when a user chooses the button. For example, consider
      button text "NYC." When the user chooses the button, the value sent can be "New
      York City."
    """


_ClientPostTextResponseresponseCardgenericAttachmentsTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardgenericAttachmentsTypeDef",
    {
        "title": str,
        "subTitle": str,
        "attachmentLinkUrl": str,
        "imageUrl": str,
        "buttons": List[
            ClientPostTextResponseresponseCardgenericAttachmentsbuttonsTypeDef
        ],
    },
    total=False,
)


class ClientPostTextResponseresponseCardgenericAttachmentsTypeDef(
    _ClientPostTextResponseresponseCardgenericAttachmentsTypeDef
):
    """
    Type definition for `ClientPostTextResponseresponseCard` `genericAttachments`

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


_ClientPostTextResponseresponseCardTypeDef = TypedDict(
    "_ClientPostTextResponseresponseCardTypeDef",
    {
        "version": str,
        "contentType": str,
        "genericAttachments": List[
            ClientPostTextResponseresponseCardgenericAttachmentsTypeDef
        ],
    },
    total=False,
)


class ClientPostTextResponseresponseCardTypeDef(
    _ClientPostTextResponseresponseCardTypeDef
):
    """
    Type definition for `ClientPostTextResponse` `responseCard`

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


_ClientPostTextResponseTypeDef = TypedDict(
    "_ClientPostTextResponseTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "messageFormat": str,
        "dialogState": str,
        "slotToElicit": str,
        "responseCard": ClientPostTextResponseresponseCardTypeDef,
    },
    total=False,
)


class ClientPostTextResponseTypeDef(_ClientPostTextResponseTypeDef):
    """
    Type definition for `ClientPostText` `Response`

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


_ClientPutSessionResponseTypeDef = TypedDict(
    "_ClientPutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "message": str,
        "messageFormat": str,
        "dialogState": str,
        "slotToElicit": str,
        "sessionId": str,
    },
    total=False,
)


class ClientPutSessionResponseTypeDef(_ClientPutSessionResponseTypeDef):
    """
    Type definition for `ClientPutSession` `Response`

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


_RequiredClientPutSessiondialogActionTypeDef = TypedDict(
    "_RequiredClientPutSessiondialogActionTypeDef", {"type": str}
)
_OptionalClientPutSessiondialogActionTypeDef = TypedDict(
    "_OptionalClientPutSessiondialogActionTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": str,
        "message": str,
        "messageFormat": str,
    },
    total=False,
)


class ClientPutSessiondialogActionTypeDef(
    _RequiredClientPutSessiondialogActionTypeDef,
    _OptionalClientPutSessiondialogActionTypeDef,
):
    """
    Type definition for `ClientPutSession` `dialogAction`

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
    """


_RequiredClientPutSessionrecentIntentSummaryViewTypeDef = TypedDict(
    "_RequiredClientPutSessionrecentIntentSummaryViewTypeDef", {"dialogActionType": str}
)
_OptionalClientPutSessionrecentIntentSummaryViewTypeDef = TypedDict(
    "_OptionalClientPutSessionrecentIntentSummaryViewTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": str,
        "fulfillmentState": str,
        "slotToElicit": str,
    },
    total=False,
)


class ClientPutSessionrecentIntentSummaryViewTypeDef(
    _RequiredClientPutSessionrecentIntentSummaryViewTypeDef,
    _OptionalClientPutSessionrecentIntentSummaryViewTypeDef,
):
    """
    Type definition for `ClientPutSession` `recentIntentSummaryView`

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
    """
