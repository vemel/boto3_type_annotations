"Main interface for translate type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientGetTerminologyResponseTypeDef",
    "ClientImportTerminologyEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientImportTerminologyResponseTypeDef",
    "ClientImportTerminologyTerminologyDataTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    "ClientListTerminologiesResponseTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    "ClientTranslateTextResponseTypeDef",
    "ListTerminologiesPaginatePaginationConfigTypeDef",
    "ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    "ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef",
    "ListTerminologiesPaginateResponseTypeDef",
)


_ClientGetTerminologyResponseTerminologyDataLocationTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    {"RepositoryType": str, "Location": str},
    total=False,
)


class ClientGetTerminologyResponseTerminologyDataLocationTypeDef(
    _ClientGetTerminologyResponseTerminologyDataLocationTypeDef
):
    """
    Type definition for `ClientGetTerminologyResponse` `TerminologyDataLocation`

    The data location of the custom terminology being retrieved. The custom terminology file is
    returned in a presigned url that has a 30 minute expiration.

    - **RepositoryType** *(string) --*

      The repository type for the custom terminology data.

    - **Location** *(string) --*

      The location of the custom terminology data.
    """


_ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef(
    _ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef
):
    """
    Type definition for `ClientGetTerminologyResponseTerminologyProperties` `EncryptionKey`

    The encryption key for the custom terminology.

    - **Type** *(string) --*

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.

    - **Id** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
      terminology.
    """


_ClientGetTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientGetTerminologyResponseTerminologyPropertiesTypeDef(
    _ClientGetTerminologyResponseTerminologyPropertiesTypeDef
):
    """
    Type definition for `ClientGetTerminologyResponse` `TerminologyProperties`

    The properties of the custom terminology being retrieved.

    - **Name** *(string) --*

      The name of the custom terminology.

    - **Description** *(string) --*

      The description of the custom terminology properties.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the custom terminology.

    - **SourceLanguageCode** *(string) --*

      The language code for the source text of the translation request for which the custom
      terminology is being used.

    - **TargetLanguageCodes** *(list) --*

      The language codes for the target languages available with the custom terminology file. All
      possible target languages are returned in array.

      - *(string) --*

    - **EncryptionKey** *(dict) --*

      The encryption key for the custom terminology.

      - **Type** *(string) --*

        The type of encryption key used by Amazon Translate to encrypt custom terminologies.

      - **Id** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
        terminology.

    - **SizeBytes** *(integer) --*

      The size of the file used when importing a custom terminology.

    - **TermCount** *(integer) --*

      The number of terms included in the custom terminology.

    - **CreatedAt** *(datetime) --*

      The time at which the custom terminology was created, based on the timestamp.

    - **LastUpdatedAt** *(datetime) --*

      The time at which the custom terminology was last update, based on the timestamp.
    """


_ClientGetTerminologyResponseTypeDef = TypedDict(
    "_ClientGetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": ClientGetTerminologyResponseTerminologyPropertiesTypeDef,
        "TerminologyDataLocation": ClientGetTerminologyResponseTerminologyDataLocationTypeDef,
    },
    total=False,
)


class ClientGetTerminologyResponseTypeDef(_ClientGetTerminologyResponseTypeDef):
    """
    Type definition for `ClientGetTerminology` `Response`

    - **TerminologyProperties** *(dict) --*

      The properties of the custom terminology being retrieved.

      - **Name** *(string) --*

        The name of the custom terminology.

      - **Description** *(string) --*

        The description of the custom terminology properties.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the custom terminology.

      - **SourceLanguageCode** *(string) --*

        The language code for the source text of the translation request for which the custom
        terminology is being used.

      - **TargetLanguageCodes** *(list) --*

        The language codes for the target languages available with the custom terminology file. All
        possible target languages are returned in array.

        - *(string) --*

      - **EncryptionKey** *(dict) --*

        The encryption key for the custom terminology.

        - **Type** *(string) --*

          The type of encryption key used by Amazon Translate to encrypt custom terminologies.

        - **Id** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
          terminology.

      - **SizeBytes** *(integer) --*

        The size of the file used when importing a custom terminology.

      - **TermCount** *(integer) --*

        The number of terms included in the custom terminology.

      - **CreatedAt** *(datetime) --*

        The time at which the custom terminology was created, based on the timestamp.

      - **LastUpdatedAt** *(datetime) --*

        The time at which the custom terminology was last update, based on the timestamp.

    - **TerminologyDataLocation** *(dict) --*

      The data location of the custom terminology being retrieved. The custom terminology file is
      returned in a presigned url that has a 30 minute expiration.

      - **RepositoryType** *(string) --*

        The repository type for the custom terminology data.

      - **Location** *(string) --*

        The location of the custom terminology data.
    """


_ClientImportTerminologyEncryptionKeyTypeDef = TypedDict(
    "_ClientImportTerminologyEncryptionKeyTypeDef", {"Type": str, "Id": str}
)


class ClientImportTerminologyEncryptionKeyTypeDef(
    _ClientImportTerminologyEncryptionKeyTypeDef
):
    """
    Type definition for `ClientImportTerminology` `EncryptionKey`

    The encryption key for the custom terminology being imported.

    - **Type** *(string) --* **[REQUIRED]**

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.

    - **Id** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
      terminology.
    """


_ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef(
    _ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef
):
    """
    Type definition for `ClientImportTerminologyResponseTerminologyProperties` `EncryptionKey`

    The encryption key for the custom terminology.

    - **Type** *(string) --*

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.

    - **Id** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
      terminology.
    """


_ClientImportTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientImportTerminologyResponseTerminologyPropertiesTypeDef(
    _ClientImportTerminologyResponseTerminologyPropertiesTypeDef
):
    """
    Type definition for `ClientImportTerminologyResponse` `TerminologyProperties`

    The properties of the custom terminology being imported.

    - **Name** *(string) --*

      The name of the custom terminology.

    - **Description** *(string) --*

      The description of the custom terminology properties.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the custom terminology.

    - **SourceLanguageCode** *(string) --*

      The language code for the source text of the translation request for which the custom
      terminology is being used.

    - **TargetLanguageCodes** *(list) --*

      The language codes for the target languages available with the custom terminology file. All
      possible target languages are returned in array.

      - *(string) --*

    - **EncryptionKey** *(dict) --*

      The encryption key for the custom terminology.

      - **Type** *(string) --*

        The type of encryption key used by Amazon Translate to encrypt custom terminologies.

      - **Id** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
        terminology.

    - **SizeBytes** *(integer) --*

      The size of the file used when importing a custom terminology.

    - **TermCount** *(integer) --*

      The number of terms included in the custom terminology.

    - **CreatedAt** *(datetime) --*

      The time at which the custom terminology was created, based on the timestamp.

    - **LastUpdatedAt** *(datetime) --*

      The time at which the custom terminology was last update, based on the timestamp.
    """


_ClientImportTerminologyResponseTypeDef = TypedDict(
    "_ClientImportTerminologyResponseTypeDef",
    {
        "TerminologyProperties": ClientImportTerminologyResponseTerminologyPropertiesTypeDef
    },
    total=False,
)


class ClientImportTerminologyResponseTypeDef(_ClientImportTerminologyResponseTypeDef):
    """
    Type definition for `ClientImportTerminology` `Response`

    - **TerminologyProperties** *(dict) --*

      The properties of the custom terminology being imported.

      - **Name** *(string) --*

        The name of the custom terminology.

      - **Description** *(string) --*

        The description of the custom terminology properties.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the custom terminology.

      - **SourceLanguageCode** *(string) --*

        The language code for the source text of the translation request for which the custom
        terminology is being used.

      - **TargetLanguageCodes** *(list) --*

        The language codes for the target languages available with the custom terminology file. All
        possible target languages are returned in array.

        - *(string) --*

      - **EncryptionKey** *(dict) --*

        The encryption key for the custom terminology.

        - **Type** *(string) --*

          The type of encryption key used by Amazon Translate to encrypt custom terminologies.

        - **Id** *(string) --*

          The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
          terminology.

      - **SizeBytes** *(integer) --*

        The size of the file used when importing a custom terminology.

      - **TermCount** *(integer) --*

        The number of terms included in the custom terminology.

      - **CreatedAt** *(datetime) --*

        The time at which the custom terminology was created, based on the timestamp.

      - **LastUpdatedAt** *(datetime) --*

        The time at which the custom terminology was last update, based on the timestamp.
    """


_ClientImportTerminologyTerminologyDataTypeDef = TypedDict(
    "_ClientImportTerminologyTerminologyDataTypeDef", {"File": bytes, "Format": str}
)


class ClientImportTerminologyTerminologyDataTypeDef(
    _ClientImportTerminologyTerminologyDataTypeDef
):
    """
    Type definition for `ClientImportTerminology` `TerminologyData`

    The terminology data for the custom terminology being imported.

    - **File** *(bytes) --* **[REQUIRED]**

      The file containing the custom terminology data.

    - **Format** *(string) --* **[REQUIRED]**

      The data format of the custom terminology. Either CSV or TMX.
    """


_ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef(
    _ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef
):
    """
    Type definition for `ClientListTerminologiesResponseTerminologyPropertiesList` `EncryptionKey`

    The encryption key for the custom terminology.

    - **Type** *(string) --*

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.

    - **Id** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
      terminology.
    """


_ClientListTerminologiesResponseTerminologyPropertiesListTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ClientListTerminologiesResponseTerminologyPropertiesListTypeDef(
    _ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
):
    """
    Type definition for `ClientListTerminologiesResponse` `TerminologyPropertiesList`

    The properties of the custom terminology.

    - **Name** *(string) --*

      The name of the custom terminology.

    - **Description** *(string) --*

      The description of the custom terminology properties.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the custom terminology.

    - **SourceLanguageCode** *(string) --*

      The language code for the source text of the translation request for which the custom
      terminology is being used.

    - **TargetLanguageCodes** *(list) --*

      The language codes for the target languages available with the custom terminology file.
      All possible target languages are returned in array.

      - *(string) --*

    - **EncryptionKey** *(dict) --*

      The encryption key for the custom terminology.

      - **Type** *(string) --*

        The type of encryption key used by Amazon Translate to encrypt custom terminologies.

      - **Id** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
        terminology.

    - **SizeBytes** *(integer) --*

      The size of the file used when importing a custom terminology.

    - **TermCount** *(integer) --*

      The number of terms included in the custom terminology.

    - **CreatedAt** *(datetime) --*

      The time at which the custom terminology was created, based on the timestamp.

    - **LastUpdatedAt** *(datetime) --*

      The time at which the custom terminology was last update, based on the timestamp.
    """


_ClientListTerminologiesResponseTypeDef = TypedDict(
    "_ClientListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListTerminologiesResponseTypeDef(_ClientListTerminologiesResponseTypeDef):
    """
    Type definition for `ClientListTerminologies` `Response`

    - **TerminologyPropertiesList** *(list) --*

      The properties list of the custom terminologies returned on the list request.

      - *(dict) --*

        The properties of the custom terminology.

        - **Name** *(string) --*

          The name of the custom terminology.

        - **Description** *(string) --*

          The description of the custom terminology properties.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the custom terminology.

        - **SourceLanguageCode** *(string) --*

          The language code for the source text of the translation request for which the custom
          terminology is being used.

        - **TargetLanguageCodes** *(list) --*

          The language codes for the target languages available with the custom terminology file.
          All possible target languages are returned in array.

          - *(string) --*

        - **EncryptionKey** *(dict) --*

          The encryption key for the custom terminology.

          - **Type** *(string) --*

            The type of encryption key used by Amazon Translate to encrypt custom terminologies.

          - **Id** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
            terminology.

        - **SizeBytes** *(integer) --*

          The size of the file used when importing a custom terminology.

        - **TermCount** *(integer) --*

          The number of terms included in the custom terminology.

        - **CreatedAt** *(datetime) --*

          The time at which the custom terminology was created, based on the timestamp.

        - **LastUpdatedAt** *(datetime) --*

          The time at which the custom terminology was last update, based on the timestamp.

    - **NextToken** *(string) --*

      If the response to the ListTerminologies was truncated, the NextToken fetches the next group
      of custom terminologies.
    """


_ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef = TypedDict(
    "_ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    {"SourceText": str, "TargetText": str},
    total=False,
)


class ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef(
    _ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef
):
    """
    Type definition for `ClientTranslateTextResponseAppliedTerminologies` `Terms`

    The term being translated by the custom terminology.

    - **SourceText** *(string) --*

      The source text of the term being translated by the custom terminology.

    - **TargetText** *(string) --*

      The target text of the term being translated by the custom terminology.
    """


_ClientTranslateTextResponseAppliedTerminologiesTypeDef = TypedDict(
    "_ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    {
        "Name": str,
        "Terms": List[ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef],
    },
    total=False,
)


class ClientTranslateTextResponseAppliedTerminologiesTypeDef(
    _ClientTranslateTextResponseAppliedTerminologiesTypeDef
):
    """
    Type definition for `ClientTranslateTextResponse` `AppliedTerminologies`

    The custom terminology applied to the input text by Amazon Translate for the translated
    text response. This is optional in the response and will only be present if you specified
    terminology input in the request. Currently, only one terminology can be applied per
    TranslateText request.

    - **Name** *(string) --*

      The name of the custom terminology applied to the input text by Amazon Translate for the
      translated text response.

    - **Terms** *(list) --*

      The specific terms of the custom terminology applied to the input text by Amazon
      Translate for the translated text response. A maximum of 250 terms will be returned, and
      the specific terms applied will be the first 250 terms in the source text.

      - *(dict) --*

        The term being translated by the custom terminology.

        - **SourceText** *(string) --*

          The source text of the term being translated by the custom terminology.

        - **TargetText** *(string) --*

          The target text of the term being translated by the custom terminology.
    """


_ClientTranslateTextResponseTypeDef = TypedDict(
    "_ClientTranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List[
            ClientTranslateTextResponseAppliedTerminologiesTypeDef
        ],
    },
    total=False,
)


class ClientTranslateTextResponseTypeDef(_ClientTranslateTextResponseTypeDef):
    """
    Type definition for `ClientTranslateText` `Response`

    - **TranslatedText** *(string) --*

      The the translated text. The maximum length of this text is 5kb.

    - **SourceLanguageCode** *(string) --*

      The language code for the language of the source text.

    - **TargetLanguageCode** *(string) --*

      The language code for the language of the target text.

    - **AppliedTerminologies** *(list) --*

      The names of the custom terminologies applied to the input text by Amazon Translate for the
      translated text response.

      - *(dict) --*

        The custom terminology applied to the input text by Amazon Translate for the translated
        text response. This is optional in the response and will only be present if you specified
        terminology input in the request. Currently, only one terminology can be applied per
        TranslateText request.

        - **Name** *(string) --*

          The name of the custom terminology applied to the input text by Amazon Translate for the
          translated text response.

        - **Terms** *(list) --*

          The specific terms of the custom terminology applied to the input text by Amazon
          Translate for the translated text response. A maximum of 250 terms will be returned, and
          the specific terms applied will be the first 250 terms in the source text.

          - *(dict) --*

            The term being translated by the custom terminology.

            - **SourceText** *(string) --*

              The source text of the term being translated by the custom terminology.

            - **TargetText** *(string) --*

              The target text of the term being translated by the custom terminology.
    """


_ListTerminologiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTerminologiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTerminologiesPaginatePaginationConfigTypeDef(
    _ListTerminologiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTerminologiesPaginate` `PaginationConfig`

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


_ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)


class ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef(
    _ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef
):
    """
    Type definition for `ListTerminologiesPaginateResponseTerminologyPropertiesList` `EncryptionKey`

    The encryption key for the custom terminology.

    - **Type** *(string) --*

      The type of encryption key used by Amazon Translate to encrypt custom terminologies.

    - **Id** *(string) --*

      The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
      terminology.
    """


_ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ListTerminologiesPaginateResponseTerminologyPropertiesListEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)


class ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef(
    _ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef
):
    """
    Type definition for `ListTerminologiesPaginateResponse` `TerminologyPropertiesList`

    The properties of the custom terminology.

    - **Name** *(string) --*

      The name of the custom terminology.

    - **Description** *(string) --*

      The description of the custom terminology properties.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the custom terminology.

    - **SourceLanguageCode** *(string) --*

      The language code for the source text of the translation request for which the custom
      terminology is being used.

    - **TargetLanguageCodes** *(list) --*

      The language codes for the target languages available with the custom terminology file.
      All possible target languages are returned in array.

      - *(string) --*

    - **EncryptionKey** *(dict) --*

      The encryption key for the custom terminology.

      - **Type** *(string) --*

        The type of encryption key used by Amazon Translate to encrypt custom terminologies.

      - **Id** *(string) --*

        The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
        terminology.

    - **SizeBytes** *(integer) --*

      The size of the file used when importing a custom terminology.

    - **TermCount** *(integer) --*

      The number of terms included in the custom terminology.

    - **CreatedAt** *(datetime) --*

      The time at which the custom terminology was created, based on the timestamp.

    - **LastUpdatedAt** *(datetime) --*

      The time at which the custom terminology was last update, based on the timestamp.
    """


_ListTerminologiesPaginateResponseTypeDef = TypedDict(
    "_ListTerminologiesPaginateResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ListTerminologiesPaginateResponseTerminologyPropertiesListTypeDef
        ]
    },
    total=False,
)


class ListTerminologiesPaginateResponseTypeDef(
    _ListTerminologiesPaginateResponseTypeDef
):
    """
    Type definition for `ListTerminologiesPaginate` `Response`

    - **TerminologyPropertiesList** *(list) --*

      The properties list of the custom terminologies returned on the list request.

      - *(dict) --*

        The properties of the custom terminology.

        - **Name** *(string) --*

          The name of the custom terminology.

        - **Description** *(string) --*

          The description of the custom terminology properties.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the custom terminology.

        - **SourceLanguageCode** *(string) --*

          The language code for the source text of the translation request for which the custom
          terminology is being used.

        - **TargetLanguageCodes** *(list) --*

          The language codes for the target languages available with the custom terminology file.
          All possible target languages are returned in array.

          - *(string) --*

        - **EncryptionKey** *(dict) --*

          The encryption key for the custom terminology.

          - **Type** *(string) --*

            The type of encryption key used by Amazon Translate to encrypt custom terminologies.

          - **Id** *(string) --*

            The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom
            terminology.

        - **SizeBytes** *(integer) --*

          The size of the file used when importing a custom terminology.

        - **TermCount** *(integer) --*

          The number of terms included in the custom terminology.

        - **CreatedAt** *(datetime) --*

          The time at which the custom terminology was created, based on the timestamp.

        - **LastUpdatedAt** *(datetime) --*

          The time at which the custom terminology was last update, based on the timestamp.
    """
