"Main interface for lex-models type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    "ClientCreateBotVersionResponseabortStatementTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    "ClientCreateBotVersionResponseclarificationPromptTypeDef",
    "ClientCreateBotVersionResponseintentsTypeDef",
    "ClientCreateBotVersionResponseTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    "ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    "ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    "ClientCreateIntentVersionResponserejectionStatementTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    "ClientCreateIntentVersionResponseslotsTypeDef",
    "ClientCreateIntentVersionResponseTypeDef",
    "ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    "ClientCreateSlotTypeVersionResponseTypeDef",
    "ClientGetBotAliasResponseTypeDef",
    "ClientGetBotAliasesResponseBotAliasesTypeDef",
    "ClientGetBotAliasesResponseTypeDef",
    "ClientGetBotChannelAssociationResponseTypeDef",
    "ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    "ClientGetBotChannelAssociationsResponseTypeDef",
    "ClientGetBotResponseabortStatementmessagesTypeDef",
    "ClientGetBotResponseabortStatementTypeDef",
    "ClientGetBotResponseclarificationPromptmessagesTypeDef",
    "ClientGetBotResponseclarificationPromptTypeDef",
    "ClientGetBotResponseintentsTypeDef",
    "ClientGetBotResponseTypeDef",
    "ClientGetBotVersionsResponsebotsTypeDef",
    "ClientGetBotVersionsResponseTypeDef",
    "ClientGetBotsResponsebotsTypeDef",
    "ClientGetBotsResponseTypeDef",
    "ClientGetBuiltinIntentResponseslotsTypeDef",
    "ClientGetBuiltinIntentResponseTypeDef",
    "ClientGetBuiltinIntentsResponseintentsTypeDef",
    "ClientGetBuiltinIntentsResponseTypeDef",
    "ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    "ClientGetBuiltinSlotTypesResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetImportResponseTypeDef",
    "ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    "ClientGetIntentResponseconclusionStatementTypeDef",
    "ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientGetIntentResponseconfirmationPromptTypeDef",
    "ClientGetIntentResponsedialogCodeHookTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientGetIntentResponsefollowUpPromptTypeDef",
    "ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientGetIntentResponsefulfillmentActivityTypeDef",
    "ClientGetIntentResponserejectionStatementmessagesTypeDef",
    "ClientGetIntentResponserejectionStatementTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientGetIntentResponseslotsTypeDef",
    "ClientGetIntentResponseTypeDef",
    "ClientGetIntentVersionsResponseintentsTypeDef",
    "ClientGetIntentVersionsResponseTypeDef",
    "ClientGetIntentsResponseintentsTypeDef",
    "ClientGetIntentsResponseTypeDef",
    "ClientGetSlotTypeResponseenumerationValuesTypeDef",
    "ClientGetSlotTypeResponseTypeDef",
    "ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    "ClientGetSlotTypeVersionsResponseTypeDef",
    "ClientGetSlotTypesResponseslotTypesTypeDef",
    "ClientGetSlotTypesResponseTypeDef",
    "ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    "ClientGetUtterancesViewResponseutterancesTypeDef",
    "ClientGetUtterancesViewResponseTypeDef",
    "ClientPutBotAliasResponseTypeDef",
    "ClientPutBotResponseabortStatementmessagesTypeDef",
    "ClientPutBotResponseabortStatementTypeDef",
    "ClientPutBotResponseclarificationPromptmessagesTypeDef",
    "ClientPutBotResponseclarificationPromptTypeDef",
    "ClientPutBotResponseintentsTypeDef",
    "ClientPutBotResponseTypeDef",
    "ClientPutBotabortStatementmessagesTypeDef",
    "ClientPutBotabortStatementTypeDef",
    "ClientPutBotclarificationPromptmessagesTypeDef",
    "ClientPutBotclarificationPromptTypeDef",
    "ClientPutBotintentsTypeDef",
    "ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    "ClientPutIntentResponseconclusionStatementTypeDef",
    "ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    "ClientPutIntentResponseconfirmationPromptTypeDef",
    "ClientPutIntentResponsedialogCodeHookTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentResponsefollowUpPromptTypeDef",
    "ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentResponsefulfillmentActivityTypeDef",
    "ClientPutIntentResponserejectionStatementmessagesTypeDef",
    "ClientPutIntentResponserejectionStatementTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    "ClientPutIntentResponseslotsTypeDef",
    "ClientPutIntentResponseTypeDef",
    "ClientPutIntentconclusionStatementmessagesTypeDef",
    "ClientPutIntentconclusionStatementTypeDef",
    "ClientPutIntentconfirmationPromptmessagesTypeDef",
    "ClientPutIntentconfirmationPromptTypeDef",
    "ClientPutIntentdialogCodeHookTypeDef",
    "ClientPutIntentfollowUpPromptpromptmessagesTypeDef",
    "ClientPutIntentfollowUpPromptpromptTypeDef",
    "ClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef",
    "ClientPutIntentfollowUpPromptrejectionStatementTypeDef",
    "ClientPutIntentfollowUpPromptTypeDef",
    "ClientPutIntentfulfillmentActivitycodeHookTypeDef",
    "ClientPutIntentfulfillmentActivityTypeDef",
    "ClientPutIntentrejectionStatementmessagesTypeDef",
    "ClientPutIntentrejectionStatementTypeDef",
    "ClientPutIntentslotsvalueElicitationPromptmessagesTypeDef",
    "ClientPutIntentslotsvalueElicitationPromptTypeDef",
    "ClientPutIntentslotsTypeDef",
    "ClientPutSlotTypeResponseenumerationValuesTypeDef",
    "ClientPutSlotTypeResponseTypeDef",
    "ClientPutSlotTypeenumerationValuesTypeDef",
    "ClientStartImportResponseTypeDef",
    "GetBotAliasesPaginatePaginationConfigTypeDef",
    "GetBotAliasesPaginateResponseBotAliasesTypeDef",
    "GetBotAliasesPaginateResponseTypeDef",
    "GetBotChannelAssociationsPaginatePaginationConfigTypeDef",
    "GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef",
    "GetBotChannelAssociationsPaginateResponseTypeDef",
    "GetBotVersionsPaginatePaginationConfigTypeDef",
    "GetBotVersionsPaginateResponsebotsTypeDef",
    "GetBotVersionsPaginateResponseTypeDef",
    "GetBotsPaginatePaginationConfigTypeDef",
    "GetBotsPaginateResponsebotsTypeDef",
    "GetBotsPaginateResponseTypeDef",
    "GetBuiltinIntentsPaginatePaginationConfigTypeDef",
    "GetBuiltinIntentsPaginateResponseintentsTypeDef",
    "GetBuiltinIntentsPaginateResponseTypeDef",
    "GetBuiltinSlotTypesPaginatePaginationConfigTypeDef",
    "GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef",
    "GetBuiltinSlotTypesPaginateResponseTypeDef",
    "GetIntentVersionsPaginatePaginationConfigTypeDef",
    "GetIntentVersionsPaginateResponseintentsTypeDef",
    "GetIntentVersionsPaginateResponseTypeDef",
    "GetIntentsPaginatePaginationConfigTypeDef",
    "GetIntentsPaginateResponseintentsTypeDef",
    "GetIntentsPaginateResponseTypeDef",
    "GetSlotTypeVersionsPaginatePaginationConfigTypeDef",
    "GetSlotTypeVersionsPaginateResponseslotTypesTypeDef",
    "GetSlotTypeVersionsPaginateResponseTypeDef",
    "GetSlotTypesPaginatePaginationConfigTypeDef",
    "GetSlotTypesPaginateResponseslotTypesTypeDef",
    "GetSlotTypesPaginateResponseTypeDef",
)


_ClientCreateBotVersionResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseabortStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateBotVersionResponseabortStatementmessagesTypeDef(
    _ClientCreateBotVersionResponseabortStatementmessagesTypeDef
):
    """
    Type definition for `ClientCreateBotVersionResponseabortStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateBotVersionResponseabortStatementTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseabortStatementTypeDef",
    {
        "messages": List[ClientCreateBotVersionResponseabortStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateBotVersionResponseabortStatementTypeDef(
    _ClientCreateBotVersionResponseabortStatementTypeDef
):
    """
    Type definition for `ClientCreateBotVersionResponse` `abortStatement`

    The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef(
    _ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef
):
    """
    Type definition for `ClientCreateBotVersionResponseclarificationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateBotVersionResponseclarificationPromptTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseclarificationPromptTypeDef",
    {
        "messages": List[
            ClientCreateBotVersionResponseclarificationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateBotVersionResponseclarificationPromptTypeDef(
    _ClientCreateBotVersionResponseclarificationPromptTypeDef
):
    """
    Type definition for `ClientCreateBotVersionResponse` `clarificationPrompt`

    The message that Amazon Lex uses when it doesn't understand the user's request. For more
    information, see  PutBot .

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientCreateBotVersionResponseintentsTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseintentsTypeDef",
    {"intentName": str, "intentVersion": str},
    total=False,
)


class ClientCreateBotVersionResponseintentsTypeDef(
    _ClientCreateBotVersionResponseintentsTypeDef
):
    """
    Type definition for `ClientCreateBotVersionResponse` `intents`

    Identifies the specific version of an intent.

    - **intentName** *(string) --*

      The name of the intent.

    - **intentVersion** *(string) --*

      The version of the intent.
    """


_ClientCreateBotVersionResponseTypeDef = TypedDict(
    "_ClientCreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientCreateBotVersionResponseintentsTypeDef],
        "clarificationPrompt": ClientCreateBotVersionResponseclarificationPromptTypeDef,
        "abortStatement": ClientCreateBotVersionResponseabortStatementTypeDef,
        "status": str,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": str,
        "childDirected": bool,
    },
    total=False,
)


class ClientCreateBotVersionResponseTypeDef(_ClientCreateBotVersionResponseTypeDef):
    """
    Type definition for `ClientCreateBotVersion` `Response`

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **intents** *(list) --*

      An array of ``Intent`` objects. For more information, see  PutBot .

      - *(dict) --*

        Identifies the specific version of an intent.

        - **intentName** *(string) --*

          The name of the intent.

        - **intentVersion** *(string) --*

          The version of the intent.

    - **clarificationPrompt** *(dict) --*

      The message that Amazon Lex uses when it doesn't understand the user's request. For more
      information, see  PutBot .

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **abortStatement** *(dict) --*

      The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **status** *(string) --*

      When you send a request to create or update a bot, Amazon Lex sets the ``status`` response
      element to ``BUILDING`` . After Amazon Lex builds the bot, it sets ``status`` to ``READY`` .
      If Amazon Lex can't build the bot, it sets ``status`` to ``FAILED`` . Amazon Lex returns the
      reason for the failure in the ``failureReason`` response element.

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to build the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date when the ``$LATEST`` version of this bot was updated.

    - **createdDate** *(datetime) --*

      The date when the bot version was created.

    - **idleSessionTTLInSeconds** *(integer) --*

      The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For
      more information, see  PutBot .

    - **voiceId** *(string) --*

      The Amazon Polly voice ID that Amazon Lex uses for voice interactions with the user.

    - **checksum** *(string) --*

      Checksum identifying the version of the bot that was created.

    - **version** *(string) --*

      The version of the bot.

    - **locale** *(string) --*

      Specifies the target locale for the bot.

    - **childDirected** *(boolean) --*

      For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to the
      Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the
      ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm
      that your use of Amazon Lex **is** related to a website, program, or other application that
      is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
      By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon
      Lex **is not** related to a website, program, or other application that is directed or
      targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not
      specify a default value for the ``childDirected`` field that does not accurately reflect
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

      If your use of Amazon Lex relates to a website, program, or other application that is
      directed in whole or in part, to children under age 13, you must obtain any required
      verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in
      connection with websites, programs, or other applications that are directed or targeted, in
      whole or in part, to children under age 13, see the `Amazon Lex FAQ.
      <https://aws.amazon.com/lex/faqs#data-security>`__
    """


_ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponseconclusionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponseconclusionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconclusionStatementTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponseconclusionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconclusionStatementTypeDef(
    _ClientCreateIntentVersionResponseconclusionStatementTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `conclusionStatement`

    After the Lambda function specified in the ``fulfillmentActivity`` field fulfills the intent,
    Amazon Lex conveys this statement to the user.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef(
    _ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponseconfirmationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseconfirmationPromptTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponseconfirmationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseconfirmationPromptTypeDef(
    _ClientCreateIntentVersionResponseconfirmationPromptTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `confirmationPrompt`

    If defined, the prompt that Amazon Lex uses to confirm the user's intent before fulfilling it.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientCreateIntentVersionResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientCreateIntentVersionResponsedialogCodeHookTypeDef(
    _ClientCreateIntentVersionResponsedialogCodeHookTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `dialogCodeHook`

    If defined, Amazon Lex invokes this Lambda function for each user input.

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponsefollowUpPromptprompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponsefollowUpPromptpromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponsefollowUpPrompt` `prompt`

    Prompts for information from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponsefollowUpPromptrejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponsefollowUpPrompt` `rejectionStatement`

    If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientCreateIntentVersionResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientCreateIntentVersionResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefollowUpPromptTypeDef(
    _ClientCreateIntentVersionResponsefollowUpPromptTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `followUpPrompt`

    If defined, Amazon Lex uses this prompt to solicit additional user activity after the intent
    is fulfilled.

    - **prompt** *(dict) --*

      Prompts for information from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.
    """


_ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef(
    _ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponsefulfillmentActivity` `codeHook`

    A description of the Lambda function that is run to fulfill the intent.

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientCreateIntentVersionResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponsefulfillmentActivityTypeDef",
    {
        "type": str,
        "codeHook": ClientCreateIntentVersionResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientCreateIntentVersionResponsefulfillmentActivityTypeDef(
    _ClientCreateIntentVersionResponsefulfillmentActivityTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `fulfillmentActivity`

    Describes how the intent is fulfilled.

    - **type** *(string) --*

      How the intent should be fulfilled, either by running a Lambda function or by returning the
      slot data to the client application.

    - **codeHook** *(dict) --*

      A description of the Lambda function that is run to fulfill the intent.

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .
    """


_ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef(
    _ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponserejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponserejectionStatementTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponserejectionStatementTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponserejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponserejectionStatementTypeDef(
    _ClientCreateIntentVersionResponserejectionStatementTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `rejectionStatement`

    If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponseslotsvalueElicitationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned
      to a message, Amazon Lex returns one message from each group in the response.
    """


_ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[
            ClientCreateIntentVersionResponseslotsvalueElicitationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef(
    _ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponseslots` `valueElicitationPrompt`

    The prompt that Amazon Lex uses to elicit the slot value from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned
          to a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientCreateIntentVersionResponseslotsTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientCreateIntentVersionResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseslotsTypeDef(
    _ClientCreateIntentVersionResponseslotsTypeDef
):
    """
    Type definition for `ClientCreateIntentVersionResponse` `slots`

    Identifies the version of a specific slot.

    - **name** *(string) --*

      The name of the slot.

    - **description** *(string) --*

      A description of the slot.

    - **slotConstraint** *(string) --*

      Specifies whether the slot is required or optional.

    - **slotType** *(string) --*

      The type of the slot, either a custom slot type that you defined or one of the built-in
      slot types.

    - **slotTypeVersion** *(string) --*

      The version of the slot type.

    - **valueElicitationPrompt** *(dict) --*

      The prompt that Amazon Lex uses to elicit the slot value from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned
            to a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **priority** *(integer) --*

      Directs Lex the order in which to elicit this slot value from the user. For example, if
      the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
      slot with priority 1.

      If multiple slots share the same priority, the order in which Lex elicits values is
      arbitrary.

    - **sampleUtterances** *(list) --*

      If you know a specific pattern with which users might respond to an Amazon Lex request
      for a slot value, you can provide those utterances to improve accuracy. This is optional.
      In most cases, Amazon Lex is capable of understanding user utterances.

      - *(string) --*

    - **responseCard** *(string) --*

      A set of possible responses for the slot type used by text-based clients. A user chooses
      an option from the response card, instead of using text to reply.
    """


_ClientCreateIntentVersionResponseTypeDef = TypedDict(
    "_ClientCreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientCreateIntentVersionResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientCreateIntentVersionResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientCreateIntentVersionResponserejectionStatementTypeDef,
        "followUpPrompt": ClientCreateIntentVersionResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientCreateIntentVersionResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientCreateIntentVersionResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientCreateIntentVersionResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)


class ClientCreateIntentVersionResponseTypeDef(
    _ClientCreateIntentVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateIntentVersion` `Response`

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **slots** *(list) --*

      An array of slot types that defines the information required to fulfill the intent.

      - *(dict) --*

        Identifies the version of a specific slot.

        - **name** *(string) --*

          The name of the slot.

        - **description** *(string) --*

          A description of the slot.

        - **slotConstraint** *(string) --*

          Specifies whether the slot is required or optional.

        - **slotType** *(string) --*

          The type of the slot, either a custom slot type that you defined or one of the built-in
          slot types.

        - **slotTypeVersion** *(string) --*

          The version of the slot type.

        - **valueElicitationPrompt** *(dict) --*

          The prompt that Amazon Lex uses to elicit the slot value from the user.

          - **messages** *(list) --*

            An array of objects, each of which provides a message string and its type. You can
            specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            - *(dict) --*

              The message object that provides the message text and its type.

              - **contentType** *(string) --*

                The content type of the message string.

              - **content** *(string) --*

                The text of the message.

              - **groupNumber** *(integer) --*

                Identifies the message group that the message belongs to. When a group is assigned
                to a message, Amazon Lex returns one message from each group in the response.

          - **maxAttempts** *(integer) --*

            The number of times to prompt the user for information.

          - **responseCard** *(string) --*

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
            response. It substitutes session attributes and slot values for placeholders in the
            response card. For more information, see  ex-resp-card .

        - **priority** *(integer) --*

          Directs Lex the order in which to elicit this slot value from the user. For example, if
          the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
          slot with priority 1.

          If multiple slots share the same priority, the order in which Lex elicits values is
          arbitrary.

        - **sampleUtterances** *(list) --*

          If you know a specific pattern with which users might respond to an Amazon Lex request
          for a slot value, you can provide those utterances to improve accuracy. This is optional.
          In most cases, Amazon Lex is capable of understanding user utterances.

          - *(string) --*

        - **responseCard** *(string) --*

          A set of possible responses for the slot type used by text-based clients. A user chooses
          an option from the response card, instead of using text to reply.

    - **sampleUtterances** *(list) --*

      An array of sample utterances configured for the intent.

      - *(string) --*

    - **confirmationPrompt** *(dict) --*

      If defined, the prompt that Amazon Lex uses to confirm the user's intent before fulfilling it.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **followUpPrompt** *(dict) --*

      If defined, Amazon Lex uses this prompt to solicit additional user activity after the intent
      is fulfilled.

      - **prompt** *(dict) --*

        Prompts for information from the user.

        - **messages** *(list) --*

          An array of objects, each of which provides a message string and its type. You can
          specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **maxAttempts** *(integer) --*

          The number of times to prompt the user for information.

        - **responseCard** *(string) --*

          A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
          response. It substitutes session attributes and slot values for placeholders in the
          response card. For more information, see  ex-resp-card .

      - **rejectionStatement** *(dict) --*

        If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
        responds with this statement to acknowledge that the intent was canceled.

        - **messages** *(list) --*

          A collection of message objects.

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **responseCard** *(string) --*

          At runtime, if the client is using the `PostText
          <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
          includes the response card in the response. It substitutes all of the session attributes
          and slot values for placeholders in the response card.

    - **conclusionStatement** *(dict) --*

      After the Lambda function specified in the ``fulfillmentActivity`` field fulfills the intent,
      Amazon Lex conveys this statement to the user.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **dialogCodeHook** *(dict) --*

      If defined, Amazon Lex invokes this Lambda function for each user input.

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .

    - **fulfillmentActivity** *(dict) --*

      Describes how the intent is fulfilled.

      - **type** *(string) --*

        How the intent should be fulfilled, either by running a Lambda function or by returning the
        slot data to the client application.

      - **codeHook** *(dict) --*

        A description of the Lambda function that is run to fulfill the intent.

        - **uri** *(string) --*

          The Amazon Resource Name (ARN) of the Lambda function.

        - **messageVersion** *(string) --*

          The version of the request-response that you want Amazon Lex to use to invoke your Lambda
          function. For more information, see  using-lambda .

    - **parentIntentSignature** *(string) --*

      A unique identifier for a built-in intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version number assigned to the new version of the intent.

    - **checksum** *(string) --*

      Checksum of the intent version created.
    """


_ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef = TypedDict(
    "_ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef(
    _ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef
):
    """
    Type definition for `ClientCreateSlotTypeVersionResponse` `enumerationValues`

    Each slot type can have a set of values. Each enumeration value represents a value the slot
    type can take.

    For example, a pizza ordering bot could have a slot type that specifies the type of crust
    that the pizza should have. The slot type could include the values

    * thick

    * thin

    * stuffed

    - **value** *(string) --*

      The value of the slot type.

    - **synonyms** *(list) --*

      Additional values related to the slot type value.

      - *(string) --*
    """


_ClientCreateSlotTypeVersionResponseTypeDef = TypedDict(
    "_ClientCreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[
            ClientCreateSlotTypeVersionResponseenumerationValuesTypeDef
        ],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": str,
    },
    total=False,
)


class ClientCreateSlotTypeVersionResponseTypeDef(
    _ClientCreateSlotTypeVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateSlotTypeVersion` `Response`

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **enumerationValues** *(list) --*

      A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

      - *(dict) --*

        Each slot type can have a set of values. Each enumeration value represents a value the slot
        type can take.

        For example, a pizza ordering bot could have a slot type that specifies the type of crust
        that the pizza should have. The slot type could include the values

        * thick

        * thin

        * stuffed

        - **value** *(string) --*

          The value of the slot type.

        - **synonyms** *(list) --*

          Additional values related to the slot type value.

          - *(string) --*

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date and
      last update date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version assigned to the new slot type version.

    - **checksum** *(string) --*

      Checksum of the ``$LATEST`` version of the slot type.

    - **valueSelectionStrategy** *(string) --*

      The strategy that Amazon Lex uses to determine the value of the slot. For more information,
      see  PutSlotType .
    """


_ClientGetBotAliasResponseTypeDef = TypedDict(
    "_ClientGetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientGetBotAliasResponseTypeDef(_ClientGetBotAliasResponseTypeDef):
    """
    Type definition for `ClientGetBotAlias` `Response`

    - **name** *(string) --*

      The name of the bot alias.

    - **description** *(string) --*

      A description of the bot alias.

    - **botVersion** *(string) --*

      The version of the bot that the alias points to.

    - **botName** *(string) --*

      The name of the bot that the alias points to.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot alias was updated. When you create a resource, the creation date and
      the last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot alias was created.

    - **checksum** *(string) --*

      Checksum of the bot alias.
    """


_ClientGetBotAliasesResponseBotAliasesTypeDef = TypedDict(
    "_ClientGetBotAliasesResponseBotAliasesTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientGetBotAliasesResponseBotAliasesTypeDef(
    _ClientGetBotAliasesResponseBotAliasesTypeDef
):
    """
    Type definition for `ClientGetBotAliasesResponse` `BotAliases`

    Provides information about a bot alias.

    - **name** *(string) --*

      The name of the bot alias.

    - **description** *(string) --*

      A description of the bot alias.

    - **botVersion** *(string) --*

      The version of the Amazon Lex bot to which the alias points.

    - **botName** *(string) --*

      The name of the bot to which the alias points.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot alias was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot alias was created.

    - **checksum** *(string) --*

      Checksum of the bot alias.
    """


_ClientGetBotAliasesResponseTypeDef = TypedDict(
    "_ClientGetBotAliasesResponseTypeDef",
    {
        "BotAliases": List[ClientGetBotAliasesResponseBotAliasesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetBotAliasesResponseTypeDef(_ClientGetBotAliasesResponseTypeDef):
    """
    Type definition for `ClientGetBotAliases` `Response`

    - **BotAliases** *(list) --*

      An array of ``BotAliasMetadata`` objects, each describing a bot alias.

      - *(dict) --*

        Provides information about a bot alias.

        - **name** *(string) --*

          The name of the bot alias.

        - **description** *(string) --*

          A description of the bot alias.

        - **botVersion** *(string) --*

          The version of the Amazon Lex bot to which the alias points.

        - **botName** *(string) --*

          The name of the bot to which the alias points.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot alias was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot alias was created.

        - **checksum** *(string) --*

          Checksum of the bot alias.

    - **nextToken** *(string) --*

      A pagination token for fetching next page of aliases. If the response to this call is
      truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of
      aliases, specify the pagination token in the next request.
    """


_ClientGetBotChannelAssociationResponseTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": str,
        "botConfiguration": Dict[str, str],
        "status": str,
        "failureReason": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationResponseTypeDef(
    _ClientGetBotChannelAssociationResponseTypeDef
):
    """
    Type definition for `ClientGetBotChannelAssociation` `Response`

    - **name** *(string) --*

      The name of the association between the bot and the channel.

    - **description** *(string) --*

      A description of the association between the bot and the channel.

    - **botAlias** *(string) --*

      An alias pointing to the specific version of the Amazon Lex bot to which this association is
      being made.

    - **botName** *(string) --*

      The name of the Amazon Lex bot.

    - **createdDate** *(datetime) --*

      The date that the association between the bot and the channel was created.

    - **type** *(string) --*

      The type of the messaging platform.

    - **botConfiguration** *(dict) --*

      Provides information that the messaging platform needs to communicate with the Amazon Lex bot.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the bot channel.

      * ``CREATED`` - The channel has been created and is ready for use.

      * ``IN_PROGRESS`` - Channel creation is in progress.

      * ``FAILED`` - There was an error creating the channel. For information about the reason for
      the failure, see the ``failureReason`` field.

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the
      association.
    """


_ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": str,
        "botConfiguration": Dict[str, str],
        "status": str,
        "failureReason": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef(
    _ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef
):
    """
    Type definition for `ClientGetBotChannelAssociationsResponse` `botChannelAssociations`

    Represents an association between an Amazon Lex bot and an external messaging platform.

    - **name** *(string) --*

      The name of the association between the bot and the channel.

    - **description** *(string) --*

      A text description of the association you are creating.

    - **botAlias** *(string) --*

      An alias pointing to the specific version of the Amazon Lex bot to which this association
      is being made.

    - **botName** *(string) --*

      The name of the Amazon Lex bot to which this association is being made.

      .. note::

        Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.

    - **createdDate** *(datetime) --*

      The date that the association between the Amazon Lex bot and the channel was created.

    - **type** *(string) --*

      Specifies the type of association by indicating the type of channel being established
      between the Amazon Lex bot and the external messaging platform.

    - **botConfiguration** *(dict) --*

      Provides information necessary to communicate with the messaging platform.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the bot channel.

      * ``CREATED`` - The channel has been created and is ready for use.

      * ``IN_PROGRESS`` - Channel creation is in progress.

      * ``FAILED`` - There was an error creating the channel. For information about the reason
      for the failure, see the ``failureReason`` field.

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the
      association.
    """


_ClientGetBotChannelAssociationsResponseTypeDef = TypedDict(
    "_ClientGetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List[
            ClientGetBotChannelAssociationsResponsebotChannelAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetBotChannelAssociationsResponseTypeDef(
    _ClientGetBotChannelAssociationsResponseTypeDef
):
    """
    Type definition for `ClientGetBotChannelAssociations` `Response`

    - **botChannelAssociations** *(list) --*

      An array of objects, one for each association, that provides information about the Amazon Lex
      bot and its association with the channel.

      - *(dict) --*

        Represents an association between an Amazon Lex bot and an external messaging platform.

        - **name** *(string) --*

          The name of the association between the bot and the channel.

        - **description** *(string) --*

          A text description of the association you are creating.

        - **botAlias** *(string) --*

          An alias pointing to the specific version of the Amazon Lex bot to which this association
          is being made.

        - **botName** *(string) --*

          The name of the Amazon Lex bot to which this association is being made.

          .. note::

            Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.

        - **createdDate** *(datetime) --*

          The date that the association between the Amazon Lex bot and the channel was created.

        - **type** *(string) --*

          Specifies the type of association by indicating the type of channel being established
          between the Amazon Lex bot and the external messaging platform.

        - **botConfiguration** *(dict) --*

          Provides information necessary to communicate with the messaging platform.

          - *(string) --*

            - *(string) --*

        - **status** *(string) --*

          The status of the bot channel.

          * ``CREATED`` - The channel has been created and is ready for use.

          * ``IN_PROGRESS`` - Channel creation is in progress.

          * ``FAILED`` - There was an error creating the channel. For information about the reason
          for the failure, see the ``failureReason`` field.

        - **failureReason** *(string) --*

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the
          association.

    - **nextToken** *(string) --*

      A pagination token that fetches the next page of associations. If the response to this call
      is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page
      of associations, specify the pagination token in the next request.
    """


_ClientGetBotResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientGetBotResponseabortStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetBotResponseabortStatementmessagesTypeDef(
    _ClientGetBotResponseabortStatementmessagesTypeDef
):
    """
    Type definition for `ClientGetBotResponseabortStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetBotResponseabortStatementTypeDef = TypedDict(
    "_ClientGetBotResponseabortStatementTypeDef",
    {
        "messages": List[ClientGetBotResponseabortStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetBotResponseabortStatementTypeDef(
    _ClientGetBotResponseabortStatementTypeDef
):
    """
    Type definition for `ClientGetBotResponse` `abortStatement`

    The message that Amazon Lex returns when the user elects to end the conversation without
    completing it. For more information, see  PutBot .

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientGetBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientGetBotResponseclarificationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetBotResponseclarificationPromptmessagesTypeDef(
    _ClientGetBotResponseclarificationPromptmessagesTypeDef
):
    """
    Type definition for `ClientGetBotResponseclarificationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetBotResponseclarificationPromptTypeDef = TypedDict(
    "_ClientGetBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientGetBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetBotResponseclarificationPromptTypeDef(
    _ClientGetBotResponseclarificationPromptTypeDef
):
    """
    Type definition for `ClientGetBotResponse` `clarificationPrompt`

    The message Amazon Lex uses when it doesn't understand the user's request. For more
    information, see  PutBot .

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientGetBotResponseintentsTypeDef = TypedDict(
    "_ClientGetBotResponseintentsTypeDef",
    {"intentName": str, "intentVersion": str},
    total=False,
)


class ClientGetBotResponseintentsTypeDef(_ClientGetBotResponseintentsTypeDef):
    """
    Type definition for `ClientGetBotResponse` `intents`

    Identifies the specific version of an intent.

    - **intentName** *(string) --*

      The name of the intent.

    - **intentVersion** *(string) --*

      The version of the intent.
    """


_ClientGetBotResponseTypeDef = TypedDict(
    "_ClientGetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientGetBotResponseintentsTypeDef],
        "clarificationPrompt": ClientGetBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientGetBotResponseabortStatementTypeDef,
        "status": str,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": str,
        "childDirected": bool,
    },
    total=False,
)


class ClientGetBotResponseTypeDef(_ClientGetBotResponseTypeDef):
    """
    Type definition for `ClientGetBot` `Response`

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **intents** *(list) --*

      An array of ``intent`` objects. For more information, see  PutBot .

      - *(dict) --*

        Identifies the specific version of an intent.

        - **intentName** *(string) --*

          The name of the intent.

        - **intentVersion** *(string) --*

          The version of the intent.

    - **clarificationPrompt** *(dict) --*

      The message Amazon Lex uses when it doesn't understand the user's request. For more
      information, see  PutBot .

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **abortStatement** *(dict) --*

      The message that Amazon Lex returns when the user elects to end the conversation without
      completing it. For more information, see  PutBot .

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **status** *(string) --*

      The status of the bot. If the bot is ready to run, the status is ``READY`` . If there was a
      problem with building the bot, the status is ``FAILED`` and the ``failureReason`` explains
      why the bot did not build. If the bot was saved but not built, the status is ``NOT BUILT`` .

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex explains why it failed to build the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a resource, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **idleSessionTTLInSeconds** *(integer) --*

      The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For
      more information, see  PutBot .

    - **voiceId** *(string) --*

      The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more
      information, see  PutBot .

    - **checksum** *(string) --*

      Checksum of the bot used to identify a specific revision of the bot's ``$LATEST`` version.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **locale** *(string) --*

      The target locale for the bot.

    - **childDirected** *(boolean) --*

      For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to the
      Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the
      ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm
      that your use of Amazon Lex **is** related to a website, program, or other application that
      is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
      By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon
      Lex **is not** related to a website, program, or other application that is directed or
      targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not
      specify a default value for the ``childDirected`` field that does not accurately reflect
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

      If your use of Amazon Lex relates to a website, program, or other application that is
      directed in whole or in part, to children under age 13, you must obtain any required
      verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in
      connection with websites, programs, or other applications that are directed or targeted, in
      whole or in part, to children under age 13, see the `Amazon Lex FAQ.
      <https://aws.amazon.com/lex/faqs#data-security>`__
    """


_ClientGetBotVersionsResponsebotsTypeDef = TypedDict(
    "_ClientGetBotVersionsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetBotVersionsResponsebotsTypeDef(_ClientGetBotVersionsResponsebotsTypeDef):
    """
    Type definition for `ClientGetBotVersionsResponse` `bots`

    Provides information about a bot. .

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **status** *(string) --*

      The status of the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a bot, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .
    """


_ClientGetBotVersionsResponseTypeDef = TypedDict(
    "_ClientGetBotVersionsResponseTypeDef",
    {"bots": List[ClientGetBotVersionsResponsebotsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBotVersionsResponseTypeDef(_ClientGetBotVersionsResponseTypeDef):
    """
    Type definition for `ClientGetBotVersions` `Response`

    - **bots** *(list) --*

      An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for
      the ``$LATEST`` version.

      - *(dict) --*

        Provides information about a bot. .

        - **name** *(string) --*

          The name of the bot.

        - **description** *(string) --*

          A description of the bot.

        - **status** *(string) --*

          The status of the bot.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot was updated. When you create a bot, the creation date and last
          updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot was created.

        - **version** *(string) --*

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **nextToken** *(string) --*

      A pagination token for fetching the next page of bot versions. If the response to this call
      is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page
      of versions, specify the pagination token in the next request.
    """


_ClientGetBotsResponsebotsTypeDef = TypedDict(
    "_ClientGetBotsResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetBotsResponsebotsTypeDef(_ClientGetBotsResponsebotsTypeDef):
    """
    Type definition for `ClientGetBotsResponse` `bots`

    Provides information about a bot. .

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **status** *(string) --*

      The status of the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a bot, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .
    """


_ClientGetBotsResponseTypeDef = TypedDict(
    "_ClientGetBotsResponseTypeDef",
    {"bots": List[ClientGetBotsResponsebotsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBotsResponseTypeDef(_ClientGetBotsResponseTypeDef):
    """
    Type definition for `ClientGetBots` `Response`

    - **bots** *(list) --*

      An array of ``botMetadata`` objects, with one entry for each bot.

      - *(dict) --*

        Provides information about a bot. .

        - **name** *(string) --*

          The name of the bot.

        - **description** *(string) --*

          A description of the bot.

        - **status** *(string) --*

          The status of the bot.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot was updated. When you create a bot, the creation date and last
          updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot was created.

        - **version** *(string) --*

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **nextToken** *(string) --*

      If the response is truncated, it includes a pagination token that you can specify in your
      next request to fetch the next page of bots.
    """


_ClientGetBuiltinIntentResponseslotsTypeDef = TypedDict(
    "_ClientGetBuiltinIntentResponseslotsTypeDef", {"name": str}, total=False
)


class ClientGetBuiltinIntentResponseslotsTypeDef(
    _ClientGetBuiltinIntentResponseslotsTypeDef
):
    """
    Type definition for `ClientGetBuiltinIntentResponse` `slots`

    Provides information about a slot used in a built-in intent.

    - **name** *(string) --*

      A list of the slots defined for the intent.
    """


_ClientGetBuiltinIntentResponseTypeDef = TypedDict(
    "_ClientGetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[str],
        "slots": List[ClientGetBuiltinIntentResponseslotsTypeDef],
    },
    total=False,
)


class ClientGetBuiltinIntentResponseTypeDef(_ClientGetBuiltinIntentResponseTypeDef):
    """
    Type definition for `ClientGetBuiltinIntent` `Response`

    - **signature** *(string) --*

      The unique identifier for a built-in intent.

    - **supportedLocales** *(list) --*

      A list of locales that the intent supports.

      - *(string) --*

    - **slots** *(list) --*

      An array of ``BuiltinIntentSlot`` objects, one entry for each slot type in the intent.

      - *(dict) --*

        Provides information about a slot used in a built-in intent.

        - **name** *(string) --*

          A list of the slots defined for the intent.
    """


_ClientGetBuiltinIntentsResponseintentsTypeDef = TypedDict(
    "_ClientGetBuiltinIntentsResponseintentsTypeDef",
    {"signature": str, "supportedLocales": List[str]},
    total=False,
)


class ClientGetBuiltinIntentsResponseintentsTypeDef(
    _ClientGetBuiltinIntentsResponseintentsTypeDef
):
    """
    Type definition for `ClientGetBuiltinIntentsResponse` `intents`

    Provides metadata for a built-in intent.

    - **signature** *(string) --*

      A unique identifier for the built-in intent. To find the signature for an intent, see
      `Standard Built-in Intents
      <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
      in the *Alexa Skills Kit* .

    - **supportedLocales** *(list) --*

      A list of identifiers for the locales that the intent supports.

      - *(string) --*
    """


_ClientGetBuiltinIntentsResponseTypeDef = TypedDict(
    "_ClientGetBuiltinIntentsResponseTypeDef",
    {"intents": List[ClientGetBuiltinIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetBuiltinIntentsResponseTypeDef(_ClientGetBuiltinIntentsResponseTypeDef):
    """
    Type definition for `ClientGetBuiltinIntents` `Response`

    - **intents** *(list) --*

      An array of ``builtinIntentMetadata`` objects, one for each intent in the response.

      - *(dict) --*

        Provides metadata for a built-in intent.

        - **signature** *(string) --*

          A unique identifier for the built-in intent. To find the signature for an intent, see
          `Standard Built-in Intents
          <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
          in the *Alexa Skills Kit* .

        - **supportedLocales** *(list) --*

          A list of identifiers for the locales that the intent supports.

          - *(string) --*

    - **nextToken** *(string) --*

      A pagination token that fetches the next page of intents. If the response to this API call is
      truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of
      intents, specify the pagination token in the next request.
    """


_ClientGetBuiltinSlotTypesResponseslotTypesTypeDef = TypedDict(
    "_ClientGetBuiltinSlotTypesResponseslotTypesTypeDef",
    {"signature": str, "supportedLocales": List[str]},
    total=False,
)


class ClientGetBuiltinSlotTypesResponseslotTypesTypeDef(
    _ClientGetBuiltinSlotTypesResponseslotTypesTypeDef
):
    """
    Type definition for `ClientGetBuiltinSlotTypesResponse` `slotTypes`

    Provides information about a built in slot type.

    - **signature** *(string) --*

      A unique identifier for the built-in slot type. To find the signature for a slot type,
      see `Slot Type Reference
      <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
      in the *Alexa Skills Kit* .

    - **supportedLocales** *(list) --*

      A list of target locales for the slot.

      - *(string) --*
    """


_ClientGetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "_ClientGetBuiltinSlotTypesResponseTypeDef",
    {
        "slotTypes": List[ClientGetBuiltinSlotTypesResponseslotTypesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetBuiltinSlotTypesResponseTypeDef(
    _ClientGetBuiltinSlotTypesResponseTypeDef
):
    """
    Type definition for `ClientGetBuiltinSlotTypes` `Response`

    - **slotTypes** *(list) --*

      An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.

      - *(dict) --*

        Provides information about a built in slot type.

        - **signature** *(string) --*

          A unique identifier for the built-in slot type. To find the signature for a slot type,
          see `Slot Type Reference
          <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
          in the *Alexa Skills Kit* .

        - **supportedLocales** *(list) --*

          A list of target locales for the slot.

          - *(string) --*

    - **nextToken** *(string) --*

      If the response is truncated, the response includes a pagination token that you can use in
      your next request to fetch the next page of slot types.
    """


_ClientGetExportResponseTypeDef = TypedDict(
    "_ClientGetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": str,
        "exportType": str,
        "exportStatus": str,
        "failureReason": str,
        "url": str,
    },
    total=False,
)


class ClientGetExportResponseTypeDef(_ClientGetExportResponseTypeDef):
    """
    Type definition for `ClientGetExport` `Response`

    - **name** *(string) --*

      The name of the bot being exported.

    - **version** *(string) --*

      The version of the bot being exported.

    - **resourceType** *(string) --*

      The type of the exported resource.

    - **exportType** *(string) --*

      The format of the exported data.

    - **exportStatus** *(string) --*

      The status of the export.

      * ``IN_PROGRESS`` - The export is in progress.

      * ``READY`` - The export is complete.

      * ``FAILED`` - The export could not be completed.

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to export the
      resource.

    - **url** *(string) --*

      An S3 pre-signed URL that provides the location of the exported resource. The exported
      resource is a ZIP archive that contains the exported resource in JSON format. The structure
      of the archive may change. Your code should not rely on the archive structure.
    """


_ClientGetImportResponseTypeDef = TypedDict(
    "_ClientGetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": str,
        "mergeStrategy": str,
        "importId": str,
        "importStatus": str,
        "failureReason": List[str],
        "createdDate": datetime,
    },
    total=False,
)


class ClientGetImportResponseTypeDef(_ClientGetImportResponseTypeDef):
    """
    Type definition for `ClientGetImport` `Response`

    - **name** *(string) --*

      The name given to the import job.

    - **resourceType** *(string) --*

      The type of resource imported.

    - **mergeStrategy** *(string) --*

      The action taken when there was a conflict between an existing resource and a resource in the
      import file.

    - **importId** *(string) --*

      The identifier for the specific import job.

    - **importStatus** *(string) --*

      The status of the import job. If the status is ``FAILED`` , you can get the reason for the
      failure from the ``failureReason`` field.

    - **failureReason** *(list) --*

      A string that describes why an import job failed to complete.

      - *(string) --*

    - **createdDate** *(datetime) --*

      A timestamp for the date and time that the import job was created.
    """


_ClientGetIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseconclusionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponseconclusionStatementmessagesTypeDef(
    _ClientGetIntentResponseconclusionStatementmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponseconclusionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponseconclusionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseconclusionStatementTypeDef(
    _ClientGetIntentResponseconclusionStatementTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `conclusionStatement`

    After the Lambda function specified in the ``fulfillmentActivity`` element fulfills the
    intent, Amazon Lex conveys this statement to the user.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientGetIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseconfirmationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponseconfirmationPromptmessagesTypeDef(
    _ClientGetIntentResponseconfirmationPromptmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponseconfirmationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientGetIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientGetIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseconfirmationPromptTypeDef(
    _ClientGetIntentResponseconfirmationPromptTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `confirmationPrompt`

    If defined in the bot, Amazon Lex uses prompt to confirm the intent before fulfilling the
    user's request. For more information, see  PutIntent .

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientGetIntentResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientGetIntentResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientGetIntentResponsedialogCodeHookTypeDef(
    _ClientGetIntentResponsedialogCodeHookTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `dialogCodeHook`

    If defined in the bot, Amazon Amazon Lex invokes this Lambda function for each user input.
    For more information, see  PutIntent .

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponsefollowUpPromptprompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientGetIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptpromptTypeDef(
    _ClientGetIntentResponsefollowUpPromptpromptTypeDef
):
    """
    Type definition for `ClientGetIntentResponsefollowUpPrompt` `prompt`

    Prompts for information from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponsefollowUpPromptrejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[
            ClientGetIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef
):
    """
    Type definition for `ClientGetIntentResponsefollowUpPrompt` `rejectionStatement`

    If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientGetIntentResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientGetIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientGetIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientGetIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientGetIntentResponsefollowUpPromptTypeDef(
    _ClientGetIntentResponsefollowUpPromptTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `followUpPrompt`

    If defined in the bot, Amazon Lex uses this prompt to solicit additional user activity after
    the intent is fulfilled. For more information, see  PutIntent .

    - **prompt** *(dict) --*

      Prompts for information from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.
    """


_ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef(
    _ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef
):
    """
    Type definition for `ClientGetIntentResponsefulfillmentActivity` `codeHook`

    A description of the Lambda function that is run to fulfill the intent.

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientGetIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientGetIntentResponsefulfillmentActivityTypeDef",
    {
        "type": str,
        "codeHook": ClientGetIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientGetIntentResponsefulfillmentActivityTypeDef(
    _ClientGetIntentResponsefulfillmentActivityTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `fulfillmentActivity`

    Describes how the intent is fulfilled. For more information, see  PutIntent .

    - **type** *(string) --*

      How the intent should be fulfilled, either by running a Lambda function or by returning the
      slot data to the client application.

    - **codeHook** *(dict) --*

      A description of the Lambda function that is run to fulfill the intent.

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .
    """


_ClientGetIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponserejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponserejectionStatementmessagesTypeDef(
    _ClientGetIntentResponserejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponserejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponserejectionStatementTypeDef = TypedDict(
    "_ClientGetIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientGetIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponserejectionStatementTypeDef(
    _ClientGetIntentResponserejectionStatementTypeDef
):
    """
    Type definition for `ClientGetIntentResponse` `rejectionStatement`

    If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef
):
    """
    Type definition for `ClientGetIntentResponseslotsvalueElicitationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned
      to a message, Amazon Lex returns one message from each group in the response.
    """


_ClientGetIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[
            ClientGetIntentResponseslotsvalueElicitationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseslotsvalueElicitationPromptTypeDef(
    _ClientGetIntentResponseslotsvalueElicitationPromptTypeDef
):
    """
    Type definition for `ClientGetIntentResponseslots` `valueElicitationPrompt`

    The prompt that Amazon Lex uses to elicit the slot value from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned
          to a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientGetIntentResponseslotsTypeDef = TypedDict(
    "_ClientGetIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientGetIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientGetIntentResponseslotsTypeDef(_ClientGetIntentResponseslotsTypeDef):
    """
    Type definition for `ClientGetIntentResponse` `slots`

    Identifies the version of a specific slot.

    - **name** *(string) --*

      The name of the slot.

    - **description** *(string) --*

      A description of the slot.

    - **slotConstraint** *(string) --*

      Specifies whether the slot is required or optional.

    - **slotType** *(string) --*

      The type of the slot, either a custom slot type that you defined or one of the built-in
      slot types.

    - **slotTypeVersion** *(string) --*

      The version of the slot type.

    - **valueElicitationPrompt** *(dict) --*

      The prompt that Amazon Lex uses to elicit the slot value from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned
            to a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **priority** *(integer) --*

      Directs Lex the order in which to elicit this slot value from the user. For example, if
      the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
      slot with priority 1.

      If multiple slots share the same priority, the order in which Lex elicits values is
      arbitrary.

    - **sampleUtterances** *(list) --*

      If you know a specific pattern with which users might respond to an Amazon Lex request
      for a slot value, you can provide those utterances to improve accuracy. This is optional.
      In most cases, Amazon Lex is capable of understanding user utterances.

      - *(string) --*

    - **responseCard** *(string) --*

      A set of possible responses for the slot type used by text-based clients. A user chooses
      an option from the response card, instead of using text to reply.
    """


_ClientGetIntentResponseTypeDef = TypedDict(
    "_ClientGetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientGetIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientGetIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientGetIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientGetIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientGetIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientGetIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientGetIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
    },
    total=False,
)


class ClientGetIntentResponseTypeDef(_ClientGetIntentResponseTypeDef):
    """
    Type definition for `ClientGetIntent` `Response`

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **slots** *(list) --*

      An array of intent slots configured for the intent.

      - *(dict) --*

        Identifies the version of a specific slot.

        - **name** *(string) --*

          The name of the slot.

        - **description** *(string) --*

          A description of the slot.

        - **slotConstraint** *(string) --*

          Specifies whether the slot is required or optional.

        - **slotType** *(string) --*

          The type of the slot, either a custom slot type that you defined or one of the built-in
          slot types.

        - **slotTypeVersion** *(string) --*

          The version of the slot type.

        - **valueElicitationPrompt** *(dict) --*

          The prompt that Amazon Lex uses to elicit the slot value from the user.

          - **messages** *(list) --*

            An array of objects, each of which provides a message string and its type. You can
            specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            - *(dict) --*

              The message object that provides the message text and its type.

              - **contentType** *(string) --*

                The content type of the message string.

              - **content** *(string) --*

                The text of the message.

              - **groupNumber** *(integer) --*

                Identifies the message group that the message belongs to. When a group is assigned
                to a message, Amazon Lex returns one message from each group in the response.

          - **maxAttempts** *(integer) --*

            The number of times to prompt the user for information.

          - **responseCard** *(string) --*

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
            response. It substitutes session attributes and slot values for placeholders in the
            response card. For more information, see  ex-resp-card .

        - **priority** *(integer) --*

          Directs Lex the order in which to elicit this slot value from the user. For example, if
          the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
          slot with priority 1.

          If multiple slots share the same priority, the order in which Lex elicits values is
          arbitrary.

        - **sampleUtterances** *(list) --*

          If you know a specific pattern with which users might respond to an Amazon Lex request
          for a slot value, you can provide those utterances to improve accuracy. This is optional.
          In most cases, Amazon Lex is capable of understanding user utterances.

          - *(string) --*

        - **responseCard** *(string) --*

          A set of possible responses for the slot type used by text-based clients. A user chooses
          an option from the response card, instead of using text to reply.

    - **sampleUtterances** *(list) --*

      An array of sample utterances configured for the intent.

      - *(string) --*

    - **confirmationPrompt** *(dict) --*

      If defined in the bot, Amazon Lex uses prompt to confirm the intent before fulfilling the
      user's request. For more information, see  PutIntent .

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **followUpPrompt** *(dict) --*

      If defined in the bot, Amazon Lex uses this prompt to solicit additional user activity after
      the intent is fulfilled. For more information, see  PutIntent .

      - **prompt** *(dict) --*

        Prompts for information from the user.

        - **messages** *(list) --*

          An array of objects, each of which provides a message string and its type. You can
          specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **maxAttempts** *(integer) --*

          The number of times to prompt the user for information.

        - **responseCard** *(string) --*

          A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
          response. It substitutes session attributes and slot values for placeholders in the
          response card. For more information, see  ex-resp-card .

      - **rejectionStatement** *(dict) --*

        If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
        responds with this statement to acknowledge that the intent was canceled.

        - **messages** *(list) --*

          A collection of message objects.

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **responseCard** *(string) --*

          At runtime, if the client is using the `PostText
          <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
          includes the response card in the response. It substitutes all of the session attributes
          and slot values for placeholders in the response card.

    - **conclusionStatement** *(dict) --*

      After the Lambda function specified in the ``fulfillmentActivity`` element fulfills the
      intent, Amazon Lex conveys this statement to the user.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **dialogCodeHook** *(dict) --*

      If defined in the bot, Amazon Amazon Lex invokes this Lambda function for each user input.
      For more information, see  PutIntent .

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .

    - **fulfillmentActivity** *(dict) --*

      Describes how the intent is fulfilled. For more information, see  PutIntent .

      - **type** *(string) --*

        How the intent should be fulfilled, either by running a Lambda function or by returning the
        slot data to the client application.

      - **codeHook** *(dict) --*

        A description of the Lambda function that is run to fulfill the intent.

        - **uri** *(string) --*

          The Amazon Resource Name (ARN) of the Lambda function.

        - **messageVersion** *(string) --*

          The version of the request-response that you want Amazon Lex to use to invoke your Lambda
          function. For more information, see  using-lambda .

    - **parentIntentSignature** *(string) --*

      A unique identifier for a built-in intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create a resource, the creation date and the
      last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent.

    - **checksum** *(string) --*

      Checksum of the intent.
    """


_ClientGetIntentVersionsResponseintentsTypeDef = TypedDict(
    "_ClientGetIntentVersionsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetIntentVersionsResponseintentsTypeDef(
    _ClientGetIntentVersionsResponseintentsTypeDef
):
    """
    Type definition for `ClientGetIntentVersionsResponse` `intents`

    Provides information about an intent.

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create an intent, the creation date and
      last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent.
    """


_ClientGetIntentVersionsResponseTypeDef = TypedDict(
    "_ClientGetIntentVersionsResponseTypeDef",
    {"intents": List[ClientGetIntentVersionsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetIntentVersionsResponseTypeDef(_ClientGetIntentVersionsResponseTypeDef):
    """
    Type definition for `ClientGetIntentVersions` `Response`

    - **intents** *(list) --*

      An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one
      for the ``$LATEST`` version.

      - *(dict) --*

        Provides information about an intent.

        - **name** *(string) --*

          The name of the intent.

        - **description** *(string) --*

          A description of the intent.

        - **lastUpdatedDate** *(datetime) --*

          The date that the intent was updated. When you create an intent, the creation date and
          last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the intent was created.

        - **version** *(string) --*

          The version of the intent.

    - **nextToken** *(string) --*

      A pagination token for fetching the next page of intent versions. If the response to this
      call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next
      page of versions, specify the pagination token in the next request.
    """


_ClientGetIntentsResponseintentsTypeDef = TypedDict(
    "_ClientGetIntentsResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetIntentsResponseintentsTypeDef(_ClientGetIntentsResponseintentsTypeDef):
    """
    Type definition for `ClientGetIntentsResponse` `intents`

    Provides information about an intent.

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create an intent, the creation date and
      last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent.
    """


_ClientGetIntentsResponseTypeDef = TypedDict(
    "_ClientGetIntentsResponseTypeDef",
    {"intents": List[ClientGetIntentsResponseintentsTypeDef], "nextToken": str},
    total=False,
)


class ClientGetIntentsResponseTypeDef(_ClientGetIntentsResponseTypeDef):
    """
    Type definition for `ClientGetIntents` `Response`

    - **intents** *(list) --*

      An array of ``Intent`` objects. For more information, see  PutBot .

      - *(dict) --*

        Provides information about an intent.

        - **name** *(string) --*

          The name of the intent.

        - **description** *(string) --*

          A description of the intent.

        - **lastUpdatedDate** *(datetime) --*

          The date that the intent was updated. When you create an intent, the creation date and
          last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the intent was created.

        - **version** *(string) --*

          The version of the intent.

    - **nextToken** *(string) --*

      If the response is truncated, the response includes a pagination token that you can specify
      in your next request to fetch the next page of intents.
    """


_ClientGetSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "_ClientGetSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientGetSlotTypeResponseenumerationValuesTypeDef(
    _ClientGetSlotTypeResponseenumerationValuesTypeDef
):
    """
    Type definition for `ClientGetSlotTypeResponse` `enumerationValues`

    Each slot type can have a set of values. Each enumeration value represents a value the slot
    type can take.

    For example, a pizza ordering bot could have a slot type that specifies the type of crust
    that the pizza should have. The slot type could include the values

    * thick

    * thin

    * stuffed

    - **value** *(string) --*

      The value of the slot type.

    - **synonyms** *(list) --*

      Additional values related to the slot type value.

      - *(string) --*
    """


_ClientGetSlotTypeResponseTypeDef = TypedDict(
    "_ClientGetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientGetSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": str,
    },
    total=False,
)


class ClientGetSlotTypeResponseTypeDef(_ClientGetSlotTypeResponseTypeDef):
    """
    Type definition for `ClientGetSlotType` `Response`

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **enumerationValues** *(list) --*

      A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

      - *(dict) --*

        Each slot type can have a set of values. Each enumeration value represents a value the slot
        type can take.

        For example, a pizza ordering bot could have a slot type that specifies the type of crust
        that the pizza should have. The slot type could include the values

        * thick

        * thin

        * stuffed

        - **value** *(string) --*

          The value of the slot type.

        - **synonyms** *(list) --*

          Additional values related to the slot type value.

          - *(string) --*

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date and
      last update date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type.

    - **checksum** *(string) --*

      Checksum of the ``$LATEST`` version of the slot type.

    - **valueSelectionStrategy** *(string) --*

      The strategy that Amazon Lex uses to determine the value of the slot. For more information,
      see  PutSlotType .
    """


_ClientGetSlotTypeVersionsResponseslotTypesTypeDef = TypedDict(
    "_ClientGetSlotTypeVersionsResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetSlotTypeVersionsResponseslotTypesTypeDef(
    _ClientGetSlotTypeVersionsResponseslotTypesTypeDef
):
    """
    Type definition for `ClientGetSlotTypeVersionsResponse` `slotTypes`

    Provides information about a slot type..

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type.
    """


_ClientGetSlotTypeVersionsResponseTypeDef = TypedDict(
    "_ClientGetSlotTypeVersionsResponseTypeDef",
    {
        "slotTypes": List[ClientGetSlotTypeVersionsResponseslotTypesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetSlotTypeVersionsResponseTypeDef(
    _ClientGetSlotTypeVersionsResponseTypeDef
):
    """
    Type definition for `ClientGetSlotTypeVersions` `Response`

    - **slotTypes** *(list) --*

      An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type plus
      one for the ``$LATEST`` version.

      - *(dict) --*

        Provides information about a slot type..

        - **name** *(string) --*

          The name of the slot type.

        - **description** *(string) --*

          A description of the slot type.

        - **lastUpdatedDate** *(datetime) --*

          The date that the slot type was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the slot type was created.

        - **version** *(string) --*

          The version of the slot type.

    - **nextToken** *(string) --*

      A pagination token for fetching the next page of slot type versions. If the response to this
      call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next
      page of versions, specify the pagination token in the next request.
    """


_ClientGetSlotTypesResponseslotTypesTypeDef = TypedDict(
    "_ClientGetSlotTypesResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class ClientGetSlotTypesResponseslotTypesTypeDef(
    _ClientGetSlotTypesResponseslotTypesTypeDef
):
    """
    Type definition for `ClientGetSlotTypesResponse` `slotTypes`

    Provides information about a slot type..

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type.
    """


_ClientGetSlotTypesResponseTypeDef = TypedDict(
    "_ClientGetSlotTypesResponseTypeDef",
    {"slotTypes": List[ClientGetSlotTypesResponseslotTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetSlotTypesResponseTypeDef(_ClientGetSlotTypesResponseTypeDef):
    """
    Type definition for `ClientGetSlotTypes` `Response`

    - **slotTypes** *(list) --*

      An array of objects, one for each slot type, that provides information such as the name of
      the slot type, the version, and a description.

      - *(dict) --*

        Provides information about a slot type..

        - **name** *(string) --*

          The name of the slot type.

        - **description** *(string) --*

          A description of the slot type.

        - **lastUpdatedDate** *(datetime) --*

          The date that the slot type was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the slot type was created.

        - **version** *(string) --*

          The version of the slot type.

    - **nextToken** *(string) --*

      If the response is truncated, it includes a pagination token that you can specify in your
      next request to fetch the next page of slot types.
    """


_ClientGetUtterancesViewResponseutterancesutterancesTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseutterancesutterancesTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)


class ClientGetUtterancesViewResponseutterancesutterancesTypeDef(
    _ClientGetUtterancesViewResponseutterancesutterancesTypeDef
):
    """
    Type definition for `ClientGetUtterancesViewResponseutterances` `utterances`

    Provides information about a single utterance that was made to your bot.

    - **utteranceString** *(string) --*

      The text that was entered by the user or the text representation of an audio clip.

    - **count** *(integer) --*

      The number of times that the utterance was processed.

    - **distinctUsers** *(integer) --*

      The total number of individuals that used the utterance.

    - **firstUtteredDate** *(datetime) --*

      The date that the utterance was first recorded.

    - **lastUtteredDate** *(datetime) --*

      The date that the utterance was last recorded.
    """


_ClientGetUtterancesViewResponseutterancesTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseutterancesTypeDef",
    {
        "botVersion": str,
        "utterances": List[ClientGetUtterancesViewResponseutterancesutterancesTypeDef],
    },
    total=False,
)


class ClientGetUtterancesViewResponseutterancesTypeDef(
    _ClientGetUtterancesViewResponseutterancesTypeDef
):
    """
    Type definition for `ClientGetUtterancesViewResponse` `utterances`

    Provides a list of utterances that have been made to a specific version of your bot. The
    list contains a maximum of 100 utterances.

    - **botVersion** *(string) --*

      The version of the bot that processed the list.

    - **utterances** *(list) --*

      One or more  UtteranceData objects that contain information about the utterances that
      have been made to a bot. The maximum number of object is 100.

      - *(dict) --*

        Provides information about a single utterance that was made to your bot.

        - **utteranceString** *(string) --*

          The text that was entered by the user or the text representation of an audio clip.

        - **count** *(integer) --*

          The number of times that the utterance was processed.

        - **distinctUsers** *(integer) --*

          The total number of individuals that used the utterance.

        - **firstUtteredDate** *(datetime) --*

          The date that the utterance was first recorded.

        - **lastUtteredDate** *(datetime) --*

          The date that the utterance was last recorded.
    """


_ClientGetUtterancesViewResponseTypeDef = TypedDict(
    "_ClientGetUtterancesViewResponseTypeDef",
    {
        "botName": str,
        "utterances": List[ClientGetUtterancesViewResponseutterancesTypeDef],
    },
    total=False,
)


class ClientGetUtterancesViewResponseTypeDef(_ClientGetUtterancesViewResponseTypeDef):
    """
    Type definition for `ClientGetUtterancesView` `Response`

    - **botName** *(string) --*

      The name of the bot for which utterance information was returned.

    - **utterances** *(list) --*

      An array of  UtteranceList objects, each containing a list of  UtteranceData objects
      describing the utterances that were processed by your bot. The response contains a maximum of
      100 ``UtteranceData`` objects for each version.

      - *(dict) --*

        Provides a list of utterances that have been made to a specific version of your bot. The
        list contains a maximum of 100 utterances.

        - **botVersion** *(string) --*

          The version of the bot that processed the list.

        - **utterances** *(list) --*

          One or more  UtteranceData objects that contain information about the utterances that
          have been made to a bot. The maximum number of object is 100.

          - *(dict) --*

            Provides information about a single utterance that was made to your bot.

            - **utteranceString** *(string) --*

              The text that was entered by the user or the text representation of an audio clip.

            - **count** *(integer) --*

              The number of times that the utterance was processed.

            - **distinctUsers** *(integer) --*

              The total number of individuals that used the utterance.

            - **firstUtteredDate** *(datetime) --*

              The date that the utterance was first recorded.

            - **lastUtteredDate** *(datetime) --*

              The date that the utterance was last recorded.
    """


_ClientPutBotAliasResponseTypeDef = TypedDict(
    "_ClientPutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class ClientPutBotAliasResponseTypeDef(_ClientPutBotAliasResponseTypeDef):
    """
    Type definition for `ClientPutBotAlias` `Response`

    - **name** *(string) --*

      The name of the alias.

    - **description** *(string) --*

      A description of the alias.

    - **botVersion** *(string) --*

      The version of the bot that the alias points to.

    - **botName** *(string) --*

      The name of the bot that the alias points to.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot alias was updated. When you create a resource, the creation date and
      the last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot alias was created.

    - **checksum** *(string) --*

      The checksum for the current version of the alias.
    """


_ClientPutBotResponseabortStatementmessagesTypeDef = TypedDict(
    "_ClientPutBotResponseabortStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotResponseabortStatementmessagesTypeDef(
    _ClientPutBotResponseabortStatementmessagesTypeDef
):
    """
    Type definition for `ClientPutBotResponseabortStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutBotResponseabortStatementTypeDef = TypedDict(
    "_ClientPutBotResponseabortStatementTypeDef",
    {
        "messages": List[ClientPutBotResponseabortStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutBotResponseabortStatementTypeDef(
    _ClientPutBotResponseabortStatementTypeDef
):
    """
    Type definition for `ClientPutBotResponse` `abortStatement`

    The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientPutBotResponseclarificationPromptmessagesTypeDef = TypedDict(
    "_ClientPutBotResponseclarificationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutBotResponseclarificationPromptmessagesTypeDef(
    _ClientPutBotResponseclarificationPromptmessagesTypeDef
):
    """
    Type definition for `ClientPutBotResponseclarificationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutBotResponseclarificationPromptTypeDef = TypedDict(
    "_ClientPutBotResponseclarificationPromptTypeDef",
    {
        "messages": List[ClientPutBotResponseclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutBotResponseclarificationPromptTypeDef(
    _ClientPutBotResponseclarificationPromptTypeDef
):
    """
    Type definition for `ClientPutBotResponse` `clarificationPrompt`

    The prompts that Amazon Lex uses when it doesn't understand the user's intent. For more
    information, see  PutBot .

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientPutBotResponseintentsTypeDef = TypedDict(
    "_ClientPutBotResponseintentsTypeDef",
    {"intentName": str, "intentVersion": str},
    total=False,
)


class ClientPutBotResponseintentsTypeDef(_ClientPutBotResponseintentsTypeDef):
    """
    Type definition for `ClientPutBotResponse` `intents`

    Identifies the specific version of an intent.

    - **intentName** *(string) --*

      The name of the intent.

    - **intentVersion** *(string) --*

      The version of the intent.
    """


_ClientPutBotResponseTypeDef = TypedDict(
    "_ClientPutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[ClientPutBotResponseintentsTypeDef],
        "clarificationPrompt": ClientPutBotResponseclarificationPromptTypeDef,
        "abortStatement": ClientPutBotResponseabortStatementTypeDef,
        "status": str,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": str,
        "childDirected": bool,
        "createVersion": bool,
    },
    total=False,
)


class ClientPutBotResponseTypeDef(_ClientPutBotResponseTypeDef):
    """
    Type definition for `ClientPutBot` `Response`

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **intents** *(list) --*

      An array of ``Intent`` objects. For more information, see  PutBot .

      - *(dict) --*

        Identifies the specific version of an intent.

        - **intentName** *(string) --*

          The name of the intent.

        - **intentVersion** *(string) --*

          The version of the intent.

    - **clarificationPrompt** *(dict) --*

      The prompts that Amazon Lex uses when it doesn't understand the user's intent. For more
      information, see  PutBot .

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **abortStatement** *(dict) --*

      The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **status** *(string) --*

      When you send a request to create a bot with ``processBehavior`` set to ``BUILD`` , Amazon
      Lex sets the ``status`` response element to ``BUILDING`` . After Amazon Lex builds the bot,
      it sets ``status`` to ``READY`` . If Amazon Lex can't build the bot, Amazon Lex sets
      ``status`` to ``FAILED`` . Amazon Lex returns the reason for the failure in the
      ``failureReason`` response element.

      When you set ``processBehavior`` to ``SAVE`` , Amazon Lex sets the status code to ``NOT
      BUILT`` .

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to build the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a resource, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **idleSessionTTLInSeconds** *(integer) --*

      The maximum length of time that Amazon Lex retains the data gathered in a conversation. For
      more information, see  PutBot .

    - **voiceId** *(string) --*

      The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more
      information, see  PutBot .

    - **checksum** *(string) --*

      Checksum of the bot that you created.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **locale** *(string) --*

      The target locale for the bot.

    - **childDirected** *(boolean) --*

      For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to the
      Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the
      ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm
      that your use of Amazon Lex **is** related to a website, program, or other application that
      is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
      By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon
      Lex **is not** related to a website, program, or other application that is directed or
      targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not
      specify a default value for the ``childDirected`` field that does not accurately reflect
      whether your use of Amazon Lex is related to a website, program, or other application that is
      directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

      If your use of Amazon Lex relates to a website, program, or other application that is
      directed in whole or in part, to children under age 13, you must obtain any required
      verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in
      connection with websites, programs, or other applications that are directed or targeted, in
      whole or in part, to children under age 13, see the `Amazon Lex FAQ.
      <https://aws.amazon.com/lex/faqs#data-security>`__

    - **createVersion** *(boolean) --*
    """


_RequiredClientPutBotabortStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotabortStatementmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutBotabortStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotabortStatementmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutBotabortStatementmessagesTypeDef(
    _RequiredClientPutBotabortStatementmessagesTypeDef,
    _OptionalClientPutBotabortStatementmessagesTypeDef,
):
    """
    Type definition for `ClientPutBotabortStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutBotabortStatementTypeDef = TypedDict(
    "_RequiredClientPutBotabortStatementTypeDef",
    {"messages": List[ClientPutBotabortStatementmessagesTypeDef]},
)
_OptionalClientPutBotabortStatementTypeDef = TypedDict(
    "_OptionalClientPutBotabortStatementTypeDef", {"responseCard": str}, total=False
)


class ClientPutBotabortStatementTypeDef(
    _RequiredClientPutBotabortStatementTypeDef,
    _OptionalClientPutBotabortStatementTypeDef,
):
    """
    Type definition for `ClientPutBot` `abortStatement`

    When Amazon Lex can't understand the user's input in context, it tries to elicit the information
    a few times. After that, Amazon Lex sends the message defined in ``abortStatement`` to the user,
    and then aborts the conversation. To set the number of retries, use the
    ``valueElicitationPrompt`` field for the slot type.

    For example, in a pizza ordering bot, Amazon Lex might ask a user "What type of crust would you
    like?" If the user's response is not one of the expected responses (for example, "thin crust,
    "deep dish," etc.), Amazon Lex tries to elicit a correct response a few more times.

    For example, in a pizza ordering application, ``OrderPizza`` might be one of the intents. This
    intent might require the ``CrustType`` slot. You specify the ``valueElicitationPrompt`` field
    when you create the ``CrustType`` slot.

    - **messages** *(list) --* **[REQUIRED]**

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes and
      slot values for placeholders in the response card.
    """


_RequiredClientPutBotclarificationPromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutBotclarificationPromptmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutBotclarificationPromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutBotclarificationPromptmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutBotclarificationPromptmessagesTypeDef(
    _RequiredClientPutBotclarificationPromptmessagesTypeDef,
    _OptionalClientPutBotclarificationPromptmessagesTypeDef,
):
    """
    Type definition for `ClientPutBotclarificationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutBotclarificationPromptTypeDef = TypedDict(
    "_RequiredClientPutBotclarificationPromptTypeDef",
    {
        "messages": List[ClientPutBotclarificationPromptmessagesTypeDef],
        "maxAttempts": int,
    },
)
_OptionalClientPutBotclarificationPromptTypeDef = TypedDict(
    "_OptionalClientPutBotclarificationPromptTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutBotclarificationPromptTypeDef(
    _RequiredClientPutBotclarificationPromptTypeDef,
    _OptionalClientPutBotclarificationPromptTypeDef,
):
    """
    Type definition for `ClientPutBot` `clarificationPrompt`

    When Amazon Lex doesn't understand the user's intent, it uses this message to get clarification.
    To specify how many times Amazon Lex should repeate the clarification prompt, use the
    ``maxAttempts`` field. If Amazon Lex still doesn't understand, it sends the message in the
    ``abortStatement`` field.

    When you create a clarification prompt, make sure that it suggests the correct response from the
    user. for example, for a bot that orders pizza and drinks, you might create this clarification
    prompt: "What would you like to do? You can say 'Order a pizza' or 'Order a drink.'"

    - **messages** *(list) --* **[REQUIRED]**

      An array of objects, each of which provides a message string and its type. You can specify the
      message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --* **[REQUIRED]**

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It
      substitutes session attributes and slot values for placeholders in the response card. For more
      information, see  ex-resp-card .
    """


_ClientPutBotintentsTypeDef = TypedDict(
    "_ClientPutBotintentsTypeDef", {"intentName": str, "intentVersion": str}
)


class ClientPutBotintentsTypeDef(_ClientPutBotintentsTypeDef):
    """
    Type definition for `ClientPutBot` `intents`

    Identifies the specific version of an intent.

    - **intentName** *(string) --* **[REQUIRED]**

      The name of the intent.

    - **intentVersion** *(string) --* **[REQUIRED]**

      The version of the intent.
    """


_ClientPutIntentResponseconclusionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseconclusionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponseconclusionStatementmessagesTypeDef(
    _ClientPutIntentResponseconclusionStatementmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponseconclusionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponseconclusionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponseconclusionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponseconclusionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseconclusionStatementTypeDef(
    _ClientPutIntentResponseconclusionStatementTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `conclusionStatement`

    After the Lambda function specified in the``fulfillmentActivity`` intent fulfills the intent,
    Amazon Lex conveys this statement to the user.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientPutIntentResponseconfirmationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseconfirmationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponseconfirmationPromptmessagesTypeDef(
    _ClientPutIntentResponseconfirmationPromptmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponseconfirmationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponseconfirmationPromptTypeDef = TypedDict(
    "_ClientPutIntentResponseconfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentResponseconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseconfirmationPromptTypeDef(
    _ClientPutIntentResponseconfirmationPromptTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `confirmationPrompt`

    If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling
    it.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_ClientPutIntentResponsedialogCodeHookTypeDef = TypedDict(
    "_ClientPutIntentResponsedialogCodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientPutIntentResponsedialogCodeHookTypeDef(
    _ClientPutIntentResponsedialogCodeHookTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `dialogCodeHook`

    If defined in the intent, Amazon Lex invokes this Lambda function for each user input.

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef(
    _ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponsefollowUpPromptprompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponsefollowUpPromptpromptTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientPutIntentResponsefollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptpromptTypeDef(
    _ClientPutIntentResponsefollowUpPromptpromptTypeDef
):
    """
    Type definition for `ClientPutIntentResponsefollowUpPrompt` `prompt`

    Prompts for information from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef(
    _ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponsefollowUpPromptrejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to
      a message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef",
    {
        "messages": List[
            ClientPutIntentResponsefollowUpPromptrejectionStatementmessagesTypeDef
        ],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef(
    _ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef
):
    """
    Type definition for `ClientPutIntentResponsefollowUpPrompt` `rejectionStatement`

    If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to
          a message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientPutIntentResponsefollowUpPromptTypeDef = TypedDict(
    "_ClientPutIntentResponsefollowUpPromptTypeDef",
    {
        "prompt": ClientPutIntentResponsefollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientPutIntentResponsefollowUpPromptrejectionStatementTypeDef,
    },
    total=False,
)


class ClientPutIntentResponsefollowUpPromptTypeDef(
    _ClientPutIntentResponsefollowUpPromptTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `followUpPrompt`

    If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity
    after the intent is fulfilled.

    - **prompt** *(dict) --*

      Prompts for information from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to
            a message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.
    """


_ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
    total=False,
)


class ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef(
    _ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef
):
    """
    Type definition for `ClientPutIntentResponsefulfillmentActivity` `codeHook`

    A description of the Lambda function that is run to fulfill the intent.

    - **uri** *(string) --*

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --*

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_ClientPutIntentResponsefulfillmentActivityTypeDef = TypedDict(
    "_ClientPutIntentResponsefulfillmentActivityTypeDef",
    {
        "type": str,
        "codeHook": ClientPutIntentResponsefulfillmentActivitycodeHookTypeDef,
    },
    total=False,
)


class ClientPutIntentResponsefulfillmentActivityTypeDef(
    _ClientPutIntentResponsefulfillmentActivityTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `fulfillmentActivity`

    If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after
    the user provides all of the information required by the intent.

    - **type** *(string) --*

      How the intent should be fulfilled, either by running a Lambda function or by returning the
      slot data to the client application.

    - **codeHook** *(dict) --*

      A description of the Lambda function that is run to fulfill the intent.

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .
    """


_ClientPutIntentResponserejectionStatementmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponserejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponserejectionStatementmessagesTypeDef(
    _ClientPutIntentResponserejectionStatementmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponserejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponserejectionStatementTypeDef = TypedDict(
    "_ClientPutIntentResponserejectionStatementTypeDef",
    {
        "messages": List[ClientPutIntentResponserejectionStatementmessagesTypeDef],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponserejectionStatementTypeDef(
    _ClientPutIntentResponserejectionStatementTypeDef
):
    """
    Type definition for `ClientPutIntentResponse` `rejectionStatement`

    If the user answers "no" to the question defined in ``confirmationPrompt`` Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --*

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes
      and slot values for placeholders in the response card.
    """


_ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef",
    {"contentType": str, "content": str, "groupNumber": int},
    total=False,
)


class ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef(
    _ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef
):
    """
    Type definition for `ClientPutIntentResponseslotsvalueElicitationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --*

      The content type of the message string.

    - **content** *(string) --*

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned
      to a message, Amazon Lex returns one message from each group in the response.
    """


_ClientPutIntentResponseslotsvalueElicitationPromptTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[
            ClientPutIntentResponseslotsvalueElicitationPromptmessagesTypeDef
        ],
        "maxAttempts": int,
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseslotsvalueElicitationPromptTypeDef(
    _ClientPutIntentResponseslotsvalueElicitationPromptTypeDef
):
    """
    Type definition for `ClientPutIntentResponseslots` `valueElicitationPrompt`

    The prompt that Amazon Lex uses to elicit the slot value from the user.

    - **messages** *(list) --*

      An array of objects, each of which provides a message string and its type. You can
      specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --*

          The content type of the message string.

        - **content** *(string) --*

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned
          to a message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --*

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
      response. It substitutes session attributes and slot values for placeholders in the
      response card. For more information, see  ex-resp-card .
    """


_ClientPutIntentResponseslotsTypeDef = TypedDict(
    "_ClientPutIntentResponseslotsTypeDef",
    {
        "name": str,
        "description": str,
        "slotConstraint": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentResponseslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentResponseslotsTypeDef(_ClientPutIntentResponseslotsTypeDef):
    """
    Type definition for `ClientPutIntentResponse` `slots`

    Identifies the version of a specific slot.

    - **name** *(string) --*

      The name of the slot.

    - **description** *(string) --*

      A description of the slot.

    - **slotConstraint** *(string) --*

      Specifies whether the slot is required or optional.

    - **slotType** *(string) --*

      The type of the slot, either a custom slot type that you defined or one of the built-in
      slot types.

    - **slotTypeVersion** *(string) --*

      The version of the slot type.

    - **valueElicitationPrompt** *(dict) --*

      The prompt that Amazon Lex uses to elicit the slot value from the user.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can
        specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned
            to a message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
        response. It substitutes session attributes and slot values for placeholders in the
        response card. For more information, see  ex-resp-card .

    - **priority** *(integer) --*

      Directs Lex the order in which to elicit this slot value from the user. For example, if
      the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
      slot with priority 1.

      If multiple slots share the same priority, the order in which Lex elicits values is
      arbitrary.

    - **sampleUtterances** *(list) --*

      If you know a specific pattern with which users might respond to an Amazon Lex request
      for a slot value, you can provide those utterances to improve accuracy. This is optional.
      In most cases, Amazon Lex is capable of understanding user utterances.

      - *(string) --*

    - **responseCard** *(string) --*

      A set of possible responses for the slot type used by text-based clients. A user chooses
      an option from the response card, instead of using text to reply.
    """


_ClientPutIntentResponseTypeDef = TypedDict(
    "_ClientPutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[ClientPutIntentResponseslotsTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": ClientPutIntentResponseconfirmationPromptTypeDef,
        "rejectionStatement": ClientPutIntentResponserejectionStatementTypeDef,
        "followUpPrompt": ClientPutIntentResponsefollowUpPromptTypeDef,
        "conclusionStatement": ClientPutIntentResponseconclusionStatementTypeDef,
        "dialogCodeHook": ClientPutIntentResponsedialogCodeHookTypeDef,
        "fulfillmentActivity": ClientPutIntentResponsefulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
    },
    total=False,
)


class ClientPutIntentResponseTypeDef(_ClientPutIntentResponseTypeDef):
    """
    Type definition for `ClientPutIntent` `Response`

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **slots** *(list) --*

      An array of intent slots that are configured for the intent.

      - *(dict) --*

        Identifies the version of a specific slot.

        - **name** *(string) --*

          The name of the slot.

        - **description** *(string) --*

          A description of the slot.

        - **slotConstraint** *(string) --*

          Specifies whether the slot is required or optional.

        - **slotType** *(string) --*

          The type of the slot, either a custom slot type that you defined or one of the built-in
          slot types.

        - **slotTypeVersion** *(string) --*

          The version of the slot type.

        - **valueElicitationPrompt** *(dict) --*

          The prompt that Amazon Lex uses to elicit the slot value from the user.

          - **messages** *(list) --*

            An array of objects, each of which provides a message string and its type. You can
            specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            - *(dict) --*

              The message object that provides the message text and its type.

              - **contentType** *(string) --*

                The content type of the message string.

              - **content** *(string) --*

                The text of the message.

              - **groupNumber** *(integer) --*

                Identifies the message group that the message belongs to. When a group is assigned
                to a message, Amazon Lex returns one message from each group in the response.

          - **maxAttempts** *(integer) --*

            The number of times to prompt the user for information.

          - **responseCard** *(string) --*

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
            response. It substitutes session attributes and slot values for placeholders in the
            response card. For more information, see  ex-resp-card .

        - **priority** *(integer) --*

          Directs Lex the order in which to elicit this slot value from the user. For example, if
          the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the
          slot with priority 1.

          If multiple slots share the same priority, the order in which Lex elicits values is
          arbitrary.

        - **sampleUtterances** *(list) --*

          If you know a specific pattern with which users might respond to an Amazon Lex request
          for a slot value, you can provide those utterances to improve accuracy. This is optional.
          In most cases, Amazon Lex is capable of understanding user utterances.

          - *(string) --*

        - **responseCard** *(string) --*

          A set of possible responses for the slot type used by text-based clients. A user chooses
          an option from the response card, instead of using text to reply.

    - **sampleUtterances** *(list) --*

      An array of sample utterances that are configured for the intent.

      - *(string) --*

    - **confirmationPrompt** *(dict) --*

      If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling
      it.

      - **messages** *(list) --*

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --*

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --*

      If the user answers "no" to the question defined in ``confirmationPrompt`` Amazon Lex
      responds with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **followUpPrompt** *(dict) --*

      If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity
      after the intent is fulfilled.

      - **prompt** *(dict) --*

        Prompts for information from the user.

        - **messages** *(list) --*

          An array of objects, each of which provides a message string and its type. You can
          specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **maxAttempts** *(integer) --*

          The number of times to prompt the user for information.

        - **responseCard** *(string) --*

          A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API
          response. It substitutes session attributes and slot values for placeholders in the
          response card. For more information, see  ex-resp-card .

      - **rejectionStatement** *(dict) --*

        If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex
        responds with this statement to acknowledge that the intent was canceled.

        - **messages** *(list) --*

          A collection of message objects.

          - *(dict) --*

            The message object that provides the message text and its type.

            - **contentType** *(string) --*

              The content type of the message string.

            - **content** *(string) --*

              The text of the message.

            - **groupNumber** *(integer) --*

              Identifies the message group that the message belongs to. When a group is assigned to
              a message, Amazon Lex returns one message from each group in the response.

        - **responseCard** *(string) --*

          At runtime, if the client is using the `PostText
          <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
          includes the response card in the response. It substitutes all of the session attributes
          and slot values for placeholders in the response card.

    - **conclusionStatement** *(dict) --*

      After the Lambda function specified in the``fulfillmentActivity`` intent fulfills the intent,
      Amazon Lex conveys this statement to the user.

      - **messages** *(list) --*

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --*

            The content type of the message string.

          - **content** *(string) --*

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes
        and slot values for placeholders in the response card.

    - **dialogCodeHook** *(dict) --*

      If defined in the intent, Amazon Lex invokes this Lambda function for each user input.

      - **uri** *(string) --*

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --*

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .

    - **fulfillmentActivity** *(dict) --*

      If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after
      the user provides all of the information required by the intent.

      - **type** *(string) --*

        How the intent should be fulfilled, either by running a Lambda function or by returning the
        slot data to the client application.

      - **codeHook** *(dict) --*

        A description of the Lambda function that is run to fulfill the intent.

        - **uri** *(string) --*

          The Amazon Resource Name (ARN) of the Lambda function.

        - **messageVersion** *(string) --*

          The version of the request-response that you want Amazon Lex to use to invoke your Lambda
          function. For more information, see  using-lambda .

    - **parentIntentSignature** *(string) --*

      A unique identifier for the built-in intent that this intent is based on.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create a resource, the creation date and last
      update dates are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent. For a new intent, the version is always ``$LATEST`` .

    - **checksum** *(string) --*

      Checksum of the ``$LATEST`` version of the intent created or updated.

    - **createVersion** *(boolean) --*
    """


_RequiredClientPutIntentconclusionStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentconclusionStatementmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentconclusionStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentconclusionStatementmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentconclusionStatementmessagesTypeDef(
    _RequiredClientPutIntentconclusionStatementmessagesTypeDef,
    _OptionalClientPutIntentconclusionStatementmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentconclusionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentconclusionStatementTypeDef = TypedDict(
    "_RequiredClientPutIntentconclusionStatementTypeDef",
    {"messages": List[ClientPutIntentconclusionStatementmessagesTypeDef]},
)
_OptionalClientPutIntentconclusionStatementTypeDef = TypedDict(
    "_OptionalClientPutIntentconclusionStatementTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentconclusionStatementTypeDef(
    _RequiredClientPutIntentconclusionStatementTypeDef,
    _OptionalClientPutIntentconclusionStatementTypeDef,
):
    """
    Type definition for `ClientPutIntent` `conclusionStatement`

    The statement that you want Amazon Lex to convey to the user after the intent is successfully
    fulfilled by the Lambda function.

    This element is relevant only if you provide a Lambda function in the ``fulfillmentActivity`` .
    If you return the intent to the client application, you can't specify this element.

    .. note::

      The ``followUpPrompt`` and ``conclusionStatement`` are mutually exclusive. You can specify only
      one.

    - **messages** *(list) --* **[REQUIRED]**

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes and
      slot values for placeholders in the response card.
    """


_RequiredClientPutIntentconfirmationPromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentconfirmationPromptmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentconfirmationPromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentconfirmationPromptmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentconfirmationPromptmessagesTypeDef(
    _RequiredClientPutIntentconfirmationPromptmessagesTypeDef,
    _OptionalClientPutIntentconfirmationPromptmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentconfirmationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentconfirmationPromptTypeDef = TypedDict(
    "_RequiredClientPutIntentconfirmationPromptTypeDef",
    {
        "messages": List[ClientPutIntentconfirmationPromptmessagesTypeDef],
        "maxAttempts": int,
    },
)
_OptionalClientPutIntentconfirmationPromptTypeDef = TypedDict(
    "_OptionalClientPutIntentconfirmationPromptTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentconfirmationPromptTypeDef(
    _RequiredClientPutIntentconfirmationPromptTypeDef,
    _OptionalClientPutIntentconfirmationPromptTypeDef,
):
    """
    Type definition for `ClientPutIntent` `confirmationPrompt`

    Prompts the user to confirm the intent. This question should have a yes or no answer.

    Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for
    fulfillment. For example, with the ``OrderPizza`` intent, you might want to confirm that the
    order is correct before placing it. For other intents, such as intents that simply respond to
    user questions, you might not need to ask the user for confirmation before providing the
    information.

    .. note::

      You you must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or
      neither.

    - **messages** *(list) --* **[REQUIRED]**

      An array of objects, each of which provides a message string and its type. You can specify the
      message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --* **[REQUIRED]**

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It
      substitutes session attributes and slot values for placeholders in the response card. For more
      information, see  ex-resp-card .
    """


_ClientPutIntentdialogCodeHookTypeDef = TypedDict(
    "_ClientPutIntentdialogCodeHookTypeDef", {"uri": str, "messageVersion": str}
)


class ClientPutIntentdialogCodeHookTypeDef(_ClientPutIntentdialogCodeHookTypeDef):
    """
    Type definition for `ClientPutIntent` `dialogCodeHook`

    Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to
    personalize user interaction.

    For example, suppose your bot determines that the user is John. Your Lambda function might
    retrieve John's information from a backend database and prepopulate some of the values. For
    example, if you find that John is gluten intolerant, you might set the corresponding intent slot,
    ``GlutenIntolerant`` , to true. You might find John's phone number and set the corresponding
    session attribute.

    - **uri** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --* **[REQUIRED]**

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_RequiredClientPutIntentfollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentfollowUpPromptpromptmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentfollowUpPromptpromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentfollowUpPromptpromptmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentfollowUpPromptpromptmessagesTypeDef(
    _RequiredClientPutIntentfollowUpPromptpromptmessagesTypeDef,
    _OptionalClientPutIntentfollowUpPromptpromptmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentfollowUpPromptprompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentfollowUpPromptpromptTypeDef = TypedDict(
    "_RequiredClientPutIntentfollowUpPromptpromptTypeDef",
    {
        "messages": List[ClientPutIntentfollowUpPromptpromptmessagesTypeDef],
        "maxAttempts": int,
    },
)
_OptionalClientPutIntentfollowUpPromptpromptTypeDef = TypedDict(
    "_OptionalClientPutIntentfollowUpPromptpromptTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentfollowUpPromptpromptTypeDef(
    _RequiredClientPutIntentfollowUpPromptpromptTypeDef,
    _OptionalClientPutIntentfollowUpPromptpromptTypeDef,
):
    """
    Type definition for `ClientPutIntentfollowUpPrompt` `prompt`

    Prompts for information from the user.

    - **messages** *(list) --* **[REQUIRED]**

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --* **[REQUIRED]**

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It
      substitutes session attributes and slot values for placeholders in the response card. For
      more information, see  ex-resp-card .
    """


_RequiredClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef(
    _RequiredClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef,
    _OptionalClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentfollowUpPromptrejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentfollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_RequiredClientPutIntentfollowUpPromptrejectionStatementTypeDef",
    {"messages": List[ClientPutIntentfollowUpPromptrejectionStatementmessagesTypeDef]},
)
_OptionalClientPutIntentfollowUpPromptrejectionStatementTypeDef = TypedDict(
    "_OptionalClientPutIntentfollowUpPromptrejectionStatementTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentfollowUpPromptrejectionStatementTypeDef(
    _RequiredClientPutIntentfollowUpPromptrejectionStatementTypeDef,
    _OptionalClientPutIntentfollowUpPromptrejectionStatementTypeDef,
):
    """
    Type definition for `ClientPutIntentfollowUpPrompt` `rejectionStatement`

    If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds
    with this statement to acknowledge that the intent was canceled.

    - **messages** *(list) --* **[REQUIRED]**

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes and
      slot values for placeholders in the response card.
    """


_ClientPutIntentfollowUpPromptTypeDef = TypedDict(
    "_ClientPutIntentfollowUpPromptTypeDef",
    {
        "prompt": ClientPutIntentfollowUpPromptpromptTypeDef,
        "rejectionStatement": ClientPutIntentfollowUpPromptrejectionStatementTypeDef,
    },
)


class ClientPutIntentfollowUpPromptTypeDef(_ClientPutIntentfollowUpPromptTypeDef):
    """
    Type definition for `ClientPutIntent` `followUpPrompt`

    Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For
    example, after the ``OrderPizza`` intent is fulfilled, you might prompt the user to order a drink.

    The action that Amazon Lex takes depends on the user's response, as follows:

    * If the user says "Yes" it responds with the clarification prompt that is configured for the bot.

    * if the user says "Yes" and continues with an utterance that triggers an intent it starts a
    conversation for the intent.

    * If the user says "No" it responds with the rejection statement configured for the the follow-up
    prompt.

    * If it doesn't recognize the utterance it repeats the follow-up prompt again.

    The ``followUpPrompt`` field and the ``conclusionStatement`` field are mutually exclusive. You
    can specify only one.

    - **prompt** *(dict) --* **[REQUIRED]**

      Prompts for information from the user.

      - **messages** *(list) --* **[REQUIRED]**

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --* **[REQUIRED]**

            The content type of the message string.

          - **content** *(string) --* **[REQUIRED]**

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --* **[REQUIRED]**

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It
        substitutes session attributes and slot values for placeholders in the response card. For
        more information, see  ex-resp-card .

    - **rejectionStatement** *(dict) --* **[REQUIRED]**

      If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds
      with this statement to acknowledge that the intent was canceled.

      - **messages** *(list) --* **[REQUIRED]**

        A collection of message objects.

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --* **[REQUIRED]**

            The content type of the message string.

          - **content** *(string) --* **[REQUIRED]**

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **responseCard** *(string) --*

        At runtime, if the client is using the `PostText
        <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
        includes the response card in the response. It substitutes all of the session attributes and
        slot values for placeholders in the response card.
    """


_ClientPutIntentfulfillmentActivitycodeHookTypeDef = TypedDict(
    "_ClientPutIntentfulfillmentActivitycodeHookTypeDef",
    {"uri": str, "messageVersion": str},
)


class ClientPutIntentfulfillmentActivitycodeHookTypeDef(
    _ClientPutIntentfulfillmentActivitycodeHookTypeDef
):
    """
    Type definition for `ClientPutIntentfulfillmentActivity` `codeHook`

    A description of the Lambda function that is run to fulfill the intent.

    - **uri** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Lambda function.

    - **messageVersion** *(string) --* **[REQUIRED]**

      The version of the request-response that you want Amazon Lex to use to invoke your Lambda
      function. For more information, see  using-lambda .
    """


_RequiredClientPutIntentfulfillmentActivityTypeDef = TypedDict(
    "_RequiredClientPutIntentfulfillmentActivityTypeDef", {"type": str}
)
_OptionalClientPutIntentfulfillmentActivityTypeDef = TypedDict(
    "_OptionalClientPutIntentfulfillmentActivityTypeDef",
    {"codeHook": ClientPutIntentfulfillmentActivitycodeHookTypeDef},
    total=False,
)


class ClientPutIntentfulfillmentActivityTypeDef(
    _RequiredClientPutIntentfulfillmentActivityTypeDef,
    _OptionalClientPutIntentfulfillmentActivityTypeDef,
):
    """
    Type definition for `ClientPutIntent` `fulfillmentActivity`

    Required. Describes how the intent is fulfilled. For example, after a user provides all of the
    information for a pizza order, ``fulfillmentActivity`` defines how the bot places an order with a
    local pizza store.

    You might configure Amazon Lex to return all of the intent information to the client application,
    or direct it to invoke a Lambda function that can process the intent (for example, place an order
    with a pizzeria).

    - **type** *(string) --* **[REQUIRED]**

      How the intent should be fulfilled, either by running a Lambda function or by returning the
      slot data to the client application.

    - **codeHook** *(dict) --*

      A description of the Lambda function that is run to fulfill the intent.

      - **uri** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Lambda function.

      - **messageVersion** *(string) --* **[REQUIRED]**

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda
        function. For more information, see  using-lambda .
    """


_RequiredClientPutIntentrejectionStatementmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentrejectionStatementmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentrejectionStatementmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentrejectionStatementmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentrejectionStatementmessagesTypeDef(
    _RequiredClientPutIntentrejectionStatementmessagesTypeDef,
    _OptionalClientPutIntentrejectionStatementmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentrejectionStatement` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentrejectionStatementTypeDef = TypedDict(
    "_RequiredClientPutIntentrejectionStatementTypeDef",
    {"messages": List[ClientPutIntentrejectionStatementmessagesTypeDef]},
)
_OptionalClientPutIntentrejectionStatementTypeDef = TypedDict(
    "_OptionalClientPutIntentrejectionStatementTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentrejectionStatementTypeDef(
    _RequiredClientPutIntentrejectionStatementTypeDef,
    _OptionalClientPutIntentrejectionStatementTypeDef,
):
    """
    Type definition for `ClientPutIntent` `rejectionStatement`

    When the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex
    responds with this statement to acknowledge that the intent was canceled.

    .. note::

      You must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or neither.

    - **messages** *(list) --* **[REQUIRED]**

      A collection of message objects.

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **responseCard** *(string) --*

      At runtime, if the client is using the `PostText
      <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex
      includes the response card in the response. It substitutes all of the session attributes and
      slot values for placeholders in the response card.
    """


_RequiredClientPutIntentslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_RequiredClientPutIntentslotsvalueElicitationPromptmessagesTypeDef",
    {"contentType": str, "content": str},
)
_OptionalClientPutIntentslotsvalueElicitationPromptmessagesTypeDef = TypedDict(
    "_OptionalClientPutIntentslotsvalueElicitationPromptmessagesTypeDef",
    {"groupNumber": int},
    total=False,
)


class ClientPutIntentslotsvalueElicitationPromptmessagesTypeDef(
    _RequiredClientPutIntentslotsvalueElicitationPromptmessagesTypeDef,
    _OptionalClientPutIntentslotsvalueElicitationPromptmessagesTypeDef,
):
    """
    Type definition for `ClientPutIntentslotsvalueElicitationPrompt` `messages`

    The message object that provides the message text and its type.

    - **contentType** *(string) --* **[REQUIRED]**

      The content type of the message string.

    - **content** *(string) --* **[REQUIRED]**

      The text of the message.

    - **groupNumber** *(integer) --*

      Identifies the message group that the message belongs to. When a group is assigned to a
      message, Amazon Lex returns one message from each group in the response.
    """


_RequiredClientPutIntentslotsvalueElicitationPromptTypeDef = TypedDict(
    "_RequiredClientPutIntentslotsvalueElicitationPromptTypeDef",
    {
        "messages": List[ClientPutIntentslotsvalueElicitationPromptmessagesTypeDef],
        "maxAttempts": int,
    },
)
_OptionalClientPutIntentslotsvalueElicitationPromptTypeDef = TypedDict(
    "_OptionalClientPutIntentslotsvalueElicitationPromptTypeDef",
    {"responseCard": str},
    total=False,
)


class ClientPutIntentslotsvalueElicitationPromptTypeDef(
    _RequiredClientPutIntentslotsvalueElicitationPromptTypeDef,
    _OptionalClientPutIntentslotsvalueElicitationPromptTypeDef,
):
    """
    Type definition for `ClientPutIntentslots` `valueElicitationPrompt`

    The prompt that Amazon Lex uses to elicit the slot value from the user.

    - **messages** *(list) --* **[REQUIRED]**

      An array of objects, each of which provides a message string and its type. You can specify
      the message string in plain text or in Speech Synthesis Markup Language (SSML).

      - *(dict) --*

        The message object that provides the message text and its type.

        - **contentType** *(string) --* **[REQUIRED]**

          The content type of the message string.

        - **content** *(string) --* **[REQUIRED]**

          The text of the message.

        - **groupNumber** *(integer) --*

          Identifies the message group that the message belongs to. When a group is assigned to a
          message, Amazon Lex returns one message from each group in the response.

    - **maxAttempts** *(integer) --* **[REQUIRED]**

      The number of times to prompt the user for information.

    - **responseCard** *(string) --*

      A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
      It substitutes session attributes and slot values for placeholders in the response card.
      For more information, see  ex-resp-card .
    """


_RequiredClientPutIntentslotsTypeDef = TypedDict(
    "_RequiredClientPutIntentslotsTypeDef", {"name": str, "slotConstraint": str}
)
_OptionalClientPutIntentslotsTypeDef = TypedDict(
    "_OptionalClientPutIntentslotsTypeDef",
    {
        "description": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": ClientPutIntentslotsvalueElicitationPromptTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
    },
    total=False,
)


class ClientPutIntentslotsTypeDef(
    _RequiredClientPutIntentslotsTypeDef, _OptionalClientPutIntentslotsTypeDef
):
    """
    Type definition for `ClientPutIntent` `slots`

    Identifies the version of a specific slot.

    - **name** *(string) --* **[REQUIRED]**

      The name of the slot.

    - **description** *(string) --*

      A description of the slot.

    - **slotConstraint** *(string) --* **[REQUIRED]**

      Specifies whether the slot is required or optional.

    - **slotType** *(string) --*

      The type of the slot, either a custom slot type that you defined or one of the built-in slot
      types.

    - **slotTypeVersion** *(string) --*

      The version of the slot type.

    - **valueElicitationPrompt** *(dict) --*

      The prompt that Amazon Lex uses to elicit the slot value from the user.

      - **messages** *(list) --* **[REQUIRED]**

        An array of objects, each of which provides a message string and its type. You can specify
        the message string in plain text or in Speech Synthesis Markup Language (SSML).

        - *(dict) --*

          The message object that provides the message text and its type.

          - **contentType** *(string) --* **[REQUIRED]**

            The content type of the message string.

          - **content** *(string) --* **[REQUIRED]**

            The text of the message.

          - **groupNumber** *(integer) --*

            Identifies the message group that the message belongs to. When a group is assigned to a
            message, Amazon Lex returns one message from each group in the response.

      - **maxAttempts** *(integer) --* **[REQUIRED]**

        The number of times to prompt the user for information.

      - **responseCard** *(string) --*

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response.
        It substitutes session attributes and slot values for placeholders in the response card.
        For more information, see  ex-resp-card .

    - **priority** *(integer) --*

      Directs Lex the order in which to elicit this slot value from the user. For example, if the
      intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with
      priority 1.

      If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

    - **sampleUtterances** *(list) --*

      If you know a specific pattern with which users might respond to an Amazon Lex request for a
      slot value, you can provide those utterances to improve accuracy. This is optional. In most
      cases, Amazon Lex is capable of understanding user utterances.

      - *(string) --*

    - **responseCard** *(string) --*

      A set of possible responses for the slot type used by text-based clients. A user chooses an
      option from the response card, instead of using text to reply.
    """


_ClientPutSlotTypeResponseenumerationValuesTypeDef = TypedDict(
    "_ClientPutSlotTypeResponseenumerationValuesTypeDef",
    {"value": str, "synonyms": List[str]},
    total=False,
)


class ClientPutSlotTypeResponseenumerationValuesTypeDef(
    _ClientPutSlotTypeResponseenumerationValuesTypeDef
):
    """
    Type definition for `ClientPutSlotTypeResponse` `enumerationValues`

    Each slot type can have a set of values. Each enumeration value represents a value the slot
    type can take.

    For example, a pizza ordering bot could have a slot type that specifies the type of crust
    that the pizza should have. The slot type could include the values

    * thick

    * thin

    * stuffed

    - **value** *(string) --*

      The value of the slot type.

    - **synonyms** *(list) --*

      Additional values related to the slot type value.

      - *(string) --*
    """


_ClientPutSlotTypeResponseTypeDef = TypedDict(
    "_ClientPutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[ClientPutSlotTypeResponseenumerationValuesTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": str,
        "createVersion": bool,
    },
    total=False,
)


class ClientPutSlotTypeResponseTypeDef(_ClientPutSlotTypeResponseTypeDef):
    """
    Type definition for `ClientPutSlotType` `Response`

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **enumerationValues** *(list) --*

      A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

      - *(dict) --*

        Each slot type can have a set of values. Each enumeration value represents a value the slot
        type can take.

        For example, a pizza ordering bot could have a slot type that specifies the type of crust
        that the pizza should have. The slot type could include the values

        * thick

        * thin

        * stuffed

        - **value** *(string) --*

          The value of the slot type.

        - **synonyms** *(list) --*

          Additional values related to the slot type value.

          - *(string) --*

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a slot type, the creation date and
      last update date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type. For a new slot type, the version is always ``$LATEST`` .

    - **checksum** *(string) --*

      Checksum of the ``$LATEST`` version of the slot type.

    - **valueSelectionStrategy** *(string) --*

      The slot resolution strategy that Amazon Lex uses to determine the value of the slot. For
      more information, see  PutSlotType .

    - **createVersion** *(boolean) --*
    """


_RequiredClientPutSlotTypeenumerationValuesTypeDef = TypedDict(
    "_RequiredClientPutSlotTypeenumerationValuesTypeDef", {"value": str}
)
_OptionalClientPutSlotTypeenumerationValuesTypeDef = TypedDict(
    "_OptionalClientPutSlotTypeenumerationValuesTypeDef",
    {"synonyms": List[str]},
    total=False,
)


class ClientPutSlotTypeenumerationValuesTypeDef(
    _RequiredClientPutSlotTypeenumerationValuesTypeDef,
    _OptionalClientPutSlotTypeenumerationValuesTypeDef,
):
    """
    Type definition for `ClientPutSlotType` `enumerationValues`

    Each slot type can have a set of values. Each enumeration value represents a value the slot
    type can take.

    For example, a pizza ordering bot could have a slot type that specifies the type of crust that
    the pizza should have. The slot type could include the values

    * thick

    * thin

    * stuffed

    - **value** *(string) --* **[REQUIRED]**

      The value of the slot type.

    - **synonyms** *(list) --*

      Additional values related to the slot type value.

      - *(string) --*
    """


_ClientStartImportResponseTypeDef = TypedDict(
    "_ClientStartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": str,
        "mergeStrategy": str,
        "importId": str,
        "importStatus": str,
        "createdDate": datetime,
    },
    total=False,
)


class ClientStartImportResponseTypeDef(_ClientStartImportResponseTypeDef):
    """
    Type definition for `ClientStartImport` `Response`

    - **name** *(string) --*

      The name given to the import job.

    - **resourceType** *(string) --*

      The type of resource to import.

    - **mergeStrategy** *(string) --*

      The action to take when there is a merge conflict.

    - **importId** *(string) --*

      The identifier for the specific import job.

    - **importStatus** *(string) --*

      The status of the import job. If the status is ``FAILED`` , you can get the reason for the
      failure using the ``GetImport`` operation.

    - **createdDate** *(datetime) --*

      A timestamp for the date and time that the import job was requested.
    """


_GetBotAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotAliasesPaginatePaginationConfigTypeDef(
    _GetBotAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBotAliasesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBotAliasesPaginateResponseBotAliasesTypeDef = TypedDict(
    "_GetBotAliasesPaginateResponseBotAliasesTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
    },
    total=False,
)


class GetBotAliasesPaginateResponseBotAliasesTypeDef(
    _GetBotAliasesPaginateResponseBotAliasesTypeDef
):
    """
    Type definition for `GetBotAliasesPaginateResponse` `BotAliases`

    Provides information about a bot alias.

    - **name** *(string) --*

      The name of the bot alias.

    - **description** *(string) --*

      A description of the bot alias.

    - **botVersion** *(string) --*

      The version of the Amazon Lex bot to which the alias points.

    - **botName** *(string) --*

      The name of the bot to which the alias points.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot alias was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot alias was created.

    - **checksum** *(string) --*

      Checksum of the bot alias.
    """


_GetBotAliasesPaginateResponseTypeDef = TypedDict(
    "_GetBotAliasesPaginateResponseTypeDef",
    {
        "BotAliases": List[GetBotAliasesPaginateResponseBotAliasesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetBotAliasesPaginateResponseTypeDef(_GetBotAliasesPaginateResponseTypeDef):
    """
    Type definition for `GetBotAliasesPaginate` `Response`

    - **BotAliases** *(list) --*

      An array of ``BotAliasMetadata`` objects, each describing a bot alias.

      - *(dict) --*

        Provides information about a bot alias.

        - **name** *(string) --*

          The name of the bot alias.

        - **description** *(string) --*

          A description of the bot alias.

        - **botVersion** *(string) --*

          The version of the Amazon Lex bot to which the alias points.

        - **botName** *(string) --*

          The name of the bot to which the alias points.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot alias was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot alias was created.

        - **checksum** *(string) --*

          Checksum of the bot alias.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetBotChannelAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotChannelAssociationsPaginatePaginationConfigTypeDef(
    _GetBotChannelAssociationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBotChannelAssociationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": str,
        "botConfiguration": Dict[str, str],
        "status": str,
        "failureReason": str,
    },
    total=False,
)


class GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef(
    _GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef
):
    """
    Type definition for `GetBotChannelAssociationsPaginateResponse` `botChannelAssociations`

    Represents an association between an Amazon Lex bot and an external messaging platform.

    - **name** *(string) --*

      The name of the association between the bot and the channel.

    - **description** *(string) --*

      A text description of the association you are creating.

    - **botAlias** *(string) --*

      An alias pointing to the specific version of the Amazon Lex bot to which this association
      is being made.

    - **botName** *(string) --*

      The name of the Amazon Lex bot to which this association is being made.

      .. note::

        Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.

    - **createdDate** *(datetime) --*

      The date that the association between the Amazon Lex bot and the channel was created.

    - **type** *(string) --*

      Specifies the type of association by indicating the type of channel being established
      between the Amazon Lex bot and the external messaging platform.

    - **botConfiguration** *(dict) --*

      Provides information necessary to communicate with the messaging platform.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the bot channel.

      * ``CREATED`` - The channel has been created and is ready for use.

      * ``IN_PROGRESS`` - Channel creation is in progress.

      * ``FAILED`` - There was an error creating the channel. For information about the reason
      for the failure, see the ``failureReason`` field.

    - **failureReason** *(string) --*

      If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the
      association.
    """


_GetBotChannelAssociationsPaginateResponseTypeDef = TypedDict(
    "_GetBotChannelAssociationsPaginateResponseTypeDef",
    {
        "botChannelAssociations": List[
            GetBotChannelAssociationsPaginateResponsebotChannelAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetBotChannelAssociationsPaginateResponseTypeDef(
    _GetBotChannelAssociationsPaginateResponseTypeDef
):
    """
    Type definition for `GetBotChannelAssociationsPaginate` `Response`

    - **botChannelAssociations** *(list) --*

      An array of objects, one for each association, that provides information about the Amazon Lex
      bot and its association with the channel.

      - *(dict) --*

        Represents an association between an Amazon Lex bot and an external messaging platform.

        - **name** *(string) --*

          The name of the association between the bot and the channel.

        - **description** *(string) --*

          A text description of the association you are creating.

        - **botAlias** *(string) --*

          An alias pointing to the specific version of the Amazon Lex bot to which this association
          is being made.

        - **botName** *(string) --*

          The name of the Amazon Lex bot to which this association is being made.

          .. note::

            Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.

        - **createdDate** *(datetime) --*

          The date that the association between the Amazon Lex bot and the channel was created.

        - **type** *(string) --*

          Specifies the type of association by indicating the type of channel being established
          between the Amazon Lex bot and the external messaging platform.

        - **botConfiguration** *(dict) --*

          Provides information necessary to communicate with the messaging platform.

          - *(string) --*

            - *(string) --*

        - **status** *(string) --*

          The status of the bot channel.

          * ``CREATED`` - The channel has been created and is ready for use.

          * ``IN_PROGRESS`` - Channel creation is in progress.

          * ``FAILED`` - There was an error creating the channel. For information about the reason
          for the failure, see the ``failureReason`` field.

        - **failureReason** *(string) --*

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the
          association.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetBotVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotVersionsPaginatePaginationConfigTypeDef(
    _GetBotVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBotVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBotVersionsPaginateResponsebotsTypeDef = TypedDict(
    "_GetBotVersionsPaginateResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetBotVersionsPaginateResponsebotsTypeDef(
    _GetBotVersionsPaginateResponsebotsTypeDef
):
    """
    Type definition for `GetBotVersionsPaginateResponse` `bots`

    Provides information about a bot. .

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **status** *(string) --*

      The status of the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a bot, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .
    """


_GetBotVersionsPaginateResponseTypeDef = TypedDict(
    "_GetBotVersionsPaginateResponseTypeDef",
    {"bots": List[GetBotVersionsPaginateResponsebotsTypeDef], "NextToken": str},
    total=False,
)


class GetBotVersionsPaginateResponseTypeDef(_GetBotVersionsPaginateResponseTypeDef):
    """
    Type definition for `GetBotVersionsPaginate` `Response`

    - **bots** *(list) --*

      An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for
      the ``$LATEST`` version.

      - *(dict) --*

        Provides information about a bot. .

        - **name** *(string) --*

          The name of the bot.

        - **description** *(string) --*

          A description of the bot.

        - **status** *(string) --*

          The status of the bot.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot was updated. When you create a bot, the creation date and last
          updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot was created.

        - **version** *(string) --*

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetBotsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBotsPaginatePaginationConfigTypeDef(_GetBotsPaginatePaginationConfigTypeDef):
    """
    Type definition for `GetBotsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBotsPaginateResponsebotsTypeDef = TypedDict(
    "_GetBotsPaginateResponsebotsTypeDef",
    {
        "name": str,
        "description": str,
        "status": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetBotsPaginateResponsebotsTypeDef(_GetBotsPaginateResponsebotsTypeDef):
    """
    Type definition for `GetBotsPaginateResponse` `bots`

    Provides information about a bot. .

    - **name** *(string) --*

      The name of the bot.

    - **description** *(string) --*

      A description of the bot.

    - **status** *(string) --*

      The status of the bot.

    - **lastUpdatedDate** *(datetime) --*

      The date that the bot was updated. When you create a bot, the creation date and last
      updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the bot was created.

    - **version** *(string) --*

      The version of the bot. For a new bot, the version is always ``$LATEST`` .
    """


_GetBotsPaginateResponseTypeDef = TypedDict(
    "_GetBotsPaginateResponseTypeDef",
    {"bots": List[GetBotsPaginateResponsebotsTypeDef], "NextToken": str},
    total=False,
)


class GetBotsPaginateResponseTypeDef(_GetBotsPaginateResponseTypeDef):
    """
    Type definition for `GetBotsPaginate` `Response`

    - **bots** *(list) --*

      An array of ``botMetadata`` objects, with one entry for each bot.

      - *(dict) --*

        Provides information about a bot. .

        - **name** *(string) --*

          The name of the bot.

        - **description** *(string) --*

          A description of the bot.

        - **status** *(string) --*

          The status of the bot.

        - **lastUpdatedDate** *(datetime) --*

          The date that the bot was updated. When you create a bot, the creation date and last
          updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the bot was created.

        - **version** *(string) --*

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetBuiltinIntentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBuiltinIntentsPaginatePaginationConfigTypeDef(
    _GetBuiltinIntentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBuiltinIntentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBuiltinIntentsPaginateResponseintentsTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginateResponseintentsTypeDef",
    {"signature": str, "supportedLocales": List[str]},
    total=False,
)


class GetBuiltinIntentsPaginateResponseintentsTypeDef(
    _GetBuiltinIntentsPaginateResponseintentsTypeDef
):
    """
    Type definition for `GetBuiltinIntentsPaginateResponse` `intents`

    Provides metadata for a built-in intent.

    - **signature** *(string) --*

      A unique identifier for the built-in intent. To find the signature for an intent, see
      `Standard Built-in Intents
      <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
      in the *Alexa Skills Kit* .

    - **supportedLocales** *(list) --*

      A list of identifiers for the locales that the intent supports.

      - *(string) --*
    """


_GetBuiltinIntentsPaginateResponseTypeDef = TypedDict(
    "_GetBuiltinIntentsPaginateResponseTypeDef",
    {
        "intents": List[GetBuiltinIntentsPaginateResponseintentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetBuiltinIntentsPaginateResponseTypeDef(
    _GetBuiltinIntentsPaginateResponseTypeDef
):
    """
    Type definition for `GetBuiltinIntentsPaginate` `Response`

    - **intents** *(list) --*

      An array of ``builtinIntentMetadata`` objects, one for each intent in the response.

      - *(dict) --*

        Provides metadata for a built-in intent.

        - **signature** *(string) --*

          A unique identifier for the built-in intent. To find the signature for an intent, see
          `Standard Built-in Intents
          <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__
          in the *Alexa Skills Kit* .

        - **supportedLocales** *(list) --*

          A list of identifiers for the locales that the intent supports.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetBuiltinSlotTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBuiltinSlotTypesPaginatePaginationConfigTypeDef(
    _GetBuiltinSlotTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetBuiltinSlotTypesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef",
    {"signature": str, "supportedLocales": List[str]},
    total=False,
)


class GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef(
    _GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef
):
    """
    Type definition for `GetBuiltinSlotTypesPaginateResponse` `slotTypes`

    Provides information about a built in slot type.

    - **signature** *(string) --*

      A unique identifier for the built-in slot type. To find the signature for a slot type,
      see `Slot Type Reference
      <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
      in the *Alexa Skills Kit* .

    - **supportedLocales** *(list) --*

      A list of target locales for the slot.

      - *(string) --*
    """


_GetBuiltinSlotTypesPaginateResponseTypeDef = TypedDict(
    "_GetBuiltinSlotTypesPaginateResponseTypeDef",
    {
        "slotTypes": List[GetBuiltinSlotTypesPaginateResponseslotTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetBuiltinSlotTypesPaginateResponseTypeDef(
    _GetBuiltinSlotTypesPaginateResponseTypeDef
):
    """
    Type definition for `GetBuiltinSlotTypesPaginate` `Response`

    - **slotTypes** *(list) --*

      An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.

      - *(dict) --*

        Provides information about a built in slot type.

        - **signature** *(string) --*

          A unique identifier for the built-in slot type. To find the signature for a slot type,
          see `Slot Type Reference
          <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__
          in the *Alexa Skills Kit* .

        - **supportedLocales** *(list) --*

          A list of target locales for the slot.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetIntentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntentVersionsPaginatePaginationConfigTypeDef(
    _GetIntentVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetIntentVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetIntentVersionsPaginateResponseintentsTypeDef = TypedDict(
    "_GetIntentVersionsPaginateResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetIntentVersionsPaginateResponseintentsTypeDef(
    _GetIntentVersionsPaginateResponseintentsTypeDef
):
    """
    Type definition for `GetIntentVersionsPaginateResponse` `intents`

    Provides information about an intent.

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create an intent, the creation date and
      last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent.
    """


_GetIntentVersionsPaginateResponseTypeDef = TypedDict(
    "_GetIntentVersionsPaginateResponseTypeDef",
    {
        "intents": List[GetIntentVersionsPaginateResponseintentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetIntentVersionsPaginateResponseTypeDef(
    _GetIntentVersionsPaginateResponseTypeDef
):
    """
    Type definition for `GetIntentVersionsPaginate` `Response`

    - **intents** *(list) --*

      An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one
      for the ``$LATEST`` version.

      - *(dict) --*

        Provides information about an intent.

        - **name** *(string) --*

          The name of the intent.

        - **description** *(string) --*

          A description of the intent.

        - **lastUpdatedDate** *(datetime) --*

          The date that the intent was updated. When you create an intent, the creation date and
          last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the intent was created.

        - **version** *(string) --*

          The version of the intent.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetIntentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntentsPaginatePaginationConfigTypeDef(
    _GetIntentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetIntentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetIntentsPaginateResponseintentsTypeDef = TypedDict(
    "_GetIntentsPaginateResponseintentsTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetIntentsPaginateResponseintentsTypeDef(
    _GetIntentsPaginateResponseintentsTypeDef
):
    """
    Type definition for `GetIntentsPaginateResponse` `intents`

    Provides information about an intent.

    - **name** *(string) --*

      The name of the intent.

    - **description** *(string) --*

      A description of the intent.

    - **lastUpdatedDate** *(datetime) --*

      The date that the intent was updated. When you create an intent, the creation date and
      last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the intent was created.

    - **version** *(string) --*

      The version of the intent.
    """


_GetIntentsPaginateResponseTypeDef = TypedDict(
    "_GetIntentsPaginateResponseTypeDef",
    {"intents": List[GetIntentsPaginateResponseintentsTypeDef], "NextToken": str},
    total=False,
)


class GetIntentsPaginateResponseTypeDef(_GetIntentsPaginateResponseTypeDef):
    """
    Type definition for `GetIntentsPaginate` `Response`

    - **intents** *(list) --*

      An array of ``Intent`` objects. For more information, see  PutBot .

      - *(dict) --*

        Provides information about an intent.

        - **name** *(string) --*

          The name of the intent.

        - **description** *(string) --*

          A description of the intent.

        - **lastUpdatedDate** *(datetime) --*

          The date that the intent was updated. When you create an intent, the creation date and
          last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the intent was created.

        - **version** *(string) --*

          The version of the intent.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetSlotTypeVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSlotTypeVersionsPaginatePaginationConfigTypeDef(
    _GetSlotTypeVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSlotTypeVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetSlotTypeVersionsPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginateResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetSlotTypeVersionsPaginateResponseslotTypesTypeDef(
    _GetSlotTypeVersionsPaginateResponseslotTypesTypeDef
):
    """
    Type definition for `GetSlotTypeVersionsPaginateResponse` `slotTypes`

    Provides information about a slot type..

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type.
    """


_GetSlotTypeVersionsPaginateResponseTypeDef = TypedDict(
    "_GetSlotTypeVersionsPaginateResponseTypeDef",
    {
        "slotTypes": List[GetSlotTypeVersionsPaginateResponseslotTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetSlotTypeVersionsPaginateResponseTypeDef(
    _GetSlotTypeVersionsPaginateResponseTypeDef
):
    """
    Type definition for `GetSlotTypeVersionsPaginate` `Response`

    - **slotTypes** *(list) --*

      An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type plus
      one for the ``$LATEST`` version.

      - *(dict) --*

        Provides information about a slot type..

        - **name** *(string) --*

          The name of the slot type.

        - **description** *(string) --*

          A description of the slot type.

        - **lastUpdatedDate** *(datetime) --*

          The date that the slot type was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the slot type was created.

        - **version** *(string) --*

          The version of the slot type.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetSlotTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSlotTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSlotTypesPaginatePaginationConfigTypeDef(
    _GetSlotTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSlotTypesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetSlotTypesPaginateResponseslotTypesTypeDef = TypedDict(
    "_GetSlotTypesPaginateResponseslotTypesTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)


class GetSlotTypesPaginateResponseslotTypesTypeDef(
    _GetSlotTypesPaginateResponseslotTypesTypeDef
):
    """
    Type definition for `GetSlotTypesPaginateResponse` `slotTypes`

    Provides information about a slot type..

    - **name** *(string) --*

      The name of the slot type.

    - **description** *(string) --*

      A description of the slot type.

    - **lastUpdatedDate** *(datetime) --*

      The date that the slot type was updated. When you create a resource, the creation date
      and last updated date are the same.

    - **createdDate** *(datetime) --*

      The date that the slot type was created.

    - **version** *(string) --*

      The version of the slot type.
    """


_GetSlotTypesPaginateResponseTypeDef = TypedDict(
    "_GetSlotTypesPaginateResponseTypeDef",
    {"slotTypes": List[GetSlotTypesPaginateResponseslotTypesTypeDef], "NextToken": str},
    total=False,
)


class GetSlotTypesPaginateResponseTypeDef(_GetSlotTypesPaginateResponseTypeDef):
    """
    Type definition for `GetSlotTypesPaginate` `Response`

    - **slotTypes** *(list) --*

      An array of objects, one for each slot type, that provides information such as the name of
      the slot type, the version, and a description.

      - *(dict) --*

        Provides information about a slot type..

        - **name** *(string) --*

          The name of the slot type.

        - **description** *(string) --*

          A description of the slot type.

        - **lastUpdatedDate** *(datetime) --*

          The date that the slot type was updated. When you create a resource, the creation date
          and last updated date are the same.

        - **createdDate** *(datetime) --*

          The date that the slot type was created.

        - **version** *(string) --*

          The version of the slot type.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
