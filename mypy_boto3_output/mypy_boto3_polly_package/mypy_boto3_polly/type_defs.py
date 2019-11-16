"Main interface for polly type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeVoicesResponseVoicesTypeDef",
    "ClientDescribeVoicesResponseTypeDef",
    "ClientGetLexiconResponseLexiconAttributesTypeDef",
    "ClientGetLexiconResponseLexiconTypeDef",
    "ClientGetLexiconResponseTypeDef",
    "ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    "ClientGetSpeechSynthesisTaskResponseTypeDef",
    "ClientListLexiconsResponseLexiconsAttributesTypeDef",
    "ClientListLexiconsResponseLexiconsTypeDef",
    "ClientListLexiconsResponseTypeDef",
    "ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef",
    "ClientListSpeechSynthesisTasksResponseTypeDef",
    "ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    "ClientStartSpeechSynthesisTaskResponseTypeDef",
    "ClientSynthesizeSpeechResponseTypeDef",
    "DescribeVoicesPaginatePaginationConfigTypeDef",
    "DescribeVoicesPaginateResponseVoicesTypeDef",
    "DescribeVoicesPaginateResponseTypeDef",
    "ListLexiconsPaginatePaginationConfigTypeDef",
    "ListLexiconsPaginateResponseLexiconsAttributesTypeDef",
    "ListLexiconsPaginateResponseLexiconsTypeDef",
    "ListLexiconsPaginateResponseTypeDef",
    "ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef",
    "ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef",
    "ListSpeechSynthesisTasksPaginateResponseTypeDef",
)


_ClientDescribeVoicesResponseVoicesTypeDef = TypedDict(
    "_ClientDescribeVoicesResponseVoicesTypeDef",
    {
        "Gender": str,
        "Id": str,
        "LanguageCode": str,
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[str],
        "SupportedEngines": List[str],
    },
    total=False,
)


class ClientDescribeVoicesResponseVoicesTypeDef(
    _ClientDescribeVoicesResponseVoicesTypeDef
):
    """
    Type definition for `ClientDescribeVoicesResponse` `Voices`

    Description of the voice.

    - **Gender** *(string) --*

      Gender of the voice.

    - **Id** *(string) --*

      Amazon Polly assigned voice ID. This is the ID that you specify when calling the
      ``SynthesizeSpeech`` operation.

    - **LanguageCode** *(string) --*

      Language code of the voice.

    - **LanguageName** *(string) --*

      Human readable name of the language in English.

    - **Name** *(string) --*

      Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable
      voice name that you might display in your application.

    - **AdditionalLanguageCodes** *(list) --*

      Additional codes for languages available for the specified voice in addition to its
      default language.

      For example, the default language for Aditi is Indian English (en-IN) because it was
      first used for that language. Since Aditi is bilingual and fluent in both Indian English
      and Hindi, this parameter would show the code ``hi-IN`` .

      - *(string) --*

    - **SupportedEngines** *(list) --*

      Specifies which engines (``standard`` or ``neural`` ) that are supported by a given voice.

      - *(string) --*
    """


_ClientDescribeVoicesResponseTypeDef = TypedDict(
    "_ClientDescribeVoicesResponseTypeDef",
    {"Voices": List[ClientDescribeVoicesResponseVoicesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeVoicesResponseTypeDef(_ClientDescribeVoicesResponseTypeDef):
    """
    Type definition for `ClientDescribeVoices` `Response`

    - **Voices** *(list) --*

      A list of voices with their properties.

      - *(dict) --*

        Description of the voice.

        - **Gender** *(string) --*

          Gender of the voice.

        - **Id** *(string) --*

          Amazon Polly assigned voice ID. This is the ID that you specify when calling the
          ``SynthesizeSpeech`` operation.

        - **LanguageCode** *(string) --*

          Language code of the voice.

        - **LanguageName** *(string) --*

          Human readable name of the language in English.

        - **Name** *(string) --*

          Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable
          voice name that you might display in your application.

        - **AdditionalLanguageCodes** *(list) --*

          Additional codes for languages available for the specified voice in addition to its
          default language.

          For example, the default language for Aditi is Indian English (en-IN) because it was
          first used for that language. Since Aditi is bilingual and fluent in both Indian English
          and Hindi, this parameter would show the code ``hi-IN`` .

          - *(string) --*

        - **SupportedEngines** *(list) --*

          Specifies which engines (``standard`` or ``neural`` ) that are supported by a given voice.

          - *(string) --*

    - **NextToken** *(string) --*

      The pagination token to use in the next request to continue the listing of voices.
      ``NextToken`` is returned only if the response is truncated.
    """


_ClientGetLexiconResponseLexiconAttributesTypeDef = TypedDict(
    "_ClientGetLexiconResponseLexiconAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": str,
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ClientGetLexiconResponseLexiconAttributesTypeDef(
    _ClientGetLexiconResponseLexiconAttributesTypeDef
):
    """
    Type definition for `ClientGetLexiconResponse` `LexiconAttributes`

    Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN,
    number of lexemes defined in the lexicon, and size of lexicon in bytes.

    - **Alphabet** *(string) --*

      Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

    - **LanguageCode** *(string) --*

      Language code that the lexicon applies to. A lexicon with a language code such as "en"
      would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

    - **LastModified** *(datetime) --*

      Date lexicon was last modified (a timestamp value).

    - **LexiconArn** *(string) --*

      Amazon Resource Name (ARN) of the lexicon.

    - **LexemesCount** *(integer) --*

      Number of lexemes in the lexicon.

    - **Size** *(integer) --*

      Total size of the lexicon, in characters.
    """


_ClientGetLexiconResponseLexiconTypeDef = TypedDict(
    "_ClientGetLexiconResponseLexiconTypeDef",
    {"Content": str, "Name": str},
    total=False,
)


class ClientGetLexiconResponseLexiconTypeDef(_ClientGetLexiconResponseLexiconTypeDef):
    """
    Type definition for `ClientGetLexiconResponse` `Lexicon`

    Lexicon object that provides name and the string content of the lexicon.

    - **Content** *(string) --*

      Lexicon content in string format. The content of a lexicon must be in PLS format.

    - **Name** *(string) --*

      Name of the lexicon.
    """


_ClientGetLexiconResponseTypeDef = TypedDict(
    "_ClientGetLexiconResponseTypeDef",
    {
        "Lexicon": ClientGetLexiconResponseLexiconTypeDef,
        "LexiconAttributes": ClientGetLexiconResponseLexiconAttributesTypeDef,
    },
    total=False,
)


class ClientGetLexiconResponseTypeDef(_ClientGetLexiconResponseTypeDef):
    """
    Type definition for `ClientGetLexicon` `Response`

    - **Lexicon** *(dict) --*

      Lexicon object that provides name and the string content of the lexicon.

      - **Content** *(string) --*

        Lexicon content in string format. The content of a lexicon must be in PLS format.

      - **Name** *(string) --*

        Name of the lexicon.

    - **LexiconAttributes** *(dict) --*

      Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN,
      number of lexemes defined in the lexicon, and size of lexicon in bytes.

      - **Alphabet** *(string) --*

        Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

      - **LanguageCode** *(string) --*

        Language code that the lexicon applies to. A lexicon with a language code such as "en"
        would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

      - **LastModified** *(datetime) --*

        Date lexicon was last modified (a timestamp value).

      - **LexiconArn** *(string) --*

        Amazon Resource Name (ARN) of the lexicon.

      - **LexemesCount** *(integer) --*

        Number of lexemes in the lexicon.

      - **Size** *(integer) --*

        Total size of the lexicon, in characters.
    """


_ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef = TypedDict(
    "_ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    {
        "Engine": str,
        "TaskId": str,
        "TaskStatus": str,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": str,
        "SampleRate": str,
        "SpeechMarkTypes": List[str],
        "TextType": str,
        "VoiceId": str,
        "LanguageCode": str,
    },
    total=False,
)


class ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef(
    _ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef
):
    """
    Type definition for `ClientGetSpeechSynthesisTaskResponse` `SynthesisTask`

    SynthesisTask object that provides information from the requested task, including output
    format, creation time, task status, and so on.

    - **Engine** *(string) --*

      Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
      input text for speech synthesis. Using a voice that is not supported for the engine
      selected will result in an error.

    - **TaskId** *(string) --*

      The Amazon Polly generated identifier for a speech synthesis task.

    - **TaskStatus** *(string) --*

      Current status of the individual speech synthesis task.

    - **TaskStatusReason** *(string) --*

      Reason for the current status of a specific speech synthesis task, including errors if the
      task has failed.

    - **OutputUri** *(string) --*

      Pathway for the output speech file.

    - **CreationTime** *(datetime) --*

      Timestamp for the time the synthesis task was started.

    - **RequestCharacters** *(integer) --*

      Number of billable characters synthesized.

    - **SnsTopicArn** *(string) --*

      ARN for the SNS topic optionally used for providing status notification for a speech
      synthesis task.

    - **LexiconNames** *(list) --*

      List of one or more pronunciation lexicon names you want the service to apply during
      synthesis. Lexicons are applied only if the language of the lexicon is the same as the
      language of the voice.

      - *(string) --*

    - **OutputFormat** *(string) --*

      The format in which the returned output will be encoded. For audio stream, this will be
      mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

    - **SampleRate** *(string) --*

      The audio frequency specified in Hz.

      The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
      default value for standard voices is "22050". The default value for neural voices is
      "24000".

      Valid values for pcm are "8000" and "16000" The default value is "16000".

    - **SpeechMarkTypes** *(list) --*

      The type of speech marks returned for the input text.

      - *(string) --*

    - **TextType** *(string) --*

      Specifies whether the input text is plain text or SSML. The default value is plain text.

    - **VoiceId** *(string) --*

      Voice ID to use for the synthesis.

    - **LanguageCode** *(string) --*

      Optional language code for a synthesis task. This is only necessary if using a bilingual
      voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

      If a bilingual voice is used and no language code is specified, Amazon Polly will use the
      default language of the bilingual voice. The default language for any voice is the one
      returned by the `DescribeVoices
      <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
      ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
      Indian English rather than Hindi.
    """


_ClientGetSpeechSynthesisTaskResponseTypeDef = TypedDict(
    "_ClientGetSpeechSynthesisTaskResponseTypeDef",
    {"SynthesisTask": ClientGetSpeechSynthesisTaskResponseSynthesisTaskTypeDef},
    total=False,
)


class ClientGetSpeechSynthesisTaskResponseTypeDef(
    _ClientGetSpeechSynthesisTaskResponseTypeDef
):
    """
    Type definition for `ClientGetSpeechSynthesisTask` `Response`

    - **SynthesisTask** *(dict) --*

      SynthesisTask object that provides information from the requested task, including output
      format, creation time, task status, and so on.

      - **Engine** *(string) --*

        Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
        input text for speech synthesis. Using a voice that is not supported for the engine
        selected will result in an error.

      - **TaskId** *(string) --*

        The Amazon Polly generated identifier for a speech synthesis task.

      - **TaskStatus** *(string) --*

        Current status of the individual speech synthesis task.

      - **TaskStatusReason** *(string) --*

        Reason for the current status of a specific speech synthesis task, including errors if the
        task has failed.

      - **OutputUri** *(string) --*

        Pathway for the output speech file.

      - **CreationTime** *(datetime) --*

        Timestamp for the time the synthesis task was started.

      - **RequestCharacters** *(integer) --*

        Number of billable characters synthesized.

      - **SnsTopicArn** *(string) --*

        ARN for the SNS topic optionally used for providing status notification for a speech
        synthesis task.

      - **LexiconNames** *(list) --*

        List of one or more pronunciation lexicon names you want the service to apply during
        synthesis. Lexicons are applied only if the language of the lexicon is the same as the
        language of the voice.

        - *(string) --*

      - **OutputFormat** *(string) --*

        The format in which the returned output will be encoded. For audio stream, this will be
        mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

      - **SampleRate** *(string) --*

        The audio frequency specified in Hz.

        The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
        default value for standard voices is "22050". The default value for neural voices is
        "24000".

        Valid values for pcm are "8000" and "16000" The default value is "16000".

      - **SpeechMarkTypes** *(list) --*

        The type of speech marks returned for the input text.

        - *(string) --*

      - **TextType** *(string) --*

        Specifies whether the input text is plain text or SSML. The default value is plain text.

      - **VoiceId** *(string) --*

        Voice ID to use for the synthesis.

      - **LanguageCode** *(string) --*

        Optional language code for a synthesis task. This is only necessary if using a bilingual
        voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

        If a bilingual voice is used and no language code is specified, Amazon Polly will use the
        default language of the bilingual voice. The default language for any voice is the one
        returned by the `DescribeVoices
        <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
        ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
        Indian English rather than Hindi.
    """


_ClientListLexiconsResponseLexiconsAttributesTypeDef = TypedDict(
    "_ClientListLexiconsResponseLexiconsAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": str,
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ClientListLexiconsResponseLexiconsAttributesTypeDef(
    _ClientListLexiconsResponseLexiconsAttributesTypeDef
):
    """
    Type definition for `ClientListLexiconsResponseLexicons` `Attributes`

    Provides lexicon metadata.

    - **Alphabet** *(string) --*

      Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

    - **LanguageCode** *(string) --*

      Language code that the lexicon applies to. A lexicon with a language code such as "en"
      would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

    - **LastModified** *(datetime) --*

      Date lexicon was last modified (a timestamp value).

    - **LexiconArn** *(string) --*

      Amazon Resource Name (ARN) of the lexicon.

    - **LexemesCount** *(integer) --*

      Number of lexemes in the lexicon.

    - **Size** *(integer) --*

      Total size of the lexicon, in characters.
    """


_ClientListLexiconsResponseLexiconsTypeDef = TypedDict(
    "_ClientListLexiconsResponseLexiconsTypeDef",
    {"Name": str, "Attributes": ClientListLexiconsResponseLexiconsAttributesTypeDef},
    total=False,
)


class ClientListLexiconsResponseLexiconsTypeDef(
    _ClientListLexiconsResponseLexiconsTypeDef
):
    """
    Type definition for `ClientListLexiconsResponse` `Lexicons`

    Describes the content of the lexicon.

    - **Name** *(string) --*

      Name of the lexicon.

    - **Attributes** *(dict) --*

      Provides lexicon metadata.

      - **Alphabet** *(string) --*

        Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

      - **LanguageCode** *(string) --*

        Language code that the lexicon applies to. A lexicon with a language code such as "en"
        would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

      - **LastModified** *(datetime) --*

        Date lexicon was last modified (a timestamp value).

      - **LexiconArn** *(string) --*

        Amazon Resource Name (ARN) of the lexicon.

      - **LexemesCount** *(integer) --*

        Number of lexemes in the lexicon.

      - **Size** *(integer) --*

        Total size of the lexicon, in characters.
    """


_ClientListLexiconsResponseTypeDef = TypedDict(
    "_ClientListLexiconsResponseTypeDef",
    {"Lexicons": List[ClientListLexiconsResponseLexiconsTypeDef], "NextToken": str},
    total=False,
)


class ClientListLexiconsResponseTypeDef(_ClientListLexiconsResponseTypeDef):
    """
    Type definition for `ClientListLexicons` `Response`

    - **Lexicons** *(list) --*

      A list of lexicon names and attributes.

      - *(dict) --*

        Describes the content of the lexicon.

        - **Name** *(string) --*

          Name of the lexicon.

        - **Attributes** *(dict) --*

          Provides lexicon metadata.

          - **Alphabet** *(string) --*

            Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

          - **LanguageCode** *(string) --*

            Language code that the lexicon applies to. A lexicon with a language code such as "en"
            would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

          - **LastModified** *(datetime) --*

            Date lexicon was last modified (a timestamp value).

          - **LexiconArn** *(string) --*

            Amazon Resource Name (ARN) of the lexicon.

          - **LexemesCount** *(integer) --*

            Number of lexemes in the lexicon.

          - **Size** *(integer) --*

            Total size of the lexicon, in characters.

    - **NextToken** *(string) --*

      The pagination token to use in the next request to continue the listing of lexicons.
      ``NextToken`` is returned only if the response is truncated.
    """


_ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef = TypedDict(
    "_ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef",
    {
        "Engine": str,
        "TaskId": str,
        "TaskStatus": str,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": str,
        "SampleRate": str,
        "SpeechMarkTypes": List[str],
        "TextType": str,
        "VoiceId": str,
        "LanguageCode": str,
    },
    total=False,
)


class ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef(
    _ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef
):
    """
    Type definition for `ClientListSpeechSynthesisTasksResponse` `SynthesisTasks`

    SynthesisTask object that provides information about a speech synthesis task.

    - **Engine** *(string) --*

      Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
      processing input text for speech synthesis. Using a voice that is not supported for the
      engine selected will result in an error.

    - **TaskId** *(string) --*

      The Amazon Polly generated identifier for a speech synthesis task.

    - **TaskStatus** *(string) --*

      Current status of the individual speech synthesis task.

    - **TaskStatusReason** *(string) --*

      Reason for the current status of a specific speech synthesis task, including errors if
      the task has failed.

    - **OutputUri** *(string) --*

      Pathway for the output speech file.

    - **CreationTime** *(datetime) --*

      Timestamp for the time the synthesis task was started.

    - **RequestCharacters** *(integer) --*

      Number of billable characters synthesized.

    - **SnsTopicArn** *(string) --*

      ARN for the SNS topic optionally used for providing status notification for a speech
      synthesis task.

    - **LexiconNames** *(list) --*

      List of one or more pronunciation lexicon names you want the service to apply during
      synthesis. Lexicons are applied only if the language of the lexicon is the same as the
      language of the voice.

      - *(string) --*

    - **OutputFormat** *(string) --*

      The format in which the returned output will be encoded. For audio stream, this will be
      mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

    - **SampleRate** *(string) --*

      The audio frequency specified in Hz.

      The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
      default value for standard voices is "22050". The default value for neural voices is
      "24000".

      Valid values for pcm are "8000" and "16000" The default value is "16000".

    - **SpeechMarkTypes** *(list) --*

      The type of speech marks returned for the input text.

      - *(string) --*

    - **TextType** *(string) --*

      Specifies whether the input text is plain text or SSML. The default value is plain text.

    - **VoiceId** *(string) --*

      Voice ID to use for the synthesis.

    - **LanguageCode** *(string) --*

      Optional language code for a synthesis task. This is only necessary if using a bilingual
      voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi
      (hi-IN).

      If a bilingual voice is used and no language code is specified, Amazon Polly will use the
      default language of the bilingual voice. The default language for any voice is the one
      returned by the `DescribeVoices
      <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for
      the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will
      use Indian English rather than Hindi.
    """


_ClientListSpeechSynthesisTasksResponseTypeDef = TypedDict(
    "_ClientListSpeechSynthesisTasksResponseTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List[
            ClientListSpeechSynthesisTasksResponseSynthesisTasksTypeDef
        ],
    },
    total=False,
)


class ClientListSpeechSynthesisTasksResponseTypeDef(
    _ClientListSpeechSynthesisTasksResponseTypeDef
):
    """
    Type definition for `ClientListSpeechSynthesisTasks` `Response`

    - **NextToken** *(string) --*

      An opaque pagination token returned from the previous List operation in this request. If
      present, this indicates where to continue the listing.

    - **SynthesisTasks** *(list) --*

      List of SynthesisTask objects that provides information from the specified task in the list
      request, including output format, creation time, task status, and so on.

      - *(dict) --*

        SynthesisTask object that provides information about a speech synthesis task.

        - **Engine** *(string) --*

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
          processing input text for speech synthesis. Using a voice that is not supported for the
          engine selected will result in an error.

        - **TaskId** *(string) --*

          The Amazon Polly generated identifier for a speech synthesis task.

        - **TaskStatus** *(string) --*

          Current status of the individual speech synthesis task.

        - **TaskStatusReason** *(string) --*

          Reason for the current status of a specific speech synthesis task, including errors if
          the task has failed.

        - **OutputUri** *(string) --*

          Pathway for the output speech file.

        - **CreationTime** *(datetime) --*

          Timestamp for the time the synthesis task was started.

        - **RequestCharacters** *(integer) --*

          Number of billable characters synthesized.

        - **SnsTopicArn** *(string) --*

          ARN for the SNS topic optionally used for providing status notification for a speech
          synthesis task.

        - **LexiconNames** *(list) --*

          List of one or more pronunciation lexicon names you want the service to apply during
          synthesis. Lexicons are applied only if the language of the lexicon is the same as the
          language of the voice.

          - *(string) --*

        - **OutputFormat** *(string) --*

          The format in which the returned output will be encoded. For audio stream, this will be
          mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

        - **SampleRate** *(string) --*

          The audio frequency specified in Hz.

          The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
          default value for standard voices is "22050". The default value for neural voices is
          "24000".

          Valid values for pcm are "8000" and "16000" The default value is "16000".

        - **SpeechMarkTypes** *(list) --*

          The type of speech marks returned for the input text.

          - *(string) --*

        - **TextType** *(string) --*

          Specifies whether the input text is plain text or SSML. The default value is plain text.

        - **VoiceId** *(string) --*

          Voice ID to use for the synthesis.

        - **LanguageCode** *(string) --*

          Optional language code for a synthesis task. This is only necessary if using a bilingual
          voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi
          (hi-IN).

          If a bilingual voice is used and no language code is specified, Amazon Polly will use the
          default language of the bilingual voice. The default language for any voice is the one
          returned by the `DescribeVoices
          <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for
          the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will
          use Indian English rather than Hindi.
    """


_ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef = TypedDict(
    "_ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef",
    {
        "Engine": str,
        "TaskId": str,
        "TaskStatus": str,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": str,
        "SampleRate": str,
        "SpeechMarkTypes": List[str],
        "TextType": str,
        "VoiceId": str,
        "LanguageCode": str,
    },
    total=False,
)


class ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef(
    _ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef
):
    """
    Type definition for `ClientStartSpeechSynthesisTaskResponse` `SynthesisTask`

    SynthesisTask object that provides information and attributes about a newly submitted speech
    synthesis task.

    - **Engine** *(string) --*

      Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
      input text for speech synthesis. Using a voice that is not supported for the engine
      selected will result in an error.

    - **TaskId** *(string) --*

      The Amazon Polly generated identifier for a speech synthesis task.

    - **TaskStatus** *(string) --*

      Current status of the individual speech synthesis task.

    - **TaskStatusReason** *(string) --*

      Reason for the current status of a specific speech synthesis task, including errors if the
      task has failed.

    - **OutputUri** *(string) --*

      Pathway for the output speech file.

    - **CreationTime** *(datetime) --*

      Timestamp for the time the synthesis task was started.

    - **RequestCharacters** *(integer) --*

      Number of billable characters synthesized.

    - **SnsTopicArn** *(string) --*

      ARN for the SNS topic optionally used for providing status notification for a speech
      synthesis task.

    - **LexiconNames** *(list) --*

      List of one or more pronunciation lexicon names you want the service to apply during
      synthesis. Lexicons are applied only if the language of the lexicon is the same as the
      language of the voice.

      - *(string) --*

    - **OutputFormat** *(string) --*

      The format in which the returned output will be encoded. For audio stream, this will be
      mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

    - **SampleRate** *(string) --*

      The audio frequency specified in Hz.

      The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
      default value for standard voices is "22050". The default value for neural voices is
      "24000".

      Valid values for pcm are "8000" and "16000" The default value is "16000".

    - **SpeechMarkTypes** *(list) --*

      The type of speech marks returned for the input text.

      - *(string) --*

    - **TextType** *(string) --*

      Specifies whether the input text is plain text or SSML. The default value is plain text.

    - **VoiceId** *(string) --*

      Voice ID to use for the synthesis.

    - **LanguageCode** *(string) --*

      Optional language code for a synthesis task. This is only necessary if using a bilingual
      voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

      If a bilingual voice is used and no language code is specified, Amazon Polly will use the
      default language of the bilingual voice. The default language for any voice is the one
      returned by the `DescribeVoices
      <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
      ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
      Indian English rather than Hindi.
    """


_ClientStartSpeechSynthesisTaskResponseTypeDef = TypedDict(
    "_ClientStartSpeechSynthesisTaskResponseTypeDef",
    {"SynthesisTask": ClientStartSpeechSynthesisTaskResponseSynthesisTaskTypeDef},
    total=False,
)


class ClientStartSpeechSynthesisTaskResponseTypeDef(
    _ClientStartSpeechSynthesisTaskResponseTypeDef
):
    """
    Type definition for `ClientStartSpeechSynthesisTask` `Response`

    - **SynthesisTask** *(dict) --*

      SynthesisTask object that provides information and attributes about a newly submitted speech
      synthesis task.

      - **Engine** *(string) --*

        Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when processing
        input text for speech synthesis. Using a voice that is not supported for the engine
        selected will result in an error.

      - **TaskId** *(string) --*

        The Amazon Polly generated identifier for a speech synthesis task.

      - **TaskStatus** *(string) --*

        Current status of the individual speech synthesis task.

      - **TaskStatusReason** *(string) --*

        Reason for the current status of a specific speech synthesis task, including errors if the
        task has failed.

      - **OutputUri** *(string) --*

        Pathway for the output speech file.

      - **CreationTime** *(datetime) --*

        Timestamp for the time the synthesis task was started.

      - **RequestCharacters** *(integer) --*

        Number of billable characters synthesized.

      - **SnsTopicArn** *(string) --*

        ARN for the SNS topic optionally used for providing status notification for a speech
        synthesis task.

      - **LexiconNames** *(list) --*

        List of one or more pronunciation lexicon names you want the service to apply during
        synthesis. Lexicons are applied only if the language of the lexicon is the same as the
        language of the voice.

        - *(string) --*

      - **OutputFormat** *(string) --*

        The format in which the returned output will be encoded. For audio stream, this will be
        mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

      - **SampleRate** *(string) --*

        The audio frequency specified in Hz.

        The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
        default value for standard voices is "22050". The default value for neural voices is
        "24000".

        Valid values for pcm are "8000" and "16000" The default value is "16000".

      - **SpeechMarkTypes** *(list) --*

        The type of speech marks returned for the input text.

        - *(string) --*

      - **TextType** *(string) --*

        Specifies whether the input text is plain text or SSML. The default value is plain text.

      - **VoiceId** *(string) --*

        Voice ID to use for the synthesis.

      - **LanguageCode** *(string) --*

        Optional language code for a synthesis task. This is only necessary if using a bilingual
        voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

        If a bilingual voice is used and no language code is specified, Amazon Polly will use the
        default language of the bilingual voice. The default language for any voice is the one
        returned by the `DescribeVoices
        <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for the
        ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will use
        Indian English rather than Hindi.
    """


_ClientSynthesizeSpeechResponseTypeDef = TypedDict(
    "_ClientSynthesizeSpeechResponseTypeDef",
    {"ContentType": str, "RequestCharacters": int},
    total=False,
)


class ClientSynthesizeSpeechResponseTypeDef(_ClientSynthesizeSpeechResponseTypeDef):
    """
    Type definition for `ClientSynthesizeSpeech` `Response`

    - **AudioStream** (:class:`.StreamingBody`) --

      Stream containing the synthesized speech.

    - **ContentType** *(string) --*

      Specifies the type audio stream. This should reflect the ``OutputFormat`` parameter in your
      request.

      * If you request ``mp3`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/mpeg.

      * If you request ``ogg_vorbis`` as the ``OutputFormat`` , the ``ContentType`` returned is
      audio/ogg.

      * If you request ``pcm`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/pcm
      in a signed 16-bit, 1 channel (mono), little-endian format.

      * If you request ``json`` as the ``OutputFormat`` , the ``ContentType`` returned is
      audio/json.

    - **RequestCharacters** *(integer) --*

      Number of characters synthesized.
    """


_DescribeVoicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeVoicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeVoicesPaginatePaginationConfigTypeDef(
    _DescribeVoicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeVoicesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeVoicesPaginateResponseVoicesTypeDef = TypedDict(
    "_DescribeVoicesPaginateResponseVoicesTypeDef",
    {
        "Gender": str,
        "Id": str,
        "LanguageCode": str,
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[str],
        "SupportedEngines": List[str],
    },
    total=False,
)


class DescribeVoicesPaginateResponseVoicesTypeDef(
    _DescribeVoicesPaginateResponseVoicesTypeDef
):
    """
    Type definition for `DescribeVoicesPaginateResponse` `Voices`

    Description of the voice.

    - **Gender** *(string) --*

      Gender of the voice.

    - **Id** *(string) --*

      Amazon Polly assigned voice ID. This is the ID that you specify when calling the
      ``SynthesizeSpeech`` operation.

    - **LanguageCode** *(string) --*

      Language code of the voice.

    - **LanguageName** *(string) --*

      Human readable name of the language in English.

    - **Name** *(string) --*

      Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable
      voice name that you might display in your application.

    - **AdditionalLanguageCodes** *(list) --*

      Additional codes for languages available for the specified voice in addition to its
      default language.

      For example, the default language for Aditi is Indian English (en-IN) because it was
      first used for that language. Since Aditi is bilingual and fluent in both Indian English
      and Hindi, this parameter would show the code ``hi-IN`` .

      - *(string) --*

    - **SupportedEngines** *(list) --*

      Specifies which engines (``standard`` or ``neural`` ) that are supported by a given voice.

      - *(string) --*
    """


_DescribeVoicesPaginateResponseTypeDef = TypedDict(
    "_DescribeVoicesPaginateResponseTypeDef",
    {"Voices": List[DescribeVoicesPaginateResponseVoicesTypeDef]},
    total=False,
)


class DescribeVoicesPaginateResponseTypeDef(_DescribeVoicesPaginateResponseTypeDef):
    """
    Type definition for `DescribeVoicesPaginate` `Response`

    - **Voices** *(list) --*

      A list of voices with their properties.

      - *(dict) --*

        Description of the voice.

        - **Gender** *(string) --*

          Gender of the voice.

        - **Id** *(string) --*

          Amazon Polly assigned voice ID. This is the ID that you specify when calling the
          ``SynthesizeSpeech`` operation.

        - **LanguageCode** *(string) --*

          Language code of the voice.

        - **LanguageName** *(string) --*

          Human readable name of the language in English.

        - **Name** *(string) --*

          Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable
          voice name that you might display in your application.

        - **AdditionalLanguageCodes** *(list) --*

          Additional codes for languages available for the specified voice in addition to its
          default language.

          For example, the default language for Aditi is Indian English (en-IN) because it was
          first used for that language. Since Aditi is bilingual and fluent in both Indian English
          and Hindi, this parameter would show the code ``hi-IN`` .

          - *(string) --*

        - **SupportedEngines** *(list) --*

          Specifies which engines (``standard`` or ``neural`` ) that are supported by a given voice.

          - *(string) --*
    """


_ListLexiconsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLexiconsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListLexiconsPaginatePaginationConfigTypeDef(
    _ListLexiconsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLexiconsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListLexiconsPaginateResponseLexiconsAttributesTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseLexiconsAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": str,
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)


class ListLexiconsPaginateResponseLexiconsAttributesTypeDef(
    _ListLexiconsPaginateResponseLexiconsAttributesTypeDef
):
    """
    Type definition for `ListLexiconsPaginateResponseLexicons` `Attributes`

    Provides lexicon metadata.

    - **Alphabet** *(string) --*

      Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

    - **LanguageCode** *(string) --*

      Language code that the lexicon applies to. A lexicon with a language code such as "en"
      would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

    - **LastModified** *(datetime) --*

      Date lexicon was last modified (a timestamp value).

    - **LexiconArn** *(string) --*

      Amazon Resource Name (ARN) of the lexicon.

    - **LexemesCount** *(integer) --*

      Number of lexemes in the lexicon.

    - **Size** *(integer) --*

      Total size of the lexicon, in characters.
    """


_ListLexiconsPaginateResponseLexiconsTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseLexiconsTypeDef",
    {"Name": str, "Attributes": ListLexiconsPaginateResponseLexiconsAttributesTypeDef},
    total=False,
)


class ListLexiconsPaginateResponseLexiconsTypeDef(
    _ListLexiconsPaginateResponseLexiconsTypeDef
):
    """
    Type definition for `ListLexiconsPaginateResponse` `Lexicons`

    Describes the content of the lexicon.

    - **Name** *(string) --*

      Name of the lexicon.

    - **Attributes** *(dict) --*

      Provides lexicon metadata.

      - **Alphabet** *(string) --*

        Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

      - **LanguageCode** *(string) --*

        Language code that the lexicon applies to. A lexicon with a language code such as "en"
        would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

      - **LastModified** *(datetime) --*

        Date lexicon was last modified (a timestamp value).

      - **LexiconArn** *(string) --*

        Amazon Resource Name (ARN) of the lexicon.

      - **LexemesCount** *(integer) --*

        Number of lexemes in the lexicon.

      - **Size** *(integer) --*

        Total size of the lexicon, in characters.
    """


_ListLexiconsPaginateResponseTypeDef = TypedDict(
    "_ListLexiconsPaginateResponseTypeDef",
    {"Lexicons": List[ListLexiconsPaginateResponseLexiconsTypeDef]},
    total=False,
)


class ListLexiconsPaginateResponseTypeDef(_ListLexiconsPaginateResponseTypeDef):
    """
    Type definition for `ListLexiconsPaginate` `Response`

    - **Lexicons** *(list) --*

      A list of lexicon names and attributes.

      - *(dict) --*

        Describes the content of the lexicon.

        - **Name** *(string) --*

          Name of the lexicon.

        - **Attributes** *(dict) --*

          Provides lexicon metadata.

          - **Alphabet** *(string) --*

            Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

          - **LanguageCode** *(string) --*

            Language code that the lexicon applies to. A lexicon with a language code such as "en"
            would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

          - **LastModified** *(datetime) --*

            Date lexicon was last modified (a timestamp value).

          - **LexiconArn** *(string) --*

            Amazon Resource Name (ARN) of the lexicon.

          - **LexemesCount** *(integer) --*

            Number of lexemes in the lexicon.

          - **Size** *(integer) --*

            Total size of the lexicon, in characters.
    """


_ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef(
    _ListSpeechSynthesisTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSpeechSynthesisTasksPaginate` `PaginationConfig`

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


_ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef",
    {
        "Engine": str,
        "TaskId": str,
        "TaskStatus": str,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": str,
        "SampleRate": str,
        "SpeechMarkTypes": List[str],
        "TextType": str,
        "VoiceId": str,
        "LanguageCode": str,
    },
    total=False,
)


class ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef(
    _ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef
):
    """
    Type definition for `ListSpeechSynthesisTasksPaginateResponse` `SynthesisTasks`

    SynthesisTask object that provides information about a speech synthesis task.

    - **Engine** *(string) --*

      Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
      processing input text for speech synthesis. Using a voice that is not supported for the
      engine selected will result in an error.

    - **TaskId** *(string) --*

      The Amazon Polly generated identifier for a speech synthesis task.

    - **TaskStatus** *(string) --*

      Current status of the individual speech synthesis task.

    - **TaskStatusReason** *(string) --*

      Reason for the current status of a specific speech synthesis task, including errors if
      the task has failed.

    - **OutputUri** *(string) --*

      Pathway for the output speech file.

    - **CreationTime** *(datetime) --*

      Timestamp for the time the synthesis task was started.

    - **RequestCharacters** *(integer) --*

      Number of billable characters synthesized.

    - **SnsTopicArn** *(string) --*

      ARN for the SNS topic optionally used for providing status notification for a speech
      synthesis task.

    - **LexiconNames** *(list) --*

      List of one or more pronunciation lexicon names you want the service to apply during
      synthesis. Lexicons are applied only if the language of the lexicon is the same as the
      language of the voice.

      - *(string) --*

    - **OutputFormat** *(string) --*

      The format in which the returned output will be encoded. For audio stream, this will be
      mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

    - **SampleRate** *(string) --*

      The audio frequency specified in Hz.

      The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
      default value for standard voices is "22050". The default value for neural voices is
      "24000".

      Valid values for pcm are "8000" and "16000" The default value is "16000".

    - **SpeechMarkTypes** *(list) --*

      The type of speech marks returned for the input text.

      - *(string) --*

    - **TextType** *(string) --*

      Specifies whether the input text is plain text or SSML. The default value is plain text.

    - **VoiceId** *(string) --*

      Voice ID to use for the synthesis.

    - **LanguageCode** *(string) --*

      Optional language code for a synthesis task. This is only necessary if using a bilingual
      voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi
      (hi-IN).

      If a bilingual voice is used and no language code is specified, Amazon Polly will use the
      default language of the bilingual voice. The default language for any voice is the one
      returned by the `DescribeVoices
      <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for
      the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will
      use Indian English rather than Hindi.
    """


_ListSpeechSynthesisTasksPaginateResponseTypeDef = TypedDict(
    "_ListSpeechSynthesisTasksPaginateResponseTypeDef",
    {
        "SynthesisTasks": List[
            ListSpeechSynthesisTasksPaginateResponseSynthesisTasksTypeDef
        ]
    },
    total=False,
)


class ListSpeechSynthesisTasksPaginateResponseTypeDef(
    _ListSpeechSynthesisTasksPaginateResponseTypeDef
):
    """
    Type definition for `ListSpeechSynthesisTasksPaginate` `Response`

    - **SynthesisTasks** *(list) --*

      List of SynthesisTask objects that provides information from the specified task in the list
      request, including output format, creation time, task status, and so on.

      - *(dict) --*

        SynthesisTask object that provides information about a speech synthesis task.

        - **Engine** *(string) --*

          Specifies the engine (``standard`` or ``neural`` ) for Amazon Polly to use when
          processing input text for speech synthesis. Using a voice that is not supported for the
          engine selected will result in an error.

        - **TaskId** *(string) --*

          The Amazon Polly generated identifier for a speech synthesis task.

        - **TaskStatus** *(string) --*

          Current status of the individual speech synthesis task.

        - **TaskStatusReason** *(string) --*

          Reason for the current status of a specific speech synthesis task, including errors if
          the task has failed.

        - **OutputUri** *(string) --*

          Pathway for the output speech file.

        - **CreationTime** *(datetime) --*

          Timestamp for the time the synthesis task was started.

        - **RequestCharacters** *(integer) --*

          Number of billable characters synthesized.

        - **SnsTopicArn** *(string) --*

          ARN for the SNS topic optionally used for providing status notification for a speech
          synthesis task.

        - **LexiconNames** *(list) --*

          List of one or more pronunciation lexicon names you want the service to apply during
          synthesis. Lexicons are applied only if the language of the lexicon is the same as the
          language of the voice.

          - *(string) --*

        - **OutputFormat** *(string) --*

          The format in which the returned output will be encoded. For audio stream, this will be
          mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

        - **SampleRate** *(string) --*

          The audio frequency specified in Hz.

          The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The
          default value for standard voices is "22050". The default value for neural voices is
          "24000".

          Valid values for pcm are "8000" and "16000" The default value is "16000".

        - **SpeechMarkTypes** *(list) --*

          The type of speech marks returned for the input text.

          - *(string) --*

        - **TextType** *(string) --*

          Specifies whether the input text is plain text or SSML. The default value is plain text.

        - **VoiceId** *(string) --*

          Voice ID to use for the synthesis.

        - **LanguageCode** *(string) --*

          Optional language code for a synthesis task. This is only necessary if using a bilingual
          voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi
          (hi-IN).

          If a bilingual voice is used and no language code is specified, Amazon Polly will use the
          default language of the bilingual voice. The default language for any voice is the one
          returned by the `DescribeVoices
          <https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation for
          the ``LanguageCode`` parameter. For example, if no language code is specified, Aditi will
          use Indian English rather than Hindi.
    """
