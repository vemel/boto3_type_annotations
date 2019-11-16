"Main interface for comprehend type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDetectDominantLanguageResponseErrorListTypeDef",
    "ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef",
    "ClientBatchDetectDominantLanguageResponseResultListTypeDef",
    "ClientBatchDetectDominantLanguageResponseTypeDef",
    "ClientBatchDetectEntitiesResponseErrorListTypeDef",
    "ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef",
    "ClientBatchDetectEntitiesResponseResultListTypeDef",
    "ClientBatchDetectEntitiesResponseTypeDef",
    "ClientBatchDetectKeyPhrasesResponseErrorListTypeDef",
    "ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef",
    "ClientBatchDetectKeyPhrasesResponseResultListTypeDef",
    "ClientBatchDetectKeyPhrasesResponseTypeDef",
    "ClientBatchDetectSentimentResponseErrorListTypeDef",
    "ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef",
    "ClientBatchDetectSentimentResponseResultListTypeDef",
    "ClientBatchDetectSentimentResponseTypeDef",
    "ClientBatchDetectSyntaxResponseErrorListTypeDef",
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef",
    "ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef",
    "ClientBatchDetectSyntaxResponseResultListTypeDef",
    "ClientBatchDetectSyntaxResponseTypeDef",
    "ClientCreateDocumentClassifierInputDataConfigTypeDef",
    "ClientCreateDocumentClassifierOutputDataConfigTypeDef",
    "ClientCreateDocumentClassifierResponseTypeDef",
    "ClientCreateDocumentClassifierTagsTypeDef",
    "ClientCreateDocumentClassifierVpcConfigTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef",
    "ClientCreateEntityRecognizerInputDataConfigTypeDef",
    "ClientCreateEntityRecognizerResponseTypeDef",
    "ClientCreateEntityRecognizerTagsTypeDef",
    "ClientCreateEntityRecognizerVpcConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef",
    "ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef",
    "ClientDescribeDocumentClassificationJobResponseTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef",
    "ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef",
    "ClientDescribeDocumentClassifierResponseTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef",
    "ClientDescribeDominantLanguageDetectionJobResponseTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef",
    "ClientDescribeEntitiesDetectionJobResponseTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef",
    "ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef",
    "ClientDescribeEntityRecognizerResponseTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef",
    "ClientDescribeKeyPhrasesDetectionJobResponseTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef",
    "ClientDescribeSentimentDetectionJobResponseTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef",
    "ClientDescribeTopicsDetectionJobResponseTypeDef",
    "ClientDetectDominantLanguageResponseLanguagesTypeDef",
    "ClientDetectDominantLanguageResponseTypeDef",
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    "ClientDetectEntitiesResponseTypeDef",
    "ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef",
    "ClientDetectKeyPhrasesResponseTypeDef",
    "ClientDetectSentimentResponseSentimentScoreTypeDef",
    "ClientDetectSentimentResponseTypeDef",
    "ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef",
    "ClientDetectSyntaxResponseSyntaxTokensTypeDef",
    "ClientDetectSyntaxResponseTypeDef",
    "ClientListDocumentClassificationJobsFilterTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    "ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef",
    "ClientListDocumentClassificationJobsResponseTypeDef",
    "ClientListDocumentClassifiersFilterTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    "ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef",
    "ClientListDocumentClassifiersResponseTypeDef",
    "ClientListDominantLanguageDetectionJobsFilterTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    "ClientListDominantLanguageDetectionJobsResponseTypeDef",
    "ClientListEntitiesDetectionJobsFilterTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef",
    "ClientListEntitiesDetectionJobsResponseTypeDef",
    "ClientListEntityRecognizersFilterTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    "ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef",
    "ClientListEntityRecognizersResponseTypeDef",
    "ClientListKeyPhrasesDetectionJobsFilterTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    "ClientListKeyPhrasesDetectionJobsResponseTypeDef",
    "ClientListSentimentDetectionJobsFilterTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef",
    "ClientListSentimentDetectionJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTopicsDetectionJobsFilterTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    "ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef",
    "ClientListTopicsDetectionJobsResponseTypeDef",
    "ClientStartDocumentClassificationJobInputDataConfigTypeDef",
    "ClientStartDocumentClassificationJobOutputDataConfigTypeDef",
    "ClientStartDocumentClassificationJobResponseTypeDef",
    "ClientStartDocumentClassificationJobVpcConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef",
    "ClientStartDominantLanguageDetectionJobResponseTypeDef",
    "ClientStartDominantLanguageDetectionJobVpcConfigTypeDef",
    "ClientStartEntitiesDetectionJobInputDataConfigTypeDef",
    "ClientStartEntitiesDetectionJobOutputDataConfigTypeDef",
    "ClientStartEntitiesDetectionJobResponseTypeDef",
    "ClientStartEntitiesDetectionJobVpcConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef",
    "ClientStartKeyPhrasesDetectionJobResponseTypeDef",
    "ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef",
    "ClientStartSentimentDetectionJobInputDataConfigTypeDef",
    "ClientStartSentimentDetectionJobOutputDataConfigTypeDef",
    "ClientStartSentimentDetectionJobResponseTypeDef",
    "ClientStartSentimentDetectionJobVpcConfigTypeDef",
    "ClientStartTopicsDetectionJobInputDataConfigTypeDef",
    "ClientStartTopicsDetectionJobOutputDataConfigTypeDef",
    "ClientStartTopicsDetectionJobResponseTypeDef",
    "ClientStartTopicsDetectionJobVpcConfigTypeDef",
    "ClientStopDominantLanguageDetectionJobResponseTypeDef",
    "ClientStopEntitiesDetectionJobResponseTypeDef",
    "ClientStopKeyPhrasesDetectionJobResponseTypeDef",
    "ClientStopSentimentDetectionJobResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListDocumentClassificationJobsPaginateFilterTypeDef",
    "ListDocumentClassificationJobsPaginatePaginationConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    "ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef",
    "ListDocumentClassificationJobsPaginateResponseTypeDef",
    "ListDocumentClassifiersPaginateFilterTypeDef",
    "ListDocumentClassifiersPaginatePaginationConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    "ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef",
    "ListDocumentClassifiersPaginateResponseTypeDef",
    "ListDominantLanguageDetectionJobsPaginateFilterTypeDef",
    "ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    "ListDominantLanguageDetectionJobsPaginateResponseTypeDef",
    "ListEntitiesDetectionJobsPaginateFilterTypeDef",
    "ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef",
    "ListEntitiesDetectionJobsPaginateResponseTypeDef",
    "ListEntityRecognizersPaginateFilterTypeDef",
    "ListEntityRecognizersPaginatePaginationConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    "ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef",
    "ListEntityRecognizersPaginateResponseTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateFilterTypeDef",
    "ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    "ListKeyPhrasesDetectionJobsPaginateResponseTypeDef",
    "ListSentimentDetectionJobsPaginateFilterTypeDef",
    "ListSentimentDetectionJobsPaginatePaginationConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    "ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef",
    "ListSentimentDetectionJobsPaginateResponseTypeDef",
    "ListTopicsDetectionJobsPaginateFilterTypeDef",
    "ListTopicsDetectionJobsPaginatePaginationConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef",
    "ListTopicsDetectionJobsPaginateResponseTypeDef",
)


_ClientBatchDetectDominantLanguageResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectDominantLanguageResponseErrorListTypeDef(
    _ClientBatchDetectDominantLanguageResponseErrorListTypeDef
):
    """
    Type definition for `ClientBatchDetectDominantLanguageResponse` `ErrorList`

    Describes an error that occurred while processing a document in a batch. The operation
    returns on ``BatchItemError`` object for each document that contained an error.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **ErrorCode** *(string) --*

      The numeric error code of the error.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef",
    {"LanguageCode": str, "Score": float},
    total=False,
)


class ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef(
    _ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef
):
    """
    Type definition for `ClientBatchDetectDominantLanguageResponseResultList` `Languages`

    Returns the code for the dominant language in the input text and the level of
    confidence that Amazon Comprehend has in the accuracy of the detection.

    - **LanguageCode** *(string) --*

      The RFC 5646 language code for the dominant language. For more information about RFC
      5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on
      the *IETF Tools* web site.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientBatchDetectDominantLanguageResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseResultListTypeDef",
    {
        "Index": int,
        "Languages": List[
            ClientBatchDetectDominantLanguageResponseResultListLanguagesTypeDef
        ],
    },
    total=False,
)


class ClientBatchDetectDominantLanguageResponseResultListTypeDef(
    _ClientBatchDetectDominantLanguageResponseResultListTypeDef
):
    """
    Type definition for `ClientBatchDetectDominantLanguageResponse` `ResultList`

    The result of calling the operation. The operation returns one object for each document
    that is successfully processed by the operation.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **Languages** *(list) --*

      One or more  DominantLanguage objects describing the dominant languages in the document.

      - *(dict) --*

        Returns the code for the dominant language in the input text and the level of
        confidence that Amazon Comprehend has in the accuracy of the detection.

        - **LanguageCode** *(string) --*

          The RFC 5646 language code for the dominant language. For more information about RFC
          5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on
          the *IETF Tools* web site.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientBatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "_ClientBatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectDominantLanguageResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectDominantLanguageResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectDominantLanguageResponseTypeDef(
    _ClientBatchDetectDominantLanguageResponseTypeDef
):
    """
    Type definition for `ClientBatchDetectDominantLanguage` `Response`

    - **ResultList** *(list) --*

      A list of objects containing the results of the operation. The results are sorted in
      ascending order by the ``Index`` field and match the order of the documents in the input
      list. If all of the documents contain an error, the ``ResultList`` is empty.

      - *(dict) --*

        The result of calling the operation. The operation returns one object for each document
        that is successfully processed by the operation.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **Languages** *(list) --*

          One or more  DominantLanguage objects describing the dominant languages in the document.

          - *(dict) --*

            Returns the code for the dominant language in the input text and the level of
            confidence that Amazon Comprehend has in the accuracy of the detection.

            - **LanguageCode** *(string) --*

              The RFC 5646 language code for the dominant language. For more information about RFC
              5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on
              the *IETF Tools* web site.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

    - **ErrorList** *(list) --*

      A list containing one object for each document that contained an error. The results are
      sorted in ascending order by the ``Index`` field and match the order of the documents in the
      input list. If there are no errors in the batch, the ``ErrorList`` is empty.

      - *(dict) --*

        Describes an error that occurred while processing a document in a batch. The operation
        returns on ``BatchItemError`` object for each document that contained an error.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **ErrorCode** *(string) --*

          The numeric error code of the error.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchDetectEntitiesResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectEntitiesResponseErrorListTypeDef(
    _ClientBatchDetectEntitiesResponseErrorListTypeDef
):
    """
    Type definition for `ClientBatchDetectEntitiesResponse` `ErrorList`

    Describes an error that occurred while processing a document in a batch. The operation
    returns on ``BatchItemError`` object for each document that contained an error.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **ErrorCode** *(string) --*

      The numeric error code of the error.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef",
    {"Score": float, "Type": str, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef(
    _ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef
):
    """
    Type definition for `ClientBatchDetectEntitiesResponseResultList` `Entities`

    Provides information about an entity.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.

    - **Type** *(string) --*

      The entity's type.

    - **Text** *(string) --*

      The text of the entity.

    - **BeginOffset** *(integer) --*

      A character offset in the input text that shows where the entity begins (the first
      character is at position 0). The offset returns the position of each UTF-8 code point
      in the string. A *code point* is the abstract character from a particular graphical
      representation. For example, a multi-byte UTF-8 character maps to a single code point.

    - **EndOffset** *(integer) --*

      A character offset in the input text that shows where the entity ends. The offset
      returns the position of each UTF-8 code point in the string. A *code point* is the
      abstract character from a particular graphical representation. For example, a
      multi-byte UTF-8 character maps to a single code point.
    """


_ClientBatchDetectEntitiesResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseResultListTypeDef",
    {
        "Index": int,
        "Entities": List[ClientBatchDetectEntitiesResponseResultListEntitiesTypeDef],
    },
    total=False,
)


class ClientBatchDetectEntitiesResponseResultListTypeDef(
    _ClientBatchDetectEntitiesResponseResultListTypeDef
):
    """
    Type definition for `ClientBatchDetectEntitiesResponse` `ResultList`

    The result of calling the operation. The operation returns one object for each document
    that is successfully processed by the operation.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **Entities** *(list) --*

      One or more  Entity objects, one for each entity detected in the document.

      - *(dict) --*

        Provides information about an entity.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.

        - **Type** *(string) --*

          The entity's type.

        - **Text** *(string) --*

          The text of the entity.

        - **BeginOffset** *(integer) --*

          A character offset in the input text that shows where the entity begins (the first
          character is at position 0). The offset returns the position of each UTF-8 code point
          in the string. A *code point* is the abstract character from a particular graphical
          representation. For example, a multi-byte UTF-8 character maps to a single code point.

        - **EndOffset** *(integer) --*

          A character offset in the input text that shows where the entity ends. The offset
          returns the position of each UTF-8 code point in the string. A *code point* is the
          abstract character from a particular graphical representation. For example, a
          multi-byte UTF-8 character maps to a single code point.
    """


_ClientBatchDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientBatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectEntitiesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectEntitiesResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectEntitiesResponseTypeDef(
    _ClientBatchDetectEntitiesResponseTypeDef
):
    """
    Type definition for `ClientBatchDetectEntities` `Response`

    - **ResultList** *(list) --*

      A list of objects containing the results of the operation. The results are sorted in
      ascending order by the ``Index`` field and match the order of the documents in the input
      list. If all of the documents contain an error, the ``ResultList`` is empty.

      - *(dict) --*

        The result of calling the operation. The operation returns one object for each document
        that is successfully processed by the operation.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **Entities** *(list) --*

          One or more  Entity objects, one for each entity detected in the document.

          - *(dict) --*

            Provides information about an entity.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

            - **Type** *(string) --*

              The entity's type.

            - **Text** *(string) --*

              The text of the entity.

            - **BeginOffset** *(integer) --*

              A character offset in the input text that shows where the entity begins (the first
              character is at position 0). The offset returns the position of each UTF-8 code point
              in the string. A *code point* is the abstract character from a particular graphical
              representation. For example, a multi-byte UTF-8 character maps to a single code point.

            - **EndOffset** *(integer) --*

              A character offset in the input text that shows where the entity ends. The offset
              returns the position of each UTF-8 code point in the string. A *code point* is the
              abstract character from a particular graphical representation. For example, a
              multi-byte UTF-8 character maps to a single code point.

    - **ErrorList** *(list) --*

      A list containing one object for each document that contained an error. The results are
      sorted in ascending order by the ``Index`` field and match the order of the documents in the
      input list. If there are no errors in the batch, the ``ErrorList`` is empty.

      - *(dict) --*

        Describes an error that occurred while processing a document in a batch. The operation
        returns on ``BatchItemError`` object for each document that contained an error.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **ErrorCode** *(string) --*

          The numeric error code of the error.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchDetectKeyPhrasesResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseErrorListTypeDef(
    _ClientBatchDetectKeyPhrasesResponseErrorListTypeDef
):
    """
    Type definition for `ClientBatchDetectKeyPhrasesResponse` `ErrorList`

    Describes an error that occurred while processing a document in a batch. The operation
    returns on ``BatchItemError`` object for each document that contained an error.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **ErrorCode** *(string) --*

      The numeric error code of the error.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef(
    _ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef
):
    """
    Type definition for `ClientBatchDetectKeyPhrasesResponseResultList` `KeyPhrases`

    Describes a key noun phrase.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.

    - **Text** *(string) --*

      The text of a key noun phrase.

    - **BeginOffset** *(integer) --*

      A character offset in the input text that shows where the key phrase begins (the
      first character is at position 0). The offset returns the position of each UTF-8 code
      point in the string. A *code point* is the abstract character from a particular
      graphical representation. For example, a multi-byte UTF-8 character maps to a single
      code point.

    - **EndOffset** *(integer) --*

      A character offset in the input text where the key phrase ends. The offset returns
      the position of each UTF-8 code point in the string. A ``code point`` is the abstract
      character from a particular graphical representation. For example, a multi-byte UTF-8
      character maps to a single code point.
    """


_ClientBatchDetectKeyPhrasesResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseResultListTypeDef",
    {
        "Index": int,
        "KeyPhrases": List[
            ClientBatchDetectKeyPhrasesResponseResultListKeyPhrasesTypeDef
        ],
    },
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseResultListTypeDef(
    _ClientBatchDetectKeyPhrasesResponseResultListTypeDef
):
    """
    Type definition for `ClientBatchDetectKeyPhrasesResponse` `ResultList`

    The result of calling the operation. The operation returns one object for each document
    that is successfully processed by the operation.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **KeyPhrases** *(list) --*

      One or more  KeyPhrase objects, one for each key phrase detected in the document.

      - *(dict) --*

        Describes a key noun phrase.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.

        - **Text** *(string) --*

          The text of a key noun phrase.

        - **BeginOffset** *(integer) --*

          A character offset in the input text that shows where the key phrase begins (the
          first character is at position 0). The offset returns the position of each UTF-8 code
          point in the string. A *code point* is the abstract character from a particular
          graphical representation. For example, a multi-byte UTF-8 character maps to a single
          code point.

        - **EndOffset** *(integer) --*

          A character offset in the input text where the key phrase ends. The offset returns
          the position of each UTF-8 code point in the string. A ``code point`` is the abstract
          character from a particular graphical representation. For example, a multi-byte UTF-8
          character maps to a single code point.
    """


_ClientBatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "_ClientBatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectKeyPhrasesResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectKeyPhrasesResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectKeyPhrasesResponseTypeDef(
    _ClientBatchDetectKeyPhrasesResponseTypeDef
):
    """
    Type definition for `ClientBatchDetectKeyPhrases` `Response`

    - **ResultList** *(list) --*

      A list of objects containing the results of the operation. The results are sorted in
      ascending order by the ``Index`` field and match the order of the documents in the input
      list. If all of the documents contain an error, the ``ResultList`` is empty.

      - *(dict) --*

        The result of calling the operation. The operation returns one object for each document
        that is successfully processed by the operation.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **KeyPhrases** *(list) --*

          One or more  KeyPhrase objects, one for each key phrase detected in the document.

          - *(dict) --*

            Describes a key noun phrase.

            - **Score** *(float) --*

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

            - **Text** *(string) --*

              The text of a key noun phrase.

            - **BeginOffset** *(integer) --*

              A character offset in the input text that shows where the key phrase begins (the
              first character is at position 0). The offset returns the position of each UTF-8 code
              point in the string. A *code point* is the abstract character from a particular
              graphical representation. For example, a multi-byte UTF-8 character maps to a single
              code point.

            - **EndOffset** *(integer) --*

              A character offset in the input text where the key phrase ends. The offset returns
              the position of each UTF-8 code point in the string. A ``code point`` is the abstract
              character from a particular graphical representation. For example, a multi-byte UTF-8
              character maps to a single code point.

    - **ErrorList** *(list) --*

      A list containing one object for each document that contained an error. The results are
      sorted in ascending order by the ``Index`` field and match the order of the documents in the
      input list. If there are no errors in the batch, the ``ErrorList`` is empty.

      - *(dict) --*

        Describes an error that occurred while processing a document in a batch. The operation
        returns on ``BatchItemError`` object for each document that contained an error.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **ErrorCode** *(string) --*

          The numeric error code of the error.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchDetectSentimentResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectSentimentResponseErrorListTypeDef(
    _ClientBatchDetectSentimentResponseErrorListTypeDef
):
    """
    Type definition for `ClientBatchDetectSentimentResponse` `ErrorList`

    Describes an error that occurred while processing a document in a batch. The operation
    returns on ``BatchItemError`` object for each document that contained an error.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **ErrorCode** *(string) --*

      The numeric error code of the error.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef",
    {"Positive": float, "Negative": float, "Neutral": float, "Mixed": float},
    total=False,
)


class ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef(
    _ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef
):
    """
    Type definition for `ClientBatchDetectSentimentResponseResultList` `SentimentScore`

    The level of confidence that Amazon Comprehend has in the accuracy of its sentiment
    detection.

    - **Positive** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of
      the ``POSITIVE`` sentiment.

    - **Negative** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of
      the ``NEGATIVE`` sentiment.

    - **Neutral** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of
      the ``NEUTRAL`` sentiment.

    - **Mixed** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of
      the ``MIXED`` sentiment.
    """


_ClientBatchDetectSentimentResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseResultListTypeDef",
    {
        "Index": int,
        "Sentiment": str,
        "SentimentScore": ClientBatchDetectSentimentResponseResultListSentimentScoreTypeDef,
    },
    total=False,
)


class ClientBatchDetectSentimentResponseResultListTypeDef(
    _ClientBatchDetectSentimentResponseResultListTypeDef
):
    """
    Type definition for `ClientBatchDetectSentimentResponse` `ResultList`

    The result of calling the operation. The operation returns one object for each document
    that is successfully processed by the operation.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **Sentiment** *(string) --*

      The sentiment detected in the document.

    - **SentimentScore** *(dict) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its sentiment
      detection.

      - **Positive** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of
        the ``POSITIVE`` sentiment.

      - **Negative** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of
        the ``NEGATIVE`` sentiment.

      - **Neutral** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of
        the ``NEUTRAL`` sentiment.

      - **Mixed** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of
        the ``MIXED`` sentiment.
    """


_ClientBatchDetectSentimentResponseTypeDef = TypedDict(
    "_ClientBatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSentimentResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSentimentResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectSentimentResponseTypeDef(
    _ClientBatchDetectSentimentResponseTypeDef
):
    """
    Type definition for `ClientBatchDetectSentiment` `Response`

    - **ResultList** *(list) --*

      A list of objects containing the results of the operation. The results are sorted in
      ascending order by the ``Index`` field and match the order of the documents in the input
      list. If all of the documents contain an error, the ``ResultList`` is empty.

      - *(dict) --*

        The result of calling the operation. The operation returns one object for each document
        that is successfully processed by the operation.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **Sentiment** *(string) --*

          The sentiment detected in the document.

        - **SentimentScore** *(dict) --*

          The level of confidence that Amazon Comprehend has in the accuracy of its sentiment
          detection.

          - **Positive** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of
            the ``POSITIVE`` sentiment.

          - **Negative** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of
            the ``NEGATIVE`` sentiment.

          - **Neutral** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of
            the ``NEUTRAL`` sentiment.

          - **Mixed** *(float) --*

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of
            the ``MIXED`` sentiment.

    - **ErrorList** *(list) --*

      A list containing one object for each document that contained an error. The results are
      sorted in ascending order by the ``Index`` field and match the order of the documents in the
      input list. If there are no errors in the batch, the ``ErrorList`` is empty.

      - *(dict) --*

        Describes an error that occurred while processing a document in a batch. The operation
        returns on ``BatchItemError`` object for each document that contained an error.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **ErrorCode** *(string) --*

          The numeric error code of the error.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchDetectSyntaxResponseErrorListTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseErrorListTypeDef",
    {"Index": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDetectSyntaxResponseErrorListTypeDef(
    _ClientBatchDetectSyntaxResponseErrorListTypeDef
):
    """
    Type definition for `ClientBatchDetectSyntaxResponse` `ErrorList`

    Describes an error that occurred while processing a document in a batch. The operation
    returns on ``BatchItemError`` object for each document that contained an error.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **ErrorCode** *(string) --*

      The numeric error code of the error.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef",
    {"Tag": str, "Score": float},
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef(
    _ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef
):
    """
    Type definition for `ClientBatchDetectSyntaxResponseResultListSyntaxTokens` `PartOfSpeech`

    Provides the part of speech label and the confidence level that Amazon Comprehend has
    that the part of speech was correctly identified. For more information, see
    how-syntax .

    - **Tag** *(string) --*

      Identifies the part of speech that the token represents.

    - **Score** *(float) --*

      The confidence that Amazon Comprehend has that the part of speech was correctly
      identified.
    """


_ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientBatchDetectSyntaxResponseResultListSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef(
    _ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef
):
    """
    Type definition for `ClientBatchDetectSyntaxResponseResultList` `SyntaxTokens`

    Represents a work in the input text that was recognized and assigned a part of speech.
    There is one syntax token record for each word in the source text.

    - **TokenId** *(integer) --*

      A unique identifier for a token.

    - **Text** *(string) --*

      The word that was recognized in the source text.

    - **BeginOffset** *(integer) --*

      The zero-based offset from the beginning of the source text to the first character in
      the word.

    - **EndOffset** *(integer) --*

      The zero-based offset from the beginning of the source text to the last character in
      the word.

    - **PartOfSpeech** *(dict) --*

      Provides the part of speech label and the confidence level that Amazon Comprehend has
      that the part of speech was correctly identified. For more information, see
      how-syntax .

      - **Tag** *(string) --*

        Identifies the part of speech that the token represents.

      - **Score** *(float) --*

        The confidence that Amazon Comprehend has that the part of speech was correctly
        identified.
    """


_ClientBatchDetectSyntaxResponseResultListTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseResultListTypeDef",
    {
        "Index": int,
        "SyntaxTokens": List[
            ClientBatchDetectSyntaxResponseResultListSyntaxTokensTypeDef
        ],
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseResultListTypeDef(
    _ClientBatchDetectSyntaxResponseResultListTypeDef
):
    """
    Type definition for `ClientBatchDetectSyntaxResponse` `ResultList`

    The result of calling the operation. The operation returns one object that is successfully
    processed by the operation.

    - **Index** *(integer) --*

      The zero-based index of the document in the input list.

    - **SyntaxTokens** *(list) --*

      The syntax tokens for the words in the document, one token for each word.

      - *(dict) --*

        Represents a work in the input text that was recognized and assigned a part of speech.
        There is one syntax token record for each word in the source text.

        - **TokenId** *(integer) --*

          A unique identifier for a token.

        - **Text** *(string) --*

          The word that was recognized in the source text.

        - **BeginOffset** *(integer) --*

          The zero-based offset from the beginning of the source text to the first character in
          the word.

        - **EndOffset** *(integer) --*

          The zero-based offset from the beginning of the source text to the last character in
          the word.

        - **PartOfSpeech** *(dict) --*

          Provides the part of speech label and the confidence level that Amazon Comprehend has
          that the part of speech was correctly identified. For more information, see
          how-syntax .

          - **Tag** *(string) --*

            Identifies the part of speech that the token represents.

          - **Score** *(float) --*

            The confidence that Amazon Comprehend has that the part of speech was correctly
            identified.
    """


_ClientBatchDetectSyntaxResponseTypeDef = TypedDict(
    "_ClientBatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List[ClientBatchDetectSyntaxResponseResultListTypeDef],
        "ErrorList": List[ClientBatchDetectSyntaxResponseErrorListTypeDef],
    },
    total=False,
)


class ClientBatchDetectSyntaxResponseTypeDef(_ClientBatchDetectSyntaxResponseTypeDef):
    """
    Type definition for `ClientBatchDetectSyntax` `Response`

    - **ResultList** *(list) --*

      A list of objects containing the results of the operation. The results are sorted in
      ascending order by the ``Index`` field and match the order of the documents in the input
      list. If all of the documents contain an error, the ``ResultList`` is empty.

      - *(dict) --*

        The result of calling the operation. The operation returns one object that is successfully
        processed by the operation.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **SyntaxTokens** *(list) --*

          The syntax tokens for the words in the document, one token for each word.

          - *(dict) --*

            Represents a work in the input text that was recognized and assigned a part of speech.
            There is one syntax token record for each word in the source text.

            - **TokenId** *(integer) --*

              A unique identifier for a token.

            - **Text** *(string) --*

              The word that was recognized in the source text.

            - **BeginOffset** *(integer) --*

              The zero-based offset from the beginning of the source text to the first character in
              the word.

            - **EndOffset** *(integer) --*

              The zero-based offset from the beginning of the source text to the last character in
              the word.

            - **PartOfSpeech** *(dict) --*

              Provides the part of speech label and the confidence level that Amazon Comprehend has
              that the part of speech was correctly identified. For more information, see
              how-syntax .

              - **Tag** *(string) --*

                Identifies the part of speech that the token represents.

              - **Score** *(float) --*

                The confidence that Amazon Comprehend has that the part of speech was correctly
                identified.

    - **ErrorList** *(list) --*

      A list containing one object for each document that contained an error. The results are
      sorted in ascending order by the ``Index`` field and match the order of the documents in the
      input list. If there are no errors in the batch, the ``ErrorList`` is empty.

      - *(dict) --*

        Describes an error that occurred while processing a document in a batch. The operation
        returns on ``BatchItemError`` object for each document that contained an error.

        - **Index** *(integer) --*

          The zero-based index of the document in the input list.

        - **ErrorCode** *(string) --*

          The numeric error code of the error.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientCreateDocumentClassifierInputDataConfigTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierInputDataConfigTypeDef", {"S3Uri": str}
)


class ClientCreateDocumentClassifierInputDataConfigTypeDef(
    _ClientCreateDocumentClassifierInputDataConfigTypeDef
):
    """
    Type definition for `ClientCreateDocumentClassifier` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of input files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.
    """


_ClientCreateDocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientCreateDocumentClassifierOutputDataConfigTypeDef(
    _ClientCreateDocumentClassifierOutputDataConfigTypeDef
):
    """
    Type definition for `ClientCreateDocumentClassifier` `OutputDataConfig`

    Enables the addition of output results configuration parameters for custom classifier jobs.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object while creating a custom classifier, you specify
      the Amazon S3 location where you want to write the confusion matrix. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix for
      the actual location of this output file.

      When the custom classifier job is finished, the service creates the output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the confusion matrix.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientCreateDocumentClassifierResponseTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierResponseTypeDef",
    {"DocumentClassifierArn": str},
    total=False,
)


class ClientCreateDocumentClassifierResponseTypeDef(
    _ClientCreateDocumentClassifierResponseTypeDef
):
    """
    Type definition for `ClientCreateDocumentClassifier` `Response`

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.
    """


_RequiredClientCreateDocumentClassifierTagsTypeDef = TypedDict(
    "_RequiredClientCreateDocumentClassifierTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDocumentClassifierTagsTypeDef = TypedDict(
    "_OptionalClientCreateDocumentClassifierTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDocumentClassifierTagsTypeDef(
    _RequiredClientCreateDocumentClassifierTagsTypeDef,
    _OptionalClientCreateDocumentClassifierTagsTypeDef,
):
    """
    Type definition for `ClientCreateDocumentClassifier` `Tags`

    A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
    a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate its
    use by a particular department.

    - **Key** *(string) --* **[REQUIRED]**

      The initial part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the key portion of the pair, with multiple possible values such as “sales,”
      “legal,” and “administration.”

    - **Value** *(string) --*

      The second part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the initial (key) portion of the pair, with a value of “sales” to indicate
      the sales department.
    """


_ClientCreateDocumentClassifierVpcConfigTypeDef = TypedDict(
    "_ClientCreateDocumentClassifierVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientCreateDocumentClassifierVpcConfigTypeDef(
    _ClientCreateDocumentClassifierVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateDocumentClassifier` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom classifier. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef", {"S3Uri": str}
)


class ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizerInputDataConfig` `Annotations`

    S3 location of the annotations file for an entity recognizer.

    - **S3Uri** *(string) --* **[REQUIRED]**

      Specifies the Amazon S3 location where the annotations for an entity recognizer are located.
      The URI must be in the same region as the API endpoint that you are calling.
    """


_ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef", {"S3Uri": str}
)


class ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizerInputDataConfig` `Documents`

    S3 location of the documents folder for an entity recognizer

    - **S3Uri** *(string) --* **[REQUIRED]**

      Specifies the Amazon S3 location where the training documents for an entity recognizer are
      located. The URI must be in the same region as the API endpoint that you are calling.
    """


_ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef", {"S3Uri": str}
)


class ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizerInputDataConfig` `EntityList`

    S3 location of the entity list for an entity recognizer.

    - **S3Uri** *(string) --* **[REQUIRED]**

      Specifies the Amazon S3 location where the entity list is located. The URI must be in the
      same region as the API endpoint that you are calling.
    """


_ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef", {"Type": str}
)


class ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef(
    _ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizerInputDataConfig` `EntityTypes`

    Information about an individual item on a list of entity types.

    - **Type** *(string) --* **[REQUIRED]**

      Entity type of an item on an entity type list.
    """


_RequiredClientCreateEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreateEntityRecognizerInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ClientCreateEntityRecognizerInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ClientCreateEntityRecognizerInputDataConfigDocumentsTypeDef,
    },
)
_OptionalClientCreateEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreateEntityRecognizerInputDataConfigTypeDef",
    {
        "Annotations": ClientCreateEntityRecognizerInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientCreateEntityRecognizerInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientCreateEntityRecognizerInputDataConfigTypeDef(
    _RequiredClientCreateEntityRecognizerInputDataConfigTypeDef,
    _OptionalClientCreateEntityRecognizerInputDataConfigTypeDef,
):
    """
    Type definition for `ClientCreateEntityRecognizer` `InputDataConfig`

    Specifies the format and location of the input data. The S3 bucket containing the input data must
    be located in the same region as the entity recognizer being created.

    - **EntityTypes** *(list) --* **[REQUIRED]**

      The entity types in the input data for an entity recognizer. A maximum of 12 entity types can
      be used at one time to train an entity recognizer.

      - *(dict) --*

        Information about an individual item on a list of entity types.

        - **Type** *(string) --* **[REQUIRED]**

          Entity type of an item on an entity type list.

    - **Documents** *(dict) --* **[REQUIRED]**

      S3 location of the documents folder for an entity recognizer

      - **S3Uri** *(string) --* **[REQUIRED]**

        Specifies the Amazon S3 location where the training documents for an entity recognizer are
        located. The URI must be in the same region as the API endpoint that you are calling.

    - **Annotations** *(dict) --*

      S3 location of the annotations file for an entity recognizer.

      - **S3Uri** *(string) --* **[REQUIRED]**

        Specifies the Amazon S3 location where the annotations for an entity recognizer are located.
        The URI must be in the same region as the API endpoint that you are calling.

    - **EntityList** *(dict) --*

      S3 location of the entity list for an entity recognizer.

      - **S3Uri** *(string) --* **[REQUIRED]**

        Specifies the Amazon S3 location where the entity list is located. The URI must be in the
        same region as the API endpoint that you are calling.
    """


_ClientCreateEntityRecognizerResponseTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerResponseTypeDef",
    {"EntityRecognizerArn": str},
    total=False,
)


class ClientCreateEntityRecognizerResponseTypeDef(
    _ClientCreateEntityRecognizerResponseTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizer` `Response`

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """


_RequiredClientCreateEntityRecognizerTagsTypeDef = TypedDict(
    "_RequiredClientCreateEntityRecognizerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEntityRecognizerTagsTypeDef = TypedDict(
    "_OptionalClientCreateEntityRecognizerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEntityRecognizerTagsTypeDef(
    _RequiredClientCreateEntityRecognizerTagsTypeDef,
    _OptionalClientCreateEntityRecognizerTagsTypeDef,
):
    """
    Type definition for `ClientCreateEntityRecognizer` `Tags`

    A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
    a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate its
    use by a particular department.

    - **Key** *(string) --* **[REQUIRED]**

      The initial part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the key portion of the pair, with multiple possible values such as “sales,”
      “legal,” and “administration.”

    - **Value** *(string) --*

      The second part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the initial (key) portion of the pair, with a value of “sales” to indicate
      the sales department.
    """


_ClientCreateEntityRecognizerVpcConfigTypeDef = TypedDict(
    "_ClientCreateEntityRecognizerVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientCreateEntityRecognizerVpcConfigTypeDef(
    _ClientCreateEntityRecognizerVpcConfigTypeDef
):
    """
    Type definition for `ClientCreateEntityRecognizer` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom entity recognizer. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the document classification
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the document
    classification job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your document classification job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef(
    _ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassificationJobResponse` `DocumentClassificationJobProperties`

    An object that describes the properties associated with the document classification job.

    - **JobId** *(string) --*

      The identifier assigned to the document classification job.

    - **JobName** *(string) --*

      The name that you assigned to the document classification job.

    - **JobStatus** *(string) --*

      The current status of the document classification job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of the job.

    - **SubmitTime** *(datetime) --*

      The time that the document classification job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the document classification job completed.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document classification
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the document
      classification job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
      grants Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your document classification job. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": ClientDescribeDocumentClassificationJobResponseDocumentClassificationJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDocumentClassificationJobResponseTypeDef(
    _ClientDescribeDocumentClassificationJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassificationJob` `Response`

    - **DocumentClassificationJobProperties** *(dict) --*

      An object that describes the properties associated with the document classification job.

      - **JobId** *(string) --*

        The identifier assigned to the document classification job.

      - **JobName** *(string) --*

        The name that you assigned to the document classification job.

      - **JobStatus** *(string) --*

        The current status of the document classification job. If the status is ``FAILED`` , the
        ``Message`` field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of the job.

      - **SubmitTime** *(datetime) --*

        The time that the document classification job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the document classification job completed.

      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the document classification
        job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the document
        classification job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
        grants Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your document classification job. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadata` `EvaluationMetrics`

    Describes the result metrics for the test data associated with an documentation
    classifier.

    - **Accuracy** *(float) --*

      The fraction of the labels that were correct recognized. It is computed by dividing the
      number of labels in the test documents that were correctly recognized by the total
      number of labels in the test documents.

    - **Precision** *(float) --*

      A measure of the usefulness of the classifier results in the test data. High precision
      means that the classifier returned substantially more relevant results than irrelevant
      ones.

    - **Recall** *(float) --*

      A measure of how complete the classifier results are for the test data. High recall
      means that the classifier returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the classifier results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponseDocumentClassifierProperties` `ClassifierMetadata`

    Information about the document classifier, including the number of documents used for
    training the classifier, the number of documents used for test the classifier, and an
    accuracy rating.

    - **NumberOfLabels** *(integer) --*

      The number of labels in the input data.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the classifier.
      Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the classifier.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Describes the result metrics for the test data associated with an documentation
      classifier.

      - **Accuracy** *(float) --*

        The fraction of the labels that were correct recognized. It is computed by dividing the
        number of labels in the test documents that were correctly recognized by the total
        number of labels in the test documents.

      - **Precision** *(float) --*

        A measure of the usefulness of the classifier results in the test data. High precision
        means that the classifier returned substantially more relevant results than irrelevant
        ones.

      - **Recall** *(float) --*

        A measure of how complete the classifier results are for the test data. High recall
        means that the classifier returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the classifier results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponseDocumentClassifierProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the document classifier for
    training.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can provide
      the prefix for a collection of input files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponseDocumentClassifierProperties` `OutputDataConfig`

    Provides output results configuration parameters for custom classifier jobs.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object while creating a custom classifier, you
      specify the Amazon S3 location where you want to write the confusion matrix. The URI must
      be in the same region as the API endpoint that you are calling. The location is used as
      the prefix for the actual location of this output file.

      When the custom classifier job is finished, the service creates the output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
      matrix.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponseDocumentClassifierProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your custom classifier. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesOutputDataConfigTypeDef,
        "ClassifierMetadata": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef(
    _ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifierResponse` `DocumentClassifierProperties`

    An object that contains the properties associated with a document classifier.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **LanguageCode** *(string) --*

      The language code for the language of the documents that the classifier was trained on.

    - **Status** *(string) --*

      The status of the document classifier. If the status is ``TRAINED`` the classifier is ready
      to use. If the status is ``FAILED`` you can see additional information about why the
      classifier wasn't trained in the ``Message`` field.

    - **Message** *(string) --*

      Additional information about the status of the classifier.

    - **SubmitTime** *(datetime) --*

      The time that the document classifier was submitted for training.

    - **EndTime** *(datetime) --*

      The time that training the document classifier completed.

    - **TrainingStartTime** *(datetime) --*

      Indicates the time when the training starts on documentation classifiers. You are billed
      for the time interval between this time and the value of TrainingEndTime.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the document classifier was completed. Indicates the time when
      the training completes on documentation classifiers. You are billed for the time interval
      between this time and the value of TrainingStartTime.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document classifier for
      training.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can provide
        the prefix for a collection of input files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

    - **OutputDataConfig** *(dict) --*

      Provides output results configuration parameters for custom classifier jobs.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object while creating a custom classifier, you
        specify the Amazon S3 location where you want to write the confusion matrix. The URI must
        be in the same region as the API endpoint that you are calling. The location is used as
        the prefix for the actual location of this output file.

        When the custom classifier job is finished, the service creates the output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
        matrix.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **ClassifierMetadata** *(dict) --*

      Information about the document classifier, including the number of documents used for
      training the classifier, the number of documents used for test the classifier, and an
      accuracy rating.

      - **NumberOfLabels** *(integer) --*

        The number of labels in the input data.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the classifier.
        Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the classifier.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Describes the result metrics for the test data associated with an documentation
        classifier.

        - **Accuracy** *(float) --*

          The fraction of the labels that were correct recognized. It is computed by dividing the
          number of labels in the test documents that were correctly recognized by the total
          number of labels in the test documents.

        - **Precision** *(float) --*

          A measure of the usefulness of the classifier results in the test data. High precision
          means that the classifier returned substantially more relevant results than irrelevant
          ones.

        - **Recall** *(float) --*

          A measure of how complete the classifier results are for the test data. High recall
          means that the classifier returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the classifier results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your custom classifier. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeDocumentClassifierResponseTypeDef = TypedDict(
    "_ClientDescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": ClientDescribeDocumentClassifierResponseDocumentClassifierPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDocumentClassifierResponseTypeDef(
    _ClientDescribeDocumentClassifierResponseTypeDef
):
    """
    Type definition for `ClientDescribeDocumentClassifier` `Response`

    - **DocumentClassifierProperties** *(dict) --*

      An object that contains the properties associated with a document classifier.

      - **DocumentClassifierArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the document classifier.

      - **LanguageCode** *(string) --*

        The language code for the language of the documents that the classifier was trained on.

      - **Status** *(string) --*

        The status of the document classifier. If the status is ``TRAINED`` the classifier is ready
        to use. If the status is ``FAILED`` you can see additional information about why the
        classifier wasn't trained in the ``Message`` field.

      - **Message** *(string) --*

        Additional information about the status of the classifier.

      - **SubmitTime** *(datetime) --*

        The time that the document classifier was submitted for training.

      - **EndTime** *(datetime) --*

        The time that training the document classifier completed.

      - **TrainingStartTime** *(datetime) --*

        Indicates the time when the training starts on documentation classifiers. You are billed
        for the time interval between this time and the value of TrainingEndTime.

      - **TrainingEndTime** *(datetime) --*

        The time that training of the document classifier was completed. Indicates the time when
        the training completes on documentation classifiers. You are billed for the time interval
        between this time and the value of TrainingStartTime.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the document classifier for
        training.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API
          endpoint that you are calling. The URI can point to a single input file or it can provide
          the prefix for a collection of input files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

      - **OutputDataConfig** *(dict) --*

        Provides output results configuration parameters for custom classifier jobs.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object while creating a custom classifier, you
          specify the Amazon S3 location where you want to write the confusion matrix. The URI must
          be in the same region as the API endpoint that you are calling. The location is used as
          the prefix for the actual location of this output file.

          When the custom classifier job is finished, the service creates the output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
          matrix.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **ClassifierMetadata** *(dict) --*

        Information about the document classifier, including the number of documents used for
        training the classifier, the number of documents used for test the classifier, and an
        accuracy rating.

        - **NumberOfLabels** *(integer) --*

          The number of labels in the input data.

        - **NumberOfTrainedDocuments** *(integer) --*

          The number of documents in the input data that were used to train the classifier.
          Typically this is 80 to 90 percent of the input documents.

        - **NumberOfTestDocuments** *(integer) --*

          The number of documents in the input data that were used to test the classifier.
          Typically this is 10 to 20 percent of the input documents.

        - **EvaluationMetrics** *(dict) --*

          Describes the result metrics for the test data associated with an documentation
          classifier.

          - **Accuracy** *(float) --*

            The fraction of the labels that were correct recognized. It is computed by dividing the
            number of labels in the test documents that were correctly recognized by the total
            number of labels in the test documents.

          - **Precision** *(float) --*

            A measure of the usefulness of the classifier results in the test data. High precision
            means that the classifier returned substantially more relevant results than irrelevant
            ones.

          - **Recall** *(float) --*

            A measure of how complete the classifier results are for the test data. High recall
            means that the classifier returned most of the relevant results.

          - **F1Score** *(float) --*

            A measure of how accurate the classifier results are for the test data. It is derived
            from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
            of the two scores. The highest score is 1, and the worst score is 0.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
        Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your custom classifier. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your dominant language detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeDominantLanguageDetectionJobResponse` `DominantLanguageDetectionJobProperties`

    An object that contains the properties associated with a dominant language detection job.

    - **JobId** *(string) --*

      The identifier assigned to the dominant language detection job.

    - **JobName** *(string) --*

      The name that you assigned to the dominant language detection job.

    - **JobStatus** *(string) --*

      The current status of the dominant language detection job. If the status is ``FAILED`` ,
      the ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the dominant language detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the dominant language detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your dominant language detection job. For more information, see `Amazon
      VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": ClientDescribeDominantLanguageDetectionJobResponseDominantLanguageDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeDominantLanguageDetectionJobResponseTypeDef(
    _ClientDescribeDominantLanguageDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeDominantLanguageDetectionJob` `Response`

    - **DominantLanguageDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a dominant language detection job.

      - **JobId** *(string) --*

        The identifier assigned to the dominant language detection job.

      - **JobName** *(string) --*

        The name that you assigned to the dominant language detection job.

      - **JobStatus** *(string) --*

        The current status of the dominant language detection job. If the status is ``FAILED`` ,
        the ``Message`` field shows the reason for the failure.

      - **Message** *(string) --*

        A description for the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the dominant language detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the dominant language detection job completed.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the dominant language
        detection job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the dominant language
        detection job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your dominant language detection job. For more information, see `Amazon
        VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the entities detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the entities detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your entity detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionJobResponse` `EntitiesDetectionJobProperties`

    An object that contains the properties associated with an entities detection job.

    - **JobId** *(string) --*

      The identifier assigned to the entities detection job.

    - **JobName** *(string) --*

      The name that you assigned the entities detection job.

    - **JobStatus** *(string) --*

      The current status of the entities detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the entities detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the entities detection job completed

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the entities detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the entities detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your entity detection job. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": ClientDescribeEntitiesDetectionJobResponseEntitiesDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntitiesDetectionJobResponseTypeDef(
    _ClientDescribeEntitiesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeEntitiesDetectionJob` `Response`

    - **EntitiesDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with an entities detection job.

      - **JobId** *(string) --*

        The identifier assigned to the entities detection job.

      - **JobName** *(string) --*

        The name that you assigned the entities detection job.

      - **JobStatus** *(string) --*

        The current status of the entities detection job. If the status is ``FAILED`` , the
        ``Message`` field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the entities detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the entities detection job completed

      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the entities detection job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the entities detection job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **LanguageCode** *(string) --*

        The language code of the input documents.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your entity detection job. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfig` `Annotations`

    S3 location of the annotations file for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the annotations for an entity recognizer are
      located. The URI must be in the same region as the API endpoint that you are calling.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfig` `Documents`

    S3 location of the documents folder for an entity recognizer

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the training documents for an entity recognizer
      are located. The URI must be in the same region as the API endpoint that you are
      calling.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfig` `EntityList`

    S3 location of the entity list for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the entity list is located. The URI must be in
      the same region as the API endpoint that you are calling.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfig` `EntityTypes`

    Information about an individual item on a list of entity types.

    - **Type** *(string) --*

      Entity type of an item on an entity type list.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigDocumentsTypeDef,
        "Annotations": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerProperties` `InputDataConfig`

    The input data properties of an entity recognizer.

    - **EntityTypes** *(list) --*

      The entity types in the input data for an entity recognizer. A maximum of 12 entity types
      can be used at one time to train an entity recognizer.

      - *(dict) --*

        Information about an individual item on a list of entity types.

        - **Type** *(string) --*

          Entity type of an item on an entity type list.

    - **Documents** *(dict) --*

      S3 location of the documents folder for an entity recognizer

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the training documents for an entity recognizer
        are located. The URI must be in the same region as the API endpoint that you are
        calling.

    - **Annotations** *(dict) --*

      S3 location of the annotations file for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the annotations for an entity recognizer are
        located. The URI must be in the same region as the API endpoint that you are calling.

    - **EntityList** *(dict) --*

      S3 location of the entity list for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the entity list is located. The URI must be in
        the same region as the API endpoint that you are calling.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypes` `EvaluationMetrics`

    Detailed information about the accuracy of the entity recognizer for a specific item
    on the list of entity types.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results for a specific entity type in
      the test data. High precision means that the recognizer returned substantially more
      relevant results than irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for a specific entity type in
      the test data. High recall means that the recognizer returned most of the relevant
      results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for for a specific entity type
      in the test data. It is derived from the ``Precision`` and ``Recall`` values. The
      ``F1Score`` is the harmonic average of the two scores. The highest score is 1, and
      the worst score is 0.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadata` `EntityTypes`

    Individual item from the list of entity types in the metadata of an entity recognizer.

    - **Type** *(string) --*

      Type of entity from the list of entity types in the metadata of an entity recognizer.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of the entity recognizer for a specific item
      on the list of entity types.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results for a specific entity type in
        the test data. High precision means that the recognizer returned substantially more
        relevant results than irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for a specific entity type in
        the test data. High recall means that the recognizer returned most of the relevant
        results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for for a specific entity type
        in the test data. It is derived from the ``Precision`` and ``Recall`` values. The
        ``F1Score`` is the harmonic average of the two scores. The highest score is 1, and
        the worst score is 0.

    - **NumberOfTrainMentions** *(integer) --*

      Indicates the number of times the given entity type was seen in the training data.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadata` `EvaluationMetrics`

    Detailed information about the accuracy of an entity recognizer.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results in the test data. High precision
      means that the recognizer returned substantially more relevant results than irrelevant
      ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for the test data. High recall
      means that the recognizer returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerProperties` `RecognizerMetadata`

    Provides information about an entity recognizer.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the entity recognizer.
      Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the entity recognizer.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of an entity recognizer.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results in the test data. High precision
        means that the recognizer returned substantially more relevant results than irrelevant
        ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for the test data. High recall
        means that the recognizer returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.

    - **EntityTypes** *(list) --*

      Entity types from the metadata of an entity recognizer.

      - *(dict) --*

        Individual item from the list of entity types in the metadata of an entity recognizer.

        - **Type** *(string) --*

          Type of entity from the list of entity types in the metadata of an entity recognizer.

        - **EvaluationMetrics** *(dict) --*

          Detailed information about the accuracy of the entity recognizer for a specific item
          on the list of entity types.

          - **Precision** *(float) --*

            A measure of the usefulness of the recognizer results for a specific entity type in
            the test data. High precision means that the recognizer returned substantially more
            relevant results than irrelevant ones.

          - **Recall** *(float) --*

            A measure of how complete the recognizer results are for a specific entity type in
            the test data. High recall means that the recognizer returned most of the relevant
            results.

          - **F1Score** *(float) --*

            A measure of how accurate the recognizer results are for for a specific entity type
            in the test data. It is derived from the ``Precision`` and ``Recall`` values. The
            ``F1Score`` is the harmonic average of the two scores. The highest score is 1, and
            the worst score is 0.

        - **NumberOfTrainMentions** *(integer) --*

          Indicates the number of times the given entity type was seen in the training data.
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponseEntityRecognizerProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your custom entity recognizer. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesInputDataConfigTypeDef,
        "RecognizerMetadata": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef(
    _ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizerResponse` `EntityRecognizerProperties`

    Describes information associated with an entity recognizer.

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **LanguageCode** *(string) --*

      The language of the input documents. All documents must be in the same language. Only
      English ("en") is currently supported.

    - **Status** *(string) --*

      Provides the status of the entity recognizer.

    - **Message** *(string) --*

      A description of the status of the recognizer.

    - **SubmitTime** *(datetime) --*

      The time that the recognizer was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the recognizer creation completed.

    - **TrainingStartTime** *(datetime) --*

      The time that training of the entity recognizer started.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the entity recognizer was completed.

    - **InputDataConfig** *(dict) --*

      The input data properties of an entity recognizer.

      - **EntityTypes** *(list) --*

        The entity types in the input data for an entity recognizer. A maximum of 12 entity types
        can be used at one time to train an entity recognizer.

        - *(dict) --*

          Information about an individual item on a list of entity types.

          - **Type** *(string) --*

            Entity type of an item on an entity type list.

      - **Documents** *(dict) --*

        S3 location of the documents folder for an entity recognizer

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the training documents for an entity recognizer
          are located. The URI must be in the same region as the API endpoint that you are
          calling.

      - **Annotations** *(dict) --*

        S3 location of the annotations file for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the annotations for an entity recognizer are
          located. The URI must be in the same region as the API endpoint that you are calling.

      - **EntityList** *(dict) --*

        S3 location of the entity list for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the entity list is located. The URI must be in
          the same region as the API endpoint that you are calling.

    - **RecognizerMetadata** *(dict) --*

      Provides information about an entity recognizer.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the entity recognizer.
        Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the entity recognizer.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Detailed information about the accuracy of an entity recognizer.

        - **Precision** *(float) --*

          A measure of the usefulness of the recognizer results in the test data. High precision
          means that the recognizer returned substantially more relevant results than irrelevant
          ones.

        - **Recall** *(float) --*

          A measure of how complete the recognizer results are for the test data. High recall
          means that the recognizer returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the recognizer results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

      - **EntityTypes** *(list) --*

        Entity types from the metadata of an entity recognizer.

        - *(dict) --*

          Individual item from the list of entity types in the metadata of an entity recognizer.

          - **Type** *(string) --*

            Type of entity from the list of entity types in the metadata of an entity recognizer.

          - **EvaluationMetrics** *(dict) --*

            Detailed information about the accuracy of the entity recognizer for a specific item
            on the list of entity types.

            - **Precision** *(float) --*

              A measure of the usefulness of the recognizer results for a specific entity type in
              the test data. High precision means that the recognizer returned substantially more
              relevant results than irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the recognizer results are for a specific entity type in
              the test data. High recall means that the recognizer returned most of the relevant
              results.

            - **F1Score** *(float) --*

              A measure of how accurate the recognizer results are for for a specific entity type
              in the test data. It is derived from the ``Precision`` and ``Recall`` values. The
              ``F1Score`` is the harmonic average of the two scores. The highest score is 1, and
              the worst score is 0.

          - **NumberOfTrainMentions** *(integer) --*

            Indicates the number of times the given entity type was seen in the training data.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your custom entity recognizer. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeEntityRecognizerResponseTypeDef = TypedDict(
    "_ClientDescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": ClientDescribeEntityRecognizerResponseEntityRecognizerPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntityRecognizerResponseTypeDef(
    _ClientDescribeEntityRecognizerResponseTypeDef
):
    """
    Type definition for `ClientDescribeEntityRecognizer` `Response`

    - **EntityRecognizerProperties** *(dict) --*

      Describes information associated with an entity recognizer.

      - **EntityRecognizerArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the entity recognizer.

      - **LanguageCode** *(string) --*

        The language of the input documents. All documents must be in the same language. Only
        English ("en") is currently supported.

      - **Status** *(string) --*

        Provides the status of the entity recognizer.

      - **Message** *(string) --*

        A description of the status of the recognizer.

      - **SubmitTime** *(datetime) --*

        The time that the recognizer was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the recognizer creation completed.

      - **TrainingStartTime** *(datetime) --*

        The time that training of the entity recognizer started.

      - **TrainingEndTime** *(datetime) --*

        The time that training of the entity recognizer was completed.

      - **InputDataConfig** *(dict) --*

        The input data properties of an entity recognizer.

        - **EntityTypes** *(list) --*

          The entity types in the input data for an entity recognizer. A maximum of 12 entity types
          can be used at one time to train an entity recognizer.

          - *(dict) --*

            Information about an individual item on a list of entity types.

            - **Type** *(string) --*

              Entity type of an item on an entity type list.

        - **Documents** *(dict) --*

          S3 location of the documents folder for an entity recognizer

          - **S3Uri** *(string) --*

            Specifies the Amazon S3 location where the training documents for an entity recognizer
            are located. The URI must be in the same region as the API endpoint that you are
            calling.

        - **Annotations** *(dict) --*

          S3 location of the annotations file for an entity recognizer.

          - **S3Uri** *(string) --*

            Specifies the Amazon S3 location where the annotations for an entity recognizer are
            located. The URI must be in the same region as the API endpoint that you are calling.

        - **EntityList** *(dict) --*

          S3 location of the entity list for an entity recognizer.

          - **S3Uri** *(string) --*

            Specifies the Amazon S3 location where the entity list is located. The URI must be in
            the same region as the API endpoint that you are calling.

      - **RecognizerMetadata** *(dict) --*

        Provides information about an entity recognizer.

        - **NumberOfTrainedDocuments** *(integer) --*

          The number of documents in the input data that were used to train the entity recognizer.
          Typically this is 80 to 90 percent of the input documents.

        - **NumberOfTestDocuments** *(integer) --*

          The number of documents in the input data that were used to test the entity recognizer.
          Typically this is 10 to 20 percent of the input documents.

        - **EvaluationMetrics** *(dict) --*

          Detailed information about the accuracy of an entity recognizer.

          - **Precision** *(float) --*

            A measure of the usefulness of the recognizer results in the test data. High precision
            means that the recognizer returned substantially more relevant results than irrelevant
            ones.

          - **Recall** *(float) --*

            A measure of how complete the recognizer results are for the test data. High recall
            means that the recognizer returned most of the relevant results.

          - **F1Score** *(float) --*

            A measure of how accurate the recognizer results are for the test data. It is derived
            from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
            of the two scores. The highest score is 1, and the worst score is 0.

        - **EntityTypes** *(list) --*

          Entity types from the metadata of an entity recognizer.

          - *(dict) --*

            Individual item from the list of entity types in the metadata of an entity recognizer.

            - **Type** *(string) --*

              Type of entity from the list of entity types in the metadata of an entity recognizer.

            - **EvaluationMetrics** *(dict) --*

              Detailed information about the accuracy of the entity recognizer for a specific item
              on the list of entity types.

              - **Precision** *(float) --*

                A measure of the usefulness of the recognizer results for a specific entity type in
                the test data. High precision means that the recognizer returned substantially more
                relevant results than irrelevant ones.

              - **Recall** *(float) --*

                A measure of how complete the recognizer results are for a specific entity type in
                the test data. High recall means that the recognizer returned most of the relevant
                results.

              - **F1Score** *(float) --*

                A measure of how accurate the recognizer results are for for a specific entity type
                in the test data. It is derived from the ``Precision`` and ``Recall`` values. The
                ``F1Score`` is the harmonic average of the two scores. The highest score is 1, and
                the worst score is 0.

            - **NumberOfTrainMentions** *(integer) --*

              Indicates the number of times the given entity type was seen in the training data.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
        Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your custom entity recognizer. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the key phrases detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the key phrases detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your key phrases detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeKeyPhrasesDetectionJobResponse` `KeyPhrasesDetectionJobProperties`

    An object that contains the properties associated with a key phrases detection job.

    - **JobId** *(string) --*

      The identifier assigned to the key phrases detection job.

    - **JobName** *(string) --*

      The name that you assigned the key phrases detection job.

    - **JobStatus** *(string) --*

      The current status of the key phrases detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the key phrases detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the key phrases detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the key phrases detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the key phrases detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your key phrases detection job. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": ClientDescribeKeyPhrasesDetectionJobResponseKeyPhrasesDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeKeyPhrasesDetectionJobResponseTypeDef(
    _ClientDescribeKeyPhrasesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeKeyPhrasesDetectionJob` `Response`

    - **KeyPhrasesDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a key phrases detection job.

      - **JobId** *(string) --*

        The identifier assigned to the key phrases detection job.

      - **JobName** *(string) --*

        The name that you assigned the key phrases detection job.

      - **JobStatus** *(string) --*

        The current status of the key phrases detection job. If the status is ``FAILED`` , the
        ``Message`` field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the key phrases detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the key phrases detection job completed.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the key phrases detection
        job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the key phrases detection
        job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **LanguageCode** *(string) --*

        The language code of the input documents.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your key phrases detection job. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobProperties` `InputDataConfig`

    The input data configuration that you supplied when you created the sentiment detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobProperties` `OutputDataConfig`

    The output data configuration that you supplied when you created the sentiment detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your sentiment detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef(
    _ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeSentimentDetectionJobResponse` `SentimentDetectionJobProperties`

    An object that contains the properties associated with a sentiment detection job.

    - **JobId** *(string) --*

      The identifier assigned to the sentiment detection job.

    - **JobName** *(string) --*

      The name that you assigned to the sentiment detection job

    - **JobStatus** *(string) --*

      The current status of the sentiment detection job. If the status is ``FAILED`` , the
      ``Messages`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the sentiment detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the sentiment detection job ended.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the sentiment detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the sentiment detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your sentiment detection job. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": ClientDescribeSentimentDetectionJobResponseSentimentDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeSentimentDetectionJobResponseTypeDef(
    _ClientDescribeSentimentDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeSentimentDetectionJob` `Response`

    - **SentimentDetectionJobProperties** *(dict) --*

      An object that contains the properties associated with a sentiment detection job.

      - **JobId** *(string) --*

        The identifier assigned to the sentiment detection job.

      - **JobName** *(string) --*

        The name that you assigned to the sentiment detection job

      - **JobStatus** *(string) --*

        The current status of the sentiment detection job. If the status is ``FAILED`` , the
        ``Messages`` field shows the reason for the failure.

      - **Message** *(string) --*

        A description of the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the sentiment detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the sentiment detection job ended.

      - **InputDataConfig** *(dict) --*

        The input data configuration that you supplied when you created the sentiment detection job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration that you supplied when you created the sentiment detection
        job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **LanguageCode** *(string) --*

        The language code of the input documents.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your sentiment detection job. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobProperties` `InputDataConfig`

    The input data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
      that you are calling. The URI can point to a single input file or it can provide the
      prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
      option when you are processing many short documents, such as text messages.
    """


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef
):
    """
    Type definition for `ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobProperties` `OutputDataConfig`

    The output data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the prefix
      for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef
):
    """
    Type definition for `ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobProperties` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
    you are using for your topic detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups on
      your VPC function serve as a virtual firewall to control inbound and outbound traffic and
      provides security for the resources that you’ll be accessing on the VPC. This ID number
      is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
      `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesVpcConfigTypeDef,
    },
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeTopicsDetectionJobResponse` `TopicsDetectionJobProperties`

    The list of properties for the requested job.

    - **JobId** *(string) --*

      The identifier assigned to the topic detection job.

    - **JobName** *(string) --*

      The name of the topic detection job.

    - **JobStatus** *(string) --*

      The current status of the topic detection job. If the status is ``Failed`` , the reason for
      the failure is shown in the ``Message`` field.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the topic detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the topic detection job was completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
        that you are calling. The URI can point to a single input file or it can provide the
        prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
        option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the prefix
        for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **NumberOfTopics** *(integer) --*

      The number of topics to detect supplied when you created the topic detection job. The
      default is 10.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your job data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
      on the storage volume attached to the ML compute instance(s) that process the analysis job.
      The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
      you are using for your topic detection job. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups on
        your VPC function serve as a virtual firewall to control inbound and outbound traffic and
        provides security for the resources that you’ll be accessing on the VPC. This ID number
        is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
        `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientDescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": ClientDescribeTopicsDetectionJobResponseTopicsDetectionJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeTopicsDetectionJobResponseTypeDef(
    _ClientDescribeTopicsDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeTopicsDetectionJob` `Response`

    - **TopicsDetectionJobProperties** *(dict) --*

      The list of properties for the requested job.

      - **JobId** *(string) --*

        The identifier assigned to the topic detection job.

      - **JobName** *(string) --*

        The name of the topic detection job.

      - **JobStatus** *(string) --*

        The current status of the topic detection job. If the status is ``Failed`` , the reason for
        the failure is shown in the ``Message`` field.

      - **Message** *(string) --*

        A description for the status of a job.

      - **SubmitTime** *(datetime) --*

        The time that the topic detection job was submitted for processing.

      - **EndTime** *(datetime) --*

        The time that the topic detection job was completed.

      - **InputDataConfig** *(dict) --*

        The input data configuration supplied when you created the topic detection job.

        - **S3Uri** *(string) --*

          The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
          that you are calling. The URI can point to a single input file or it can provide the
          prefix for a collection of data files.

          For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
          file, Amazon Comprehend uses that file as input. If more than one file begins with the
          prefix, Amazon Comprehend uses all of them as input.

        - **InputFormat** *(string) --*

          Specifies how the text in an input file should be processed:

          * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
          when you are processing large documents, such as newspaper articles or scientific papers.

          * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
          option when you are processing many short documents, such as text messages.

      - **OutputDataConfig** *(dict) --*

        The output data configuration supplied when you created the topic detection job.

        - **S3Uri** *(string) --*

          When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
          the Amazon S3 location where you want to write the output data. The URI must be in the
          same region as the API endpoint that you are calling. The location is used as the prefix
          for the actual location of the output file.

          When the topic detection job is finished, the service creates an output file in a
          directory specific to the job. The ``S3Uri`` field contains the location of the output
          file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
          the operation.

        - **KmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          the output results from an analysis job. The KmsKeyId can be one of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

          * KMS Key Alias: ``"alias/ExampleAlias"``

          * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

      - **NumberOfTopics** *(integer) --*

        The number of topics to detect supplied when you created the topic detection job. The
        default is 10.

      - **DataAccessRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
        Amazon Comprehend read access to your job data.

      - **VolumeKmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data
        on the storage volume attached to the ML compute instance(s) that process the analysis job.
        The VolumeKmsKeyId can be either of the following formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      - **VpcConfig** *(dict) --*

        Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources
        you are using for your topic detection job. For more information, see `Amazon VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

        - **SecurityGroupIds** *(list) --*

          The ID number for a security group on an instance of your private VPC. Security groups on
          your VPC function serve as a virtual firewall to control inbound and outbound traffic and
          provides security for the resources that you’ll be accessing on the VPC. This ID number
          is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see
          `Security Groups for your VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

          - *(string) --*

        - **Subnets** *(list) --*

          The ID for each subnet being used in your private VPC. This subnet is a subset of the a
          range of IPv4 addresses used by the VPC and is specific to a given availability zone in
          the VPC’s region. This ID number is preceded by "subnet-", for instance:
          "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
          <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

          - *(string) --*
    """


_ClientDetectDominantLanguageResponseLanguagesTypeDef = TypedDict(
    "_ClientDetectDominantLanguageResponseLanguagesTypeDef",
    {"LanguageCode": str, "Score": float},
    total=False,
)


class ClientDetectDominantLanguageResponseLanguagesTypeDef(
    _ClientDetectDominantLanguageResponseLanguagesTypeDef
):
    """
    Type definition for `ClientDetectDominantLanguageResponse` `Languages`

    Returns the code for the dominant language in the input text and the level of confidence
    that Amazon Comprehend has in the accuracy of the detection.

    - **LanguageCode** *(string) --*

      The RFC 5646 language code for the dominant language. For more information about RFC
      5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the
      *IETF Tools* web site.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectDominantLanguageResponseTypeDef = TypedDict(
    "_ClientDetectDominantLanguageResponseTypeDef",
    {"Languages": List[ClientDetectDominantLanguageResponseLanguagesTypeDef]},
    total=False,
)


class ClientDetectDominantLanguageResponseTypeDef(
    _ClientDetectDominantLanguageResponseTypeDef
):
    """
    Type definition for `ClientDetectDominantLanguage` `Response`

    - **Languages** *(list) --*

      The languages that Amazon Comprehend detected in the input text. For each language, the
      response returns the RFC 5646 language code and the level of confidence that Amazon
      Comprehend has in the accuracy of its inference. For more information about RFC 5646, see
      `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools*
      web site.

      - *(dict) --*

        Returns the code for the dominant language in the input text and the level of confidence
        that Amazon Comprehend has in the accuracy of the detection.

        - **LanguageCode** *(string) --*

          The RFC 5646 language code for the dominant language. For more information about RFC
          5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the
          *IETF Tools* web site.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.
    """


_ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTypeDef",
    {"Score": float, "Type": str, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTypeDef(
    _ClientDetectEntitiesResponseEntitiesTypeDef
):
    """
    Type definition for `ClientDetectEntitiesResponse` `Entities`

    Provides information about an entity.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.

    - **Type** *(string) --*

      The entity's type.

    - **Text** *(string) --*

      The text of the entity.

    - **BeginOffset** *(integer) --*

      A character offset in the input text that shows where the entity begins (the first
      character is at position 0). The offset returns the position of each UTF-8 code point in
      the string. A *code point* is the abstract character from a particular graphical
      representation. For example, a multi-byte UTF-8 character maps to a single code point.

    - **EndOffset** *(integer) --*

      A character offset in the input text that shows where the entity ends. The offset returns
      the position of each UTF-8 code point in the string. A *code point* is the abstract
      character from a particular graphical representation. For example, a multi-byte UTF-8
      character maps to a single code point.
    """


_ClientDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseTypeDef",
    {"Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef]},
    total=False,
)


class ClientDetectEntitiesResponseTypeDef(_ClientDetectEntitiesResponseTypeDef):
    """
    Type definition for `ClientDetectEntities` `Response`

    - **Entities** *(list) --*

      A collection of entities identified in the input text. For each entity, the response provides
      the entity text, entity type, where the entity text begins and ends, and the level of
      confidence that Amazon Comprehend has in the detection. For a list of entity types, see
      how-entities .

      - *(dict) --*

        Provides information about an entity.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.

        - **Type** *(string) --*

          The entity's type.

        - **Text** *(string) --*

          The text of the entity.

        - **BeginOffset** *(integer) --*

          A character offset in the input text that shows where the entity begins (the first
          character is at position 0). The offset returns the position of each UTF-8 code point in
          the string. A *code point* is the abstract character from a particular graphical
          representation. For example, a multi-byte UTF-8 character maps to a single code point.

        - **EndOffset** *(integer) --*

          A character offset in the input text that shows where the entity ends. The offset returns
          the position of each UTF-8 code point in the string. A *code point* is the abstract
          character from a particular graphical representation. For example, a multi-byte UTF-8
          character maps to a single code point.
    """


_ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef = TypedDict(
    "_ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef(
    _ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef
):
    """
    Type definition for `ClientDetectKeyPhrasesResponse` `KeyPhrases`

    Describes a key noun phrase.

    - **Score** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of the detection.

    - **Text** *(string) --*

      The text of a key noun phrase.

    - **BeginOffset** *(integer) --*

      A character offset in the input text that shows where the key phrase begins (the first
      character is at position 0). The offset returns the position of each UTF-8 code point in
      the string. A *code point* is the abstract character from a particular graphical
      representation. For example, a multi-byte UTF-8 character maps to a single code point.

    - **EndOffset** *(integer) --*

      A character offset in the input text where the key phrase ends. The offset returns the
      position of each UTF-8 code point in the string. A ``code point`` is the abstract
      character from a particular graphical representation. For example, a multi-byte UTF-8
      character maps to a single code point.
    """


_ClientDetectKeyPhrasesResponseTypeDef = TypedDict(
    "_ClientDetectKeyPhrasesResponseTypeDef",
    {"KeyPhrases": List[ClientDetectKeyPhrasesResponseKeyPhrasesTypeDef]},
    total=False,
)


class ClientDetectKeyPhrasesResponseTypeDef(_ClientDetectKeyPhrasesResponseTypeDef):
    """
    Type definition for `ClientDetectKeyPhrases` `Response`

    - **KeyPhrases** *(list) --*

      A collection of key phrases that Amazon Comprehend identified in the input text. For each key
      phrase, the response provides the text of the key phrase, where the key phrase begins and
      ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection.

      - *(dict) --*

        Describes a key noun phrase.

        - **Score** *(float) --*

          The level of confidence that Amazon Comprehend has in the accuracy of the detection.

        - **Text** *(string) --*

          The text of a key noun phrase.

        - **BeginOffset** *(integer) --*

          A character offset in the input text that shows where the key phrase begins (the first
          character is at position 0). The offset returns the position of each UTF-8 code point in
          the string. A *code point* is the abstract character from a particular graphical
          representation. For example, a multi-byte UTF-8 character maps to a single code point.

        - **EndOffset** *(integer) --*

          A character offset in the input text where the key phrase ends. The offset returns the
          position of each UTF-8 code point in the string. A ``code point`` is the abstract
          character from a particular graphical representation. For example, a multi-byte UTF-8
          character maps to a single code point.
    """


_ClientDetectSentimentResponseSentimentScoreTypeDef = TypedDict(
    "_ClientDetectSentimentResponseSentimentScoreTypeDef",
    {"Positive": float, "Negative": float, "Neutral": float, "Mixed": float},
    total=False,
)


class ClientDetectSentimentResponseSentimentScoreTypeDef(
    _ClientDetectSentimentResponseSentimentScoreTypeDef
):
    """
    Type definition for `ClientDetectSentimentResponse` `SentimentScore`

    An object that lists the sentiments, and their corresponding confidence levels.

    - **Positive** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
      ``POSITIVE`` sentiment.

    - **Negative** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
      ``NEGATIVE`` sentiment.

    - **Neutral** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
      ``NEUTRAL`` sentiment.

    - **Mixed** *(float) --*

      The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
      ``MIXED`` sentiment.
    """


_ClientDetectSentimentResponseTypeDef = TypedDict(
    "_ClientDetectSentimentResponseTypeDef",
    {
        "Sentiment": str,
        "SentimentScore": ClientDetectSentimentResponseSentimentScoreTypeDef,
    },
    total=False,
)


class ClientDetectSentimentResponseTypeDef(_ClientDetectSentimentResponseTypeDef):
    """
    Type definition for `ClientDetectSentiment` `Response`

    - **Sentiment** *(string) --*

      The inferred sentiment that Amazon Comprehend has the highest level of confidence in.

    - **SentimentScore** *(dict) --*

      An object that lists the sentiments, and their corresponding confidence levels.

      - **Positive** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
        ``POSITIVE`` sentiment.

      - **Negative** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
        ``NEGATIVE`` sentiment.

      - **Neutral** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
        ``NEUTRAL`` sentiment.

      - **Mixed** *(float) --*

        The level of confidence that Amazon Comprehend has in the accuracy of its detection of the
        ``MIXED`` sentiment.
    """


_ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef",
    {"Tag": str, "Score": float},
    total=False,
)


class ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef(
    _ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef
):
    """
    Type definition for `ClientDetectSyntaxResponseSyntaxTokens` `PartOfSpeech`

    Provides the part of speech label and the confidence level that Amazon Comprehend has
    that the part of speech was correctly identified. For more information, see  how-syntax .

    - **Tag** *(string) --*

      Identifies the part of speech that the token represents.

    - **Score** *(float) --*

      The confidence that Amazon Comprehend has that the part of speech was correctly
      identified.
    """


_ClientDetectSyntaxResponseSyntaxTokensTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseSyntaxTokensTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": ClientDetectSyntaxResponseSyntaxTokensPartOfSpeechTypeDef,
    },
    total=False,
)


class ClientDetectSyntaxResponseSyntaxTokensTypeDef(
    _ClientDetectSyntaxResponseSyntaxTokensTypeDef
):
    """
    Type definition for `ClientDetectSyntaxResponse` `SyntaxTokens`

    Represents a work in the input text that was recognized and assigned a part of speech.
    There is one syntax token record for each word in the source text.

    - **TokenId** *(integer) --*

      A unique identifier for a token.

    - **Text** *(string) --*

      The word that was recognized in the source text.

    - **BeginOffset** *(integer) --*

      The zero-based offset from the beginning of the source text to the first character in the
      word.

    - **EndOffset** *(integer) --*

      The zero-based offset from the beginning of the source text to the last character in the
      word.

    - **PartOfSpeech** *(dict) --*

      Provides the part of speech label and the confidence level that Amazon Comprehend has
      that the part of speech was correctly identified. For more information, see  how-syntax .

      - **Tag** *(string) --*

        Identifies the part of speech that the token represents.

      - **Score** *(float) --*

        The confidence that Amazon Comprehend has that the part of speech was correctly
        identified.
    """


_ClientDetectSyntaxResponseTypeDef = TypedDict(
    "_ClientDetectSyntaxResponseTypeDef",
    {"SyntaxTokens": List[ClientDetectSyntaxResponseSyntaxTokensTypeDef]},
    total=False,
)


class ClientDetectSyntaxResponseTypeDef(_ClientDetectSyntaxResponseTypeDef):
    """
    Type definition for `ClientDetectSyntax` `Response`

    - **SyntaxTokens** *(list) --*

      A collection of syntax tokens describing the text. For each token, the response provides the
      text, the token type, where the text begins and ends, and the level of confidence that Amazon
      Comprehend has that the token is correct. For a list of token types, see  how-syntax .

      - *(dict) --*

        Represents a work in the input text that was recognized and assigned a part of speech.
        There is one syntax token record for each word in the source text.

        - **TokenId** *(integer) --*

          A unique identifier for a token.

        - **Text** *(string) --*

          The word that was recognized in the source text.

        - **BeginOffset** *(integer) --*

          The zero-based offset from the beginning of the source text to the first character in the
          word.

        - **EndOffset** *(integer) --*

          The zero-based offset from the beginning of the source text to the last character in the
          word.

        - **PartOfSpeech** *(dict) --*

          Provides the part of speech label and the confidence level that Amazon Comprehend has
          that the part of speech was correctly identified. For more information, see  how-syntax .

          - **Tag** *(string) --*

            Identifies the part of speech that the token represents.

          - **Score** *(float) --*

            The confidence that Amazon Comprehend has that the part of speech was correctly
            identified.
    """


_ClientListDocumentClassificationJobsFilterTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListDocumentClassificationJobsFilterTypeDef(
    _ClientListDocumentClassificationJobsFilterTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobs` `Filter`

    Filters the jobs that are returned. You can filter jobs on their names, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the document
    classification job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the document
    classification job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your document classification job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef(
    _ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobsResponse` `DocumentClassificationJobPropertiesList`

    Provides information about a document classification job.

    - **JobId** *(string) --*

      The identifier assigned to the document classification job.

    - **JobName** *(string) --*

      The name that you assigned to the document classification job.

    - **JobStatus** *(string) --*

      The current status of the document classification job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of the job.

    - **SubmitTime** *(datetime) --*

      The time that the document classification job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the document classification job completed.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document
      classification job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the document
      classification job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
      grants Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your document classification job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "_ClientListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ClientListDocumentClassificationJobsResponseDocumentClassificationJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentClassificationJobsResponseTypeDef(
    _ClientListDocumentClassificationJobsResponseTypeDef
):
    """
    Type definition for `ClientListDocumentClassificationJobs` `Response`

    - **DocumentClassificationJobPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a document classification job.

        - **JobId** *(string) --*

          The identifier assigned to the document classification job.

        - **JobName** *(string) --*

          The name that you assigned to the document classification job.

        - **JobStatus** *(string) --*

          The current status of the document classification job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of the job.

        - **SubmitTime** *(datetime) --*

          The time that the document classification job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the document classification job completed.

        - **DocumentClassifierArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the document classifier.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the document
          classification job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the document
          classification job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your document classification job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListDocumentClassifiersFilterTypeDef = TypedDict(
    "_ClientListDocumentClassifiersFilterTypeDef",
    {"Status": str, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)


class ClientListDocumentClassifiersFilterTypeDef(
    _ClientListDocumentClassifiersFilterTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiers` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **Status** *(string) --*

      Filters the list of classifiers based on status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of classifiers based on the time that the classifier was submitted for
      processing. Returns only classifiers submitted before the specified time. Classifiers are
      returned in ascending order, oldest to newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of classifiers based on the time that the classifier was submitted for
      processing. Returns only classifiers submitted after the specified time. Classifiers are
      returned in descending order, newest to oldest.
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadata` `EvaluationMetrics`

    Describes the result metrics for the test data associated with an documentation
    classifier.

    - **Accuracy** *(float) --*

      The fraction of the labels that were correct recognized. It is computed by dividing
      the number of labels in the test documents that were correctly recognized by the
      total number of labels in the test documents.

    - **Precision** *(float) --*

      A measure of the usefulness of the classifier results in the test data. High
      precision means that the classifier returned substantially more relevant results than
      irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the classifier results are for the test data. High recall
      means that the classifier returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the classifier results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponseDocumentClassifierPropertiesList` `ClassifierMetadata`

    Information about the document classifier, including the number of documents used for
    training the classifier, the number of documents used for test the classifier, and an
    accuracy rating.

    - **NumberOfLabels** *(integer) --*

      The number of labels in the input data.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the classifier.
      Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the classifier.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Describes the result metrics for the test data associated with an documentation
      classifier.

      - **Accuracy** *(float) --*

        The fraction of the labels that were correct recognized. It is computed by dividing
        the number of labels in the test documents that were correctly recognized by the
        total number of labels in the test documents.

      - **Precision** *(float) --*

        A measure of the usefulness of the classifier results in the test data. High
        precision means that the classifier returned substantially more relevant results than
        irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the classifier results are for the test data. High recall
        means that the classifier returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the classifier results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponseDocumentClassifierPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the document classifier
    for training.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
      API endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of input files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponseDocumentClassifierPropertiesList` `OutputDataConfig`

    Provides output results configuration parameters for custom classifier jobs.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object while creating a custom classifier, you
      specify the Amazon S3 location where you want to write the confusion matrix. The URI
      must be in the same region as the API endpoint that you are calling. The location is
      used as the prefix for the actual location of this output file.

      When the custom classifier job is finished, the service creates the output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
      matrix.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponseDocumentClassifierPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom classifier. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef,
        "ClassifierMetadata": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef(
    _ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiersResponse` `DocumentClassifierPropertiesList`

    Provides information about a document classifier.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **LanguageCode** *(string) --*

      The language code for the language of the documents that the classifier was trained on.

    - **Status** *(string) --*

      The status of the document classifier. If the status is ``TRAINED`` the classifier is
      ready to use. If the status is ``FAILED`` you can see additional information about why
      the classifier wasn't trained in the ``Message`` field.

    - **Message** *(string) --*

      Additional information about the status of the classifier.

    - **SubmitTime** *(datetime) --*

      The time that the document classifier was submitted for training.

    - **EndTime** *(datetime) --*

      The time that training the document classifier completed.

    - **TrainingStartTime** *(datetime) --*

      Indicates the time when the training starts on documentation classifiers. You are billed
      for the time interval between this time and the value of TrainingEndTime.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the document classifier was completed. Indicates the time when
      the training completes on documentation classifiers. You are billed for the time interval
      between this time and the value of TrainingStartTime.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document classifier
      for training.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
        API endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of input files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

    - **OutputDataConfig** *(dict) --*

      Provides output results configuration parameters for custom classifier jobs.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object while creating a custom classifier, you
        specify the Amazon S3 location where you want to write the confusion matrix. The URI
        must be in the same region as the API endpoint that you are calling. The location is
        used as the prefix for the actual location of this output file.

        When the custom classifier job is finished, the service creates the output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
        matrix.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **ClassifierMetadata** *(dict) --*

      Information about the document classifier, including the number of documents used for
      training the classifier, the number of documents used for test the classifier, and an
      accuracy rating.

      - **NumberOfLabels** *(integer) --*

        The number of labels in the input data.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the classifier.
        Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the classifier.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Describes the result metrics for the test data associated with an documentation
        classifier.

        - **Accuracy** *(float) --*

          The fraction of the labels that were correct recognized. It is computed by dividing
          the number of labels in the test documents that were correctly recognized by the
          total number of labels in the test documents.

        - **Precision** *(float) --*

          A measure of the usefulness of the classifier results in the test data. High
          precision means that the classifier returned substantially more relevant results than
          irrelevant ones.

        - **Recall** *(float) --*

          A measure of how complete the classifier results are for the test data. High recall
          means that the classifier returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the classifier results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your custom classifier. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListDocumentClassifiersResponseTypeDef = TypedDict(
    "_ClientListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ClientListDocumentClassifiersResponseDocumentClassifierPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDocumentClassifiersResponseTypeDef(
    _ClientListDocumentClassifiersResponseTypeDef
):
    """
    Type definition for `ClientListDocumentClassifiers` `Response`

    - **DocumentClassifierPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a document classifier.

        - **DocumentClassifierArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the document classifier.

        - **LanguageCode** *(string) --*

          The language code for the language of the documents that the classifier was trained on.

        - **Status** *(string) --*

          The status of the document classifier. If the status is ``TRAINED`` the classifier is
          ready to use. If the status is ``FAILED`` you can see additional information about why
          the classifier wasn't trained in the ``Message`` field.

        - **Message** *(string) --*

          Additional information about the status of the classifier.

        - **SubmitTime** *(datetime) --*

          The time that the document classifier was submitted for training.

        - **EndTime** *(datetime) --*

          The time that training the document classifier completed.

        - **TrainingStartTime** *(datetime) --*

          Indicates the time when the training starts on documentation classifiers. You are billed
          for the time interval between this time and the value of TrainingEndTime.

        - **TrainingEndTime** *(datetime) --*

          The time that training of the document classifier was completed. Indicates the time when
          the training completes on documentation classifiers. You are billed for the time interval
          between this time and the value of TrainingStartTime.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the document classifier
          for training.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
            API endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of input files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

        - **OutputDataConfig** *(dict) --*

          Provides output results configuration parameters for custom classifier jobs.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object while creating a custom classifier, you
            specify the Amazon S3 location where you want to write the confusion matrix. The URI
            must be in the same region as the API endpoint that you are calling. The location is
            used as the prefix for the actual location of this output file.

            When the custom classifier job is finished, the service creates the output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
            matrix.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **ClassifierMetadata** *(dict) --*

          Information about the document classifier, including the number of documents used for
          training the classifier, the number of documents used for test the classifier, and an
          accuracy rating.

          - **NumberOfLabels** *(integer) --*

            The number of labels in the input data.

          - **NumberOfTrainedDocuments** *(integer) --*

            The number of documents in the input data that were used to train the classifier.
            Typically this is 80 to 90 percent of the input documents.

          - **NumberOfTestDocuments** *(integer) --*

            The number of documents in the input data that were used to test the classifier.
            Typically this is 10 to 20 percent of the input documents.

          - **EvaluationMetrics** *(dict) --*

            Describes the result metrics for the test data associated with an documentation
            classifier.

            - **Accuracy** *(float) --*

              The fraction of the labels that were correct recognized. It is computed by dividing
              the number of labels in the test documents that were correctly recognized by the
              total number of labels in the test documents.

            - **Precision** *(float) --*

              A measure of the usefulness of the classifier results in the test data. High
              precision means that the classifier returned substantially more relevant results than
              irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the classifier results are for the test data. High recall
              means that the classifier returned most of the relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the classifier results are for the test data. It is derived
              from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
              of the two scores. The highest score is 1, and the worst score is 0.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your custom classifier. For more information, see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListDominantLanguageDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsFilterTypeDef(
    _ClientListDominantLanguageDetectionJobsFilterTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobs` `Filter`

    Filters that jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your dominant language detection job. For more information,
    see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobsResponse` `DominantLanguageDetectionJobPropertiesList`

    Provides information about a dominant language detection job.

    - **JobId** *(string) --*

      The identifier assigned to the dominant language detection job.

    - **JobName** *(string) --*

      The name that you assigned to the dominant language detection job.

    - **JobStatus** *(string) --*

      The current status of the dominant language detection job. If the status is ``FAILED`` ,
      the ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the dominant language detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the dominant language detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your dominant language detection job. For more information,
      see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ClientListDominantLanguageDetectionJobsResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDominantLanguageDetectionJobsResponseTypeDef(
    _ClientListDominantLanguageDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListDominantLanguageDetectionJobs` `Response`

    - **DominantLanguageDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a dominant language detection job.

        - **JobId** *(string) --*

          The identifier assigned to the dominant language detection job.

        - **JobName** *(string) --*

          The name that you assigned to the dominant language detection job.

        - **JobStatus** *(string) --*

          The current status of the dominant language detection job. If the status is ``FAILED`` ,
          the ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description for the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the dominant language detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the dominant language detection job completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the dominant language
          detection job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the dominant language
          detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your dominant language detection job. For more information,
          see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListEntitiesDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsFilterTypeDef(
    _ClientListEntitiesDetectionJobsFilterTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobs` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the entities detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the entities detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your entity detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef(
    _ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobsResponse` `EntitiesDetectionJobPropertiesList`

    Provides information about an entities detection job.

    - **JobId** *(string) --*

      The identifier assigned to the entities detection job.

    - **JobName** *(string) --*

      The name that you assigned the entities detection job.

    - **JobStatus** *(string) --*

      The current status of the entities detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the entities detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the entities detection job completed

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the entities detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the entities detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your entity detection job. For more information, see `Amazon
      VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ClientListEntitiesDetectionJobsResponseEntitiesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntitiesDetectionJobsResponseTypeDef(
    _ClientListEntitiesDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListEntitiesDetectionJobs` `Response`

    - **EntitiesDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about an entities detection job.

        - **JobId** *(string) --*

          The identifier assigned to the entities detection job.

        - **JobName** *(string) --*

          The name that you assigned the entities detection job.

        - **JobStatus** *(string) --*

          The current status of the entities detection job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the entities detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the entities detection job completed

        - **EntityRecognizerArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the entities detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the entities detection
          job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your entity detection job. For more information, see `Amazon
          VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListEntityRecognizersFilterTypeDef = TypedDict(
    "_ClientListEntityRecognizersFilterTypeDef",
    {"Status": str, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)


class ClientListEntityRecognizersFilterTypeDef(
    _ClientListEntityRecognizersFilterTypeDef
):
    """
    Type definition for `ClientListEntityRecognizers` `Filter`

    Filters the list of entities returned. You can filter on ``Status`` , ``SubmitTimeBefore`` , or
    ``SubmitTimeAfter`` . You can only set one filter at a time.

    - **Status** *(string) --*

      The status of an entity recognizer.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of entities based on the time that the list was submitted for processing.
      Returns only jobs submitted before the specified time. Jobs are returned in descending order,
      newest to oldest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of entities based on the time that the list was submitted for processing.
      Returns only jobs submitted after the specified time. Jobs are returned in ascending order,
      oldest to newest.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfig` `Annotations`

    S3 location of the annotations file for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the annotations for an entity recognizer are
      located. The URI must be in the same region as the API endpoint that you are calling.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfig` `Documents`

    S3 location of the documents folder for an entity recognizer

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the training documents for an entity
      recognizer are located. The URI must be in the same region as the API endpoint that
      you are calling.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfig` `EntityList`

    S3 location of the entity list for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the entity list is located. The URI must be in
      the same region as the API endpoint that you are calling.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfig` `EntityTypes`

    Information about an individual item on a list of entity types.

    - **Type** *(string) --*

      Entity type of an item on an entity type list.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef,
        "Annotations": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef,
        "EntityList": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesList` `InputDataConfig`

    The input data properties of an entity recognizer.

    - **EntityTypes** *(list) --*

      The entity types in the input data for an entity recognizer. A maximum of 12 entity
      types can be used at one time to train an entity recognizer.

      - *(dict) --*

        Information about an individual item on a list of entity types.

        - **Type** *(string) --*

          Entity type of an item on an entity type list.

    - **Documents** *(dict) --*

      S3 location of the documents folder for an entity recognizer

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the training documents for an entity
        recognizer are located. The URI must be in the same region as the API endpoint that
        you are calling.

    - **Annotations** *(dict) --*

      S3 location of the annotations file for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the annotations for an entity recognizer are
        located. The URI must be in the same region as the API endpoint that you are calling.

    - **EntityList** *(dict) --*

      S3 location of the entity list for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the entity list is located. The URI must be in
        the same region as the API endpoint that you are calling.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypes` `EvaluationMetrics`

    Detailed information about the accuracy of the entity recognizer for a specific
    item on the list of entity types.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results for a specific entity type
      in the test data. High precision means that the recognizer returned substantially
      more relevant results than irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for a specific entity type
      in the test data. High recall means that the recognizer returned most of the
      relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for for a specific entity
      type in the test data. It is derived from the ``Precision`` and ``Recall``
      values. The ``F1Score`` is the harmonic average of the two scores. The highest
      score is 1, and the worst score is 0.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadata` `EntityTypes`

    Individual item from the list of entity types in the metadata of an entity recognizer.

    - **Type** *(string) --*

      Type of entity from the list of entity types in the metadata of an entity
      recognizer.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of the entity recognizer for a specific
      item on the list of entity types.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results for a specific entity type
        in the test data. High precision means that the recognizer returned substantially
        more relevant results than irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for a specific entity type
        in the test data. High recall means that the recognizer returned most of the
        relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for for a specific entity
        type in the test data. It is derived from the ``Precision`` and ``Recall``
        values. The ``F1Score`` is the harmonic average of the two scores. The highest
        score is 1, and the worst score is 0.

    - **NumberOfTrainMentions** *(integer) --*

      Indicates the number of times the given entity type was seen in the training data.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadata` `EvaluationMetrics`

    Detailed information about the accuracy of an entity recognizer.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results in the test data. High
      precision means that the recognizer returned substantially more relevant results than
      irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for the test data. High recall
      means that the recognizer returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesList` `RecognizerMetadata`

    Provides information about an entity recognizer.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the entity
      recognizer. Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the entity recognizer.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of an entity recognizer.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results in the test data. High
        precision means that the recognizer returned substantially more relevant results than
        irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for the test data. High recall
        means that the recognizer returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.

    - **EntityTypes** *(list) --*

      Entity types from the metadata of an entity recognizer.

      - *(dict) --*

        Individual item from the list of entity types in the metadata of an entity recognizer.

        - **Type** *(string) --*

          Type of entity from the list of entity types in the metadata of an entity
          recognizer.

        - **EvaluationMetrics** *(dict) --*

          Detailed information about the accuracy of the entity recognizer for a specific
          item on the list of entity types.

          - **Precision** *(float) --*

            A measure of the usefulness of the recognizer results for a specific entity type
            in the test data. High precision means that the recognizer returned substantially
            more relevant results than irrelevant ones.

          - **Recall** *(float) --*

            A measure of how complete the recognizer results are for a specific entity type
            in the test data. High recall means that the recognizer returned most of the
            relevant results.

          - **F1Score** *(float) --*

            A measure of how accurate the recognizer results are for for a specific entity
            type in the test data. It is derived from the ``Precision`` and ``Recall``
            values. The ``F1Score`` is the harmonic average of the two scores. The highest
            score is 1, and the worst score is 0.

        - **NumberOfTrainMentions** *(integer) --*

          Indicates the number of times the given entity type was seen in the training data.
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponseEntityRecognizerPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom entity recognizer. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListInputDataConfigTypeDef,
        "RecognizerMetadata": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListEntityRecognizersResponseEntityRecognizerPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef(
    _ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef
):
    """
    Type definition for `ClientListEntityRecognizersResponse` `EntityRecognizerPropertiesList`

    Describes information about an entity recognizer.

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **LanguageCode** *(string) --*

      The language of the input documents. All documents must be in the same language. Only
      English ("en") is currently supported.

    - **Status** *(string) --*

      Provides the status of the entity recognizer.

    - **Message** *(string) --*

      A description of the status of the recognizer.

    - **SubmitTime** *(datetime) --*

      The time that the recognizer was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the recognizer creation completed.

    - **TrainingStartTime** *(datetime) --*

      The time that training of the entity recognizer started.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the entity recognizer was completed.

    - **InputDataConfig** *(dict) --*

      The input data properties of an entity recognizer.

      - **EntityTypes** *(list) --*

        The entity types in the input data for an entity recognizer. A maximum of 12 entity
        types can be used at one time to train an entity recognizer.

        - *(dict) --*

          Information about an individual item on a list of entity types.

          - **Type** *(string) --*

            Entity type of an item on an entity type list.

      - **Documents** *(dict) --*

        S3 location of the documents folder for an entity recognizer

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the training documents for an entity
          recognizer are located. The URI must be in the same region as the API endpoint that
          you are calling.

      - **Annotations** *(dict) --*

        S3 location of the annotations file for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the annotations for an entity recognizer are
          located. The URI must be in the same region as the API endpoint that you are calling.

      - **EntityList** *(dict) --*

        S3 location of the entity list for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the entity list is located. The URI must be in
          the same region as the API endpoint that you are calling.

    - **RecognizerMetadata** *(dict) --*

      Provides information about an entity recognizer.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the entity
        recognizer. Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the entity recognizer.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Detailed information about the accuracy of an entity recognizer.

        - **Precision** *(float) --*

          A measure of the usefulness of the recognizer results in the test data. High
          precision means that the recognizer returned substantially more relevant results than
          irrelevant ones.

        - **Recall** *(float) --*

          A measure of how complete the recognizer results are for the test data. High recall
          means that the recognizer returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the recognizer results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

      - **EntityTypes** *(list) --*

        Entity types from the metadata of an entity recognizer.

        - *(dict) --*

          Individual item from the list of entity types in the metadata of an entity recognizer.

          - **Type** *(string) --*

            Type of entity from the list of entity types in the metadata of an entity
            recognizer.

          - **EvaluationMetrics** *(dict) --*

            Detailed information about the accuracy of the entity recognizer for a specific
            item on the list of entity types.

            - **Precision** *(float) --*

              A measure of the usefulness of the recognizer results for a specific entity type
              in the test data. High precision means that the recognizer returned substantially
              more relevant results than irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the recognizer results are for a specific entity type
              in the test data. High recall means that the recognizer returned most of the
              relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the recognizer results are for for a specific entity
              type in the test data. It is derived from the ``Precision`` and ``Recall``
              values. The ``F1Score`` is the harmonic average of the two scores. The highest
              score is 1, and the worst score is 0.

          - **NumberOfTrainMentions** *(integer) --*

            Indicates the number of times the given entity type was seen in the training data.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your custom entity recognizer. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListEntityRecognizersResponseTypeDef = TypedDict(
    "_ClientListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ClientListEntityRecognizersResponseEntityRecognizerPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntityRecognizersResponseTypeDef(
    _ClientListEntityRecognizersResponseTypeDef
):
    """
    Type definition for `ClientListEntityRecognizers` `Response`

    - **EntityRecognizerPropertiesList** *(list) --*

      The list of properties of an entity recognizer.

      - *(dict) --*

        Describes information about an entity recognizer.

        - **EntityRecognizerArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        - **LanguageCode** *(string) --*

          The language of the input documents. All documents must be in the same language. Only
          English ("en") is currently supported.

        - **Status** *(string) --*

          Provides the status of the entity recognizer.

        - **Message** *(string) --*

          A description of the status of the recognizer.

        - **SubmitTime** *(datetime) --*

          The time that the recognizer was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the recognizer creation completed.

        - **TrainingStartTime** *(datetime) --*

          The time that training of the entity recognizer started.

        - **TrainingEndTime** *(datetime) --*

          The time that training of the entity recognizer was completed.

        - **InputDataConfig** *(dict) --*

          The input data properties of an entity recognizer.

          - **EntityTypes** *(list) --*

            The entity types in the input data for an entity recognizer. A maximum of 12 entity
            types can be used at one time to train an entity recognizer.

            - *(dict) --*

              Information about an individual item on a list of entity types.

              - **Type** *(string) --*

                Entity type of an item on an entity type list.

          - **Documents** *(dict) --*

            S3 location of the documents folder for an entity recognizer

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the training documents for an entity
              recognizer are located. The URI must be in the same region as the API endpoint that
              you are calling.

          - **Annotations** *(dict) --*

            S3 location of the annotations file for an entity recognizer.

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the annotations for an entity recognizer are
              located. The URI must be in the same region as the API endpoint that you are calling.

          - **EntityList** *(dict) --*

            S3 location of the entity list for an entity recognizer.

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the entity list is located. The URI must be in
              the same region as the API endpoint that you are calling.

        - **RecognizerMetadata** *(dict) --*

          Provides information about an entity recognizer.

          - **NumberOfTrainedDocuments** *(integer) --*

            The number of documents in the input data that were used to train the entity
            recognizer. Typically this is 80 to 90 percent of the input documents.

          - **NumberOfTestDocuments** *(integer) --*

            The number of documents in the input data that were used to test the entity recognizer.
            Typically this is 10 to 20 percent of the input documents.

          - **EvaluationMetrics** *(dict) --*

            Detailed information about the accuracy of an entity recognizer.

            - **Precision** *(float) --*

              A measure of the usefulness of the recognizer results in the test data. High
              precision means that the recognizer returned substantially more relevant results than
              irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the recognizer results are for the test data. High recall
              means that the recognizer returned most of the relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the recognizer results are for the test data. It is derived
              from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
              of the two scores. The highest score is 1, and the worst score is 0.

          - **EntityTypes** *(list) --*

            Entity types from the metadata of an entity recognizer.

            - *(dict) --*

              Individual item from the list of entity types in the metadata of an entity recognizer.

              - **Type** *(string) --*

                Type of entity from the list of entity types in the metadata of an entity
                recognizer.

              - **EvaluationMetrics** *(dict) --*

                Detailed information about the accuracy of the entity recognizer for a specific
                item on the list of entity types.

                - **Precision** *(float) --*

                  A measure of the usefulness of the recognizer results for a specific entity type
                  in the test data. High precision means that the recognizer returned substantially
                  more relevant results than irrelevant ones.

                - **Recall** *(float) --*

                  A measure of how complete the recognizer results are for a specific entity type
                  in the test data. High recall means that the recognizer returned most of the
                  relevant results.

                - **F1Score** *(float) --*

                  A measure of how accurate the recognizer results are for for a specific entity
                  type in the test data. It is derived from the ``Precision`` and ``Recall``
                  values. The ``F1Score`` is the harmonic average of the two scores. The highest
                  score is 1, and the worst score is 0.

              - **NumberOfTrainMentions** *(integer) --*

                Indicates the number of times the given entity type was seen in the training data.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your custom entity recognizer. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListKeyPhrasesDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsFilterTypeDef(
    _ClientListKeyPhrasesDetectionJobsFilterTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobs` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the key phrases detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the key phrases
    detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your key phrases detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobsResponse` `KeyPhrasesDetectionJobPropertiesList`

    Provides information about a key phrases detection job.

    - **JobId** *(string) --*

      The identifier assigned to the key phrases detection job.

    - **JobName** *(string) --*

      The name that you assigned the key phrases detection job.

    - **JobStatus** *(string) --*

      The current status of the key phrases detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the key phrases detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the key phrases detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the key phrases detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the key phrases
      detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your key phrases detection job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ClientListKeyPhrasesDetectionJobsResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListKeyPhrasesDetectionJobsResponseTypeDef(
    _ClientListKeyPhrasesDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListKeyPhrasesDetectionJobs` `Response`

    - **KeyPhrasesDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a key phrases detection job.

        - **JobId** *(string) --*

          The identifier assigned to the key phrases detection job.

        - **JobName** *(string) --*

          The name that you assigned the key phrases detection job.

        - **JobStatus** *(string) --*

          The current status of the key phrases detection job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the key phrases detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the key phrases detection job completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the key phrases detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the key phrases
          detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your key phrases detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_ClientListSentimentDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListSentimentDetectionJobsFilterTypeDef(
    _ClientListSentimentDetectionJobsFilterTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobs` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the sentiment detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the sentiment detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your sentiment detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef(
    _ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobsResponse` `SentimentDetectionJobPropertiesList`

    Provides information about a sentiment detection job.

    - **JobId** *(string) --*

      The identifier assigned to the sentiment detection job.

    - **JobName** *(string) --*

      The name that you assigned to the sentiment detection job

    - **JobStatus** *(string) --*

      The current status of the sentiment detection job. If the status is ``FAILED`` , the
      ``Messages`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the sentiment detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the sentiment detection job ended.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the sentiment detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the sentiment detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your sentiment detection job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ClientListSentimentDetectionJobsResponseSentimentDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSentimentDetectionJobsResponseTypeDef(
    _ClientListSentimentDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListSentimentDetectionJobs` `Response`

    - **SentimentDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a sentiment detection job.

        - **JobId** *(string) --*

          The identifier assigned to the sentiment detection job.

        - **JobName** *(string) --*

          The name that you assigned to the sentiment detection job

        - **JobStatus** *(string) --*

          The current status of the sentiment detection job. If the status is ``FAILED`` , the
          ``Messages`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the sentiment detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the sentiment detection job ended.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the sentiment detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the sentiment detection
          job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your sentiment detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
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

    A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
    example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to
    indicate its use by a particular department.

    - **Key** *(string) --*

      The initial part of a key-value pair that forms a tag associated with a given resource.
      For instance, if you want to show which resources are used by which departments, you
      might use “Department” as the key portion of the pair, with multiple possible values such
      as “sales,” “legal,” and “administration.”

    - **Value** *(string) --*

      The second part of a key-value pair that forms a tag associated with a given resource.
      For instance, if you want to show which resources are used by which departments, you
      might use “Department” as the initial (key) portion of the pair, with a value of “sales”
      to indicate the sales department.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"ResourceArn": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are querying.

    - **Tags** *(list) --*

      Tags associated with the Amazon Comprehend resource being queried. A tag is a key-value pair
      that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with
      "Sales" as the key might be added to a resource to indicate its use by the sales department.

      - *(dict) --*

        A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
        example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to
        indicate its use by a particular department.

        - **Key** *(string) --*

          The initial part of a key-value pair that forms a tag associated with a given resource.
          For instance, if you want to show which resources are used by which departments, you
          might use “Department” as the key portion of the pair, with multiple possible values such
          as “sales,” “legal,” and “administration.”

        - **Value** *(string) --*

          The second part of a key-value pair that forms a tag associated with a given resource.
          For instance, if you want to show which resources are used by which departments, you
          might use “Department” as the initial (key) portion of the pair, with a value of “sales”
          to indicate the sales department.
    """


_ClientListTopicsDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListTopicsDetectionJobsFilterTypeDef(
    _ClientListTopicsDetectionJobsFilterTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobs` `Filter`

    Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and
    time that they were submitted. You can set only one filter at a time.

    - **JobName** *(string) --*

    - **JobStatus** *(string) --*

      Filters the list of topic detection jobs based on job status. Returns only jobs with the
      specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Only
      returns jobs submitted before the specified time. Jobs are returned in descending order, newest
      to oldest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Only
      returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest
      to newest.
    """


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your topic detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef(
    _ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobsResponse` `TopicsDetectionJobPropertiesList`

    Provides information about a topic detection job.

    - **JobId** *(string) --*

      The identifier assigned to the topic detection job.

    - **JobName** *(string) --*

      The name of the topic detection job.

    - **JobStatus** *(string) --*

      The current status of the topic detection job. If the status is ``Failed`` , the reason
      for the failure is shown in the ``Message`` field.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the topic detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the topic detection job was completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **NumberOfTopics** *(integer) --*

      The number of topics to detect supplied when you created the topic detection job. The
      default is 10.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your job data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your topic detection job. For more information, see `Amazon
      VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ClientListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ClientListTopicsDetectionJobsResponseTopicsDetectionJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTopicsDetectionJobsResponseTypeDef(
    _ClientListTopicsDetectionJobsResponseTypeDef
):
    """
    Type definition for `ClientListTopicsDetectionJobs` `Response`

    - **TopicsDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a topic detection job.

        - **JobId** *(string) --*

          The identifier assigned to the topic detection job.

        - **JobName** *(string) --*

          The name of the topic detection job.

        - **JobStatus** *(string) --*

          The current status of the topic detection job. If the status is ``Failed`` , the reason
          for the failure is shown in the ``Message`` field.

        - **Message** *(string) --*

          A description for the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the topic detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the topic detection job was completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration supplied when you created the topic detection job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration supplied when you created the topic detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **NumberOfTopics** *(integer) --*

          The number of topics to detect supplied when you created the topic detection job. The
          default is 10.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your job data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your topic detection job. For more information, see `Amazon
          VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

    - **NextToken** *(string) --*

      Identifies the next page of results to return.
    """


_RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef",
    {"S3Uri": str},
)
_OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartDocumentClassificationJobInputDataConfigTypeDef(
    _RequiredClientStartDocumentClassificationJobInputDataConfigTypeDef,
    _OptionalClientStartDocumentClassificationJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartDocumentClassificationJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef",
    {"S3Uri": str},
)
_OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartDocumentClassificationJobOutputDataConfigTypeDef(
    _RequiredClientStartDocumentClassificationJobOutputDataConfigTypeDef,
    _OptionalClientStartDocumentClassificationJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartDocumentClassificationJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartDocumentClassificationJobResponseTypeDef = TypedDict(
    "_ClientStartDocumentClassificationJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartDocumentClassificationJobResponseTypeDef(
    _ClientStartDocumentClassificationJobResponseTypeDef
):
    """
    Type definition for `ClientStartDocumentClassificationJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of the job, use this identifier with
      the operation.

    - **JobStatus** *(string) --*

      The status of the job:

      * SUBMITTED - The job has been received and queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. For details, use the operation.

      * STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is
      processing the request.

      * STOPPED - The job was successfully stopped without completing.
    """


_ClientStartDocumentClassificationJobVpcConfigTypeDef = TypedDict(
    "_ClientStartDocumentClassificationJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartDocumentClassificationJobVpcConfigTypeDef(
    _ClientStartDocumentClassificationJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartDocumentClassificationJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your document classification job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef",
    {"S3Uri": str},
)
_OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartDominantLanguageDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef",
    {"S3Uri": str},
)
_OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartDominantLanguageDetectionJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartDominantLanguageDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartDominantLanguageDetectionJobResponseTypeDef(
    _ClientStartDominantLanguageDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartDominantLanguageDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of a job, use this identifier with
      the operation.

    - **JobStatus** *(string) --*

      The status of the job.

      * SUBMITTED - The job has been received and is queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. To get details, use the operation.
    """


_ClientStartDominantLanguageDetectionJobVpcConfigTypeDef = TypedDict(
    "_ClientStartDominantLanguageDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartDominantLanguageDetectionJobVpcConfigTypeDef(
    _ClientStartDominantLanguageDetectionJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartDominantLanguageDetectionJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your dominant language detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartEntitiesDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartEntitiesDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartEntitiesDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartEntitiesDetectionJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartEntitiesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartEntitiesDetectionJobResponseTypeDef(
    _ClientStartEntitiesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartEntitiesDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of job, use this identifier with the
      operation.

    - **JobStatus** *(string) --*

      The status of the job.

      * SUBMITTED - The job has been received and is queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. To get details, use the operation.

      * STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is
      processing the request.

      * STOPPED - The job was successfully stopped without completing.
    """


_ClientStartEntitiesDetectionJobVpcConfigTypeDef = TypedDict(
    "_ClientStartEntitiesDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartEntitiesDetectionJobVpcConfigTypeDef(
    _ClientStartEntitiesDetectionJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartEntitiesDetectionJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your entity detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartKeyPhrasesDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartKeyPhrasesDetectionJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartKeyPhrasesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartKeyPhrasesDetectionJobResponseTypeDef(
    _ClientStartKeyPhrasesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartKeyPhrasesDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of a job, use this identifier with
      the operation.

    - **JobStatus** *(string) --*

      The status of the job.

      * SUBMITTED - The job has been received and is queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. To get details, use the operation.
    """


_ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef = TypedDict(
    "_ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef(
    _ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartKeyPhrasesDetectionJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your key phrases detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartSentimentDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartSentimentDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartSentimentDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartSentimentDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartSentimentDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartSentimentDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartSentimentDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartSentimentDetectionJob` `OutputDataConfig`

    Specifies where to send the output files.

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartSentimentDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartSentimentDetectionJobResponseTypeDef(
    _ClientStartSentimentDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartSentimentDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of a job, use this identifier with
      the operation.

    - **JobStatus** *(string) --*

      The status of the job.

      * SUBMITTED - The job has been received and is queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. To get details, use the operation.
    """


_ClientStartSentimentDetectionJobVpcConfigTypeDef = TypedDict(
    "_ClientStartSentimentDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartSentimentDetectionJobVpcConfigTypeDef(
    _ClientStartSentimentDetectionJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartSentimentDetectionJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your sentiment detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef",
    {"InputFormat": str},
    total=False,
)


class ClientStartTopicsDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartTopicsDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartTopicsDetectionJobInputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartTopicsDetectionJob` `InputDataConfig`

    Specifies the format and location of the input data for the job.

    - **S3Uri** *(string) --* **[REQUIRED]**

      The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that
      you are calling. The URI can point to a single input file or it can provide the prefix for a
      collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file,
      Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon
      Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you
      are processing large documents, such as newspaper articles or scientific papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option
      when you are processing many short documents, such as text messages.
    """


_RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientStartTopicsDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartTopicsDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartTopicsDetectionJobOutputDataConfigTypeDef,
):
    """
    Type definition for `ClientStartTopicsDetectionJob` `OutputDataConfig`

    Specifies where to send the output files. The output is a compressed archive with two files,
    ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that
    lists the documents associated with each topic

    - **S3Uri** *(string) --* **[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output file.

      When the topic detection job is finished, the service creates an output file in a directory
      specific to the job. The ``S3Uri`` field contains the location of the output file, called
      ``output.tar.gz`` . It is a compressed archive that contains the ouput of the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the
      output results from an analysis job. The KmsKeyId can be one of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ClientStartTopicsDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartTopicsDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStartTopicsDetectionJobResponseTypeDef(
    _ClientStartTopicsDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStartTopicsDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier generated for the job. To get the status of the job, use this identifier with
      the ``DescribeTopicDetectionJob`` operation.

    - **JobStatus** *(string) --*

      The status of the job:

      * SUBMITTED - The job has been received and is queued for processing.

      * IN_PROGRESS - Amazon Comprehend is processing the job.

      * COMPLETED - The job was successfully completed and the output is available.

      * FAILED - The job did not complete. To get details, use the ``DescribeTopicDetectionJob``
      operation.
    """


_ClientStartTopicsDetectionJobVpcConfigTypeDef = TypedDict(
    "_ClientStartTopicsDetectionJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
)


class ClientStartTopicsDetectionJobVpcConfigTypeDef(
    _ClientStartTopicsDetectionJobVpcConfigTypeDef
):
    """
    Type definition for `ClientStartTopicsDetectionJob` `VpcConfig`

    Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the
    resources you are using for your topic detection job. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --* **[REQUIRED]**

      The ID number for a security group on an instance of your private VPC. Security groups on your
      VPC function serve as a virtual firewall to control inbound and outbound traffic and provides
      security for the resources that you’ll be accessing on the VPC. This ID number is preceded by
      "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for
      your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --* **[REQUIRED]**

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a range
      of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s
      region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For
      more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ClientStopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopDominantLanguageDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStopDominantLanguageDetectionJobResponseTypeDef(
    _ClientStopDominantLanguageDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStopDominantLanguageDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier of the dominant language detection job to stop.

    - **JobStatus** *(string) --*

      Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was
      previously stopped with the ``StopDominantLanguageDetectionJob`` operation.
    """


_ClientStopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopEntitiesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStopEntitiesDetectionJobResponseTypeDef(
    _ClientStopEntitiesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStopEntitiesDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier of the entities detection job to stop.

    - **JobStatus** *(string) --*

      Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was
      previously stopped with the ``StopEntitiesDetectionJob`` operation.
    """


_ClientStopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopKeyPhrasesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStopKeyPhrasesDetectionJobResponseTypeDef(
    _ClientStopKeyPhrasesDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStopKeyPhrasesDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier of the key phrases detection job to stop.

    - **JobStatus** *(string) --*

      Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was
      previously stopped with the ``StopKeyPhrasesDetectionJob`` operation.
    """


_ClientStopSentimentDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopSentimentDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": str},
    total=False,
)


class ClientStopSentimentDetectionJobResponseTypeDef(
    _ClientStopSentimentDetectionJobResponseTypeDef
):
    """
    Type definition for `ClientStopSentimentDetectionJob` `Response`

    - **JobId** *(string) --*

      The identifier of the sentiment detection job to stop.

    - **JobStatus** *(string) --*

      Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job was
      previously stopped with the ``StopSentimentDetectionJob`` operation.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    Type definition for `ClientTagResource` `Tags`

    A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example,
    a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate its
    use by a particular department.

    - **Key** *(string) --* **[REQUIRED]**

      The initial part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the key portion of the pair, with multiple possible values such as “sales,”
      “legal,” and “administration.”

    - **Value** *(string) --*

      The second part of a key-value pair that forms a tag associated with a given resource. For
      instance, if you want to show which resources are used by which departments, you might use
      “Department” as the initial (key) portion of the pair, with a value of “sales” to indicate
      the sales department.
    """


_ListDocumentClassificationJobsPaginateFilterTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateFilterTypeDef(
    _ListDocumentClassificationJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginate` `Filter`

    Filters the jobs that are returned. You can filter jobs on their names, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ListDocumentClassificationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentClassificationJobsPaginatePaginationConfigTypeDef(
    _ListDocumentClassificationJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginate` `PaginationConfig`

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


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the document
    classification job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the document
    classification job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your document classification job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef(
    _ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginateResponse` `DocumentClassificationJobPropertiesList`

    Provides information about a document classification job.

    - **JobId** *(string) --*

      The identifier assigned to the document classification job.

    - **JobName** *(string) --*

      The name that you assigned to the document classification job.

    - **JobStatus** *(string) --*

      The current status of the document classification job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of the job.

    - **SubmitTime** *(datetime) --*

      The time that the document classification job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the document classification job completed.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document
      classification job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the document
      classification job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
      grants Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your document classification job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListDocumentClassificationJobsPaginateResponseTypeDef = TypedDict(
    "_ListDocumentClassificationJobsPaginateResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            ListDocumentClassificationJobsPaginateResponseDocumentClassificationJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDocumentClassificationJobsPaginateResponseTypeDef(
    _ListDocumentClassificationJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListDocumentClassificationJobsPaginate` `Response`

    - **DocumentClassificationJobPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a document classification job.

        - **JobId** *(string) --*

          The identifier assigned to the document classification job.

        - **JobName** *(string) --*

          The name that you assigned to the document classification job.

        - **JobStatus** *(string) --*

          The current status of the document classification job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of the job.

        - **SubmitTime** *(datetime) --*

          The time that the document classification job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the document classification job completed.

        - **DocumentClassifierArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the document classifier.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the document
          classification job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the document
          classification job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your document classification job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListDocumentClassifiersPaginateFilterTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateFilterTypeDef",
    {"Status": str, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)


class ListDocumentClassifiersPaginateFilterTypeDef(
    _ListDocumentClassifiersPaginateFilterTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginate` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **Status** *(string) --*

      Filters the list of classifiers based on status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of classifiers based on the time that the classifier was submitted for
      processing. Returns only classifiers submitted before the specified time. Classifiers are
      returned in ascending order, oldest to newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of classifiers based on the time that the classifier was submitted for
      processing. Returns only classifiers submitted after the specified time. Classifiers are
      returned in descending order, newest to oldest.
    """


_ListDocumentClassifiersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDocumentClassifiersPaginatePaginationConfigTypeDef(
    _ListDocumentClassifiersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginate` `PaginationConfig`

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


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef",
    {"Accuracy": float, "Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadata` `EvaluationMetrics`

    Describes the result metrics for the test data associated with an documentation
    classifier.

    - **Accuracy** *(float) --*

      The fraction of the labels that were correct recognized. It is computed by dividing
      the number of labels in the test documents that were correctly recognized by the
      total number of labels in the test documents.

    - **Precision** *(float) --*

      A measure of the usefulness of the classifier results in the test data. High
      precision means that the classifier returned substantially more relevant results than
      irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the classifier results are for the test data. High recall
      means that the classifier returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the classifier results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataEvaluationMetricsTypeDef,
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesList` `ClassifierMetadata`

    Information about the document classifier, including the number of documents used for
    training the classifier, the number of documents used for test the classifier, and an
    accuracy rating.

    - **NumberOfLabels** *(integer) --*

      The number of labels in the input data.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the classifier.
      Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the classifier.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Describes the result metrics for the test data associated with an documentation
      classifier.

      - **Accuracy** *(float) --*

        The fraction of the labels that were correct recognized. It is computed by dividing
        the number of labels in the test documents that were correctly recognized by the
        total number of labels in the test documents.

      - **Precision** *(float) --*

        A measure of the usefulness of the classifier results in the test data. High
        precision means that the classifier returned substantially more relevant results than
        irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the classifier results are for the test data. High recall
        means that the classifier returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the classifier results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the document classifier
    for training.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
      API endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of input files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesList` `OutputDataConfig`

    Provides output results configuration parameters for custom classifier jobs.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object while creating a custom classifier, you
      specify the Amazon S3 location where you want to write the confusion matrix. The URI
      must be in the same region as the API endpoint that you are calling. The location is
      used as the prefix for the actual location of this output file.

      When the custom classifier job is finished, the service creates the output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
      matrix.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom classifier. For more information, see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListOutputDataConfigTypeDef,
        "ClassifierMetadata": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListClassifierMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef(
    _ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginateResponse` `DocumentClassifierPropertiesList`

    Provides information about a document classifier.

    - **DocumentClassifierArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the document classifier.

    - **LanguageCode** *(string) --*

      The language code for the language of the documents that the classifier was trained on.

    - **Status** *(string) --*

      The status of the document classifier. If the status is ``TRAINED`` the classifier is
      ready to use. If the status is ``FAILED`` you can see additional information about why
      the classifier wasn't trained in the ``Message`` field.

    - **Message** *(string) --*

      Additional information about the status of the classifier.

    - **SubmitTime** *(datetime) --*

      The time that the document classifier was submitted for training.

    - **EndTime** *(datetime) --*

      The time that training the document classifier completed.

    - **TrainingStartTime** *(datetime) --*

      Indicates the time when the training starts on documentation classifiers. You are billed
      for the time interval between this time and the value of TrainingEndTime.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the document classifier was completed. Indicates the time when
      the training completes on documentation classifiers. You are billed for the time interval
      between this time and the value of TrainingStartTime.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the document classifier
      for training.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
        API endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of input files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

    - **OutputDataConfig** *(dict) --*

      Provides output results configuration parameters for custom classifier jobs.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object while creating a custom classifier, you
        specify the Amazon S3 location where you want to write the confusion matrix. The URI
        must be in the same region as the API endpoint that you are calling. The location is
        used as the prefix for the actual location of this output file.

        When the custom classifier job is finished, the service creates the output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
        matrix.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **ClassifierMetadata** *(dict) --*

      Information about the document classifier, including the number of documents used for
      training the classifier, the number of documents used for test the classifier, and an
      accuracy rating.

      - **NumberOfLabels** *(integer) --*

        The number of labels in the input data.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the classifier.
        Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the classifier.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Describes the result metrics for the test data associated with an documentation
        classifier.

        - **Accuracy** *(float) --*

          The fraction of the labels that were correct recognized. It is computed by dividing
          the number of labels in the test documents that were correctly recognized by the
          total number of labels in the test documents.

        - **Precision** *(float) --*

          A measure of the usefulness of the classifier results in the test data. High
          precision means that the classifier returned substantially more relevant results than
          irrelevant ones.

        - **Recall** *(float) --*

          A measure of how complete the classifier results are for the test data. High recall
          means that the classifier returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the classifier results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your custom classifier. For more information, see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListDocumentClassifiersPaginateResponseTypeDef = TypedDict(
    "_ListDocumentClassifiersPaginateResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[
            ListDocumentClassifiersPaginateResponseDocumentClassifierPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDocumentClassifiersPaginateResponseTypeDef(
    _ListDocumentClassifiersPaginateResponseTypeDef
):
    """
    Type definition for `ListDocumentClassifiersPaginate` `Response`

    - **DocumentClassifierPropertiesList** *(list) --*

      A list containing the properties of each job returned.

      - *(dict) --*

        Provides information about a document classifier.

        - **DocumentClassifierArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the document classifier.

        - **LanguageCode** *(string) --*

          The language code for the language of the documents that the classifier was trained on.

        - **Status** *(string) --*

          The status of the document classifier. If the status is ``TRAINED`` the classifier is
          ready to use. If the status is ``FAILED`` you can see additional information about why
          the classifier wasn't trained in the ``Message`` field.

        - **Message** *(string) --*

          Additional information about the status of the classifier.

        - **SubmitTime** *(datetime) --*

          The time that the document classifier was submitted for training.

        - **EndTime** *(datetime) --*

          The time that training the document classifier completed.

        - **TrainingStartTime** *(datetime) --*

          Indicates the time when the training starts on documentation classifiers. You are billed
          for the time interval between this time and the value of TrainingEndTime.

        - **TrainingEndTime** *(datetime) --*

          The time that training of the document classifier was completed. Indicates the time when
          the training completes on documentation classifiers. You are billed for the time interval
          between this time and the value of TrainingStartTime.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the document classifier
          for training.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
            API endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of input files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

        - **OutputDataConfig** *(dict) --*

          Provides output results configuration parameters for custom classifier jobs.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object while creating a custom classifier, you
            specify the Amazon S3 location where you want to write the confusion matrix. The URI
            must be in the same region as the API endpoint that you are calling. The location is
            used as the prefix for the actual location of this output file.

            When the custom classifier job is finished, the service creates the output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
            matrix.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **ClassifierMetadata** *(dict) --*

          Information about the document classifier, including the number of documents used for
          training the classifier, the number of documents used for test the classifier, and an
          accuracy rating.

          - **NumberOfLabels** *(integer) --*

            The number of labels in the input data.

          - **NumberOfTrainedDocuments** *(integer) --*

            The number of documents in the input data that were used to train the classifier.
            Typically this is 80 to 90 percent of the input documents.

          - **NumberOfTestDocuments** *(integer) --*

            The number of documents in the input data that were used to test the classifier.
            Typically this is 10 to 20 percent of the input documents.

          - **EvaluationMetrics** *(dict) --*

            Describes the result metrics for the test data associated with an documentation
            classifier.

            - **Accuracy** *(float) --*

              The fraction of the labels that were correct recognized. It is computed by dividing
              the number of labels in the test documents that were correctly recognized by the
              total number of labels in the test documents.

            - **Precision** *(float) --*

              A measure of the usefulness of the classifier results in the test data. High
              precision means that the classifier returned substantially more relevant results than
              irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the classifier results are for the test data. High recall
              means that the classifier returned most of the relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the classifier results are for the test data. It is derived
              from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
              of the two scores. The highest score is 1, and the worst score is 0.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your custom classifier. For more information, see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListDominantLanguageDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateFilterTypeDef(
    _ListDominantLanguageDetectionJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginate` `Filter`

    Filters that jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginate` `PaginationConfig`

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


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the dominant language
    detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your dominant language detection job. For more information,
    see `Amazon VPC
    <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginateResponse` `DominantLanguageDetectionJobPropertiesList`

    Provides information about a dominant language detection job.

    - **JobId** *(string) --*

      The identifier assigned to the dominant language detection job.

    - **JobName** *(string) --*

      The name that you assigned to the dominant language detection job.

    - **JobStatus** *(string) --*

      The current status of the dominant language detection job. If the status is ``FAILED`` ,
      the ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the dominant language detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the dominant language detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the dominant language
      detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your dominant language detection job. For more information,
      see `Amazon VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListDominantLanguageDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListDominantLanguageDetectionJobsPaginateResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            ListDominantLanguageDetectionJobsPaginateResponseDominantLanguageDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListDominantLanguageDetectionJobsPaginateResponseTypeDef(
    _ListDominantLanguageDetectionJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListDominantLanguageDetectionJobsPaginate` `Response`

    - **DominantLanguageDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a dominant language detection job.

        - **JobId** *(string) --*

          The identifier assigned to the dominant language detection job.

        - **JobName** *(string) --*

          The name that you assigned to the dominant language detection job.

        - **JobStatus** *(string) --*

          The current status of the dominant language detection job. If the status is ``FAILED`` ,
          the ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description for the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the dominant language detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the dominant language detection job completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the dominant language
          detection job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the dominant language
          detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your dominant language detection job. For more information,
          see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListEntitiesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateFilterTypeDef(
    _ListEntitiesDetectionJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginate` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef(
    _ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginate` `PaginationConfig`

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


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the entities detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the entities detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your entity detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginateResponse` `EntitiesDetectionJobPropertiesList`

    Provides information about an entities detection job.

    - **JobId** *(string) --*

      The identifier assigned to the entities detection job.

    - **JobName** *(string) --*

      The name that you assigned the entities detection job.

    - **JobStatus** *(string) --*

      The current status of the entities detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the entities detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the entities detection job completed

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the entities detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the entities detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your entity detection job. For more information, see `Amazon
      VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListEntitiesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListEntitiesDetectionJobsPaginateResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[
            ListEntitiesDetectionJobsPaginateResponseEntitiesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListEntitiesDetectionJobsPaginateResponseTypeDef(
    _ListEntitiesDetectionJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListEntitiesDetectionJobsPaginate` `Response`

    - **EntitiesDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about an entities detection job.

        - **JobId** *(string) --*

          The identifier assigned to the entities detection job.

        - **JobName** *(string) --*

          The name that you assigned the entities detection job.

        - **JobStatus** *(string) --*

          The current status of the entities detection job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the entities detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the entities detection job completed

        - **EntityRecognizerArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the entities detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the entities detection
          job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your entity detection job. For more information, see `Amazon
          VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListEntityRecognizersPaginateFilterTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateFilterTypeDef",
    {"Status": str, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)


class ListEntityRecognizersPaginateFilterTypeDef(
    _ListEntityRecognizersPaginateFilterTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginate` `Filter`

    Filters the list of entities returned. You can filter on ``Status`` , ``SubmitTimeBefore`` , or
    ``SubmitTimeAfter`` . You can only set one filter at a time.

    - **Status** *(string) --*

      The status of an entity recognizer.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of entities based on the time that the list was submitted for processing.
      Returns only jobs submitted before the specified time. Jobs are returned in descending order,
      newest to oldest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of entities based on the time that the list was submitted for processing.
      Returns only jobs submitted after the specified time. Jobs are returned in ascending order,
      oldest to newest.
    """


_ListEntityRecognizersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntityRecognizersPaginatePaginationConfigTypeDef(
    _ListEntityRecognizersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginate` `PaginationConfig`

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


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfig` `Annotations`

    S3 location of the annotations file for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the annotations for an entity recognizer are
      located. The URI must be in the same region as the API endpoint that you are calling.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfig` `Documents`

    S3 location of the documents folder for an entity recognizer

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the training documents for an entity
      recognizer are located. The URI must be in the same region as the API endpoint that
      you are calling.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef",
    {"S3Uri": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfig` `EntityList`

    S3 location of the entity list for an entity recognizer.

    - **S3Uri** *(string) --*

      Specifies the Amazon S3 location where the entity list is located. The URI must be in
      the same region as the API endpoint that you are calling.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef",
    {"Type": str},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfig` `EntityTypes`

    Information about an individual item on a list of entity types.

    - **Type** *(string) --*

      Entity type of an item on an entity type list.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef",
    {
        "EntityTypes": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityTypesTypeDef
        ],
        "Documents": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigDocumentsTypeDef,
        "Annotations": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigAnnotationsTypeDef,
        "EntityList": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigEntityListTypeDef,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesList` `InputDataConfig`

    The input data properties of an entity recognizer.

    - **EntityTypes** *(list) --*

      The entity types in the input data for an entity recognizer. A maximum of 12 entity
      types can be used at one time to train an entity recognizer.

      - *(dict) --*

        Information about an individual item on a list of entity types.

        - **Type** *(string) --*

          Entity type of an item on an entity type list.

    - **Documents** *(dict) --*

      S3 location of the documents folder for an entity recognizer

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the training documents for an entity
        recognizer are located. The URI must be in the same region as the API endpoint that
        you are calling.

    - **Annotations** *(dict) --*

      S3 location of the annotations file for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the annotations for an entity recognizer are
        located. The URI must be in the same region as the API endpoint that you are calling.

    - **EntityList** *(dict) --*

      S3 location of the entity list for an entity recognizer.

      - **S3Uri** *(string) --*

        Specifies the Amazon S3 location where the entity list is located. The URI must be in
        the same region as the API endpoint that you are calling.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypes` `EvaluationMetrics`

    Detailed information about the accuracy of the entity recognizer for a specific
    item on the list of entity types.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results for a specific entity type
      in the test data. High precision means that the recognizer returned substantially
      more relevant results than irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for a specific entity type
      in the test data. High recall means that the recognizer returned most of the
      relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for for a specific entity
      type in the test data. It is derived from the ``Precision`` and ``Recall``
      values. The ``F1Score`` is the harmonic average of the two scores. The highest
      score is 1, and the worst score is 0.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesEvaluationMetricsTypeDef,
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadata` `EntityTypes`

    Individual item from the list of entity types in the metadata of an entity recognizer.

    - **Type** *(string) --*

      Type of entity from the list of entity types in the metadata of an entity
      recognizer.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of the entity recognizer for a specific
      item on the list of entity types.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results for a specific entity type
        in the test data. High precision means that the recognizer returned substantially
        more relevant results than irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for a specific entity type
        in the test data. High recall means that the recognizer returned most of the
        relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for for a specific entity
        type in the test data. It is derived from the ``Precision`` and ``Recall``
        values. The ``F1Score`` is the harmonic average of the two scores. The highest
        score is 1, and the worst score is 0.

    - **NumberOfTrainMentions** *(integer) --*

      Indicates the number of times the given entity type was seen in the training data.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadata` `EvaluationMetrics`

    Detailed information about the accuracy of an entity recognizer.

    - **Precision** *(float) --*

      A measure of the usefulness of the recognizer results in the test data. High
      precision means that the recognizer returned substantially more relevant results than
      irrelevant ones.

    - **Recall** *(float) --*

      A measure of how complete the recognizer results are for the test data. High recall
      means that the recognizer returned most of the relevant results.

    - **F1Score** *(float) --*

      A measure of how accurate the recognizer results are for the test data. It is derived
      from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
      of the two scores. The highest score is 1, and the worst score is 0.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEvaluationMetricsTypeDef,
        "EntityTypes": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataEntityTypesTypeDef
        ],
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesList` `RecognizerMetadata`

    Provides information about an entity recognizer.

    - **NumberOfTrainedDocuments** *(integer) --*

      The number of documents in the input data that were used to train the entity
      recognizer. Typically this is 80 to 90 percent of the input documents.

    - **NumberOfTestDocuments** *(integer) --*

      The number of documents in the input data that were used to test the entity recognizer.
      Typically this is 10 to 20 percent of the input documents.

    - **EvaluationMetrics** *(dict) --*

      Detailed information about the accuracy of an entity recognizer.

      - **Precision** *(float) --*

        A measure of the usefulness of the recognizer results in the test data. High
        precision means that the recognizer returned substantially more relevant results than
        irrelevant ones.

      - **Recall** *(float) --*

        A measure of how complete the recognizer results are for the test data. High recall
        means that the recognizer returned most of the relevant results.

      - **F1Score** *(float) --*

        A measure of how accurate the recognizer results are for the test data. It is derived
        from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
        of the two scores. The highest score is 1, and the worst score is 0.

    - **EntityTypes** *(list) --*

      Entity types from the metadata of an entity recognizer.

      - *(dict) --*

        Individual item from the list of entity types in the metadata of an entity recognizer.

        - **Type** *(string) --*

          Type of entity from the list of entity types in the metadata of an entity
          recognizer.

        - **EvaluationMetrics** *(dict) --*

          Detailed information about the accuracy of the entity recognizer for a specific
          item on the list of entity types.

          - **Precision** *(float) --*

            A measure of the usefulness of the recognizer results for a specific entity type
            in the test data. High precision means that the recognizer returned substantially
            more relevant results than irrelevant ones.

          - **Recall** *(float) --*

            A measure of how complete the recognizer results are for a specific entity type
            in the test data. High recall means that the recognizer returned most of the
            relevant results.

          - **F1Score** *(float) --*

            A measure of how accurate the recognizer results are for for a specific entity
            type in the test data. It is derived from the ``Precision`` and ``Recall``
            values. The ``F1Score`` is the harmonic average of the two scores. The highest
            score is 1, and the worst score is 0.

        - **NumberOfTrainMentions** *(integer) --*

          Indicates the number of times the given entity type was seen in the training data.
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your custom entity recognizer. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": str,
        "Status": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListInputDataConfigTypeDef,
        "RecognizerMetadata": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListRecognizerMetadataTypeDef,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef(
    _ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginateResponse` `EntityRecognizerPropertiesList`

    Describes information about an entity recognizer.

    - **EntityRecognizerArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the entity recognizer.

    - **LanguageCode** *(string) --*

      The language of the input documents. All documents must be in the same language. Only
      English ("en") is currently supported.

    - **Status** *(string) --*

      Provides the status of the entity recognizer.

    - **Message** *(string) --*

      A description of the status of the recognizer.

    - **SubmitTime** *(datetime) --*

      The time that the recognizer was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the recognizer creation completed.

    - **TrainingStartTime** *(datetime) --*

      The time that training of the entity recognizer started.

    - **TrainingEndTime** *(datetime) --*

      The time that training of the entity recognizer was completed.

    - **InputDataConfig** *(dict) --*

      The input data properties of an entity recognizer.

      - **EntityTypes** *(list) --*

        The entity types in the input data for an entity recognizer. A maximum of 12 entity
        types can be used at one time to train an entity recognizer.

        - *(dict) --*

          Information about an individual item on a list of entity types.

          - **Type** *(string) --*

            Entity type of an item on an entity type list.

      - **Documents** *(dict) --*

        S3 location of the documents folder for an entity recognizer

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the training documents for an entity
          recognizer are located. The URI must be in the same region as the API endpoint that
          you are calling.

      - **Annotations** *(dict) --*

        S3 location of the annotations file for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the annotations for an entity recognizer are
          located. The URI must be in the same region as the API endpoint that you are calling.

      - **EntityList** *(dict) --*

        S3 location of the entity list for an entity recognizer.

        - **S3Uri** *(string) --*

          Specifies the Amazon S3 location where the entity list is located. The URI must be in
          the same region as the API endpoint that you are calling.

    - **RecognizerMetadata** *(dict) --*

      Provides information about an entity recognizer.

      - **NumberOfTrainedDocuments** *(integer) --*

        The number of documents in the input data that were used to train the entity
        recognizer. Typically this is 80 to 90 percent of the input documents.

      - **NumberOfTestDocuments** *(integer) --*

        The number of documents in the input data that were used to test the entity recognizer.
        Typically this is 10 to 20 percent of the input documents.

      - **EvaluationMetrics** *(dict) --*

        Detailed information about the accuracy of an entity recognizer.

        - **Precision** *(float) --*

          A measure of the usefulness of the recognizer results in the test data. High
          precision means that the recognizer returned substantially more relevant results than
          irrelevant ones.

        - **Recall** *(float) --*

          A measure of how complete the recognizer results are for the test data. High recall
          means that the recognizer returned most of the relevant results.

        - **F1Score** *(float) --*

          A measure of how accurate the recognizer results are for the test data. It is derived
          from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
          of the two scores. The highest score is 1, and the worst score is 0.

      - **EntityTypes** *(list) --*

        Entity types from the metadata of an entity recognizer.

        - *(dict) --*

          Individual item from the list of entity types in the metadata of an entity recognizer.

          - **Type** *(string) --*

            Type of entity from the list of entity types in the metadata of an entity
            recognizer.

          - **EvaluationMetrics** *(dict) --*

            Detailed information about the accuracy of the entity recognizer for a specific
            item on the list of entity types.

            - **Precision** *(float) --*

              A measure of the usefulness of the recognizer results for a specific entity type
              in the test data. High precision means that the recognizer returned substantially
              more relevant results than irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the recognizer results are for a specific entity type
              in the test data. High recall means that the recognizer returned most of the
              relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the recognizer results are for for a specific entity
              type in the test data. It is derived from the ``Precision`` and ``Recall``
              values. The ``F1Score`` is the harmonic average of the two scores. The highest
              score is 1, and the worst score is 0.

          - **NumberOfTrainMentions** *(integer) --*

            Indicates the number of times the given entity type was seen in the training data.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your input data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your custom entity recognizer. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListEntityRecognizersPaginateResponseTypeDef = TypedDict(
    "_ListEntityRecognizersPaginateResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[
            ListEntityRecognizersPaginateResponseEntityRecognizerPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListEntityRecognizersPaginateResponseTypeDef(
    _ListEntityRecognizersPaginateResponseTypeDef
):
    """
    Type definition for `ListEntityRecognizersPaginate` `Response`

    - **EntityRecognizerPropertiesList** *(list) --*

      The list of properties of an entity recognizer.

      - *(dict) --*

        Describes information about an entity recognizer.

        - **EntityRecognizerArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        - **LanguageCode** *(string) --*

          The language of the input documents. All documents must be in the same language. Only
          English ("en") is currently supported.

        - **Status** *(string) --*

          Provides the status of the entity recognizer.

        - **Message** *(string) --*

          A description of the status of the recognizer.

        - **SubmitTime** *(datetime) --*

          The time that the recognizer was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the recognizer creation completed.

        - **TrainingStartTime** *(datetime) --*

          The time that training of the entity recognizer started.

        - **TrainingEndTime** *(datetime) --*

          The time that training of the entity recognizer was completed.

        - **InputDataConfig** *(dict) --*

          The input data properties of an entity recognizer.

          - **EntityTypes** *(list) --*

            The entity types in the input data for an entity recognizer. A maximum of 12 entity
            types can be used at one time to train an entity recognizer.

            - *(dict) --*

              Information about an individual item on a list of entity types.

              - **Type** *(string) --*

                Entity type of an item on an entity type list.

          - **Documents** *(dict) --*

            S3 location of the documents folder for an entity recognizer

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the training documents for an entity
              recognizer are located. The URI must be in the same region as the API endpoint that
              you are calling.

          - **Annotations** *(dict) --*

            S3 location of the annotations file for an entity recognizer.

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the annotations for an entity recognizer are
              located. The URI must be in the same region as the API endpoint that you are calling.

          - **EntityList** *(dict) --*

            S3 location of the entity list for an entity recognizer.

            - **S3Uri** *(string) --*

              Specifies the Amazon S3 location where the entity list is located. The URI must be in
              the same region as the API endpoint that you are calling.

        - **RecognizerMetadata** *(dict) --*

          Provides information about an entity recognizer.

          - **NumberOfTrainedDocuments** *(integer) --*

            The number of documents in the input data that were used to train the entity
            recognizer. Typically this is 80 to 90 percent of the input documents.

          - **NumberOfTestDocuments** *(integer) --*

            The number of documents in the input data that were used to test the entity recognizer.
            Typically this is 10 to 20 percent of the input documents.

          - **EvaluationMetrics** *(dict) --*

            Detailed information about the accuracy of an entity recognizer.

            - **Precision** *(float) --*

              A measure of the usefulness of the recognizer results in the test data. High
              precision means that the recognizer returned substantially more relevant results than
              irrelevant ones.

            - **Recall** *(float) --*

              A measure of how complete the recognizer results are for the test data. High recall
              means that the recognizer returned most of the relevant results.

            - **F1Score** *(float) --*

              A measure of how accurate the recognizer results are for the test data. It is derived
              from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the harmonic average
              of the two scores. The highest score is 1, and the worst score is 0.

          - **EntityTypes** *(list) --*

            Entity types from the metadata of an entity recognizer.

            - *(dict) --*

              Individual item from the list of entity types in the metadata of an entity recognizer.

              - **Type** *(string) --*

                Type of entity from the list of entity types in the metadata of an entity
                recognizer.

              - **EvaluationMetrics** *(dict) --*

                Detailed information about the accuracy of the entity recognizer for a specific
                item on the list of entity types.

                - **Precision** *(float) --*

                  A measure of the usefulness of the recognizer results for a specific entity type
                  in the test data. High precision means that the recognizer returned substantially
                  more relevant results than irrelevant ones.

                - **Recall** *(float) --*

                  A measure of how complete the recognizer results are for a specific entity type
                  in the test data. High recall means that the recognizer returned most of the
                  relevant results.

                - **F1Score** *(float) --*

                  A measure of how accurate the recognizer results are for for a specific entity
                  type in the test data. It is derived from the ``Precision`` and ``Recall``
                  values. The ``F1Score`` is the harmonic average of the two scores. The highest
                  score is 1, and the worst score is 0.

              - **NumberOfTrainMentions** *(integer) --*

                Indicates the number of times the given entity type was seen in the training data.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your custom entity recognizer. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListKeyPhrasesDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateFilterTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginate` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginate` `PaginationConfig`

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


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the key phrases detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the key phrases
    detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your key phrases detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginateResponse` `KeyPhrasesDetectionJobPropertiesList`

    Provides information about a key phrases detection job.

    - **JobId** *(string) --*

      The identifier assigned to the key phrases detection job.

    - **JobName** *(string) --*

      The name that you assigned the key phrases detection job.

    - **JobStatus** *(string) --*

      The current status of the key phrases detection job. If the status is ``FAILED`` , the
      ``Message`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the key phrases detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the key phrases detection job completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the key phrases detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the key phrases
      detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your key phrases detection job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListKeyPhrasesDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListKeyPhrasesDetectionJobsPaginateResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            ListKeyPhrasesDetectionJobsPaginateResponseKeyPhrasesDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListKeyPhrasesDetectionJobsPaginateResponseTypeDef(
    _ListKeyPhrasesDetectionJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListKeyPhrasesDetectionJobsPaginate` `Response`

    - **KeyPhrasesDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a key phrases detection job.

        - **JobId** *(string) --*

          The identifier assigned to the key phrases detection job.

        - **JobName** *(string) --*

          The name that you assigned the key phrases detection job.

        - **JobStatus** *(string) --*

          The current status of the key phrases detection job. If the status is ``FAILED`` , the
          ``Message`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the key phrases detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the key phrases detection job completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the key phrases detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the key phrases
          detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your key phrases detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListSentimentDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateFilterTypeDef(
    _ListSentimentDetectionJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginate` `Filter`

    Filters the jobs that are returned. You can filter jobs on their name, status, or the date and
    time that they were submitted. You can only set one filter at a time.

    - **JobName** *(string) --*

      Filters on the name of the job.

    - **JobStatus** *(string) --*

      Filters the list of jobs based on job status. Returns only jobs with the specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to
      newest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Returns
      only jobs submitted after the specified time. Jobs are returned in descending order, newest to
      oldest.
    """


_ListSentimentDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSentimentDetectionJobsPaginatePaginationConfigTypeDef(
    _ListSentimentDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginate` `PaginationConfig`

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


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration that you supplied when you created the sentiment detection
    job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration that you supplied when you created the sentiment detection
    job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your sentiment detection job. For more information, see
    `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
    .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef(
    _ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginateResponse` `SentimentDetectionJobPropertiesList`

    Provides information about a sentiment detection job.

    - **JobId** *(string) --*

      The identifier assigned to the sentiment detection job.

    - **JobName** *(string) --*

      The name that you assigned to the sentiment detection job

    - **JobStatus** *(string) --*

      The current status of the sentiment detection job. If the status is ``FAILED`` , the
      ``Messages`` field shows the reason for the failure.

    - **Message** *(string) --*

      A description of the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the sentiment detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the sentiment detection job ended.

    - **InputDataConfig** *(dict) --*

      The input data configuration that you supplied when you created the sentiment detection
      job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration that you supplied when you created the sentiment detection
      job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **LanguageCode** *(string) --*

      The language code of the input documents.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
      data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your sentiment detection job. For more information, see
      `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
      .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListSentimentDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListSentimentDetectionJobsPaginateResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            ListSentimentDetectionJobsPaginateResponseSentimentDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListSentimentDetectionJobsPaginateResponseTypeDef(
    _ListSentimentDetectionJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListSentimentDetectionJobsPaginate` `Response`

    - **SentimentDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a sentiment detection job.

        - **JobId** *(string) --*

          The identifier assigned to the sentiment detection job.

        - **JobName** *(string) --*

          The name that you assigned to the sentiment detection job

        - **JobStatus** *(string) --*

          The current status of the sentiment detection job. If the status is ``FAILED`` , the
          ``Messages`` field shows the reason for the failure.

        - **Message** *(string) --*

          A description of the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the sentiment detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the sentiment detection job ended.

        - **InputDataConfig** *(dict) --*

          The input data configuration that you supplied when you created the sentiment detection
          job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration that you supplied when you created the sentiment detection
          job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **LanguageCode** *(string) --*

          The language code of the input documents.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your input
          data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your sentiment detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """


_ListTopicsDetectionJobsPaginateFilterTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": str,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateFilterTypeDef(
    _ListTopicsDetectionJobsPaginateFilterTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginate` `Filter`

    Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and
    time that they were submitted. You can set only one filter at a time.

    - **JobName** *(string) --*

    - **JobStatus** *(string) --*

      Filters the list of topic detection jobs based on job status. Returns only jobs with the
      specified status.

    - **SubmitTimeBefore** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Only
      returns jobs submitted before the specified time. Jobs are returned in descending order, newest
      to oldest.

    - **SubmitTimeAfter** *(datetime) --*

      Filters the list of jobs based on the time that the job was submitted for processing. Only
      returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest
      to newest.
    """


_ListTopicsDetectionJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTopicsDetectionJobsPaginatePaginationConfigTypeDef(
    _ListTopicsDetectionJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginate` `PaginationConfig`

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


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "InputFormat": str},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesList` `InputDataConfig`

    The input data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      The Amazon S3 URI for the input data. The URI must be in same region as the API
      endpoint that you are calling. The URI can point to a single input file or it can
      provide the prefix for a collection of data files.

      For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
      file, Amazon Comprehend uses that file as input. If more than one file begins with the
      prefix, Amazon Comprehend uses all of them as input.

    - **InputFormat** *(string) --*

      Specifies how the text in an input file should be processed:

      * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
      when you are processing large documents, such as newspaper articles or scientific
      papers.

      * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
      this option when you are processing many short documents, such as text messages.
    """


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str, "KmsKeyId": str},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesList` `OutputDataConfig`

    The output data configuration supplied when you created the topic detection job.

    - **S3Uri** *(string) --*

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
      the Amazon S3 location where you want to write the output data. The URI must be in the
      same region as the API endpoint that you are calling. The location is used as the
      prefix for the actual location of the output file.

      When the topic detection job is finished, the service creates an output file in a
      directory specific to the job. The ``S3Uri`` field contains the location of the output
      file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
      the operation.

    - **KmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      the output results from an analysis job. The KmsKeyId can be one of the following
      formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

      * KMS Key Alias: ``"alias/ExampleAlias"``

      * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
    """


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesList` `VpcConfig`

    Configuration parameters for a private Virtual Private Cloud (VPC) containing the
    resources you are using for your topic detection job. For more information, see `Amazon
    VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

    - **SecurityGroupIds** *(list) --*

      The ID number for a security group on an instance of your private VPC. Security groups
      on your VPC function serve as a virtual firewall to control inbound and outbound
      traffic and provides security for the resources that you’ll be accessing on the VPC.
      This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
      information, see `Security Groups for your VPC
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

      - *(string) --*

    - **Subnets** *(list) --*

      The ID for each subnet being used in your private VPC. This subnet is a subset of the a
      range of IPv4 addresses used by the VPC and is specific to a given availability zone in
      the VPC’s region. This ID number is preceded by "subnet-", for instance:
      "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

      - *(string) --*
    """


_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": str,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListOutputDataConfigTypeDef,
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListVpcConfigTypeDef,
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginateResponse` `TopicsDetectionJobPropertiesList`

    Provides information about a topic detection job.

    - **JobId** *(string) --*

      The identifier assigned to the topic detection job.

    - **JobName** *(string) --*

      The name of the topic detection job.

    - **JobStatus** *(string) --*

      The current status of the topic detection job. If the status is ``Failed`` , the reason
      for the failure is shown in the ``Message`` field.

    - **Message** *(string) --*

      A description for the status of a job.

    - **SubmitTime** *(datetime) --*

      The time that the topic detection job was submitted for processing.

    - **EndTime** *(datetime) --*

      The time that the topic detection job was completed.

    - **InputDataConfig** *(dict) --*

      The input data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        The Amazon S3 URI for the input data. The URI must be in same region as the API
        endpoint that you are calling. The URI can point to a single input file or it can
        provide the prefix for a collection of data files.

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
        file, Amazon Comprehend uses that file as input. If more than one file begins with the
        prefix, Amazon Comprehend uses all of them as input.

      - **InputFormat** *(string) --*

        Specifies how the text in an input file should be processed:

        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
        when you are processing large documents, such as newspaper articles or scientific
        papers.

        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
        this option when you are processing many short documents, such as text messages.

    - **OutputDataConfig** *(dict) --*

      The output data configuration supplied when you created the topic detection job.

      - **S3Uri** *(string) --*

        When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
        the Amazon S3 location where you want to write the output data. The URI must be in the
        same region as the API endpoint that you are calling. The location is used as the
        prefix for the actual location of the output file.

        When the topic detection job is finished, the service creates an output file in a
        directory specific to the job. The ``S3Uri`` field contains the location of the output
        file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
        the operation.

      - **KmsKeyId** *(string) --*

        ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
        the output results from an analysis job. The KmsKeyId can be one of the following
        formats:

        * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

        * Amazon Resource Name (ARN) of a KMS Key:
        ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        * KMS Key Alias: ``"alias/ExampleAlias"``

        * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

    - **NumberOfTopics** *(integer) --*

      The number of topics to detect supplied when you created the topic detection job. The
      default is 10.

    - **DataAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
      Amazon Comprehend read access to your job data.

    - **VolumeKmsKeyId** *(string) --*

      ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
      data on the storage volume attached to the ML compute instance(s) that process the
      analysis job. The VolumeKmsKeyId can be either of the following formats:

      * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

      * Amazon Resource Name (ARN) of a KMS Key:
      ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

    - **VpcConfig** *(dict) --*

      Configuration parameters for a private Virtual Private Cloud (VPC) containing the
      resources you are using for your topic detection job. For more information, see `Amazon
      VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

      - **SecurityGroupIds** *(list) --*

        The ID number for a security group on an instance of your private VPC. Security groups
        on your VPC function serve as a virtual firewall to control inbound and outbound
        traffic and provides security for the resources that you’ll be accessing on the VPC.
        This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
        information, see `Security Groups for your VPC
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

        - *(string) --*

      - **Subnets** *(list) --*

        The ID for each subnet being used in your private VPC. This subnet is a subset of the a
        range of IPv4 addresses used by the VPC and is specific to a given availability zone in
        the VPC’s region. This ID number is preceded by "subnet-", for instance:
        "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

        - *(string) --*
    """


_ListTopicsDetectionJobsPaginateResponseTypeDef = TypedDict(
    "_ListTopicsDetectionJobsPaginateResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[
            ListTopicsDetectionJobsPaginateResponseTopicsDetectionJobPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListTopicsDetectionJobsPaginateResponseTypeDef(
    _ListTopicsDetectionJobsPaginateResponseTypeDef
):
    """
    Type definition for `ListTopicsDetectionJobsPaginate` `Response`

    - **TopicsDetectionJobPropertiesList** *(list) --*

      A list containing the properties of each job that is returned.

      - *(dict) --*

        Provides information about a topic detection job.

        - **JobId** *(string) --*

          The identifier assigned to the topic detection job.

        - **JobName** *(string) --*

          The name of the topic detection job.

        - **JobStatus** *(string) --*

          The current status of the topic detection job. If the status is ``Failed`` , the reason
          for the failure is shown in the ``Message`` field.

        - **Message** *(string) --*

          A description for the status of a job.

        - **SubmitTime** *(datetime) --*

          The time that the topic detection job was submitted for processing.

        - **EndTime** *(datetime) --*

          The time that the topic detection job was completed.

        - **InputDataConfig** *(dict) --*

          The input data configuration supplied when you created the topic detection job.

          - **S3Uri** *(string) --*

            The Amazon S3 URI for the input data. The URI must be in same region as the API
            endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use
            this option when you are processing many short documents, such as text messages.

        - **OutputDataConfig** *(dict) --*

          The output data configuration supplied when you created the topic detection job.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the
            prefix for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        - **NumberOfTopics** *(integer) --*

          The number of topics to detect supplied when you created the topic detection job. The
          default is 10.

        - **DataAccessRoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your job data.

        - **VolumeKmsKeyId** *(string) --*

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        - **VpcConfig** *(dict) --*

          Configuration parameters for a private Virtual Private Cloud (VPC) containing the
          resources you are using for your topic detection job. For more information, see `Amazon
          VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --*

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound
            traffic and provides security for the resources that you’ll be accessing on the VPC.
            This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more
            information, see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --*

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*
    """
