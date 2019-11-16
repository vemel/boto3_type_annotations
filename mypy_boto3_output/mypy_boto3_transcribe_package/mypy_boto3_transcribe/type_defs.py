"Main interface for transcribe type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateVocabularyResponseTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientGetTranscriptionJobResponseTypeDef",
    "ClientGetVocabularyResponseTypeDef",
    "ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    "ClientListTranscriptionJobsResponseTypeDef",
    "ClientListVocabulariesResponseVocabulariesTypeDef",
    "ClientListVocabulariesResponseTypeDef",
    "ClientStartTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientStartTranscriptionJobResponseTypeDef",
    "ClientStartTranscriptionJobSettingsTypeDef",
    "ClientUpdateVocabularyResponseTypeDef",
)


_ClientCreateVocabularyResponseTypeDef = TypedDict(
    "_ClientCreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": str,
        "VocabularyState": str,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)


class ClientCreateVocabularyResponseTypeDef(_ClientCreateVocabularyResponseTypeDef):
    """
    Type definition for `ClientCreateVocabulary` `Response`

    - **VocabularyName** *(string) --*

      The name of the vocabulary.

    - **LanguageCode** *(string) --*

      The language code of the vocabulary entries.

    - **VocabularyState** *(string) --*

      The processing state of the vocabulary. When the ``VocabularyState`` field contains ``READY``
      the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the vocabulary was created.

    - **FailureReason** *(string) --*

      If the ``VocabularyState`` field is ``FAILED`` , this field contains information about why
      the job failed.
    """


_ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef
):
    """
    Type definition for `ClientGetTranscriptionJobResponseTranscriptionJob` `Media`

    An object that describes the input media for the transcription job.

    - **MediaFileUri** *(string) --*

      The S3 location of the input media file. The URI must be in the same region as the API
      endpoint that you are calling. The general form is:

       ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

      For example:

       ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

       ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

      For more information about S3 object names, see `Object Keys
      <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
      *Amazon S3 Developer Guide* .
    """


_ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
    },
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef
):
    """
    Type definition for `ClientGetTranscriptionJobResponseTranscriptionJob` `Settings`

    Optional settings for the transcription job. Use these settings to turn on speaker
    recognition, to set the maximum number of speakers that should be identified and to specify
    a custom vocabulary to use when processing the transcription job.

    - **VocabularyName** *(string) --*

      The name of a vocabulary to use when processing the transcription job.

    - **ShowSpeakerLabels** *(boolean) --*

      Determines whether the transcription job uses speaker recognition to identify different
      speakers in the input audio. Speaker recognition labels individual speakers in the audio
      file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
      number of speaker labels ``MaxSpeakerLabels`` field.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
      request. If you set both, your request returns a ``BadRequestException`` .

    - **MaxSpeakerLabels** *(integer) --*

      The maximum number of speakers to identify in the input audio. If there are more speakers
      in the audio than this number, multiple speakers will be identified as a single speaker.
      If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
      field to true.

    - **ChannelIdentification** *(boolean) --*

      Instructs Amazon Transcribe to process each audio channel separately and then merge the
      transcription output of each channel into a single transcription.

      Amazon Transcribe also produces a transcription of each item detected on an audio
      channel, including the start time and end time of the item and alternative transcriptions
      of the item including the confidence that Amazon Transcribe has in the transcription.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
      request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef
):
    """
    Type definition for `ClientGetTranscriptionJobResponseTranscriptionJob` `Transcript`

    An object that describes the output of the transcription job.

    - **TranscriptFileUri** *(string) --*

      The location where the transcription is stored.

      Use this URI to access the transcription. If you specified an S3 bucket in the
      ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
      you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
      provides secure access to that location.
    """


_ClientGetTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": str,
        "LanguageCode": str,
        "MediaSampleRateHertz": int,
        "MediaFormat": str,
        "Media": ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
    },
    total=False,
)


class ClientGetTranscriptionJobResponseTranscriptionJobTypeDef(
    _ClientGetTranscriptionJobResponseTranscriptionJobTypeDef
):
    """
    Type definition for `ClientGetTranscriptionJobResponse` `TranscriptionJob`

    An object that contains the results of the transcription job.

    - **TranscriptionJobName** *(string) --*

      The name of the transcription job.

    - **TranscriptionJobStatus** *(string) --*

      The status of the transcription job.

    - **LanguageCode** *(string) --*

      The language code for the input speech.

    - **MediaSampleRateHertz** *(integer) --*

      The sample rate, in Hertz, of the audio track in the input media file.

    - **MediaFormat** *(string) --*

      The format of the input media file.

    - **Media** *(dict) --*

      An object that describes the input media for the transcription job.

      - **MediaFileUri** *(string) --*

        The S3 location of the input media file. The URI must be in the same region as the API
        endpoint that you are calling. The general form is:

         ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

        For example:

         ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

         ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

        For more information about S3 object names, see `Object Keys
        <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
        *Amazon S3 Developer Guide* .

    - **Transcript** *(dict) --*

      An object that describes the output of the transcription job.

      - **TranscriptFileUri** *(string) --*

        The location where the transcription is stored.

        Use this URI to access the transcription. If you specified an S3 bucket in the
        ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
        you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
        provides secure access to that location.

    - **CreationTime** *(datetime) --*

      A timestamp that shows when the job was created.

    - **CompletionTime** *(datetime) --*

      A timestamp that shows when the job was completed.

    - **FailureReason** *(string) --*

      If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information
      about why the job failed.

      The ``FailureReason`` field can contain one of the following values:

      * ``Unsupported media format`` - The media format specified in the ``MediaFormat`` field of
      the request isn't valid. See the description of the ``MediaFormat`` field for a list of
      valid values.

      * ``The media format provided does not match the detected media format`` - The media format
      of the audio file doesn't match the format specified in the ``MediaFormat`` field in the
      request. Check the media format of your media file and make sure that the two values match.

      * ``Invalid sample rate for audio file`` - The sample rate specified in the
      ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between 8000
      and 48000 Hertz.

      * ``The sample rate provided does not match the detected sample rate`` - The sample rate in
      the audio file doesn't match the sample rate specified in the ``MediaSampleRateHertz``
      field in the request. Check the sample rate of your media file and make sure that the two
      values match.

      * ``Invalid file size: file size too large`` - The size of your audio file is larger than
      Amazon Transcribe can process. For more information, see `Limits
      <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__ in the
      *Amazon Transcribe Developer Guide* .

      * ``Invalid number of channels: number of channels too large`` - Your audio contains more
      channels than Amazon Transcribe is configured to process. To request additional channels,
      see `Amazon Transcribe Limits
      <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
      in the *Amazon Web Services General Reference* .

    - **Settings** *(dict) --*

      Optional settings for the transcription job. Use these settings to turn on speaker
      recognition, to set the maximum number of speakers that should be identified and to specify
      a custom vocabulary to use when processing the transcription job.

      - **VocabularyName** *(string) --*

        The name of a vocabulary to use when processing the transcription job.

      - **ShowSpeakerLabels** *(boolean) --*

        Determines whether the transcription job uses speaker recognition to identify different
        speakers in the input audio. Speaker recognition labels individual speakers in the audio
        file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
        number of speaker labels ``MaxSpeakerLabels`` field.

        You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
        request. If you set both, your request returns a ``BadRequestException`` .

      - **MaxSpeakerLabels** *(integer) --*

        The maximum number of speakers to identify in the input audio. If there are more speakers
        in the audio than this number, multiple speakers will be identified as a single speaker.
        If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
        field to true.

      - **ChannelIdentification** *(boolean) --*

        Instructs Amazon Transcribe to process each audio channel separately and then merge the
        transcription output of each channel into a single transcription.

        Amazon Transcribe also produces a transcription of each item detected on an audio
        channel, including the start time and end time of the item and alternative transcriptions
        of the item including the confidence that Amazon Transcribe has in the transcription.

        You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
        request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientGetTranscriptionJobResponseTypeDef = TypedDict(
    "_ClientGetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientGetTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)


class ClientGetTranscriptionJobResponseTypeDef(
    _ClientGetTranscriptionJobResponseTypeDef
):
    """
    Type definition for `ClientGetTranscriptionJob` `Response`

    - **TranscriptionJob** *(dict) --*

      An object that contains the results of the transcription job.

      - **TranscriptionJobName** *(string) --*

        The name of the transcription job.

      - **TranscriptionJobStatus** *(string) --*

        The status of the transcription job.

      - **LanguageCode** *(string) --*

        The language code for the input speech.

      - **MediaSampleRateHertz** *(integer) --*

        The sample rate, in Hertz, of the audio track in the input media file.

      - **MediaFormat** *(string) --*

        The format of the input media file.

      - **Media** *(dict) --*

        An object that describes the input media for the transcription job.

        - **MediaFileUri** *(string) --*

          The S3 location of the input media file. The URI must be in the same region as the API
          endpoint that you are calling. The general form is:

           ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

          For example:

           ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

           ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

          For more information about S3 object names, see `Object Keys
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
          *Amazon S3 Developer Guide* .

      - **Transcript** *(dict) --*

        An object that describes the output of the transcription job.

        - **TranscriptFileUri** *(string) --*

          The location where the transcription is stored.

          Use this URI to access the transcription. If you specified an S3 bucket in the
          ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
          you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
          provides secure access to that location.

      - **CreationTime** *(datetime) --*

        A timestamp that shows when the job was created.

      - **CompletionTime** *(datetime) --*

        A timestamp that shows when the job was completed.

      - **FailureReason** *(string) --*

        If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information
        about why the job failed.

        The ``FailureReason`` field can contain one of the following values:

        * ``Unsupported media format`` - The media format specified in the ``MediaFormat`` field of
        the request isn't valid. See the description of the ``MediaFormat`` field for a list of
        valid values.

        * ``The media format provided does not match the detected media format`` - The media format
        of the audio file doesn't match the format specified in the ``MediaFormat`` field in the
        request. Check the media format of your media file and make sure that the two values match.

        * ``Invalid sample rate for audio file`` - The sample rate specified in the
        ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between 8000
        and 48000 Hertz.

        * ``The sample rate provided does not match the detected sample rate`` - The sample rate in
        the audio file doesn't match the sample rate specified in the ``MediaSampleRateHertz``
        field in the request. Check the sample rate of your media file and make sure that the two
        values match.

        * ``Invalid file size: file size too large`` - The size of your audio file is larger than
        Amazon Transcribe can process. For more information, see `Limits
        <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__ in the
        *Amazon Transcribe Developer Guide* .

        * ``Invalid number of channels: number of channels too large`` - Your audio contains more
        channels than Amazon Transcribe is configured to process. To request additional channels,
        see `Amazon Transcribe Limits
        <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
        in the *Amazon Web Services General Reference* .

      - **Settings** *(dict) --*

        Optional settings for the transcription job. Use these settings to turn on speaker
        recognition, to set the maximum number of speakers that should be identified and to specify
        a custom vocabulary to use when processing the transcription job.

        - **VocabularyName** *(string) --*

          The name of a vocabulary to use when processing the transcription job.

        - **ShowSpeakerLabels** *(boolean) --*

          Determines whether the transcription job uses speaker recognition to identify different
          speakers in the input audio. Speaker recognition labels individual speakers in the audio
          file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
          number of speaker labels ``MaxSpeakerLabels`` field.

          You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
          request. If you set both, your request returns a ``BadRequestException`` .

        - **MaxSpeakerLabels** *(integer) --*

          The maximum number of speakers to identify in the input audio. If there are more speakers
          in the audio than this number, multiple speakers will be identified as a single speaker.
          If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
          field to true.

        - **ChannelIdentification** *(boolean) --*

          Instructs Amazon Transcribe to process each audio channel separately and then merge the
          transcription output of each channel into a single transcription.

          Amazon Transcribe also produces a transcription of each item detected on an audio
          channel, including the start time and end time of the item and alternative transcriptions
          of the item including the confidence that Amazon Transcribe has in the transcription.

          You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
          request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientGetVocabularyResponseTypeDef = TypedDict(
    "_ClientGetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": str,
        "VocabularyState": str,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)


class ClientGetVocabularyResponseTypeDef(_ClientGetVocabularyResponseTypeDef):
    """
    Type definition for `ClientGetVocabulary` `Response`

    - **VocabularyName** *(string) --*

      The name of the vocabulary to return.

    - **LanguageCode** *(string) --*

      The language code of the vocabulary entries.

    - **VocabularyState** *(string) --*

      The processing state of the vocabulary.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the vocabulary was last modified.

    - **FailureReason** *(string) --*

      If the ``VocabularyState`` field is ``FAILED`` , this field contains information about why
      the job failed.

    - **DownloadUri** *(string) --*

      The S3 location where the vocabulary is stored. Use this URI to get the contents of the
      vocabulary. The URI is available for a limited time.
    """


_ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef = TypedDict(
    "_ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": str,
        "TranscriptionJobStatus": str,
        "FailureReason": str,
        "OutputLocationType": str,
    },
    total=False,
)


class ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef(
    _ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
):
    """
    Type definition for `ClientListTranscriptionJobsResponse` `TranscriptionJobSummaries`

    Provides a summary of information about a transcription job.

    - **TranscriptionJobName** *(string) --*

      The name of the transcription job.

    - **CreationTime** *(datetime) --*

      A timestamp that shows when the job was created.

    - **CompletionTime** *(datetime) --*

      A timestamp that shows when the job was completed.

    - **LanguageCode** *(string) --*

      The language code for the input speech.

    - **TranscriptionJobStatus** *(string) --*

      The status of the transcription job. When the status is ``COMPLETED`` , use the
      ``GetTranscriptionJob`` operation to get the results of the transcription.

    - **FailureReason** *(string) --*

      If the ``TranscriptionJobStatus`` field is ``FAILED`` , a description of the error.

    - **OutputLocationType** *(string) --*

      Indicates the location of the output of the transcription job.

      If the value is ``CUSTOMER_BUCKET`` then the location is the S3 bucket specified in the
      ``outputBucketName`` field when the transcription job was started with the
      ``StartTranscriptionJob`` operation.

      If the value is ``SERVICE_BUCKET`` then the output is stored by Amazon Transcribe and can
      be retrieved using the URI in the ``GetTranscriptionJob`` response's
      ``TranscriptFileUri`` field.
    """


_ClientListTranscriptionJobsResponseTypeDef = TypedDict(
    "_ClientListTranscriptionJobsResponseTypeDef",
    {
        "Status": str,
        "NextToken": str,
        "TranscriptionJobSummaries": List[
            ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
        ],
    },
    total=False,
)


class ClientListTranscriptionJobsResponseTypeDef(
    _ClientListTranscriptionJobsResponseTypeDef
):
    """
    Type definition for `ClientListTranscriptionJobs` `Response`

    - **Status** *(string) --*

      The requested status of the jobs returned.

    - **NextToken** *(string) --*

      The ``ListTranscriptionJobs`` operation returns a page of jobs at a time. The maximum size of
      the page is set by the ``MaxResults`` parameter. If there are more jobs in the list than the
      page size, Amazon Transcribe returns the ``NextPage`` token. Include the token in the next
      request to the ``ListTranscriptionJobs`` operation to return in the next page of jobs.

    - **TranscriptionJobSummaries** *(list) --*

      A list of objects containing summary information for a transcription job.

      - *(dict) --*

        Provides a summary of information about a transcription job.

        - **TranscriptionJobName** *(string) --*

          The name of the transcription job.

        - **CreationTime** *(datetime) --*

          A timestamp that shows when the job was created.

        - **CompletionTime** *(datetime) --*

          A timestamp that shows when the job was completed.

        - **LanguageCode** *(string) --*

          The language code for the input speech.

        - **TranscriptionJobStatus** *(string) --*

          The status of the transcription job. When the status is ``COMPLETED`` , use the
          ``GetTranscriptionJob`` operation to get the results of the transcription.

        - **FailureReason** *(string) --*

          If the ``TranscriptionJobStatus`` field is ``FAILED`` , a description of the error.

        - **OutputLocationType** *(string) --*

          Indicates the location of the output of the transcription job.

          If the value is ``CUSTOMER_BUCKET`` then the location is the S3 bucket specified in the
          ``outputBucketName`` field when the transcription job was started with the
          ``StartTranscriptionJob`` operation.

          If the value is ``SERVICE_BUCKET`` then the output is stored by Amazon Transcribe and can
          be retrieved using the URI in the ``GetTranscriptionJob`` response's
          ``TranscriptFileUri`` field.
    """


_ClientListVocabulariesResponseVocabulariesTypeDef = TypedDict(
    "_ClientListVocabulariesResponseVocabulariesTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": str,
        "LastModifiedTime": datetime,
        "VocabularyState": str,
    },
    total=False,
)


class ClientListVocabulariesResponseVocabulariesTypeDef(
    _ClientListVocabulariesResponseVocabulariesTypeDef
):
    """
    Type definition for `ClientListVocabulariesResponse` `Vocabularies`

    Provides information about a custom vocabulary.

    - **VocabularyName** *(string) --*

      The name of the vocabulary.

    - **LanguageCode** *(string) --*

      The language code of the vocabulary entries.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the vocabulary was last modified.

    - **VocabularyState** *(string) --*

      The processing state of the vocabulary. If the state is ``READY`` you can use the
      vocabulary in a ``StartTranscriptionJob`` request.
    """


_ClientListVocabulariesResponseTypeDef = TypedDict(
    "_ClientListVocabulariesResponseTypeDef",
    {
        "Status": str,
        "NextToken": str,
        "Vocabularies": List[ClientListVocabulariesResponseVocabulariesTypeDef],
    },
    total=False,
)


class ClientListVocabulariesResponseTypeDef(_ClientListVocabulariesResponseTypeDef):
    """
    Type definition for `ClientListVocabularies` `Response`

    - **Status** *(string) --*

      The requested vocabulary state.

    - **NextToken** *(string) --*

      The ``ListVocabularies`` operation returns a page of vocabularies at a time. The maximum size
      of the page is set by the ``MaxResults`` parameter. If there are more jobs in the list than
      the page size, Amazon Transcribe returns the ``NextPage`` token. Include the token in the
      next request to the ``ListVocabularies`` operation to return in the next page of jobs.

    - **Vocabularies** *(list) --*

      A list of objects that describe the vocabularies that match the search criteria in the
      request.

      - *(dict) --*

        Provides information about a custom vocabulary.

        - **VocabularyName** *(string) --*

          The name of the vocabulary.

        - **LanguageCode** *(string) --*

          The language code of the vocabulary entries.

        - **LastModifiedTime** *(datetime) --*

          The date and time that the vocabulary was last modified.

        - **VocabularyState** *(string) --*

          The processing state of the vocabulary. If the state is ``READY`` you can use the
          vocabulary in a ``StartTranscriptionJob`` request.
    """


_ClientStartTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientStartTranscriptionJobMediaTypeDef", {"MediaFileUri": str}, total=False
)


class ClientStartTranscriptionJobMediaTypeDef(_ClientStartTranscriptionJobMediaTypeDef):
    """
    Type definition for `ClientStartTranscriptionJob` `Media`

    An object that describes the input media for a transcription job.

    - **MediaFileUri** *(string) --*

      The S3 location of the input media file. The URI must be in the same region as the API endpoint
      that you are calling. The general form is:

       ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

      For example:

       ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

       ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

      For more information about S3 object names, see `Object Keys
      <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
      *Amazon S3 Developer Guide* .
    """


_ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJobResponseTranscriptionJob` `Media`

    An object that describes the input media for the transcription job.

    - **MediaFileUri** *(string) --*

      The S3 location of the input media file. The URI must be in the same region as the API
      endpoint that you are calling. The general form is:

       ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

      For example:

       ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

       ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

      For more information about S3 object names, see `Object Keys
      <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
      *Amazon S3 Developer Guide* .
    """


_ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
    },
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJobResponseTranscriptionJob` `Settings`

    Optional settings for the transcription job. Use these settings to turn on speaker
    recognition, to set the maximum number of speakers that should be identified and to specify
    a custom vocabulary to use when processing the transcription job.

    - **VocabularyName** *(string) --*

      The name of a vocabulary to use when processing the transcription job.

    - **ShowSpeakerLabels** *(boolean) --*

      Determines whether the transcription job uses speaker recognition to identify different
      speakers in the input audio. Speaker recognition labels individual speakers in the audio
      file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
      number of speaker labels ``MaxSpeakerLabels`` field.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
      request. If you set both, your request returns a ``BadRequestException`` .

    - **MaxSpeakerLabels** *(integer) --*

      The maximum number of speakers to identify in the input audio. If there are more speakers
      in the audio than this number, multiple speakers will be identified as a single speaker.
      If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
      field to true.

    - **ChannelIdentification** *(boolean) --*

      Instructs Amazon Transcribe to process each audio channel separately and then merge the
      transcription output of each channel into a single transcription.

      Amazon Transcribe also produces a transcription of each item detected on an audio
      channel, including the start time and end time of the item and alternative transcriptions
      of the item including the confidence that Amazon Transcribe has in the transcription.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
      request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJobResponseTranscriptionJob` `Transcript`

    An object that describes the output of the transcription job.

    - **TranscriptFileUri** *(string) --*

      The location where the transcription is stored.

      Use this URI to access the transcription. If you specified an S3 bucket in the
      ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
      you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
      provides secure access to that location.
    """


_ClientStartTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": str,
        "LanguageCode": str,
        "MediaSampleRateHertz": int,
        "MediaFormat": str,
        "Media": ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
    },
    total=False,
)


class ClientStartTranscriptionJobResponseTranscriptionJobTypeDef(
    _ClientStartTranscriptionJobResponseTranscriptionJobTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJobResponse` `TranscriptionJob`

    An object containing details of the asynchronous transcription job.

    - **TranscriptionJobName** *(string) --*

      The name of the transcription job.

    - **TranscriptionJobStatus** *(string) --*

      The status of the transcription job.

    - **LanguageCode** *(string) --*

      The language code for the input speech.

    - **MediaSampleRateHertz** *(integer) --*

      The sample rate, in Hertz, of the audio track in the input media file.

    - **MediaFormat** *(string) --*

      The format of the input media file.

    - **Media** *(dict) --*

      An object that describes the input media for the transcription job.

      - **MediaFileUri** *(string) --*

        The S3 location of the input media file. The URI must be in the same region as the API
        endpoint that you are calling. The general form is:

         ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

        For example:

         ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

         ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

        For more information about S3 object names, see `Object Keys
        <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
        *Amazon S3 Developer Guide* .

    - **Transcript** *(dict) --*

      An object that describes the output of the transcription job.

      - **TranscriptFileUri** *(string) --*

        The location where the transcription is stored.

        Use this URI to access the transcription. If you specified an S3 bucket in the
        ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
        you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
        provides secure access to that location.

    - **CreationTime** *(datetime) --*

      A timestamp that shows when the job was created.

    - **CompletionTime** *(datetime) --*

      A timestamp that shows when the job was completed.

    - **FailureReason** *(string) --*

      If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information
      about why the job failed.

      The ``FailureReason`` field can contain one of the following values:

      * ``Unsupported media format`` - The media format specified in the ``MediaFormat`` field of
      the request isn't valid. See the description of the ``MediaFormat`` field for a list of
      valid values.

      * ``The media format provided does not match the detected media format`` - The media format
      of the audio file doesn't match the format specified in the ``MediaFormat`` field in the
      request. Check the media format of your media file and make sure that the two values match.

      * ``Invalid sample rate for audio file`` - The sample rate specified in the
      ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between 8000
      and 48000 Hertz.

      * ``The sample rate provided does not match the detected sample rate`` - The sample rate in
      the audio file doesn't match the sample rate specified in the ``MediaSampleRateHertz``
      field in the request. Check the sample rate of your media file and make sure that the two
      values match.

      * ``Invalid file size: file size too large`` - The size of your audio file is larger than
      Amazon Transcribe can process. For more information, see `Limits
      <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__ in the
      *Amazon Transcribe Developer Guide* .

      * ``Invalid number of channels: number of channels too large`` - Your audio contains more
      channels than Amazon Transcribe is configured to process. To request additional channels,
      see `Amazon Transcribe Limits
      <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
      in the *Amazon Web Services General Reference* .

    - **Settings** *(dict) --*

      Optional settings for the transcription job. Use these settings to turn on speaker
      recognition, to set the maximum number of speakers that should be identified and to specify
      a custom vocabulary to use when processing the transcription job.

      - **VocabularyName** *(string) --*

        The name of a vocabulary to use when processing the transcription job.

      - **ShowSpeakerLabels** *(boolean) --*

        Determines whether the transcription job uses speaker recognition to identify different
        speakers in the input audio. Speaker recognition labels individual speakers in the audio
        file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
        number of speaker labels ``MaxSpeakerLabels`` field.

        You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
        request. If you set both, your request returns a ``BadRequestException`` .

      - **MaxSpeakerLabels** *(integer) --*

        The maximum number of speakers to identify in the input audio. If there are more speakers
        in the audio than this number, multiple speakers will be identified as a single speaker.
        If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
        field to true.

      - **ChannelIdentification** *(boolean) --*

        Instructs Amazon Transcribe to process each audio channel separately and then merge the
        transcription output of each channel into a single transcription.

        Amazon Transcribe also produces a transcription of each item detected on an audio
        channel, including the start time and end time of the item and alternative transcriptions
        of the item including the confidence that Amazon Transcribe has in the transcription.

        You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
        request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientStartTranscriptionJobResponseTypeDef = TypedDict(
    "_ClientStartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientStartTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)


class ClientStartTranscriptionJobResponseTypeDef(
    _ClientStartTranscriptionJobResponseTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJob` `Response`

    - **TranscriptionJob** *(dict) --*

      An object containing details of the asynchronous transcription job.

      - **TranscriptionJobName** *(string) --*

        The name of the transcription job.

      - **TranscriptionJobStatus** *(string) --*

        The status of the transcription job.

      - **LanguageCode** *(string) --*

        The language code for the input speech.

      - **MediaSampleRateHertz** *(integer) --*

        The sample rate, in Hertz, of the audio track in the input media file.

      - **MediaFormat** *(string) --*

        The format of the input media file.

      - **Media** *(dict) --*

        An object that describes the input media for the transcription job.

        - **MediaFileUri** *(string) --*

          The S3 location of the input media file. The URI must be in the same region as the API
          endpoint that you are calling. The general form is:

           ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

          For example:

           ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

           ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

          For more information about S3 object names, see `Object Keys
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
          *Amazon S3 Developer Guide* .

      - **Transcript** *(dict) --*

        An object that describes the output of the transcription job.

        - **TranscriptFileUri** *(string) --*

          The location where the transcription is stored.

          Use this URI to access the transcription. If you specified an S3 bucket in the
          ``OutputBucketName`` field when you created the job, this is the URI of that bucket. If
          you chose to store the transcription in Amazon Transcribe, this is a shareable URL that
          provides secure access to that location.

      - **CreationTime** *(datetime) --*

        A timestamp that shows when the job was created.

      - **CompletionTime** *(datetime) --*

        A timestamp that shows when the job was completed.

      - **FailureReason** *(string) --*

        If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains information
        about why the job failed.

        The ``FailureReason`` field can contain one of the following values:

        * ``Unsupported media format`` - The media format specified in the ``MediaFormat`` field of
        the request isn't valid. See the description of the ``MediaFormat`` field for a list of
        valid values.

        * ``The media format provided does not match the detected media format`` - The media format
        of the audio file doesn't match the format specified in the ``MediaFormat`` field in the
        request. Check the media format of your media file and make sure that the two values match.

        * ``Invalid sample rate for audio file`` - The sample rate specified in the
        ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between 8000
        and 48000 Hertz.

        * ``The sample rate provided does not match the detected sample rate`` - The sample rate in
        the audio file doesn't match the sample rate specified in the ``MediaSampleRateHertz``
        field in the request. Check the sample rate of your media file and make sure that the two
        values match.

        * ``Invalid file size: file size too large`` - The size of your audio file is larger than
        Amazon Transcribe can process. For more information, see `Limits
        <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__ in the
        *Amazon Transcribe Developer Guide* .

        * ``Invalid number of channels: number of channels too large`` - Your audio contains more
        channels than Amazon Transcribe is configured to process. To request additional channels,
        see `Amazon Transcribe Limits
        <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
        in the *Amazon Web Services General Reference* .

      - **Settings** *(dict) --*

        Optional settings for the transcription job. Use these settings to turn on speaker
        recognition, to set the maximum number of speakers that should be identified and to specify
        a custom vocabulary to use when processing the transcription job.

        - **VocabularyName** *(string) --*

          The name of a vocabulary to use when processing the transcription job.

        - **ShowSpeakerLabels** *(boolean) --*

          Determines whether the transcription job uses speaker recognition to identify different
          speakers in the input audio. Speaker recognition labels individual speakers in the audio
          file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
          number of speaker labels ``MaxSpeakerLabels`` field.

          You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
          request. If you set both, your request returns a ``BadRequestException`` .

        - **MaxSpeakerLabels** *(integer) --*

          The maximum number of speakers to identify in the input audio. If there are more speakers
          in the audio than this number, multiple speakers will be identified as a single speaker.
          If you specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels``
          field to true.

        - **ChannelIdentification** *(boolean) --*

          Instructs Amazon Transcribe to process each audio channel separately and then merge the
          transcription output of each channel into a single transcription.

          Amazon Transcribe also produces a transcription of each item detected on an audio
          channel, including the start time and end time of the item and alternative transcriptions
          of the item including the confidence that Amazon Transcribe has in the transcription.

          You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
          request. If you set both, your request returns a ``BadRequestException`` .
    """


_ClientStartTranscriptionJobSettingsTypeDef = TypedDict(
    "_ClientStartTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
    },
    total=False,
)


class ClientStartTranscriptionJobSettingsTypeDef(
    _ClientStartTranscriptionJobSettingsTypeDef
):
    """
    Type definition for `ClientStartTranscriptionJob` `Settings`

    A ``Settings`` object that provides optional settings for a transcription job.

    - **VocabularyName** *(string) --*

      The name of a vocabulary to use when processing the transcription job.

    - **ShowSpeakerLabels** *(boolean) --*

      Determines whether the transcription job uses speaker recognition to identify different
      speakers in the input audio. Speaker recognition labels individual speakers in the audio file.
      If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum number of
      speaker labels ``MaxSpeakerLabels`` field.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If
      you set both, your request returns a ``BadRequestException`` .

    - **MaxSpeakerLabels** *(integer) --*

      The maximum number of speakers to identify in the input audio. If there are more speakers in
      the audio than this number, multiple speakers will be identified as a single speaker. If you
      specify the ``MaxSpeakerLabels`` field, you must set the ``ShowSpeakerLabels`` field to true.

    - **ChannelIdentification** *(boolean) --*

      Instructs Amazon Transcribe to process each audio channel separately and then merge the
      transcription output of each channel into a single transcription.

      Amazon Transcribe also produces a transcription of each item detected on an audio channel,
      including the start time and end time of the item and alternative transcriptions of the item
      including the confidence that Amazon Transcribe has in the transcription.

      You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same request. If
      you set both, your request returns a ``BadRequestException`` .
    """


_ClientUpdateVocabularyResponseTypeDef = TypedDict(
    "_ClientUpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": str,
        "LastModifiedTime": datetime,
        "VocabularyState": str,
    },
    total=False,
)


class ClientUpdateVocabularyResponseTypeDef(_ClientUpdateVocabularyResponseTypeDef):
    """
    Type definition for `ClientUpdateVocabulary` `Response`

    - **VocabularyName** *(string) --*

      The name of the vocabulary that was updated.

    - **LanguageCode** *(string) --*

      The language code of the vocabulary entries.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the vocabulary was updated.

    - **VocabularyState** *(string) --*

      The processing state of the vocabulary. When the ``VocabularyState`` field contains ``READY``
      the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.
    """
